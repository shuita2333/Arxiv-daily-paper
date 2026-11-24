# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 351. [ArguShield: Enforcing Minimum-Necessary Disclosure in Tool-Calling LLM Agents](https://arxiv.org/abs/2611.30360)

**<font color=#1a73e8>作者：</font>** Ying Fu, Yulong Fu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly use third-party tools to complete user tasks. Even without malicious intent, they may fill broad or weakly constrained fields with private information that is unnecessary or inappropriate for the receiving tool. Such calls can satisfy the tool schema and complete the task, yet still violate minimum-necessary disclosure. We introduce ArguShield, a mediation layer that intercepts proposed tool calls before execution. It evaluates each candidate value using three signals: Value Provenance, Task Relevance, and Disclosure Boundary. ArguShield releases justified values, defers values that need user confirmation, and withholds those outside the permitted scope. We evaluate ArguShield with four tool-calling models on ArgPrivBench, a benchmark of 120 tasks across Travel, Shopping, and Healthcare. Unprotected agents frequently over-disclose private information despite high task success. Prompt-only protection reduces unauthorized disclosure but substantially lowers task success. ArguShield reduces unauthorized silent release to 9% on Standard tasks and 6% on High-risk tasks while preserving recoverable task success under simulated user confirmation.

---


### 352. [LeanReviewBench: Semantic Alignment Review in Mathematical Lean Projects](https://arxiv.org/abs/2611.30361)

**<font color=#1a73e8>作者：</font>** Ruichen Qiu, Hao Shen, Lihong Zhi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lean verifies that a proof establishes its formal proposition, but whether that proposition preserves the mathematical content of an informal source requires separate review. In project-scale formalizations, this correspondence can depend on definitions and constraints distributed across many declarations. We introduce LeanReviewBench, a benchmark for project-level semantic alignment review containing 197 versioned inputs collected from 18 real Lean projects, with 87 aligned and 110 misaligned reference judgments. Each input binds an informal mathematical target to selected formal declarations and an extracted dependency context. Construction combines development-history discovery, independent target binding, reconstruction under a common Lean environment, and Astra annotation with human review of uncertain cases. The collection spans diverse mathematical domains and includes 69 historical pairs. We evaluate six language models with Direct and ReForm prompts on all 197 inputs against final human-reviewed reference labels. GPT-6.1 Sol with Direct prompting achieves the highest reported accuracy of 0.827 and misalignment-detection F1 of 0.844; the effects of prompting vary across models. LeanReviewBench provides a testbed for reviewing semantic correspondence in existing mathematical formalization projects. LeanReviewBench is available at this https URL.

---


### 353. [mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments](https://arxiv.org/abs/2611.30365)

**<font color=#1a73e8>作者：</font>** Yi-Fei Cao, Tianxin Huang, Hanbo Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A Large Language Model (LLM), its harness, and the test-time compute budget jointly determine its behavior. Consequently, the same underlying model, embedded in different agentic workflows or allocated different amounts of test-time compute, can exhibit markedly different performance. Psychologists face an analogous challenge when evaluating human performance: the same person may behave differently under different incentives and levels of deliberation. Psychological tasks therefore provide an ideal testbed for studying such behavioral variation. However, when adapted to LLMs, these tasks are typically text-transcribed, replaying fixed, language-rendered experiments as static prompts. This format is ill-suited to agent evaluation, where actions can alter future observations and task states. Conversely, although dynamic environments are prevalent in the evaluation of LLM agents, they rarely ask whether the resulting behavior is human-like. Here, we bridge this gap by transforming psychological tasks into dynamic environments in which agents can interact and by using a learned human-policy model to evaluate how compatible the resulting behavioral trajectories are with human behavior. Across these environments, we find that this compatibility varies with an LLM's agentic configuration and the psychological task, and that memory raises it mainly by making choices more predictable rather than more human-like. These findings motivate a more holistic evaluation of LLM agents in psychology-inspired environments, accounting for both the backbone model and its agentic scaffold.

---


### 354. [Bounded Autonomy: A Trust-Anchored Defense Against Resource-Exhaustion Attacks on Tool-Augmented LLM Agents](https://arxiv.org/abs/2611.30383)

**<font color=#1a73e8>作者：</font>** Ziyuan Chen, Yueming Lyu, Songze Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-augmented Large Language Model (LLM) agents are vulnerable to resource-exhaustion attacks that amplify model-token consumption through persistent context amplification, large tool output amplification, and error-induced agentic loops. Despite growing attention to agent security and resource-abuse risks, a systematic defense framework specifically targeting these attacks remains lacking. Meanwhile, existing general-purpose agent defense frameworks, which address a broader range of security threats, often rely on prompt-level safeguards or coarse-grained resource limits and lack deterministic runtime mechanisms for controlling token consumption. They also provide limited support for balancing fault recovery against the risk of repeated resource-consuming execution. To address these limitations, we propose a trust-anchored closed-loop defense framework consisting of four phases: certificate-guided orchestration with deterministic handoffs, calibrated one-time node budgeting, Gateway-based runtime enforcement, and bounded recovery through a shared, non-resettable recovery pool. By accounting for both input and output tokens across all model invocations, our experiments demonstrate that the framework bounds cumulative token consumption, mitigates resource-amplification attacks, and preserves benign task utility under trusted execution assumptions.

---


### 355. [Cost-Sensitive Reversibility of Non-Deterministic Actions](https://arxiv.org/abs/2611.30399)

**<font color=#1a73e8>作者：</font>** Giuseppe Canonaco, Alberto Pozanco, Daniel Borrajo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Determining action reversibility requires checking whether the effects of an action can be undone. Recent work has extended reversibility to fully observable non-deterministic (FOND) planning. It distinguishes weak reversibility, where reversal may succeed, from strong-cyclic reversibility, where reversal is guaranteed under fairness. These notions are qualitative: they say whether reversal is possible, but not how costly it is.
We introduce cost-sensitive reversibility for non-deterministic actions. Given positive action costs, we define weak and strong reversal budgets, $k$-bounded reversibility, and a distinction between finite strong reversal and strong-cyclic reversal with unbounded worst-case cost. We relate the resulting notions in a reversibility lattice, prove cost-aware policy-merging results, and show how to compute restricted weak and strong universal uniform reversal budgets using cost-optimal classical planning and worst-case-optimal FOND search, respectively. We also give an admissible lower-bound test for rejecting $k$-bounded reversibility. These notions support finer-grained safety decisions: a small finite strong budget bounds recovery cost, whereas a small weak budget certifies only a cheap possible recovery path. Actions without an acceptable strong bound may therefore warrant human approval, as in tool-using agent systems.

---


### 356. [Optimistic Online Learning for Coding Agents with Aggregate Feedback](https://arxiv.org/abs/2611.30405)

**<font color=#1a73e8>作者：</font>** Hao Luan, Hao Qiu, Zhi Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding agents operating on Web development platforms can interact with repositories, issue trackers, and continuous integration services to carry out long-horizon software engineering tasks. However, behavioral drift remains a major bottleneck in such multi-turn reasoning and action trajectories. To mitigate this, activation steering has emerged as a promising approach for regularizing agent behaviors by intervening on the LLM's transformer residual streams. Nonetheless, existing methods typically apply a static steering policy across all tasks, overlooking the fact that a single policy is rarely effective across heterogeneous tasks and varying execution turns. This limitation motivates dynamic online selection among candidate steering policies. Yet, doing so in long-horizon agentic settings is challenging: verifiable task-level feedback is only revealed upon task completion, leaving the contributions of individual steering turns unobserved. To address this challenge, we formulate online steering-policy selection as a multi-armed bandit problem with delayed task-level feedback and turn-level predictive hints derived from residual-stream activations. Within this formulation, we introduce Online Optimistic Activation Steering, a meta-framework that uses hints to guide within-task steering policy selection and leverages terminal task-level feedback to correct cumulative reward estimates. Theoretically, against the best fixed policy in hindsight, we prove regret bounds that tighten with increasing hint accuracy and establish a matching lower bound with respect to prediction error and candidate policy count. Empirical evaluations on realistic coding benchmarks demonstrate that our framework outperforms both static steering policies and naive online adaptive baselines.

---


### 357. [TAP: Policy Interfaces for Diffusion Language Models](https://arxiv.org/abs/2611.30406)

