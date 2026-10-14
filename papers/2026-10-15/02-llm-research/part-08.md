# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 351. [RIFT: Token Influence Follows the Path of Least Resistance](https://arxiv.org/abs/2610.16349)

**<font color=#1a73e8>作者：</font>** Tingan Jin, Shuhang Dong, Haosong Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Which context tokens drive a language model's answer? Graph-based tools such as attention rollout and attention flow answer this from a single forward pass, yet their faithfulness in decoder-only models is rarely tested against interventions. We view the layers of a decoder as a causal network whose conductances are attention weights, and read a token's influence on the answer from the resistance between them. We propose RIFT (Resistance-based Information Flow in Transformers), which scores a token by the series resistance of its path of least resistance to the answer, found exactly by a classic shortest-path dynamic program. On synthetic in-context retrieval tasks and extractive question answering over Wikipedia paragraphs, RIFT predicts the effect of replacing a token with a Spearman correlation of 0.52-0.68; predicting a single replacement, it reaches 77-96% of the agreement between two different random replacements. It needs no gradients and no extra forward passes, scoring every token of a prompt in 0.9-3.4 ms on one CPU thread, whereas the replacement experiment needs a forward pass per token. On 576 held-out prompts from four models of two families (Qwen3 and Llama 3.2), it outperforms token distance, attention rollout and attention flow in every pre-specified comparison, by 0.23 to 0.88 in mean Spearman correlation, and it is the best or tied-best of all attention-based scores we test. Aggregates that add up all routes (attention flow, effective resistance and rollout) instead mostly encode token position: as a simple proposition shows, early tokens have many more parallel routes to the answer.

---


### 352. [A Production-Grade, High-Efficiency Agentic RL Framework for Frontier LLMs with Validated Recipes](https://arxiv.org/abs/2610.16352)

**<font color=#1a73e8>作者：</font>** LoonSage Team, Bowei Song, Caiwei Zhao 等 48 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a critical phase in the post-training pipeline of large language models (LLMs). As the frontier of LLM capabilities shifts from static reasoning to agentic tasks--characterized by external tool invocation, multi-turn interactions, and long-horizon decision-making--existing mainstream RL frameworks have grown increasingly unwieldy, raising the overhead of adoption, usage, and debugging. To address these challenges, we present LoongSage, an agent-native, fully asynchronous RL framework with a lightweight core of roughly 14K lines of code. Built upon Megatron for distributed training and SGLang for high-throughput inference, LoongSage centralizes orchestration within a single controller process and encapsulates all GPU-resident components as Ray actors. It introduces AgentFlow, a unified execution paradigm that orchestrates both white-box and black-box agents. For asynchronous execution, it integrates sliding-window strategies that bound trajectory staleness, and employs TransferMesh, a topology-aware synchronization mechanism that routes weights after each step over the fastest transport available to each receiver. Beyond agentic RL, LoongSage incorporates a memory-efficient Teacher Manager that decouples the scaling of teacher models from GPU memory constraints, natively supporting Multi-Teacher On-Policy Distillation. Extensive evaluations across four complete training runs, spanning complex reinforcement learning and multi-teacher distillation, demonstrate that task rewards improve steadily while the train-inference gap is kept under continuous control, and the fully asynchronous pipeline removes synchronous idle bubbles, sustaining hardware utilization.

---


### 353. [Self-Distillation with Verbal Regularization](https://arxiv.org/abs/2610.16354)

**<font color=#1a73e8>作者：</font>** Jiazheng Li, Yawei Li, Junru Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a large language model using supervision from a teacher instantiated from the same model as the student. The teacher is conditioned on privileged information (PI), such as verified solutions. The student, which does not observe PI, learns from the teacher's next-token distributions along its own sampled responses. However, PI can bias supervision toward shortcut reasoning with limited verification or reconsideration, accompanied by a sharp drop in the entropy of the output distribution. To address this challenge, we introduce self-distillation with verbal regularization (VRSD), which uses system prompts to regulate how the teacher uses PI, thereby encouraging rethinking and exploration to counteract premature commitment. Theoretically, we model prompting as attenuating the influence of PI on the teacher distribution and derive conditions for entropy preservation. Across three models and four tasks, VRSD improves Pass@1 over OPSD in 11 of 12 model-task settings, by 3.9 percentage points on average, while generally maintaining higher token entropy.

---


### 354. [HexaBee-4B: Six-Language Translation with Multilingual Answering and Bidirectional Supervision](https://arxiv.org/abs/2610.16361)

**<font color=#1a73e8>作者：</font>** Iman Barati, Mohammadmostafa Rostamkhani, Mohammad Badzohreh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual translation requires a model to preserve meaning while producing text in a requested language. We present HexaBee-4B, a translator adapted from Gemma 3 4B IT through three stages: Wikipedia continued pretraining, joint multilingual answering and answer-text translation, and bidirectional translation specialization. The intermediate stage connects two tasks through shared multilingual answers: answering a question in the requested language and translating an answer into that language. It comprises 19.46 million answering records, including 5.76 million cross-language question-answer pairs, and 10.70 million answer-text translations. The final stage uses 658,274 forward and reverse synthetic translation examples. On 36,572 synthetic test examples spanning all 30 directions among Arabic, Chinese, English, Hebrew, Persian, and Spanish, HexaBee-4B achieves direction-macro chrF++ of 73.75, compared with 57.11 for Gemma 3 4B IT and 66.83 for Gemma 3 12B IT. BLEU, TER, COMET, and a matched model-judged subset support the same overall ranking. These results demonstrate improved translation across the six-language set, with chrF++ gains in every evaluated direction over both baselines.

---


### 355. [From Sound to Sense: An Anatomy of Semantic Supervision for Speech-Driven Visual Grounding in Remote Sensing Imagery](https://arxiv.org/abs/2610.16364)

**<font color=#1a73e8>作者：</font>** Zhongyu Pang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speech-driven visual grounding in remote sensing (RSVG) removes the typing bottleneck of text-based interaction and is intended to preserve prosodic intent, enabling hands-free target acquisition in time-critical missions. The direct-audio paradigm, mapping raw speech straight to a bounding box and bypassing automatic speech recognition (ASR), was recently adopted by RSTalker, but what such grounders actually learn about language remains unmeasured. SemEcho grafts a frozen Whisper speech pathway onto a VLTVG grounding host so that speech and text share one decoder, making the paired text, free by construction since speech corpora in this task are synthesized from DIOR-RSVG expressions, a training-time teacher and a fair, same-host text upper bound. On this instrument we dissect three semantic injection channels (feature-mimicry distillation, word-level CTC supervision, and two-stage ASR pretraining) with linear semantic probes, and release Audio-DIOR-R (80,973 training clips; 10 timbres x K=3; Qwen3-TTS synthesis with online sox noise lambda in [0, 0.4]) and Audio-DIOR-Comp, a re-split holding out 17 attribute-category combinations under a 2x2 acoustic-semantic protocol. Our anatomy yields four findings. (i) Whether direct alignment beats a domain-trained ASR cascade is decided by recognizer quality: against a weak in-domain cascade (CTC 0.53) direct wins by 9.0 Acc@0.5 points with transcription errors concentrated on spatial-relation words, but a strong in-domain cascade (CTC 0.029) reaches the text upper bound (80.8 vs. 81.0) and beats even the strongest direct model by 8.8 points; the anti-ASR premise holds only against weak recognizers.

---


### 356. [LoopQuant: Accurate and Efficient Post-Training Quantization for Looped Transformers](https://arxiv.org/abs/2610.16368)

**<font color=#1a73e8>作者：</font>** Zhixiong Zhao, Zukang Xu, Xing Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Language Models (LoopLMs) improve parameter efficiency by recursively reusing shared Transformer modules, yet their repeated computation over evolving recurrent states poses new challenges for low-bit deployment. Existing post-training quantization (PTQ) methods, largely designed for feed-forward Transformers, fail to account for cross-loop activation dynamics, heterogeneous loop sensitivity, and recursive error propagation, leading to substantial performance degradation at low precision. To address these challenges, we propose LoopQuant, a loop-aware PTQ framework for accurate and efficient low-bit quantization of LoopLMs. LoopQuant is built on three core components: 1) Cross-Loop Distribution Canonicalization (CLDC) learns a shared quantization-friendly representation across recurrent states while preserving parameter sharing; 2) Interaction-Aware Loop-wise Precision Allocation (ILPA) allocates activation precision under a fixed bit budget by modeling task-level loop sensitivity and cross-loop interactions; and 3) Loop-Conditioned Task Calibration (LCTC) further aligns quantized inference with the low-bit recursive trajectory through lightweight task-space calibration. Extensive experiments across LoopLM architectures demonstrate that LoopQuant consistently outperforms existing low-bit PTQ methods. On Ouro-2.6B, LoopQuant under W4A4 surpasses all W4A8 baselines in performance, while reducing model memory by 65.3% with only 3.4% additional storage overhead over naive INT4 and achieving a 1.7 times decoding speedup over BF16. These results demonstrate a strong balance among accuracy, compression, and inference efficiency, providing a practical and deployment-friendly solution for low-bit LoopLM inference. The code is available at [this https URL].

