# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 51. [A Large-Scale Benchmark and Risk Assessment of Traffic Analysis Attacks on Cloud LLM Services](https://arxiv.org/abs/2609.31877)

**<font color=#1a73e8>作者：</font>** Shahrooz Pouryousef, Jesus Lopez, Saeefa Rubaiyat Nowmi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-based Large language model (LLM) services create a network-level traffic side channel that can expose model, prompt, and task behavior despite encryption. From packet sizes, directions, timing, and burst structure alone, a passive local observer can infer the serving model, the user's prompt category, and the task executed by a collaborative multi-agent system. Yet current evidence is fragmented across separate datasets and settings, limiting reproducibility and comparison. We present, to our knowledge, the first unified measurement study and public benchmark of encrypted LLM traffic across both user--LLM and multi-agent executions. The large-scale benchmark contains 60,000 user--LLM interactions across 10 models and 6 prompt categories, plus 2,838 multi-agent executions covering 10 task categories and two coordination topologies. Using only encrypted packet metadata, we assess the risk of traffic analysis attack by characterizing traffic signatures, identifying the features most associated with leakage, and testing robustness under prompt reformulation, decoding-temperature changes, larger candidate model sets, and partial traffic observation. Model fingerprinting achieves 97.7\% balanced accuracy, prompt-category fingerprinting reaches 76.7\% mean accuracy, and multi-agent task fingerprinting achieves up to 90.7\% accuracy. Prompt reformulation weakens but does not remove model-specific leakage, and task fingerprints remain detectable even from a single agent's traffic.

---


### 52. [TemporalGraphLLM: Temporal Graph Neural Networks with Large Language Models for Dynamic Text-Attributed Graphs](https://arxiv.org/abs/2609.31881)

**<font color=#1a73e8>作者：</font>** Moran Beladev, Or Eitan, Gilad Katz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic text-attributed graphs (DTAGs), where nodes, edges, and textual attributes evolve over time, are crucial in applications such as social networks, citation graphs, and knowledge graphs. However, existing approaches struggle to jointly model the temporal evolution of graph structures and the semantic richness of textual attributes. While Temporal Graph Neural Networks (TGNNs) capture evolving node relationships, they often lack contextual text reasoning. Conversely, Large Language Models (LLMs) excel in textual understanding but struggle with structured graph reasoning in temporal settings. To bridge this gap, we propose TemporalGraphLLM, a novel framework that can integrate any temporal GNN with an LLM for enhanced reasoning in DTAGs. Our approach fine-tunes LLMs using graph-time-aware instruction tuning and novel temporal GNNs injection to replace dedicated added tokens with graph embeddings. TemporalGraphLLM effectively leverages pretrained TGNNs within an LLM framework to achieve state-of-the-art performance on edge classification, link prediction, and edge-based text generation tasks. Extensive evaluation on real-world dynamic graph datasets demonstrates state-of-the-art performance. Our findings highlight the synergistic potential of LLMs and TGNNs, opening new directions for learning on evolving graphs.

---


### 53. [Understanding the Synergy between SFT, RLVR, and OPD in LLM Post-Training](https://arxiv.org/abs/2609.31900)

**<font color=#1a73e8>作者：</font>** Emre Can Acikgoz, Yang Li, Zeyu Leo Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM post-training composes supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and on-policy distillation (OPD) into multi-stage pipelines, yet these stages are typically designed and evaluated in isolation. We show that this composition is consequential: a stage that improves the current model can make the next stage less effective. Through controlled experiments with Qwen3 models on math and science reasoning, we first characterize OPD across nine student-teacher pairs spanning 2x to 53x parameter ratios and show that OPD effectiveness depends on student-teacher compatibility rather than teacher scale alone. The surrounding stages of OPD reshape this compatibility in three ways: (1) A brief SFT warm-up improves subsequent OPD, while an RLVR-strengthened student regresses under distillation from the same teacher. (2) Adapting the teacher with RLVR raises downstream OPD accuracy in proportion to the capability it adds. Following these two interventions, we find that combining teacher adaptation and student warm-up alone raise average OPD accuracy from 29.2\% to 43.8\% (50\% relative improvement) after the same number of distillation steps, with additional preparatory training. (3) At comparable accuracy, OPD leaves a stronger initialization for downstream RLVR than SFT, with a gap that widens as RL compute scales. Our results suggest that each post-training stage should be chosen not only for the capability it adds, but for the learning interface it creates for the next stage.

---


### 54. [Choir: An Open Protocol for Distributed Multi-Agent Autoformalization](https://arxiv.org/abs/2609.31903)

**<font color=#1a73e8>作者：</font>** Yidi Qi, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can now formalize entire textbooks and major theorems in proof assistants such as Lean, but current efforts are typically centralized: a single team runs all agents and bears the full computational cost. We introduce Choir, an open protocol for distributed formalization. Choir decomposes a project into tasks that can be completed by independent contributors, each running their own agent with their own LLM subscription, while coordinating entirely through the project's GitHub repository. To support open participation, every contribution is checked by a deterministic gate before merge. Choir supports Lean 4, Isabelle, and Rocq, and is open source and modular, allowing projects to replace individual components or extend the protocol.

---


### 55. [EmailBench: A Benchmark for Evaluating LLM Agents on Enterprise Email and Productivity Tasks](https://arxiv.org/abs/2609.31906)

**<font color=#1a73e8>作者：</font>** Mukul Singh, Mansi Uniyal, Devin Devlin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise email agents must combine information retrieval, structured state changes, temporal reasoning, and multi-step coordination. Recent agent benchmarks include productivity tasks, but few center on typed email workflows in a self-contained environment. We introduce EmailBench, a benchmark of 206 email and productivity scenarios across 16 task categories. The benchmark couples a typed email API specification with provider-neutral naming, a deterministic synthetic Enron-inspired corpus, and a scenario suite whose topic selection was informed by aggregate task-intent telemetry from an interactive prototype. Its hybrid evaluation protocol combines 258 executable static assertions with 211 LLM rubrics. We evaluate eight LM configurations on a fixed single-user corpus. The best-performing configuration passes only 33.5% of scenarios despite 99.7% of its tool calls completing without an observed API failure, with pass rates varying substantially across task categories. This gap shows that valid tool execution is not equivalent to task completion. EmailBench provides a self-contained environment for end-to-end email-agent evaluation, with broader tool coverage, multi-persona testing, and repeated-run evaluation as future work areas.

---


### 56. [Improving Medical Calculation of LLMs with Embedded Coding](https://arxiv.org/abs/2609.31908)

**<font color=#1a73e8>作者：</font>** Tianshi Ming, Yingying Zhang, Xian Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) perform well on medical examinations and question-answering benchmarks, but remain unreliable on medical calculation tasks that require exact numerical outputs. These calculations support high-stakes decisions such as medication dosing, organ-function assessment, and prognostic scoring, for which even small errors can have serious clinical consequences. We introduce MedCode, a framework that improves medical calculation by training LLMs to generate embedded executable code. Given a clinical context, the model identifies the relevant calculator, extracts its input variables, and produces a script that delegates arithmetic operations to a deterministic interpreter. Executing the script returns the calculated value together with an explanation and the appropriate unit. We construct supervised fine-tuning (SFT) and preference datasets from the MedCalc benchmark and additionally curate a dataset for calculation tasks in Intensive Care Unit (ICU) scenarios. We further propose weighted Direct Preference Optimization (wDPO), which adaptively emphasizes preference pairs that are difficult for the model to distinguish. Experiments with LLaMA3-8B, Qwen2.5-7B, and Mistral-7B show absolute accuracy gains of 20--30 percentage points, demonstrating the effectiveness of embedded code generation for medical calculation.

---


### 57. [Enhancing Visual Reasoning in Chest X-Ray Report Generation Using Reinforcement Learning](https://arxiv.org/abs/2609.31911)

**<font color=#1a73e8>作者：</font>** Denis Musinguzi, Andrew Katumba, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical report generation has made significant progress with the rise of modern vision-language models and the growing availability of large-scale medical datasets. However, hallucinations remain a major challenge, largely due to the limitations of supervised fine-tuning (SFT), which prioritizes lexical similarity to reference reports rather than clinical correctness. While reinforcement learning has shown strong performance in domains with verifiable rewards such as mathematics and code generation, its application to open-ended medical tasks remains limited. Existing work focuses on evaluating final answers, overlooking the model's reasoning, despite evidence that flawed reasoning can degrade overall performance. In this study, we propose a framework that verifies the model's reasoning process by integrating anatomical regions, bounding boxes, and region-level textual descriptions. We design spatial and factual reward mechanisms to ensure that the model's reasoning is both visually grounded and factually accurate. Starting from Qwen3-VL-8B-Instruct as our base model, we adapt it to the medical domain using supervised fine-tuning, introduce reasoning capability through a cold-start SFT stage, and refine it with reinforcement learning. We find that RL provides performance gains beyond those achievable through SFT alone, and that jointly verifying both reasoning steps and final outputs yields larger improvements than verifying either in isolation. We further identify multiple modes of reward hacking in the RL stage. Finally, the model's structured think traces enhance interpretability, making its outputs easier to audit for clinical use.