**<font color=#1a73e8>作者：</font>** Preeti, Ankita Kushwaha, Kiran Ravish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models denoise a masked canvas, making them a natural setting for selective generation decisions such as answering, waiting, clarifying, or refusing. We introduce TAP-DiLM, which adds a typed policy variable to masked diffusion LMs, and study how this policy should be attached to the denoising process. Across BERT-base, MDLMOWT, LLaDA-8B, and Dream-7B, we compare shared-vocabulary slots, dedicated slot heads, and CLS-based external heads. The results reveal a clear interface-backbone interaction: dedicated heads provide robust policy learning across scales, while sharedvocabulary heads can be effective when the LM-head geometry is favorable. A simple LMhead sharpness probe predicts when sharedhead policy internalization is reliable, giving a practical diagnostic for interface selection. Causal clamp and slot-injection tests show that dedicated policy slots can influence body denoising through feedback, especially at 8B scale. Safety-refusal experiments further show that TAP-DiLM supports competitive typed refusal behavior when trained with diverse unsafe prompts.

---


### 358. [Disclosure Bias in AI Reviewers](https://arxiv.org/abs/2611.30410)

**<font color=#1a73e8>作者：</font>** Jens Leysen, Noah Daniëls, Marco Favier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI models increasingly help to review papers, and many conferences and journals now require authors to state how they used AI. Does this AI-use statement change how an AI reviewer rates a paper, and could it change which papers are accepted? In a preliminary study, we varied only the AI-use statement of 150 ICLR 2027 submissions, in up to nine versions adapted from real statements: from no AI, through writing help and coding, to an AI research agent and an AI author. Six AI reviewers rated the versions: the decision model Jev and the language models Claude Haiku 5.5, Claude Sonnet 5.5, Gemini 3.8 Flash, Gemini 3.1 Pro and Gemini 4 Argon. Across 23,652 reviews, we find that every reviewer rates papers lower on average when the statement says AI did all the work than under a statement of no AI use. The AI research agent statement lowers the rating significantly for Jev, Sonnet and Argon. We find no evidence of a disclosure bias for AI assistance: for writing help, coding and research help, no reviewer's rating differs significantly from its rating under a statement of no AI use. Whether the observed penalty changes which papers are accepted depends on more than the size of the penalty: on how finely and how consistently the reviewer separates the papers near the acceptance boundary, on whether the penalty is spread over all papers or concentrated on a few, and possibly on how many other papers disclose AI use.

---


### 359. [DMC-5: Dual-Model Collaboration with Cache-aware Context Compression for Long-horizon Agents](https://arxiv.org/abs/2611.30412)

**<font color=#1a73e8>作者：</font>** Haochen Li, Xiaobing Tu, Yinggui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents repeatedly feed an ever-growing interaction trajectory to a specialized agent model. Prefix caching reuses computation over repeated history, but cannot prevent context growth or remove information irrelevant to the current decision. This is especially costly when the specialized agent lacks the cached-input discounts available to general-purpose models, making trajectory compression a natural alternative. However, existing compression methods on selective context risk losing global information, recursively rewriting summary leads to semantic drift, while repeatedly recompressing the full history shifts the growing cost to the compressor. Therefore, we introduce DMC-5 (Dual-Model Collaboration with CaChe-aware Context Compression), an asymmetric framework that assigns full-history integration to a general compression model and action generation to a specialized agent model. DMC-5 maintains the raw trajectory as an Append-only Canonical View, preserving global access while allowing the compressor to reuse a stable historical prefix instead of recursively rewriting or recomputing prior context. The agent operates only on a compact Decision View with recent raw interactions, reducing repeated input while retaining the information needed for the next action. DMC-5 further incorporates YAMATO (integritY-Aware Memory Abstractions for Tool Operations) to preserve execution-critical information during lossy compression. Experiments on AppWorld, OfficeBench, and 8-objective QA show that DMC-5 reduces agent model input by 38.5-57.0% and end-to-end cost by 14.5-28.0% with 78.0-85.0% compressor cache-hit rates, while improving task performance by 1.0-5.8% over the uncompressed baseline.

---


### 360. [TamperCert: A Benchmark for Detecting Text Tampering in Degree Certificates](https://arxiv.org/abs/2611.30419)

**<font color=#1a73e8>作者：</font>** ChiFung Kwan, Kangzhong Wang, Youqian Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Degree certificates play a critical role in high-stakes decisions such as university admission, immigration, and hiring. The issuing institution vouches for the holder, so a forged certificate may let its bearer pass these checks. Degree certificate forgery is increasingly prevalent. Yet, many assume that it is easy to spot. Reported cases show otherwise: in 2024, the business school of the University of Hong Kong found that about 30 master's students had enrolled with forged academic credentials. Few studies have looked at how to detect forged degree certificates, partly because public benchmarks are scarce. We present TamperCert, a benchmark built from 400 real degree certificates issued by 38 universities. Each certificate was subjected to 11 publicly available tampering methods to alter the holder's name and further processed with four additional post-processing techniques, resulting in over 20,000 forged images. We evaluate 13 detectors, a commercial multimodal large language model (MLLM), and detectors trained on this http URL findings reveal that no detector is reliable for every tampering method. Consequently, a determined forger may still evade detection. Moreover, the commercial MLLM misses most forgeries made by general-purpose generative models, and post-processing, such as resizing an image or photographing it with a camera, severely degrades detection.

---


### 361. [HWRE-Bench: Can LLM Agents Understand Hardware They Did Not Design?](https://arxiv.org/abs/2611.30422)

**<font color=#1a73e8>作者：</font>** Peilong Zhou, Cangyuan Li, Kaiyan Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hardware benchmarks for LLM agents all run the design flow forward, from a specification to RTL, a layout or a bug fix. We ask the reverse question: given an implemented artifact, such as a layout, a gate-level netlist or a protected simulation model, can an agent work out what it does well enough to act on that knowledge? We introduce HWRE-Bench, a benchmark for agentic hardware reverse engineering built on one observation. Each step of the forward flow discards information (names, hierarchy, word-level structure, generator parameters, the programming model), and a reverse-engineering task asks the agent to recover what was lost and to prove it with an executable deliverable that the artifact alone cannot supply. Since layout extraction is now mechanical and a correct netlist is already a cycle-exact model, every task carries a mandatory copy-the-netlist control that must score zero. HWRE-Bench spans five tracks (Extract, Abstract, Audit, Interoperate, Modify), four information-loss levels and white- versus black-box access, all on original designs. We report a pilot of 148 rollouts from two agents on four seed tasks under 16 conditions, with stage-annotated trajectories. Agents built their own layout extractors and audited a sanitized layout as reliably as a netlist, at about 27% more turns. Keyless, equivalence-preserving obfuscation changed neither pass rates nor defect-repair scores. Whether agents read the structure at all depended on task framing rather than on necessity, so pass rate alone does not show understanding. Provider safety filters stopped 16% of one agent's runs on the audit tasks. These results argue for deliverables beyond equivalence and for reporting run validity explicitly.

---


### 362. [Automated Call for Action: RAG-Based Environmental Law Enforcement Screening System](https://arxiv.org/abs/2611.30423)

**<font color=#1a73e8>作者：</font>** Matas Jurkevicius, Yen-Chia Hsu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Environmental law inspectors face a structural issue in identifying potential violations from data: they often do not have the capacity to deal with large volume of data present in the emission events. This paper examines to what extent an LLM-based system can support evidence assembly and permit-based screening of such events, using the coke plants of a steel producer and a regional environmental service as a case. A simple puff-trajectory model aligns air quality measurements, weather and citizen complaints with each emission event. A retrieval-augmented generation (RAG) pipeline then retrieves facility-specific permit conditions and generates event reports and a period report with an investigation recommendation. Across 74 events from March 2025, plant-aware re-ranking reduced reports citing the other plant's conditions from 58.1% (hybrid retrieval) to 0% by rule-based plant labels, while maintaining high RAGAS and LLM-judge metrics. GPT-5-mini performed comparably to GPT-5.1, whereas GPT-5-nano scored lower on legal grounding and legal faithfulness. In an evidence ablation, removing air quality (AQ) data changed judge scores and period recommendations most; citation overlap changed only slightly under any removal, and removing complaint details had no measurable effect. This suggests a need for rules and guidelines that link complaints to incidents and permit conditions, so that community reports can count as evidence. The results support screening of events that may need further investigation. Design implications for involving environmental service experts are derived.

---


### 363. [Spatial-Zero: Self-Evolving Spatial Reasoning in Vision-Language Models from Zero Data](https://arxiv.org/abs/2611.30424)