---


### 357. [Rule vs.Consequence: Dissociable Internal Representations of Moral Reasoning in LLMs](https://arxiv.org/abs/2610.16371)

**<font color=#1a73e8>作者：</font>** Eugenie Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in morally and legally sensitive contexts, yet little is known about how they internally represent distinctions between moral reasoning styles. We ask whether a model's differential response to rule-framed and consequence-framed moral questions reflects distinct internal structure or merely surface lexical sensitivity. We construct a 2$\times$2 factorial dataset crossing reasoning style (rule-based vs. consequence-based framing) with judgment polarity (permissive vs. prohibitive), drawn from three established moral reasoning benchmarks and evaluated on a cleanroom test set of novel phrasings that includes conflict pairs where the two framings predict opposite labels. Using linear probing and activation steering, we identify two orthogonal directions in the residual stream: Dir-A tracks reasoning style and Dir-B tracks judgment polarity, each near-blind to the other factor (cross-correlation $|r| < 0.04$). This double dissociation replicates across three instruction-tuned models from different developers at comparable proportional depth, and it is not knife-edged in layer: the directions are recoverable and causally effective throughout an extended band of the network. Dir-A can causally change judgments, and in conflicting scenarios, it selectively corrects errors in rule-based judgments without changing consequence-based judgments, suggesting that it does not simply make the model more likely to accept everything. Generalization beyond the training templates is partial: the direction transfers across benchmark sources, but its advantage over lexical baselines on novel phrasings is modest. We therefore frame the result as moral reasoning style sensitivity, a geometrically dissociable and causally effective structure, rather than internalized normative reasoning.

---


### 358. [PersonaFactor: Preference Factors with Dynamic Selection for LLM Personalization](https://arxiv.org/abs/2610.16372)

**<font color=#1a73e8>作者：</font>** Hang Su, Zequn Liu, Jianghan Chao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although users may express different personalization needs across tasks, these task-specific behaviors can reflect shared underlying preference mechanisms. Existing LLM personalization methods often focus on surface-level interactions or undifferentiated histories, overlooking the shared mechanisms underlying these behaviors. We introduce PersonaFactors, a framework that distills reusable and interpretable personalization factors from heterogeneous user interactions. We construct a library of thirteen PersonaFactors by extracting evidence-grounded rationales and clustering recurring patterns across tasks, and develop a dynamic factor-guided generation framework that selects factors relevant to each user's history and current request. Across four personalization benchmarks and four backbone models, Dynamic PersonaFactor achieves the best score on every reported metric. Representation analyses further show that PersonaFactors and user history induce partially overlapping low-dimensional representations, and that their joint use yields complementary shifts. Taken together, these findings suggest that factor-based and history-based personalization can mutually reinforce each other.

---


### 359. [RetroPlanner: Multi-Route Expansion and Multi-Objective Reasoning for LLM-Based Retrosynthesis Planning](https://arxiv.org/abs/2610.16391)

**<font color=#1a73e8>作者：</font>** Ye Rin Kim, Yongjun Jeong, Seongjun Yun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step retrosynthesis planning is often considered solved once a route to purchasable starting materials is found, but such a route should also be practical in real-world chemistry. Recent LLM-based planners formulate this process as sequential decision-making over an AND-OR graph, yet typically expand a single molecule per turn and are optimized for solvability alone, leaving alternative routes uncompared across the multiple objectives that determine practicality before the search budget is committed. We introduce RetroPlanner, an LLM-based planner that jointly compares multiple routes to steer the search toward higher synthesizability, as measured by reaction plausibility, round-trip consistency, and starting-material price. RetroPlanner is trained to reason over chemical evidence: structural progress from the target molecule, bond changes and reaction classes, where candidate routes diverge from one another, and how they rank across multiple objectives. Experiments on multi-step retrosynthesis benchmarks demonstrate that RetroPlanner recovers more alternative routes than prior LLM-based planners while improving synthetic route quality and maintaining a high success rate.

---


### 360. [EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications](https://arxiv.org/abs/2610.16402)

**<font color=#1a73e8>作者：</font>** David Nukrai, Bar Alon, Nativ Levy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web application development often proceeds through successive requests that extend an existing implementation. Yet web-generation benchmarks primarily evaluate development toward fixed specifications. We introduce EvoWeb, a novel benchmark comprising 320 cumulative requests over 32 web applications, grounded in real-world product features and structured by functional dependency graphs. Agents iteratively modify a persistent codebase, while a multimodal web agent tests each intermediate application in a live browser, assessing newly requested functionality, cross-request integration, and previously requested functionality. To characterize reliability throughout development, we integrate trajectory performance across user-tolerance thresholds rather than impose a fixed stopping criterion. Experiments across open- and closed-source frontier models show that EvoWeb reveals clear performance differences between models, with cross-request integration emerging as a key challenge. Further analysis shows that later requests with deeper or more numerous dependencies are solved less accurately, while runtime errors become more frequent over successive requests. EvoWeb provides a testbed for evaluating and improving coding agents in long-horizon, multi-request development.

---


### 361. [SLS-Bench: A Benchmark for Incident Log Summarization with Synthetic Observability Data](https://arxiv.org/abs/2610.16412)

**<font color=#1a73e8>作者：</font>** Valerii Iakovlev, Markus Spanring, Martin Flechl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As IT systems grow in complexity, automated agent-driven incident response becomes increasingly critical. A key capability for these agents is summarizing large log streams into human-readable reports. Further progress requires meaningfully evaluating this function, yet existing benchmarks leave end-to-end summarization from large log streams underexplored due to the prohibitive cost and complexity of collecting real-world data. We introduce SLS-Bench, a benchmark for incident log summarization featuring 90 tasks grounded in real-world incident reports, each with a synthetic log stream and a reference summary. To construct SLS-Bench, we developed a data generation pipeline that converts incident reports into structured incident models, which guide the generation of synthetic logs and reference summaries. This pipeline combines narrative grounding, explicit incident modeling, generator-verifier loops, and statistical comparisons with real-world log streams to produce realistic and controllable observability data. Our evaluation of 14 LLMs on SLS-Bench shows that while frontier models can produce useful summaries, they do so at substantial cost and latency, and open-weight models lag significantly. SLS-Bench provides a framework for systematic evaluation of log analysis agents and a scalable blueprint for future synthetic observability benchmarks.

---


### 362. [Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State](https://arxiv.org/abs/2610.16414)

**<font color=#1a73e8>作者：</font>** Dongsheng Chen, Xiangyu Zhao, Lei Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-agent workflows routinely transform rich observations into plans, summaries, memories, handoffs, and other reusable state. This creates a privacy boundary that task relevance alone does not capture: an observation may be needed as evidence for a task without its full semantics being authorized to persist. We call this mismatch the purpose-to-state semantic gap. The key distinction is that evidence authority is not release authority. We introduce Purpose IR, a bounded typed intermediate representation that compiles natural-language user purpose into an executable semantic boundary for reusable agent state. A Purpose program is an acyclic semantic dataflow graph in which evidence leaves specify task-required semantics, typed dependencies constrain authorized derivations, and declared sinks determine which values or actions may cross the reusable-state boundary. A deterministic compiler constructs and validates the authoritative program, while a typed runtime reconstructs reusable state only from validated sink outputs. Under explicit execution contracts, this design yields release confinement and purpose noninterference, characterizing what factual semantics may be released and which observation differences must become irrelevant to reusable state. Across 1,200 cases spanning LangGraph, CrewAI, and MobileRun, Purpose IR achieves 99.6% Privacy, 83.3% Task, and 83.3% Privacy-Compliant Success (PCS), outperforming the strongest high-privacy baseline by 27.5 PCS points. On 493 PrivacyLens trajectories, it achieves the highest Safe Action Rate at 77.3%, 10.4 points above the next-best method, extending the same boundary from reusable state to downstream actions. These results show that privacy-preserving agent state requires more than filtering sensitive or task-irrelevant content: it requires an explicit, executable representation of what the user's purpose authorizes to survive.

