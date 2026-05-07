import { h, render } from 'https://esm.sh/preact@10.19.6';
import htm from 'https://esm.sh/htm@3.1.1';

const html = htm.bind(h);

// Force light mode
document.documentElement.style.colorScheme = 'light';
document.body.style.margin = '0';
document.body.style.background = '#ffffff';
document.body.style.color = '#000000';
document.body.style.fontFamily = 'Arial, sans-serif';

const copyCommand = () => {
  navigator.clipboard.writeText('pip install gh-download-cli');
};

const app = html`
<div
  style="
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: white;
    color: black;
    padding: 2rem;
    box-sizing: border-box;
  "
>
  <div style="max-width: 700px; width: 100%;">
    <h1 style="margin-bottom: 1rem;">ghdownload</h1>

    <div
      class="card"
      style="
        padding: 2rem;
        border: 1px solid #ddd;
        border-radius: 12px;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
      "
    >
      <p>A CLI command to download your GitHub repo.</p>

      <div style="margin-top: 2rem;">
        <p>To install, run the following command:</p>

        <pre
          style="
            background: #f4f4f4;
            color: black;
            padding: 1rem;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            overflow-x: auto;
            gap: 1rem;
          "
        >
<code>pip install gh-download-cli</code>

<button
  aria-label="Copy to clipboard"
  onClick=${copyCommand}
  style="
    background: white;
    border: 1px solid #ccc;
    border-radius: 6px;
    cursor: pointer;
    padding: 0.5rem;
    display: flex;
    align-items: center;
    color: black;
  "
>
  <svg
    width="16"
    height="16"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
  </svg>
</button>
        </pre>
      </div>

      <p style="margin-top: 1.5rem; line-height: 1.6;">
        Please get a classic token (auth scope being 'repo') here:
        <br />
        <a
          href="https://github.com/settings/tokens"
          target="_blank"
          rel="noopener"
          style="color: #2563eb;"
        >
          https://github.com/settings/tokens
        </a>
      </p>

      <p
        style="
          margin-top: 2rem;
          font-size: 0.9rem;
          color: #666;
        "
      >
        Creator:
        <a
          href="mailto:rhithesh1947@gmail.com"
          style="color: #2563eb;"
        >
          rhithesh1947@gmail.com
        </a>
      </p>
    </div>
  </div>
</div>
`;

render(app, document.getElementById('app'));