---


### 58. [Vibe Analysis: Exploring LLM Adoption by Data Visualization Practitioners](https://arxiv.org/abs/2609.31922)

**<font color=#1a73e8>作者：</font>** Shani C Spivak, Aditi Krishna, Mahsan Nourani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are enticing in their promise to support data visualization (Vis) through faster and simpler workflows for data prep, analysis, and visualization creation. Yet LLMs are notoriously error-prone and not built for data visualization tasks. Few studies have explored LLM adoption among Vis practitioners. To fill this gap, we conducted semi-structured interviews with members of the Data Visualization Society, a global community of data visualization designers. Our findings show that Vis designers actively use LLMs for both creative and technical aspects of the visualization process. A new visualization workflow is emerging, a process we call vibe analysis, analogous to vibe coding. Some key challenges raised by participants parallel those of vibe coding, while others are Vis-specific, like gaps in Vis knowledge and chart verification. This work opens up opportunities for research combining LLM-mediated work with Vis tools that incorporate data visualization guidance, constraints, and best practices.

---


### 59. [Resource-Aware Federated Mixture-of-Experts with Adaptive Pruning for Onboard Learning in LEO Satellite Constellations](https://arxiv.org/abs/2609.31932)

**<font color=#1a73e8>作者：</font>** Mohamed Shaaban, Mohamed Elmahallawy, Marius Bernahrndt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Earth-orbit (LEO) satellites are increasingly expected to perform onboard learning for applications such as disaster response and environmental monitoring. However, conventional federated learning (FL) is ill-suited to onboard satellite learning, as it assumes computational, memory, and communication resources beyond the capabilities of resource-constrained LEO platforms, often necessitating the transmission of raw imagery to ground stations. We present COSMIC-FL, a resource-aware FL framework for efficient onboard learning in LEO satellite constellations. COSMIC-FL introduces two complementary Mixture-of-Experts (MoE) architectures: a Sliced design that shares backbone representations while activating task-specific channel subsets, and a Modular design that employs lightweight gating to route inputs to physically separated expert networks. A semantic class-to-expert mapping enables each satellite to train, update, and communicate only the expert paths relevant to its local data. To further improve efficiency, COSMIC-FL integrates staged optimization with three structured pruning strategies: server-side pruning, client-side fixed-ratio pruning with mean-vote aggregation, and adaptive client-side per-layer pruning based on aggregated importance and a MAD-based gap criterion. Combined with semantic expert routing, these techniques jointly adapt computation and model sparsity to both data semantics and layer importance, yielding a favourable accuracy--efficiency trade-off for heterogeneous space platforms. Experiments on six image classification benchmarks under highly non-i.i.d. settings show that COSMIC-FL maintains competitive accuracy while reducing communication, computation, and energy consumption by up to 80% over SOTA FL methods. We further validate COSMIC-FL on an NVIDIA Jetson AGX Orin, confirming its efficiency gains under realistic embedded deployment constraints.

---


### 60. [BioDyad: Synchronize Biomedical Discovery and Machine Learning Engineering](https://arxiv.org/abs/2609.31939)

**<font color=#1a73e8>作者：</font>** Xingbo Du, Fadli Aulawi Al Ghiffari, Leonard Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic biomedical machine learning (ML) draws on complementary advances in biomedical evidence acquisition and executable program search. Existing systems connect aspects of these capabilities, but coordinating them throughout program search remains challenging. New evidence must guide candidate construction, execution outcomes must inform subsequent discovery and reuse, and validation demands must fit the search budget. We introduce BioDyad, which couples biomedical discovery and ML engineering through two hierarchies within Monte Carlo graph search. Its scientific hierarchy combines prior biomedical guidance with iterative discovery, then links biomedical plans to execution outcomes in memory for reuse across candidates. Its engineering hierarchy moves candidate programs from smoke execution, through train/validation evaluation, to full-data retraining. We evaluate BioDyad on the 76-task BioXArena benchmark under a two-hour per-task budget with three matched LLM backends. It achieves the highest penalized all-task score and task success rate among four agent methods and a one-shot baseline under each backend. These results support coordinating biomedical discovery and ML engineering to integrate external knowledge into executable programs across heterogeneous biomedical tasks.

---


### 61. [On-Policy Attention Linearization](https://arxiv.org/abs/2609.31947)

**<font color=#1a73e8>作者：</font>** Arian Raje, Anupam Nayak, Anthony Fei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid transformer architectures that replace most softmax attention layers with linear attention offer transformer-level quality at a fraction of the memory cost. Rather than pretraining such models, a growing body of work distills them from already trained full-attention transformers. However, these distilled models often collapse on long-context retrieval and reasoning tasks, particularly when operating in thinking mode, where the efficiency gains of hybrid architectures matter most. Since linear attention layers must compress context into a fixed-size state, their errors compound over long sequences. As off-policy distillation never teaches the student model to recover from this drift, tasks that necessitate longer sequence lengths become especially challenging. We introduce On-Policy Attention Linearization (OPAL) in which the hybrid attention student samples its own long-context trajectories and receives dense supervision from the frozen full-attention teacher. Applying OPAL to Qwen3-4B and MiMo-7B-RL-0530, we recover $87$--$94\%$ of full-attention performance on commonsense reasoning, $100\%$ on needle-in-a-haystack (NIAH) retrieval, and $83$--$93\%$ on mathematical reasoning with only 3B training tokens. We achieve these results without supervised fine-tuning (SFT) or reinforcement learning with verifiable rewards (RLVR). Compared with the strongest prior linearization method, which recovers $68\%$ of its teacher's retrieval performance and $21.6\%$ absolute average mathematical reasoning accuracy, OPAL fully recovers retrieval and achieves $67.6$--$72.2\%$ on math reasoning.

---


### 62. [CaptchaArena: A Large-Scale, Fine-Grained Dataset for Training Computer-Use Agents on Interactive CAPTCHAs](https://arxiv.org/abs/2609.31957)

**<font color=#1a73e8>作者：</font>** Zhenhao Zhang, Zhaoyu Fan, Haohan Ying 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive CAPTCHAs remain challenging for computer-use agents, while existing datasets face trade-offs among type coverage, interaction fidelity, and trajectory supervision. To address these gaps, we present CaptchaArena, the first large-scale, fine-grained training dataset for interactive CAPTCHA solving. It contains 50K puzzles across 20 CAPTCHA types and 5 interaction modes, with every solution verified through execution. CaptchaArena provides 50K screenshot-action trajectories, including 46K with step-by-step reasoning annotations. It also includes fine-grained pixel-mask annotations for irregular targets. Using CaptchaArena, we train CaptchaAgent, a single 9B policy for all 20 CAPTCHA types, with supervised fine-tuning followed by reinforcement learning. The environment verifier directly provides the RL reward. Supervised fine-tuning reaches 70.5 Pass@1, and reinforcement learning further improves it to 71.7, while also improving performance on two external benchmarks. These results demonstrate the value of large-scale, fine-grained computer-use supervision for training interactive CAPTCHA agents. We release CaptchaArena and CaptchaAgent at this https URL.

---


### 63. [Model-Agnostic Online Certificate-Driven Calibration for Time Series Forecasting Under Distribution Shift](https://arxiv.org/abs/2609.31960)

**<font color=#1a73e8>作者：</font>** Chenfeng Huang, Zixuan Ma, George Michailidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series out-of-distribution generalization requires forecasters to remain reliable when deployment dynamics differ from training conditions due to covariate shift, concept shift, and temporal dependence. Probably Approximately Correct Bayesian domain adaptation provides computable certificates by decomposing target risk into a source risk term, a source-to-target mismatch term, and a complexity term, but standard analyses rely on independent sampling and distributional stability, assumptions that are violated in time series by serial dependence and nonstationary shift. We propose a model-agnostic online martingale Probably Approximately Correct Bayesian framework that yields finite-sample certificates under temporal dependence and distribution shift. The certificate replaces independent-sample concentration with martingale concentration that adapts to loss scale and predictable variation. We use the certificate as a surrogate regularizer for online calibration by training a gated residual Bayesian head on top of a fixed forecasting backbone, producing a corrective update that reverts to the backbone prediction when the gate is closed. Online calibration combines a source risk anchor, a posterior-shift penalty, and a time-adaptive mismatch term computed from target windows observed before forecasting. It follows a predict-then-update protocol in which outcomes become available only after forecasting and are used to update subsequent predictions. Experiments across convolutional, attention-based, and large language model-based forecasters show improved stability and accuracy under covariate and concept shift.