---


### 363. [AuthGateBench: Benchmarking LLMs as Authorization Gate](https://arxiv.org/abs/2610.16426)

**<font color=#1a73e8>作者：</font>** Zhixiong Zhuang, Jin Jia, Zhiwei Shang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated approval systems let coding agents execute high-risk actions with minimal human oversight by delegating the authorization decision to a classifier, typically a large language model (LLM). Such systems, adopted in tools like Claude Code and Codex, remain vulnerable to failure modes such as scope escalation, where the agent takes actions exceeding what the user authorized. Existing benchmarks focus mainly on malicious requests, evaluating refusal under an implicit policy. We introduce AuthGateBench, the first policy-guided benchmark for authorization gating under benign requests. We implement a novel pipeline where an LLM generates contrast pairs with identical action and trajectory but differing request, flipping the label between block and allow. This allows us to assess whether models reason over context rather than the action alone. We further examine whether auxiliary environment signals can help models make better decisions. The resulting benchmark comprises 1,400 instances spanning five failure modes drawn from real-world Claude Code incidents. Evaluations show accuracy degrades unevenly across failure modes as models over-rely on internal safety alignment, and models still block most actions even when explicitly authorized, revealing unstable rather than deterministic decisions; retrospectively retrieved environment signals, however, substantially improve authorization accuracy.

---


### 364. [ARMED: Adaptive Retrieval-Augmented Medication Recommendation](https://arxiv.org/abs/2610.16440)

**<font color=#1a73e8>作者：</font>** Kyungkeon Chung, Se Un Park, Hyejin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medication recommendation requires jointly considering diagnoses, comorbidities, longitudinal patient history, and treatment interactions. Although recent retrieval-augmented generation approaches using language models have shown promise for clinical recommendation, most existing systems rely on fixed retrieval pipelines that cannot adapt to diverse clinical retrieval scenarios and may introduce noisy or irrelevant evidence. We propose ARMED, an adaptive clinical RAG framework that dynamically expands retrieval according to retrieval sufficiency and current-admission relevance. ARMED first observes the initial retrieval outcome and selectively performs supplementary or fallback multi-query retrieval when additional evidence is needed. The framework also incorporates a relevance gate that activates only clinically relevant same-patient history and organizes retrieved evidence into structured query-level clinical evidence. Experiments on MIMIC-IV demonstrate that ARMED consistently outperforms previous static retrieval baselines and improves overall medication recommendation quality. By combining locally runnable small language models with adaptive retrieval, ARMED supports medication recommendation without relying on external language model APIs or task-specific fine-tuning.

---


### 365. [VisExMEM: Visual Evidence-Based Explainable Multimodal Evaluation Metric](https://arxiv.org/abs/2610.16441)

**<font color=#1a73e8>作者：</font>** Subhadeep Roy, Christoph Leiter, Steffen Eger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current image-text evaluation often relies on a global score, which gives limited insight into which semantic details are supported by the image. Explainable metrics provide rationales, but the visual evidence supporting those rationales can still be difficult to verify. We introduce VisExMEM, a reference-free evaluator that decomposes captions into atomic claims, localizes visual evidence, verifies each claim, and averages claim-level support into a global score. Explanations use the same evidence and decisions. We train Qwen3.5-based 4B and 9B models on 100K samples with multi-task SFT, counterfactual refinement, and evidence-aware GDPO. Across eight benchmarks, VisExMEM-9B achieves the highest descriptive composite among open-source evaluators in our comparison, exceeding VQAScore by 11.7 points while remaining competitive with GPT-5.6 Sol. We also introduce AGITA-Bench, containing 600 human-annotated image-text pairs and 8.7K atomic claims for global and claim-level evaluation. For untuned Qwen3.5 and GPT-5.6 Sol controls, decomposed prompting raises the same composite by 3.6-5.1 points relative to holistic prompting. Human evaluation shows that VisExMEM explanations outperform prior explainable metrics and approach GPT-5.6 Sol.

---


### 366. [Pixels or Code? Benchmarking Instruction-Guided Visual Artifact Operation](https://arxiv.org/abs/2610.16444)

**<font color=#1a73e8>作者：</font>** Shun Guo, Shuizhou Shi, Boao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual artifacts such as charts, technical diagrams, webpages, and document pages underpin scientific, commercial, and engineering workflows. Editing these artifacts requires direct modification, dependency-aware updates, preservation of unaffected content, and compliance with domain constraints. We define this capability as Visual Artifact Operation (VAO). Prior benchmarks test parts of this problem, including cascading updates in charts. We study direct edits, dependent updates, and preservation across visual domains and pixel, code, and agent paradigms under one image-only protocol. We introduce Visual Artifact Operation Bench (VAO-Bench), comprising 1,573 manually screened tasks across nine artifact categories and three difficulty levels. VAO-Bench uses executable artifacts and deterministic rendering to trace reference transformations and annotate direct edits, dependent updates, and preservation constraints. All systems receive the same source image and instruction; we evaluate pixel-space editors, code-generating multimodal systems, and tool-using agents on direct-edit accuracy, dependency-aware update, content preservation, domain validity, and visual quality. Experiments show that executable-code systems better support dependent updates, while pixel-space editors offer faster execution and strong visual quality. Explicitly stating dependencies improves both paradigms, identifying implicit-update inference as a central bottleneck. VAO-Bench provides a reproducible foundation for dependable visual artifact editing across generation paradigms.

---


### 367. [CivWorldBench: Evaluating Language World Models in Structured Multi-Agent Sandbox Worlds](https://arxiv.org/abs/2610.16450)

**<font color=#1a73e8>作者：</font>** Ang Li, Haofei Yu, Zhengwei Tao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing use of language models for forecasting motivates a broader evaluation of their world-model capabilities. Such evaluation must go beyond predictive accuracy to assess hidden-state inference and intervention prediction. Real-world forecasting benchmarks offer limited access to hidden-state ground truth and controlled experiments. We introduce CivWorldBench, a benchmark built on a multi-agent strategy game engine with recorded internal states, controlled observations, and paired intervention rollouts. Its 1,900 decision points from 475 worlds support three task levels: association forecasting, belief inference, and intervention prediction. Reference predictors support attributable evaluation of capability gaps, with an expert harness and empirical ceiling estimates contextualizing scores. Stored trajectories make intermediate predictions verifiable, while agent-play experiments test whether world-model capabilities support decision-making. The main panel comprises eleven frontier language models. Composite benchmark scores correlate with real-world forecasting leaderboards on matched model panels, more closely than with a general-capability index, supporting its use as a proxy for real-world forecasting capability. Strong association forecasts do not consistently extend to belief inference or intervention prediction, and effect magnitudes remain poorly calibrated despite informative direction predictions. Process verification reveals errors missed by final-answer evaluation, and structured reasoning improves intervention prediction for the strongest model in the process study. Agent-play experiments identify useful assisted plans and motivate evaluating decision-relevant capabilities beyond association forecasting. These findings identify hidden-state inference, intermediate-state prediction, and effect calibration as priorities for world-model training.

---


### 368. [StructZO: Structured Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning](https://arxiv.org/abs/2610.16451)

**<font color=#1a73e8>作者：</font>** Xuanlin Yang, Jia Li, Zhouchen Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models at scale is increasingly limited by the memory cost of backpropagation. Zeroth-Order (ZO) optimizers reduce this burden by relying only on forward function evaluations, but they still exhibit a substantial performance gap to first-order (FO) optimizers such as Adam. We argue that this gap does not arise solely from the absence of explicit gradients: FO fine-tuning also benefits from informative low-rank optimization geometry, large-scale signal aggregation, and well-conditioned update directions. Motivated by this, we introduce StructZO, a structured Zeroth-Order optimization framework for memory-efficient LLM fine-tuning. StructZO performs large-query ZO estimation within an activation-induced informative subspace and applies spectral control to the resulting reduced-space update before mapping it back to the original parameters. This lets ZO aggregate useful directional signals in a compact, geometry-aware space while avoiding the activation and optimizer-state memory costs of backpropagation. We show theoretically that, when the induced subspace captures concentrated optimization-relevant directions, StructZO reduces the effective ZO estimation dimension from $mn$ to $mr$, with the remaining projection error governed by the spectral tail of the activation Gram matrix. Empirically, across OPT-series and Llama3.1-8B on diverse downstreamtasks, StructZO improves over the strongest existing ZO baselines by up to $8.7%$ relative on average and up to $26.9%$ relative on individual tasks, while remaining within $1.5%$ of FO-Adam on average. These results suggest that structured and spectrally controlled ZO updates can substantially narrow the gap between ZO and FO optimization.

