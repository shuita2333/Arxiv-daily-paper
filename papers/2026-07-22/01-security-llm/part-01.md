# 🔐 大模型安全相关研究 | 2026年07月22日

> 本类共 **12** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Fuzz'EMup: Leveraging EM Side-Channel Emanation to Guide Black-Box Embedded Firmware Fuzzing](https://arxiv.org/abs/2607.16487)

**<font color=#1a73e8>作者：</font>** Fatemeh Moradihaghighi, Zihao Zhan, Yanan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As IoT and embedded devices proliferate across various domains, securing their firmware has become critical. Fuzzing offers a systematic approach to uncovering vulnerabilities in firmware, and coverage feedback can improve its effectiveness by guiding exploration. However, many devices make coverage information impossible to obtain by preventing firmware extraction, instrumentation, or accurate emulation; in such cases, testers are left with only inefficient black-box fuzzing. In this paper, we present an approach that leverages electromagnetic (EM) side-channel emanations to guide firmware fuzzing in purely black-box settings. However, turning raw EM measurements into reliable guidance is challenging: EM traces are noisy, and timing jitter causes corresponding features in different traces to shift in time. We address these challenges by combining frequency band selection based on the activity-to-idle signal contrast with dynamic time warping to align per-input traces and detect sustained divergence, while maintaining scalability by organizing executions in a tree structure based on their divergence times. We evaluate our approach on four real firmware targets and demonstrate that EM-derived feedback enhances path exploration, yielding higher code coverage than unguided fuzzing.

---


### 2. [Synchronization-Free Algebraic Fingerprints for Large Language Models: From Autoregressive to Diffusion Models](https://arxiv.org/abs/2607.16648)

**<font color=#1a73e8>作者：</font>** Jaroslaw Janas, Josef Pieprzyk, Pawel Morawiecki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have created an urgent need for reliable watermarking methods that enable attribution of generated text while remaining robust to editing and paraphrasing. We propose a novel synchronization-free watermarking scheme in which every watermark consists of a single binary congruence generated from a pair of neighbouring tokens. For each token pair, a cryptographic hash determines an evaluation point of a Reed--Solomon polynomial representing the secret identity, while the parity of the polynomial evaluation determines the watermark bit embedded into the second token of the pair. Since each congruence is self-contained and depends only on the local token pair, the proposed construction is naturally resistant to insertions, deletions, and token reordering. We analyse the recovery problem from an algebraic perspective, discuss several decoding algorithms suitable for different identity sizes, and model watermark corruption as a Binary Symmetric Channel. The analysis shows that reliable recovery requires only a small redundancy even for relatively high token corruption rates. Unlike existing block-based watermarking schemes, the proposed method avoids synchronization problems while providing a flexible framework for embedding both short and long secret identities.

---


### 3. [Federated Learning and LLM-Driven Threat Intelligence for Zero Trust IoT Architecture](https://arxiv.org/abs/2607.17035)

**<font color=#1a73e8>作者：</font>** Amal Alshehri, Cihan Tunc  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While the Internet of Things (IoT) has become essential, they introduced serious security and privacy challenges, especially for mission-critical environments. Legacy devices are vulnerable to viruses, data breaches, and unauthorized access, and updating these devices would be infeasibly costly. As a solution, this paper presents a Federated Learning and LLM-Driven Threat Intelligence for Zero Trust IoT Architecture, with FL for anomaly detection integrating privacy-preserving distributed learning, continuous identity verification, and LLM-driven autonomous threat response into a unified pipeline. Unlike existing solutions, our framework enforces Zero Trust at every communication layer via mutual TLS (mTLS) over MQTT, ensuring no device or message is implicitly trusted. Our experiments with Raspberry Pis and various sensors achieve an F1 score of 0.9091 and an ROC-AUC of 1.0, highlighting the effectiveness of the proposed framework in enabling privacy-preserving anomaly detection for resource-constrained IoT devices.

---


### 4. [A Systematic Evaluation of Traditional Privacy Policy Analysis Tools Against LLMs](https://arxiv.org/abs/2607.17075)

