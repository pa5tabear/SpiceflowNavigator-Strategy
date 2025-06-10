# Energy Podcast Test Data Requirements

## Purpose
Test transcripts for SpiceflowNavigator-Strategy analysis validation and demonstration.

## Required Test Transcripts

| # | Podcast & Episode | URL | Output File | Test Focus |
|---|---|---|---|---|
| 1 | Volts - "What's up with clean-energy supply chains and global trade?" | [volts.wtf](https://www.volts.wtf/p/whats-up-with-clean-energy-supply) | `volts_supply_chains.txt` | Supply-chain policy terms |
| 2 | Catalyst - "The case for colocating data centers and generation" | [latitudemedia.com](https://www.latitudemedia.com/podcast/the-case-for-colocating-data-centers-and-generation) | `catalyst_data_centers.txt` | Tech/finance buzzwords |
| 3 | Catalyst - "FOAK tales – lessons on financing first-of-a-kind projects" | [latitudemedia.com](https://www.latitudemedia.com/podcast/foak-tales-lessons-on-financing-first-of-a-kind-projects) | `catalyst_foak_financing.txt` | Project finance jargon |
| 4 | Columbia Energy Exchange - "America's Energy Priorities Reconsidered" | [energypolicy.columbia.edu](https://www.energypolicy.columbia.edu/podcast/americas-energy-priorities-reconsidered) | `columbia_energy_priorities.txt` | Policy/LNG/trade terms |
| 5 | Cleaning Up - "A Clean Energy Playbook for the Global South" | [simplecast.com](https://cleaning-up-leadership-in-the-age-of-climate-change.simplecast.com) | `cleaning_up_global_south.txt` | Emerging market finance |

## Implementation Requirements

### Data Collection Script
```bash
# Engineering task for Codex
python scripts/util/download_transcript.py \
  --url "<source_url>" \
  --outfile "data/raw_podcasts/<filename>.txt"
```

### Content Processing
- Strip HTML tags and extract plain text
- Preserve paragraph structure
- Minimum 5,000 words per transcript
- UTF-8 encoding

### Validation Criteria
- All 5 transcripts collected successfully
- Files readable by StrategicAnalyzer
- Content suitable for goal-based scoring tests
- No copyright violations (all sources are publicly accessible)

## Test Value
- **Format Variety**: Monologue, interview, panel discussions
- **Content Currency**: 2025 content with modern terminology  
- **Geographic Scope**: US, global, emerging markets
- **Domain Coverage**: Policy, finance, technology, supply chains

## Next Steps
This specification should be implemented as part of Sprint 2 or Sprint 3 by the engineering team (Codex) to provide test data for Goal-Based Analysis validation. 