---


### 369. [Differential Privacy Protected Preference Alignment on Survey Derived Data](https://arxiv.org/abs/2610.16458)

**<font color=#1a73e8>作者：</font>** Xiuyuan Qi, Yi Wang, Wenjie Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Preference alignment enables language models to better reflect human values, but the preference data contains sensitive information, especially when derived from surveys about political beliefs, social norms, religion, gender attitudes, and cultural values. This paper studies privacy-preserving alignment on questionnaire-derived data from the World Values Survey, where supervision takes the form of ordinal labels rather than standard pairwise rankings. Existing efforts mainly focus on general privacy protections upon model training, while data-specific methods for survey data remain unexplored. We first show the vulnerability of aligned models, then formulate the task as rating prediction and introduce label differential privacy. Building on this formulation, we construct a differential private pipeline utilizing three privacy mechanisms: randomized response, exponential mechanism, and DP-SGD. Experiments show that simple label-level mechanisms outperform gradient-level methods, and proper aggregation function for preprocessing also make large contribution. The new fine-grained private comparison motivates explorations toward language model alignment with formal privacy guarantees.

---


### 370. [The interpreter as developer: An autoethnographic design study of building a computer-assisted interpreting tool through human-LLM co-creation](https://arxiv.org/abs/2610.16460)

**<font color=#1a73e8>作者：</font>** Zeming Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time AI captioning now serves audiences at multilingual events, yet computer-assisted interpreting (CAI) tools are still built for interpreters, rarely by them. This article reports an autoethnographic design study in which a professional interpreter with no programming training built a local-first CAI system through expert-led 'vibe coding', co-creating with an LLM architect and a coding agent. Analysis of the complete development dialogues shows how tacit professional knowledge, from segmentation to booth infrastructure, was externalized into design after generic defaults failed in use. In a demanding public scientific event, three mechanisms of in-booth appropriation emerge under a firmly human-led division of labor; telemetry from a first fully instrumented assignment shows a fully local chain sustaining a median translation latency of 0.94 s across 971 utterances. The case is read as lead-user innovation newly enabled by generative AI, with implications for the technological literacy of interpreters and the future of interpreter training.

---


### 371. [Teaching Vision-Language Models to Decline: Support Completion Against Mirage](https://arxiv.org/abs/2610.16465)

**<font color=#1a73e8>作者：</font>** Alfaj Uddin Ahmed, Md. Shaown Miah, Md Arid Hasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models answer questions about images they were never shown, a failure called mirage. Such an answer can be correct without being justified by the evidence, and the difference matters wherever a model's output is checked by someone who did not see its input. We locate the failure in the training objective: cross-entropy separates a model that reads the image from one that ignores it by only the conditional mutual information between answer and image, and no training example rewards declining. We formalise support completion, TIDE, which also shows each training question with a blank image, a same-domain wrong image and an out-of-domain image, with targets that decline, and prove that under TIDE every image-blind predictor is suboptimal by at least 1.04 nats per example, that the optimum declines exactly on the counterfactual kinds while keeping its behaviour on valid images, and that for any finite model the error of its answer-or-decline decision, declining on valid input plus answering on invalid input, is bounded below by how well its representation separates valid from invalid evidence. On Qwen2.5-VL-7B under a frozen held-out protocol with two judges, the three-condition predecessor of TIDE reduced the invalid-evidence mirage rate from 0.759 to 0.097 and the blank-image rate from 0.700 to 0.003 at a false-abstention cost of 0.126; label-free grounding raised the rate to 0.859, a likelihood-advantage contrast moved it only to 0.718 because its empty-image term carries no gradient, and grounding applied after support completion re-opened the mirage. The four-condition protocol on three base models, with seeds and component ablations, is in progress and not reported here.

---


### 372. [PATMT2: Two-stage domain adaptation for multilingual patent translation](https://arxiv.org/abs/2610.16466)

**<font color=#1a73e8>作者：</font>** Xiaowei Su, Xusen Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present PatMT2 (Patent Machine Translation, v2), a two-stage LoRA pipeline that adapts the Hy-MT2-7B dedicated translation model to four-language (Chinese/English/Japanese/Korean) patent translation. On six translation directions, the Stage-2 checkpoint reaches a macro-average BLEU of 43.39 (BF16) to 43.57 (AWQ INT4), improving over the Hy-MT2-7B base by up to +8.8 BLEU and also exceeding Qwen3-32B and several external systems on the same average. We then measure the cost of adaptation: probing 38 languages absent from the fine-tuning data, the model still produces correct, fluent output on 34, while four low-resource languages collapse into distinct, reproducible failure modes. We treat these as diagnostic cases rather than retention rates, and report their mechanisms without attributing them to a single cause. Paired bootstrap tests confirm the translation gains over all baselines (p < 0.001).

---


### 373. [CircuitBreak: Pruning a Sparse Safety Circuit of Neurons](https://arxiv.org/abs/2610.16470)

**<font color=#1a73e8>作者：</font>** Jincheng Ying, Li Wenlin, Wencheng Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> White-box neuron pruning has shown that refusal in large language models (LLMs) can depend on a small, removable set of feed-forward (FFN) channels. Existing attacks either need carefully paired ``twin'' prompts or score each neuron in isolation. Pruning also has an unavoidable capability cost, so over-removal compounds the loss. TwinBreak removes $1\%$--$5\%$ of parameters and NeuroStrike removes $0.3\%$--$0.7\%$ of neurons in targeted layers. We model safety as a small \emph{circuit} whose neurons contribute jointly rather than independently. We propose \textsc{CircuitBreak}, a neuron-pruning attack that greedily searches for a sparse set of FFN neurons whose joint ablation flips a refusal readout. \textsc{CircuitBreak} re-scores every candidate after the neurons already removed and needs no twin prompts. On ten instruction-tuned models, the greedy search converges after removing $29$--$150$ neurons ($0.0066\%$--$0.0388\%$ of the MLP). The pruned models raise the attack success rate from $2.24\%$/$7.35\%$ to $87.54\%$/$87.54\%$ on Llama-3.2-3B-Instruct/Llama-3.1-8B-Instruct and from $8.95\%$/$5.43\%$ to $88.50\%$/$88.18\%$ on Qwen2.5-7B-Instruct/Qwen2.5-14B-Instruct, as judged by Llama Guard 3 8B on StrongREJECT.

---


### 374. [MiMaAlign: Hierarchical Micro-Macro Alignment for Physically Plausible Video Generation](https://arxiv.org/abs/2610.16482)

**<font color=#1a73e8>作者：</font>** Yansong Liu, Litong Gong, Weijie Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) diffusion models have made remarkable progress in generating high-fidelity visuals, yet their outputs still often exhibit physically implausible phenomena, including discontinuous dynamics and implausible event interactions. Existing representation alignment methods mainly transfer generic video features or short-range motion cues, treating physical plausibility as a single-level representation problem. To address this issue, we propose MiMaAlign, a hierarchical micro-macro alignment framework that transfers complementary dynamics-oriented and event-oriented knowledge into different abstraction depths of a pretrained video diffusion model. Specifically, micro-level continuous dynamics alignment imposes constraints by aligning diffusion features with a continuous-time motion representation learned by a Neural Ordinary Differential Equation (Neural ODE), while macro-level event-commonsense alignment provides representations of object interactions and event semantics through an instruction-prompted vision-language model (VLM). With training-only auxiliary objectives, we align the complementary supervision from the two teachers with shallower and deeper generator features, respectively, enabling the generator to internalize the corresponding physical priors. Empirical evaluations show that, on CogVideoX-2B, MiMaAlign achieves a relative improvement of up to 21.0% in the Physical Commonsense (PC) score on the VideoPhy benchmark over the baseline, and also delivers substantial gains on the highly challenging VideoPhy2 benchmark, while maintaining general video quality on VBench and being supported by blind user comparisons.

---


### 375. [Growing and Transferring Pathways for LLM Reinforcement Learning](https://arxiv.org/abs/2610.16489)

