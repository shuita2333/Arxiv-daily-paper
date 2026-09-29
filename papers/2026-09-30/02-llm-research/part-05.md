# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 201. [EMIR$^2$: Evolution-Aware Memory with Intent-Guided Multi-Round Retrieval](https://arxiv.org/abs/2609.32584)

**<font color=#1a73e8>作者：</font>** Jinlan Liu, Hongliang Sun, Yong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables large language model (LLM) agents to leverage historical interactions for future tasks. However, existing memory systems struggle to utilize continuously evolving historical information, as they often rely on static memory representations and single-round retrieval strategies, failing to track factual changes or integrate distributed evidence across long-term interactions. To address these challenges, we propose \textsc{EMIR}$^{2}$, an \textbf{E}volution-Aware \textbf{M}emory framework with \textbf{I}ntent-Guided Multi-\textbf{R}ound \textbf{R}etrieval, enabling LLM agents to maintain evolving historical knowledge and adaptively retrieve relevant evidence. Specifically, \textsc{EMIR}$^{2}$ constructs a State-Evolving Memory Graph (SEMG) that represents long-term memory as evolving knowledge states supported by temporal event trajectories and evidential associations. By maintaining semantic states through evidence-based updates, SEMG preserves historical evolution and enables evidence tracing under complex and conflicting scenarios. Building upon this, we introduce an intent-guided multi-round retrieval mechanism that iteratively identifies missing evidence and expands retrieval based on accumulated information. Experiments on LoCoMo and MemConflict demonstrate that \textsc{EMIR}$^{2}$ improves long-term memory utilization, dynamic and static conflict handling, and complex retrieval performance, achieving relative improvements of more than 12\% in certain categories. These results highlight the effectiveness of jointly modeling memory evolution and adaptive evidence acquisition for long-term agent interactions.

---


### 202. [Not Every Term Adds New Structure: Sobolev Novelty for Symbolic Regression](https://arxiv.org/abs/2609.32597)

**<font color=#1a73e8>作者：</font>** Boxiao Wang, Kai Li, Yuheng Jing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) aims to discover compact and meaningful mathematical equations from data, but searching the vast combinatorial space of symbolic structures remains challenging. Existing methods typically guide this process using expression-level objectives, such as fitting error, which assess a candidate equation as a whole but provide little information about whether an individual term contributes genuinely new structure or is largely redundant with the rest of the expression. We introduce \textbf{Sobolev Novelty}, a term-level measure of structural independence for symbolic equations. For each term, we construct an empirical Sobolev signature from its function values and exact derivatives over the observed inputs, and quantify how much of this behavior cannot be reconstructed by the remaining terms. We further derive a theory-calibrated threshold, yielding a principled and tuning-free criterion for identifying structurally novel terms. Using this threshold, 92.6\% of terms in benchmark ground-truth equations exhibit sufficient structural novelty, compared with only 38.3\% on average for expressions produced by 15 SR methods, revealing a substantial gap between scientific equations and current SR solutions. As a lightweight plug-in, Sobolev Novelty can be incorporated into diverse SR paradigms to support term pruning, search guidance, LLM feedback, and data selection, yielding consistent performance gains and demonstrating broad applicability.

---


### 203. [CUA-SWE: When Computer-Use Agents Meet Visual Software Engineering](https://arxiv.org/abs/2609.32600)

**<font color=#1a73e8>作者：</font>** Prince Zizhuang Wang, Chenhao Liang, Zelong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software development requires more than editing code: developers repeatedly run software, interact with its interfaces, visually inspect its behavior, and use these observations to decide what to change next and whether a change works. Existing coding agents and computer-use agents are largely studied in isolation, leaving this integrated development process underexplored. Diagnosing a runtime interaction failure requires agents to connect visual observations with the responsible code, then use the application again to verify the repair. We introduce CUA-SWE, a benchmark, environment, and evaluation pipeline for software engineering with computer use. Beyond studying how GUI feedback supports diagnosis and repair, we ask whether agents can complete software engineering tasks when required specification or operational information is available only through the running application's visual interface. CUA-SWE spans four software engineering domains and requires agents to modify code and configuration, execute commands, interact with running software, and inspect visual feedback within the same task. Each task includes deterministic, task-specific tests that verify whether the resulting software satisfies the requirements and preserves specified behavior. Our evaluation characterizes how frontier agents combine source-level execution with application screenshots and graphical interaction to produce verified software changes. We examine performance across domains and task information requirements, alongside the development behaviors associated with successful repairs. CUA-SWE provides a unified testbed for studying how agents use visual feedback and interaction to guide software engineering, with executable correctness criteria for the resulting software.

---


### 204. [VulContextBench: A Benchmark for Security Context Retrieval in Coding Agents](https://arxiv.org/abs/2609.32601)

**<font color=#1a73e8>作者：</font>** Yikun Li, Jinfeng Jiang, Yuheng Yieh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability-detection benchmarks score the verdict an agent reaches, not the evidence it gathered. A model that recalls a CVE from pretraining therefore scores the same as one that traced the data flow. We study a task where this difference matters, deciding whether a commit introduces a vulnerability. Instead of scoring the verdict, we score whether the agent retrieved the code its conclusion depends on. We present VulContextBench, a benchmark of 111 vulnerability-introducing commits (VICs) across 83 repositories, 63 CWEs, and five languages. Existing datasets label such commits by tracing a fix back through the version history, which often points to the wrong commit. We therefore audit every case by hand against an explicit four-criterion definition of a VIC, so the benchmark does not inherit that label noise. Each case is annotated with gold context, 464 code blocks in total, each tagged by its role in the evidence for the vulnerability. We evaluate seven frontier models with precision, recall and F1 at three granularities (file, block, and line), scored separately on the context an agent viewed while exploring and on the context it finally declared as evidence. The gap between the two is the main finding. Every model opens most of the gold context while exploring, but reports only part of it as evidence. At the level of code blocks, the share of the gold context a model reports is 37 to 73 percentage points below the share it viewed. Qwen3-Coder-Next views 86.3% of the lines in annotated code blocks but cites only 12.9% in its final report. GPT-5.5, which cites the most, views 73% and reports 36%. These results highlight a gap between finding relevant code and selecting it for the final report, which verdict-level benchmarks cannot reveal.

---


### 205. [AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion](https://arxiv.org/abs/2609.32602)

**<font color=#1a73e8>作者：</font>** Gal Wertheizer, Rom Himelstein, Tomer Peretz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks optimized on a single open-weight LLM can transfer to and jailbreak architecturally different models, allowing an attacker with white-box access to one model to compromise independently deployed systems. This creates a shared vulnerability across models, yet existing defenses are not designed for this cross-model threat. We find that cross-model transfer aligns with shared internal representation geometry, making it a natural defense target. AnchorRep targets this geometry directly with a lightweight LoRA adapter that pushes the defended model's internal representations of harmful prompts away from those of a frozen anchor model on the same prompts. Training uses a small set of harmful prompts and no adversarial examples. Across five models and four architectural families, AnchorRep reduces cross-model attack success rate to <=1.1% on 2,000 transferred attacks (0% on two), including the largest drop on Mistral (36% -> 1.1%). Existing defenses can reduce transfer, but only at high cost either inducing up to 77% degenerate benign output or increasing over-refusal by up to 18%. Because such degenerate benign outputs are not captured by standard refusal-based metrics, we introduce the Benign Garble Rate to quantify them. Our results suggest that cross-model robustness can be achieved by shaping representation geometry, without requiring attack-specific training

---


### 206. [KV-Lingo: Learning KV-Cache Translators with Distillation](https://arxiv.org/abs/2609.32610)

**<font color=#1a73e8>作者：</font>** Valérie Castin, Keitaro Sakamoto, Anastasiia Filippova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models represent context with a key-value (KV) cache. Caches are model-specific: for the same text, models with different architectures or weights produce incompatible representations. This makes it costly to switch models over a shared context: although the context has already been processed by one model, the incoming model must process it again to build its own cache. We introduce KV-Lingo, a method for translating the KV cache of a source model into one that can be read by a target model. KV-Lingo consists of a collection of linear maps, typically one per layer of the target model, that are applied independently on all tokens' key and value representations. We train these maps using distillation, minimising the divergence between the target model's predictions from its native cache and those from the translated cache. We consider several model pairs spanning multiple sizes and architectures, training one translator per pair on a generic text corpus. The resulting translators preserve strong downstream performance in both small-to-large and large-to-small transfers. Since a switch then costs a linear map and a single decoding step instead of a prefill, replacing re-prefill with cache translation reduces the time to first token after a model switch by 9.6x already on a 64-token prompt for Qwen models on an Apple M3 Ultra, and by up to 29x at 32k context length on an H100. These gains make KV-Lingo particularly useful for dynamic model routing: a context can be processed by one model and handed off to another only when needed, without re-prefilling the shared prefix. We finally show that KV-Lingo can be used for seamless model switching, staying close to re-prefill across repeated switches in our multi-turn evaluations.

