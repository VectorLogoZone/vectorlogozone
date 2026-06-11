import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.join(__dirname, '..');

const srcDir = path.join(repoRoot, 'src/content/logos');
const destDir = path.join(repoRoot, 'public/logos');

// Recursively copy image files from src/content/logos to public/logos
function copyLogos(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const files = fs.readdirSync(src);
  files.forEach((file) => {
    const srcPath = path.join(src, file);
    const destPath = path.join(dest, file);
    const stat = fs.statSync(srcPath);

    if (stat.isDirectory()) {
      copyLogos(srcPath, destPath);
    } else if (file.match(/\.(svg|png)$/i)) {
      // Only copy image files, skip index.md
      fs.copyFileSync(srcPath, destPath);
    }
  });
}

copyLogos(srcDir, destDir);
console.log('Logos copied from src/content/logos to public/logos');
