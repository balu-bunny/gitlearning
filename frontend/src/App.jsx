import React, { useState } from 'react'

const API = 'http://localhost:8000'

export default function App() {
  const [objectName, setObjectName] = useState('Account')
  const [fieldJson, setFieldJson] = useState('[{"name":"name","type":"text","required":true}]')
  const [layoutJson, setLayoutJson] = useState('{"sections":[{"title":"Main","fields":["name"]}]}')
  const [pageJson, setPageJson] = useState('{"type":"page","children":[{"type":"section","title":"Main","children":[{"type":"field","name":"name"}]}]}')
  const [log, setLog] = useState('')

  async function createObject() {
    const fields = JSON.parse(fieldJson)
    const res = await fetch(`${API}/objects`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: objectName, label: objectName, fields })
    })
    setLog(JSON.stringify(await res.json(), null, 2))
  }

  async function saveLayout() {
    const layout = JSON.parse(layoutJson)
    console.log('Saving layout:', { objectName, layout })
    const res = await fetch(`${API}/objects/${objectName}/layouts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ object_name: objectName, layout })
    })
    setLog(JSON.stringify(await res.json(), null, 2))
  }

  async function savePage() {
    const page = JSON.parse(pageJson)
    const res = await fetch(`${API}/pages`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: `${objectName}Page`, page })
    })
    setLog(JSON.stringify(await res.json(), null, 2))
  }

  return (
    <div className="app">
      <header>
        <h1>Platform Builder</h1>
        <p>Define objects, layouts, automations, and UI pages.</p>
      </header>

      <section>
        <h2>Object</h2>
        <label>Object Name</label>
        <input value={objectName} onChange={e => setObjectName(e.target.value)} />
        <label>Fields (JSON)</label>
        <textarea value={fieldJson} onChange={e => setFieldJson(e.target.value)} />
        <button onClick={createObject}>Create Object</button>
      </section>

      <section>
        <h2>Layout</h2>
        <label>Layout (JSON)</label>
        <textarea value={layoutJson} onChange={e => setLayoutJson(e.target.value)} />
        <button onClick={saveLayout}>Save Layout</button>
      </section>

      <section>
        <h2>UI Builder Page</h2>
        <label>Page (JSON)</label>
        <textarea value={pageJson} onChange={e => setPageJson(e.target.value)} />
        <button onClick={savePage}>Save Page</button>
      </section>

      <section>
        <h2>Output</h2>
        <pre>{log}</pre>
      </section>
    </div>
  )
}