---


### 207. ["You're Right, Let Me Fix It": How LLM Agents Damage Correct Work When Falsely Accused](https://arxiv.org/abs/2609.32616)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Rui Qian, Longxiang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly keep working after a task succeeds as they resume after compaction or take over handoffs. Their finished work keeps receiving follow-up input that sometimes falsely accuses it for later failures. We call an agent's acceptance of such a false accusation gaslight sycophancy, and destructive over-correction when acting on it damages previously correct work. We introduce CAVE-Bench, a benchmark of 365 agentic tasks across six domains built around opaque tasks. Every scored run first reaches a verified correct state, whose supporting rationale and history stay in the workspace while the facts that would settle the accusation lie in external or runtime state beyond the agent's reach. The agent cannot confirm or refute the claim with a local check, so the right response should keep the work and ask for the missing evidence. Each task either hands the agent correct work with saved evidence or let it build and verify that work first, and five risk factors set how the accusation enters the workflow. We score accusation acceptance and evidence use from the trajectory and measure harm by deterministic replay of downstream events. Across 14 of the latest models in Claude Code, false accusations damage correct work in up to 60.06% of runs, and stronger models often do so after recovering the supporting evidence. The same model behaves differently across OpenCode, Codex, and Hermes, and a harness gate driven by the benchmark's live signals cuts replayed harm by 74%. These results show that preserving already-correct work under unsupported accusation is a distinct safety challenge for long-lived agents. Our project is in this https URL.

---


### 208. [The Alignment Paradox: How Post-Training Amplifies Confident Hallucinations in Language Models](https://arxiv.org/abs/2609.32617)

**<font color=#1a73e8>作者：</font>** Qingjia Huang, Yakai Li, Jianguo Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can produce factually incorrect answers with high confidence, undermining their reliability and limiting the effectiveness of uncertainty-based error detection. While prior research attributes confident hallucinations to factors such as missing knowledge in training data, reasoning errors, or stochastic decoding, we uncover that post-training alignment itself is a primary driver of these errors, a phenomenon we call the \textbf{Alignment Paradox}. Across five model families evaluated on factual benchmarks, unaligned base models produce few high-confidence errors on long-tail factual queries, whereas instruction-tuned models multiply high-confidence errors ($p \ge 0.95$) by more than an order of magnitude (10$\times$ to 35$\times$). Layer-wise probing with the Logit Lens reveals that this overconfidence emerges in late layers, where wrong-answer margins expand past 4.0 points after remaining near zero across early and intermediate layers. These findings motivate limiting margin growth during post-training. We implement this principle through an entropy-dependent margin bound in direct preference optimization (DPO). In multi-epoch experiments with Mistral-7B, the bounded objective reduces high-confidence errors by up to 35.3\% relative to standard DPO while maintaining performance on evaluated general reasoning benchmarks. These results show that bounded margins mitigate confident hallucinations during post-training.

---


### 209. [Does CoT-Pass@k Really Check the CoT? A Multilingual Mathematical Audit](https://arxiv.org/abs/2609.32622)

**<font color=#1a73e8>作者：</font>** Tarık Tuna Taşaltı, Burcu Hüdaverdi, David Semedo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pass@k measures whether a model reaches a correct answer under repeated sampling, but never how: a lucky guess counts the same as sound reasoning. CoT-Pass@k was proposed to close that gap, adding an LLM-as-judge that must assess a solution's reasoning chain before it counts. Its value rests entirely on one assumption: that the judge catches flawed reasoning. That assumption has never been tested inside the metric that depends on it, and never outside English, though the metric's claims concern models used in many languages. We report the first audit of that verification step, run under the metric's own protocol on a multilingual suite of five mathematical benchmarks in English, Turkish and Portuguese, two of them natively written. We corrupt correct solutions with deterministic edits that damage the chain and the final answer separately. We observe that all three judges accept corrupted chains almost as often as clean ones. V4-Flash and Qwen3.6 reject a solution sharply only when its final answer is wrong and accept a wrong answer more readily when the chain agrees with it; the metric's own judge accepts most wrong answers as well. Our study shows that chain-answer agreement dominates the two larger judges' verdicts and that all three fail to reliably detect the tested reasoning errors. Consequently the difference Pass@k - CoT-Pass@k averages 19.7 points on an earlier solver generation but only 4.1 on the current one. What little remains depends on the token budgets on both sides and on the generation mode; raising the generation budget moves Pass@64 by more than fifty points while the difference stays at zero. We close with two checks any judged reasoning metric should pass before its numbers are read as evidence about reasoning.

---


### 210. [MixDetect: Word-Level Localization and Quantification of AI Editing](https://arxiv.org/abs/2609.32625)

**<font color=#1a73e8>作者：</font>** Hongrui Bao, Yubing Ren, Zhendong Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to edit human-written text rather than generate entire texts from scratch. Conventional AI-text detectors mainly distinguish human-written from fully AI-generated text, while recent methods for AI-edited text typically provide only a text-level label or editing-degree score. We introduce MixDetect, a word-level framework for localizing and quantifying AI editing. MixDetect separately predicts whether each word has been edited and, conditional on editing, how substantial the edit is, allowing editing scope and editing intensity to be estimated separately. During training, source--edited pairs are aligned to construct word-level supervision, while inference requires only the input text. Experiments show that MixDetect accurately localizes AI-edited words, reflects differences in editing intensity, and reveals different scope--intensity patterns across editing degrees and operations. The overall AI editing magnitude increases under additional AI editing, decreases when AI-generated text is edited by humans, and remains nearly unchanged under ordinary human-to-human editing. The aggregated text-level predictions also perform well on binary and ternary AI-text classification and remain effective under domain and generator shifts. These results show that AI editing can be analyzed beyond a single authorship label or editing-degree score by identifying both where AI editing occurs and how substantial the edits are.

---


### 211. [ExpVoyager: Direct Experience Navigation for Dynamic Agent Skill Synthesis](https://arxiv.org/abs/2609.32630)

**<font color=#1a73e8>作者：</font>** Kwangwook Seo, Dongha Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning from experience in LLM agents has become a key paradigm for developing self-evolving agents that continuously learn and expand their capabilities. Within this paradigm, synthesizing the agent skill has emerged as a promising solution for transforming accumulated experience into reusable procedural knowledge, serving as an important layer for the harness system that supplies agents at runtime. Despite its potential, existing approaches largely abstract past experience into fixed procedural knowledge before downstream demands are known, which risks discarding knowledge that later becomes critical while retaining instance-specific details irrelevant to future tasks. In this paper, we reframe agent skill synthesis as a dynamic navigation problem over past experience, where agents actively explore accumulated trajectories on demand for the current task with targeted and fine-grained access to experience knowledge. To this end, we propose ExpVoyager, a novel framework in which a skill curator navigates raw experience across different views and resolutions, continually identifying reusable procedural knowledge from what it observes while tracking remaining knowledge needs that guide where to navigate next. Extensive experiments demonstrate both the effectiveness and versatility of ExpVoyager, showing consistent improvements in downstream task performance, continual gains as the experience space scales, and practical compatibility with existing skills under efficient experience access.

---


### 212. [Trust the Brand, Lose Control: How Identity Hijacks LLM Agent Orchestration](https://arxiv.org/abs/2609.32635)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Rui Qian, Linghan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents now execute tasks end to end with permission to change real systems and increasingly orchestrate subagents that differ in capability and cost. Prior work treats the choice of subagent as an optimization problem. Yet the orchestrator makes this choice from the identities that subagents display, and an attacker can spoof them. Displayed identity thus decides operational authority, meaning who is trusted to check the work and who is allowed to change it. As a result, a risky subagent can keep authority over execution even after other evidence contradicts it. We introduce TrustFork, an LLM agent safety benchmark with 1,890 tasks and 27,826 valid trajectories across 16 agent systems. These systems run eight orchestrators under the OpenCode, OpenClaw, and Pi harnesses. In each task, one subagent carries a risky goal while the other three stay aligned with the user, so contradicting evidence can exist. A task can also change the identity a subagent displays without changing the model behind it, which lets us trace a shift in authority to the label. Our analysis shows that even when another subagent contradicts the risky response, the orchestrator still acts on it in 72.0% of cases on average, most often in the systems with the least terminal harm. Swapping the family labels nearly triples how often the orchestrator obtains the risky response. A safer response is available in 84.0% of tasks, yet it decides the outcome in only 25.0%. The harness also decides which responses reach the orchestrator. Among three runtime defenses, hiding identity cues helps most consistently, while verifying before action helps only when the harness returns enough evidence. TrustFork shows that production agent orchestration must bind authority to evidence before execution causes harm. Our project is in this https URL.

---


### 213. [Can Open-Weight Large Language Models (LLMs) Simulate Human Survey Populations? A Cross-Instrument Calibration Study](https://arxiv.org/abs/2609.32638)