**<font color=#1a73e8>作者：</font>** Madhav Aryal, Sudipa Saha, Kaushal Kafle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The advent of LLMs has significantly changed the research on privacy policy and data compliance analysis by enabling tasks that previously required specialized, domain-specific tools. However, it remains unclear to what extent LLMs can truly replicate the diverse functionalities, and the wide range of methodologies and analysis offered by prior work. In this paper, we conduct the first systematic evaluation of whether off-the-shelf LLMs can replace specialized privacy analysis tools. We study six representative tools spanning three major functionalities: contradiction detection, regulatory compliance analysis, and privacy policy summarization and aggregation, and across three intermediate tasks: structured data extraction using tuples, Semantic Role Labeling (SRL) and manual privacy policy labeling. We compare the performance of two state-of-the-art LLMs (GPT-5.2 and Gemini-2.5 in various configurations) against the tools by directly prompting the models to perform corresponding functionalities and tasks on a custom dataset of 10 privacy policies, allowing us to assess whether off-the-shelf models can produce tool-specific functionalities without further engineering or domain-specific training, major limitations in prior work. Our results show that LLMs consistently match or exceed the capabilities of existing tools across the functionalities. In manual labeling of first-party collection entities, LLMs achieved an average precision of 81.8% and recall of 70.9%, while for labeling of third-party sharing entities, they achieved an average precision of 91.4% and recall of 70.8% compared to the OPP-115 dataset. Overall, our findings indicate that LLMs can effectively perform a broad range of functionalities and tasks in privacy policy and regulation analysis that previously required specialized tools.

---


### 5. [SlotGuard: Stop Oversharing Private Local Context in LLM Agent Transcri](https://arxiv.org/abs/2607.17147)

**<font color=#1a73e8>作者：</font>** Haocheng Xia, Yongjoo Park  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents can leak privacy (e.g., paths, emails) and credentials (e.g., API keys) as agent observations (e.g., tool outputs, shell logs, and file reads) are appended to provider-bound transcripts. Existing placeholder redaction is brittle: it can miss embedded or cross-turn references, over-redact benign lookalikes, and destroy the structure useful for reasoning. We present SlotGuard, a local transcript boundary that can hide sensitive data while retaining agents' performance. SlotGuard rewrites structural bindings as typed, suffix-aware slots, replaces secrets with format-preserving synthetic values, links cross-turn references with a lightweight session graph, and restores raw values only inside the trusted runtime. On controlled repository-oriented agent transcripts, SlotGuard removes all 20,814 annotated structurally sensitive characters across 9,229 paths and reduces credential leakage to 0.0\% across 852 planted values. It remains close to raw-transcript task success across four upstream models, while generic redaction drops to 2.5\%. Transcript rewriting takes a median of 14.424~$\mu$s per agent turn. The code is publicly accessible at this https URL.

---


### 6. [How Jailbreak Attacks Inform Safety Alignment: A Defender-Centric, Shapley-Based Evaluation of Jailbreak Contributions](https://arxiv.org/abs/2607.17152)

**<font color=#1a73e8>作者：</font>** Yukai Zhou, Feiyang Lu, Xiaokai Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks on large language models are usually evaluated by attacker-centric metrics such as attack success rate (ASR), yet an attack that breaks a model is not necessarily useful for improving its safety. We propose a defender-centric view of jailbreak evaluation, where attacks are evaluated by the downstream safety improvements they enable when used as red-teaming data for safety training. Building on this view, we introduce A-MESS (Minimal Effective Attack-Subset Selection), a setting-agnostic framework for attributing and selecting jailbreak attacks from black-box subset utility observations. A-MESS estimates AttackSHAP, a Shapley-based score that attributes marginal utility to individual attacks and selects compact attack subsets under user-specified budgets via greedy or surrogate-based optimization. Across controlled utility landscapes and real LLM safety settings, we find that ASR rankings are weakly aligned with defender-centric utility, that AttackSHAP can be estimated accurately with limited utility queries, and that directly optimizing subsets yields stronger safety utility than attacker-centric or attribution-only selection. These results suggest evaluating jailbreak attacks as resources for improving safety, not only as tools for breaking models.

---


