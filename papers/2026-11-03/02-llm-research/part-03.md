# 🧠 大模型相关研究 | 2026年11月03日

> 本类共 **188** 篇论文：已确认 **175** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-188](./part-04.md)

---

### 101. [Queryable Gaussian View Index: Text Retrieval and Selective Camera Localization](https://arxiv.org/abs/2610.41373)

**<font color=#1a73e8>作者：</font>** Tianyu Xiong, Rui Li, Jiaqi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Queryable Gaussian View Index (QGVI) for querying existing Gaussian scene assets and their associated calibrated reference data. Text-view retrieval and selective RGB camera localization return poses in the asset's coordinate frame. QGVI-T turns Gaussian-rendered views into a language-searchable index of scene locations, binding structured captions to known camera poses and place identifiers. Semantic and lexical retrieval select views from distinct places without online rendering, VLM calls, or a scene-specific pose network. The image route, QGVI-I, filters LoGS-based geometric estimates using distinct inlier query keypoints. It omits photometric refinement and preserves accepted pose coordinates. On nine development scenes, QGVI-T achieves 58.3% Top-1 and 78.3% Top-5 joint relevance-and-validity success, compared with 26.1% and 34.6% for our CityLoC reimplementation with refinement. QGVI-I achieves 97.3% scene-mean pose success at 1 m/2 degrees, with pooled false-acceptance and false-rejection rates of 0.707% and 1.142%. A paired cached evaluation retains all 1,775 initializer poses correct at this threshold. Recorded median text query latency is 0.020 s. Matched controls show competitive BM25 retrieval and slightly lower false acceptance for thresholded full LoGS; grid augmentation suggests modest gains on novel-view-derived descriptions. We report model-judged semantic success separately from source-camera recovery, with source-verified or estimated scales for geometric evaluation.

---


### 102. [From the Zoo to the BULLPEN: Sample-Efficient LLM Profiling via Multi-Channel Model Embeddings](https://arxiv.org/abs/2610.41375)

**<font color=#1a73e8>作者：</font>** Russell Ro, Qiming Cui, Reza Abbasi-Asl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Choosing among the hundreds of thousands of available large language models (LLMs) requires a thorough understanding of each candidate model's properties. In practice, each property is measured by its own benchmark suite, so profiling a model on many properties means paying for many separate evaluations. To address this, model embeddings compress each model into a fixed-length vector from which many properties can be predicted. Existing methods, such as EmbedLLM, build these vectors from correctness patterns and question features, and often need large probe batteries to do so. However, many behaviors that are important when choosing a model, such as its verbosity, safety and style, show up more in how it answers than in whether it is correct. We introduce BULLPEN (Behavioral Understanding of Large Language models via Profile ENcodings), a framework that extends EmbedLLM in three ways. First, BULLPEN organizes the downstream tasks that prior work uses and adds 20 task benchmarks we built on behavior, style and provenance. Second, it is the first framework to read a model's own answer text jointly with its correctness and the question text. Third, it encodes models from a few hundred questions instead of the full 24,118-question pool. Across 260 open-weight models, our answer-text encoder scores 0.48 +/- 0.10 on the new tasks against 0.35 +/- 0.10 for the best prior encoder. Our encoders that read answer text keep at least 91% of their full-pool skill from only 400 questions (1.3% of the inference compute of the full question pool), while a correctness-only baseline keeps 83% with the same 400 questions. Because these embeddings need only model outputs, they support behavioral auditing and low-cost profiling, and could extend to API-only models. Code and data: this https URL

---


### 103. [Ask on Demand: Targeted Peer Communication for Parallel Agentic Systems](https://arxiv.org/abs/2610.41378)

**<font color=#1a73e8>作者：</font>** Haofu Yang, Hongyang Yin, Ran Bi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallel LLM agents tackle complex tasks by exploring multiple trajectories, yet useful discoveries remain isolated in individual execution histories. Existing sharing methods often select or summarize information before other agents' needs become clear, potentially overlooking details that become important later. We propose Ask on Demand (AOD), a communication framework that enables agents to seek targeted peer assistance when specific information needs arise. Upon an approved request, AOD retrieves relevant evidence from peer execution histories, selects a suitable peer, and generates a response tailored to the request. To determine when such assistance is worthwhile, we train a lightweight gate using paired team continuations, with supervision derived from final team outcomes and inference cost. Experiments on AppWorld and WebShop demonstrate that AOD consistently improves task performance over independent parallel execution while achieving lower inference cost than existing information-sharing baselines. These findings highlight the benefits of aligning peer communication with agents' evolving information needs to achieve more effective and efficient collaboration.

---


### 104. [Parse Before You Execute: Efficient Spatial Reasoning with Executable Primitives](https://arxiv.org/abs/2610.41389)

**<font color=#1a73e8>作者：</font>** Xiwei Liu, Yulong Li, Xinling Zhuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning in Vision-Language Models (VLMs) has increasingly benefited from tool-integrated pipelines that ground computation in explicit geometry. However, existing systems often compile queries into relatively open-ended artifacts, such as code, task constraints, tool plans, or gathered evidence, leaving what must be resolved before execution under-specified. This can lead to unnecessary tool acquisition and iterative refinement, while still producing plausible reasoning traces from incomplete spatial commitments. We identify this failure mode as under-committed query compilation. To address it, we propose PEPS, a training-free agentic paradigm Parsing Executable Primitives for Spatial reasoning under a typed FESM schema over Frame, Entity, State, and Metric. PEPS follows a parse-before-execute principle: the Parser commits each query to a compact set of executable requirements; the Executor selectively grounds the required primitives through fixed geometric APIs and deterministic computation; and the Verifier checks execution sufficiency, enabling early termination or targeted repair. Extensive experiments across challenging spatial reasoning benchmarks show that PEPS consistently improves reasoning accuracy while substantially reducing refinement rounds, API cost, and end-to-end latency over strong tool-integrated baselines. These results demonstrate that explicit requirement commitment can make tool-integrated spatial reasoning not only more reliable, but also more execution-efficient.

---


### 105. [Comparative Evaluation of LLM-Based Review Paradigms for Academic Paper Quality Assessment](https://arxiv.org/abs/2610.41391)

**<font color=#1a73e8>作者：</font>** Fan Huang, Hongyu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Growing submission volumes have renewed interest in using large language models (LLMs) to support peer review. It remains unclear how such evaluation should be structured, how much the model matters, and whether LLM scores predict research impact. We evaluate five paradigms across three input representations and three LLMs on 232 stratified ICLR 2025 submissions. Direct absolute rating matches comparative ranking on rank correlation with human scores, yet compresses most predictions above the accept threshold, flagging almost none of the papers reviewers scored below it. A base-rate-matched recalibration control locates the cause: comparative ranking supplies placement, not better ordering, and after recalibration Direct Rating reaches higher agreement than Elo while making 24% as many API calls. Abstract-only input beats full-paper summarization, and model choice matters as much as paradigm choice. Replicating on all 11,513 scored submissions reproduces these patterns, shows absolute agreement depends on the evaluated set's score spread, and finds none beating an always-reject baseline in accuracy. Human scores track citations better than any paradigm, with one exception: Group Rating retains its citation correlation after controlling for human scores, and alone ranks within the accepted pool. Ranking quality alone cannot assess review quality; calibration, thresholds, model, and target outcome all matter.

---


### 106. [Cross-Interface Authorization for AI Computer-Use Agents](https://arxiv.org/abs/2610.41397)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents act through graphical interfaces, command lines, APIs, scripts, and Model Context Protocol servers. A policy decision can be interface-invariant while its executable authorization is not: another route can bypass mediation, alter a security-relevant default, or commit after the authorized state has changed. We present a profile-bounded protocol for a fixed, versioned computer-use deployment. It enumerates effect-bearing routes and durable sinks, checks a route-to-sink enforcement cut, normalizes each concrete request to a canonical effect, issues a route-bound prepare ticket, and verifies the route, effect, grant, trace, profile, inventory, and authoritative state again at commit. A committed result requires an agreeing sink receipt. Under explicit assumptions, we prove profile-bounded refinement, matched-effect decision invariance, resistance to alternate-route laundering and declared cross-surface recomposition, commit-time state safety, and receipt-grounded outcomes.
The reference profile registers 12 effect families, five interfaces, and 60 routes. Two structurally distinct runtime mappings produce 3,464 traces over 1,732 scenarios each: 960 commits, 2,312 denials, and 192 commits after re-preparation. An independent checker accepts every retained trace and pair and rejects 26/26 semantic regressions; coverage and normalizer suites reject 24/24 and 720/720 mutants; and 168/168 commit probes match their declared outcomes. A frozen-source audit passes 52 checks over 12 files from two independent hybrid runtimes and one public authorization substrate. Source-shaped adapter refinements commit 48/48 instrumented calls and reject 15/15 unbound cases. The resulting guarantees bind the declared profile and its effect semantics.