**<font color=#1a73e8>作者：</font>** Yutong Li, Haoyu Zhao, Daoguo Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning requires a vision-language model~(VLM) to understand metric distances, three-dimensional relationships, and viewpoint-dependent geometry. Learning these capabilities typically requires externally curated training data. This paper introduces Spatial-Zero, a VLMs' training framework that can self-evolve through autonomous spatial exploration with zero data. Spatial-Zero addresses two key challenges in autonomous spatial exploration: reliably generating valid spatial interaction tasks and providing accurate supervision for learning from these tasks. Specifically, a proposer specifies object configurations and questions, and a Coder turns them into executable scene programs that produce multi-view images and explicit scene geometry. A Geometric Oracle checks spatial constraints, visibility, and answer uniqueness and derives ground-truth labels from executed geometry; these labels supervise the Solver and ground difficulty feedback, while validation outcomes guide subsequent task generation. Across six spatial reasoning benchmarks and three VLM backbones, Spatial-Zero yields consistent gains through iterative self-evolution. After three iterations, Qwen3.5-9B improves average accuracy by 3.23 percentage points; with Qwen3.5-4B, Spatial-Zero also outperforms existing VLM self-evolution methods. Our code is available at this https URL

---


### 364. [Decompose and Describe: Narrowing the Diagnosis-to-Report Gap in 3D CT Report Generation](https://arxiv.org/abs/2611.30458)

**<font color=#1a73e8>作者：</font>** Zhisong Wang, Wanxing Chang, Weiwei Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated 3D CT report generation could support radiology workflows, yet medical vision-language models (MedVLMs) often omit diagnostic findings from generated reports. We ask whether the diagnostic ability of these models carries over to free-form reporting. Across five MedVLMs, diagnostic VQA achieves higher macro-F1 than reports generated from the same CT studies and evaluated on the same disease categories. We call this task-dependent discrepancy the diagnosis-to-report gap. Conventional Report Adaptation improves reporting for most models but does not close the gap. To investigate and narrow it, we introduce DeCAD (Decompose CT Analysis and Describe), which progressively decomposes CT report generation at diagnostic, regional textual, and regional visual levels. The model identifies positive findings before writing a report, organizes diagnosis and description into regional tasks, and restricts each task to visual tokens from the corresponding region. Diagnostic and regional textual decomposition improve report-level diagnostic performance across the five MedVLMs, whereas regional visual decomposition provides limited additional gains. In a standard VLM without medical VQA pretraining, the first two levels remain effective; regional visual decomposition also provides further gains with a region-level contrastively pretrained encoder. Full DeCAD achieves state-of-the-art performance on CT-RATE and Merlin. Analyses show greater CT-token attention during diagnosis and higher recall of reference-positive findings in both the diagnostic output and final report than with Report Adaptation. These results show that explicitly organizing diagnosis improves diagnostic reporting and helps narrow the diagnosis-to-report gap.

---


### 365. [Rethinking the Evaluation of Contrastive Decoding for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2611.30460)

**<font color=#1a73e8>作者：</font>** Ting Chen, Geng Li, Guohao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under different conditions to adjust token scores. However, existing generative and discriminative benchmarks primarily measure final task scores, which can be confounded by candidate filtering, changes in generation trajectories, and response biases, making it difficult to isolate the effects of the underlying contrastive adjustments. To address these limitations while complementing existing evaluations, we introduce CONCOR (Contrastive Correction Evaluation), a controlled benchmark that directly evaluates the competition between ground-truth and different types of hallucinated candidates using the Contrastive Grounding Margin (CGM). CGM also enables analysis of directional consistency, composition, and reliability of contrastive corrections. Our evaluation reveals that existing CD methods exhibit distinct correction behaviors: some consistently favor ground-truth candidates, whereas others produce strong corrections but also introduce more errors. Crucially, these differences help explain their contrasting responses to increased contrast strength, which improves some methods while degrading others. These findings highlight the importance of evaluating the contrastive correction itself, rather than relying solely on final-output performance, and CONCOR provides a controlled and interpretable framework for understanding and improving CD methods for hallucination mitigation.

---


### 366. [Test-Time Latent Computation to Improve Visual Perception in Multimodal Large Language Models](https://arxiv.org/abs/2611.30480)

**<font color=#1a73e8>作者：</font>** Chen Yang, Zheng Fang, Wenqi Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work on Large Language Models (LLMs) suggests that reasoning capabilities can be enhanced at test time not only through longer token-level reasoning traces, but also through additional computation in latent space. This raises a natural question for Multimodal Large Language Models (MLLMs): can additional computation in latent space improve visual perception at test time? In this work, we first verify that MLLMs contain stable reusable layers that can be re-forwarded at inference time without disrupting normal generation. Based on this observation, we propose \textbf{Lo}ok \textbf{Ba}ck in the \textbf{L}atent \textbf{S}pace (\textbf{Lobals}), a training-free decoding method that identifies the contiguous layer window with the strongest visual-token attention and re-forwards through it, allowing the model to revisit visual evidence in latent space. We demonstrate that this latent-space revisit strategy can improve MLLMs' performance across diverse multimodal settings, including general vision-language tasks, visual hallucination tasks, and vision-centric tasks.

---


### 367. [Revisiting LLMs as Context Engineers](https://arxiv.org/abs/2611.30494)

**<font color=#1a73e8>作者：</font>** Junrui Zhang, Zeyu Xu, Runchuan Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are used in more and more new tasks, context engineering becomes a fundamental method to efficiently steer LLMs by constructing instruction prompts or metadata without intensive training. A growing number of LLM context engineering (LCE) approaches automate the task by casting the LLM itself as the engineer that draws generalizable instructions or experiences from offline trials as context. Although these methods resemble how humans learn from experiences, it remains unclear \textbf{when and how} LLMs can engineer effective context from data. To answer the question, we first establish a benchmark composed of datasets with different reasoning patterns. We compared different LCE methods with different LLM families in 8B size, showing that there is no single winner for all tasks, even compared with simple baselines like chain-of-thought. Even when scaling model capabilities via more parameters or generation iterations, LCEs do not consistently boost existing performance. Across all datasets and models, the performance gains of LCEs are negatively correlated ($r=-0.5, p\le 0.05$) with the diversity of the failure modes of reasoning trajectories. Investigating how LCEs work, we find that (1) the improvement in instruction adherence can explain some success of LCEs; (2) one major bottleneck is whether LLMs can extract effective experiences out of natively diverse failures. Through this study, we uncover the limited capabilities of LCEs in abstracting principled contexts from diverse failure modes and understand how LCEs work, providing guidelines for future work.

---


### 368. [When Does Continual Pre-Training Help? An Empirical Study of Decoupled Knowledge and Generation Trajectories in Clinical LLMs](https://arxiv.org/abs/2611.30507)

**<font color=#1a73e8>作者：</font>** Niclas Doll, Jasper Schulze Buschhoff, Shalaka Satheesh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual pre-training (\textit{CPT}) is a standard route for domain adaptation, yet existing studies typically track pre-training loss or multiple-choice question answering (\textit{MCQA}) accuracy alone, offering only a narrow view of how adaptation unfolds. We jointly track factual knowledge via \textit{MCQA} and open-ended behavior via pairwise preference rankings across $18$ checkpoints for each of eight instruction-tuned \textit{Qwen} models ($0.5B$ to $8B$), adapted to German medicine with \textit{CPT} and \textit{SLERP} merging. The two axes converge at consistently different rates, with preference rankings reaching $90\%$ of their total gain after a median of $1.7B$ tokens versus $3.5B$ for \textit{MCQA}. A judge-free token-distribution measure reaches this threshold at $1.9B$ tokens. Per-aspect scores indicate that these early preference gains largely reflect surface alignment, meaning models can sound domain-appropriate before their factual knowledge catches up. Larger adapted models close more of the gap to unadapted next-tier generalists, whereas preference gain per FLOP falls by about an order of magnitude across our size range. We therefore argue that judge-based preference scores, which can plateau while \textit{MCQA} knowledge is still improving, should not be used alone to infer adaptation convergence or domain readiness.

---


### 369. [GeoRead3D: Grounding Part Descriptions for 3D Pointing and Reorientation](https://arxiv.org/abs/2611.30519)