---


### 64. [Symbolic Guidance for LLM Agents in Distributed Multiagent Coordination](https://arxiv.org/abs/2609.31963)

**<font color=#1a73e8>作者：</font>** Ben Rachmut, Ning Zhang, Yevgeniy Vorobeychik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as autonomous agents in multi-agent systems, yet their ability to reliably execute distributed coordination protocols remains poorly understood. While AgentsNet, a benchmark framework for distributed coordination among LLM agents, enables such coordination, granting full reasoning autonomy often leads to inconsistent or degraded performance in complex domains.
We hypothesize that coordination can be improved by regulating agent autonomy through symbolic guidance derived from established algorithms. To investigate this, we introduce the \emph{Symbolic Guidance Taxonomy (SGT)}, which characterizes a spectrum of autonomy ranging from open-ended natural language reasoning to fully prescribed algorithmic execution, with intermediate levels providing partial pseudocode guidance. Our results show that intermediate autonomy levels consistently outperform both unguided agents and fully prescriptive specifications. These findings identify autonomy regulation as a key design principle for LLM-based distributed coordination.

---


### 65. [IndicFDB: Benchmarking Full-Duplex Voice Agents across Indian Languages](https://arxiv.org/abs/2609.31967)

**<font color=#1a73e8>作者：</font>** Rajarshi Roy, Shobhit Banga, Jonathan Raiman 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex voice agents must handle pauses, take turns, backchannel, and respond to user interruptions in real time. Full-Duplex-Bench evaluates these behaviors, but its English-only corpus and reliance on word-timestamped ASR and an English-prompted LLM judge make it difficult to extend to Indian languages. We introduce IndicFDB, which extends it to ten languages spoken in India with 12,350 samples, nearly 17 times as many as the original. We address three challenges: finding conversational events in multilingual speech, evaluating their timing without reliable word-level alignment, and judging responses across languages. We mine pause handling, turn taking, and backchanneling samples from roughly 50,000 hours of channel-separated conversations using voice activity detection (VAD), and construct human-validated synthetic user interruption samples. Language-independent VAD heuristics evaluate timing, while an open-weight transcription and translation pipeline converts responses to English for LLM ratings of relevance and quality. Across seven voice agents, commercial APIs show unexpectedly consistent behavior across languages but are either fast or robust to pauses, never both, while monolingual open full-duplex models expose further tradeoffs among backchanneling, response quality, and latency.

---


### 66. [Extraction of clinical findings from mammography and breast ultrasound reports: a comparison between specialists and Artificial Intelligence](https://arxiv.org/abs/2609.31974)

**<font color=#1a73e8>作者：</font>** Lorenzo Farias, Hanna Reckziegel, Daniela Duarte da Silva Bagatini 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Breast cancer is the leading cause of cancer-related death among women in Brazil, and the time between the request and the release of mammography reports directly influences adherence to screening, making the agility in processing these reports a critical factor for early diagnosis. In this context, this study compares the performance of a Large Language Model (LLM) with manual extraction performed by a team of health researchers in identifying clinical findings from mammography and breast ultrasound reports written in Brazilian Portuguese. Named Entity Recognition (NER) was applied through Prompt Engineering using a few-shot strategy, employing the Gemini 2.5 Flash model, selected from preliminary exploratory tests with four candidate models. The Gemini 2.5 Flash model demonstrated the best performance, achieving a Macro F1 of 0.91 and a Micro F1 of 0.98. The subjective validation, in which 29 exams of different formats were evaluated by health researchers using a Likert scale, yielded an agreement index of 93.1%. The model outperformed human extraction in overall Macro F1 (0.91 vs. 0.72), as in four reports the model correctly identified information that had been omitted or incorrectly recorded during manual extraction, demonstrating its potential as a complementary verification tool alongside specialists. The results confirm the hypothesis that LLMs, when instructed through Prompt Engineering, can achieve performance comparable to or superior to manual extraction by health professionals.

---


### 67. [Goal-Persistent Coding Agents as Scientific Performance Engineers: A Fixed-Radius Nearest-Neighbor Case Study](https://arxiv.org/abs/2609.31980)

**<font color=#1a73e8>作者：</font>** Xiangyang Ju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents can pursue persistent objectives across many tool-use turns, but evidence that general-purpose agents can conduct rigorous scientific performance engineering remains limited. We present a repository-scale case study in which off-the-shelf Codex and Claude Code agents optimize fixed-radius nearest-neighbor (FRNN) search for particle tracking. Starting from a PyTorch-dependent CUDA implementation, the agents follow an executable goal that specifies exact-correctness tests, profiling requirements, and acceptance criteria without prescribing code transformations. In the primary sequential trajectory, they autonomously remove the PyTorch dependency and conduct hypothesis-driven optimization experiments. The resulting standalone C++/CUDA library exactly reproduces the targeted reference result. Its synchronous NumPy interface achieved 1.6-fold speedup over the original GPU-resident PyTorch interface, despite including host transfers. Similar speedups were observed across different GPU architectures and software stacks. An independent optimization rerun followed a different sequence of hypotheses and reached even better performance on the target workload. These results show that goal-persistent coding agents can act as experimental performance engineers, and that executable scientific contracts are needed both to guide and to validate their optimization.

---


### 68. [Communication between Frozen Large Language Models via Prompt Optimization in a Referential Game](https://arxiv.org/abs/2609.31989)

**<font color=#1a73e8>作者：</font>** Vivek Anand, Muthu Chandrasekaran, Shiva Chaitanya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study communication between two frozen large language models from different providers, with different tokenizers, accessed through their API endpoints. The two play a referential game: one sees an object and describes it in a short fixed-length message over a small alphabet; the other must pick that object out of a candidate set. Neither model's weights are updated. Each agent's prompt is rewritten by an isolated prompt optimizer whose reflection model reads that agent's scored interactions. In the positional setting, optimized prompts carry a shared code that generalizes to held-out objects above a measured no-codebook baseline, including when the memory window is removed. In a second setting, independent per-letter blocks no longer fit within the message, although a whole-object place value code does. The base system fails to establish reliable communication: the sender struggles to retain an injective rule, and the receiver has too few confirmed examples in view. A sender collision penalty, retention of successful interactions, and sequential optimization enable successful place value communication in some runs. Outcomes vary across runs and reflection models. In successful runs, the protocol is written into the optimized prompts, where it can be read and audited directly.

---


### 69. [CSI-Agent: LLM-Assisted Few-Shot Adaptation for Cross-Domain Wi-Fi CSI Sensing](https://arxiv.org/abs/2609.31990)

**<font color=#1a73e8>作者：</font>** Tianya Zhao, Chuan Liu, Xuyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wi-Fi channel state information (CSI) has enabled device-free sensing applications such as human activity recognition. However, CSI sensing models remain brittle in cross-domain deployment, where changes in users or environments can produce incorrect predictions. Existing solutions usually treat this problem as an offline model-design problem, by pretraining a stronger representation or applying one fixed adaptation method to the entire target domain. In practice, labeled target data are scarce and different classes may fail in different ways under the same domain shift. To address this, we propose CSI-Agent, an evidence-seeking LLM agent that reformulates cross-domain CSI adaptation as a deployment-time decision-making problem. Rather than processing raw CSI or making sample-level predictions, CSI-Agent summarizes target-domain behavior into sensing-grounded class-level evidence. It establishes a strong target-adaptive default from complementary CSI views and uses an LLM planner to determine whether each class should retain the default or invoke a specialized action. Deterministic verification and bounded execution further reduce unreliable interventions. We evaluate CSI-Agent on four public datasets using five cross-domain splits covering device, user, environment, and compositional shifts. Under 1-shot adaptation, CSI-Agent achieves the best target-domain performance across all splits and improves the average Macro-F1 by about 16\% compared to the strongest baseline method.

---


### 70. [Before the Rollout Ends: Early Terminal Reward Prediction for Long-horizon Coding Agents](https://arxiv.org/abs/2609.31995)

**<font color=#1a73e8>作者：</font>** Jihan Yao, Sihan Zeng, Shangbin Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon coding agents receive verifiable rewards only after completing expensive sequences of tool calls. This increases inference cost, amplifies early wrong hypotheses, and can lead to sparse terminal reward and unstable training. We introduce Contextual Early Reward (CER), which predicts terminal reward through behavioral evidence in a trajectory prefix. CER synthesizes adaptive rubrics specific to the current task and stage through experiences summarized from related historical tasks. In test-time scaling on SWE-bench Verified, CER improves RM@8 over the strongest baseline by 4.2 percentage points (pp) on Nemotron 3 Ultra and 2.0 pp on Qwen 3.6 27B; on Nemotron, it takes only 15.3% tokens to match the best baseline performance. In RL training experiments, CER exceeds full-rollout TMax by 1.9 pp while using 52.7% fewer online policy-and-judge tokens. Together, CER provides an interpretable, efficient, and dense evaluation method for long-horizon coding agents.