---


### 107. [When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing](https://arxiv.org/abs/2610.41401)

**<font color=#1a73e8>作者：</font>** Yixiang Luo, Ziheng Ma, Ke Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents interact with online services through tool calls that may access private data or perform sensitive actions. Specialized providers can supply and maintain pre-execution safety auditing capabilities for agent operators. However, sending task descriptions, call arguments, and interaction histories to an external auditor may expose sensitive user information. In this work, we propose a paradigm for privacy-preserving safety auditing that separates delegated audit computation from plaintext access and execution authority. Grounded in a three-domain auditing model, the paradigm connects trusted representation construction, encrypted audit computation, and trusted decision and execution through explicit interfaces. These interfaces accommodate alternative representations and scorers, while encrypted computation protects audit inputs from a semi-honest auditor. We instantiate this paradigm in SealCall, a framework combining learned audit representations, CKKS-based encrypted similarity computation, and execution control bound to audited tool calls. Evaluated on 1,252 public binary candidates, SealCall achieves a mean F1 score of 0.840 under grouped nested evaluation, while preserving plaintext audit decisions in all measured cases. A representative configuration completes each encrypted scoring operation in 0.176 s.

---


### 108. [SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2610.41408)

**<font color=#1a73e8>作者：</font>** Haesung Lee, Insu Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms. Weight quantization is a natural remedy, yet post-training quantization (PTQ) recipes inherited from large language models degrade when applied to VLAs at ultra-low precision. Existing low-bit PTQ methods often fail to explicitly account for the structure of downstream operations and allocate precision without considering its effect on the policy actions. We introduce SACQ, an ultra- low-bit weight-only vector-codebook quantization framework for VLAs. SACQ combines (1) structure-aware codebook fitting with role-specific quadratic metrics that reflect input statistics and downstream sensitivity; (2) action-aware mixed-bit allocation based on the increase in final-action error as individual layers are compressed; and (3) two-stage post-quantization refinement that reassigns codeword indices with second-order error compensation and calibrates codebooks and row-group scales against the decoded action. Using GR00T N1.7, SACQ achieves 93.85% average success across four LIBERO suites at 1.5 bits per language/action weight while reducing model memory by 4.83x. With INT8 activation quantization and low-precision attention, it retains 93.55% success while running 1.51x faster than BF16. On SimplER, SACQ further achieves 63.76% and 52.27% success under Visual Matching and Variant Aggregation at 2 bits per language/action weight, compared to 58.90% and 53.45% for BF16, respectively.

---


### 109. [SparseGDN: Chunk Sparse in Linear Attention](https://arxiv.org/abs/2610.41420)

**<font color=#1a73e8>作者：</font>** Jiedong Zhuang, Peng Zhao, Jialin Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gated Delta Networks (GDNs) offer linear-time sequence modeling, yet long-context prefill remains costly due to dense intra-chunk computation, recurrent-state updates, and intermediate state storage. We introduce SparseGDN, a hardware-aware framework that combines structured intra-chunk approximation with input-dependent recurrent-event selection while producing outputs for every token. A block-adjacent solver reduces local Delta-solve computation, while a dynamic selector allocates recurrent-update budgets across head pairs. The GPU implementation materializes updates only for selected events and reconstructs token outputs using compact state snapshots and group-local interactions, reducing computation and memory traffic. We evaluate SparseGDN on Qwen3.5-4B and Qwen3.5-9B across RULER tasks and context lengths from 4K to 128K. Retaining approximately 29% of recurrent events on average, SparseGDN achieves 1.50-1.94x GDN-core prefill speedups over native FLA kernels, including online selection overhead.

---


### 110. [Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents](https://arxiv.org/abs/2610.41432)

**<font color=#1a73e8>作者：</font>** Haoqing Wang, Xiaoyi Zhang, Sicheng Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computer-use agents increasingly tackle tasks ranging from everyday desktop activities to long-horizon professional workflows. Yet interfaces centered on screenshots and mouse-and-keyboard actions can impose a human-interaction prior, requiring repeated screen interpretation while leaving the computer's semantic and programmatic capabilities underexposed. We argue for exposing these capabilities and letting models choose and combine them. We introduce Hybrid Computer Use (HCU), a unified interface for general agents that combines three complementary channels: programmatic interaction through code and command-line tools, semantic interaction through accessibility (AX), and visual interaction through graphical user interfaces (GUI). Our HCU supports efficient AX interaction and guards against stale-state actions during channel switching. A supplementary HCU skill guides agents in selecting and coordinating channels to use the unified interface effectively. Our designed AX tools return compact observations, execute actions in batches, and report their effects as AX diffs, so the model needs fewer round trips. On OSWorld 2.0, HCU achieves the highest Partial and Binary scores among the compared systems. Analyzing agent trajectories, we find that all evaluated models improve with HCU yet allocate work across the channels differently and consistently outperform compared baselines in terms of both efficiency and task success, highlighting the value of unified computer-use interfaces that allow flexible channel selection and combination.

---


### 111. [A prospective randomized study of patient-centered AI for clinical visit preparation](https://arxiv.org/abs/2610.41437)

**<font color=#1a73e8>作者：</font>** Xincheng Tan, Matthew Thompson, Xiang Ji 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Patients often arrive at brief, time-constrained clinical visits unsure of what to expect or ask, and millions of adults now turn to general-purpose AI chatbots to prepare beforehand. Yet whether conversational AI improves visit readiness remains unclear. We designed a large language model (LLM)-based visit preparation agent to guide patients before an appointment by gathering clinical context, setting visit expectations, providing relevant health information, building a prioritized list of questions for their clinician, and generating a summary. In a prospective consented randomized study in the Google Health app, 802 U.S. adults held 866 health-related conversations with the visit preparation agent (standard or concise variant) or a minimally prompted control chatbot built on the same LLM. The visit preparation agent significantly outperformed the control across blinded clinician evaluations and patient self-reports. In clinician reviews of completed sessions (n = 272), the agent achieved a 16.6% higher rate of comprehensive preparation (67.2% vs. 50.6%; P < 0.05) and an 8.5% higher rate of alignment with patients' health context (98.9% vs. 90.4%; P < 0.01), while maintaining high medical safety and appropriateness across all study arms. Patient post-surveys (n = 460) showed 16.8% higher visit preparedness (73.8% vs. 57.0%; P < 0.01), 14.3% higher confidence in knowing what to ask (81.4% vs. 67.1%; P < 0.01), and 12.0% higher overall satisfaction (74.0% vs. 62.0%; P < 0.05). Clinician and participant metrics were not significantly correlated, indicating that expert review and patient self-assessment capture complementary dimensions of patient-facing AI. These findings suggest that LLM chatbots can safely help patients prepare for clinical visits, with greater benefit when following a structured workflow, and motivate future studies on in-visit communication and clinical outcomes.

---


### 112. [From Representation to Readout: Mechanistic Analysis of Membership Signals in Language Models](https://arxiv.org/abs/2610.41445)

**<font color=#1a73e8>作者：</font>** Wenxi Dai, Jingyu Hu, Yanting Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership inference aims to determine whether a particular example was included in a model's training data. Such membership signals are often broadly described as memorization, while the underlying mechanisms can involve both how information is represented internally and how it is accessed by the model to produce behaviors. We therefore present a mechanistic study of membership signals in large language models (LLMs). We introduce Decodable Information Score, Used Information Score, and Readout Accessibility Gap (DUG), a set of complementary measures that separately quantify membership information decodable from internal representations and the extent to which it is exposed through the model's readout. Across supervised fine-tuning (SFT) and reinforcement learning (RL)-based membership inference methods, membership-specific effects appear in both the amount of decodable information and readout under SFT, while under RL-based membership inference methods they appear primarily in readout. Activation patching further localizes this membership-specific effect to intermediate layers. To examine whether these findings extend to a more general RL setting, we further study reinforcement learning with verifiable rewards (RLVR) contamination, where the training reward is independent of the reference solution. In this setting, we find that behavioral changes can emerge without a corresponding increase in likelihood-based membership inference signals.

---


### 113. [NormDetect: Anchored Calibration for Low-False-Positive Detection of Machine-Generated Web Text](https://arxiv.org/abs/2610.41459)

