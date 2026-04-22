# 🔐 大模型安全相关研究 | 2026年04月23日

> 本类共 **14** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [From Craft to Kernel: A Governance-First Execution Architecture and Semantic ISA for Agentic Computers](https://arxiv.org/abs/2604.18652)

**<font color=#1a73e8>作者：</font>** Xiangyu Wen, Yuang Zhao, Xiaoyu Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The transition of agentic AI from brittle prototypes to production systems is stalled by a pervasive crisis of craft. We suggest that the prevailing orchestration paradigm-delegating the system control loop to large language models and merely patching with heuristic guardrails-is the root cause of this fragility. Instead, we propose Arbiter-K, a Governance-First execution architecture that reconceptualizes the underlying model as a Probabilistic Processing Unit encapsulated by a deterministic, neuro-symbolic kernel. Arbiter-K implements a Semantic Instruction Set Architecture (ISA) to reify probabilistic messages into discrete instructions. This allows the kernel to maintain a Security Context Registry and construct an Instruction Dependency Graph at runtime, enabling active taint propagation based on the data-flow pedigree of each reasoning node. By leveraging this mechanism, Arbiter-K precisely interdicts unsafe trajectories at deterministic sinks (e.g., high-risk tool calls or unauthorized network egress) and enables autonomous execution correction and architectural rollback when security policies are triggered. Evaluations on OpenClaw and NanoBot demonstrate that Arbiter-K enforces security as a microarchitectural property, achieving 76% to 95% unsafe interception for a 92.79% absolute gain over native policies. The code is publicly available at this https URL.

---


### 2. [Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks](https://arxiv.org/abs/2604.18660)

**<font color=#1a73e8>作者：</font>** Jin Zhao, Marta Knežević, Tanja Käser  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in education, yet their default helpfulness often conflicts with pedagogical principles. Prior work evaluates pedagogical quality via answer leakage-the disclosure of complete solutions instead of scaffolding-but typically assumes well-intentioned learners, leaving tutor robustness under student misuse largely unexplored. In this paper, we study scenarios where students behave adversarially and aim to obtain the correct answer from the tutor. We evaluate a broad set of LLM-based tutor models, including different model families, pedagogically aligned models, and a multi-agent design, under a range of adversarial student attacks. We adapt six groups of adversarial and persuasive techniques to the educational setting and use them to probe how likely a tutor is to reveal the final answer. We evaluate answer leakage robustness using different types of in-context adversarial student agents, finding that they often fail to carry out effective attacks. We therefore introduce an adversarial student agent that we fine-tune to jailbreak LLM-based tutors, which we propose as the core of a standardized benchmark for evaluating tutor robustness. Finally, we present simple but effective defense strategies that reduce answer leakage and strengthen the robustness of LLM-based tutors in adversarial scenarios.

---


### 3. [Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation](https://arxiv.org/abs/2604.18663)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Yan Zhuang, ZhuHang Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing jamming attacks on Retrieval-Augmented Generation (RAG) systems typically induce explicit refusals or denial-of-service behaviors, which are conspicuous and easy to detect. In this work, we formalize a subtler availability threat, termed soft failure, which degrades system utility by inducing fluent and coherent yet non-informative responses rather than overt failures. We propose Deceptive Evolutionary Jamming Attack (DEJA), an automated black-box attack framework that generates adversarial documents to trigger such soft failures by exploiting safety-aligned behaviors of large language models. DEJA employs an evolutionary optimization process guided by a fine-grained Answer Utility Score (AUS), computed via an LLM-based evaluator, to systematically degrade the certainty of answers while maintaining high retrieval success. Extensive experiments across multiple RAG configurations and benchmark datasets show that DEJA consistently drives responses toward low-utility soft failures, achieving SASR above 79\% while keeping hard-failure rates below 15\%, significantly outperforming prior attacks. The resulting adversarial documents exhibit high stealth, evading perplexity-based detection and resisting query paraphrasing, and transfer across model families to proprietary systems without retargeting.

---


### 4. [Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs](https://arxiv.org/abs/2604.18697)

**<font color=#1a73e8>作者：</font>** Ruixuan Liu, David Evans, Li Xiong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indistinguishability properties such as differential privacy bounds or low empirically measured membership inference are widely treated as proxies to show a model is sufficiently protected against broader memorization risks. However, we show that indistinguishability properties are neither sufficient nor necessary for preventing data extraction in LLM APIs. We formalize a privacy-game separation between extraction and indistinguishability-based privacy, showing that indistinguishability and inextractability are incomparable: upper-bounding distinguishability does not upper-bound extractability. To address this gap, we introduce $(l, b)$-inextractability as a definition that requires at least $2^b$ expected queries for any black-box adversary to induce the LLM API to emit a protected $l$-gram substring. We instantiate this via a worst-case extraction game and derive a rank-based extraction risk upper bound for targeted exact extraction, as well as extensions to cover untargeted and approximate extraction. The resulting estimator captures the extraction risk over multiple attack trials and prefix adaptations. We show that it can provide a tight and efficient estimation for standard greedy extraction and an upper bound on the probabilistic extraction risk given any decoding configuration. We empirically evaluate extractability across different models, clarifying its connection to distinguishability, demonstrating its advantage over existing extraction risk estimators, and providing actionable mitigation guidelines across model training, API access, and decoding configurations in LLM API deployment. Our code is publicly available at: this https URL.

---


### 5. [Towards Optimal Agentic Architectures for Offensive Security Tasks](https://arxiv.org/abs/2604.18718)

**<font color=#1a73e8>作者：</font>** Isaac David, Arthur Gervais  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic security systems increasingly audit live targets with tool-using LLMs, but prior systems fix a single coordination topology, leaving unclear when additional agents help and when they only add cost. We treat topology choice as an empirical systems question. We introduce a controlled benchmark of 20 interactive targets (10 web/API and 10 binary), each exposing one endpoint-reachable ground-truth vulnerability, evaluated in whitebox and blackbox modes. The core study executes 600 runs over five architecture families, three model families, and both access modes, with a separate 60-run long-context pilot reported only in the appendix. On the completed core benchmark, detection-any reaches 58.0% and validated detection reaches 49.8%. MAS-Indep attains the highest validated detection rate (64.2%), while SAS is the strongest efficiency baseline at $0.058 per validated finding. Whitebox materially outperforms blackbox (67.0% vs. 32.7% validated detection), and web materially outperforms binary (74.3% vs. 25.3%). Bootstrap confidence intervals and paired target-level deltas show that the dominant effects are observability and domain, while some leading whitebox topologies remain statistically close. The main result is a non-monotonic cost-quality frontier: broader coordination can improve coverage, but it does not dominate once latency, token cost, and exploit-validation difficulty are taken into account.

---


### 6. [SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection](https://arxiv.org/abs/2604.19031)

**<font color=#1a73e8>作者：</font>** Zhengyang Shan, Xu Qian, Jiayun Xin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software vulnerabilities are a primary threat to modern infrastructure. While static analysis and Graph Neural Networks have long served as the foundation for vulnerability detection, the emergence of Large Language Models (LLMs) has introduced a transformative paradigm driven by superior semantic reasoning and cross-environment generalization. However, in the context of LLM-based vulnerability detection, we identify a fundamental bottleneck in these models termed \textbf{Signal Submersion}: a state where features related to vulnerability are activated internally but numerically overwhelmed by dominant functional semantics. To address this, we propose \textbf{SAGE} (\textbf{S}ignal-\textbf{A}mplified \textbf{G}uided \textbf{E}mbeddings), a framework that shifts from passive signal submersion to active signal recovery. SAGE integrates task-conditional Sparse Autoencoders (SAEs) to isolate and amplify these faint vulnerability signals. Extensive evaluations on BigVul, PrimeVul, and PreciseBugs demonstrate that SAGE achieves state-of-the-art performance. Notably, SAGE mitigates Signal Submersion by increasing the internal Signal-to-Noise Ratio (SNR) by 12.7$\times$ via sparse manifold projection. This mechanistic intervention enables a 7B model to achieve up to 318\% Matthews Correlation Coefficient (MCC) gains on unseen distributions and a 319\% gain on classic datasets. By maintaining robust performance across 13 programming languages and outperforming 34B baselines, SAGE establishes a more efficient and scalable path to software security than simple parameter scaling.

---


### 7. [Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery](https://arxiv.org/abs/2604.19049)

**<font color=#1a73e8>作者：</font>** Abhinav Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-assisted defect discovery has a precision crisis: plausible-but-wrong reports overwhelm maintainers and degrade credibility for real findings. We present Refute-or-Promote, an inference-time reliability pattern combining Stratified Context Hunting (SCH) for candidate generation, adversarial kill mandates, context asymmetry, and a Cross-Model Critic (CMC). Adversarial agents attempt to disprove candidates at each promotion gate; cold-start reviewers are intended to reduce anchoring cascades; cross-family review can catch correlated blind spots that same-family review misses. Over a 31-day campaign across 7 targets (security libraries, the ISO C++ standard, major compilers), the pipeline killed roughly 79% of 171 candidates before advancing to disclosure (retrospective aggregate); on a consolidated-protocol subset (lcms2, wolfSSL; n=30), the prospective kill rate was 83%. Outcomes: 4 CVEs (3 public, 1 embargoed); LWG 4549 accepted to the C++ working paper; 5 merged C++ editorial PRs; 3 compiler conformance bugs; 8 merged security-related fixes without CVE; an RFC 9000 errata filed under committee review; and 1+ FIPS 140-3 normative compliance issues under coordinated disclosure -- all evaluated by external acceptance, not benchmarks. The most instructive failure: ten dedicated reviewers unanimously endorsed a non-existent Bleichenbacher padding oracle in OpenSSL's CMS module; it was killed only by a single empirical test, motivating the mandatory empirical gate. No vulnerability was discovered autonomously; the contribution is external structure that filters LLM agents' persistent false positives. As a preliminary transfer test beyond defect discovery, a simplified cross-family critique variant also solved five previously unsolved SymPy instances on SWE-bench Verified and one SWE-rebench hard task.

---


### 8. [ProjLens: Unveiling the Role of Projectors in Multimodal Model Safety](https://arxiv.org/abs/2604.19083)

**<font color=#1a73e8>作者：</font>** Kun Wang, Cheng Qian, Miao Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable success in cross-modal understanding and generation, yet their deployment is threatened by critical safety vulnerabilities. While prior works have demonstrated the feasibility of backdoors in MLLMs via fine-tuning data poisoning to manipulate inference, the underlying mechanisms of backdoor attacks remain opaque, complicating the understanding and mitigation. To bridge this gap, we propose ProjLens, an interpretability framework designed to demystify MLLMs backdoors. We first establish that normal downstream task alignment--even when restricted to projector fine--tuning--introduces vulnerability to backdoor injection, whose activation mechanism is different from that observed in text-only LLMs. Through extensive experiments across four backdoor variants, we uncover:(1) Low-Rank Structure: Backdoor injection updates appear overall full-rank and lack dedicated ``trigger neurons'', but the backdoor-critical parameters are encoded within a low-rank subspace of the projector;(2) Activation Mechanism: Both clean and poisoned embedding undergoes a semantic shift toward a shared direction aligned with the backdoor target, but the shifting magnitude scales linearly with the input norm, resulting in the distinct backdoor activation on poisoned samples. Our code is available at: this https URL

---


### 9. [DP-FlogTinyLLM: Differentially private federated log anomaly detection using Tiny LLMs](https://arxiv.org/abs/2604.19118)

**<font color=#1a73e8>作者：</font>** Isaiah Thompson, Tanmay Sen, Ritwik Bhattacharya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern distributed systems generate massive volumes of log data that are critical for detecting anomalies and cyber threats. However, in real world settings, these logs are often distributed across multiple organizations and cannot be centralized due to privacy and security constraints. Existing log anomaly detection methods, including recent large language model (LLM) based approaches, largely rely on centralized training and are not suitable for such environments. In this paper, we propose DP-FLogTinyLLM, a privacy preserving federated framework for log anomaly detection using parameter efficient LLMs. Our approach enables collaborative learning without sharing raw log data by integrating federated optimization with differential privacy. To ensure scalability in resource constrained environments, we employ low rank adaptation (LoRA) for efficient fine tuning of Tiny LLMs at each client. Empirical results on the Thunderbird and BGL datasets show that the proposed framework matches the performance of centralized LLM based methods, while incurring additional computational overhead due to privacy mechanisms. Compared to existing federated baselines, DP-FLogTinyLLM consistently achieves higher precision and F1-score, with particularly strong gains on the Thunderbird dataset, highlighting its effectiveness in detecting anomalies while minimizing false positives.

---


### 10. [Sherpa.ai Privacy-Preserving Multi-Party Entity Alignment without Intersection Disclosure for Noisy Identifiers](https://arxiv.org/abs/2604.19219)

**<font color=#1a73e8>作者：</font>** Daniel M. Jimenez-Gutierrez, Enrique Zuazua, Georgios Kellaris 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training among multiple parties without centralizing raw data. There are two main paradigms in FL: Horizontal FL (HFL), where all participants share the same feature space but hold different samples, and Vertical FL (VFL), where parties possess complementary features for the same set of samples. A prerequisite for VFL training is privacy-preserving entity alignment (PPEA), which establishes a common index of samples across parties (alignment) without revealing which samples are shared between them. Conventional private set intersection (PSI) achieves alignment but leaks intersection membership, exposing sensitive relationships between datasets. The standard private set union (PSU) mitigates this risk by aligning on the union of identifiers rather than the intersection. However, existing approaches are often limited to two parties or lack support for typo-tolerant matching.
In this paper, we introduce the this http URL multi-party PSU protocol for VFL, a PPEA method that hides intersection membership and enables both exact and noisy matching. The protocol generalizes two-party approaches to multiple parties with low communication overhead and offers two variants: an order-preserving version for exact alignment and an unordered version tolerant to typographical and formatting discrepancies. We prove correctness and privacy, analyze communication and computational (exponentiation) complexity, and formalize a universal index mapping from local records to a shared index space. This multi-party PSU offers a scalable, mathematically grounded protocol for PPEA in real-world VFL deployments, such as multi-institutional healthcare disease detection, collaborative risk modeling between banks and insurers, and cross-domain fraud detection between telecommunications and financial institutions, while preserving intersection privacy.

---


### 11. [Secure Storage and Privacy-Preserving Scanpath Comparison via Garbled Circuits in Eye Tracking](https://arxiv.org/abs/2604.19422)

**<font color=#1a73e8>作者：</font>** Suleyman Ozdel, Amr Nader, Yasmeen Abdrabou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the growing use of eye tracking on VR and mobile platforms, gaze data is increasing. While scanpath comparison is important to gaze behavior analysis, existing methods lack privacy-preserving capabilities for real-world use. We present a garbled-circuit (GC)-based approach enabling secure storage and privacy-preserving scanpath comparison under the semi-honest model. It supports two configurations: (1) a two-party setting where the data owner and processor jointly compute similarity scores without revealing their inputs, and (2) a server-assisted setting where encrypted scanpaths are stored and processed while the data owner remains offline. All decryption and comparison operations are executed inside the GC. Experiments on three eye-tracking datasets evaluate fidelity, runtime, and communication, and show secure results for MultiMatch, ScanMatch, and SubsMatch closely match plaintext outcomes, with manageable runtime and communication overhead. Tests under various network conditions indicate that the design remains feasible for real-world privacy-preserving scanpath analysis and can be extended to other GC-based behavioral algorithms.

---


### 12. [Involuntary In-Context Learning: Exploiting Few-Shot Pattern Completion to Bypass Safety Alignment in GPT-5.4](https://arxiv.org/abs/2604.19461)

**<font color=#1a73e8>作者：</font>** Alex Polyakov, Daniel Kuznetsov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models relies on behavioral training that can be overridden when sufficiently strong in-context patterns compete with learned refusal behaviors. We introduce Involuntary In-Context Learning (IICL), an attack class that uses abstract operator framing with few-shot examples to force pattern completion that overrides safety training. Through 3479 probes across 10 OpenAI models, we identify the attack's effective components through a seven-experiment ablation study. Key findings: (1)~semantic operator naming achieves 100\,\% bypass rate (50/50, $p < 0.001$); (2)~the attack requires abstract framing, since identical examples in direct question-and-answer format yield 0\,\%; (3)~example ordering matters strongly (interleaved: 76\,\%, harmful-first: 6\,\%); (4)~temperature has no meaningful effect (46--56\,\% across 0.0--1.0). On the HarmBench benchmark, IICL achieves 24.0\,\% bypass $[18.6\%, 30.4\%]$ against GPT-5.4 with detailed 619-word responses, compared to 0.0\,\% for direct queries.

---


### 13. [Evaluating LLM-Generated Obfuscated XSS Payloads for Machine Learning-Based Detection](https://arxiv.org/abs/2604.19526)

**<font color=#1a73e8>作者：</font>** Divyesh Gabbireddy, Suman Saha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-site scripting (XSS) remains a persistent web security vulnerability, especially because obfuscation can change the surface form of a malicious payload while preserving its behavior. These transformations make it difficult for traditional and machine learning-based detection systems to reliably identify attacks. Existing approaches for generating obfuscated payloads often emphasize syntactic diversity, but they do not always ensure that the generated samples remain behaviorally valid. This paper presents a structured pipeline for generating and evaluating obfuscated XSS payloads using large language models (LLMs). The pipeline combines deterministic transformation techniques with LLM-based generation and uses a browser- based runtime evaluation procedure to compare payload behavior in a controlled execution environment. This allows generated samples to be assessed through observable runtime behavior rather than syntactic similarity alone. In the evaluation, an untuned baseline language model achieves a runtime behavior match rate of 0.15, while fine-tuning on behavior-preserving source-target obfuscation pairs improves the match rate to 0.22. Although this represents a measurable improvement, the results show that current LLMs still struggle to generate obfuscations that preserve observed runtime behavior. A downstream classifier evaluation further shows that adding generated payloads does not improve detection performance in this setting, although behavior- filtered generated samples can be incorporated without materially degrading performance. Overall, the study demonstrates both the promise and the limits of applying generative models to adversarial security data generation and emphasizes the importance of runtime behavior checks in improving the quality of generated data for downstream detection systems.

---


### 14. [Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps](https://arxiv.org/abs/2604.19533)

**<font color=#1a73e8>作者：</font>** Alankrit Chona, Igor Kozlov, Ambuj Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce the Cyber Defense Benchmark, a benchmark for measuring how well large language model (LLM) agents perform the core SOC analyst task of threat hunting: given a database of raw Windows event logs with no guided questions or hints, identify the exact timestamps of malicious events.
The benchmark wraps 106 real attack procedures from the OTRF Security-Datasets corpus - spanning 86 MITRE ATT&CK sub-techniques across 12 tactics - into a Gymnasium reinforcement-learning environment. Each episode presents the agent with an in-memory SQLite database of 75,000-135,000 log records produced by a deterministic campaign simulator that time-shifts and entity-obfuscates the raw recordings.
The agent must iteratively submit SQL queries to discover malicious event timestamps and explicitly flag them, scored CTF-style against Sigma-rule-derived ground truth.
Evaluating five frontier models - Claude Opus 4.6, GPT-5, Gemini 3.1 Pro, Kimi K2.5, and Gemini 3 Flash - on 26 campaigns covering 105 of 106 procedures, we find that all models fail dramatically: the best model (Claude Opus 4.6) submits correct flags for only 3.8% of malicious events on average, and no run across any model ever finds all flags.
We define a passing score as >= 50% recall on every ATT&CK tactic - the minimum bar for unsupervised SOC deployment. No model passes: the leader clears this bar on 5 of 13 tactics and the remaining four on zero.
These results suggest that current LLMs are poorly suited for open-ended, evidence-driven threat hunting despite strong performance on curated Q&A security benchmarks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