---


### 71. [Integrating Language Models into Listened and Imagined Speech Decoding from MEG](https://arxiv.org/abs/2609.31997)

**<font color=#1a73e8>作者：</font>** Maryam Maghsoudi, Sai Samrat Kankanala, Shihab A. Shamma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding imagined speech is an important goal for brain-computer interfaces but remains challenging due to weak neural responses, low signal-to-noise ratio, and limited imagined-speech datasets. Language models provide strong contextual cues for text prediction, but how much they can help neural decoding and whether their contribution differs for decoding perceived and imagined speech remains unclear. To investigate this, we use a paired listened-imagined MEG dataset and incorporate language-model information at two stages. First, we train a contrastive neural decoder that aligns MEG representations with acoustic and contextual language representations, improving cross-subject word decoding for both listened and imagined speech. Second, at inference, we introduce a neural-constrained beam-search framework that combines neural evidence with language-model next-word probabilities. We find that imagined-speech decoding benefits more from the language model than listened-speech decoding. For Imagined speech, the best-performing balance between neural and language-model evidence shifts toward the language model, and the gain over neural-only decoding is larger. Together, these results suggest that language priors are most useful when neural evidence is weaker, making them particularly valuable for imagined-speech BCIs.

---


### 72. [SenseAgent: An LLM Agent for Adaptive Cross-Domain IMU Sensing](https://arxiv.org/abs/2609.32000)

**<font color=#1a73e8>作者：</font>** Tianya Zhao, Chuan Liu, Xuyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning has improved inertial measurement unit (IMU) sensing for mobile and wearable applications. However, an IMU model trained in one domain often becomes unreliable when it is used with a new user, device, or body position. Existing methods usually treat this problem as a static model-design task: they pretrain a stronger representation, add data augmentation, or select one adaptation method before deployment. In practice, the target domain is only gradually observed, labels are scarce, and different domain shifts require different sensing actions. This paper presents SenseAgent, an LLM-guided sensing agent for cross-domain IMU activity recognition. Instead of asking an LLM to classify raw IMU signals, SenseAgent uses the LLM as a runtime planner over sensing tools, source-domain experience memory, online target memory, and verifiers. The agent builds a label-free diagnosis report from the target stream and uses it to decide whether to keep raw inference or invoke specialized tools, including gravity-aware sensing, prototype transfer, and style normalization. Verifiers check source calibration, target-memory reliability, and no-harm criteria before accepting high-risk tool decisions. SenseAgent also supports scarce feedback without retraining the backbone or replacing the label-free route. This design converts cross-domain IMU sensing from a fixed inference pipeline into a closed-loop sensing process that diagnoses target shifts, selects suitable sensing actions, and rejects unsafe adaptations. We evaluate SenseAgent across multiple IMU datasets and deployment shifts. Results show that its verified route selection improves cross-domain sensing, especially under harder placement and compound shifts, and further benefits from limited user feedback.

---


### 73. [A Benchmark for LLM's Understanding of Middle School and High School Science Topics](https://arxiv.org/abs/2609.32020)

**<font color=#1a73e8>作者：</font>** Noah L. Schroeder, Yessy Eka Ambarwati, Yuji Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into educational settings, yet educators lack robust, standards-aligned tools to evaluate their effectiveness in K-12 science contexts. Existing benchmarks predominantly assess general language or advanced scientific reasoning, leaving a critical gap in understanding LLMs' performance on content directly relevant to secondary science curricula. To address this gap, we developed a comprehensive NGSS-aligned benchmark for both middle and high school science using a rigorous synthetic data pipeline, multi-judge validation, and item-level psychometric analysis. Nine open-weight LLMs were systematically evaluated using this benchmark, indicating that several smaller, locally deployable models achieved high accuracy across diverse science domains and question types. Our findings indicate that model size did not consistently predict performance, emphasizing the importance of intentional model selection for educational deployment. We then incorporated a human reviewer into the loop, reviewing the items generated by the LLMs for alignment with NGSS standards. The human review indicated that synthetically generated items were not in perfect alignment with the NGSS standards, indicating the benefits of human-in-the-loop item development, the need to explore the intersection of content and pedagogical knowledge, and the need to extend benchmarks to evaluate LLMs' capacity for interactive, evidence-based feedback in educational scenarios.

---


### 74. [ScreenHaystack: Finding Blind Zones in GUI Grounding](https://arxiv.org/abs/2609.32036)

**<font color=#1a73e8>作者：</font>** Chenyue Li, Xiaoxiao Sun, Yubo Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ScreenHaystack, a dynamic needle-in-a-haystack benchmark for evaluating spatial reliability in GUI grounding. Instead of testing each target at a fixed position, ScreenHaystack systematically relocates controlled target icons across high-resolution GUI backgrounds and measures whether models can localize them consistently. Using this benchmark, we find that leading GUI grounding models, including Qwen3-VL, UI-TARS, GTA, and UI-Venus, exhibit blind zones: spatial regions where grounding accuracy drops sharply despite fixed target appearance and instruction. These blind zones transfer to unseen ScreenSpot-Pro examples: targets inside blind zones are consistently harder to ground, with Qwen3-VL-8B dropping by 16.1 percentage points, and controlled relocation shows that moving targets into blind zones decreases accuracy while moving them out improves accuracy. We further show through controlled synthetic experiments that uneven spatial coverage in training data can induce such blind zones. Therefore, we propose a simple strategy, blind-zone-oriented augmentation, which adds supervision in blind zones and improves ScreenSpot-Pro accuracy over both original and randomly augmented Click-100k fine-tuning.

---


### 75. [Quantization Thresholds Replicate, Failure Modes Do Not: A Three-Model Study of Agentic Tool Use in Polish from 8-bit to 2-bit](https://arxiv.org/abs/2609.32042)

**<font color=#1a73e8>作者：</font>** Jakub Prejzner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask how GGUF quantization affects agentic tool use in Polish and whether the effects generalize across models. We introduce PolAgentBench, a deterministic benchmark with Polish prompts and English tool schemas: a 67-task main suite (15 adversarial probes, 52 hard-tier tasks) and a 46-task arithmetic isolation ladder. Three models span two axes of variation: Bielik-11B-v3.0 and its pruned, distilled child Bielik-Minitron-7B-v3.0 isolate model compression, and Llama-PLLuM-8B adds a change of pretraining family. Each is measured at six precisions, Q8_0 to Q2_K. Only the collapse threshold replicates. (1) All three models fall off a cliff between 3-bit and 2-bit (11B 0.716 to 0.045, 7B 0.463 to 0.149, PLLuM 0.224 to 0.015; paired McNemar p < 0.001 in each), across a fourfold capability spread and both axes. (2) Failure modes do not replicate: at 2-bit the 7B fails long (median 9.1k tokens, 4 steps) while the 11B mostly answers at the first step with a confabulated final answer (37 of 64 failures); PLLuM fails on content across precisions (71.8-92.0% of steps parse). (3) On the arithmetic ladder the unscaffolded rung is a floor, left standing by a rerun that states the no-tool rule; four explicit calls lift the 8-bit 11B from 1/10 to 9/10 and the 7B from 0/10 to 7/10 after format-only failures with the gold value are forgiven, an exploratory effect with eight distinct baseline inputs that does not survive multiplicity correction, while the order-trap arm separates the models at 8-bit (11B 6/6, 7B 0/6). (4) The Polish-versus-English gap is associated with degradation or with task family. We document four artifacts that shaped our conclusions (rounding-hostile gold values, strict answer typing, a no-tool rule the prompt never stated, priority-ordered failure labels), report affected results in strict and corrected form, and release the benchmark, trajectories and commit-stamped artifacts.

---


### 76. [Receiver-Conditioned Latent Communication gives 94% CacheBack](https://arxiv.org/abs/2609.32046)

**<font color=#1a73e8>作者：</font>** Maximillian Rossi, Prajwal Raghunath, Haoqing Xuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems distribute large contexts across agents that communicate to solve a task. Text messages are compact but require decoding and may omit evidence the receiving agent needs. Recent latent communication instead transfers KV caches. This avoids text generation and can improve accuracy and latency. However, a full KV cache grows linearly with both the context an individual agent processes, and the number of agents that coordinate together. This raises memory and context costs, often far exceeding available GPU resources and context window sizes. Our key observation is that agents need only send what the receiving agent requires for its local task -- which we call receiver-conditioned communication. The receiver agent passes the sender a small description of its information needs, which serves to filter and compress the sender agent's KV cache. CacheBack is a simple, robust, training-free instance of receiver conditioning based on the sender's attention weights. On FanOutQA, CacheBack with Qwen 3 removes 75% of the state the agent would otherwise receive, improving accuracy by 14.7 percentage points and reducing median task-completion latency by 3.2x relative to text communication. We show comparable improvements across model families that span dense Transformers, Mamba-attention hybrids, and sliding-window attention.

