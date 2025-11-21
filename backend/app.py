from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from processor import read_and_extract, aggregate_by_date_type

UPLOAD_DIR = Path('/app/uploads')
OUTPUT_DIR = Path('/app/output')
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    results = []
    for f in files:
        filename = f.filename
        path = UPLOAD_DIR / filename
        f.save(path)
        proc = read_and_extract(path)
        type_name = Path(filename).stem
        summary = aggregate_by_date_type(proc, type_name)
        proc.to_csv(OUTPUT_DIR / f'processed_{type_name}.csv', index=False)
        summary.to_csv(OUTPUT_DIR / f'summary_{type_name}.csv', index=False)
        results.append({'file': filename, 'rows': len(proc), 'dates_parsed': int(proc['date'].notna().sum())})
    return jsonify({'processed': results})

@app.route('/list_outputs')
def list_outputs():
    files = [p.name for p in OUTPUT_DIR.glob('*.csv')]
    return jsonify(files)

@app.route('/outputs/<path:fname>')
def outputs(fname):
    return send_from_directory(OUTPUT_DIR, fname, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