**<font color=#1a73e8>作者：</font>** Hanshuai Cui, Fanshuai Meng, Zhiqing Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web platforms screen posts for text written by large language models, and every false flag hits a human writer. Detectors must therefore run at a very low false positive rate (FPR). Zero-shot detectors such as Binoculars score text with frozen language models, but invisible edits such as homoglyphs shatter tokenization and push machine text into the human range. Unicode normalization undoes these edits, yet the normalized score still misses half of the machine text at a strict FPR, under attacks that leave nothing to clean. We find that with the Falcon-7B scoring pair, heads on token statistics recall less than the normalized score at this FPR, and several flag too many human posts in some sections. We propose NormDetect, which anchors a learned per-section head to the normalized zero-shot score. A blend weight chosen on training folds under a human FPR cap combines the two scores, and one threshold is calibrated on human text only. On eight sections of the RAID benchmark with eleven attacks, NormDetect raises recall at a 0.1% calibrated FPR by 5.0 points over normalized Binoculars. Its human FPR bound stays at most 1% in every section, and no other detector within this bound recalls as much.

---


### 114. [When Links Mislead: Label-Free Structural Polarity for Zero-Shot Classification of Web Pages](https://arxiv.org/abs/2610.41464)

**<font color=#1a73e8>作者：</font>** Hanshuai Cui, Zhiqing Tang, Zhi Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web platforms such as digital libraries, online stores and university sites must classify new pages before anyone labels them. Large language models (LLMs) can label each page from its text, but these labels are noisy, and links could correct them only where linked pages share classes. Existing zero-shot methods ignore the links, or pull a page toward its neighbours as label propagation and graph neural networks (GNNs) do, which hurts where linked pages differ in class. Others weight propagation by an LLM-estimated homophily that costs extra calls and drifts across LLMs. We find that the sign with which links should enter a prediction, which we call structural polarity, is readable without true labels. It is the excess agreement of LLM labels and text-prototype predictions along links. We thus propose ZeroPolar, which gates one signed propagation step by this statistic. Training-free ZeroPolar mixes prototype scores with any number of LLM labels, and ZeroPolar-T denoises the labels with a text classifier once half of the pages carry one. With one GPT-4o label per page, ZeroPolar-T reaches the highest mean accuracy on eleven graphs (73.99%), 6.01 points above LLM-BP and significantly above all eighteen baselines we compare. With LLM labels on only 5% of the pages, training-free ZeroPolar leads a GNN trained on these labels by 10.80 points.

---


### 115. [KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise](https://arxiv.org/abs/2610.41480)

**<font color=#1a73e8>作者：</font>** Jonas Loos, Oliver Eberle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model changes how it responds, but where is this fine-tuned behavior instantiated? To better understand this, we evaluate whether the change in model behavior arises only during the generation of the answer tokens where the change manifests, or whether altered processing of previous tokens causes it via the attention mechanism. For this, we patch the KV cache from a LoRA fine-tuned model into the unmodified base model, and vice versa. Our results show that for some behaviors, like responding in German or emergent misalignment, patching the KV cache can indeed transfer them from the fine-tuned to the base model. Correspondingly, patching the KV cache from base to fine-tune can partially or fully remove fine-tuned behavior. Furthermore, we find that the effect of patching grows with how much of the KV cache is patched and concentrates at a few pivotal positions, with system-prompt and chat-template tokens having disproportionate influence.

---


### 116. [KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.41482)

**<font color=#1a73e8>作者：</font>** Jinkyeong Choi, Chaebin Jeong, Junsung Jeon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive textual memory can carry earlier errors into later updates, yet task performance alone does not establish memory reliability. We define self-consistency bias as the persistence of incorrect claims already present in the incoming memory. We present KEEPER, a comparative analysis of four auxiliary objectives along information-content and update-sensitivity axes within a shared recursive interface, examining how supervision targets relate to agent performance. Among evaluated conditions, reward-related prediction achieve the highest task performance before and after offline reinforcement learning, outperforming joint supervision. A claim-level analysis of one baseline trajectory documents error persistence despite corrective observations. Together, these analyses motivate evaluating error persistence and valid-information retention alongside task outcomes.

---


### 117. [Multi-Test Nation Bias Benchmarking of LLMs with Explicit Unbiased Baselines](https://arxiv.org/abs/2610.41486)

**<font color=#1a73e8>作者：</font>** Jonghyeon Choi, Yeonjun Choi, Beakcheol Jang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While prior work has highlighted that systematic nation-level bias in large language models (LLMs) can pose operational risks for international relations (IR) applications, many existing evaluations still lack a clearly specified unbiased reference (ground truth), limiting fully quantitative and cross-setting measurement. Using an expanded corpus of 722 official UN Security Council (UNSC) records, we measure nation-level bias with five complementary tests, thereby extending prior approaches to cover a broader set of bias expression channels: opinion ranking (WOW), association sorting (AK+-), vote simulation (PVS), opposition attribution (F-Oppose), and framing (Headliner). To enable grounded bias evaluation, we explicitly define an unbiased status for each test; in particular, for WOW and AK+- where ground truth is difficult to specify, we propose an action-based pseudo unbiased status derived from observable voting behavior to construct a quantifiable baseline. Benchmarking 4 LLMs (GPT-4o-mini, Llama 3.3-70B, Mistral-22B-Small, and Qwen3-30B) across the five permanent members of the UNSC, we find a test-agnostic macro-pattern: relative to the reference baselines defined for each test, model outputs lean toward the opposition (red) side for China and Russia and toward the supportive (blue) side for the U.K., the U.S., and France. These results underscore the need to audit IR-facing LLM deployments with grounded, multi-test benchmarks tied to explicit reference points.

---


### 118. [Specification-Guided Generation for Large Language Models](https://arxiv.org/abs/2610.41511)

**<font color=#1a73e8>作者：</font>** Alessandro Previti, Konstantinos Vandikas, Mario Alviano 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate structured outputs, but existing constrained-decoding methods mainly enforce syntax and cannot directly enforce satisfaction of a formal specification. We introduce a neuro-symbolic, specification-guided decoding framework that combines LLM generation with symbolic reasoning. At each step, the framework refines the decoding grammar by filtering out values that cannot be extended to an output satisfying the specification. We present a forward-only variant that guarantees specification satisfaction by construction, and a backtracking variant that revises earlier feasible choices when their downstream consequences leave only values that the LLM itself judges unsuitable. The framework is model-agnostic, requires no retraining, and builds on existing grammar-constrained decoding mechanisms. Experiments on configuration and constraint-solving benchmarks show that the forward-only variant reliably produces specification-compliant outputs while reducing repeated LLM inference compared with rejection sampling and incurring modest symbolic-reasoning overhead. The backtracking variant further reduces cases in which the model is forced to select values that it has itself judged unsuitable, thereby substantially improving adherence to the LLM's stated interpretation of the prompt.

---


### 119. [Enhancing Knowledge Entity Relation Extraction in Abstracts and Full-text Content of Academic Articles Using Large Language Models](https://arxiv.org/abs/2610.41552)

**<font color=#1a73e8>作者：</font>** Yingyi Zhang, Chengzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates the effectiveness of large pre-trained language models (LLMs) for knowledge entity relation extraction (KERE) from academic papers. Existing studies have examined individual types of LLM-based strategies and evaluated model performance using metrics such as precision and recall. To provide a broader evaluation, this study investigates multiple strategies, including closed-source LLM-based CoT prompting, LoRA-adapted open-source LLMs, LLM-enhanced small pre-trained language models (SLMs), and SLM-enhanced closed-source LLMs. In addition, this study introduces two strategies, namely SLM-enhanced open-source LLMs and closed-source LLM-enhanced open-source LLMs. These strategies are evaluated from multiple perspectives, including metrics, their ability to mitigate errors observed in SLMs, and potential directions for model optimization. This study manually constructs two annotated datasets in the NLP domain, covering Abstract and Full-Text datasets. Experimental results show that the LoRA-adapted T5 model achieves the highest macro F1 scores of 0.7408 and 0.7013 on the Abstract and Full-Text datasets, respectively. SLMs also benefit from LLM-generated entity descriptions under the LLM-enhanced SLM strategy. Error analysis further reveals that the effectiveness of LLM-based strategies in mitigating SLM errors varies across error types. Based on the identified limitations and error patterns of these strategies, several optimization directions are proposed. In addition, combining strategies with different error patterns further improves KERE performance.

---


### 120. [ORION: An Outcome-Driven LLM Advisor for RL-Based Multi-Domain 6G Slice Placement](https://arxiv.org/abs/2610.41563)