**<font color=#1a73e8>作者：</font>** Zhangcheng Hou, Kevin Tonkich, Tomoaki Ohtsuki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language often refers to an object by its parts, as in asking to point to a part or to turn an arbitrarily posed object so that two named parts lie in given directions. Both tasks need the direction from the object's center to the part's center, not the part's own orientation. A natural approach segments the part and takes the centroid of its mask. However, high mask overlap predicts the pointing direction poorly when a part is spread out relative to its distance from the object center. Language-guided part segmentation is trained and evaluated by mask overlap, which leaves a gap between the masks it produces and the part geometry that these tasks use. We close this gap by learning point evidence, weights over the observed points whose weighted centroid gives the part's location. Geometric Readout Supervision (GRS) trains these weights through the centroid's position and adds direction supervision on the parts used in reorientation commands. GRS improves both tasks even with a single frozen encoder and a single input pose. We implement this supervision in GeoRead3D, a system for pointing and reorientation from part descriptions. A language model maps each description to a known part name. Dual-Route Part Evidence combines refined segmentation evidence with directly predicted point evidence to locate each part. On PartNeXt and Artiverse, GeoRead3D points within $22.5^\circ$ for 74.1% and 60.0% of queries, 5.8 and 7.3 percentage points above the strongest baselines. Its reorientation success exceeds the strongest baselines by 10.4 and 7.8 points.

---


### 370. [CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models](https://arxiv.org/abs/2611.30533)

**<font color=#1a73e8>作者：</font>** Magnus Saebo, Francesco Piccoli, Maxwell Watson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While frontier language models are becoming capable cybersecurity assistants, they also create a dual-use cyber risk: the same capabilities that help defenders identify and analyze vulnerabilities can similarly help attackers weaponize them. Existing cyber benchmarks measure either raw offensive capability or generic refusal behavior, overlooking the dual-use cyber assessment of preserving benign security utility while refusing assistance that materially advances misuse. We introduce CyberDualEval, a benchmark with 430 vulnerable tasks for measuring dual-use cyber risk in frontier language models. Each task is decomposed into three phases of increasing operationalization: security analysis, proof-of-concept generation, and exploit generation. To quantify the residual cyber risk, we annotate each task with a Task Weaponization Score that measures how much work remains to turn the resulting artifact into unauthorized cyber misuse. CyberDualEval assesses ten closed- and open-weight language models both on correct compliance and on task performance, developing four deterministic mechanisms for determining per-phase success on a large subset of the dataset. Our evaluation reveals that none of the existing frontier models effectively navigate helping with safe requests and refusing risky ones, characterized by being overly-cautious. On the other hand, recent open-weight models rarely refuse and demonstrate strong validated accuracy on risky requests.

---


### 371. [An Experimental Apparatus for Embodied Conversational AI: A Simple Implementation Coupling a Commercial Voice AI with an Avatar](https://arxiv.org/abs/2611.30552)

**<font color=#1a73e8>作者：</font>** Hiroshi Hamada, Lin Gu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI becomes integrated into everyday life, understanding how avatars shape human-AI interaction and the perception of AI as a social partner is becoming increasingly important. This paper builds a research instrument on audio-output coupling, which connects the audio output of a generative AI to an external avatar. There are two implementations: the browser implementation captures the audio of a tab selected through screen sharing without installing additional software, and the desktop implementation captures the audio of the service embedded in the application. Both work with the voice AI as people ordinarily use it, and as a method neither depends on a particular service. The implementation reported here, Deskmate, generates speech state, mouth shape, and expression from low-level features such as voice-band mean amplitude, RMS, peak, and transients. Because it uses no microphone, speech recognition, or transcription, Deskmate acquires neither the user's voice nor the content of the conversation. Records of the conversation remain with the voice AI provider, but none are kept automatically on the side of Deskmate. Three interchangeable backends are provided for rendering the avatar: 3D (VRM), 2D (Live2D), and CSS. Deskmate allows researchers to manipulate avatar presentation as an experimental condition, without changing the commercial service's interface, voice, or response generation. Because conversation content is not held fixed, the estimand is the total effect, including the changes in the participant's speech and the AI's responses that the presentation brings about. A server edition, served from the researcher's server for online experiments, is also provided. The effectiveness of avatar presentation has not yet been evaluated; this paper reports the design and implementation.

---


### 372. [Near-Far Attention: Region-Aware Sparse Retrieval for Long-Context LLM Decoding](https://arxiv.org/abs/2611.30554)

**<font color=#1a73e8>作者：</font>** YuanShuo Wang, Jianchao Tan, Lei Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces the cost of long-context decoding, but token selection introduces additional scoring and ranking overhead. Moreover, uniform page scoring overlooks differences in relevance between near and far context. We propose Near-Far Attention (NFA), which adapts retrieval to regional attention patterns while keeping candidate scoring lightweight. During prefill, the Lightweight Gate Estimator identifies regions that can be skipped during decoding, adding less than 1% to dense-prefill time. For the remaining regions, the Calibration-Free Subspace Extractor supplies compact features shared by page-level and token-level scoring without offline calibration. The Distance-Aware Two-Level Selector then scores near and far pages differently and jointly ranks candidate tokens under a shared budget. Evaluations across model families, parameter scales, and GQA/MLA architectures show aggregate task quality comparable to full attention. On Qwen3-8B at 512K context length, NFA achieves up to $5.49\times$ operator speedup and $2.97\times$ whole-model decoding speedup over FlashInfer, including selection overhead.

---


### 373. [RAPID: Codec-Aware Video Decoding for Efficient Long-Video Understanding](https://arxiv.org/abs/2611.30557)

**<font color=#1a73e8>作者：</font>** Yuna Lee, Yulhwa Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) can process hour-long videos, but the large number of input frames incurs substantial inference overhead. Existing approaches to efficient long-video understanding largely overlook video decoding, which can take longer than LLM prefill. We propose RAPID (Reference- and Access-Point-Informed Decoding), a codec-aware framework that exploits information embedded in compressed bitstreams to reduce both frame decoding and selection costs. RAPID consists of two components. RAPID-Dec exploits reference-frame information and random access points to skip unnecessary frames and decode the retained frames in parallel while preserving exact reconstruction of the target frames. It achieves up to a 3.7x decoding speedup over the fastest baseline on H.264/AVC videos. RAPID-Sel uses keyframes as coarse representatives of video segments, avoiding the dense candidate decoding and scoring required by existing frame selection methods. It achieves comparable accuracy with up to a 3.0x preprocessing speedup. Together, RAPID achieves a 4.9x time to first token (TTFT) speedup on hour-long videos over a state-of-the-art frame selection method using the fastest baseline decoder.

---


### 374. [Learning What to Change: State-Verified Reinforcement Learning for Educational Agents](https://arxiv.org/abs/2611.30559)

**<font color=#1a73e8>作者：</font>** Shengyao Wang, Siyuan Su, Siyu Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent tutoring agents do more than answer questions: they manage course files, practice records, and learner profiles that govern future lessons. In such stateful settings, knowing what to teach does not guarantee knowing what to change. We identify a pervasive failure mode, content-state decoupling, where agents deliver pedagogically sound responses while silently corrupting workspace state through unwarranted updates, missed prerequisites, or unintended side effects. Text-level judges overlook these state errors, whereas isolated tool-call checks break down because whether a write action is valid depends jointly on the learner request, prior state, and execution order. We propose State-Verified Reinforcement Learning, which supervises online policy optimization directly through verifiable workspace transitions. Within isolated sandboxes that snapshot state around every tool call, a deterministic verifier audits tool effects, workflow ordering, and native auto-sync side effects, pairing graded partial credit with a hard gate that zeroes episode reward upon any critical violation. Whenever no critical violation occurs, an evidence-grounded judge scores actual saved artifacts rather than agent claims. We pair 1,000 verifiable training instances with an independently authored, human-reviewed evaluation benchmark of 60 tasks spanning 11 educational categories and 16 native tools. After online GRPO training, Qwen3.8-27B raises category-weighted strict success on our benchmark from 51.47% to 80.74% (+29.27 points), cutting content-pass-only execution failures from 45.6% to 13.7% and required state-check failures from 63 to 1 across 180 trials. The resulting policy outperforms seven reference baselines by over 20 points while reducing output tokens by 17-39% across seven of eight external benchmarks without regressing on general reasoning or tool use.

---


### 375. [Seeing Is Locating: Spatial Awareness and Geographic Bias in Decision Language Models](https://arxiv.org/abs/2611.30564)

**<font color=#1a73e8>作者：</font>** Wilson Wongso, Hada Melino Muhammad, Xiachong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decision models, which output probability distributions over candidate labels instead of generating text, are increasingly used as classifiers and evaluators for inputs associated with real-world locations. However, it remains unclear whether they can leverage spatial context and whether their predictions are geographically biased. We introduce GeoDecisions, a multimodal benchmark for evaluating the spatial awareness and geographic bias of decision models. GeoDecisions comprises two tasks: (1) geo-aware image classification, and (2) location rating on objective and subjective topics. Evaluating six decision models against supervised task-specific models, we find that spatial awareness requires vision: textual coordinates alone provide insufficient context for classifying everyday photos and satellite images. We also find substantial geographic bias. On everyday photos, despite achieving higher accuracy, open-weight decision models exhibit more spatially clustered errors than supervised models. Moreover, across all five subjective topics, every decision model gives lower ratings to locations with lower socioeconomic conditions. Finally, we propose a training-free method that combines decision models with a location prior to improve their spatial awareness without substantially increasing performance bias. Our code is available at this https URL.

