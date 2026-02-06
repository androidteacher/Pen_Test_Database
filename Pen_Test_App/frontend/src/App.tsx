import { useState, useEffect } from 'react'
import './index.css'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

interface Snippet {
  language: string;
  content: string;
}

interface TechniqueDetail {
  id: number;
  title: string;
  description: string;
  categories: string[];
  platforms: string[];
  technologies: string[];
  snippets: Snippet[];
  category_ids?: number[]; // Added for edit mapping
  platform_ids?: number[]; // Added for edit mapping
}

interface SearchResult {
  id: number;
  title: string;
  description: string;
  categories: string[];
  platforms: string[];
  snippet_content: string;
  summary?: string;
  rank: number;
}

interface MetaItem {
  id: number;
  name: string;
}

function App() {
  // Navigation State
  const [view, setView] = useState<'home' | 'login' | 'admin' | 'create'>('home')
  const [token, setToken] = useState<string | null>(localStorage.getItem('token'))

  // Search State
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<SearchResult[]>([])
  const [loading, setLoading] = useState(false)

  // Modal State
  const [selectedId, setSelectedId] = useState<number | null>(null)
  const [detailData, setDetailData] = useState<TechniqueDetail | null>(null)
  const [detailLoading, setDetailLoading] = useState(false)

  // Login State
  const [username, setUsername] = useState('admin')
  const [password, setPassword] = useState('admin')
  const [loginError, setLoginError] = useState('')

  // Admin State
  const [restoreStatus, setRestoreStatus] = useState('')
  const [uploadFile, setUploadFile] = useState<File | null>(null)

  // Create/Edit State
  const [editId, setEditId] = useState<number | null>(null)
  const [categories, setCategories] = useState<MetaItem[]>([])
  const [platforms, setPlatforms] = useState<MetaItem[]>([])
  const [createForm, setCreateForm] = useState({
    title: '',
    summary: '', // Purpose
    description: '', // Sub-page Markdown
    category_ids: [] as number[],
    platform_ids: [] as number[]
  })
  const [createStatus, setCreateStatus] = useState('')


  // --- Auth Logic ---
  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoginError('')
    try {
      const formData = new FormData()
      formData.append('username', username)
      formData.append('password', password)

      const res = await fetch('/api/auth/login', {
        method: 'POST',
        body: formData,
      })

      if (!res.ok) {
        throw new Error('Login failed')
      }

      const data = await res.json()
      localStorage.setItem('token', data.access_token)
      setToken(data.access_token)
      setView('admin')
    } catch (err) {
      setLoginError('Invalid credentials')
    }
  }

  const logout = () => {
    localStorage.removeItem('token')
    setToken(null)
    setView('home')
  }

  // --- Admin Logic ---
  const handleBackup = async () => {
    try {
      const res = await fetch('/api/admin/backup', {
        headers: { Authorization: `Bearer ${token}` }
      })
      if (!res.ok) throw new Error('Backup failed')

      const blob = await res.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `pen_test_backup_${new Date().toISOString().slice(0, 10)}.db`
      document.body.appendChild(a)
      a.click()
      a.remove()
    } catch (err) {
      alert('Backup failed')
    }
  }

  const handleRestore = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!uploadFile) return

    const formData = new FormData()
    formData.append('file', uploadFile)

    try {
      setRestoreStatus('Restoring...')
      const res = await fetch('/api/admin/restore', {
        method: 'POST',
        headers: { Authorization: `Bearer ${token}` },
        body: formData
      })

      if (!res.ok) throw new Error('Restore failed')

      setRestoreStatus('Database restored successfully!')
      // Refresh data if needed, or just warn user
    } catch (err) {
      setRestoreStatus('Restore failed.')
    }
  }

  // --- Create/Edit Logic ---
  useEffect(() => {
    if (view === 'create') {
      const fetchMeta = async () => {
        try {
          const [catRes, platRes] = await Promise.all([
            fetch('/api/meta/categories'),
            fetch('/api/meta/platforms')
          ]);
          const cats = await catRes.json();
          const plats = await platRes.json();
          setCategories(cats);
          setPlatforms(plats);

          // If Editing, pre-fill form
          if (editId) {
            const res = await fetch(`/api/technique/${editId}`);
            const data = await res.json();

            // Need to map names back to IDs which is tricky if API doesn't return joined IDs
            // For now, let's assume we can match by name or fetch raw tags.
            // BETTER APPROACH: Update GET /technique/{id} to return IDs or do it client side
            // For simplicity: Map names to IDs
            const cIds = data.categories.map((cName: string) => cats.find((c: MetaItem) => c.name === cName)?.id).filter(Boolean);
            const pIds = data.platforms.map((pName: string) => plats.find((p: MetaItem) => p.name === pName)?.id).filter(Boolean);

            setCreateForm({
              title: data.title,
              summary: data.summary || '', // API might verify returning summary, currently it does
              description: data.description || '',
              category_ids: cIds,
              platform_ids: pIds
            });
          } else {
            // Reset form for create
            setCreateForm({
              title: '', summary: '', description: '', category_ids: [], platform_ids: []
            });
          }
        } catch (e) { console.error("Failed to load meta or technique", e); }
      }
      fetchMeta();
    }
  }, [view, editId]);

  const handleCreateSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setCreateStatus(editId ? 'Updating...' : 'Creating...');
    const url = editId ? `/api/technique/${editId}` : '/api/technique';
    const method = editId ? 'PUT' : 'POST';

    try {
      const res = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(createForm)
      });
      if (!res.ok) throw new Error("Operation failed");
      setCreateStatus(editId ? 'Technique updated successfully!' : 'Technique created successfully!');

      if (!editId) {
        setCreateForm({
          title: '', summary: '', description: '', category_ids: [], platform_ids: []
        });
      }
      setTimeout(() => setCreateStatus(''), 3000);
    } catch (err) {
      setCreateStatus('Error saving technique.');
    }
  }

  const handleEditInit = (id: number) => {
    setEditId(id);
    setView('create');
  }

  const handleDelete = async (e: React.MouseEvent, id: number) => {
    e.stopPropagation(); // prevent row click
    if (!window.confirm("Are you sure you want to delete this entry?")) return;

    try {
      const res = await fetch(`/api/technique/${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) throw new Error("Delete failed");

      // Refresh results
      fetchResults(query);
    } catch (err) {
      alert("Failed to delete technique");
    }
  }

  const toggleSelection = (id: number, field: 'category_ids' | 'platform_ids') => {
    setCreateForm(prev => {
      const list = prev[field];
      if (list.includes(id)) {
        return { ...prev, [field]: list.filter(x => x !== id) };
      } else {
        return { ...prev, [field]: [...list, id] };
      }
    });
  }


  // --- Search Logic ---
  const fetchResults = async (q: string) => {
    setLoading(true)
    try {
      const url = `/api/search?limit=200&q=${encodeURIComponent(q)}`
      const res = await fetch(url)
      const data = await res.json()
      setResults(data)
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  // Fetch initial data
  useEffect(() => {
    if (view === 'home') {
      fetchResults('')
    }
  }, [view])

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    fetchResults(query)
  }

  // Fetch details
  useEffect(() => {
    if (selectedId !== null) {
      setDetailLoading(true)
      fetch(`/api/technique/${selectedId}`)
        .then(res => res.json())
        .then(data => setDetailData(data))
        .catch(console.error)
        .finally(() => setDetailLoading(false))
    } else {
      setDetailData(null)
    }
  }, [selectedId])

  const closeModal = () => setSelectedId(null)

  // --- Renders ---

  return (
    <div className="min-h-screen bg-slate-900 text-slate-200 font-sans p-4">
      <div className="max-w-7xl mx-auto">

        {/* Header / Nav */}
        <div className="flex justify-between items-center mb-8 border-b border-slate-800 pb-4">
          <h1 className="text-3xl font-bold text-blue-400 cursor-pointer" onClick={() => { setView('home'); setEditId(null); }}>
            Pen Test Database
          </h1>
          <div>
            {token ? (
              <div className="flex gap-4 items-center">
                <button
                  onClick={() => { setEditId(null); setView('create'); }}
                  className={`text-slate-300 hover:text-white ${view === 'create' ? 'font-bold text-blue-300' : ''}`}
                >
                  New Entry
                </button>
                <button
                  onClick={() => setView('admin')}
                  className={`text-slate-300 hover:text-white ${view === 'admin' ? 'font-bold text-blue-300' : ''}`}
                >
                  Admin Panel
                </button>
                <button
                  onClick={logout}
                  className="text-red-400 hover:text-red-300 text-sm border border-red-900/50 px-3 py-1 rounded"
                >
                  Logout
                </button>
              </div>
            ) : (
              view !== 'login' && (
                <button
                  onClick={() => setView('login')}
                  className="text-slate-300 hover:text-white font-semibold"
                >
                  Login
                </button>
              )
            )}
          </div>
        </div>

        {/* Views */}

        {view === 'login' && (
          <div className="max-w-md mx-auto mt-20 p-8 bg-slate-800 rounded-lg shadow-xl border border-slate-700">
            <h2 className="text-2xl font-bold mb-6 text-center text-white">Admin Login</h2>
            <form onSubmit={handleLogin} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-slate-400 mb-1">Username</label>
                <input
                  type="text"
                  value={username}
                  onChange={e => setUsername(e.target.value)}
                  className="w-full p-2 rounded bg-slate-900 border border-slate-600 focus:border-blue-500 outline-none text-white"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-400 mb-1">Password</label>
                <input
                  type="password"
                  value={password}
                  onChange={e => setPassword(e.target.value)}
                  className="w-full p-2 rounded bg-slate-900 border border-slate-600 focus:border-blue-500 outline-none text-white"
                />
              </div>
              {loginError && <p className="text-red-400 text-sm text-center">{loginError}</p>}
              <button
                type="submit"
                className="w-full py-2 bg-blue-600 hover:bg-blue-700 rounded font-bold text-white transition-colors"
              >
                Sign In
              </button>
              <div className="text-center mt-4">
                <button type="button" onClick={() => setView('home')} className="text-slate-500 hover:text-slate-300 text-sm">Cancel</button>
              </div>
            </form>
          </div>
        )}

        {view === 'admin' && (
          <div className="max-w-4xl mx-auto space-y-8">
            <h2 className="text-2xl font-bold text-slate-200">System Administration</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {/* Backup Card */}
              <div className="bg-slate-800 p-6 rounded-lg border border-slate-700">
                <h3 className="text-xl font-semibold mb-4 text-green-400">Database Backup</h3>
                <p className="text-slate-400 mb-6 text-sm">Download a full snapshot of the current <code>pen_test.db</code> database (SQLite).</p>
                <button
                  onClick={handleBackup}
                  className="w-full py-3 bg-green-700 hover:bg-green-600 rounded font-bold transition-colors flex items-center justify-center gap-2"
                >
                  <span>Download Backup (.db)</span>
                </button>
              </div>

              {/* Restore Card */}
              <div className="bg-slate-800 p-6 rounded-lg border border-slate-700">
                <h3 className="text-xl font-semibold mb-4 text-orange-400">Restore Database</h3>
                <p className="text-slate-400 mb-4 text-sm">Upload a previously backed-up <code>.db</code> file. <br /><strong className="text-red-400">Warning: This will overwrite the current database immediately.</strong></p>

                <form onSubmit={handleRestore} className="space-y-4">
                  <input
                    type="file"
                    onChange={e => setUploadFile(e.target.files ? e.target.files[0] : null)}
                    className="block w-full text-sm text-slate-400
                      file:mr-4 file:py-2 file:px-4
                      file:rounded-full file:border-0
                      file:text-sm file:font-semibold
                      file:bg-slate-700 file:text-blue-300
                      hover:file:bg-slate-600
                    "
                  />
                  <button
                    type="submit"
                    disabled={!uploadFile}
                    className="w-full py-3 bg-orange-700 hover:bg-orange-600 disabled:opacity-50 disabled:cursor-not-allowed rounded font-bold transition-colors"
                  >
                    Restore
                  </button>
                  {restoreStatus && <p className="text-center text-sm font-mono text-yellow-300">{restoreStatus}</p>}
                </form>
              </div>
            </div>
          </div>
        )}

        {view === 'create' && (
          <div className="max-w-4xl mx-auto bg-slate-800 p-8 rounded-lg border border-slate-700 shadow-xl">
            <h2 className="text-2xl font-bold mb-8 text-blue-400">{editId ? 'Edit Entry' : 'Create New Entry'}</h2>
            <form onSubmit={handleCreateSubmit} className="space-y-6">

              {/* Vector */}
              <div>
                <label className="block text-sm font-bold text-slate-300 mb-2">Vector (Title)</label>
                <input
                  type="text"
                  className="w-full p-3 bg-slate-900 border border-slate-600 rounded focus:border-blue-500 outline-none"
                  placeholder="e.g. Blind SQL Injection"
                  value={createForm.title}
                  onChange={e => setCreateForm({ ...createForm, title: e.target.value })}
                  required
                />
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Categories */}
                <div>
                  <label className="block text-sm font-bold text-slate-300 mb-2">Security Domains</label>
                  <div className="max-h-40 overflow-y-auto bg-slate-900 border border-slate-600 rounded p-2 space-y-1">
                    {categories.map(c => (
                      <label key={c.id} className="flex items-center space-x-2 text-sm text-slate-300 cursor-pointer hover:bg-slate-800 p-1 rounded">
                        <input
                          type="checkbox"
                          checked={createForm.category_ids.includes(c.id)}
                          onChange={() => toggleSelection(c.id, 'category_ids')}
                          className="form-checkbox text-blue-500 rounded bg-slate-800 border-slate-600"
                        />
                        <span>{c.name}</span>
                      </label>
                    ))}
                  </div>
                </div>

                {/* Platforms */}
                <div>
                  <label className="block text-sm font-bold text-slate-300 mb-2">OS / Platform</label>
                  <div className="max-h-40 overflow-y-auto bg-slate-900 border border-slate-600 rounded p-2 space-y-1">
                    {platforms.map(p => (
                      <label key={p.id} className="flex items-center space-x-2 text-sm text-slate-300 cursor-pointer hover:bg-slate-800 p-1 rounded">
                        <input
                          type="checkbox"
                          checked={createForm.platform_ids.includes(p.id)}
                          onChange={() => toggleSelection(p.id, 'platform_ids')}
                          className="form-checkbox text-blue-500 rounded bg-slate-800 border-slate-600"
                        />
                        <span>{p.name}</span>
                      </label>
                    ))}
                  </div>
                </div>
              </div>

              {/* Purpose */}
              <div>
                <label className="block text-sm font-bold text-slate-300 mb-2">Purpose (Summary)</label>
                <input
                  type="text"
                  className="w-full p-3 bg-slate-900 border border-slate-600 rounded focus:border-blue-500 outline-none"
                  placeholder="Brief description of the technique..."
                  value={createForm.summary}
                  onChange={e => setCreateForm({ ...createForm, summary: e.target.value })}
                />
              </div>

              {/* Sub-page */}
              <div>
                <label className="block text-sm font-bold text-slate-300 mb-2">Sub-page Content (Markdown)</label>
                <p className="text-xs text-slate-500 mb-2">This content will be rendered when the user clicks the row.</p>
                <textarea
                  className="w-full h-64 p-3 bg-black border border-slate-700 rounded focus:border-blue-500 outline-none font-mono text-sm text-green-400"
                  placeholder="# Detailed Explanation\n\n- Step 1\n- Step 2\n\n```python\nprint('hello')\n```"
                  value={createForm.description}
                  onChange={e => setCreateForm({ ...createForm, description: e.target.value })}
                />
              </div>

              <div className="flex gap-4">
                <button
                  type="submit"
                  className="flex-1 py-4 bg-blue-600 hover:bg-blue-700 rounded font-bold text-lg transition-colors"
                >
                  {editId ? 'Update Entry' : 'Create Entry'}
                </button>
                {editId && (
                  <button
                    type="button"
                    onClick={() => { setEditId(null); setView('home'); }}
                    className="px-6 py-4 bg-slate-700 hover:bg-slate-600 rounded font-bold text-lg transition-colors"
                  >
                    Cancel
                  </button>
                )}
              </div>

              {createStatus && <p className="text-center font-bold text-green-400 mt-4">{createStatus}</p>}

            </form>
          </div>
        )}

        {view === 'home' && (
          <>
            <form onSubmit={handleSearch} className="mb-8 flex gap-4">
              <input
                type="text"
                className="flex-1 p-4 rounded-lg bg-slate-800 border border-slate-700 focus:outline-none focus:border-blue-500 text-lg"
                placeholder="Search filters..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
              <button
                type="submit"
                className="px-8 py-4 bg-blue-600 hover:bg-blue-700 rounded-lg font-bold transition-colors"
                disabled={loading}
              >
                {loading ? '...' : 'Refine'}
              </button>
            </form>

            <div className="overflow-x-auto rounded-lg border border-slate-700">
              <table className="w-full text-left bg-slate-800">
                <thead className="bg-slate-950 text-slate-400 uppercase text-sm font-semibold">
                  <tr>
                    <th className="p-4 border-b border-slate-700">Vector</th>
                    <th className="p-4 border-b border-slate-700">Security Domains</th>
                    <th className="p-4 border-b border-slate-700">OS</th>
                    <th className="p-4 border-b border-slate-700 w-1/3">Purpose</th>
                    {token && <th className="p-4 border-b border-slate-700">Actions</th>}
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-700">
                  {results.map((r) => (
                    <tr
                      key={r.id}
                      onClick={() => setSelectedId(r.id)}
                      className="hover:bg-slate-700 cursor-pointer transition-colors group"
                    >
                      <td className="p-4 font-medium text-blue-300 group-hover:text-blue-200">{r.title}</td>
                      <td className="p-4">
                        <div className="flex flex-wrap gap-2">
                          {r.categories.map((c, i) => (
                            <span key={i} className="bg-slate-900 text-xs px-2 py-1 rounded border border-slate-600">
                              {c}
                            </span>
                          ))}
                        </div>
                      </td>
                      <td className="p-4 text-slate-400">
                        {r.platforms.join(', ')}
                      </td>
                      <td className="p-4 text-sm text-slate-500">
                        <div className="line-clamp-2">
                          {r.summary || r.description}
                        </div>
                      </td>
                      {token && (
                        <td className="p-4">
                          <div className="flex gap-2">
                            <button
                              onClick={(e) => { e.stopPropagation(); handleEditInit(r.id); }}
                              className="px-3 py-1 bg-blue-600/20 hover:bg-blue-600/40 text-blue-400 rounded text-sm font-medium border border-blue-600/50"
                            >
                              Edit
                            </button>
                            <button
                              onClick={(e) => handleDelete(e, r.id)}
                              className="px-3 py-1 bg-red-600/20 hover:bg-red-600/40 text-red-400 rounded text-sm font-medium border border-red-600/50"
                            >
                              Delete
                            </button>
                          </div>
                        </td>
                      )}
                    </tr>
                  ))}
                  {results.length === 0 && !loading && (
                    <tr>
                      <td colSpan={token ? 5 : 4} className="p-8 text-center text-slate-500">No results found</td>
                    </tr>
                  )}
                </tbody>
              </table >
            </div >
          </>
        )}
      </div>

      {/* Detail Modal */}
      {
        selectedId !== null && (
          <div className="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50 animate-fade-in" onClick={closeModal}>
            <div
              className="bg-slate-900 w-full max-w-4xl max-h-[90vh] rounded-xl border border-slate-700 shadow-2xl overflow-hidden flex flex-col"
              onClick={e => e.stopPropagation()}
            >
              {detailLoading || !detailData ? (
                <div className="p-12 text-center text-slate-500">Loading details...</div>
              ) : (
                <>
                  <div className="p-6 border-b border-slate-800 bg-slate-950 flex justify-between items-start">
                    <div>
                      <h2 className="text-2xl font-bold text-blue-400">{detailData.title}</h2>
                      <div className="flex gap-2 mt-2">
                        {detailData.categories.map((c, i) => <span key={i} className="text-xs bg-slate-800 px-2 py-1 rounded text-slate-300">{c}</span>)}
                        {detailData.platforms.map((p, i) => <span key={i} className="text-xs bg-indigo-900/50 px-2 py-1 rounded text-indigo-200">{p}</span>)}
                      </div>
                    </div>
                    <button onClick={closeModal} className="text-slate-500 hover:text-white text-2xl">&times;</button>
                  </div>

                  <div className="p-8 overflow-y-auto space-y-6">
                    <div>
                      <h3 className="text-lg font-semibold text-slate-300 mb-2">Description</h3>
                      {/* Markdown Rendering for Description */}
                      <div className="text-slate-400 leading-relaxed text-sm markdown-body">
                        <ReactMarkdown
                          remarkPlugins={[remarkGfm]}
                          components={{
                            table: (props: any) => <table className="border-collapse w-full text-left" {...props} />,
                            thead: (props: any) => <thead className="bg-slate-950 text-slate-300" {...props} />,
                            tbody: (props: any) => <tbody className="divide-y divide-slate-800" {...props} />,
                            tr: (props: any) => <tr className="hover:bg-slate-800/50" {...props} />,
                            th: (props: any) => <th className="p-3 font-semibold border-b border-slate-700 whitespace-nowrap" {...props} />,
                            td: (props: any) => <td className="p-3 text-slate-400 border-b border-slate-800/50 font-mono text-xs whitespace-pre-wrap" {...props} />,
                            code: (props: any) => <code className="bg-slate-800 px-1 py-0.5 rounded text-blue-300 font-mono" {...props} />
                          }}
                        >
                          {detailData.description}
                        </ReactMarkdown>
                      </div>
                    </div>

                    {detailData.snippets.length > 0 ? (
                      <div>
                        <h3 className="text-lg font-semibold text-slate-300 mb-4">Code Snippets</h3>
                        <div className="space-y-6">
                          {detailData.snippets.map((snip, i) => {
                            const isTable = snip.content.trim().startsWith('|') && (snip.content.includes('---') || snip.content.includes(':---'));

                            return (
                              <div key={i} className="relative group">
                                <div className="absolute top-0 right-0 p-2 text-xs text-slate-500 font-mono uppercase bg-slate-800 rounded-bl">{snip.language || 'text'}</div>
                                {isTable ? (
                                  <div className="bg-slate-900 p-4 rounded-lg overflow-x-auto border border-slate-800 text-sm shadow-inner">
                                    <ReactMarkdown
                                      remarkPlugins={[remarkGfm]}
                                      components={{
                                        table: (props: any) => <table className="border-collapse w-full text-left" {...props} />,
                                        thead: (props: any) => <thead className="bg-slate-950 text-slate-300" {...props} />,
                                        tbody: (props: any) => <tbody className="divide-y divide-slate-800" {...props} />,
                                        tr: (props: any) => <tr className="hover:bg-slate-800/50" {...props} />,
                                        th: (props: any) => <th className="p-3 font-semibold border-b border-slate-700 whitespace-nowrap" {...props} />,
                                        td: (props: any) => <td className="p-3 text-slate-400 border-b border-slate-800/50 font-mono text-xs whitespace-pre-wrap" {...props} />,
                                        code: (props: any) => <code className="bg-slate-800 px-1 py-0.5 rounded text-blue-300 font-mono" {...props} />
                                      }}
                                    >
                                      {snip.content}
                                    </ReactMarkdown>
                                  </div>
                                ) : (
                                  <pre className="bg-black p-4 rounded-lg overflow-x-auto border border-slate-800 text-sm text-green-400 font-mono shadow-inner">
                                    <code>{snip.content}</code>
                                  </pre>
                                )}
                              </div>
                            )
                          })}
                        </div>
                      </div>
                    ) : (
                      <div className="p-8 text-center border-2 border-dashed border-slate-800 rounded-lg">
                        <p className="text-slate-500 italic">No sub page included for this entry</p>
                      </div>
                    )}

                    {detailData.technologies.length > 0 && (
                      <div>
                        <h3 className="text-sm font-semibold text-slate-500 uppercase tracking-wider mb-2">Related Technologies</h3>
                        <div className="flex flex-wrap gap-2">
                          {detailData.technologies.map((t, i) => (
                            <span key={i} className="bg-slate-800 text-slate-300 px-3 py-1 rounded-full text-sm border border-slate-700">
                              {t}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </>
              )}
            </div>
          </div>
        )
      }
    </div >
  )
}

export default App
