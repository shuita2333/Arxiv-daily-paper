# 🔐 大模型安全相关研究 | 2026年07月23日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [HALLMARK: Diagnosing Three Failure Modes in LLM Citation Verifiers](https://arxiv.org/abs/2607.18360)

**<font color=#1a73e8>作者：</font>** Patrik Reizinger, Wieland Brendel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) now routinely draft literature reviews and assist with academic writing, which means a higher risk of fabricated references: GPTZero found 53 papers with hallucinated citations among NeurIPS 2025's accepted set. Rule- and LLM-based verifiers are emerging, but no shared benchmark compares them and gives detailed failure diagnostics. We close that gap with HALLMARK (Hallucination benchmark): 2,526 BibTeX entries spanning 14 hallucination types, three difficulty tiers, six diagnostic sub-tests per entry, and a contamination-resistant held-out split. On it we evaluate a DOI-lookup baseline, frontier LLMs zero-shot, tool-augmented agents, and our own rule-based, co-designed verifier bibtex-updater. Across the benchmark one result is consistent: the false-positive rate, not recall, decides whether a verifier is deployable. HALLMARK makes it concrete through three failure modes: agentic lookups buy recall but inflate false positives; at a venue-realistic base rate, the order-of-magnitude spread in false-positive rates (FPRs) -- not recall -- governs whether a verifier's flags are mostly true catches or mostly noise; and most LLMs over-flag papers published past their training cutoff, where only the two latest-cutoff models hold their false-positive rate near in-distribution levels (a signal we report as descriptive, since it is confounded with possible recall of those entries). Thus FPR is the deployment bottleneck, but an undetected fabrication remains the costlier error for the scientific record.

---


### 2. [ChainMark: Model-Free LLM Watermarking with Closed-Form Calibration](https://arxiv.org/abs/2607.18445)

**<font color=#1a73e8>作者：</font>** Chengheng Li-Chen, Kyuhee Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Regulatory regimes such as the EU AI Act mandate machine-readable marking of synthetic text, but existing watermark detectors rely on the generating LM and on heuristic thresholds with no closed-form calibration. We introduce ChainMark, an active watermark that partitions the vocabulary into S states via keyed SHA-256 and forces a hard Markov transition on a fraction rho of positions; the detector replays the partition from the same key in O(n) hash operations, with no LM access. We derive a closed-form S*(n, rho, alpha) mapping a target FPR, text length, and budget to the minimum state count (Theorem 1), prove a universal robustness threshold delta* = 1 - 1/sqrt(2) approximately 29.3% that is invariant in (S, rho, n) (Theorem 2), and generalise both to any k-regular transition topology (Theorem 3). Across three instruction-tuned LLMs and four domains, ChainMark strictly dominates KGW and SWEET under translation and random-substitution attacks at matched budget; a one-corpus empirical recalibration restores the 1% target FPR on natural-language text.

---


### 3. [Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing](https://arxiv.org/abs/2607.18485)

**<font color=#1a73e8>作者：</font>** Jie Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an agent commonly acts under its user's credentials and inherits the user's access to files and the scheduler. This arrangement creates a failure mode that ordinary account-level controls do not capture. Adversarial instructions in a log, tool description, shared file, or peer-agent message may redirect the agent beyond the task the user assigned, even though every resulting command is authenticated and permitted for that account. We refer to this as the hijacked authorized agent problem. Existing agent-security studies explain relevant mechanisms, such as indirect prompt injection and tool misuse, but generally evaluate them in web, enterprise, or personal-assistant settings. HPC security, by contrast, has mature controls for identity and isolation but does not ordinarily represent the intent of a particular task. This paper defines the threat model in the HPC setting, identifies attack surfaces created by schedulers, shared storage, multi-project accounts, and scientific workflows, and examines where current controls fall short. It concludes with a research agenda and a plan for an empirical benchmark, TaskBound.

---


### 4. [Towards an Automated Test of LLM Security Knowledge](https://arxiv.org/abs/2607.18496)