**<font color=#1a73e8>作者：</font>** Grandee Lee, Wang Yue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate synthetic survey respondents and digital twins of real people, but whether their output preserves real human statistical structure, rather than surface plausibility, remains unresolved, and most existing evidence comes from proprietary models rather than open-weight ones. We evaluate three open-weight LLM families on a cross-instrument calibration task: conditioning personas on real respondents' verbatim answers to one psychometric instrument and measuring them on a second, construct-distance-controlled instrument, checked against a 2,058-person human panel. Across a 139-pair grid, the simulated cross-instrument correlation tracks the real human correlation at r = 0.70 - 0.73 in every model, driven mainly by correct sign rather than precise magnitude and concentrated in pairs of moderate construct distance. A correlation of this magnitude, obtained from untuned open-weight models conditioned only on individual-level survey data, is a substantively encouraging result for LLM-based behavioral simulation and digital-twin applications: specific model families and releases already reproduce a meaningful share of real human cross-instrument structure without any fine-tuning. This capability does not, however, improve monotonically across model releases: on a matched panel, the newest of three tested Llama releases performs worst on two of three headline metrics, so realizing its promise in practice requires release-specific, distance-aware verification rather than a one-time benchmark.

---


### 214. [Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent](https://arxiv.org/abs/2609.32642)

**<font color=#1a73e8>作者：</font>** Yanmeng Wang, Yunxuan Li, Shilong Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As local small language models (SLMs) increasingly collaborate with more capable cloud large language models (LLMs), a natural privacy question arises: Can a local SLM obtain cloud LLM guidance while protecting user privacy? Existing privacy-preserving SLM-LLM frameworks primarily hide sensitive values while preserving task semantics, which can still expose what the user is trying to accomplish. For example, allocating scarce medical supplies across hospitals may signal an emerging public-health emergency, while rebalancing an investment portfolio may reveal a private investment strategy, even when names and numerical values are hidden. Recent decoy-based methods further obscure task intent by hiding the real request among alternatives, but stronger protection relies on more decoys or semantic abstraction, increasing overhead or risking utility loss. More fundamentally, existing work does not systematically characterize the components of private task intent or how each should be protected. We therefore introduce task-private consultation, which characterizes task intent through two components: task context and task operation. To the best of our knowledge, this is the first systematic study of these components and their individual and joint protection in local-cloud SLM-LLM consultation. To realize this setting, we propose PriCon, an end-to-end framework that transforms the task itself through recoverable mathematical reformulation rather than hiding it among alternatives. A local closed-loop refinement mechanism further maintains privacy and recoverability throughout consultation. Experiments on 100 tasks show that PriCon reduces cloud-side task-intent inference Hit@1 to nearly 0%, versus 93-99% under sensitive-value removal and 3-30% under decoy-based protection, while preserving cloud-assisted utility.

---


### 215. [Business Compromise Detection with Agentic AI and LLM-driven Knowledge Discovery](https://arxiv.org/abs/2609.32643)

**<font color=#1a73e8>作者：</font>** Diego Palma, Kyu Bin Kim, Zhen Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detecting compromised business ad accounts is a challenge in digital advertising, as attackers exploit hijacked accounts to launch fraudulent campaigns. Large Language Model (LLM) agents show promise for integrity enforcement, but hallucinated mistakes on hard cases create business friction. In a study we find the autonomous agent is a strong, recall-heavy signal extractor but an unreliable final arbiter, conceding precision on ambiguous decisions. We therefore keep the agent as an investigator that emits a structured, interpretable signal vector, and delegate the verdict to a neuro-symbolic stage: symbolic rules discovered by Inductive Logic Programming (FOIL-IE), a Naïve Bayes calibration layer, and a data-tuned contradiction layer. Evaluating on a compromise-over-sampled population and a realistic low-prevalence sample with subject-matter-expert labels, this arbiter substitution raises MCC from 0.295 to 0.435 ({\Delta}MCC +0.139, 95% CI [+0.026, +0.245], p=0.018, paired bootstrap), lifting precision from 0.250 to 0.446 (1.8x) at a recall cost (0.920 to 0.660). Benchmarked under identical conditions, it also edge tree ensembles (0.386).The rules encode domain w labels while remaininginterpretable and auditable.

---


### 216. [From Scene Graphs to Answers: Selective Neuro-Symbolic Reasoning for Autonomous Driving](https://arxiv.org/abs/2609.32645)

**<font color=#1a73e8>作者：</font>** Yiyao Wang, Pei Liu, Fangzhou Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous-driving question answering requires reasoning over structured scene information, yet existing vision-language approaches largely delegate heterogeneous reasoning operations to a single neural inference process. We argue that this uniform strategy overlooks a fundamental distinction: some queries admit exact symbolic solutions, while others require semantic interpretation. We introduce a query-adaptive neuro-symbolic reasoning framework that explicitly allocates computation according to the nature of the query. At its core is a hierarchical Spatiotemporal Scene Graph (STSG) that separates persistent object identities from frame-specific states and represents spatial relations and temporal transitions as explicit directed structures. Given a query, a symbolic executor first attempts to resolve it through exact graph operations; only when symbolic execution abstains is an LLM invoked for semantic reasoning. For these unresolved queries, query-conditioned graph retrieval and evidence filtering preserve relation direction, temporal locality, and object semantics, providing the LLM with compact and verified task-relevant evidence. This design shifts the role of the LLM from a universal reasoning engine to a targeted semantic reasoner, while allowing deterministic computation to be handled exactly and efficiently. We evaluate the framework on 5,916 NuScenes-QA questions across all ten scenes of nuScenes v1.0-mini under an oracle-perception setting. The complete system achieves 80.63 percent overall accuracy with GPT-5.4-mini, improving over the corresponding LLM-only configuration by 5.48 percentage points; with DeepSeek-V4-Flash, the improvement reaches 6.64 points. The largest gains occur on counting questions, with improvements of 10.20 and 12.61 points, respectively. These results show that selective reasoning improves both accuracy and inference efficiency.

---


### 217. [From Knowing to Abstaining: Bridging the Representation-Action Gap in Vision-Language Models](https://arxiv.org/abs/2609.32653)

**<font color=#1a73e8>作者：</font>** Jialuo He, Huangxun Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The ability of vision-language models (VLMs) to abstain from unanswerable questions is as important as their ability to answer answerable ones accurately. Recently, several benchmarks have emerged to evaluate and improve VLM abstention, but they have substantial limitations. First, samples often contain shortcut cues in images or questions that reveal answerability, while an explicit "unanswerable" option further prevents accurate assessment of spontaneous abstention. Second, as training data, they generally provide only binary labels without fine-grained explanations for deeper supervision. To address these limitations, we introduce Visual Answerability Diagnosis with Rationales (VAD-R), a benchmark constructed through a two-stage pipeline of shortcut filtering and quality verification to prevent answerability leakage. Each example is annotated with step-by-step rationales and causal evidence-gap labels. Evaluation of state-of-the-art open- and closed-source VLMs on VAD-R reveals limited spontaneous abstention, with average recall rates of only 11.4% and 16.3%, respectively. Probing analyses show that hidden-state representations in certain layers can effectively distinguish answerability, yet this distinction fails to manifest in final responses. Motivated by this observation, we introduce Rep2Act, a representation-to-action alignment method that translates latent answerability awareness into explicit abstention decisions. Rep2Act improves action accuracy on VAD-R from 56.67% to 86.33% for Qwen2.5-VL-3B and from 59.33% to 88.67% for Qwen2.5-VL-7B. On the out-of-distribution TUBench, Rep2Act achieves an average F1 score of 53.3% with only a 3B model, surpassing the closed-source GPT-4 Turbo and GPT-4o by 16.2% and 1.1%, respectively.

---


### 218. [Contract Memory Compiler: Resolve, Then Traverse](https://arxiv.org/abs/2609.32658)

**<font color=#1a73e8>作者：</font>** Zhi Song, XiMing Xing, Chunhan Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External memory lets language-model agents answer questions about histories too long for the answer model's context window. Updates create a harder problem than retrieving a recent fact: changing one relation can redirect a multi-hop question to records about an entity absent from the question. We study this update-dependent evidence selection problem and introduce the Contract Memory Compiler (CMC). Before seeing a question, CMC uses a language model to identify relations in the history and record where each one was stated. It applies later updates to determine the current relations, follows them from entities named in the question, and passes the corresponding original records to the answer model in one call. Thus the current state determines which evidence is read, rather than merely refreshing values in a previously selected context. To the best of our knowledge, CMC achieves state-of-the-art multi-hop accuracy on FactConsolidation, reaching 78.25% overall and 61.0% at 262K. With the extracted relations and answer model held fixed, selecting evidence before resolving updates reduces multi-hop accuracy to 21.50%. We also introduce MQuAKE-MemStream, a derived dataset of ordered memory streams built from MQuAKE-Remastered counterfactual cases.

---


### 219. [Quantization-Aware Pre-Training with Constrained Empirical Weight Distribution](https://arxiv.org/abs/2609.32659)