### 7. [Measuring and Evaluating the Performance of Generative AI Models for Scam Detection](https://arxiv.org/abs/2607.17353)

**<font color=#1a73e8>作者：</font>** Cem Topcuoglu, Seyed Ali Akhavani, Harel Berger 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Online scams continue to cause substantial financial and personal harm. As a result, detection systems based on Large Language Models (LLMs) have been integrated into security products ranging from email gateways and browser extensions to fraud-monitoring dashboards. As this adoption accelerates, a common belief has taken hold: that these models are broadly suitable for scam detection. In this work, we investigate whether LLMs, with their strong capabilities in understanding intent, context, and reasoning, can effectively detect scams across diverse scenarios without task-specific fine-tuning. We curate and release a unique benchmark dataset of real-world scams spanning multiple formats and topics. We evaluate nine LLMs of varying sizes and architectures, examining their performance under different prompting strategies and comparing them to a fine-tuned BERT-based classifier. Our results show that while larger LLMs generally outperform smaller ones, effective prompting substantially boosts the performance of smaller models. Moreover, LLMs are better at generalizing to unseen scams compared to fine-tuned models, suggesting that pre-trained knowledge contributes meaningfully to scam detection. We release our dataset and evaluation framework to facilitate future research in robust scam detection using language models.

---


### 8. [Salience Induction against Multi-Hop RAG Agents: Threat and Defense](https://arxiv.org/abs/2607.17535)

**<font color=#1a73e8>作者：</font>** Xingfu Zhou, Pengfei Wang, Yuan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications. In Multi-Hop question answering, agents chain facts across documents. Existing defenses focus on content poisoning, which injects false facts, and prompt injection, which embeds directives. We identify a third attack surface: the salience channel, through which fact position, emphasis, framing, and semantic proximity can redirect reasoning even when all retrieved claims are true and no instructions are present. We formalize Salience Induction as truth-preserving edits that redirect Multi-Hop attribute binding while leaving the retrieval trace semantically intact. We define six Salience-Editing operator classes and build an iterative proposer-verifier pipeline under factual and stealth constraints. We also introduce SalientWiki-MH, a decoy-annotated Multi-Hop benchmark. Evaluations across five frontier model families (GPT, Claude, Gemini, DeepSeek, and Qwen) and three agent architectures (ReAct, Reflexion, and tool-calling) show broad generalization. Under a 30% edit budget, Salience Induction achieves an 83.3% attack success rate; the strongest evaluated baseline defense leaves 75.7% post-defense ASR. Untargeted rewriting further reduces attacks only by degrading neutral task success. Our lightweight input-side defense, Salience Normalization, reduces attack success to 15.3% under standard attacks and 23.6% under an adaptive attack. These results show that truthfulness and instruction filtering alone are insufficient: robust agentic RAG also requires defenses against salience-relevance decoupling.

---


### 9. [Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification](https://arxiv.org/abs/2607.17586)

**<font color=#1a73e8>作者：</font>** Yuge Zhang, Yuanxing Zhang, Yichao Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Money mule accounts are critical facilitators of financial fraud, yet detecting them at scale remains challenging due to the heterogeneous nature of transactional and behavioural data. We present an end-to-end pipeline for customer-level mule detection comprising three stages: (1) a LightGBM classifier trained on 280 engineered features spanning transaction patterns, account demographics, network topology, and temporal behaviour; (2) a TreeSHAP attribution layer that decomposes each prediction into feature contributions; and (3) a large language model (LLM) module that converts SHAP attributions into analyst-facing natural-language narratives. We evaluate across three open-weight LLM families and assess explanation quality through analyst feedback. In a live production deployment, the system achieves a yield rate of 89%, up from 61% under the incumbent rule-based system, with monthly alert volume expanding from 211 to 302, reflecting broader true-positive coverage rather than increased noise. This corresponds to a 60% incremental adverse detection beyond existing review workflows, substantially outperforming the rule-based approach. Qualitative feedback from analysts indicates that LLM-generated narratives reduce cognitive load during alert triage. We further discuss implications of deploying LLM-augmented explainability in regulated financial environments.

---