**<font color=#1a73e8>作者：</font>** Mahmoud S. Mayaleh, Fetia Bannour, Nour-El-Houda Yellas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying 6G network slices across administrative domains requires an online decision for each arriving request: which domain hosts each virtual network function, how traffic crosses domain boundaries, and whether the slice is admitted. This joint decision problem is NP-hard under continuous arrivals. Experiments on a parametrized family of multi-domain topologies show that no fixed planning strategy dominates across all regimes: the performance ranking reverses between topology classes, and feasible placements exist for most rejected requests but remain undiscovered. These findings identify the plan layer as the decisive performance lever. We introduce ORION, a hierarchical orchestrator in which two LLM agents translate service intents into structured requests and generate abstract placement plans. A cooperative multi-agent RL coordinator selects the cross-domain partition, treating the plan as a persistent soft prior, while per-domain agents place the functions. ORION main contribution lies at the plan layer: an outcome-driven episodic memory that records, for each completed attempt, the network-condition profile, the proposed plan, and its verified feasibility outcome. The memory feeds verified successes and labelled failures back to the planner, thereby closing the adaptation loop using deployment feasibility rather than a scalar reward assigned to the planner's own proposals. To isolate the effect of the plan quality, we evaluate the planner on held-out topology families while keeping the downstream selection and execution mechanisms fixed. Under this controlled setting, the proposed memory improves admission by $4.6$--$11.5$ percentage points over the same planner without memory, while importance-based retention accounts for most of the improvement over a first-in-first-out store.

---


### 121. [Verify--Backtrack Loop: Structured Precondition Recovery for Long-Horizon Language Agents](https://arxiv.org/abs/2610.41564)

**<font color=#1a73e8>作者：</font>** Mingyang Liu, Qingcan Kang, Shixiong Kai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly tackle long-horizon tasks in interactive environments, where actions often depend on latent preconditions. The core difficulty is not trajectory length but recovery: when a prerequisite is missing or an earlier decomposition fails, trying another plausible action rarely helps. ReAct and later reflection or adaptive-planning methods support local correction, but express recovery as free-form text, with no explicit control state linking the terminal goal, the active goal, and the failure source. We introduce the Verify--Backtrack Loop (VBL), a training-free extension of ReAct that turns precondition discovery and failure diagnosis into structured planning-state updates. VBL maintains the task decomposition as a bounded goal stack and, on goal activation, execution failure, or material state change, jointly verifies two horizons---whether the active goal contributes to the terminal goal and whether it is feasible in the current state. These dual-horizon judgments, combined with typed failure attribution, trigger explicit operations---Push, Pop, retry, or BacktrackTo the parent. We evaluate VBL with Qwen3.5-9B, GPT-4o, and DeepSeek-V3.2 on AppWorld, ALFWorld, and ScienceWorld. VBL improves over ReAct and reflection-based control on every backbone--benchmark pair. On the challenging AppWorld setting, it improves task success by up to 22.07 percentage points over ReAct. Ablations show that removing either verification or diagnosis degrades performance, in several settings below ReAct, confirming that the two mechanisms are complementary. These results show that reliable long-horizon interaction benefits from revising the planning state, not merely the next action.

---


### 122. [BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion](https://arxiv.org/abs/2610.41574)

**<font color=#1a73e8>作者：</font>** Ruurd J.A. Kuiper, Robert A. Bagheri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unlike autoregressive (AR) models, diffusion language models (DLMs) permit parallel token updates, flexible generation, and bidirectional attention, but leading systems rely on costly pretraining or full-model fine-tuning. We present Build Your Own DLM (BYOD), a generalizable LoRA-only recipe for parameter-efficient AR-to-DLM conversion. Without architecture-specific tuning, BYOD induces diffusion generation in Gemma 2 9B, Llama 3.1 8B, Qwen2.5 7B, and Ministral 8B; to our knowledge, this is the first reported AR-to-DLM conversion of a Mistral model. The adapters comprise 4.1-5.8% of final parameters while every base-model parameter remains frozen; each 25,000-iteration conversion needs at most 102.4M tokens, processed in 3.1-4.0 hours on one Google Colab GPU. All four models generate from fully masked sequences, use bidirectional context in a controlled attention test, and retain substantial parent-model knowledge. BYOD-Gemma is the strongest BYOD conversion on our nine-task evaluation, reaching 50.6% average accuracy compared with 51.9% for LLaDA 8B Instruct in the same harness. Open-generation quality at low network function evaluation (NFE) budgets remains the principal limitation: BYOD perplexity is 8.3-11.1 versus 4.1 for LLaDA and 2.2-3.0 for the AR parents when generating 128 tokens in 64 steps. To enable further experimentation and inspection, we provide a standalone training and evaluation implementation and interactive demos for all four conversions. BYOD thus provides a practical route for extending diffusion generation to other existing model families while identifying the gap that efficient conversion must next close.

---


### 123. [Real Computation or Merely Naming? A Pre-Registered Mechanism Audit of 25 Cognitive-Architecture Modules in an LLM-Based Agent System](https://arxiv.org/abs/2610.41604)

**<font color=#1a73e8>作者：</font>** Peter Chen, Ni Zhang, Ying Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent systems built on local large language models are increasingly marketed through the vocabulary of cognitive architecture: modules named global workspace, theory of mind, causal reasoning, or active inference are listed as features, and the presence of the name is taken as the presence of the mechanism. We ask the prior question -- does the named computation actually happen -- and contribute a transferable verification method for the claim-implementation gap: a four-question static audit protocol with line-number evidence and call-chain tracing, demonstrated on two systems. We audit a system claiming 25 cognitive mechanisms, pre-register falsifiable predictions for 11 modules and execute the interventions, replicate the protocol on the IIT-phi core of a second, independent system with its own pre-committed falsification criteria, and run two repair experiments as positive controls. In 18 of 25 modules the computed value never reaches any production output; three idle-wiring shapes new to the dead-code and code-smell literatures emerge (connected-but-never-called, called-but-inert, called-but-content-blind). Of 61 frozen criteria across 12 interventions, 53 were confirmed, two partially adjudicated, five falsified, one adjudication-ambiguous. Repairs raised planner task success from 0.028 to 1.000 and cut state-controller error by 52%. Module names and module computations must be audited as independent claims; the protocol and the five-class failure taxonomy are reusable for the claim-implementation gap at two-system, case-level depth.

---


### 124. [What Should LLMs Forget: Reinforcement Unlearning of Knowledge Associations](https://arxiv.org/abs/2610.41616)

**<font color=#1a73e8>作者：</font>** Wutong Xu, Yun Qu, Haiyan Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) acquire extensive factual knowledge during pre-training, which may include sensitive, private, or copyrighted information, motivating the development of unlearning methods that selectively remove specific knowledge while preserving general capabilities. However, existing approaches typically optimize entire responses without explicitly identifying the knowledge to be forgotten, resulting in coarse and uncontrolled forgetting. To address this, we revisit the forgetting target of LLM unlearning and introduce Knowledge Association (KA), which characterizes the association between a query context and its target knowledge and is instantiated by the corresponding conditional predictive distribution, as the fundamental target of forgetting. Based on KA, we propose Knowledge Association Reinforcement Unlearning (KARU), a unified reinforcement learning framework that suppresses forgotten knowledge associations while preserving retained ones. Specifically, KARU derives complementary mechanisms from the KA-based formulation: token-level reward construction for finer-grained forgetting supervision, distribution-level regularization for precise knowledge suppression, and proximity-aware retain sampling to mitigate collateral degradation. Experiments across diverse LLMs on representative benchmarks demonstrate that KARU consistently improves forgetting effectiveness over existing baselines while maintaining comparable retention performance and general utility.

---


### 125. [Attention Maps Know When to Think: Training-Free Difficulty-Aware Chain-of-Thought for Reasoning Segmentation](https://arxiv.org/abs/2610.41618)

**<font color=#1a73e8>作者：</font>** Chanseul Cho, Jaesung Jun, Dongheon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) prompting has become a standard reasoning strategy in Multi-modal Large Language Models (MLLMs), showing strong performance in complex vision-language tasks such as reasoning segmentation. However, our analysis reveals that indiscriminate CoT usage can lead to degraded performance by inducing unnecessary reasoning, a phenomenon we term overthinking. In reasoning segmentation, overthinking often leads to misalignment between the query's intent and visual grounding. To address this, we propose Difficulty-Aware Chain-of-Thought (DA-CoT), a training-free adaptive framework that selectively triggers CoT based on the input's intrinsic difficulty. We find that the entropy of the model's attention maps reliably reflects task difficulty: low entropy indicates confident, localized grounding, while high entropy suggests uncertainty and potential benefit from CoT. DA-CoT uses this entropy signal to determine whether to apply CoT prompting. Additionally, we introduce a Bidirectional Rethinking mechanism that enables the model to automatically flip its reasoning decision when the initial output fails, enhancing robustness by recovering from failures induced by overthinking and underthinking. DA-CoT demonstrates its effectiveness by achieving state-of-the-art performance on the Reasoning Segmentation benchmarks while significantly improving inference efficiency.