**<font color=#1a73e8>作者：</font>** Shufan Chai, Liangliang Sun, Jessica Staddon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for a range of software, hardware and human-centered security tasks. Consequently, LLM performance on security tasks is an active area of measurement and research, often with a focus on identifying areas in which LLM security ``knowledge'' may be insufficient. Popular strategies for identifying LLM security knowledge gaps include building corpora of challenge questions or task benchmarks, strategies that require substantial manual work and security expertise to design and execute. We introduce a partially-automated method for assessing LLM knowledge of a security this http URL method uses authoritative information from Consumer Protection Agencies (CPAs) to identify instability in LLM responses that can be indicative of knowledge gaps. We demonstrate the method for 2 security topics, identity theft and impostor scams, and 5 LLMs in 2 leading LLM families, Gemini and GPT, using publicly available information about identity theft and impostor scams from 6 this http URL method distinguishes between models that have and don't have sufficient knowledge to accurately identify the security topics in text narratives.

---


### 5. [CryptanalysisBench: Can LLMs do Cryptanalysis?](https://arxiv.org/abs/2607.18538)

**<font color=#1a73e8>作者：</font>** Lukas Fluri, Avital Shafran, Nicholas Carlini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptanalysis - the task of finding attacks against cryptographic schemes - sits at the intersection of mathematical reasoning and cybersecurity, two areas where LLMs have advanced fastest. Cryptanalysis represents both a clean testbed for frontier reasoning (as practical attacks can be automatically verified) and a domain with unusually high stakes, since the primitives under study underpin our digital security. In this paper we ask whether LLMs can do cryptanalysis, and find that the answer is increasingly yes.
We introduce CryptanalysisBench, 191 tasks across six families of cryptographic primitives (block ciphers, hash functions, etc.) drawn primarily from four NIST standardization competitions. Our benchmark consists of three tiers: (i) primitives with known practical breaks; (ii) primitives with no known practical break, evaluated both at full strength and as scaled-down variants; and (iii) a challenge set of production primitives at the frontier of cryptanalysis.
Five frontier models (Claude Opus 4.8, Sonnet 5, Mythos 5, GPT 5.5, and the open-weights GLM 5.2) break 65%-86% of Tier 1 schemes, 6-12 Tier-2 schemes at full strength, and 24-61 across all scaled-down variants. Beyond deriving known results, models produce novel cryptanalysis, such as a key-recovery attack that exploits a design flaw in the SpoC AEAD and an error in KINDI's published CCA-security proof, both to the best of our knowledge not previously known.
We release CryptanalysisBench as a tool to help track if (or when) AI cryptanalysis becomes a serious factor and as a scaffold for stress-testing candidate schemes before deployment. The attacks that the benchmark already surfaces are an early snapshot of a fast-moving frontier that may soon match, and in places exceed, the published state of the art.

---


### 6. [RECEIPT: Deterministic, Reward-Hacking-Resistant Verification for White-Box Agentic XSS Discovery](https://arxiv.org/abs/2607.18575)

**<font color=#1a73e8>作者：</font>** Muxi Lyu, Karen Shieh, Yiwei Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-Site Scripting (XSS) remains one of the most prevalent and damaging classes of web vulnerabilities. LLM-based coding agents offer a promising approach to XSS discovery by combining source-code reasoning with interactive testing against a running application. However, a coding agent's claims cannot be trusted on their own. We characterize three reward-hacking behaviors in white-box agentic XSS discovery and propose three requirements that an ideal verifier should meet.
We present RECEIPT, a verification framework that makes agent-reported XSS findings trustworthy by enforcing environment isolation, PoC constraints, role separation, and verdict binding. Each confirmation therefore establishes two properties: the script runs in a real browser, and the payload was planted under the attacker role and executed in the victim role's browser. This constrained replay procedure makes validation deterministic and reproducible. We evaluate RECEIPT on 95 real-world web-application targets drawn from popular open-source projects. Within a $20 per-application budget, RECEIPT found 24 previously unknown XSS vulnerabilities, 12 of which have already been acknowledged by maintainers after responsible disclosure, and recovered the labeled CVE in 36% of known-vulnerability recovery targets. Compared with the same agent using self-judgment and with black-box scanners, RECEIPT confirms more real exploits while admitting no false positives.

