import { h, render } from 'https://esm.sh/preact@10.19.6';
import htm from 'https://esm.sh/htm@3.1.1';
import { signal } from 'https://esm.sh/@preact/signals@1.2.2?deps=preact@10.19.6';

const html = htm.bind(h);

const app = html`
<div style="
  display: flex;
  justify-content: center;
">

<div >
  <h1>ghdownload</h1>

  <div class="card" style="padding: 2rem;">
    <p>A cli cmnd to download your github repo</p>
    <div style="margin-top: 2rem;">
      <p>To install, run the following command:</p>
      <pre style="background: #f4f4f4; padding: 1rem; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; overflow-x: auto;"><code>pip install ghdownload</code>
        <button aria-label="Copy to clipboard" onclick=${(e) => { e.preventDefault(); navigator.clipboard.writeText('pip install ghdownload'); }} style="background: transparent; border: none; outline: none; cursor: pointer; padding: 0.4rem; display: flex; align-items: center; color: inherit;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
        </button>
      </pre>
    </div>
    <p style="margin-top: 1rem;">
      Please get a classic token (auth scope being 'repo') here: 
      <a href="https://github.com/settings/tokens" target="_blank" rel="noopener">https://github.com/settings/tokens</a>
    </p>
    <p style="margin-top: 2rem; font-size: 0.9em; color: #666;">
      Creator: <a href="mailto:rhithesh1947@gmail.com">rhithesh1947@gmail.com</a>
    </p>
  </div>
  </div>
  </div>
`;

render(app, document.getElementById("app"));