**<font color=#1a73e8>作者：</font>** Haolin Tian, Yikang Li, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) can substantially improve the reasoning capabilities of large language models, but an effective training run requires considerable resources. Reusing the computation acquired through RL across models would extend the value of that training. We propose GrowRL, an RL method that organizes learned updates into compact computational pathways through structural growth. GrowRL freezes the pretrained backbone and adds an independent causal attention branch and a feed-forward network branch at each Transformer layer. Zero-initialized output projections preserve the pretrained policy at initialization, and RL updates only the added pathways. The learned pathways remain explicit after training, allowing transfer to structurally compatible target models and subsequent adaptation with the target backbone frozen. The architecture also supports sequential transfer of additional pathways. By keeping the learned attention and feed-forward computation separate from the pretrained weights, GrowRL provides an explicit structure for preserving and reusing the outcome of an RL run. Experiments across five backbones show competitive mathematical reasoning and out-of-distribution performance with a small number of trainable parameters. Learned pathways provide immediate gains across all three transfer directions, with performance after only 10 target-side updates already close to that after 100 updates in every case. These results support computational pathways as parameter-efficient and reusable units of reinforcement learning adaptation.

---


### 376. [Communication, Vocalisation, and Language](https://arxiv.org/abs/2610.16490)

**<font color=#1a73e8>作者：</font>** Peter Wallis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The contention is that the current batch of Large Language Models don't *understand* language, but they *do* it. Rather than LLMs forming some kind of ``distributed representation'' of symbols, the claim is that LLMs are capturing ``Cultural Intelligence'' and grounding symbols in what the sociologists call practices.

---


### 377. [KARAMEL: Knowledge-Aware Ranking for Multimodal Entity Linking in the Arts via Heterogeneous Graphs](https://arxiv.org/abs/2610.16502)

**<font color=#1a73e8>作者：</font>** Raffaele Scaringi, Alejandro Sierra-Múnera, Gennaro Vessio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discovering and disambiguating entities from multimodal and heterogeneous data is a key challenge in discovery science, where relevant knowledge is often implicit and distributed across modalities. We present KARAMEL, a framework for multimodal entity linking (MEL) - the task of aligning visual and textual mentions to entities in a knowledge base - in the cultural heritage domain. Unlike prior vision-language models that primarily rely on surface-level multimodal alignment, our approach incorporates sociohistorical and contextual knowledge through a knowledge-aware architecture that fuses a vision-language encoder with a heterogeneous graph neural network. This design enables contextual reasoning over complex relational structures and supports robust entity disambiguation under ambiguous or underspecified evidence. To benchmark multimodal discovery in this setting, we introduce WikiMuSA (Wikidata-based Multimodal Semantic data for Art), a new dataset that links artworks to Wikidata entities via images, textual descriptions, and structured contextual knowledge. Experimental results show that KARAMEL surpasses strong baselines, particularly on implicit or abstract mentions, while ablation studies highlight the critical role of domain-specific, structured context in learning expressive representations. While instantiated in the cultural heritage domain, KARAMEL addresses a general knowledge discovery problem and applies to other scientific settings involving multimodal observations and heterogeneous background knowledge. Both the dataset and source code are made publicly available.

---


### 378. [Intent-Triggered Anchoring for Multi-Token Format Units in Parallel Decoding of Diffusion Language Models](https://arxiv.org/abs/2610.16516)

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Kyu Sung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In parallel decoding, diffusion language models commit several tokens per forward pass, so co-committed tokens cannot see each other, breaking multi-token format units that parsers need. On ECHO, an open-weight one-step chest X-ray (CXR) report generator, 32.7-36.7% of evaluation reports lack a parseable Impression heading and score as empty. We propose intent-triggered anchoring, a training-free decoding rule that completes a format unit once the model commits its first token, inserting only units with a unique, content-free completion; fallbacks write the unit when the model stops or loops without starting it. On three CXR evaluation sets, the rule raises readable rates from 63.3-67.3% to 100.0% with no regressions and a 95th-percentile latency ratio of 0.68-1.28 against official decoding. Broken headings state findings absent from the reference; adding the heading at the end leaves them in 15.5-31.0% of reports, our rule in at most 0.6%. For math answer markers, the rule raises accuracy in the most parallel setting of five diffusion language models by 5.8-20.8 points on GSM8K and 5.1-17.1 on GSM-Symbolic, held out from tuning. With lenient answer extraction, gains are 3.3-12.5 and 2.7-6.3 points; the rule adds 1.4-8.6 points over a stop-only fallback for four of the five models.

---


### 379. [EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents](https://arxiv.org/abs/2610.16523)

**<font color=#1a73e8>作者：</font>** Min Cai, Dan Zhang, Gao Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training LLM agents to interact with users over multiple turns is challenging because the learning signal depends not only on the agent, but also on the user simulator and environment, which jointly shape the agent's experience. Simulated users can be stochastic or inconsistent, while environments may contain unreliable tools, incomplete state coverage, and incorrect verifiers. Prior work mainly addresses the resulting instability through reward shaping or denser supervision, while treating these components as fixed. We instead introduce EAU, a meta-agent framework for environment--agent--user co-evolution. During training, EAU monitors trajectories, tool traces, rewards, and training statistics; diagnoses failures and uninformative interactions; and proposes targeted modifications to the user simulator, environment, reward design, and RL configuration. Validated changes are hot-swapped into the ongoing run, allowing the training setup to evolve together with the policy. These adaptations also persist across runs, so later training can build on previously discovered improvements rather than restarting from a fixed setup. We enable this process through an editable symbolic representation of user and environment dynamics, while the agent remains a neural LLM optimized with RL. Across three interactive-agent benchmarks and two backbone models, EAU consistently outperforms prior RL methods, improving the overall score over the strongest baseline by 14.7--15.0% and increasing successful task completion on ColBench by up to 36.7%, showing that co-evolving the training system with the policy can substantially improve multi-turn RL.

---


### 380. [Support or Magnitude? Characterizing Neuron Relevance for Instruction Data Selection](https://arxiv.org/abs/2610.16531)

**<font color=#1a73e8>作者：</font>** Yifan Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model-internal signals, such as neuron activations and gradients, have been used for instruction data selection, yet how neuron relevance should be characterized remains underexplored. In particular, should selection prioritize the magnitude of relevance or how broadly it is distributed across neurons? To investigate this question, we construct sample-level relevance profiles using AttnLRP-guided attribution and introduce two complementary criteria: Effective Relevance Support (ERS), which measures the effective support of positive relevance, and Positive Relevance Magnitude (PRM), which captures its average strength. Our analyses reveal that these characterizations produce distinct sample rankings and selection preferences despite sharing the same underlying relevance profiles. On Qwen2 models, PRM exhibits stronger associations with activation-based selection, whereas ERS produces substantially different rankings. These differences extend to task composition, within-task sample preferences, and semantic selection patterns, with varying degrees of agreement across backbones. Experiments across three language models and five downstream benchmarks demonstrate the practical value of relevance-guided selection, with ERS achieving the best overall average performance rank among the evaluated methods. Our findings highlight that how neuron relevance is distributed and characterized, rather than its magnitude alone, matters for instruction data selection.

---


### 381. [Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.16533)

**<font color=#1a73e8>作者：</font>** Zhipeng Chen, Wayne Xin Zhao, Ji-Rong Wen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is reshaping how large language models (LLMs) acquire reasoning capabilities, yet the optimizers used remain largely inherited from teacher-forcing training. This raises a fundamental question: does RLVR induce a distinct optimization geometry that calls for a different optimizer? We investigate this question through the spectral structure of LLM gradients and find that gradient energy progressively concentrates into a shrinking effective subspace, which is characteristic of RLVR, as it is absent under supervised fine-tuning (SFT) and is largely removed when the verifiable reward is replaced by a random one. Moreover, the rank required to capture a fixed fraction of gradient energy steadily decreases over training, revealing that the effective dimensionality of useful updates itself evolves with training. These findings motivate a new optimization principle: rather than prescribing the update rank externally, an optimizer should adapt its rank to the evolving spectral structure of the gradient. We introduce Ares (Adaptive Rank-Effective Spectral Optimization), which estimates the effective update rank from the gradient's spectral energy distribution, tracks its evolution, and confines the gradient signal driving each update to the resulting low-rank subspace. Across LLMs of different scales, Ares improves accuracy over widely used optimizers and generalizes across RLVR algorithms and tasks. Results suggest that effective optimization may require optimizers to be designed around the geometry and dynamics of the training process. We release the code and data at this https URL.

---


### 382. [CT0: Cybersecurity Transformer](https://arxiv.org/abs/2610.16550)