---


### 77. [EngramRAG: Dynamic Usage-Weighted Topology and Synaptic Consolidation for Multi-Hop Agentic Memory](https://arxiv.org/abs/2609.32049)

**<font color=#1a73e8>作者：</font>** Bhavyateja Potineni, Lohit Giri, Anu Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous LLM agents are deployed across multi-session environments, conventional memory architectures suffer from Associative Blindness (inability to traverse multi-hop relational dependencies), Scaffolding Amnesia (temporal decay evicting core persona invariants), and Static Topology Stagnation (immutable graphs ignoring usage dynamics). Grounded in Complementary Learning Systems (CLS) principles, we propose EngramRAG, an adaptive memory architecture coupling a low-latency Waking State reflex with an asynchronous background Dreaming State consolidation cycle. EngramRAG introduces: (1) Usage-Modulated Personalized PageRank (U-PPR), where transition probabilities adapt via Hebbian plasticity to promote persistent entities into high-centrality Epistemic Macro-Hubs; (2) Consolidation-Activated Topology Decay (CATD), which scales retention half-life by topological load-bearing weight rather than wall-clock recency, protected by a cold-start grace period (N_grace >= 4); (3) Directed SUPERSEDES DAG filtering to suppress obsolete state during fact mutations; and (4) Triple-source hybrid retrieval fusing dense vectors, BM25, and U-PPR via dynamic Reciprocal Rank Fusion (RRF). Evaluating on all 1,982 QA pairs across 10 long-term conversations in the LoCoMo benchmark, EngramRAG achieves +38.9% relative improvement in Recall@5 (53.21% vs. 38.29%, p < 0.001) and +43.1% in MRR (0.4203 vs. 0.2937) over dense vector RAG, significantly outperforming Okapi BM25 (48.66%) and isolated static graph retrieval (8.50%). On temporal reasoning, EngramRAG reaches 62.33% Recall@5 (+16.67 points over dense vectors). In controlled mutation tests, SUPERSEDES suppresses split-brain hallucinations from 70.0% to 0.0%, while 90-day simulations show 100.0% scaffolding retention under a 26.21ms interactive retrieval reflex.

---


### 78. [Depth Laws for the Precision Floor of Trained Neural Networks: Amplification, Residual Scaling, and a Quantization-Aware Training Paradox](https://arxiv.org/abs/2609.32060)

**<font color=#1a73e8>作者：</font>** Ahmad S. Tarawneh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How many bits does a network need before its accuracy collapses, and how does this grow with depth? We study the precision floor, the perturbation level or bit-width at which accuracy falls halfway to chance, in MLPs, CNNs, Vision Transformers and nine pretrained language models, under post-training quantization (PTQ) and quantization- or noise-aware training (QAT). (i) A first-order theory sets the floor through one full-precision quantity, the predictive amplification $G$: $\eta_c=\Lambda/G$, and $G^2$ grows linearly in depth at a rate proportional to the squared residual branch scale. (ii) The predicted equality $\alpha_{PTQ}=\rho$ of depth exponents holds within 95% intervals in twelve of thirteen trained architectures and in GPT-2 from 12 to 48 layers, with $\Lambda=1.45\pm14\%$ across trained architectures. (iii) Residual branches scaled by $1/\sqrt{D}$ and pre-normalisation remove the depth penalty, and each quantizer turns noise into bits at a rate fixed by its step rule, giving $b_c=(\alpha/\gamma)\log_2 D+C$. (iv) A QAT paradox: noise-aware training roughly doubles the tolerable noise of shallow networks, but the gain decays with depth, so the depth law steepens ($\alpha_{QAT}/\alpha_{PTQ}=1.45$-$1.47$ on two datasets, ten seeds each). Decision margins, cross-layer error cancellation and heavy tails do not set the floor.

---


### 79. [Toward Interactive Understanding of Code APIs](https://arxiv.org/abs/2609.32081)

**<font color=#1a73e8>作者：</font>** Dhananjay Ashok, Jesse Thomason, Jonathan May  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empowered by advances in Language Model agents, systems have made substantial strides in code generation and understanding. However, these approaches often rely on read access to the relevant code, an assumption which does not hold when dealing with external APIs. In this work, we introduce the PAU (Python API Understanding) benchmark, where we provide models with black-box, API-level access to code snippets. Models must query the API with exploratory inputs and draw insights from the resulting outputs, with the goal of describing the snippet's true functionality. By treating the code snippets as external tools that must be understood via interaction alone, PAU studies the more general problem of unsupervised tool understanding, specifically for tools implemented as Python methods. Despite recent progress in coding agents, even frontier models struggle to achieve high performance on PAU, with the best model (Claude-4-Opus) failing to understand over 45% of the PAU test set. An investigation into the common error modes reveals that models are overconfident; they often overrate the quality of their current hypothesis, leading to insufficient exploration and premature termination. Finally, we take inspiration from the Asymmetric Actor Critic (AAC) paradigm, frequently used in robot learning, to post-train models for interactive code understanding. Models trained with AAC conduct more active exploration of the APIs, with an AAC-tuned Qwen3-8B model matching the performance of GPT-5-mini.

---


### 80. [mu-bench: A Multilingual Utterance Transcription Benchmark](https://arxiv.org/abs/2609.32082)

**<font color=#1a73e8>作者：</font>** Andrea Li, Soham Ray  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice agents depend on accurate automatic speech recognition (ASR) to act on what callers say, yet ASR is evaluated on read, English-centric speech with word error rate (WER), which penalizes surface rather than semantic differences. We introduce mu-bench, a dataset of 4,270 caller utterances from 250 phone calls to an AI banking agent in English, Spanish, Turkish, Vietnamese, and Mandarin, centered on form-field inputs such as names, email addresses, and confirmation codes. We release Utterance Error Rate (UER), an LLM judge of whether a transcript preserves meaning, calibrated against human raters, together with an LLM normalizer that makes WER comparable across providers' output formats. On 1,847 human-rated transcripts, UER agrees with annotators at $\kappa$ = 0.78, versus 0.53 for exact-match WER on normalized text. We rank six commercial providers on a public leaderboard; the best reaches 11.9% UER, and Mandarin is hardest for all six.

---


### 81. [On Evaluating and Improving Conversational Agents in Production](https://arxiv.org/abs/2609.32092)

**<font color=#1a73e8>作者：</font>** Kasra Hosseini, Wen-Sen Cheng, Marco-Andrea Buchmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present a framework for evaluating and improving a large-scale, multi-agent shopping assistant in production, and report lessons from its use. Offline evaluation of such a system faces three obstacles. (i) A logged conversation cannot be replayed against a modified system, because a different response changes every turn that follows. (ii) The unchanged system itself varies from run to run. Its LLM components are stochastic, and in product search the available products, their prices, and the customer's personalization signals change. (iii) Aggregate quality scores combine distinct behaviors, so they show that quality has changed but not which behavior caused the change. Our framework addresses each obstacle in turn. For a reported behavior, an Evaluation Harness generates targeted assertions and a fixed cohort of customer scenarios. It then reproduces the behavior in a local instance of the assistant through grounded user simulation. Instead of replaying the log, the simulator writes new customer turns conditioned on the recorded messages and context. Repeated runs of the unchanged system form a stored baseline. An Improvement Orchestrator turns the assertion results into hypotheses, implements each as an isolated modification, and compares it with the baseline using paired percentile bootstrap intervals over scenario-level differences. When an investigation ends, the harness may propose revisions to future evaluations, subject to human approval and without altering past decisions. We report production investigations with this framework. Assertion profiles showed which positions of a product carousel a failure affected, and repeated runs distinguished a real improvement from run-to-run fluctuation. Audits of the evaluation itself found a judge that lacked the evidence it needed and a model setting that was configured but not applied.

---


### 82. [Emergent One-Third Scaling Law as Attention Tries to Concentrate](https://arxiv.org/abs/2609.32100)

**<font color=#1a73e8>作者：</font>** Yizhou Liu, Sara Kangaslahti, Jeff Gore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The neural scaling law relating longer training to better performance through a power law is central to today's large language models (LLMs), yet its origin remains debated. One recent proposal is that power laws can emerge from the strong non-linearity of a single softmax head learning peaked distributions. What happens with multiple softmax functions, as in LLMs, is unclear. Here, we show through toy models that any softmax learning peaked distributions, regardless of its position in the model, can develop logit magnitudes that grow in a power law with exponent $1/3$, becoming a training bottleneck whose loss contribution decays as a power law with the same exponent $1/3$. The overall loss therefore obeys $1/3$ scaling whenever at least one softmax learns peaked distributions. We confirm that many softmax functions in LLMs learn peaked distributions and that LLM loss scaling matches this $1/3$ prediction. Moreover, logit growth dynamics reveal that attention heads, rather than the language modeling head, are the bottleneck likely driving the $1/3$ loss scaling in LLMs. Attention trying to concentrate on specific information, which is the heart of Transformers, may therefore also be the heart of the neural scaling law of training.

