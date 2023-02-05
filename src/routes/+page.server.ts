// import { POLYGON_API_KEY } from '$env/static/private';
// import { writeFile } from 'node:fs/promises';
// import { resolve } from 'node:path';
// import { fileURLToPath } from 'url';
// import { dirname } from 'path';

// const __dirname = dirname(fileURLToPath(import.meta.url));

export async function load({fetch}) {
  // const res = await fetch(`https://api.polygon.io/v3/reference/tickers?active=true&apiKey=${POLYGON_API_KEY}`);
  // const tickers = await res.json();

  // const filepath = resolve(__dirname, 'ticker.json');
  // await writeFile(filepath, JSON.stringify(tickers, null, 4));

  return null;
} 