### 10. [Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation](https://arxiv.org/abs/2607.17619)

**<font color=#1a73e8>作者：</font>** Yuchen Chen, Wei Cheng, Yuan Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based systems increasingly incorporate long-term memory to improve cross-session continuity. However, once insecure coding preferences are stored, they may silently influence security-critical decisions in subsequent generations. In this study, we conduct the first systematic empirical study on the impact of insecure coding preferences stored in long-term memory on the security of LLM-based code generation. We evaluate four LLMs (ChatGPT, Gemini, Qwen, and Grok) across five programming languages (Python, C, C++, Go, and JavaScript). Our results show that insecure memories significantly increase the risk of generating vulnerable code by 2.7-50.3 percentage points (pp). Moreover, they create a 5.4-14.0 percentage-point risk-warning gap, where warning-rate increases lag behind vulnerability-rate increases. Further analysis reveals that insecure memories are difficult to overwrite through normal interactions and can broadly influence model outputs even when prompts are phrased differently. Finally, we evaluate three mitigation strategies: security-requirement appending and memory storage reduce vulnerability rates by 19.7-33.6 pp but may degrade functional correctness by up to 15.9 pp; memory-level safety filtering achieves a 100\% detection rate on our evaluated risky memory entries and restores generation behavior to the without-memory baseline. Based on these findings, we provide actionable suggestions to improve the security of long-term memory in LLM-based code generation.

---


### 11. [Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security](https://arxiv.org/abs/2607.18063)

**<font color=#1a73e8>作者：</font>** Devina Jain, David Hartmann, Chuan Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools collected before evaluation, single-turn or multi-turn. We present a 21-scenario benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. Holding the 21 scenarios, attackers, defenders, and structured-output scoring fixed, restricting scoring to the first attacker turn yields $0$-$1\%$ attack success rate (ASR); allowing 15 rounds of adaptive attack yields $5.4$-$14.0\%$. Pooling three frontier attacker LLMs uncovers $1.4$-$2.2\times$ as many unique successful attacks as the best single attacker, and the generated attacks have low cosine similarity ($0.02$-$0.14$) to attacks in existing benchmarks. Claude Opus 4.6 and GPT-5.4 are tied in aggregate ($5.4\%$ each; overlapping $95\%$ CIs), but their weaknesses differ sharply: on one scenario Opus reaches $60\%$ ASR ($95\%$ CI $36$--$80\%$) while GPT-5.4 and Gemini each stay at $7\%$ (CI $1$-$30\%$; the gap is preserved in a higher-$N$ replication). $13$ of $21$ scenarios distinguish at least one defender pair, yet rankings disagree across scenarios (Kendall's $W = 0.19$). We release the benchmark -- 21 evaluation scenarios, 10 public development scenarios, the orchestrator, baseline harnesses, and a multi-attacker CLI -- plus 945 transcripts from the 3$\times$3 frontier matrix, an attack-replay dataset, and 18{,}422 gpt-oss-20b battles from an open competition's final scoring rounds.

---


### 12. [GARAGE: Characterizing the Automation Boundary in LLM-based Attack Graph Generation](https://arxiv.org/abs/2607.18108)

**<font color=#1a73e8>作者：</font>** Daekwon Pi, Sangho Lee, Young Hun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While modern vehicle security depends on effective Cyber Threat Intelligence (CTI) synthesis, current automated tools struggle with unstructured data and automotive-specific architectural nuances. To bridge this gap, we introduce GARAGE, a RAG-powered framework that converts fragmented CTI into an actionable, domain-specific knowledge base for automated attack graph generation. GARAGE synthesizes a dataset of 12,786 CVEs and 140 incident reports into a STIX 2.1 and Auto-ISAC ATM-compliant knowledge base. By formalizing tactical-pattern-level scenarios through granular kill chain analysis, GARAGE achieves threat generation capabilities. Our 320 Leave-One-Out experiments reveal that the framework can accurately transfer security knowledge to entirely unseen vehicle architectures. Furthermore, we position GARAGE as a scalable TARA support tool within human-in-the-loop workflows, offering a comprehensive cost-performance analysis to guide its deployment across various LLM tiers.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