**<font color=#1a73e8>作者：</font>** Víctor Mayoral-Vilches  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> General-purpose frontier models are large, expensive to run, and increasingly reluctant to engage with authorised defensive- and offensive-security work. We ask the opposite question: how small can a cybersecurity-specialist transformer be while remaining genuinely useful to a security practitioner? We introduce CT0, a Cybersecurity Transformer architecture, and CT0-Micro, its first incarnation: a compact (~4B-parameter) model built on the open base model, whose backbone is specialised by two-phase on-policy distillation on our Cybersecurity AI (CAI) dataset. CT0 serves two modes from one set of weights: System 1 answers typed security decisions (is this file suspicious, is this request an attack, did the model just refuse) in a single forward pass without generating a token, System 2 is the usual tool-using agent, and a confidence gate spends generation only where the fast path is unsure. Specialisation lifts the agentic path: CT0-Micro solves 21.1% of cybench-subtask against 7.6% for its base, above every open model of comparable footprint and the densest cybersecurity capability per parameter we measured. The fast path is what the architecture buys: CT0-Micro screens eighty files per second for indicators of compromise, catches its own refusals at 96.5% accuracy in 47 ms where the model judging itself reaches 76.5% in 254 ms and misses half of them, flags jailbreak requests at AUROC 0.966 in 8 ms, and, generating only for the facts it is unsure about, extracts vulnerability facts more accurately than either mode alone at a fifth of the generative cost. All of it is built in about 314 RTX PRO 6000 GPU-hours and served from one workstation GPU, with no policy layer between operator and target. Across eighteen benchmarks and use cases run with one checkpoint and head, we report where the design helps, where it does not, and what it still lacks.

---


### 383. [VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2610.16567)

**<font color=#1a73e8>作者：</font>** Jun Xiao, Rui Ye, Dong Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level diagnosis and combinatorial perturbation coverage, often without connecting diagnosis to targeted model refinement. We introduce VLA-GAUGE, a diagnostic framework that unifies both evaluations under a shared executable task representation. It combines (1) paired in-distribution and out-of-distribution tasks across six capability suites, (2) single-factor sensitivity analysis with combinatorial perturbation screening and evaluation, and (3) diagnosis-driven refinement through targeted data augmentation and model fine-tuning. We evaluate 12 VLAs spanning different model sizes and action-modeling paradigms under a unified protocol. We find that (1) The mean Zero-Shot Score on VLA-GAUGE is only 22.3%, with SimpleVLA-RL scoring 8.0% and ranking second to last among the evaluated models. (2) Under three representative combinatorial perturbation configurations, the mean R-Score is 9.3. (3) Diagnosis-driven fine-tuning improves $\pi_{0.5}$'s zero-shot generalization and robustness under a selected perturbation combination on held-out scenarios by 72.4 and 31.8 scoring points, respectively; the latter exceeds the 10.9-point gain from LIBERO-Plus single-factor fine-tuning despite fewer successful training trajectories. These results show that high reported success rates on familiar manipulation tasks do not guarantee strong zero-shot generalization to unseen tasks or robustness to combinatorial perturbations, while diagnostic evaluation provides actionable signals for targeted model improvement.

---


### 384. [CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction](https://arxiv.org/abs/2610.16577)

**<font color=#1a73e8>作者：</font>** Jialei Wang, Zehan Wang, XiaoYang Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing reference videos as editable dynamic 3D scenes is an important path toward controllable video generation for filmmaking: these scenes provide modifiable, renderable visual proxies that enable explicit control over scene layout, subject actions, and camera behavior. To evaluate agents' ability to reconstruct editable dynamic 3D scenes from dynamic reference videos, we introduce CineRecon, a benchmark comprising 50 reference videos and 360 annotated evaluation clips. The reference videos span film, real-world footage, and games. Given a complete video, an agent uses tools to construct, animate, render, and refine its reconstruction. We evaluate this task under three representation settings: Proxy, Simplified, and Detailed. These settings increase geometric and appearance requirements while retaining the same requirements for spatial relations, camera behavior, and subject dynamics. This design tests whether agents can reproduce the events in a video when detailed appearance is unnecessary, and how performance changes as representation requirements increase. For evaluation, we construct checklists that associate observable properties and events with specific entities and times. A vision-language judge compares timestamp-aligned reference and rendered frames across 11 categories, grouped into camera, static, and dynamic consistency dimensions. We evaluate 12 models using their corresponding agent harnesses and find failures across all three dimensions. Subject motions and interactions remain difficult to reproduce even under the Proxy setting.

---


### 385. [Code-Interactive Visual Reasoning for Financial Candlestick Understanding](https://arxiv.org/abs/2610.16587)

**<font color=#1a73e8>作者：</font>** Chenxi Zhang, Youwei Pang, Xiaoqi Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Financial candlestick understanding requires locating visual elements, aligning them across trading dates and panels, and combining observations through numerical and financial reasoning. Answer accuracy alone does not reveal whether predictions are supported by chart evidence. We introduce Code-Interactive Financial Candlestick Reasoning and present Fin-Thinker, a model based on Qwen3.5-9B that generates and executes code to acquire evidence and perform computations. The model uses the returned observations to guide subsequent reasoning. To train these capabilities, we construct FinKLine-32K with 32,184 replay-verified code-observation trajectories collected through teacher-guided student exploration. These include successful solutions with and without error recovery. Our three-stage training framework combines foundational visual-code fine-tuning, financial process supervision of successful reasoning and corrective continuations, and execution-feedback reinforcement learning. For evaluation, we introduce FinKLineBench with 1,200 questions across 138 financial task types to assess answer correctness, code execution, and evidence grounding separately. On FinKLineBench, Fin-Thinker improves strict accuracy by 13.1 and 33.2 percentage points over the best-performing direct-answer baseline among those evaluated and its base model with sandbox access, respectively. Training-stage ablations further show that financial process supervision and execution-feedback reinforcement learning yield successive improvements in both answer accuracy and GPT-5.6-judged grounded accuracy.

---


### 386. [Double-Rollout Reinforcement Learning with Sampling-based Reward Estimation](https://arxiv.org/abs/2610.16593)

**<font color=#1a73e8>作者：</font>** Haifeng Qian, David Mosallanezhad, Christian Munley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) implemented with Group Relative Policy Optimization (GRPO) has driven substantial progress in training reasoning language models. However, verifiable outcome rewards provide an imperfect measure of reasoning quality: a correct final answer may not be supported by the reasoning trace, whereas an incorrect rollout may contain a nearly correct reasoning trajectory. We present empirical evidence for this mismatch and hypothesize that the resulting reward noise contributes to instability in reinforcement learning for both reasoning accuracy and token efficiency. To address this credit assignment challenge, this paper proposes double-rollout reinforcement learning. For each sampled rollout, we truncate its reasoning trace, sample multiple continuations from the truncated prefix, and replace the original reward with the mean continuation reward, yielding a more robust estimate of reasoning quality. This double-rollout algorithm incurs only a moderate increase in compute cost and yet reaches substantially higher accuracies across math and coding tasks and across Qwen and Nemotron models than baseline algorithms with fewer RL steps. For example, using only DAPO data it trains Nemotron-3-Nano-30B-A3B to reach 95.4% on AIME 2026, versus 91.5% by GRPO and substantially above state of the art for this model size, within 30 RL steps. When combined with length-based rewards, the same algorithm further improves the accuracy-efficiency Pareto frontier over existing efficiency optimizations. These findings suggest that the double-rollout reward estimation is an effective and cost-efficient way to improve both the accuracy and token efficiency of reasoning RL.

---


### 387. [Detecting Chain-of-Thought Hijacking in Backdoored Multimodal Large Reasoning Models](https://arxiv.org/abs/2610.16598)

**<font color=#1a73e8>作者：</font>** Zhifang Zhang, Qi Wei, Weitong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning enables multimodal large reasoning models (MLRMs) to solve complex visual problems, but also exposes them to CoT hijacking: an adversary implants a backdoor through poisoned fine-tuning so that a visual trigger induces a hijacking turn, redirecting an otherwise faithful reasoning chain to an attacker-chosen answer. However, since the hijack acts within the reasoning chain, existing multimodal backdoor defenses designed for MLLMs that answer directly struggle to detect it. Moreover, inspecting the chain itself does not reliably expose the hijack, since the hijacking turn can resemble honest self-correction in form. In this paper, we find that honest reasoning tends to revise its answer at high-entropy "aha moments", whereas a hijack can overturn a confident answer through a near-deterministic turn. To quantify this contrast, we formalize this phenomenon as belief inertia, the cumulative next-token entropy of a reasoning span minus the answer-belief revision it induces, with markedly lower values for hijacked spans than for honest reasoning spans. Since hijacking tokens are also image-dependent, we further improve detection by restricting the measure to image-dependent spans, yielding visual belief inertia (VBI). Building on this, we propose InertiaGuard, a training-free, test-time detector that flags a trace when its VBI falls below a threshold calibrated on a small set of clean traces. Across various attacks and benchmarks, InertiaGuard achieves higher detection performance than existing baselines, while generalizing to different model architectures and trigger types.