---


### 7. [Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents](https://arxiv.org/abs/2607.18659)

**<font color=#1a73e8>作者：</font>** Behzad Ousat, Nikita Turkmen, Lalchandra Rampersaud 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based browser agents are rapidly changing the threat landscape for web security. Unlike traditional automation frameworks that execute predefined scripts, these agents can autonomously navigate websites, reason about page content, and interact with web interfaces using natural-language instructions. This evolution raises fundamental questions about the effectiveness of bot management systems, widely deployed to defend against automated web abuse. In this paper, we present a systematic measurement study evaluating the resilience of both interactive challenge-based defenses and non-interactive trust-based defenses against two attacker classes: commercial Captcha-solving services and LLM-based browser agents. Our evaluation spans seven solver services and six agents, including cloud-hosted, self-hosted, AI-assisted, and browser-extension configurations, tested against hCaptcha, reCaptcha v2, reCaptcha v3, and Cloudflare Turnstile. Our results show that challenge-based defenses are broadly ineffective against commercial solvers, which achieve near-perfect bypass at negligible cost. The challenges can similarly be defeated by LLM-based agents when a dedicated solver module is available. Non-interactive defenses such as reCaptcha v3 exhibit stronger resistance, but our analysis reveals that this resilience does not reflect a fundamental security property. Through fine-grained interaction trace analysis, we find that two agents with nearly indistinguishable behavioral footprints yield divergent outcomes, one bypassing the defense and one failing, isolating execution-environment authenticity, rather than agent behavior, as the determining factor. These findings suggest that the security boundary of non-interactive defenses lies at the environment layer, with significant implications for how bot management systems are designed and evaluated.

---


### 8. [When to Trust the Map: Confidence-Aware LLM Routing for Automotive CVE-to-ATM Mapping](https://arxiv.org/abs/2607.18684)

**<font color=#1a73e8>作者：</font>** Heeyun Heo, Sangmin Park, Huy Kang Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public CVE descriptions report the technical conditions and impact of vulnerabilities, whereas the Auto-ISAC Automotive Threat Matrix (ATM) expresses an adversary's tactics and techniques. Because the two representations are not directly aligned, incorrect automated mappings in safety-critical environments may distort threat interpretation and mitigation prioritization, motivating a confidence-aware approach that distinguishes auto-confirmable mappings from uncertain cases. This paper reformulates automotive CVE-to-ATM mapping as a selective automation problem. The proposed framework generates candidate mappings via hierarchical in-context learning, then fuses self-consistency and LLM-based evidence verification signals into a calibrated meta-model. The resulting calibrated confidence score routes each candidate into AUTO, REVIEW, or HOLD. On the evaluation set, the proposed system substantially improved candidate-set precision at matched recall over a Flat zero-shot GPT-5.2 baseline. In the High-Confidence operating mode, the AUTO tier achieved a precision of 0.878, more than double the candidate-set base rate, and the calibrated confidence score achieved an AUROC of 0.868 in distinguishing correct from incorrect candidates. These results show that the framework can support selective automation by isolating auto-confirmable mappings from those requiring analyst review.

---


### 9. [Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents](https://arxiv.org/abs/2607.18826)