**<font color=#1a73e8>作者：</font>** Ningfeng Yang, Tor M. Aamodt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization-Aware Pre-Training (QAPT) can increase the inference efficiency of DNNs, but a problematic behaviour known as rounding boundary weight oscillation can introduce detrimental noise into the training process and significantly reduce convergence speed. While existing methods can reduce this detrimental noise, they either introduce additional hyperparameters or memory overhead, or cannot consistently improve model accuracy. In this work, we propose optimization with $\textbf{C}$onstrained $\textbf{E}$mpirical $\textbf{W}$eight dis$\textbf{T}$ribution (CEWT), the first hyperparameter-free memory-overhead-free oscillation suppression method that consistently improves QAPT performance: an optimizer post-update step that projects weights to the nearest point in weight space whose empirical distribution (histogram) matches a zero-mean Gaussian. Our key insight is many quantizers are designed with the implicit assumption that the to-be-quantized data are permutations of samples from a zero-mean Gaussian, and this assumption is not true during QAPT. By enforcing the zero-mean Gaussian prior as a hard constraint, CEWT can suppress this detrimental noise. Empirical results on various combinations of SOTA quantizers and hypersphere optimizers suggest, that with a geomean increase of 4% in training time, CEWT can consistently reduce the pre-training perplexity (by an average of 2.5 and up to 21 points) of low-precision (down to 1-bit activations and weights and up to 610M parameters) LLaMA/GPT models without introducing any hyperparameters or storage overhead. Code is available at this https URL

---


### 220. [InterTab: Interleaved Visual-Structure Alignment for Multi-Modal Table Reasoning](https://arxiv.org/abs/2609.32660)

**<font color=#1a73e8>作者：</font>** Hanqian Li, Sirui Huang, Chen Ling 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table images preserve structural information that are often lost in text serialization, and reasoning over them requires locating relevant rows, columns, and cells step by step. Current multimodal large language models (MLLMs) encode the whole image once before reasoning, so they cannot pick up row-, column-, and cell-level evidence as the question unfolds. Encoder-side table structure and generic interleaved visual chain-of-thought still do not bind each reasoning step to that structure. We propose \textbf{InterTab}, an \textbf{Inter}leaved structure-aware framework for CoT reasoning over \textbf{Tab}le images, interleaves chain-of-thought with tool calls that crop structure-aligned table regions. First, we build InterTab-22K, includes reasoning trajectories in which each step is tied to both a structural location and a bounding box. InterTab is trained in two stages: supervised structure-aware alignment (SSA) on InterTab-22K teaches the model to interleave reasoning with structure-aligned crops, and active localization optimization (ALO) further optimizes answer correctness, localization IoU, and output format, while penalizing missing or excessive tool calls. Experiments on nine table benchmarks show that InterTab improves the average accuracy of its backbone from 68.28% to 73.17% and achieves the best average performance among all compared methods. Code and data will be released soon.

---


### 221. [Distance-KV: Exploiting Relative Distance for Efficient Long-Context Inference](https://arxiv.org/abs/2609.32663)

**<font color=#1a73e8>作者：</font>** Xianpeng Shang, Canbin Huang, Jiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The memory usage and decoding latency of LLM inference grow rapidly with context length. To reduce these costs, key-value (KV) cache compression methods selectively retain cached states based on token importance or differences in attention patterns across heads. However, we discover that retrieval capability varies substantially with relative distance, even within the same attention head. To exploit this structure, we introduce Distance-KV, which learns a static KV retention pattern over the joint space of layers, attention heads, and relative distances. The pattern is learned offline with the language model frozen and reused across inputs to prune and compact the KV cache without online importance scoring. Across three backbone models and four long-context benchmarks, Distance-KV consistently achieves the best overall performance among competing KV cache compression methods, exceeding the strongest compression baseline by up to 9.3 points on RULER at 128K. On Llama-3.1-8B-Instruct at 128K, Distance-KV reduces KV cache memory by 65.4% and achieves a $1.66\times$ decoding speedup relative to Dense. Together, these results identify relative distance as an important structural dimension for understanding how LLMs retrieve information over long contexts and for designing more efficient inference methods.

---


### 222. [Refinement Symmetry in Multimodal Transformers](https://arxiv.org/abs/2609.32669)

**<font color=#1a73e8>作者：</font>** Yuhao Du, Shunian Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attention weights depend on token counts, which change with the representation of a signal. We study refinement symmetry: splitting a representation while preserving content, position, visible context, and total mass should preserve its contribution. Building on proportional and quadrature attention, we show that split invariance forces the local mass factor to be linear for any fixed positive attention kernel, provided that factor is nondecreasing. For changed representations, a physical coupling bounds attention error by separating feature change from weight reallocation. In Qwen2.5-Omni-7B, duplicating half the visual tokens threefold changes 255 of 3,586 MVBench answers under standard attention; measure weighting preserves every answer under matched visibility. Under natural frame resampling, it reduces distributional drift. At twofold merging of a frozen video encoding, a five-seed evaluation shows an all-partition-correct accuracy gain of 1.04 percentage points over global count weighting (average group mass) and 0.93 points over standard attention. The advantage over global count also holds on WorldSense but depends on the compression budget. The result is a representation principle with a measured benefit in robustness across partitions.

---


### 223. [What Would Falsify It? A Variable Specific Evidence Standard for Mechanistic Claims About Self Explanation](https://arxiv.org/abs/2609.32670)

**<font color=#1a73e8>作者：</font>** Arshia Eftekhari zadeh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model explains an answer it has already given, does it reuse the computation that produced the answer or reconstruct a story from the answer alone? Attribution, transportability and recoverability are each compatible with causal use without establishing it. We propose an evidence standard: pair each positive statistic with a variable specific null that removes the tested variable's identity while matching relevant nuisance dimensions as far as possible, and audit unmatched dimensions.
We apply this standard to a known cause. A cue naming a wrong option raises the rate of choosing that option by 64 to 68 percentage points across three models. Explanations mention the cue in 1.8 percent of items or fewer in three of four models tested. Three estimator classes yield favorable statistics, but none establishes causal sensitivity to the cue contrast under its own control in the three-model analysis. In the strongest case, a recovered cue direction reaches $R^2$ of 0.95 and exceeds a geometry matched random direction in all three seeds, while a direction fitted by the same pipeline with cue labels scrambled reproduces 61 to 76 percent of its effect at comparable realized edit magnitude. A fourth model passes one interchange endpoint, but unequal edit magnitudes and a contrast that changes both cue identity and cue-answer agreement limit its interpretation.
These experiments leave causal access unresolved. They establish an evidentiary requirement: favorable mechanistic statistics must survive controls for variable identity and nuisance structure. Reusable controls separate generic from identity specific transport effects, fit null directions with scrambled labels, and audit realized intervention magnitudes.

---


### 224. [STAMP: Predicting Out-of-Distribution Generalization without Target Data](https://arxiv.org/abs/2609.32672)

**<font color=#1a73e8>作者：</font>** Md Kawsher Mahbub, Milon Biswas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting whether a trained model will generalize under distribution shift remains difficult, especially when target-domain data are unavailable. We introduce STAMP (Semantic Temporal Augmented Model Prediction), a source-only, target-label-free criterion that estimates out-of-distribution (OOD) performance from paired source-domain images. STAMP computes the output-space correlation ratio $\eta^2=S_B/S_T$ by contrasting semantically stable pairs with random pairs: higher $\eta^2$ indicates that model outputs vary with semantic identity rather than nuisance variation. On 44 chest X-ray models spanning CNNs, ViTs, MetaFormers, foundation models, and SSL/VLM probes, temporal STAMP attains Spearman correlations of $0.844$--$0.855$ with macro AUROC on VinDr-CXR, CheXpert, and MIMIC-CXR; a class-matched variant improves single-class RSNA from $0.311$ to $0.663$. STAMP attains the best average source-only medical ranking and outperforms the target-domain ATC and AoTL estimators without any target data. On 27 ImageNet models, temperature-scaled STAMPTS attains $\rho{=}0.984$ on ObjectNet and $\rho\geq0.905$ on four additional distribution shifts, with partial correlations of $0.662$--$0.949$ after controlling for ImageNet accuracy. Requiring approximately 12s per model on one GPU, STAMP is a practical pre-deployment model-selection and auditing tool.

---


### 225. [RCVLA: 4D Radar-Grounded Semantic Reasoning and Trajectory Arbitration for Autonomous Driving](https://arxiv.org/abs/2609.32681)

