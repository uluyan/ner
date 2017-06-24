# ner

## Files
```
├── data
├── lib
│   ├── cut.py
│   ├── education.py
│   ├── hometown.py
│   ├── __init__.py
│   ├── Items.py
│   ├── title.py
│   ├── utils.py
├── ner.py
└── tools
    ├── format.py
    ├── formatText.js
    ├── posseg.py
    ├── pre.py
    ├── show.py
    ├── view.py
    ├── x2csv.py
    └── xml_parser.py
```

## Dependency

- python modules
 - jieba

## Start
- 预处理
  - 简历放在data/resumes目录下
  - `python lib/pre.py data/resumes`
- 实体识别 `./ner.py`