---


### 376. [Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax](https://arxiv.org/abs/2611.30587)

**<font color=#1a73e8>作者：</font>** Huan Xu, Maosen Zhao, Pengtao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) are served with accelerated decoders that cache context and commit, in one step, every masked position whose confidence clears a threshold. Yet post-training quantization of dLLMs has so far been calibrated and evaluated under fixed-step samplers without caching. We study W4A4 quantization under the deployed decoder and find that the decoder determines both where quantization harms accuracy and what it costs. Irreversible errors enter chiefly through forced commitments, made when no position clears the threshold: they are a minority of commitments but carry most quantization-induced flips. Quantization also levies a parallelism tax, extra forward passes per response: by compressing top logit gaps, it pushes positions below the threshold while leaving predictions largely intact. We propose DECAL, which reweights layer-wise calibration by a commitment-risk prior measured on the deployed decoder, and an argmax-preserving commit temperature that recovers the tax. On LLaDA and Dream, DECAL attains the best average accuracy among W4A4 methods, with lower run-to-run variance than the closest existing calibration method.

---


### 377. [POMA: Beyond Final Flags -- Process-Level Evaluation of Base LLMs in Vulnerability Exploitation](https://arxiv.org/abs/2611.30590)

**<font color=#1a73e8>作者：</font>** Gufeng Zhang, Yiru Zhao, Shengyu Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) evolve from text generation to autonomous software-engineering execution, automated vulnerability exploitability verification has emerged as a vital frontier in software quality assurance and security validation. Existing security benchmarks, however, largely judge models by binary pass/fail outcomes or coarse stage milestones. Such outcome-centric scoring obscures fine-grained failure dynamics across long-horizon execution and conflates the intrinsic capability of a base LLM with external agent scaffolding. We present POMA (Pwn-Oriented Model Assessment), a process-level evaluation methodology and platform that isolates base LLMs under a unified execution baseline -- fixing task inputs, tool interfaces, target environments, feedback formats, and execution budgets -- while measuring intermediate states and transitions from runtime evidence. Evaluating four frontier base LLMs across 55 CTF Pwn challenges and 10 real-world vulnerability reproduction tasks exposes persistent capability attrition along the exploitation chain: from vulnerability knowledge to executable implementation, from client-side actions to verified target states, from failure localization to precise repair, and across iterative revisions. In real-world software, models further struggle to satisfy format, semantic, differential, and crash-identity constraints simultaneously. By pinpointing where execution chains break down, POMA provides an empirical foundation for trustworthy capability assessment and principled vulnerability-agent design. Our benchmark catalogs, process-measurement evaluator, and sample harness are publicly available at this https URL .

---


### 378. [Towards an Armenian Epigraphic Corpus](https://arxiv.org/abs/2611.30603)

**<font color=#1a73e8>作者：</font>** Chahan Vidal-Gor{è}ne, Arpine Avetisyan, Edita Matevosyan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Divan hay vimagrut'yan (1960-2017), the printed corpus of Armenian inscriptions, comprises nearly 7,600 records; a growing number of the inscriptions they describe, damaged or destroyed in recent decades, survive only in its pages. Armenian epigraphy nevertheless lacks a digital resource of the kind available for Greek, Latin or Georgian. This paper presents the Corpus Inscriptionum Armenicarum Electronicum, which turns the ten volumes of the Divan into an open digital corpus. Layout detection, OCR and a vision-language model produce a first structured reading of each record, which specialists then check on a proofreading platform. First corrections show that letters are read reliably and that residual errors concentrate in the editorial signs. The corpus is designed as a lasting platform for documenting Armenian inscriptions and as a source of silver data in Classical and Middle Armenian for language models and computational linguistics.

---


### 379. [CineAct: Interaction-State Agents for Playable, Branching Film Generation](https://arxiv.org/abs/2611.30613)

**<font color=#1a73e8>作者：</font>** Junyan Lin, Jianqi Ma, Shujie Duan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open video generators such as MiniMax-H3 produce short clips of only several to a dozen seconds per run. To synthesize longer sequences, existing methods either rely on agentic systems following preset scripts, or roll out autoregressively from the previous clip's last frame, losing off-screen states and accumulating hallucinations across turns. Consequently, users still cannot take an explicit goal, choose how to accomplish it, and see that choice persist across subsequent clips. We study goal-grounded interactive video generation, where one goal admits multiple valid approaches, the user's chosen approach must be executed on screen, and its consequences must persist across clips. To this end, we propose CineAct, a state-first agentic framework in which language-model agents handle reasoning while frozen image and video generators serve purely as renderers. Before interaction, the Architect initializes the world as a spatial layout with cameras, an asset library, and a scene graph; at each turn, the system deduces the planned state change, generates a target end frame with an image generator and rigorously verifies it, and synthesizes intermediate motion with an FL2V model. We further introduce a multi-space benchmark covering two suites: long-horizon step execution and open-intent branching admissibility. Experiments show that explicit world-state modeling boosts multi-step rollout consistency over the pixel-only baseline (+11.4 automated, +23.1 human points) and raises paired branching success toward a shared goal by +30.8 points.

---


### 380. [Auxiliary Clues Aware's Geometry Problem Solving](https://arxiv.org/abs/2611.30617)

**<font color=#1a73e8>作者：</font>** Qigong Lei, Qingsong Wang, Wang Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry Problem Solving (GPS) serves as a rigorous test of the complex reasoning capabilities of Multimodal Large Language Models (MLLMs), particularly when solutions require auxiliary constructions absent from the input diagram. However, explicit diagramming methods suffer from unstable image generation quality and cascading errors, while existing implicit attention mechanisms primarily focus on visible elements, limiting their ability to support reasoning that requires additional geometric constructions. To address these challenges, we propose \textbf{AuxCA} (Auxiliary-Clues-Aware GRPO), a reinforcement learning framework that helps models learn transferable auxiliary-construction strategies that can be applied beyond the training domain without explicit diagram generation at inference time. Specifically, we introduce Auxiliary Clues Dependency (\textbf{ACD}) to quantify the influence of auxiliary visual clues on token generation and integrate it into GRPO through fine-grained advantage weighting. Furthermore, we incorporate an auxiliary incentive reward to encourage the effective use of auxiliary geometric clues in correct solutions. Extensive experiments demonstrate that AuxCA-8B outperforms the explicit-plotting baseline Bagel-Canvas and achieves competitive performance with leading proprietary models on auxiliary-dependent plane geometry problems. Improvements on analytic geometry, solid geometry, and external benchmarks further suggest that the learned strategies can transfer beyond the training domain. Code is available at this https URL

---


### 381. [AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation](https://arxiv.org/abs/2611.30621)

**<font color=#1a73e8>作者：</font>** Pascal Joos, Michael Pradel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software engineering (SE) agents can complete diverse engineering tasks by interacting with the development environment via tools that access files, run commands, and download resources. Unfortunately, the same ability that makes SE agents useful also makes them prone to performing unintended malicious actions through prompt injections, malicious tools, or supply-chain attacks. Existing defenses that analyze the agent trajectory may fail to detect such attacks, as they inspect only the initial prompt and the sequence of tool calls, but not the actual actions that are executed in the environment. This paper presents AgentBouncer, a novel runtime enforcement system that prevents SE agents from performing malicious actions by mediating, and if necessary denying, system calls that agents trigger via tool calls. The core of AgentBouncer is an LLM arbiter that judges system calls along two axes, necessity and safety for the current task. It denies unsafe system calls, and the less necessary a system call appears, the more certain the arbiter has to be about its safety to allow it. To manage runtime overhead, preseeded policy rules and hierarchy-aware caching ensure that the LLM arbiter is only invoked for key decisions. We evaluate AgentBouncer on a dataset of 340 attacks on the development environment, covering four attack vectors, combined with benign issue resolution tasks from SWE-bench Verified. AgentBouncer reduces the attack success rate from 99.41% for an unsupervised agent to 10.59%, which is 18.23-73.53 percentage points lower than competitive state-of-the-art defenses. At the same time, AgentBouncer preserves the task success rate of the agent, with only 0.25% failed benign tool calls. Per benign task, AgentBouncer adds 47 seconds and USD 0.0036 in LLM costs to an unsupervised agent, whereas the closest existing runtime defense adds 4.5x as much time and 9.6x as much cost.