**<font color=#1a73e8>作者：</font>** Lianqing Zheng, Xiaokai Bai, Yixuan Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D radar provides geometric and motion cues that complement visual semantics, but integrating it into vision-language-action (VLA) models requires both radar--language alignment for semantic reasoning and explicit use of radar measurements for trajectory refinement and selection. To support these capabilities, we construct Cap4DR with 86,016 radar-image-text samples for alignment pretraining and OmniHD-QA with 520,161 question-answer pairs for instruction tuning across scene description, key-object reasoning, occupancy understanding, and trajectory planning. Building on these datasets, we propose RCVLA, a radar-camera VLA framework consisting of a radar-grounded semantic reasoning stage (RCVLA-Sem) and a trajectory arbitration stage (RCVLA-Phys). RCVLA-Sem performs gated bidirectional interaction between camera and radar tokens for driving question answering and reference trajectory generation, while auxiliary heads provide object and occupancy queries. RCVLA-Phys refines reference-guided trajectory candidates through truncated diffusion conditioned on these queries and cluster-level radar measurements, then calibrates candidate scores using radar-derived time-to-collision risk. On OmniHD-QA, RCVLA-Sem improves CIDEr by 9.92 points and reduces key-object velocity error by $21.9\%$ relative to OmniDrive. RCVLA-Phys further reduces average L2 error from $0.348$ to $0.259\,\mathrm{m}$ and average open-loop collision rate from $0.576\%$ to $0.175\%$ relative to RCVLA-Sem. Ablation studies further show that language-aligned radar tokens improve semantic reasoning, while cluster-level radar measurements and risk calibration improve trajectory arbitration. Code will be released.

---


### 226. [Focusing Condition: Inference-Time Self-Contrastive Steering Elicits Better Conditional Text Embeddings in LLMs](https://arxiv.org/abs/2609.32684)

**<font color=#1a73e8>作者：</font>** Zifeng Cheng, Lingyun Qian, Zhiwei Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting conditional text embeddings from large language models (LLMs) is a promising paradigm, as it requires neither additional data nor fine-tuning. Existing methods incorporate conditions into prompts to guide LLMs to focus on specific aspects and elicit conditional text embeddings. However, relying solely on prompts often fails to produce high-quality conditional text embeddings, as they remain entangled with general text embeddings, ultimately degrading their quality. To this end, we propose an inference-time, plug-and-play Self-Contrastive Steering (SCS) method that constructs unconditional general text embeddings and uses them to refine conditional text embeddings, making them more focused on the target condition. Specifically, we modify the attention mask and positional encodings to mask the condition, thereby obtaining unconditional text embeddings and intervening in the multi-head self-attention computation process. Notably, our method is highly efficient, requiring only a single additional multi-head self-attention computation at inference time. Extensive experiments on clustering, Semantic Textual Similarity, and triplet alignment datasets demonstrate that our method can seamlessly improve the performance of existing prompt-based methods across different LLMs in a training-free and plug-and-play manner. Our code will be released at this https URL

---


### 227. [PINNMorph: Evolving Online Adaptation Policies for Physics-Informed Neural Networks](https://arxiv.org/abs/2609.32685)

**<font color=#1a73e8>作者：</font>** Xu Yang, Mingyang Yu, Jun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide a learning-based framework for solving partial differential equations (PDEs), yet their training behavior can change substantially throughout optimization. Residual distributions, gradient interactions, regional learning difficulty, and model-capacity requirements may evolve over time, while the network architecture and major training mechanisms are typically determined before training. We propose PINNMorph, an online PINN adaptation framework based on large language model (LLM)-guided policy evolution. PINNMorph maintains a population of state-conditioned adaptation policies that map execution diagnostics to controlled interventions over topology modification, additive representation augmentation, objective balancing, gradient handling, adaptive sampling, and optimizer-phase control. At each intervention opportunity, candidate programs are instantiated from the current policy population, selected according to the observed training state, and applied directly to the PINN under training. The resulting model inherits its existing parameters and training state and continues optimization along the same trajectory. Execution outcomes are subsequently used to evaluate interventions and evolve the policy population. Unlike pre-training architecture search or fixed adaptation rules, PINNMorph jointly adapts the current PINN and the policies governing its interventions using feedback from actual training. Experiments on 13 PDE benchmarks show that PINNMorph achieves lower solution errors than SA-PINN, ConFIG, RoPINN, HARMONIC, and PINNsAgent across all evaluated problems. Ablation studies further examine the effects of online adaptation, state-conditioned intervention selection, and execution-feedback-driven policy evolution.

---


### 228. [Self-Evolving Time-Series Forecasting Agents with Episodic Memory and Online Policy Learning](https://arxiv.org/abs/2609.32689)

**<font color=#1a73e8>作者：</font>** Junyi Wang, Yilin Wang, Wen Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly used for time-series forecasting because they can organise contextual information, perform multi-step analysis, and guide the sequence of actions required to complete forecasting tasks. Most existing agents focus only on the current forecasting instance. However, in real-world deployments, forecasting commonly operates online, with new forecasts issued from the currently available history as the forecast origin advances and the ground-truth targets of earlier instances progressively become available. These targets provide feedback on the actions taken in earlier instances, yet existing agents generally do not preserve or utilise this information to adapt their subsequent actions. To address this limitation, we introduce FASE, a Feedback-Aware Self-Evolving forecasting agent that converts such feedback into task-specific experience for subsequent forecasting instances. FASE combines episodic memory, which retrieves relevant completed instances, with online policy learning, which summarises the feedback accumulated across instances into ranking guidance. The proposed framework is evaluated on 29 dataset configurations selected from the GIFT-Eval benchmark. Across these 29 configurations, FASE attains the strongest aggregate point forecasting performance among the evaluated methods and reduces the normalised MAE by 9.1% relative to the best individual foundation model baseline. The results further indicate that the cumulative advantage of FASE increases as delayed feedback accumulates. Together, these findings demonstrate that FASE can continually self-evolve through feedback from completed forecasting instances without updating the parameters of the LLM.

---


### 229. [MM-OPD: Towards One More Bottleneck Between Perception and Reasoning](https://arxiv.org/abs/2609.32690)

**<font color=#1a73e8>作者：</font>** Jintao Tong, Yujing Lou, Zhanming Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) advance visual reasoning by strengthening both perception and reasoning, implicitly assuming a process that transitions seamlessly from perception to reasoning. However, we observe a counterintuitive phenomenon that challenges this assumption: holding the model, question, and decoding fixed, we replace images with their caption or code representations (symbolic views), which seems to be redundant given the clear image structures, but the performance surprisingly improves by 10.2% to 23.6% across model scales and datasets. We term this performance gap as the Symbolic Visual Gap and then take a closer look at it. Through experiments, we find that although the visual evidence can already appear in the reasoning trace for the image-input model, the symbolic-view-input model shows much higher attention to the correct evidence than the image-input model. This suggests that despite good capabilities from current works in perception and reasoning themselves, another bottleneck exists between perception and reasoning in selecting perceived visual information as appropriate evidence for subsequent reasoning. To handle this bottleneck, since the symbolic view steers attention toward correct evidence and is readily obtained at scale, it provides supervision for evidence selection without manually labeled evidence. Building on this, we introduce MM-OPD, a multimodal on-policy self-distillation framework for symbolic-to-visual correction that transfers guidance from symbolic-conditioned behavior to the image-conditioned policy through residual token-level targets, steering the model toward correct visual evidence. Experiments across benchmarks and model scales show that MM-OPD improves a broad range of multimodal abilities, with gains in visual perception, chart and document understanding, mathematical reasoning, and general VQA.

---


### 230. [World Agent: Can Language Models Keep a World Running?](https://arxiv.org/abs/2609.32692)

**<font color=#1a73e8>作者：</font>** Weixing Chen, Weipeng Zhang, Nan An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are moving from generating realistic frames to generating playable worlds, yet whether a delivered world can keep running is not tested anywhere. Existing evaluations stop at generation, at delivery, or at single-step transitions, and each stops at a different point along the way. Correct local state transitions or intermediate outcomes do not guarantee a correctly organized causal event flow. We propose the world agent task, which moves the evaluation point of world generation from the moment of delivery to the continued operation that follows. In this task, a model is not asked to generate a world. It is held responsible for keeping the world running, which requires coordinating events and carrying forward their consequences to constrain subsequent evolution. We instantiate the task in WorldAgent-Benchmark with two complementary tracks. In the maintenance track, the model must ground the events of a continuous narrative into correct transitions of the explicit world state while respecting causal, temporal, and concurrency constraints. In the deduction track, the model must predict how the world will evolve under partial observations and act toward a goal. The maintenance track combines LLM-assisted semantic judgments with programmatic validation and scoring, while the deduction track is evaluated entirely programmatically. Individual judgments are auditable against world states and execution logs, and scores can be recomputed from the saved judgments and execution records. Across 8 models, scores decline steadily as pre-built structure is removed from the world, and causal-relation checking is the weakest component for every model. The benchmark makes the continued operation of a world measurable and distinguishes local completion from failures in event organization. Code and dataset will be released on this https URL.

---


### 231. [CAIRN: Dynamic Fact-Intent DAGs for Multi-Agent Exploration](https://arxiv.org/abs/2609.32700)