---


### 388. [When 1+1 Backfires: Rethinking Relevance-Diversity Balancing for Sample-Aware Visual Token Reduction](https://arxiv.org/abs/2610.16615)

**<font color=#1a73e8>作者：</font>** Yihang Huang, Peisong Wen, Chenhao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual token compression has emerged as a critical technique for reducing the inference cost of Vision-Language Models. Existing methods select tokens based on text relevance, visual diversity, or a fixed combination of both---treating the relevance-diversity balance as a universal constant independent of the input. We conduct a systematic analysis to challenge this assumption. At the dataset level, grid-searching the optimal relevance-diversity weight per benchmark reveals substantial cross-task variation. More critically, we further maximize per-sample answer likelihood to recover sample-level oracle weights, finding that their distributions not only differ markedly across benchmarks but also exhibit high within-benchmark variance. Based on these observations, we propose SAVER, a framework for Sample-Aware relevance-diversity balanced Visual tokEn Reduction. We first derive a Geometric Intent Prior (GIP) from the spatial concentration of text-relevant tokens to infer a sample-specific relevance-diversity weight, and then apply this weight to jointly select tokens via a Weighted Text Centroid (WTC) for relevance scoring and a Visual Marginal Coverage Gain (VMCG) for diversity. SAVER requires no additional training and achieves sample-aware balancing entirely at inference time. Extensive experiments demonstrate that SAVER consistently outperforms state-of-the-art baselines across diverse benchmarks, retaining 96.5% of full-model performance on LLaVA-1.5-7B with only 11.1% of the original visual tokens, and further generalizing to LLaVA-NeXT and Mini-Gemini.

---


### 389. [Answer It or Not? Towards Prompt-Adapted Adversarial Images on Vision Language Models](https://arxiv.org/abs/2610.16622)

**<font color=#1a73e8>作者：</font>** Shunyuan Bai, Yuchen Ren, Le Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the advancement in language modeling, research on adversarial images has recently shifted from image classifiers to vision-language models (VLMs). Despite the new, text-prompt-driven nature of VLMs, we find that existing VLM adversaries have largely overlooked the dynamics of text prompts. In a typical use case, adversarial images can protect visual privacy by rejecting VLMs from answering questions about the image. However, existing protections are prompt-agnostic, i.e., indiscriminately rejecting any question, including those for potential legitimate use of the image. To address this limitation, we propose Prompt-Adapted (ProAda) adversarial images, which are optimized to balance the rejection of harmful prompts and the correct response of legitimate prompts. In particular, to achieve a more accurate adversarial direction, the text prompt is also iteratively updated with a simple classifier judging whether the harmfulness of the prompt remains. Extensive experiments on visual-privacy-related datasets validate that ProAda can reject over 90% of harmful prompts while allowing over 90% of legitimate ones, demonstrating superior overall performance compared to existing prompt-agnostic VLM adversaries. In addition, our ProAda achieves competitive overall cross-model transferability and improved robustness against countermeasures.

---


### 390. [LATCH: LLM-Assisted Timing Closure Harness for Post-Route FPGA Optimisation](https://arxiv.org/abs/2610.16625)

**<font color=#1a73e8>作者：</font>** Shu Gu, Matthew Youngman, Yuqin Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-route FPGA timing closure remains expert-dependent and computationally expensive. We present LATCH (LLM-Assisted Timing Closure Harness), a two-layer framework that separates large language model (LLM) orchestration from deterministic FPGA implementation and evaluation. Across sixteen designs and seven LLMs, a single-iteration study compares three agent control granularities - expert-written recipes, direct EDA operations and LLM-constructed procedures - to ask how much control an agent needs per attempt. Functional-pass rates are 98.2%, 71.4% and 17.9%, respectively; yet direct operations give slightly larger 3.4% median Fmax gains when passing, versus 3.2% for recipes. This exposes a trade-off between execution reliability and timing improvement. Informed by this trade-off, a multi-iteration study fixes the action tier at expert recipes to ask how repeated attempts are best organised, comparing a fitted deterministic heuristic with sequential LLM reasoning, branching exploration and knowledge base-guided exploration within 12 checkpoints per run. Branching raises mean maximum-frequency improvement from 10.5% (sequential) to 16.0%, and the knowledge base to 20.3%, improving 15 of 16 designs. Characterisation across 2,421 recipe attempts profiled their gain and validation rates, showing hard-block re-placement gives the largest cumulative mean gain at 41.4MHz.

---


### 391. [SuPER-Mamba: Surprisal Prioritization for Extended-Context Routing in Mamba](https://arxiv.org/abs/2610.16636)

**<font color=#1a73e8>作者：</font>** Zhetong Zhang, Gayan K Kulatilleke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State space models provide efficient linear-complexity processing for long sequences, but their performance frequently degrades as context length grows. We propose SuPER-Mamba, a training-free framework that uses Surprisal as a model-intrinsic signal for long-range state routing in pretrained Mamba models. SuPER-Mamba computes position-wise Surprisal from next-token predictions, aggregates neighboring responses through Local Pooling, and uses the resulting scores to prioritize Global-Channel updates without query-dependent scoring or additional training. We evaluate SuPER-Mamba on three state-space models across the LongBench-E benchmark. The results show that SuPER-Mamba improves the average score from 8.06 to 15.69, corresponding to a 94.7% relative gain over the Base Models and a 13.1% improvement over the state-of-the-art prior baseline. Ablation and length-wise analyses further support the effectiveness of the proposed routing framework.

---


### 392. [SIREN: Situation-aware Index for Response and Emergency ActioNability in Crisis Translation](https://arxiv.org/abs/2610.16646)

**<font color=#1a73e8>作者：</font>** Maria Carmen Staiano, Lifeng Han, Johanna Monti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation (MT) is increasingly utilized in multilingual crisis communication, yet conventional evaluation does not directly assess whether translated emergency messages preserve their actionability. We introduce SIREN (Situation-aware Index for Response and Emergency ActioNability), a human evaluation framework assessing whether translation choices compromise protective action, directive force, and urgency of the source text. We evaluate SIREN in two complementary settings. At the error level, we apply it to HOPE-annotated Italian--English translations produced by ChatGPT-4o and Google Translate: 31.63\% and 48.73\% of errors, respectively, compromise actionability, predominantly by affecting the protective action. At the message level, we evaluate English--French translations produced by TranslateGemma-4B and Google Translate, with actionability preserved in 85.34\% and 92.67\% of translations, respectively. TranslateGemma-4B failures predominantly weaken directive force, whereas Google Translate failures more often compromise protective actions and receive Major impact ratings. These findings show that translation systems can differ not only in how often actionability is lost, but also in the nature and functional impact of these failures. Alongside SIREN, we contribute an English--French crisis-translation resource with human actionability annotations and post-edited reference translations, supporting further research on function-oriented evaluation for crisis communication. Our experimental data is available at this https URL.

---


### 393. [Structural Baselines Matter for Agent Failure Detection and Attribution](https://arxiv.org/abs/2610.16661)

**<font color=#1a73e8>作者：</font>** Ramesh Arvind Naagarajan, Stefan Streif  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM agent using tools can fail silently. It stops before the task is done, raises no error, and answers fluently. Two kinds of monitor address this, one deciding whether a run failed and the other naming the step where failure became unavoidable. Much of the reported performance on both tasks comes from regularities that need no model. Failing runs are longer, and the step labelled decisive is usually the last. A rule that always names the last step is correct $67\%$ to $96\%$ of the time here, without reading the run at all. That ceiling reflects how the labels were written, not how agents break. On failures whose decisive step replay can confirm, it falls to near chance. Reporting gain over that rule therefore changes what a score means. Under that correction, methods tested here gain nothing on give-up failures, while several published systems keep a clear advantage on other splits. For detection, the agent's internal states beat transcript length and text similarity on the agent benchmark, and hold up where the text baseline does not. Precision stays low when failures are rare, so such a monitor should rank runs for review, not replace it.

---


### 394. [Revisiting Natural Language Prompts from Large Language Models for Open-Vocabulary Video Recognition](https://arxiv.org/abs/2610.16666)