---


### 83. [Residual Streams Read, Recurrent States Remember: The Global Workspace in Mamba Models](https://arxiv.org/abs/2609.32102)

**<font color=#1a73e8>作者：</font>** Wenlong Wang, Fergal Reid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can the global-workspace account of transformer representations extend to state-space language models? We fit Jacobian lenses to the residual streams and recurrent states of Mamba-1, Mamba-2 and Mamba-3, using the original 1000-prompt recipe. Joint residual--state readouts improve recovery of known intermediate concepts over the residual lens on at least five of six task families in every tested Mamba checkpoint. On Mamba-2, state alone exceeds residual and logit lenses on all six families; a normalised joint readout improves on both components on five. Temporal maps and word-list experiments show earlier content remaining state-readable as residual visibility changes. We also propose sign-guarded steering, which improves target top-five success over coordinate exchange on matched verbal-report trials in five models. Recurrent state alone supports this verbal access. These gains do not extend consistently to relational answers: guarded edits often output the edited concept itself, and Mamba-3's joint edits can disrupt successful state-only redirection. Recurrent state thus provides a complementary carrier of workspace content, whose recovery, persistence and causal uses require separate measurements.

---


### 84. [LLM Unlearning Evaluation with TRIAGE](https://arxiv.org/abs/2609.32103)

**<font color=#1a73e8>作者：</font>** Danial Ataee, Peter Triantafillou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can memorize private or harmful information, motivating machine unlearning methods that remove targeted knowledge while preserving other capabilities. However, existing evaluations rely primarily on behavioral benchmarks, which assess \emph{whether} a model appears to forget but provide limited insight into \emph{how} unlearning changes the model or affects related knowledge. We introduce \textit{TRIAGE} (\textit{Tripartite Representation-internal Introspection for Adjacency Gap Evaluation}), a benchmark-agnostic evaluation framework for characterizing these changes. TRIAGE uses diagonal approximations of the Fisher information and Hessian to measure changes in parameter sensitivity and local curvature, and utilizes a Forget / \emph{Adjacent-Retain} / \emph{Generic-Retain} partition to quantify an \emph{adjacency gap} in semantically related knowledge. Based on the magnitude and distribution of these changes, TRIAGE further classifies each algorithm's update as \emph{no-op}, \emph{partially localized}, \emph{collateral dominant}, or \emph{globally destructive}. Across 12 unlearning methods, four language models, and the WMDP, TOFU, and MUSE benchmarks, we find that methods with similar behavioral forgetting can produce substantially different internal changes and patterns of collateral damage. These signatures also vary across models and benchmarks, indicating that the effects of unlearning are not determined solely by the unlearning algorithm. TRIAGE can be applied alongside existing unlearning benchmarks to complement behavioral evaluation with a model-internal view of how unlearning reshapes the model's parameter space and affects retained knowledge.

---


### 85. [SAMBAR: Selective Anchoring via Method of Multipliers for Balanced Knowledge Acquisition and Retention in Vision-Language-Action Models](https://arxiv.org/abs/2609.32108)

**<font color=#1a73e8>作者：</font>** Aayushi Shrivastava, Xunlan Zhou, Hongrui Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models leverage large-scale pretraining to ultimately achieve generalist manipulation. Deployed VLA policies must support continual learning to acquire new tasks over time. Teaching a VLA a new task generally requires finetuning it on demonstrations of that task. However, naively finetuning on downstream tasks causes the policy to forget earlier tasks and degrades generalist capabilities. This failure is known as catastrophic forgetting. Most continual learning methods counter it by replaying data from earlier tasks. However, the old task demonstrations are not always readily available. In this paper, we introduce SAMBAR, a continual learning algorithm that prevents catastrophic forgetting during VLA finetuning without requiring access to the demonstrations of any previously learned task. We propose to cast continual learning as a constrained optimization problem and solve it with the method of multipliers. In our approach, the method of multipliers drives the policy to learn the new task without the model parameters drifting far away from their previous values. In contrast to a standard regularization penalty, the method of multipliers raises the penalty as the constraint violation accumulates by using a dual variable. We also selectively anchor the parameters critical to previous tasks to preserve past knowledge, leaving other parameters free for new task acquisition. The combination of dual variable and selective anchoring, therefore, balances knowledge acquisition with knowledge retention. We evaluate our method, SAMBAR, on the LIBERO simulation benchmark and on hardware. When sequentially finetuning on a VLA, every replay-free baseline we compare against completely forgets the first task it learned, whereas SAMBAR retains every task it has learned.

---


### 86. [How Reusable Are Benchmarks with Richer Feedback?](https://arxiv.org/abs/2609.32109)

**<font color=#1a73e8>作者：</font>** Youssef Allouah, John Duchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether benchmarks reliably guide model selection as developers adapt to evaluation feedback across multiple criteria. We find that the worst-case test-set size needed to estimate the best score among $k$ adaptively chosen models, under any convex combination of the criteria, grows exponentially with the number of criteria, reaching the $\Theta(\sqrt{k})$ cost of answering $k$ adaptive statistical queries with only $O(\log k)$ criteria, at fixed accuracy and confidence. In attacks on multi-task large language model benchmarks with five to ten criteria, feedback restricted to nondominated task profiles produces large reused-to-held-out score gaps and frequent false winners. These results challenge a prominent explanation for prior observed reliable benchmark reuse---that developers mainly respond to convincing improvements over the current best---in rich-feedback settings, while leaving open how often ordinary model development encounters this vulnerability.

---


### 87. [Using LMs to Model the Effects of Context and Coreference during Sentence Comprehension](https://arxiv.org/abs/2609.32119)

**<font color=#1a73e8>作者：</font>** Kohei Kajikawa, Lin Ai, Tatsuki Kuribayashi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) are often used as a tool to model human language processing. Recent studies suggest that severely restricting LMs' context window improves their fit to human psycholinguistic data by simulating human working memory constraints. However, it is possible that this strict memory-decay approach overlooks humans' reliance on long-range structural representations, such as discourse structre. In this work, we systematically vary the context window size of GPT-2 across four large-scale naturalistic English reading-time datasets and observe a U-shaped relationship: Although restricted contexts (< 20 tokens) successfully capture local memory limitations, expanded contexts (500--1,000 tokens) ultimately yield the highest overall psycholinguistic fit. To investigate the mechanism driving this benefit, we conduct a counterfactual inference-time experiment that disrupts cross-sentential entity chains by pronominalizing repeated discourse entities. Obscuring these structural linkages significantly degrades the predictive power of larger context windows by 20% to 40%. Our experiments demonstrate that tracking long-range coreference relations is one important factor for the alignment between LM surprisal and human reading behavior, and approximate the extent to which human comprehenders use global discourse relations during language processing.

---


### 88. [READ-Bench: Benchmarking Historical Instance Retrieval for Time-Series Diagnosis](https://arxiv.org/abs/2609.32123)

**<font color=#1a73e8>作者：</font>** Gerardo Pastrana, Haojun Li, Dhruv Mehta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series diagnostic systems rarely rely on retrieving relevant historical cases, and when they do, retrieval is evaluated only indirectly through downstream prediction. We introduce READ-Bench, a benchmark for historical-case retrieval across 12 diagnostic datasets, centered on multivariate time series, that defines relevance by shared fault or event type rather than signal shape, so visually different traces of the same fault count as relevant while similar-looking traces of different faults do not. Treating retrieval as a base retriever followed by a reranker, we evaluate classical distances, symbolic retrievers, self-supervised and foundation-model embedders, and their fusion, plus label-aware and language-model rerankers, under one protocol that varies supervision, pollution, and corpus scale with significance testing. Under a common channel-independent interface, pretrained representations offer no statistically detectable advantage over strong classical and symbolic baselines for search alone. The decisive factor is a small amount of resolved-case supervision at reranking, namely a Gaussian-process reranker that propagates a few neighbor labels in embedding space, which helps far more than more sophisticated representations or language-model reasoning and holds under pollution and at full corpus scale. Guided by these findings, we fuse a normal-residual-scored embedder with a dynamic time warping leg via reciprocal-rank fusion, then rerank with the Gaussian-process reranker, improving NDCG@10 over its own search stage on all 12 datasets, by +0.11 from reranking and +0.16 over the strongest single base retriever.

---