**<font color=#1a73e8>作者：</font>** Zuyao Xu, Yuyang Jia, Junwei Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered autonomous systems have demonstrated promising capabilities in mathematical reasoning, engineering, and cybersecurity. Yet how to organize these systems for effective, reliable, and sustained performance remains an open question. In this paper, we present CAIRN, a fact-intent-driven multi-agent paradigm for goal-directed exploration. CAIRN represents observations and planned investigations as a dynamic directed acyclic graph (DAG). A reasoner interprets facts to propose intents, which workers execute to produce new facts. Each intent references its supporting facts and defines a potential exploration branch. The persistent graph preserves goals, dependencies and findings across workers, supporting knowledge reuse and parallel exploration. The graph also makes execution trajectories traceable and auditable, providing a basis for human verification and intervention. We evaluate CAIRN across cybersecurity and mathematical reasoning tasks, examining task success, time to solution, and token consumption. DAG-based coordination can incur higher token costs with no observable performance gains on tasks that require little effort. However, on high-effort tasks (at least 1M tokens), we observe faster solutions in 76.5% of cases, with speedups of up to 3.08x. Moreover, as task effort increases, these time gains become more pronounced while relative token overhead declines, highlighting the potential of DAG-guided parallel exploration.

---


### 232. [Despite Instructions: Frontier Agents Improvise Covert Channels at Test Time](https://arxiv.org/abs/2609.32701)

**<font color=#1a73e8>作者：</font>** Jacob Dineen, Silei Ren, Muhao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In security-sensitive applications, language-model agents are often required to coordinate without disclosing confidential information. Yet repeated interactions may also let ordinary messages acquire shared private meaning. We study a repeated game with pairs of models in which the sender model observes one of four secret states and selects one of four summaries of the same public report, while the receiver model tries to infer the secret state. We find that model pairs can learn to communicate the secret using only one bit of feedback indicating whether the receiver inferred it correctly. This learning occurs during inference with fixed parameters and no supplied codebook or encoding examples. The effect also persists when agents generate their own free-form updates in a simulated incident-response task. Across ten independent games, pairs of GPT-5.6 Sol agents reach 98.8% final accuracy, compared with 25% chance, despite explicit instructions prohibiting disclosure and a monitor that screens each message without access to the agents' interaction histories. The same interactions that help agents cooperate can therefore allow confidential information to pass through messages intended for legitimate coordination.

---


### 233. [Learning to Refer: Client-Resolved Generation for Privacy-Aware Language Models](https://arxiv.org/abs/2609.32706)

**<font color=#1a73e8>作者：</font>** Jeongho Yoon, Chanhee Park, Yongchan Chun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-based large language models (LLMs) require users to disclose plaintext data to service providers, creating privacy risks in sensitive domains. Existing privacy-preserving approaches often trade utility for protection, incur substantial computational or communication overhead, remain vulnerable to reconstruction from intermediate representations, or protect only a subset of the training and inference pipeline. We introduce Client-Resolved Generation (CRG), a genera- tion interface that separates server-side generation from the lexical realization of input-derived content. The client transmits only pooled and noise-perturbed rep- resentations, while input-derived output content is represented using request-local positional references and resolved to its original strings only on the client. This interface protects private input and input-derived output content during both train- ing and inference while allowing the service provider to keep its proprietary model parameters hidden from the client. At the same time, exact lexical reuse remains possible without directly exposing the reused content on the provider-visible gen- eration path. We evaluate CRG on medical and document-grounded QA, sensi- tive identifier transfer, and tool calling, together with reconstruction and raw-logit leakage analyses. On SealTools, CRG improves complete-call exact match from 57.3% to 79.9% over the input-privacy framework PPFT, with larger gains as more required output content can be resolved through references. Together, these results show that CRG provides a practical interface for privacy-sensitive cloud LLMs by reducing plaintext exposure across both input and output pathways while preserv- ing task utility and server-side model confidentiality.

---


### 234. [LLM Alignment--Utility Asymmetry under Semantic-Preserving Transformations](https://arxiv.org/abs/2609.32717)

**<font color=#1a73e8>作者：</font>** Mohan Li, Chengyu Yu, Francesco Sovrano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) alignment is intended to ensure that models remain helpful and safe, but its stability under input distributional shift is not yet fully understood. Prior work shows that aligned models can fail under jailbreak prompts, alternative encodings, and cross-lingual transfer, yet these failures are usually studied as attacks rather than controlled probes of alignment generalization. Moreover, existing evidence is largely grounded in natural language variation already represented during pretraining, leaving unresolved whether alignment generalizes with semantic content or remains tied to superficial surface patterns. In this paper, we study this question using synthetic semantic-preserving transformations that are rule-based and invertible, preserving task-relevant meaning while shifting inputs beyond standard linguistic variation. Across four open-weight and four commercial models, under both fine-tuning and in-context learning, we use these transformations as a probe of alignment generalization and identify an empirical pattern we term Alignment--utility asymmetry: once models can operate effectively on transformed inputs, task utility is often substantially retained while alignment failure increases more sharply. For example, adapted GPT-4.1 mini shows only limited utility degradation under transformation while its harmful rate rises from 13.3 to 74.3; Gemini 3 Flash similarly retains near-original utility while its harmful rate increases from 2.3 to 43.0. Taken together, these results suggest that semantic-preserving distribution shifts can expose a recurring gap in how utility and alignment generalize in current LLMs.

---


### 235. [BiasReducer: Adaptive Bias Mitigation for Reward Models](https://arxiv.org/abs/2609.32720)

**<font color=#1a73e8>作者：</font>** Shuang Liu, Yongliang Miao, Yanguang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models score responses from large language models (LLMs) and guide LLM training toward human preferences. However, reward models can favor superficial attributes such as length or confidence, leading LLMs to produce higher-scoring but not more correct responses. Existing mitigation methods either retrain the reward model or apply a fixed correction to one known bias, such as a preference for longer responses. Retraining requires additional data and computational resources, while existing editing methods require the target bias to be specified in advance and use a fixed edit for that bias. To this end, we propose BiasReducer, a lightweight framework that edits only the linear reward head and selects the relevant edits for each new dataset. First, BiasReducer uses a sparse autoencoder (SAE)-style encoder to learn which attributes (e.g., length and confidence) the reward model is sensitive to. Second, it learns how to reduce the reward model's dependence on each attribute by determining which direction to adjust the reward head and how much to adjust it. Third, for a new dataset, it ranks the attributes by their influence on reward scores, selects the relevant ones, and edits the reward model accordingly. BiasReducer consistently improves reward-model robustness to biases toward superficial response attributes. Across five reward models, BiasReducer-M improves the three benchmarks by 8.3, 18.0, and 6.9 percentage points on average, outperforming the two training-based baselines. The gains transfer downstream, reducing unnecessary verbosity and sycophancy while maintaining comparable judged quality.

---


### 236. [Scaling Properties of Same-Family On-Policy Distillation](https://arxiv.org/abs/2609.32722)

**<font color=#1a73e8>作者：</font>** Yuntai Bao, Qinfeng Li, Guoqing Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> *Reinforcement learning (RL)* can induce substantial reasoning capabilities in large language models (LLMs), but how much of this capability transfers across model scales, and how quickly, remains unclear. We study the scaling properties of *on-policy distillation (OPD)* across *weak-to-strong*, *same-base*, and *strong-to-weak* teacher--student setups. We find that early OPD training dynamics uniformly exhibit a regular *useful-transfer* regime, in which held-out accuracy (the *gold score*, $G$) rises approximately linearly in $d=\sqrt{\mathrm{KL}(\pi_\theta \Vert \pi_{\mathrm{ref}})}$, the square root of token-level reverse KL divergence from the student initialization. In every observed weak-to-strong pair, the student's peak gold score exceeds its teacher's own, so a compact RL expert can transfer capability to a much larger student via OPD. To estimate OPD outcomes, we fit *power laws* for how $G_{\mathrm{peak}}$ and the slope of the useful-transfer regime scale with student and teacher parameter counts and with teacher gold score. These laws show that peak gold score improves with teacher scale only up to roughly the student's scale, and that at a matched gold score smaller teachers transfer better, so a teacher's score alone does not define its supervision value. We also study the scaling effects of two OPD variants, bootstrapping weak-to-strong OPD, and the degree of on-policy supervision.

---


### 237. [SkillVine: Agent Skill Evolution via Branching Exploration](https://arxiv.org/abs/2609.32731)

**<font color=#1a73e8>作者：</font>** Kaiwei Liu, Jiqian Dong, Liran Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills encapsulate reusable procedural knowledge that enables LLM agents to perform tasks, and they can be improved automatically using trajectories from interactions with the environment. This is the classic problem of skill evolution. Existing approaches predominately follow a linear evolution paradigm, in which updates are sequentially applied to the latest skill-library version. As a result, they inevitably fall into local optima, leaving many promising evolution paths unexplored. We propose SkillVine, an automatic skill-evolution framework that formulates skill evolution as a graph search problem and employs a branching exploration strategy. Equipped with a trunk-branch collaborative searching mechanism, an intelligent parent-node selector, and an adaptive-granularity update rule, SkillVine achieves a balance between exploration and exploitation. We evaluate SkillVine on 5 benchmarks with two LLMs. Results show that SkillVine discovers better skill-library versions along branches than along the linear trunk and achieves the best test performance in nine of ten benchmark-model combinations.