---


### 126. [GRIT: Gradient Masking for Visually Misgrounded Tokens in Text-Rich Reasoning](https://arxiv.org/abs/2610.41629)

**<font color=#1a73e8>作者：</font>** Chanseul Cho, Noori Bae, Dongheon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has recently been extended to vision-language models (VLMs), yet its effectiveness remains limited for text-rich reasoning tasks. We highlight a key factor contributing to this limitation: models frequently arrive at correct final answers despite misperceiving visual information during intermediate steps. We define this phenomenon as Correct-but-Visually-Misgrounded Reasoning (CVMR). Because standard RLVR rewards only final-answer correctness, it fails to differentiate between properly grounded and misgrounded reasoning, reinforcing both equally. Through token-level analysis, we reveal that CVMR tokens exhibit distinct attention patterns that differ systematically from well-grounded ones. Based on this observation, we propose GRIT, a training framework that incorporates visual grounding into RLVR to mitigate the impact of CVMR. Furthermore, to address the lack of text-rich reasoning benchmarks that allow for systematic evaluation across text length and reasoning depth, we introduce GRIT-Bench. Experiments demonstrate that GRIT significantly improves both reasoning accuracy and grounding fidelity over existing RLVR methods.

---


### 127. [When Depth Lies: Benchmarking Vision-Language Models on Mirror-Induced RGB-D Ambiguity](https://arxiv.org/abs/2610.41651)

**<font color=#1a73e8>作者：</font>** Hao Yin, Tianchen Guo, Heming Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have made significant progress in spatial reasoning, particularly by integrating RGB images with depth data, which is often assumed to faithfully reflect physical distances. However, mirrors violate this assumption: they distort depth readings while reproducing object appearances, making reflections difficult to distinguish from real objects. As existing benchmarks rarely consider such reflective scenarios, VLM performance in mirror scenes remains largely unexplored. In this work, we introduce a mirror-centric RGB-D dataset from reflective scenes to evaluate the spatial reasoning capabilities of state-of-the-art VLMs in these scenarios. Specifically, we collect 1,011 RGB-D images from 525 real-world scenes, spanning diverse indoor and outdoor environments, six reflective surface types, and both daytime and nighttime conditions. All images are annotated with reflective surface region masks and mask annotations for both directly observed and mirror-reflected objects. Then, we curate a benchmark named MIRA-Bench (Mirror-Induced Reasoning Ambiguity Benchmark), comprising 14,140 QA pairs across eight sub-tasks organized into three cognitive levels: Reflection-aware Perception, Spatial Reasoning, and Scene-level Decision-making. We evaluate state-of-the-art VLMs on MIRA-Bench and find consistent failures across tasks: models misclassify whether objects are directly observed or reflected, fail to match reflected instances to their real-world counterparts, and produce erroneous spatial inferences. Remarkably, providing depth data actually degrades reasoning performance, implying that VLMs cannot identify incorrect depth in mirror scenes. The code and data are available at this https URL

---


### 128. [When Steering Shifts Discourse: Identifying and Intervening on Discourse-Level Changes due to Activation Steering in LLMs](https://arxiv.org/abs/2610.41661)

**<font color=#1a73e8>作者：</font>** Shivam Adarsh, Hetianyu Huang, Lau Safin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering is an inference-time technique used to control or modify the behavior, tone, or safety properties of a large language model (LLM) without retraining the model's weights or editing its input prompt, but simply by adding a vector to its residual-stream activations. However, activation steering also changes the generated text in unintended ways, unrelated to intended behavior change, that are not well understood. Prior work has measured these changes only through coarse signals such as perplexity. In this work, we show that steering systematically produces significant changes in discourse dimensions of the generated text, such as its formality, use of evidence, and ambiguity. We present a way of countering this by adding a second, complementary vector that targets the affected discourse dimension. This intervention restores about 78% of the unintended discourse changes while preserving the intended steering behavior in about 93% of the generations.

---


### 129. [Breaking Information Islands in Sparse Tuning via Small-World Connectivity](https://arxiv.org/abs/2610.41665)

**<font color=#1a73e8>作者：</font>** Xianchao Guan, Zijun Xiong, Yifeng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse tuning is widely used to adapt large language models due to its parameter efficiency. However, its effectiveness depends not only on the number of trainable parameters, but also on the feature-interaction topology of the sparse update's structural support. Limited or uneven connectivity in this support may isolate subsets of feature dimensions, forming information islands that restrict direct task-specific interactions through the trainable update. To address this issue, we propose Small-World Induced Fine-Tuning (SWIFT), a sparse tuning framework inspired by small-world connectivity. SWIFT combines block-diagonal sparse updates for local feature mixing with a fixed deterministic scattering permutation that routes the mixed outputs across feature groups without additional trainable parameters. We further show theoretically that certain random sparse-update models and block-diagonal updates can exhibit information islands, whereas a sufficiently scattering permutation guarantees positive block-level expansion when the trainable block-diagonal factor consists of equal-sized, structurally dense square blocks. Extensive experiments on commonsense reasoning, natural language generation, and image classification demonstrate that SWIFT outperforms the evaluated parameter-efficient fine-tuning (PEFT) baselines on average and can match or surpass full fine-tuning. Implementation is available at this https URL

---


### 130. [Does Reasoning Make Language Models Agree?](https://arxiv.org/abs/2610.41691)

**<font color=#1a73e8>作者：</font>** Mila Gorecki, Moritz Hardt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models face two opposing concerns: monoculture, in which models err in correlated ways, and multiplicity, in which equally accurate models make conflicting decisions. The rise of reasoning models has complicated this debate: On the one hand, reasoning may increase model agreement if models anchor on the same salient features or follow similar reasoning paths. On the other hand, stochastic reasoning traces may introduce additional branch points leading to more diverse predictions. We resolve this tension by distinguishing reasoning as an intervention from reasoning as an observed behavior. We compare agreement under controlled changes in reasoning effort with agreement across observed reasoning lengths, measuring both against the agreement expected from model accuracy. Across nine models from two developers and three classification tasks, enabling reasoning increases agreement between models evaluated on the same individuals. Yet the individuals who elicit longer reasoning traces receive less consistent predictions across models. Both patterns persist after accounting for differences in accuracy. Asking models to reason more thus promotes agreement, while observing them reason longer signals disagreement.

---


### 131. [TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents](https://arxiv.org/abs/2610.41697)

**<font color=#1a73e8>作者：</font>** Rui Yu, Chong Mu, Jinchuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training interactive language agents from terminal outcomes poses three coupled problems: which task and state continuations to sample, how to assign delayed feedback to decisions, and how to aggregate token losses for multi-token actions. We present TSBPO, a tree-structured sampling-to-update paradigm that addresses these problems within one training loop. A likelihood-fitted Root/Branch allocator uses retained task and state evidence to target continuations likely to produce contrasting terminal outcomes under fixed rollout budgets. On the resulting replayed physical trees, trajectory advantages compare immediate sibling segments, while observation-group step advantages compare outcomes at matched task/observation states. The actor then sums clipped token surrogates over each complete response and normalizes across active turns, avoiding response-length averaging in the policy-gradient term. With a Qwen2.5-1.5B actor, fixed checkpoints obtain 97.79% seen and 96.64% unseen stochastic success on ALFWorld and an 81.07% per-episode success rate over six stochastic episodes for each of the 500 WebShop test goals. A WebShop step-term ablation yields 75.93% at the same update-100 evaluation; an ALFWorld aggregation comparison shows higher observed command validity with complete-turn weighting. These results support the evaluated training configuration on two interactive benchmarks.

---


### 132. [Precision--Recall Trade-off on the Inference Level for LLMs in Grammatical Error Correction](https://arxiv.org/abs/2610.41698)

**<font color=#1a73e8>作者：</font>** Ryszard Staruch, Filip Graliński  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently been adopted for Grammatical Error Correction (GEC), achieving strong performance via both full fine-tuning and prompt-based approaches. As probabilistic sequence models, LLMs expose inference-time parameters that directly modify token generation behavior; however, their potential for controlling GEC-specific trade-offs has not been systematically studied. In this work, we investigate decoding strategies for grammatical error correction. We show that the repetition penalty parameter enables controllable adjustment of the precision--recall trade-off at inference time, without modifying the model architecture, training procedure, or prompt. Through experiments on standard GEC benchmarks, we demonstrate that repetition-penalty-based decoding enables inference-time control of the precision--recall balance, conceptually related to methods previously proposed for sequence-to-sequence GEC models, such as Align-and-Predict Decoding (APD), while remaining simple and broadly applicable to existing LLMs that expose inference-time decoding penalties.