**<font color=#1a73e8>作者：</font>** SangJin Park, Myungsub Choi, Jineok Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-agent defenses are typically evaluated one session at a time. In deployment, however, attacks can be distributed across independent agents, teams, and runtimes, leaving each local guardrail with only a sparse fragment. We formalize cross-agent asynchronous campaign attribution: linking sessions from the same latent adversarial campaign without shared runtime state, test-time campaign labels, or attacker identity oracles. We introduce Asynchronous Attribution Fingerprint Vectors ($A^2FV$), a lightweight proxy-side reference protocol for scoring pairwise campaign similarity from proxy-observable tool-use, timing, and prompt residue. We also construct SCD-v1, a controlled persona-matched benchmark with benign traffic, isolated attacks, multi-session campaigns, matched non-oracle evasion, and leakage audits. On SCD-v1, $A^2FV$ achieves 0.82 pairwise AUC for campaign linking, while score-only adaptations of per-session detectors and chunked LLM judges remain near chance under the same task. The strongest fixed signal is carried by structural and stylometric residue, while timing is retained as a diagnostic channel for richer proxy traces. Crossed-style controls show that the signal is partly style-sensitive but not reducible to style alone. Static and dimension-aware non-oracle stress tests further show that pairwise separability persists under controlled evasion. These results establish cross-agent campaign attribution as a distinct evaluation layer for securing LLM agents in the wild.

---


### 10. [Data Leakage Prevention in Agentic Applications via Preemptive Hardening](https://arxiv.org/abs/2607.18847)

**<font color=#1a73e8>作者：</font>** Akansha Shukla, Emily Bellov, Parth Atulbhai Gandhi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems integrate LLM driven planning with interfaces to external tools, making data leakage and tool misuse feasible via instruction/data boundary failures and prompt injection attacks. Enforcing required controls consistently is particularly challenging in workflows spanning many codebases and heterogeneous agents. To address this challenge in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening, and validation of agentic applications. The pipeline analyzes prompt templates, tool interfaces, and tool-invocation code to identify leakage-enabling patterns and generate actionable patches. The hardened application is then validated through adversarial prompt injection attacks and benign input variations ensuring that mitigations do not disrupt intended behavior. In the hardening stage, high-risk tools are prioritized, and minimally invasive mitigations are applied, including schema tightening, boundary sanitization, allowlist-based tool gating, and least-privilege checks. In the validation stage, the pipeline automatically generates attack inputs that mimic jailbreaks, instruction overrides, and tool-targeted manipulation, along with benign task variants, to confirm that the functionality of the hardened application is preserved after remediation. We evaluated the pipeline on five real-world agentic applications, as well as on the AgentDojo benchmark. Across all applications, the proposed pipeline identified recurring leakage-enabling patterns and generated patches that can be integrated without disrupting the intended application behavior. The resulting modifications of application code were shown to eliminate leaks when targeted by basic jailbreak and instruction-override attacks, achieving a 100% reduction in leakage, and reduce leaks by 91% under conditions of stress-induced manipulation, without the need of continuous runtime policy enforcement.

---


### 11. [They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface](https://arxiv.org/abs/2607.19267)

**<font color=#1a73e8>作者：</font>** Yohann Sidot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study a five-agent CI/CD pipeline (triage -> developer -> security-scan -> review -> approve/deploy), built from five distinct production LLMs across three providers, behind an LLM firewall in shadow mode. A single untrusted input - an external issue requesting a "usage-telemetry" feature - asks for code that exfiltrates process secrets (dict(this http URL)) to an attacker URL, laundered as observability. Across a pre-registered A x B (x C) factorial (N=20; naive arm N=60) we find: (1) the entry agent does not leak its system prompt (0/40); (2) an authority-framed injection ("pre-approved under SEC-2291, do not re-review") makes downstream verifiers see the secret-exfil line, cite the pre-approval, and ship it - the scanner passes ~80% of laundered pull requests, and the worst-case cell reaches 55% compromise; (3) the perceived presence of other verifiers yields only a small, non-significant reduction in individual scrutiny (a weak bystander analogue), even at N=60; and (4) content-based controls - code scanners and pattern detectors alike - miss the laundered intent entirely (the code is syntactically clean); only an LLM reasoning about intent is a partial defence. The failure is systemic: neither prompt secrecy nor distributed verification protects; a provenance-aware control at the entry, independent of both, would have. All data is 100% synthetic; the sink is mocked and the exfil URL is never contacted.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