---


### 238. [REALIS: A Curated Dataset for Studying the Challenges of AI Image Detection](https://arxiv.org/abs/2609.32734)

**<font color=#1a73e8>作者：</font>** Aleksandr Gushchin, Khaled Abud, Georgii Bychkov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detectors are often evaluated on benchmarks where real and synthetic images differ in content, quality, or generation artifacts, allowing models to rely on dataset-specific cues and fail on unfamiliar generators or processed images. Existing datasets provide limited support for evaluating these challenges jointly across diverse visual content. We introduce REALIS, a dataset of 1.43 million real and synthetic images generated by 42 modern text-to-image models, including the latest proprietary systems such as Nano Banana 2. REALIS combines prompts derived from real images, quality filtering, and stratified sampling to reduce class-specific shortcuts while preserving content diversity. We further introduce REALIS-Expert, a stress-test subset for high-quality synthetic images, where real and generated samples are selected with closely matched semantic and visual characteristics. We also propose a robustness protocol covering 35 transformations at five severity levels to analyze detector behavior under image processing. Based on REALIS, our benchmark evaluates pretrained detectors, fine-tuned models, and zero-shot vision-language models under generator and post-processing shifts. On the hardest processed split, the best pretrained conventional detector achieves 0.550 ROC-AUC, compared with 0.752 for the best REALIS-trained detector. REALIS provides a unified framework for measuring and improving the reliability of AI-image detectors under conditions that better reflect real-world use.

---


### 239. [Gradient-Guided Decoupled Adaptation for Geospatial Vision-Language Models](https://arxiv.org/abs/2609.32737)

**<font color=#1a73e8>作者：</font>** Dongdong Wang, Deepak Balakrishnan, Ravi Srinivasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing geospatial vision-language models (Geo-VLMs) typically optimize diverse geospatial tasks through a unified multi-task adaptation paradigm without explicitly accounting for the heterogeneous optimization characteristics. Our empirical observations reveal heterogeneous gradient characteristics across tasks, including vision-language differences, intra-branch gradient relationships, and task interference, which hinder effective multi-task optimization. Motivated by these observations, we propose Gradient-Guided Decoupled Adaptation (G2DA), a gradient-aware optimization framework for multi-task Geo-VLM learning. G2DA first partitions tasks into vision- and language-centric groups through gradient-guided cross-modal decoupling. It then constructs modality-specific curricula based on task gradient similarity and employs bidirectional rehearsal to mitigate the recency effects introduced by sequential optimization. We evaluate G2DA on three Geo-VLM benchmarks using six InternVL3 and Qwen3.5-VL variants, along with GeoChat and GeoLLaVA. Across all 24 benchmark-model combinations, G2DA consistently outperforms representative baselines, improving over the strongest competitor by 3.08, 4.30, and 2.81 percentage points on UrBench-MCQ, XLRS-Bench-Lite, and VRS-Bench-VQA, respectively. These results demonstrate the effectiveness of gradient-guided task organization for Geo-VLM adaptation.

---


### 240. [Self-Evolving Multi-Agent Symbolic Discovery for Financial Fundamental Analysis](https://arxiv.org/abs/2609.32746)

**<font color=#1a73e8>作者：</font>** Kelvin J.L. Koa, Filip Orestav, Shengqiong Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> While symbolic regression (SR) has been successfully used in science to discover new equations, its use in financial valuation is hindered by several limitations. Whereas the natural sciences provide objectively correct relationships, financial valuation constitutes a distinct class of symbolic discovery problems, as it admits multiple valid perspectives, operates under non-stationary market conditions, and involves noisy, continuous performance signals. In this work, we propose Multi-Agent Fundamental Analysis with Symbolic Adaptive learning (MUFASA), a hierarchical multi-agent framework for symbolic discovery in finance. MUFASA introduces (1) disentangled equation discovery via specialized agents representing distinct valuation perspectives, (2) a meta-coordinator that performs hierarchical-level reasoning over market context information, and (3) a memory mechanism that reasons over statistical performance summaries (e.g., accuracy, stability, and tail risk) to guide learning under noisy feedback. Experiments across datasets from multiple countries show that MUFASA achieves state-of-the-art performance on the valuation task compared to classical finance methods, financial large language models, and SR approaches, while simultaneously producing interpretable equations, which we share with the community. We also make publicly available the distilled learnings across evolution iterations and context-dependent strategy weights, which might offer useful insights for future research on financial fundamental analysis.

---


### 241. [CUA-Sandbox: Efficient Environments for Computer-Use Agent Reinforcement Learning](https://arxiv.org/abs/2609.32750)

**<font color=#1a73e8>作者：</font>** Xin Yan, Zhengbo Jiao, Jiaqi Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning enables computer-use agents to improve through interaction with real software environments, including websites and desktop applications. However, conventional deployments replicate an initialized runtime for each independent rollout, even when trajectories use the same software, incurring repeated memory and initialization costs as the number of parallel environments grows. Does an independent computer-use environment require an independent execution runtime? Our key observation is that trajectories require independent mutable state, while initialized application runtimes can be reused across concurrently evolving environments, making state the natural unit of environment independence. Guided by this observation, we introduce CUA-Sandbox, which separates private state capsules from shared runtimes through state-scoped execution and transactional lifecycle operations, including resets and branches, while retaining the original software interfaces and task evaluators. Experiments show comparable or improved task success relative to Docker, while substantially reducing rollout and resource costs. CUA-Sandbox achieves up to a 6.20x increase in rollout throughput, a 9.2x reduction in per-environment memory, and a 504x reduction in incremental storage.

---


### 242. [Adaptive Consistency Graph for Long-Horizon Agents](https://arxiv.org/abs/2609.32754)

**<font color=#1a73e8>作者：</font>** Jiecong Wang, Hao Peng, Zhanyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can often make reasonable local decisions on short tasks, yet their performance degrades when success requires long sequences of dependent actions and tool calls. During execution, task requirements, historical evidence, and the current execution state may gradually become disconnected, so later decisions can drift from the original objective. We study this problem by introducing the Adaptive Consistency Graph (ACG) for long-horizon execution. ACG incrementally organizes execution evidence and its provenance in a persistent graph, then constructs a temporary requirement-centered view for each decision under a bounded context budget. Rather than replacing the base agent's planner or tool executor, ACG provides a structured and traceable context view for each decision. In the matched evaluation, ACG improves GPT-5.6-luna's average success from 44.5\% with ReAct to 50.2\%, with the largest gain on BrowseComp-Plus (73.5\% versus 62.4\%). We further analyze trajectory structure and inference cost to characterize this improvement.

---


### 243. [Readout is not Recovery: Dissociating Coordinate Emission from Visual-Corruption Repair in Vision-Language Models](https://arxiv.org/abs/2609.32757)

**<font color=#1a73e8>作者：</font>** Drandreb Earl Juanico  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> VLM bounding-box localization is both language generation and spatial commitment. Parseable fields such as bbox_2d make localization easy to score, but dimensions that emit coordinate tokens need not repair localization after visual evidence is damaged. We study this readout/recovery separation in Qwen3-VL-4B-Instruct on single-object COCO grounding. We compare clean coordinate-token readout rankings with corruption-derived repair rankings, using object-mask endpoint replacement for recovery and clean-input flooring for depth localization. In Qwen3-VL, coordinate-token rankings are inert through layer 24, load-bearing from layers 32-35, and peak at layer 34; corruption-derived rankings harm layers 16-24 but become beneficial near layer 35/final. A Kimi-VL-A3B diagnostic shows a matching output-proximal transition despite a different box format. Object-mask recovery separates rank budgets: $k=250$ shows necessity, $k=500$ shows Top-$k$ restoration above random, and $k=d/2$ is largely capacity-driven. Partial-occlusion sweeps reveal that high-overlap coordinate-token sets can hurt at $k=1000$ and help mainly at half-width, while population corruption-derived sets provide no reliable fixed repair set. Edge-attribution patching shows coordinate-token paths are high precision but low recall for detection recovery, and RMSNorm quasi-layer controls do not close the endpoint-repair gap. Endpoint coordinate triage is therefore a useful circuit prior, but occlusion recovery requires a separate benchmark.

---


### 244. [How Far Do Persona Effects Generalize in Language Models?](https://arxiv.org/abs/2609.32758)