---


### 133. [GraphNIAH: A Benchmark for Long-Context Reasoning over Real-World Graphs](https://arxiv.org/abs/2610.41704)

**<font color=#1a73e8>作者：</font>** Minh-Nam Tran, Abulhair Saparov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The needle-in-a-haystack (NIAH) benchmark was introduced as a test for measuring a model's ability to find small relevant facts within a very large body of input text. However, existing NIAH benchmarks each suffer from one or more of the following limitations: (1) reliance on synthetic data, so their evaluations may not generalize to real-world settings; (2) reuse of previously published datasets, leading to the risk of benchmark contamination; (3) dependence on manual annotation, which requires human effort to create and update data and is prone to future benchmark contamination; and (4) unrealistic simplification of long-context multi-hop reasoning where each next step is trivial given previous steps, while real-world reasoning often requires planning over multiple possible proof paths. To address these limitations, we introduce \Benchmark, a dynamic benchmark built from real citation relationships among scientific papers published after the evaluated models' knowledge cutoff date, which utilizes real-world information while ensuring no benchmark contamination. The fully automated benchmark construction pipeline samples representative subgraphs of the citation graph formed by these papers and converts each subgraph into a long-context QA example with a verifiable answer. We use GraphNIAH to evaluate eight LLMs from the GPT-5.6, Gemini-3, and Qwen3.5 families. We find that accuracy falls as questions require longer reasoning paths: at question depths of 16 and 32, the GPT-5.6 and Qwen3.5 models answer YES/NO questions no better than random guessing, mostly by answering NO; four of the eight models answer no counting example correctly, and the others model get worse as the subgraph size increases. These findings suggest that current LLMs often stop searching the citation relationships in their context before they reach the answer, even though every fact they need is in the context.

---


### 134. [Advancing Clinical Trial Outcome Prediction with Domain-Specific Large Language Models](https://arxiv.org/abs/2610.41710)

**<font color=#1a73e8>作者：</font>** Burak Bakkar, Hana Moalla, Mohamed Salem Jedidi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical trial failures are a major barrier to efficient drug development, incurring substantial costs and delaying patient access to effective therapies. Structured approaches such as the Hierarchical Interaction Network (HINT) predict trial outcomes by explicitly modelling interactions between drugs, diseases and protocols, but make limited use of the free text in trial registrations. We evaluate two domain-specific language models, BioBERT (108M parameters) and BioMistral (7B parameters), for phase-level outcome prediction on the TOP benchmark (12,477 trials), representing each trial as text built from ten this http URL fields. We compare fine-tuning (full fine-tuning for BioBERT, low-rank adaptation for BioMistral) with probing, in which the pretrained model is frozen and only a lightweight classifier is trained on its embeddings. On the held-out test set of each phase, all four language-model variants achieved higher ROC-AUC (0.613--0.772) and PR-AUC (0.649--0.901) than the published HINT results, corresponding to relative PR-AUC gains of 10--20\%. F1 differences were small and mixed, and no model, including HINT, clearly exceeded the F1 of a trivial classifier that predicts success for every trial. Under the configurations tested, probing performed comparably to fine-tuning: fine-tuned models scored highest on ROC-AUC and PR-AUC in Phases I and II, and frozen BioMistral embeddings in Phase III (ROC-AUC 0.772; PR-AUC 0.901), although most differences between variants were below 0.03 and were not tested for significance. These results suggest that pretrained biomedical representations already encode signal relevant to trial outcome, and that probing is a computationally cheaper alternative to fine-tuning for this task.

---


### 135. [Simple Features Beat Most AI Control Monitors](https://arxiv.org/abs/2610.41713)

**<font color=#1a73e8>作者：</font>** Shubhrangshu Debsarkar, Valmik Nahata  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI control relies on monitors to catch a capable model that sabotages its work. These monitors are evaluated on their ability to differentiate honest from backdoored code. We show that on a standard evaluation dataset, simple features beat most monitors without ever running the code, outranking 20 of 24 open-weight models prompted as monitors. The dataset gives its labels away in two ways. People wrote the honest solutions and older language models the backdoors, so the style of the code reveals the class. Additionally, problems that LLMs can backdoor have different characteristics, so basic facts about the problem reveal it too. Swapping one class at a time for code by Claude Sonnet 5 shows that these features reward a contrast between authors, since human code against Sonnet 5's backdoors is easier to separate than the original pairs, 0.95 against 0.79. One in seven backdoors in the standard test set fails our validity checks, which distorts comparisons between attackers. A Sonnet 5 monitor appears to catch 77% of the older models' backdoors but 37% of Sonnet 5's, and 78% against 61% once both are verified. We do not show that published monitors rely on these shortcuts, but our findings suggest that a high score on such a dataset is not by itself evidence of sabotage detection. We release the rebuilt dataset and checks.

---


### 136. [UpLoop: Training Looped Transformers via Upcycling at No Extra Pretraining Compute](https://arxiv.org/abs/2610.41720)

**<font color=#1a73e8>作者：</font>** Cheng Liang, Tengfei Zhang, Ya Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models can strengthen reasoning through repeated computation with shared weights, increasing execution depth without adding independent parameters. However, each additional pass increases training floating-point operations (FLOPs), making these gains more expensive to obtain. To address this cost, we propose UpLoop, a pretraining schedule that uses upcycling to train looped Transformers while exactly matching a standard dense baseline in final parameter count, total training tokens, and training FLOPs. Specifically, UpLoop begins with a shallow Transformer, progressively grows its depth by copying learned layers, and uses the computation saved early to support repeated execution of a shared middle block later in training. Experiments across model scales show improvements in language modeling and downstream performance, with the average score across 22 downstream tasks increasing from 22.99 to 27.52 at 1.3B parameters. These gains also extend to mathematical reasoning after supervised fine-tuning.

---


### 137. [From Training Exposure to Membership Evidence: A Controlled Study of OLMo 2](https://arxiv.org/abs/2610.41732)

**<font color=#1a73e8>作者：</font>** Ali Banaei, Muhammad Shahab Shahzad, Gerald Q. Maguire Jr. 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Whether a language model was trained on a document matters for copyright, privacy, and benchmark contamination. Yet most membership-inference (MI) evaluations on language models collect members and non-members after the fact, so success may reflect distribution shift and failure is inconclusive. We re-ran OLMo 2 1B's official 50-billion-token mid-training stage, replacing selected training chunks with documents from 7,814 pairs matched on domain and difficulty. For each pair, a coin flip determined which document was inserted and which was held out. The run released by the Allen Institute for AI (AI2) from the same seed saw identical data everywhere else and serves as the counterfactual. One exposure raises a previously unseen document's likelihood on average but rarely identifies it. Using the counterfactual as reference, the reference ratio has an area under the ROC curve (AUC) of 0.767 but, with one threshold across domains, catches 3.8% of members at a 1% false-positive rate (FPR). In contrast, 13 matched pairs give a paired test 80% power at the 5% level to detect training on a collection, given same-domain non-members and a close reference. A reference trained with another seed recovers 92% of the counterfactual's AUC advantage over chance, whereas reference-free attacks stay within 0.07 of chance when pooled over domains. The full official post-training recipe, re-run on both models, leaves 89% of the average effect. Even with a closely matched reference, substantial document-level variability limits individual membership inference. We will release the checkpoints, per-token log-probabilities, and the evaluation documents; the code is available at this https URL.

---


### 138. [Task Vectors Can Be Linearly Decomposed into Interpretable and Controllable Components](https://arxiv.org/abs/2610.41743)

**<font color=#1a73e8>作者：</font>** Yukiya Horiba, Hakaze Cho, Takahiro Yakoh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task Vectors (TVs) provide a compact way to steer large language models, but they are typically treated as atomized directions merely extracted from hidden states, leaving their internal functional structure poorly understood. Motivated by prior work that decomposes in-context learning into Task Recognition (TR) and Task Learning (TL), we ask whether a single TV can likewise be decomposed into functionally meaningful components. We formulate a TR/TL-based decomposition from candidate-label unembeddings, separating each TV into TR, TL, and residual components, and try to optimize the TR and TL coefficients using Bayesian optimization for more effective intervention. We evaluate this formulation across multiple model families, classification tasks, and both instruction- and demonstration-based TVs. Across these settings, TR/TL-based optimization identifies intervention directions that outperform the original TVs. Although optimization over random directions can also improve performance, TR/TL-based search yields more reliable gains, particularly for instruction-based TVs. Moreover, isolated interventions on the decomposed components produce distinct logit-level effects that are consistent with their intended functional roles. Together, these results suggest that TVs are not monolithic steering directions, but can be decomposed into functionally meaningful components that support both interpretation and control.