**<font color=#1a73e8>作者：</font>** Haichen He, Weibin Liu, Weiwei Xing  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) like CLIP have shown great success in image tasks, however, applying CLIP to open-vocabulary video recognition poses challenges. Due to the limited text information, directly fine-tuning CLIP on video recognition datasets may lead to overfitting and hinder its generalizability. A prevalent method is to enrich text information by generating prompts using Large Language Models (LLMs). However, limited efforts have been made to explore how to generate higher-quality prompts that can contribute to classify unseen categories, and how to further enhance vision-text alignment based on these prompts. In this paper, we propose P2CLIP (Prompt-guided CLIP), which aims to bridge this gap by exploring the impact of prompts across three aspects: category, video, and frame. At the category level, we argue that LLM-generated prompts under simple instructions may suffer from semantic overgeneralization, which can blur the category boundaries and hinder the performance of the model. To address this issue, we design Generic-Discriminative Prompt using LLMs to obtain discriminative category embeddings with rich semantic information. At the video and frame levels, we first use VLM and LLM to generate frame and video descriptions for enhancing vision-text alignment. Then we propose a Knowledge-Guided Temporal Aggregation mechanism, which leverages the expert knowledge derived from LLMs to guide the temporal modeling of videos and encourage a better construction of the joint visual-textual feature space. Extensive experiments across various benchmarks, including zero-shot and few-shot settings, demonstrate the effectiveness of our method.

---


### 395. [EvoSpatial: Experience-Driven Skill and Tool Evolution for Spatial Reasoning Agents](https://arxiv.org/abs/2610.16679)

**<font color=#1a73e8>作者：</font>** Bin Yu, Shijie Lian, Zhaolong Shen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-augmented vision-language agents compose perception and measurement to reason about spatial relationships, but effective execution also requires tracking geometric assumptions and checking intermediate evidence. Preserving this experience across tasks requires retaining procedural knowledge together with the computations it governs. We introduce EvoSpatial, an experience-driven framework that evolves a library of linked skills and tools. Our key insight is that successful and failed spatial trajectories reveal both how to compute and when to trust the result. EvoSpatial retrieves skills, reuses tools, and synthesizes reusable computational functions (generated helpers) during reasoning. After answer submission, supervised outcome feedback guides skill refinement and tool consolidation for subsequent tasks. Across 20 benchmarks, EvoSpatial attains the highest average score among the compared spatial agents, exceeding SpatialClaw by 4.0 percentage points. Further experiments show cross-benchmark transfer and improved reasoning through skill-guided distillation without external skills at evaluation. These results support accumulating spatial experience for both inference-time reuse and trajectory-based training.

---


### 396. [EHR-Bench: A Chinese Multi-Task Benchmark for Recruitment AI](https://arxiv.org/abs/2610.16689)

**<font color=#1a73e8>作者：</font>** Ruijia Yang, Bing Xu, Zulong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recruitment applications span diverse operations, from drafting job descriptions and interpreting queries to organizing profiles, assessing fit, and recommending candidates and jobs. Systematic LLM evaluation therefore requires task coverage that reflects this range of business needs. We introduce EHR-Bench, an open Chinese benchmark comprising twelve tasks across six capability families and five recruitment scenarios. The tasks cover generation, extraction, classification, retrieval, semantic similarity, and reciprocal ranking within one evaluation framework. An internal recruitment dataset guides task definitions, the occupation taxonomy and sampling targets, output requirements, and scoring protocols. Following these specifications, we construct 8,336 task instances from public materials and controlled augmentation, with source-aware expert review and documented provenance. We evaluate twelve LLMs through task-level, capability-level, and aggregate comparisons. Closely ranked models exhibit distinct task strengths, and performance varies across input sources, reference evidence, and candidate pools. Five shared models retain the same observed Overall ordering on a private operational reference, with variation in capability and task correspondence. EHR-Bench provides a reproducible foundation for systematic model assessment, task-specific model selection, and further research on LLMs for recruitment. The project repository is available at this https URL.

---


### 397. [Attention-Graph Curvature for the Verification of Mathematical Reasoning](https://arxiv.org/abs/2610.16709)

**<font color=#1a73e8>作者：</font>** Kanghyeon Kim, Johannes F. Lutzeyer, Yanzhu Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models have recently solved open Erdős problems and achieved gold-medal level performance on International Mathematical Olympiad problems. But their solutions, written in natural language, cannot yet be verified by proof assistants. An erroneous reasoning step can invalidate every step that comes after, so it is advantageous to detect errors early. Several methods have been proposed to detect erroneous reasoning quickly based on the features of the forward pass of the language model that performs reasoning. In this work, we study whether the directed Forman curvature of that model's attention graph, a local quantity computed at an edge from the attention weights around it, carries information about a step's correctness. To do so, we evaluate four per-step verifiers on ProcessBench with and without the curvature appended to their input. Appending curvature values improves the overall mean performance of all four verifiers. ReProbe, the verifier that takes every token of a step as input, shows the largest improvement. Adding the curvature increases the time of the language model's forward pass by 18% on average.

---


### 398. [Audit Before You Distill: A Controlled Workflow for Reasoning Transfer into Compact Medical Language Models](https://arxiv.org/abs/2610.16713)

**<font color=#1a73e8>作者：</font>** Tiago Martinelli, João Paulo Papa, Adriano José Pereira  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Teacher rationales can help a smaller model answer health professions questions, but they can also reinforce errors. We examined when they help and how this evidence can guide training using Brazilian Portuguese questions from medical and multiprofessional residency examinations. First, we measured how a teacher rationale changed the student's probability of selecting the correct answer and compared this effect with rationales drawn from other questions. The complete rationale increased this probability by 21~p.p. when the teacher was correct and decreased it by 14~p.p. when the teacher was wrong. By intervening on the reasoning content, we showed that shuffled rationales did not produce the same pattern. Guided by this result, we trained only with rationales attached to correct teacher answers and compared answer-only training, step-by-step distillation, and our proposed Distill-SFT method. Distill-SFT showed a modest advantage over step-by-step distillation on previously missed questions under reasoning, while using fewer training instances by combining the answer and rationale into a single target. We also investigated catastrophic forgetting using the out-of-domain ENEM dataset. Answer-only training reduced reasoning accuracy by 12~p.p. relative to baseline, compared with approximately 4~p.p. for either rationale-based training method. Together, these findings support a workflow that audits rationale content before distillation, verifies teacher answers before supervision, and trains compact models efficiently for health professions question answering.

---


### 399. [What Is the "Self" of a Large Language Model?](https://arxiv.org/abs/2610.16717)

**<font color=#1a73e8>作者：</font>** Yuchen Li, Zongqi Fan, Xintong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What could the "self" of a large language model be, if it is neither a particular word nor a single privileged layer? We propose a relational account: a functional self is an actor-centered organization of information that distinguishes the model's recorded actions from externally supplied material while content and reasoning operations change. Its representational candidate is a family of layer-specific source-binding components, rather than one unchanged vector throughout the network. Preliminary observations from a 27B BF16 model provide a geometric starting point. Across 150 matched message bodies, 450 role conditions, and a 75/75 discovery-held-out split, the combined Assistant-versus-external displacement transfers strongly across bodies and positions. Selected early components place User and System closer to one another than to Assistant, whereas this full-space distance relation does not persist throughout depth. These findings motivate a layered account: an early source-encoding candidate can be combined with role-specific information use and continuation preparation at later depths, without requiring monotonic overwriting of the common displacement. We connect this account to dynamic reasoning, historical continuity, and a computational model separating content operations, source binding, authority, and output. The reported evidence establishes a reproducible role-conditioned geometry; the proposed interpretation is that functional selfhood may reside in persistent relations among changing representations.

---


### 400. [Trace-to-Architecture: Capability Bottleneck Diagnosis for Harness Revision](https://arxiv.org/abs/2610.16725)

**<font color=#1a73e8>作者：</font>** Wenfeng Wang, Jianrui Shi, Mingang Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving an LLM agent requires knowing what to change when it fails. Similar failures can require different fixes, and resolving one problem can expose another. We introduce Trace-to-Architecture (T2A), a framework that uses execution trajectories to determine what to change in an agent's harness and when those changes apply. A development agent diagnoses failures using execution evidence from successful and failed tasks, revises the corresponding harness components, and then checks whether target tasks improve, selected successful tasks remain successful, and the edits are actually triggered. New execution evidence guides subsequent diagnosis and revision. Across ALFWorld, ScienceWorld, and AppWorld, T2A achieves the highest aggregate score for all three evaluated task agents, exceeding their respective strongest baselines by 6.2--30.3 points. We also integrate T2A's diagnosis and validation procedures into Meta-Harness, improving the resulting harnesses' mean ScienceWorld score by 21.6 points from the same starting harness.

---


> [!TIP]
> 当前位于：**351-400**（第 8/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