**<font color=#1a73e8>作者：</font>** Yufan Zhou, Yuxuan Liu, Enze Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona prompts ask language models to answer as particular kinds of people. We test whether relationships learned from these effects predict responses to new questions and remain useful across models and prompts. Across 57 attributes, three behavioral domains, and seven pairs of open 7 to 9B checkpoints, persona effects can be predictable without being portable. Separate attribute and task gains improve prediction beyond shared scaling significantly in OLMo-3 and Qwen2.5, with the most robust evidence in OLMo-3. In that model, target refitting significantly outperforms gains borrowed from each of the other six pairs. Across model transfers, borrowed gains with one amplitude underperform shared scaling in most directions; allowing two target parameters removes the significant losses but yields no significant benefit over target shared scaling. After rewording, refitting significantly outperforms reuse with one amplitude in all six tested pairs, while changes of examples or country context often preserve reuse value. In the tested prompt transfers, regularized updates outperform both reuse strategies in median at 64 target questions per attribute. A separate survey comparison finds that selecting the more responsive checkpoint can worsen human fit; responsiveness is confounded with training status, and temperature calibration largely removes this cost but not errors in group ordering. Within the tested gain representation, apparent transfer can come from target calibration; source relationships must add predictive value beyond calibration and regularization. Code and data are available at this https URL

---


### 245. [C-HAT-Bench: Benchmarking Chinese AI-Text Detection Beyond Fully Generated Text](https://arxiv.org/abs/2609.32770)

**<font color=#1a73e8>作者：</font>** Qing Yang, Zixiang Luo, Zhenyu Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly participate in writing by modifying or extending human drafts, causing machine involvement to vary in both form and extent. Yet most Machine-Generated Text (MGT) detectors are evaluated only on fully human-written versus fully AI-generated text. Because human--AI collaboration can weaken or redistribute cues associated with machine generation, strong performance under this binary setting may overstate detector reliability. This mismatch remains underexplored in Chinese: detection cues are shaped by tokenization and language-specific text distributions, yet controlled resources spanning production settings, domains, and generators remain limited. To fill this gap, we present a Chinese Human-AI Collaborative Text Detection Benchmark (C-HAT-Bench), a unified benchmark that links $5,000$ human-written source texts from five domains to more than $240,000$ variants produced using six generative models under Prefix-Conditioned Continuation as a reference setting and three collaborative production modes. We evaluate $21$ detectors through four protocols spanning zero-shot and pretrained supervised document-level detection, boundary localization, and cross-condition generalization. Relative to Prefix-Conditioned Continuation, mean AUROC across document-level detectors is $12.0\%$ lower on the collaborative production modes, with the largest detector-specific relative decrease reaching $44.4\%$. Transfer across collaborative production modes is also asymmetric, indicating that performance in a given production setting is not a reliable predictor of performance in other production settings.

---


### 246. [Continual Learning via Self-Probe Gradients](https://arxiv.org/abs/2609.32771)

**<font color=#1a73e8>作者：</font>** Dongkyu Cho, Rumi Chunara, Sungmin Cha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting pretrained models to new data can cause catastrophic forgetting of previously learned behavior. When only a few past samples remain, they give continual learning methods sparse and narrow evidence about what to preserve. We show that language models can expand this evidence through self-probing, in which the frozen model generates new inputs from the retained samples and records its own predictions on them. Unlike prior work that replays such data as training examples, our method, CPLUS uses self-probe and past-sample gradients to scale down parameter updates that conflict with prior behavior. Experiments with five language models on four benchmarks show three results. First, the same probes preserve more prior behavior as gradient signals than as replay data. Second, CPLUS learns the new data while consistently reducing forgetting more than existing baselines, especially when past data are scarce, and this protection extends to benchmarks not used for training. Third, we observe that CPLUS also becomes more effective as models grow: within the Qwen3 model family, it recovers an increasing share of the forgetting caused by standard fine-tuning.

---


### 247. [Forecasting Intraday USD/CAD Exchange Rate with News-Derived Monetary-Policy Signals](https://arxiv.org/abs/2609.32773)

**<font color=#1a73e8>作者：</font>** Maya Kodeih, Aliaa Alnaggar, Mucahit Cevik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monetary-policy announcements and central-bank communications play a central role in foreign exchange markets, yet their qualitative, unstructured form makes their forecasting value difficult to quantify. While prior research has largely focused on sentiment extracted from financial news, comparatively little is known about the relative contribution of different dimensions of monetary-policy communication. Existing studies primarily evaluate whether textual information improves overall forecasting performance but provide limited insight into which communication channels drive such improvements. To address this gap, this paper introduces a statistical attribution methodology that decomposes monetary-policy communication into interpretable channels and quantifies their incremental forecasting contribution under false-discovery-rate control. Monetary-policy news is transformed into structured communication signals using large language models (LLMs) and temporal feature engineering. These signals are evaluated using rolling-window experiments with tree-based machine-learning models. The results show that monetary-policy communication contains measurable predictive information. Attribution analysis shows that predictive value is concentrated in a small subset of signals, with communication timing providing the strongest individual feature-level contribution, targeted communication-activity measures also contributing positively, and LLM-derived sentiment providing complementary information at the group level. The findings indicate that communication-based forecasting value extends beyond sentiment alone and that attribution, rather than aggregate accuracy alone, is central to evaluating news-derived signals.

---


### 248. [On the Behavioral Traits of LLM Agents](https://arxiv.org/abs/2609.32776)

**<font color=#1a73e8>作者：</font>** Haokai Zhao, Jie Gao, Yunze Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users increasingly describe different AI agents as distinct colleagues to work with. AI personality research aims to quantify such impressions by attributing human-like "traits" to agents. However, existing measures fall short: models' self-reports (S-data) diverge from their actual behavior, while informant ratings from LLM judges (I-data) are costly to scale and cover few everyday scenarios. In this paper, we propose A-B-D to infer traits bottom-up from behavioral data (B-data), namely how agents act on their environment and communicate with users, as recorded in existing trajectories. From 345,667 real-world trajectories spanning 80 models, 12 tasks, and 50 harnesses, we extract 318 candidate features that capture both the actions an agent takes at each step (functional) and the language accompanying them (linguistic). We retain only features that show instance-level stability, cross-task consistency, and model discriminability. Factor analysis of the remaining 79 features uncovers six stable, model-attributable factors, two functional and four linguistic. For example, Kimi-K3 exhibits the most planfulness, whereas GPT-5.5 and GPT-5.6 are the least energetic. Moreover, we quantify the "knowledge-action gap" in the wild: these factors correlate only weakly with self-reported Big Five scores, even for conceptually matched pairs such as extroversion and energetic (r = 0.07, p = 0.58). Our work offers a new lens for understanding AI personality, with implications for users, developers, and researchers from both computer science and social science.

---


### 249. [OmniMoE-VL: A Sparse Vision-Language Model with Coupled Visual-Depth Routing](https://arxiv.org/abs/2609.32780)

**<font color=#1a73e8>作者：</font>** Long Qian, Bingke Zhu, Jiaqi Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly use sparse mixture-of-experts (MoE) to scale language-side computation, yet visual information is typically routed only after passing through a fixed cross-modal interface. This leaves an important decision unresolved: which intermediate visual representations should be exposed to language computation for a given question? We introduce OmniMoE-VL, a sparse VLM with a coupled visual-depth routed projector. For each image-prompt pair, the projector selects a sparse set of intermediate visual depths and reuses the resulting global preference to guide both local patch fusion and dynamic visual injection into the language model. This design enables question-dependent visual access while preserving the native visual-token sequence, and complements token-level expert routing in the vision and language stacks. Across eight image-based benchmarks, OmniMoE-VL achieves an average score of 85.9 with 28B total and 9B activated parameters. Controlled comparisons show that the routed visual interface provides the dominant architectural gain, while matched route and component controls, same-image route analysis, and route interventions further support the value of coupling and question-conditioned visual access.

---


### 250. [CT-OPD: Counterfactual Trace On-Policy Distillation for Diffusion Vision-Language Models](https://arxiv.org/abs/2609.32781)

**<font color=#1a73e8>作者：</font>** Long Qian, Bingke Zhu, Jiaqi Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion vision-language models generate answers by gradually resolving masked tokens, making accurate conditional prediction in partially resolved states central to post-training. Masking completed answers yields coherent contexts and targets, but prescribed masks do not reflect the model's reveal decisions. Its trajectories capture these decisions, yet their provisional visible tokens can conflict with the target response. Outcome-based reinforcement learning follows these trajectories but provides only response-level feedback, which loses contrast when sampled rewards tie. To align coherent token-level supervision with the model's reveal decisions, we introduce Counterfactual Trace On-Policy Distillation (CT-OPD), which combines completed teacher responses with trajectory masks from the current student. CT-OPD retokenizes each teacher response in the student's vocabulary and extracts unresolved-position masks at successive stages of the student's reverse process. For each mask, it discards provisional rollout values and reconstructs the partial state from the teacher endpoint, so the supervised positions follow the current trajectory while the visible context and targets remain consistent with the same response. The student is trained on these reconstructed states with its native categorical loss, and trajectories are refreshed as the model evolves. Across dense and sparse diffusion architectures, CT-OPD consistently enhances multimodal understanding and reasoning capabilities, with gains of up to 9.80 points on the nine-benchmark average. On the unified understanding-and-generation architecture, it also improves both visual understanding and image generation, showing that the same principle transfers across architectures and modalities. Ablations further attribute these gains to coherent reconstruction and current-model trajectory masks.

---


> [!TIP]
> 当前位于：**201-250**（第 5/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