---


### 139. [Do LLMs Know When They Are Wrong About Molecules? In-Context Property Prediction with Self-Reported Uncertainty](https://arxiv.org/abs/2610.41745)

**<font color=#1a73e8>作者：</font>** Matthias Busch, Marius Tacke, Tamadur Albaraghtheh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are used in many domains, but molecular property prediction with them is still little explored. In this work we evaluate the capability of 7 frontier LLMs to predict molecular properties together with a self-reported uncertainty from in-context examples, and compare them with classical baselines trained on the same molecules. We use 4 datasets and screen each for contamination of the training data of the LLMs: three are clean, and the fourth, ESOL, is memorised by most of the models and serves as a comparison. On the clean datasets every LLM improves with the context, at 30 examples the most accurate one beats every baseline. The requested reasoning effort changes accuracy little. The self-reported uncertainty ranks the prediction errors weakly, with Spearman rank correlations of up to 0.46, about the level reached by the uncertainties of the baselines. Combining uncertainty and prediction, on lipophilicity the most certain half of the best LLM is the most accurate at small context sizes; on BACE and antiviral, and on lipophilicity at large context sizes, the best LLMs are on par with the best baseline. On the contaminated ESOL dataset the LLMs show no improvement with the context size, as expected for a memorised dataset, and their stated uncertainty is smaller on the molecules whose value they recall.

---


### 140. [Latent-Lens: Visual Perception in Small Language Models Through Latent Communication](https://arxiv.org/abs/2610.41751)

**<font color=#1a73e8>作者：</font>** Mo Shahdloo, Faegheh Sardari, Mathew Salvaris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bridging independent vision-language models (VLMs) and small language models (SLMs) in a modular multi-agent system typically forces them to exchange information as discrete text, which creates a lossy bottleneck for spatial and fine-grained details. This constraint is especially acute for SLMs, whose limited capacity makes them more reliant on the quality of the input signal. Recent latent-communication methods exchange states between language models. How a VLM can pass visual information to a separately pretrained text-only SLM though remains unexplored. We propose \textbf{Latent-Lens}, a lightweight codec that bridges the representation gap between a frozen VLM and a frozen SLM directly in latent space, enabling them to communicate purely through hidden states. The codec consists of a domain encoder that projects hidden states from the VLM into the SLM's embedding space, and an attention decoder formalised as a LoRA that teaches the SLM to attend to these visual prefixes, while training only ${\sim}1.6$M parameters (0.2\% of the combined model size). On visual question answering (CLEVR, GQA), Latent-Lens achieves $81.0\pm7.9$\% and $65.4\pm5.4$\%, compared with $58.3\pm5.7$\% and $61.8\pm1.0$\% for text communication with the same LoRA budget (+30.2--69.8pp relative to frozen text communication), while on image captioning (Flickr8k) it improves over the same baseline by +16.5 (+18.8 frozen). We also evaluate Latent-Lens with TinyLlama-1.1B and InternVL2-1B, which use different architectures, vocabularies, and hidden dimensions.

---


### 141. [Multimodal In-Context Learning with Explicit Rule Induction](https://arxiv.org/abs/2610.41754)

**<font color=#1a73e8>作者：</font>** Yuquan Li, Xinyang Jiang, Yuhao Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central challenge in multimodal in-context learning (MICL) arises from tasks that are ill-defined without context and require uncovering the underlying rules from demonstrations. Existing methods predominantly treat MICL as direct input-output mapping, overlooking the importance of explicitly inducing and reasoning over such rules, limiting both performance and interpretability. We propose ERIM, Explicit Rule-Induction for Multimodal In-Context Learning, a unified framework that enhances MICL by explicitly inducing the latent rules governing demonstration samples. Leveraging the reasoning ability of multi-modal large language model (MLLM), ERIM constructs rule-centric MICL datasets, introduces explicit supervision for rule induction, and fine-tunes MLLM to perform explicit rule-induction via a two-stage training strategy that combines mixed cold-start supervised fine-tuning with reinforcement learning. Extensive experiments show consistent performance improvements across diverse MICL settings and demonstrate that correctly inducing underlying rules directly leads to stronger and more stable performance.

---


### 142. [Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought](https://arxiv.org/abs/2610.41769)

**<font color=#1a73e8>作者：</font>** Dicong Yu, Wenhua Wang, Tian Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning distillation is widely used to transfer the reasoning capabilities of large language models to smaller students through teacher-generated supervision. In the black-box setting, however, teachers may expose only final answers and brief solutions, leaving intermediate calculations and validity conditions unavailable and thus limiting the reasoning supervision available for distillation. We propose Stepwise Querying, which elicits step-specific explanations without requiring access to the teacher's internal chain-of-thought (CoT) traces. Independent queries to the same teacher request intermediate derivations, validity checks, and corrections for individual steps, the assembled solutions are then used for standard supervised fine-tuning. Across two teachers, two students, and four mathematics and code benchmarks, our method achieves the highest score in 14 of 16 comparisons with three baselines. We further introduce Stepwise Explanation Information Gain (SEIG), a diagnostic based on the log-ratio of a frozen student's probabilities of correct step completion under stepwise and global explanations. Analyses on GSM8K show that incorrect-answer trajectories can remain useful when they preserve valid intermediate reasoning, while further decomposition yields limited additional gains.

---


### 143. [Peeling the Matryoshka: Extracting Ontological Structure from Retrieval Embeddings](https://arxiv.org/abs/2610.41785)

**<font color=#1a73e8>作者：</font>** Eunchan Kim, Inwhee Joe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Taxonomy construction is essential for knowledge-intensive NLP yet remains costly: clustering-based methods (i) need careful per-corpus tuning and yield unstable hierarchies, while LLM-based pipelines (ii) depend on expensive task-specific training that does not transfer across domains. We report an empirical finding that bears on both: in Matryoshka Representation Learning (MRL) embeddings, where each leading prefix is itself a usable, coarser vector, prefix length aligns with the coarse-to-fine granularity of gold taxonomies; shuffled- and reverse-dimension controls isolate the alignment to the learned early prefix dimensions. The pattern holds across three architecturally distinct MRL models. To test whether this regularity is usable, we introduce PEEL (Peeling Embeddings to Extract Latent ontologies): a minimal probe over these frozen embeddings, trained once with an order-embedding objective that represents hierarchy as vector containment; a minimum spanning arborescence then decodes taxonomic DAGs. Using only a concept vocabulary (no documents), PEEL recovers taxonomic DAGs with high structural fidelity on two OLLM benchmarks, transferring to a new domain with no target-edge supervision. The end-to-end OLLM pipeline, which jointly discovers concepts and induces structure from document corpora, is reported as a cross-task reference. Pre-trained retrieval embeddings encode a decodable granularity gradient; a minimal probe renders it as explicit parent-child (is-a) structure.

---


### 144. [Whose Values, Which Contexts, and What Signals? Grounding Cultural Value Alignment with Re3Culture](https://arxiv.org/abs/2610.41793)

**<font color=#1a73e8>作者：</font>** Jing Yao, Hyunjin Hwang, Weihua Zheng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cultural value alignment requires not only model optimization but also a well-specified target grounded in real-human evidence. Yet how such targets should be grounded in human data remains largely unexplored, raising three fundamental questions: (1) whose values should be represented? (2) where should cultural values be observed? and (3) what signals reveal underlying values? We investigate these questions through Re3Culture, a large-scale dataset linking (i) Representative communities: 700+ human participants across four cultures recruited through cultural-affiliation screening and demographic-aware sampling; (ii) Realistic scenario: culturally sensitive scenarios selected by community members, e.g., family and kinship; and (iii) Revealed value signals: 1,400+ value surveys, 20,000+ topic-grounded behavioral principles and explicit value priorities with responses for 6,000+ situated questions. Our analysis shows why these choices matter for defining the target, with three implications. First, estimating cultural values requires both community affiliation and broad internal coverage. Substituting other cultures or restricting subgroup coverage shifts value estimates. LLM simulations also disproportionately reflect particular subgroups. Second, values must be observed in concrete, community-guided situations. Abstract questionnaire profiles weakly recover situated priorities, and communities differ in which scenarios they identify as culturally value-revealing. Third, value priorities should be elicited explicitly, not learned from response preferences or bottom-line answers alone. Preferences conflate value agreement with other response-level qualities, and similar answers can be derived from different value priorities. By addressing these requirements, Re3Culture provides the first human-grounded resource that explicitly informs target definition for cultural value alignment.

