.PHONY: capture-source capture-public

capture-source:
	python3 scripts/capture_codex_session.py

capture-public:
	python3 scripts/capture_codex_session.py --public