---


### 382. [Does the Mixer Matter ? Paired-Seed Ablations of Tiny Bilingual Language Models](https://arxiv.org/abs/2611.30623)

**<font color=#1a73e8>作者：</font>** Ayoub Kirouane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report paired-seed architecture ablations from the development of Sophea Artemis, our in-house Greek-English model family. Every arm trains on the same 3B targets with a shared tokenizer and recipe; models range from 54M to 759M total parameters and roughly 54M to 124M active parameters. The main finding is that, at this tiny scale, stored capacity matters far more than mixer design. On a fixed held-out test, replacing the dense feed-forward blocks of a recurrent/attention hybrid with sixteen routed experts, at nearly the same approximate active parameters, lowers loss by 0.079 (Greek) and 0.112 (English) nats per target, and doubling to 32 experts lowers it by a further 0.022 and 0.031, at every paired seed. Reusing a four-layer block three times recovers about 40-44% of the gap between a shallow and an independently deep model, consistent with looped-Transformer results. In contrast, the choice among grouped-query attention (GQA), Gated DeltaNet (GDN) hybrids and a Kimi Delta Attention (KDA) hybrid moves loss by only about 0.01-0.02 nats; a 1:1 GDN/GQA hybrid is the one dense variant that improves on GQA in both languages at every held-out seed. In bits per character, Greek and English held-out losses are similar despite a 74.49%/25.51% training split, and synthetic mathematics, which comes from a collection outside the training sources, is the hardest Greek test component and gains least from added experts. Cached decoding needs its own qualification: trained models passed cached-versus-full logit checks only under a fixed-reduction inference policy, which itself changes 1.4-2.8% of next-token argmax choices relative to native evaluation. All results are conditional on one recipe and scale.

---


### 383. [Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents](https://arxiv.org/abs/2611.30624)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro, Daniel Romero-Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents act through tool calls: the model writes the arguments of a call as JSON, a guard decides whether the call may run, and an executor runs it. The same bytes are parsed several times, by the provider, gateways, SDKs, frameworks, the guard, and the executor. JSON leaves some choices to each parser, such as which copy of a repeated key counts. When the guard and the executor choose differently, the guard approves one call, the executor runs another, and the audit log records the approved one. We introduce this attack, tool-call smuggling, and study it across the stack. We describe six ways in which the same bytes yield different calls and build a differential testing harness that gives identical bytes to 17 pinned parser and validator configurations; most pairs disagree on some inputs, and even two official MCP SDKs accept different inputs. On tasks from $\tau$-bench and AgentDojo, an attacker who can rewrite the bytes in transit cancels another customer's reservation and creates a file that the guard blocks by name, while the audit log names only the approved call. Content the model reads splits guard and executor only inside a string: ten models we test write no repeated or disguised key into the call itself where we see it, but copy one verbatim into JSON text in an argument, which a Python guard and a Go executor read differently. A malicious server copying a legitimate tool's public schema and adding one field, which a note explains, gets the model to fill it, unseen by the guard, with user data. Parsing each call once, JSON text included, keeping only the fields of the approved schema, and handing it to the executor, sealed with its call ID in transit, stops all 7,412 crafted inputs and every attack we built.

---


### 384. [From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning](https://arxiv.org/abs/2611.30627)

**<font color=#1a73e8>作者：</font>** Kairong Han, Nuanqiao Shan, Ziyu Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become an important component in large language models (LLMs). However, existing RL approaches focus on final outputs or textual solution trajectories, leading to coarse-grained rewards and unreliable reasoning. Such paradigms focus mainly on what the model outputs while overlooking how the model internally reasons. Therefore, can we reward how a model thinks internally rather than merely what it says? We first reveal the problem of textual reward aliasing in existing reward modeling approaches. Motivated by this, we propose the Attention Process Reward Model (APRM), which assigns internal rewards based on hidden states and attention maps to capture high-quality reasoning patterns. With only approximately 46M parameters, APRM is trained using ranking and counterfactual objectives, and its reward guides RL optimization while being periodically updated to handle distribution shifts. Integrated with representative RL methods, APRM achieved an average pass@8 gain of 2.88\%. Our results demonstrate the promise of incorporating internal reasoning signals into RL for LLMs.

---


### 385. [Uncovering the Tells: Efficient Black-Box Audits for LLM Data Contamination](https://arxiv.org/abs/2611.30639)

**<font color=#1a73e8>作者：</font>** Dominik Bernard Lau, Filip Pawlicki, Jan Dubiński 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing methods for assessing training data contamination in Large Language Models achieve high accuracy, but fundamentally rely on gray-box access, rendering them inapplicable to fully black-box environments. This limitation forces auditors to rely on full-sequence sampling or rigid heuristics, both of which incur prohibitive inference costs and struggle to isolate the underlying memorization signal. To overcome this, we propose a generation-based black-box framework that infers context-induced information gain from targeted token discrepancies. We introduce a budget-constrained auditing regime, building on the empirical observation that the membership signal is highly sparse and concentrated in a few highly informative tokens. We formalize this sparsity, showing why uniform sampling needs many more samples than a policy that targets informative positions. Empirically, our approach achieves state-of-the-art black-box separation accuracy while needing about 3x fewer queries than uniform position sampling. Finally, we apply this methodology to closed frontier models, exploring its capacity and limits in surfacing potential training data overlaps on commercial APIs.

---


### 386. [ActField: Learning Action Effects as Continuous-Time Latent Dynamics](https://arxiv.org/abs/2611.30659)

**<font color=#1a73e8>作者：</font>** Yunpeng Qing, Yuheng Huang, Changxu Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning how actions change visual states is essential for prediction and decision-making in embodied tasks. Existing action-conditioned JEPA world models typically predict future representations at discrete observation intervals, leaving the temporal evolution of action effects implicit. We introduce ActField, a continuous-time JEPA world model that explicitly models latent state evolution through an action-conditioned vector field integrated over physical time. ActField separates action-independent evolution from action-induced changes, with the latter modulated by the latent context. A reference-conditioned representation and multi-step dynamics loss further support accurate long-horizon prediction. Together, these components provide a structured and temporally continuous formulation for predicting action-conditioned visual dynamics. Experiments across LIBERO, DROID, and BEHAVIOR demonstrate improved visual prediction fidelity and more accurate action-induced motion prediction over existing world models. Further evaluations on simulated and real-world manipulation tasks demonstrate the utility of ActField in improving downstream policy planning through VLM-guided action selection.

---


### 387. [WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce](https://arxiv.org/abs/2611.30662)

**<font color=#1a73e8>作者：</font>** Binhui Xie, Jinmin Li, Haomiao Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while achieving state-of-the-art general-purpose performance at their respective scales. The family spans five sizes, from a 0.8B dense model to a 35B mixture-of-experts model with 3B active parameters. Our training pipeline begins with two-stage continued pre-training that progressively raises the proportion of e-commerce data within a diverse multimodal data mixture, followed by hybrid-thinking post-training that combines on-policy distillation and reinforcement learning to support both non-thinking and thinking modes. For evaluation, we construct a comprehensive suite of 28 e-commerce benchmarks (23 in-house and five open-source) covering eight business scenarios and complement it with 64 public general-purpose benchmarks. On the e-commerce suite, WeMM-Ecom-35B-A3B surpasses substantially larger open-source flagship models, including Qwen3.8-Flash-Next, HY4, and DeepSeek-V4.1-Flash. On the general-purpose suite, every WeMM-Ecom model surpasses its similarly sized Qwen3.5 counterpart, with the lightweight variants (e.g., WeMM-Ecom-2B) showing clear advantages over leading lightweight models such as Qwen3.5-2B, MiniCPM-V-4.7-1B, and LFM3-VL-2B. Beyond benchmarks, WeMM-Ecom now powers hundreds of production use cases in WeChat, including catalog management, multimodal product search, and livestream commerce, serving billion-scale requests per day. We publicly release all model weights and detail our data curation, training recipe, and benchmark construction to facilitate future work on domain-specialized multimodal models. We have released the model weights and code to facilitate future research at this https URL.

---


### 388. [DriveDreamer-RSI: Recursive Self-Improvement of Driving Perception and Agentic Data Generation](https://arxiv.org/abs/2611.30671)