---


### 145. [What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer](https://arxiv.org/abs/2610.41803)

**<font color=#1a73e8>作者：</font>** Mahmoud Abbasi, Juan M. Núñez V., Amin Shahraki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detectors can flag hijacked large language model (LLM) agents from the traces of the tools they call. In the eleven evaluations we audited, attacks or anomalies make up 16% to 86% of the test samples, no evaluation varies that share, and six report no test on data from a second benchmark or source. We ask what such evaluations hide. On the AgentDrift and AgentDojo benchmarks we test trained detectors that read tool identities, behavior, call sequences, step embeddings or text, and a released LLM action monitor, AlignmentCheck, with thresholds fixed on training data or set by the monitor's released decision rule. First, at a 2% attack rate a detector with an area under the receiver operating characteristic curve (AUROC) of 0.879 reaches a precision of 0.076, and the mix of negatives alone moves that precision between 0.039 and 0.117. Second, as tool coverage, the share of test tool calls whose tool was seen in training, falls, detector rankings cross near 50% coverage and reverse below it, because unseen tools map to inputs that training never reached. Dropout on tool inputs largely removes the reversal. Third, no detector trained on AgentDrift ranks AgentDojo traces better than chance (AUROC 0.47 to 0.52), including one that reaches 0.996 within AgentDojo. The monitor, trained on neither, reaches 0.930, but with its open backbone its released decision rule would still mostly raise false alerts at a 2% attack rate (precision 0.096). We turn these findings into a checklist for evaluating trace detectors.

---


### 146. [RECAST: REconstruction of Chain-of-Thought via Auditable Structured Traces](https://arxiv.org/abs/2610.41813)

**<font color=#1a73e8>作者：</font>** Qi Wang, Kang Xu, Chengcheng Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large closed-source reasoning models expose only their final answers. The intermediate reasoning that produces those answers is hidden behind API surfaces, tool-call policies, and safety filters. Existing chain-of-thought (CoT) extraction methods assume a side channel: a visible reasoning field, a scratchpad carried through tool calls, or a signed/encrypted reasoning block. We reproduce three representative state-of-the-art extraction methods and find that, on Claude-Sonnet-5.5 accessed through the standard chat-completions interface, all three return zero CoT tokens. The failure is structural rather than a bug: the reasoning field is absent, named tool selection is rejected, free-text scratchpad arguments are filtered, and no replayable reasoning block is exposed. We therefore take a different route. We present RECAST, a reconstruction-based framework that conditions a decoder on the question and the target model's final answer, reconstructs a first-person structured rationale, cleans it, and builds SFT-ready data. To the best of our knowledge, RECAST is the first system to reconstruct CoT from frontier closed models such as Claude-Sonnet-5.5, GPT-6.1, and Gemini 3 without using hidden reasoning channels. We instantiate RECAST on Claude-Sonnet-5.5 and additionally obtain successful qualitative reconstructions on GPT-6.1 and Gemini 3 with the same answer-only protocol. The system is open-source and packaged as an agent skill: one prompt deploys it and runs the complete pipeline to produce SFT-ready CoT data. This preprint describes the system, its threat model, and a controlled artifact validation; it does not claim large-scale benchmark improvements.

---


### 147. [Trainable Vector Quantization for Large Language Models](https://arxiv.org/abs/2610.41822)

**<font color=#1a73e8>作者：</font>** Anastasiia Prutianova, Alina Bogdanova, Mikhail Shutov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vector Quantization (VQ) is a rapidly evolving technique for compressing Large Language Model (LLM) weights, reducing memory usage, and speeding up inference. However, extreme compression deteriorates model performance, which is challenging to recover due to the discrete nature of VQ parameters. Existing methods employ training-free approaches that are limited to layer-wise reconstruction loss minimization. To address this limitation, we propose TVQ, a novel method that leverages straight-through estimation to enable gradient descent-based optimization of vector-quantized LLMs. By reformulating VQ LLM optimization with trainable latent weights, TVQ enables arbitrary objective minimization. We constitute our approach by applying TVQ in a block-wise knowledge distillation paradigm, which balances quality and training efficiency, and propose several practical solutions to accelerate training. In experiments on modern LLMs, we demonstrate that TVQ is compatible with modern VQ schemes. As a result, TVQ achieves state-of-the-art quality in low-bit post-training quantization settings with a modest training budget and straightforward PyTorch implementation. For instance, TVQ achieves near-lossless 2-bit quantization for LLaMA2-70B with only 1% accuracy drop on popular Question-Answering benchmarks.

---


### 148. [Open-Weight MLLMs Cannot Compare What They Cannot Name](https://arxiv.org/abs/2610.41841)

**<font color=#1a73e8>作者：</font>** Wenxin Su, Anna Kreshuk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly capable of understanding images and performing complex visual reasoning, suggesting the possibility of using them to automate biological image analysis. This need is becoming increasingly urgent as advances in technology continue to generate ever larger and more diverse microscopy datasets, already exceeding the scale at which manual visual analysis is feasible. With the final aim to use MLLMs for visual comparison of complex phenotypes, we investigate a very simple baseline: comparison of the size of body parts in synthetic images of ants. We find that state-of-the-art open-weight MLLMs fail for some body parts, but not for others, even though the comparison itself is visually trivial for all of them. We evaluate different in-context learning strategies and analyze performance on the related object recognition task. Our results suggest a recognition-driven grounding failure: structures that the models cannot recognize are instead associated with a recognizable semantic concept, impairing the grounding and comparison of both. Further analysis of the vision encoder is consistent with the hypothesis that fine-grained visual structure may be less well preserved without semantic support. Together, our results reveal a surprising limitation of current MLLMs: semantic recognition can gate simple visual comparisons that do not intrinsically require semantic understanding. Our code and data are available at this https URL

---


### 149. [SimXAI: A Simple Drop-in Layer Increases Interaction Quality and Understanding in Conversational XAI](https://arxiv.org/abs/2610.41856)

**<font color=#1a73e8>作者：</font>** Van Bach Nguyen, Qianli Wang, Nils Feldhus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational explainable AI (ConvXAI) agents often use GUS-style architectures with separate modules for intent recognition, dialogue management, and template-based response generation. While faithful to the underlying XAI methods, these pipelines are hard to adapt and often struggle with context-dependent follow-up questions. We present SimXAI, a lightweight LLM-centric conversational layer that replaces these modules with a single tool-calling LLM that bridges access to existing XAI resources. Rather than a standalone agent, SimXAI serves as a modular interface that enables conversational access to external XAI resources. We further introduce an evaluation suite for single- and multi-turn parsing, faithfulness, and contextualization. Across existing and new datasets, SimXAI achieves strong function-selection accuracy and high faithfulness while better handling context-dependent requests. In a user study replacing only the conversational layer of TalkToModel, a representative GUS-based agent, users completed tasks more accurately and in fewer turn. Overall, SimXAI improves GUS-based design while preserving faithfulness and improving conversational quality.

---


### 150. [Automated Keyword Generation Using LLMs in a High-Volume Data Virtualization Service](https://arxiv.org/abs/2610.41893)

**<font color=#1a73e8>作者：</font>** Saiful Khan, Yiwen Xing, Joyraj Chakraborty 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In modern data infrastructure, a data virtualization service (DVS) allows users to create many versions of source datasets for different processing tasks. For example, a multivariate or multi-modality dataset can be used for different machine learning tasks (e.g., classification, detection, segmentation, forecasting, and so on). Data selection, participation, integration, and preprocessing in different tasks result in many virtual datasets [Khan et al., SSC 2026]. Meanwhile, different users need to discover existing virtual datasets frequently and easily to avoid duplicate efforts. To enable an effective search engine in a DVS, it is desirable to automatically generate keywords for each virtual dataset. In this work, we present a solution for generating keywords for virtual datasets using large language models (LLMs). We propose five strategies for selecting different collections of text data for processing by the LLMs. We applied the five strategies to virtual datasets created in five application case studies with different source datasets. We conducted experiments with three LLM generators and two embedding techniques. The experiments show that the performances of the five strategies depend on the quality of the text descriptions. The results help us adopt a multi-strategy implementation of a new keyword generation service (KGS) as part of an extended DVS. The work demonstrates that the capability of automated keyword generation is indispensable for a high-volume DVS that is dataset-rich and frequently accessed.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