### 89. [What Should We Freeze? Guarded Freezing: Connectivity Shapes the Fine-Tuning of Pretrained Models](https://arxiv.org/abs/2609.32124)

**<font color=#1a73e8>作者：</font>** Leonel Aguilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When adapting pre-trained models through fine-tuning, freezing weights alone might not preserve performance, as updates elsewhere can change the inputs to the frozen core, ultimately affecting overall performance. We first analyse the case where a selected frozen core can be isolated and propose removal-value, a capacity-based score that approximates HOPE's removal cost averaged over removal orders. We show that in VGG-8, cutting paths from trainable neurons into a frozen core makes selection using this score useful: $70\%$ frozen preserves $5.22\pm0.51$ percentage points more old-task accuracy than DEFT at similar new-task accuracy. In transformers, shared residual streams leave paths into frozen neurons open. For this case, we derive drift-value, a forward-only proxy for the output disturbance from updating each weight entry under a local update model. In language models, at 40 epochs, this policy exceeds adapted Wanda and RIA freezing scores in settings with substantial retention loss, while its differences from Fisher remain unresolved. After 160 epochs on Qwen2.5-1.5B, it retains $0.0433\pm0.0102$ more than static Fisher. In DINOv3 vision-transformer adaptation to point clouds, drift-value retains $0.440$ image accuracy versus $0.187$ for a random mask of the same count. These results motivate Guarded Freezing: select by removal-value when incoming paths are cut, and by drift-value when they remain.

---


### 90. [Checking Leakage Witnesses versus Certifying Bounded Non-Leakage](https://arxiv.org/abs/2609.32134)

**<font color=#1a73e8>作者：</font>** Chao Feng, Burkhard Stiller  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a language-model audit finds no leak, what is needed to certify non-leakage? We study guarantees over a declared prompt domain under an executable leakage criterion and decoding rule. For general bounded polynomial-time evaluators, a supplied leaking execution is polynomial-time checkable, while leak existence is \NP-complete and deterministic certification is \coNP-complete. Exact stochastic certification is $\coNP^{\PP}$-complete at every fixed rational cutoff in $(0,1)$. Restricting the computation can change these bounds. For example, certification is in \coNP\ when all randomness is a terminal draw from an efficiently computed finite probability table. Attention models admit polynomial-time certification when local dependency windows of logarithmic length precede one global head, given deterministic decoding, fixed vocabulary, exact rational weighted means, a direct binary affine readout and finite-automaton prompt domains. A construction with two global layers instead makes certification \coNP-complete over template domains, with one head per layer, polynomial width, logarithmic precision and an inverse-polynomial logit margin. Planted-secret experiments measure what finite audits miss relative to complete references. Among 30 secret--model-state pairs that leak under greedy single-prompt execution on their secret's 4,096-prompt domain, uniformly selecting 256 recorded evaluations per pair misses every leak for an expected $41.06\%$ of these pairs. Batched and single-prompt checks disagree on one complete-domain decision among all 48 fine-tuned pairs, while a same-order repeat reproduces every single-prompt output. These results distinguish computational conditions for certification from the coverage and execution conditions needed to interpret a negative audit.

---


### 91. [CausalDriveBench: Evaluating Causal Reasoning in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2609.32157)

**<font color=#1a73e8>作者：</font>** Narendiran Chembu, Navvrat Rao, Shreedhar Shreeshail Kodate 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models for autonomous driving produce natural-language reasoning alongside predicted trajectories, but whether this reasoning reflects the causal structure of the scene remains untested. We introduce CausalDriveBench, an evaluation framework grounded in Pearl's Causal Hierarchy (PCH) that tests causal reasoning in driving-specific VLAs through structured visual question answering (QA) and alternative-trajectory prediction. To this end, we construct causal scene graphs over nuScenes that distinguish causally active, dormant, and distractor entities, separating perceptual salience from causal relevance. The benchmark spans all four rungs of PCH (association, intervention, and counterfactual along with causal discovery) for QA generation. For the higher rungs, we additionally provide reference trajectories under specified scene modifications, enabling action-level verification that complements reasoning-level evaluation. In total, the benchmark contains 7,285 verified causal QA pairs and 1,000 counterfactual trajectories derived from nuScenes. We evaluate 10 driving-specific VLAs and 3 general-purpose VLMs, and report three findings. First, the best model reaches only 70.6% QA accuracy, and 4 of 13 models score below random chance. Second, comparing each driving VLA to the general-purpose VLM that shares its language backbone, the cost of driving fine-tuning ranges from 2 to 34 percentage points on causal QA, with post-training design explaining the spread. Third, causal QA and trajectory accuracy are statistically uncorrelated across models: under counterfactual prompts, predicted trajectories either over-react or collapse onto the observed-scene baseline. Taken together, these results show that neither fluent rationales nor accurate observed-scene trajectories constitute evidence of causal understanding.

---


### 92. [PastForward: Faster On-Device GUI Agents via Computational Experience Reuse](https://arxiv.org/abs/2609.32166)

**<font color=#1a73e8>作者：</font>** Taehwan Park, Changmin Lee, Hayeon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running GUI agents on edge devices can keep sensitive screens and interaction histories local, but the computational cost of inference at every action step makes deployment challenging. Existing GUI agent systems either perform full vision-language model (VLM) inference at each action step or reuse coarse-grained knowledge matched to prior tasks. However, dynamic mobile environments and user tasks make it difficult to fully utilize prior task executions without additional fine-tuning or task-specific offline exploration. To address this challenge, we present PastForward, a system that accelerates GUI agents through validated, fine-grained reuse of computational experience accumulated during ordinary task execution. During decoding, PastForward retrieves prior output sequences as device-adaptive multi-token proposals and verifies them in a single VLM forward pass. Across action steps, it uses prior GUI transitions to begin next-step inference while the device executes the current action, retains the early computation only when the predicted screen matches the observed screen, and carries reusable KV states forward. We evaluate PastForward on AndroidWorld workloads derived from real mobile usage patterns using multiple VLM backbones across server and edge platforms. On device, PastForward achieves action-step latency speedups of 1.63-2.36$\times$ while maintaining task success rates.

---


### 93. [Noisy Test-Time Reinforcement Learning for Code LLMs](https://arxiv.org/abs/2609.32172)

**<font color=#1a73e8>作者：</font>** Xikai Yang, Hieu Trung Nguyen, Dunyuan Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable performance across various code-related tasks. However, unlike carefully curated datasets that are typically high-quality and error-free, real-world user instructions are often vague and error-prone, posing significant challenges to the robustness of code LLMs. Furthermore, robustness-oriented fine-tuning relies on paired clean-noisy samples, which are costly to curate and require sophisticated noisy simulation techniques. To address these challenges, we propose the Noisy Test-time Reinforcement Learning framework (NTRL-Code), which enables robust self-evolution of code LLMs using only unlabeled noisy data during the testing stage. Specifically, NTRL-Code uses conservative self-denoising to obtain a cleaner semantic anchor for target estimation, and employs an abstract-syntax-tree (AST)-based structural aggregation mechanism to estimate a proxy target from multiple candidate programs. The policy is then optimized on the original noisy prompts with a hybrid reward that combines format validity, code similarity, and anti-repetition signals. Extensive experiments on three benchmarks, each incorporating character-level, word-level, and paragraph-level perturbations, demonstrate that NTRL-Code yields robust and consistent improvements, stabilizing the predictions of various base models. Our code is available at this https URL.

---


### 94. [KeyRec: Bounded Visual Memory for Streaming and Long-Video Understanding](https://arxiv.org/abs/2609.32182)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Xuejian Rong, Xiaojuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used to understand long videos and continuous streams. However, dense visual tokens accumulate with video duration, making long-context inference prohibitively expensive. Existing training-free visual-token selection methods reduce this cost by retaining informative tokens, but may lose coherent event evidence and fail to distinguish detailed recent observations from long-range history. We propose \textbf{KeyRec}, a training-free framework for constructing bounded visual memory. During query-agnostic writing, KeyRec preserves fine-grained recent observations in a visual cache and organizes historical evidence into a structured event bank. Candidate events are proposed according to their novelty relative to previously stored events and maintained through an online add--merge--evict update. When a question arrives, a text-only router adaptively allocates a fixed readout budget between recent and event memory, without reprocessing historical frames. KeyRec operates on model-facing visual embeddings and supports both modular encoder--projector VLMs and the encoder- and projector-free NEO-ov architecture. Across four streaming and long-video benchmarks and three VLM backbones, KeyRec achieves the best compressed performance in 13 of 15 settings using only 10\% of the dense decoder-facing visual-token budget. It outperforms the strongest compressed baseline by 2.21--18.37 points on real-time questions, achieves the best compressed result in five of six long-video settings, and performs best in every NEO-ov 2B setting.

---