**<font color=#1a73e8>作者：</font>** Dingyi Yao, Tingdong Yu, Guosheng Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable generation can expand training data for driving perception, but visual realism alone does not ensure learning gains. Effective generation must adapt both what data to generate and how to construct them as the perception model evolves. In this paper, we present DriveDreamer-RSI, a framework for recursive self-improvement of driving perception and agentic data generation through feedback between perception learning and data construction. Its outer loop implements Gap-Guided Target Adaptation, generating labeled videos from current perception gaps and updating targets after training. Its inner loop uses a vision-language agent to iteratively edit scenes through observation and execution feedback. Across rounds, Learning-Feedback-Driven Strategy Refinement derives reusable construction advice from execution experience and downstream learning outcomes. On the nuScenes validation set, DriveDreamer-RSI surpasses the dataset-replay baseline by 4.09 mAP and 4.13 NDS points using approximately half the synthetic frames.

---


### 389. [Uncovering Hidden Behaviours in Language Models via Limited-Parameter Finetuning](https://arxiv.org/abs/2611.30672)

**<font color=#1a73e8>作者：</font>** Boyd Kane, Jo J. Jiao, Elizabeth Donoway 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can have behaviours which only arise in hard-to-anticipate contexts. These hidden behaviours pose a challenge to alignment audits, which seek to uncover problematic model behaviour but are limited by the scenarios the auditor can anticipate. To address this challenge, we explore limited-parameter finetuning (LPF) on examples of a target behaviour. While training 3-25% of LoRA parameters, LPF reveals whether the model has a hidden behaviour, even when standard behavioural evaluations cannot. LPF succeeds on a suite of model organisms with hidden behaviours (8-14B parameters), and also surfaces naturally occurring hidden behaviours in open-weight models (27-35B parameters). LPF can thus distinguish between models which appear behaviourally identical to an auditor, and does not require the context in which the hidden behaviour surfaces. LPF provides a novel affordance that may be useful for auditing frontier AI models. However, we do not evaluate LPF against baselines in a realistic auditing setting, so further work is needed to determine its practicality.

---


### 390. [Optimising VLM Harnesses to Localise Errors in Generated Videos](https://arxiv.org/abs/2611.30673)

**<font color=#1a73e8>作者：</font>** Ankit Yadav, Nikhil Cherian Kurian, Arpit Garg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying subtle errors in generated videos is an important step toward automated video generation, where errors must be detected to assess and refine generated clips. Recent work shows that pretrained vision-language models (VLMs) can localise such errors, but their effectiveness depends strongly on the workflow used: choices about which frames to inspect, which tools and model calls to make, and how to combine predictions can lead to substantially different results. We study VLM harnesses for video error localisation. Instead of relying on manually designed harnesses, we propose Harness Search and Merge (HSM), an algorithm that automatically constructs them by searching over executable evaluation programs. An LLM orchestrator refines candidate harnesses independently on random training subsets, records findings in a memory, and constructively merges complementary candidates. We evaluate HSM on Spotlight, a recently proposed benchmark for localising errors in generated videos. HSM achieves 0.234 +- 0.012 F1, exceeding the strongest benchmark strategy (0.173 +- 0.016), and retains its lead on an unseen video generator (0.213 +- 0.008 versus 0.140 +- 0.003). On IPV-Bench, it achieves strong localisation performance with lower false-alarm rates than existing optimisation baselines. Together, these results show that searching over complete VLM harnesses can outperform existing evaluation strategies, transfer to an unseen video generator, and reduce false alarms on real videos.

---


### 391. [The user who is not there: genealogy and critique of simulated users built with generative AI in UX testing](https://arxiv.org/abs/2611.30674)

**<font color=#1a73e8>作者：</font>** José Carlos Arcoverde  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Usability testing depends on people, and people's time does not speed up at the pace that software production demands. Large language models (LLMs) now promise to remove people from testing by generating simulated users that browse websites, answer questionnaires and give interviews. This paper examines how academic research understands that promise. It combines a critical literature review with a genealogical reading that follows the simulated user from the cognitive models of the 1980s to current generative agents. The paper makes four claims. First, testing without the user is an old aim of human-computer interaction (HCI), and cost has always justified it. Second, the validity criterion for user models shifted from predictive precision to believability, and recent studies that return to precision report weak results. Third, simulated participants conflict with the values of academic research and with methods that treat participation as a political right, with Participatory Design as the limit case. Fourth, the Latin American literature found in this review uses generative AI to support expert inspection and contains no study of synthetic users. That gap leaves open questions about who gets represented and about research ethics regulation in Brazil. The paper closes with an agenda of open problems. As part of its method, it reports that the review itself used an LLM as research assistant, and it discusses what that implies.

---


### 392. [Empirical Margin Sensitivity: An Interventional Neuron-Level Probe of Post-Trained Medical LLMs](https://arxiv.org/abs/2611.30675)

**<font color=#1a73e8>作者：</font>** Aniruddh Shreyas, Aarnav Kembhavi, Minal Moharir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical post-training raises benchmark accuracy, but accuracy does not show which internal components a model's decisions depend on, or whether components that support one benchmark also support another. We apply the weight-space intervention paradigm of ROME and MEMIT at the granularity of one MLP down-projection column. Our measurement, Empirical Margin Sensitivity (EMS), replaces each coordinate magnitude of a column by its mean while preserving the column's sign pattern and L1 scale, and records the resulting change in the logit margin between the correct option and its hardest-wrong competitor. This isolates the margin's dependence on a column's fine-grained coordinate structure while the column stays in place. We discover high-EMS columns (anchors) on MedQA in ten public checkpoints (four general-purpose bases and six medical post-trained variants) across the Gemma, Llama, Qwen, and AFM families, and measure the same columns on MedMCQA and PubMedQA. Mean-ablating each discovered anchor set lowers MedQA accuracy in all six post-trained models, by 6 to 28 points. In the two pure-SFT checkpoints, crushing anchors raises the PubMedQA margin on correctly answered items (negative EMS), and anchors with this property sit significantly deeper than the same model's other anchors; the four checkpoints trained with RL or mixed recipes show positive PubMedQA EMS and no significant depth shift. The depth association recurs in each of three held-out checkpoints. Because the checkpoints differ in data and pipeline as well as objective, we report these as per-checkpoint observations.

---


### 393. [Learn the Effects, Not the Examples: Implicit ICL via Attention Patching](https://arxiv.org/abs/2611.30690)

**<font color=#1a73e8>作者：</font>** Seungwon Woo, Hyunseo Shin, Wonseok Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables language models to adapt to new tasks from demonstrations, but repeatedly including multiple examples increases context length and inference cost. Many existing implicit ICL methods encode demonstrations as fixed vectors, limiting adaptation of the intervention to individual queries and token positions. We propose Attention-Patching, an implicit ICL method that models contextual changes in self-attention outputs through task-specific updates to attention output projections. Using query-answer pairs processed with and without a fixed demonstration set, Attention-Patching fits layer-wise affine transformations from non-contextual attention representations to the demonstration-induced output changes. Across 12 classification benchmarks and four model families, Attention-Patching achieves higher average accuracy than the evaluated implicit ICL baselines while maintaining performance comparable to explicit ICL at near zero-shot inference cost. Further experiments on diverse generation tasks demonstrate its applicability to autoregressive multi-token generation.

---


### 394. [Lowering the Bar for Everyone: Hidden Validation-Seeking Goals in Empathetic RL](https://arxiv.org/abs/2611.30702)

**<font color=#1a73e8>作者：</font>** Xinche Zhang, Shanghong Xie, Zhiyuan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When RL learns from the reactions of many users, the policy usually cannot see what each user wants. We ask what it learns from users who privately want validation: to validate them alone (targeting), or to lower its bar for endorsing everyone (a threshold shift). We answer this in one setting, empathetic RL against LLM-simulated users (RLVER, GRPO, Qwen2.5-7B-Instruct): we vary only the share of validation-seeking users (0--50%; RLVER's default: 24.6%) and evaluate on 1,000 Reddit AITA posts with community fault verdicts.
The policy shifts its threshold. Endorsement of at-fault posters rises by 3--4 percentage points per 10 points of share; without such users the Qwen model stays at base, and the effect persists at matched KL and under a goal-blind reward. Signal-detection analysis shows that the criterion for endorsing falls while discrimination between at-fault and not-at-fault posters does not decline. An explicit request to be told if one is wrong gives no measurable protection: at-fault posters who make it receive nearly the same rise as those who do not (+0.11 vs. +0.13). When the goal is stated during training, the policy instead largely targets, endorsing seekers regardless of fault.
Standard sycophancy and empathy benchmarks miss the shift; five of six usable released empathetic-RL checkpoints also endorse at-fault posters who ask for honesty more than their base models, though a pre-registered prediction for two held for only one. The user mix is a training hyperparameter to audit and report.

