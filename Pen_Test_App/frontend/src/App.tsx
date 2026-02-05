import { useState, useEffect } from 'react'
import './index.css'

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
}

interface SearchResult {
  id: number;
  title: string;
  description: string;
  categories: string[];
  platforms: string[];
  snippet_content: string;
  rank: number;
}

function App() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<SearchResult[]>([])
  const [loading, setLoading] = useState(false)

  // Modal State
  const [selectedId, setSelectedId] = useState<number | null>(null)
  const [detailData, setDetailData] = useState<TechniqueDetail | null>(null)
  const [detailLoading, setDetailLoading] = useState(false)

  const fetchResults = async (q: string) => {
    setLoading(true)
    try {
      // Use relative path - Nginx proxies /api to backend:8000
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

  // Fetch initial data (all records)
  useEffect(() => {
    fetchResults('')
  }, [])

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    fetchResults(query)
  }

  // Fetch details when a row is clicked
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

  return (
    <div className="min-h-screen bg-slate-900 text-slate-200 font-sans p-4">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center text-blue-400">Pen Test Database</h1>

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
                <th className="p-4 border-b border-slate-700 w-1/3">Snippet / Desc</th>
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
                    <div
                      dangerouslySetInnerHTML={{ __html: r.snippet_content || '' }}
                      className="line-clamp-2"
                    />
                  </td>
                </tr>
              ))}
              {results.length === 0 && !loading && (
                <tr>
                  <td colSpan={4} className="p-8 text-center text-slate-500">No results found</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Detail Modal */}
      {selectedId !== null && (
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
                    <p className="text-slate-400 leading-relaxed whitespace-pre-wrap">{detailData.description}</p>
                  </div>

                  {detailData.snippets.length > 0 ? (
                    <div>
                      <h3 className="text-lg font-semibold text-slate-300 mb-4">Code Snippets</h3>
                      <div className="space-y-6">
                        {detailData.snippets.map((snip, i) => (
                          <div key={i} className="relative group">
                            <div className="absolute top-0 right-0 p-2 text-xs text-slate-500 font-mono uppercase bg-slate-800 rounded-bl">{snip.language || 'text'}</div>
                            <pre className="bg-black p-4 rounded-lg overflow-x-auto border border-slate-800 text-sm text-green-400 font-mono shadow-inner">
                              <code>{snip.content}</code>
                            </pre>
                          </div>
                        ))}
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
      )}
    </div>
  )
}

export default App