### 95. [Contamination, Prior, or Evidence? Decomposing and Training Evidence Use in Whole-Slide Vision-Language Models](https://arxiv.org/abs/2609.32185)

**<font color=#1a73e8>作者：</font>** Wenhao Zhang, Zhongliang Zhou, Shiyuan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology vision-language models (VLMs) are conventionally evaluated by accuracy, but accuracy alone does not measure evidence use: it may conflate dataset contamination, prior knowledge, and image evidence. In a motivating study of lymph-node metastasis prediction, we found that most public pathology VLMs showed minimal differences when changing from feeding the models with whole-slide images, an annotated lesion, or no image at all. To better understand the specific features leveraged by these models, this paper presents two contributions aimed at disentangling these factors. First, we present CleanSlide, a TCGA-based VQA benchmark designed to eliminate image- and question-side contamination. It contains 149K audited multiple-choice questions over 9,985 slides, with patient- and tissue-source-disjoint splits. Every question is audited for option shortcuts, stem leakage, cross-split duplication, and blind solvability. Second, we propose Pair-DPO, a preference loss over counterfactual slide pairs from the same question and source. By controlling for shared confounding factors, Pair-DPO cancels out the question-attributable signal and leaves image evidence as the source of preference. Specifically, each pair consists of two real slides with opposite, verified findings, introducing neither editing artifacts nor unverified labels for diffuse or graded features such as invasion, necrosis, and tumor grade. Experiments show that our method gains 15.29% from image evidence on the CleanSlide, compared with 2.81% for the best published model. On the external CPTAC and BCNB cohorts, our method achieves accuracies of 57.6% and 59.0%, outperforming all other evaluated models by 9.7% and 3.4%, respectively. We will release the benchmark and code.

---


### 96. [BMA: Backchain Memory Attacks Create Unauthorized Control Paths in LLM Agents](https://arxiv.org/abs/2609.32186)

**<font color=#1a73e8>作者：</font>** Kaisheng Fan, Yishu Gao, Xunzhu Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent memory enables LLM agents to reuse prior experience, but creates a new security boundary: what an agent may remember is not what it should act on. We expose an unauthorized control path where edited low-trust evidence is consolidated into persistent memory, retrieved on a clean task, and used to drive a protected action. Crucially, the adversary neither writes memory nor alters the task. We introduce Backchain Memory Attack (BMA), a grey-box, LLM-driven inverse-planning attack that reasons backward from the target action to the memory that would trigger it, then to the evidence edit that would form it. BMA has two phases: preparation uses resettable trials to localize the first failed link and build experience; execution uses the frozen experience to rank and commit candidate edits without feedback. We introduce the Pathway-Certified Attack Success Rate (Path-CASR) to separate memory-mediated from coincidental hits: registered memory must form, be retrieved, drive the target behavior, and pass matched-intervention checks. Across four substrates and three decision backbones, BMA achieves 18.8% Macro Path-CASR, compared with 13.4% for the strongest access-matched baseline. Of BMA's behavioral hits, 60.3% pass all registered pathway and intervention checks versus 36.7% for the baseline. Frozen BMA edits retain 78.0% of their certified effect on average across four held-out consolidation policies. Representative memory-side controls leave 11.0% Path-CASR, whereas provenance-bound authorization reduces it to 2.0% while preserving 92.1% legitimate-action success.

---


### 97. [ScopeIF: Improving Scope-Aware Precise Instruction-Following in Large Language Models via Graded Reward Modeling](https://arxiv.org/abs/2609.32189)

**<font color=#1a73e8>作者：</font>** Bosi Wen, Yilin Niu, Xiaoying Ning 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Precise instruction-following is a fundamental ability of large language models (LLMs), requiring their outputs to strictly satisfy objective constraints in input instructions. In complex application scenarios, these constraints often possess diverse scopes that govern specific response segments rather than the entire output. However, existing optimization methods often neglect constraint scope during data construction and rely on binary per-constraint rewards, yielding limited data diversity and sparse supervision for complex constraints. To this end, we propose ScopeIF, a novel training framework for scope-aware precise instruction-following. We first introduce a unified schema that factorizes objective constraints into three decoupled dimensions: Scope, Target, and Range. Grounded in this schema, we construct ScopeInstruct, a large-scale instruction dataset with diverse scope-aware constraints, and combine tool-grounded verification with graded reward modeling to quantify the violation degree of each constraint, providing dense supervision for policy optimization. Extensive experiments demonstrate that ScopeIF consistently outperforms existing methods, particularly on complex scope-aware constraints, while preserving general capabilities. Notably, it enables optimized Qwen3-4B and 8B models to rival or surpass strong frontier models such as Gemini-2.5-Pro and DeepSeek-V3.2, establishing an effective paradigm for advancing scope-aware instruction-following. Our code and data are available at this https URL.

---


### 98. [Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling](https://arxiv.org/abs/2609.32193)

**<font color=#1a73e8>作者：</font>** Hongyi Cai, Yi Herng Ong, Tingshiuan C. Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Action (VLA) models condition actions directly on current visual and language context, without an explicit account of how the scene evolves under candidate actions. World Action Models (WAM) attempt to address this limitation by predicting future states, but existing designs keep prediction and policy learning architecturally separate, connecting them only through the predicted output, whether through pixel space video generation or a latent forecasting module trained independently of the policy. We present Devol-ONE, a Mixture of Transformers architecture that unifies vision language understanding, latent world dynamics prediction, and action generation within a single autoregressive framework. Instead of encoding vision language tokens once and feeding them to the action expert, Devol-ONE runs autoregressive prediction jointly across a vision language stream and a V-JEPA pretrained dynamics stream, attending to the vision language key-value cache at every layer to forecast future latent states under language guidance. The action expert is in turn shaped continuously by semantic reasoning and predicted physical dynamics rather than by a fixed representation computed in advance. Extensive experiments are conducted on LIBERO, LIBERO-PLUS, RoboTwin2.0 along with real-world evaluation on Flexiv single-arm and dual-arm setups. Ablation studies show the effectiveness of dynamic stream prediction and layer-wise unified attention to validate our model architectural coherency.

---


### 99. [The Judge Is Not Its Twin: Post-training makes a model's writing more predictable but barely moves its taste, as a judge, toward predictable writing](https://arxiv.org/abs/2609.32196)

**<font color=#1a73e8>作者：</font>** Arman Nik Khah, Arvin Bahreini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are now routinely graded by other language models. If post-training makes a model's own writing more predictable, it may also teach the same model, acting as a judge, to reward predictable writing, so that progress on creativity would be invisible to automated evaluation. We follow two open model families, OLMo-2 and Zephyr (7B parameters each), through their public training stages and measure every stage twice, as a writer of short stories and as a judge of pairs of stories. As writers, the models drift as feared: each family's fully trained model finds the stories of its base, supervised fine-tuned (SFT) and preference-trained (DPO) stages progressively more familiar, in all ten prompts, and a model from the other family finds the trained stories 7.0 to 9.2 percent (OLMo-2) and 24 to 25 percent (Zephyr) less surprising per token. As judges, they barely move toward predictable writing. Asked which story is better, a question every judge can use to tell a story from its own words in scrambled order, no trained judge's estimated tilt toward the more predictable story grows by as much as one point in the probability of picking it. A post hoc one-sided 95% upper bound on that growth is 2.7 points on an average pair, about the size of the untrained OLMo-2 judge's own tilt. Asked which is more creative, no trained judge's estimate favors the predictable story more than its base's does. Training instead strengthens a preference for longer stories when the question is creativity, and for one answer slot, and it breaks "more creative" as a question: trained judges asked it no longer reliably prefer a story to its scrambled words. A follow-up could not build pairs that differ in predictability but not in quality, because the routes that made this writer's stories less predictable also broke some of them, often enough to fail a quality floor set in advance.

---


### 100. [Generalization and Memorization along the Learning Trajectory of Neural Language Models: A Geometric Account of Categorization](https://arxiv.org/abs/2609.32199)

**<font color=#1a73e8>作者：</font>** Wang Bojun, Holly Jenkins, Elizabeth Wonnacott  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how generalization and memorization develop along the learning trajectory of neural language models. Using controlled synthetic grammars, we examine both the geometry of representation space and model behaviour over training. We find that continuous regions of representation space not occupied by observed tokens become systematically structured from the earliest stages of learning, forming category-level geometric organization that supports generalization to unattested combinations. Generalization therefore emerges from the beginning of learning rather than only after extensive memorization. With prolonged training, larger models increasingly distinguish observed from unobserved grammatical combinations. At the same time, the continuous geometric structure supporting category-level generalization is gradually destructed. Together, these results suggest that neural language models initially learn through categorization-based generalization, followed by a gradual transition toward more exemplar-specific memorization.

---


> [!TIP]
> 当前位于：**51-100**（第 2/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