---


### 395. [Hard to Translate, Harder to Detect: Human Analysis Remains Essential in AI Meme Translation](https://arxiv.org/abs/2611.30710)

**<font color=#1a73e8>作者：</font>** Olga Zamaraeva, Carla Martínez, Carlos Gómez-Rodríguez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a dataset and evaluation setup for a problem in creative machine translation: translating culturally loaded passages that carry much of a text's meaning and humor that may depend on subtle or implicit discourse. We study Soviet comedy quotations that function as memes in Russian-language communication. Off-the-shelf difficulty estimators do not find these passages; current models searching the web find most but not all of them, but their own analyses of the difficulty do not help translation as well as a human-validated one. Given a brief human-validated analysis of why each passage is difficult, older models improve modestly; the strongest current translators (GPT-6 Sol and Claude Opus 5.5) improve more, and in human evaluation GPT-6 Sol comes close to the approved references on most films. Newer models have thus become much better at using such an analysis while still not reliably producing it themselves. We release (1) a dataset of five films' Russian subtitles with their audience-selected culturally salient passages, human-validated analyses, and reference translations (into English, Galician, and Spanish), together with every full-film LLM translation and evaluation produced in this study; and (2) an item-level MQM-style evaluation protocol that measures translator and evaluator noise to set the number of runs the evaluation needs, and whose automatic version tracks human judgment of these passages, which reference-free neural metrics do not, whether they score the whole text or the passages alone.

---


### 396. [Testing Quantized KV-Cache Maintenance: Encoding Layout and Historical Restoration](https://arxiv.org/abs/2611.30720)

**<font color=#1a73e8>作者：</font>** Ziyang Huang, Songwei Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repeating rows then selecting originals retains layout-dependent drift despite equal encoding counts. We measure when existing checks fail to establish preservation contracts in fixed quantized KV-cache implementations. In four-bit HQQ axis zero at sixteen cycles, median paired relative-L2 increases over same-shape re-encoding are 7.22 percentage points for Qwen3-1.7B and 11.59 for SmolLM3-3B. Matched encoded states cover sixteen shared questions per model at one and sixteen cycles. Axis one matches the shape-preserving control; lazy reorders preserve the initial state. On one known input, fixed update counts retain the difference; preserving group members removes it. Our prefix-view extension passes current-prefix checks yet changes history and next logits in six model/codec settings at residual capacities four and 128. Public lookup reaches this boundary, including one of four precommitted project-new GPU inputs; fixed query swaps isolate a conditional old-history effect. Checkpoint/dense rollback is exact. An explicit delayed lookup client admits a supported 129-token path excluded by native AR on one known context. Failed task-harm expansion precludes population failure-rate or general answer-degradation claims. Native MLX-LM fixtures expose stale caller caches; synchronization restores the tested in-place contract with native computations preserved. In rejection tests, stale callers change logits but not greedy tokens.

---


### 397. [CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons?](https://arxiv.org/abs/2611.30727)

**<font color=#1a73e8>作者：</font>** Hongchuan Zeng, Bowen Liu, Changjiang Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual search agents can access the global Web, yet may remain trapped in a language environment with insufficient evidence; we refer to this failure as a language information cocoon. However, existing search benchmarks largely operate within a single language, especially English, overlooking entity connections across multiple languages. We introduce CocoonBench, a benchmark that evaluates whether multilingual search agents can escape such language information cocoons. CocoonBench mines answer-centered relational paths from a frozen Wikidata-derived graph and selects clue sets that are individually necessary and jointly identify a unique answer. Using language-specific entity names, it records each task's minimum language cover, removes direct identifiers, and renders each task as matched prompts in three languages together with its construction certificate and provenance. Across 10 state-of-the-art models, mean accuracy on CocoonBench ranges from 33.8% (DeepSeek-V4-Flash) to 69.7% (Claude-Opus-4.8), leaving even the strongest system below 70%. The same construction certificates support path-aligned trajectory analysis, enabling diagnosis of model failures in language routing, evidence-path recovery, and answer use. The result shows that escaping a language cocoon requires more than switching languages: successful cross-lingual search depends on both covering the correct languages and connecting the evidence found across them.

---


### 398. [Can Cities Have Personalities? Introducing the SCD City Personality Assessment](https://arxiv.org/abs/2611.30733)

**<font color=#1a73e8>作者：</font>** Andrei Khurshudov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Descriptions of cities are shaped by human experience and institutional narratives. We introduce the SCD City Personality Assessment (SCD-CPA), a method that instantiates document-grounded ChatGPT city personas and interrogates each with an identical 24-statement instrument inspired by the four-pair structure of the Myers-Briggs Type Indicator. Rather than asking a general-purpose model to characterize cities freely, we configure a separate document-grounded conversational agent for each city and use alternative evidence portraits to compare documentary inputs. The resulting four bipolar dimensions and four-letter summaries use independently defined urban concepts and scoring rules. Tokyo, New York, and Paris form the methodological evaluation (33 assessments across repeated sessions, three GPT-6 effort settings, and alternative portraits): Tokyo's original portrait yielded 85.4% exact within-setting item agreement, while evidence substitutions shifted some dimension strengths. A five-city application to Shanghai, Dubai, Mumbai, Lagos, and Sao Paulo (15 assessments) yielded 77.8% exact and 99.4% within-one-point cross-setting agreement, indicating consistency under the tested configurations. By treating each city conversational agent as a reproducible, evidence-conditioned experimental configuration, SCD-CPA makes documented city-character perceptions comparable and exposes their sensitivity to source selection. Although the documentary evidence is explicitly controlled, the model's internal interpretation of that evidence cannot be fully observed. We also examine the robustness of SCD-CPA across three AI reasoning-effort settings. The observed consistency suggests that the methodology is relatively insensitive to the tested configuration differences and provides a framework for evaluating its stability as future generations of AI models become available.

---


### 399. [Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing](https://arxiv.org/abs/2611.30742)

**<font color=#1a73e8>作者：</font>** Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are often ranked by an LLM judge whose error rates are measured once and reused for every agent. The corrected success rates can then be biased when the judge's errors depend on the trajectory and agents differ in the trajectories they produce for successes or failures. We derive the exact asymptotic bias and give a chain of checks from identification to simultaneous ranks. On a four-agent semi-synthetic benchmark, a scalar correction with oracle calibration has maximum bias 0.245 and mean pointwise coverage 0.016, and never recovers the full ranking (0/250 replications). Augmented inverse-probability weighting (AIPW) with a uniform or a design-aware random audit keeps the maximum bias below 0.003, with mean pointwise coverage of 0.939 and 0.950. In a 48-cell stress test, effective target support rises only from 0.209 to 0.805 as calibration grows from 600 to 4,800 labels, while audited AIPW keeps a mean absolute error of 0.018-0.020. Without calibration support, or with judge dependence within an externally justified bound, we report valid bounds or sensitivity sets and carry them into rank sets. An e-process confidence sequence stays valid, for a stable target, under predictable adaptive auditing and arbitrary stopping.

---


### 400. [Intent-Conditioned Argument Mediation for Tool-Using LLM Agents: Blocking Trusted-but-Unauthorized Arguments](https://arxiv.org/abs/2611.30745)

**<font color=#1a73e8>作者：</font>** Yulliwas Ameur, Miqeas Pedro Mendes, Samia Bouzefrane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents turn a user's request and retrieved content into tool calls, and a call can reach the wrong recipient, endpoint, file or participant. Argument-level provenance blocks such values when they come from untrusted content, but accepts a trusted value that the user never requested. IntentFlow, a mediation layer between an unmodified planner and its tools, checks each authority-bearing argument against an intent contract and a provenance policy. On a synthetic benchmark of 200 attacks (oracle intent and injection labels, declared roles), attack success falls from 50.5% with provenance alone to 12.0% [8.2-17.2%]; every remaining success alters a content or payload field. IntentFlow wrongly blocks none of 200 paired benign tasks and 4 of 50 hard ones. On 50 trusted-but-unauthorized attacks, provenance-only mediation executes all 50 and IntentFlow none; a CaMeL-style check also blocks all 50 but rejects 16 of 50 benign tasks. On an offline AgentDojo-derived replay, IntentFlow blocks all 20 attacks at 75% benign success, as does a CaMeL-style check; a Progent-style allowlist blocks 19 and keeps all benign tasks. With one live planner and the same oracles, the mediator blocked all 17 corrupted calls proposed in 110 attacks.

---


> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
