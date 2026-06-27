# 🧠 大模型相关研究 | 2026年06月28日

> 本类共 **135** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-135**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-135**

---

### 101. [A Generalization Theory for JEPA-Based World Models](https://arxiv.org/abs/2606.27014)

**<font color=#1a73e8>作者：</font>** Jingyi Cui, Qi Zhang, Hongwei Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint Embedding Predictive Architectures (JEPAs) have recently emerged as a promising paradigm for world modeling by learning predictive dynamics in a latent space rather than generating future observations at the input level. Despite their empirical success, the theoretical understanding of JEPA-based world models remains limited. In this paper, we develop the first generalization theory for JEPA-based world models. We formulate JEPA pretraining as a conditional spectral graph learning problem and show that the JEPA objective is equivalent to a low-rank factorization of an action-conditioned co-occurrence matrix. Building on this characterization, we establish a connection between JEPA pretraining error and downstream planning regret, leading to a finite-sample generalization bound for JEPA-based world models. Our analysis reveals an inherent trade-off between approximation and sample errors with respect to the latent dimension, providing theoretical insights into the advantages and limitations of latent predictive models compared with input-level predictive approaches.

---


### 102. [On-board Remote-Sensing Foundation Models for Unsupervised Change Detection of Disaster Events](https://arxiv.org/abs/2606.27018)

**<font color=#1a73e8>作者：</font>** S. Ramírez-Gallego  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote Sensing Foundation Models (RSFMs) have emerged as a powerful alternative to supervised models for Earth Observation, allowing satellites to autonomously trigger high-resolution captures or adjust tasking parameters upon detecting an anomaly, thereby maximizing the utility of the mission's limited power and computational resources. RSFMs are versatile, unified encoders that optimize onboard storage for multiple orbital applications while ensuring high-fidelity feature extraction. In particular, unsupervised change detection with RSFMs offers a well-informed and transformative path for disaster monitoring without expensive labels. In this paper, we present a novel unsupervised detection method based on ResNet (RSFM) + FPN which identifies a wide spectrum of anomalies by detecting subtle semantic shifts in the latent space between successive orbital passes. By relying on an untrained FPN architecture and its intrinsic priors, the system achieves efficient image-level generation and higher resolution mapping with minimal effort (training-free) compared to previous proposals (patch-based, trained). And by replacing tailored models with RSFMs, we can achieve comparable results through an approach that eliminates the need for bespoke training and extensive development effort and adds customization, while ensuring high-performance generalization across diverse terrains and sensors.

---


### 103. [MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignment](https://arxiv.org/abs/2606.27019)

**<font color=#1a73e8>作者：</font>** Sander Land  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Unigram tokenizer uses an elegant representation which makes it straightforward to edit vocabularies, but its training is comparatively heavy and complex. We introduce MinGram (Minimalist Unigram), which keeps the token-list representation but simplifies training using a BPE-derived seed vocabulary, Hard EM on a minimum-token path, and a single flat score-pruning step. This removes the suffix array, the forward-backward pass, and the iterative prune loop, leaving a procedure that requires little beyond tokenizer inference itself. By making token count the primary objective and using a Unigram score only as a tiebreak, MinGram keeps the compression of pure token-count methods while retaining much of the morphological alignment and downstream quality of probabilistic ones. Across six languages, MinGram compresses better than both BPE and standard Unigram, and a compression-oriented variant matches the strongest token-count compressors while retaining substantially higher morphological alignment. In controlled downstream language-model training, Unigram-family tokenizers, with MinGram among the best, consistently beat BPE in bits-per-byte.

---


### 104. [Just how sure are you? Improving Verbalized Uncertainty Calibration in Medical VQA](https://arxiv.org/abs/2606.27023)

**<font color=#1a73e8>作者：</font>** Eren Senoglu, Federico Toschi, Nicolo Brunello 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) applied to Medical Visual Question Answering (VQA) tend to produce overconfident outputs regardless of actual correctness, and existing verbalized confidence calibration methods, developed primarily for text only LLMs, do not account for the multimodal nature of medical image understanding.
This work proposes a training based framework that finetunes MLLMs to improve their calibration using a composite loss function combining a Brier style calibration term, an anchor regularizer that prevents confidence collapse toward extreme values, a contrastive image text alignment term, and a KL based model stabilization term. The alignment signal is derived from a $2 \times 2$ factorial perturbation design that crosses image presence with text integrity, probing the reliance of the model on visual modality input versus language priors. Finally, a top K KL divergence regularizer is used to protect the answering ability of the model during finetuning.
Across three Medical VQA benchmarks and two architectures (MedGemma 4B IT and Qwen2 VL 7B Instruct), our method reduces calibration error by 60% or more, and improves discrimination by 26% or more, while preserving predictive accuracy. On average across benchmarks, the technique outperforms prompting based, sampling based, and training based approaches, and ablation experiments confirm that each component of the loss function is indeed necessary for improving the calibration. All code for the experiments is publicly available.

---


### 105. [NuclearQAv2: A Structured Benchmark for Evaluating Domain-Science Competence in Large Language Models](https://arxiv.org/abs/2606.27047)

**<font color=#1a73e8>作者：</font>** Henry Shaowu Yuchi, Michal Kucer, Benjamin H. Sims 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong performance across a wide range of tasks, but ensuring their reliability in highly technical domains remains a significant challenge. In nuclear engineering, problem solving often requires not only factual knowledge but also quantitative reasoning and conceptual understanding. To address the need for systematic evaluation in this domain, we introduce NuclearQAv2, a benchmark for assessing LLMs on nuclear engineering knowledge. The benchmark comprises approximately 1,240 question-answer pairs spanning three categories: boolean, numeric, and verbal. NuclearQAv2 is constructed using a hybrid pipeline that combines expert-authored questions, existing datasets, and LLM-assisted generation from domain-specific technical corpora. By leveraging structured prompting for both automated question generation and response evaluation, the proposed framework enables scalable benchmark construction and evaluation. We evaluate a diverse set of LLMs using NuclearQAv2 and observe substantial performance differences across task types. While the models generally perform well on factual questions, quantitative reasoning and conceptual understanding remain considerably more challenging. These results highlight the importance of multi-faceted evaluation frameworks and establish NuclearQAv2 as a scalable benchmark for assessing LLM capabilities in technical domains.

---


### 106. [The Riddle Riddle: Testing Flexible Reasoning in Large Language Models and Humans](https://arxiv.org/abs/2606.27103)

**<font color=#1a73e8>作者：</font>** Bella Fascendini, Kathryn McGregor, Max D. Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans flexibly adapt their reasoning strategies to the requirements of a given problem. Large language models (LLMs) have performed well on many cognitive tasks, however, it is unclear whether this accuracy is a result of pattern matching from training data or flexible reasoning. Here, we introduce a novel paradigm to test this question: the riddle riddle paradigm. Riddle riddles are word problems written to mimic popular riddles, but altered so their answers only require literal interpretations. Identifying correct answers requires looking past the structure of each question and flexibly apply different reasoning strategies based on the content. If LLMs respond to surface features, such as form, a riddle-like structure should cause models to use an inventive reasoning strategy even when a literal interpretation suffices. Alternatively, if LLMs reason based on content, they should flexibly switch strategies when appropriate. Across two experiments with nine state-of-the-art LLMs and 100 human participants, we show humans and LLMs fail on this paradigm in opposite directions. LLMs were far more accurate on genuine riddles than on riddle riddles (84.9% vs. 50.7%); whereas humans showed the reverse effect (50.5% vs. 80.5%). Error analysis shows that 90.8% of LLM errors on riddle riddles (the condition where they show diminished performance) were due to inappropriate use of inventive reasoning while only 57.6% of human errors on genuine riddles were due to overextending literal reasoning. Thus, while both groups make mistakes, reasoning mistakes are made more often by LLMs than by humans. Overall, LLMs' strong performance on genuine riddles may reflect memory retrieval rather than flexible strategy selection, and without stimuli designed to elicit this contrast, it becomes easy to conflate LLM-generated outputs that look like reasoning with genuine reasoning.

---


### 107. [Joint Learning of Experiential Rules and Policies for Large Language Model Agents](https://arxiv.org/abs/2606.27136)

**<font color=#1a73e8>作者：</font>** Shicheng Ye, Chao Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For LLM agents in multi-step interactive environments, a key challenge is to make effective use of accumulated interaction experience. Existing work has typically separated two uses of such experience: keeping it outside the model as natural-language rules for later prompting, or using trajectories and feedback to update the model parameters. The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. We present Joint Learning of Experiential Rules and Policies for LLM Agents (JERP), which updates a long-term experiential-rule pool and the policy from the same interaction trajectories. At decision time, JERP retrieves task-relevant rules and conditions the agent on them together with the interaction history. After each episode, it uses the collected trajectories both to optimize the policy and to revise the rule pool by comparing current rollouts with reference successful trajectories. This coupling keeps the rule pool aligned with the evolving policy while allowing stable and effective behaviors to be gradually absorbed into the model itself. Experiments on AlfWorld and WebShop show that JERP yields consistent gains in decision performance for complex interactive tasks.

---


### 108. [OpenRCA 2.0: From Outcome Labels to Causal Process Supervision](https://arxiv.org/abs/2606.27154)

**<font color=#1a73e8>作者：</font>** Aoyang Fang, Yifan Yang, Jin'ao Shang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) poses a holistic test of LLM agentic capabilities, such as long-context understanding, multi-step reasoning, and tool use. However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. The mechanism is forward verification: reasoning from cause to effect rather than inferring backward from symptoms. Applying PAVE yields OpenRCA 2.0 (500 instances), the first cross-system RCA benchmark with step-wise causal annotations for LLM agents. Across 11 frontier LLMs, recovering the exact root-cause set succeeds in only 20.7% of cases on average. To locate where this difficulty lies, we relax the criterion and find what we call the ungrounded diagnosis: agents identify at least one correct root-cause service in 76.0% of cases, but ground that service in a verified causal propagation path to the observed symptom in only 61.5%. Outcome-only evaluation hides this failure mode; step-wise causal ground truth is the missing piece for trustworthy LLM-based RCA agents.

---


### 109. [TOPS: First-Principles Visual Token Pruning via Constructing Token Optimal Preservation Sets for Efficient MLLM Inference](https://arxiv.org/abs/2606.27161)

**<font color=#1a73e8>作者：</font>** Tinghao Wang, Yichen Guo, Rui Huang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved strong multimodal reasoning capabilities, but their efficiency is limited by the large number of visual tokens, which introduces substantial computational overhead. Visual token pruning offers a natural solution, yet existing methods are imperfect: attention-based criteria tend to retain redundant tokens, while diversity-based criteria are often agnostic to user instructions. Even methods that combine multiple criteria still lack a principled formulation of the intrinsic objective of token pruning. In this paper, we revisit visual token pruning from a first-principles perspective and formulate it as constructing Token Optimal Preservation Sets. Through a top-down information-theoretic analysis, we identify three fundamental principles for effective token selection: Task Relevance, Information Coverage, and Semantic Diversity. Based on these principles, we propose TOPS, a training-free and model-agnostic pruning module that can be applied to various MLLMs. Extensive experiments on 7 MLLM backbones and 14 benchmarks demonstrate that TOPS outperforms prior methods under diverse pruning settings. Notably, on LLaVA-NeXT, TOPS removes 77.8% of visual tokens while preserving 100.0% and 100.6% performance on its 7B and 13B models, respectively, suggesting that pruning redundant visual tokens can sometimes mitigate hallucination and inspire future lightweight MLLM design.

---


### 110. [Automating Potential-based Reward Shaping with Vision Language Model Guidance](https://arxiv.org/abs/2606.27180)

**<font color=#1a73e8>作者：</font>** Henrik Müller, Daniel Kudenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse rewards are inherently challenging for reinforcement learning agents as they lack intermediate feedback to guide exploration and to correctly attribute the sparse success rewards to relevant parts of the trajectory. Naive reward shaping can induce reward hacking, yielding policies that exploit auxiliary signals instead of solving the intended task. Potential-based reward shaping (PBRS) guarantees preservation of the optimal policy set, but requires the definition of a heuristic potential function over the state space. In this work, we introduce the VLM-guided PBRS framework VLM-PBRS that learns the potential function directly from vision language model (VLM) feedback. We query a lightweight VLM to obtain preferences over image pairs and train a model of the potential function using these preferences. As this approach is based on potential-based reward shaping, it preserves the original optimal policies, and removes the need for expert-designed reward shaping terms. Because large VLMs are prohibitively expensive to invoke repeatedly during policy learning, we employ smaller, more computationally efficient VLMs. Although the resulting preference labels are less accurate, empirical evidence shows that the preference labels can still be used to accelerate learning. We validate our method empirically in the Meta-World and Franka Kitchen environments and highlight the connection between VLM preference label accuracy and sample efficiency improvements. Our contributions are threefold: (1) the first application of VLM preference-based learning to synthesize a potential function for PBRS, (2) a principled, low-cost solution that leverages small VLMs, and (3) extensive empirical demonstration of improved sample efficiency and robustness to reward hacking.

---


### 111. [HarmVideoBench: Benchmarking Harmful Video Understanding in Large Multimodal Models](https://arxiv.org/abs/2606.27187)

**<font color=#1a73e8>作者：</font>** Jiajun Wu, Haoyu Kang, Yining Sun 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have recently shown immense potential in automated content moderation, sparking growing interest in developing harmful-video benchmarks. However, we identify two primary limitations in existing works: 1) The multi-layered characteristics of harmful videos are overlooked. Existing benchmarks predominantly formulate evaluation as a binary classification task, failing to capture implicit or deep contextual harms. 2) Explanatory rationales are completely absent. Current frameworks measure exclusively whether a model flags a video correctly rather than explaining why, turning evaluation into a black box where models can succeed through superficial shortcuts. To address these problems, we present HarmVideoBench, a multi-layered diagnostic benchmark comprising 1,379 videos paired with 4,137 multiple-choice questions. HarmVideoBench benchmarks three hierarchical dimensions: Observable Evidence, Clip-Internal Meaning, and Beyond-Clip Reasoning, aiming to evaluate models' deep understanding beyond surface cues with carefully balanced and curated samples. We evaluate 19 leading models on HarmVideoBench to assess their multidimensional understanding of harmful videos. Moreover, we introduce BCR, a benchmark-aligned method that predicts reasoning boundaries and dynamically retrieves context only when needed. Experimental results show that BCR substantially improves the base model's performance in harmful video understanding, raising the macro average from 61.7 percent to a state-of-the-art 84.4 percent.

---


### 112. [A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO](https://arxiv.org/abs/2606.27188)

**<font color=#1a73e8>作者：</font>** Fabiana Fournier, Lior Limonad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the process harness, a new mechanism for uplifting legacy workflows into Agentic Business Process Management (Agentic BPM) without replacing the underlying workflow engine. A process harness places a policy-governed agentic layer around a deterministic workflow engine, intercepting designated control points to contribute reasoning, adaptation, and oversight while the engine retains structural authority over the process. To define the process harness rigorously, we develop the Task-Decision-Flow (TDF) model, specifying both its data schema and its execution semantics. TDF decomposes LLM reasoning across three policy-governed agent types: a TaskAgent for knowledge-intensive task execution, a DecisionAgent for per-case gateway routing, and a FlowAgent that governs runtime flow adaptation through a principled hook mechanism. Each agent reasons within an explicit policy drawn from the process FRAME, the aggregate policy set governing all LLM calls in the system. We then present CUGA FLO as the design and implementation realization of the TDF model, and demonstrate it on a loan approval workflow that exercises all three agent types and hook-driven regulatory override. The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it.

---


### 113. [Forecasting With LLMs: Improved Generalization Through Feature Steering](https://arxiv.org/abs/2606.27199)

**<font color=#1a73e8>作者：</font>** Humzah Merchant, Bradford Levy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Successful forecasting involves identifying patterns between historical and future states of the world which generalize to future observations. We apply LLMs to a variety of forecasting tasks and inspect their internal states using sparse autoencoders to understand whether they appear to rely on time-specific pieces of knowledge versus generalizable patterns. Our analyses identify features associated with both time-aware reasoning and look-ahead-biased reasoning. We then apply the LLMs to an entirely different domain and intervene on these features. We find that amplifying time-awareness features substantially reduces look-ahead bias on forecasting prompts while preserving general reasoning performance. In contrast, steering the candidate look-ahead-bias features does not produce an effect. These results suggest that interpretable temporal features can be used to causally shift LLMs toward more historically grounded reasoning.

---


### 114. [Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes](https://arxiv.org/abs/2606.27210)

**<font color=#1a73e8>作者：</font>** Jeremias Ferrao, Niclas Müller-Hof, Iustin Sîrbu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We argue that safety classifiers should model user intent as an explicit signal between the prompt and the final label. To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. Despite its size, AIMS enables competitive safety classifiers across training regimes: DPO from model-generated intent errors improves over SFT, and intent-conditioned distillation outperforms reasoning-only distillation in most teacher-student pairs. Most notably, directly rewarding intent faithfulness with GRPO yields the strongest average performance across five external safety benchmarks, while our intent-aware models form the inference latency-F1 Pareto frontier. These results show that faithful intent modeling is a compact, high-quality supervision signal for more robust safety classifiers.

---


### 115. [Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation and Self-Improvement](https://arxiv.org/abs/2606.27226)

**<font color=#1a73e8>作者：</font>** Sangwoo Cho, Kushal Chawla, Pengshan Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM outputs remains a major bottleneck in NLP: human evaluation is expensive and slow, lexical metrics correlate poorly with human judgments on open-ended generation, and holistic LLM judges often produce opaque scores that are hard to debug. We propose BINEVAL, a framework that decomposes evaluation criteria into atomic binary questions and aggregates the resulting verdicts into interpretable, multi-dimensional scores. Given a task prompt, a meta-prompt generates fine-grained evaluation questions, and an LLM answers them independently for each output, yielding transparent question-level feedback together with calibrated overall scores. This decomposition makes evaluation easier to inspect, easier to diagnose, and directly usable for prompt improvement. Across SummEval, Topical-Chat, and QAGS, BINEVAL matches or outperforms strong baselines including UniEval and G-Eval, with especially strong results on factual consistency benchmarks such as QAGS. Beyond competitive correlation with human judgments, BINEVAL better matches human score distributions and avoids the ceiling effects common in prior LLM judges, leading to better discrimination between borderline and clearly flawed outputs. We further show that the same question-level feedback supports iterative prompt optimization, improving evaluator prompts on summarization and generation prompts on IFBench under both self-update and cross-model update settings. Overall, BINEVAL provides a task-agnostic, training-free, and interpretable evaluation framework that combines strong empirical performance with practical diagnostic and optimization value.

---


### 116. [RSPC: A Benchmark for Modeling Stress and Psychiatric Conditions in Digitally Mediated Relationships using Psychiatrist Annotations](https://arxiv.org/abs/2606.27247)

**<font color=#1a73e8>作者：</font>** Parmitha Vangapandu, Sai Ganesh Mokkapati, Sathwik Narkedimilli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In NLP, mental health conditions are often modeled as isolated phenomena, without interpersonal context. We use Reddit posts about long-distance relationships to capture both mental health distress and associated relational triggers. We introduce the Relational Stress and Psychiatry Corpus (RSPC) containing 1,799 Reddit posts annotated by psychiatrists for diagnostic categories, including the most prevalent mood disorders (anxiety and depression), relational stressor triggers, and indications of relationship phase. We benchmark seven fine-tuned transformer models and five large language models across multi-label disorder classification, relational trigger detection, and temporal phase prediction tasks. We find clear task-dependent differences between model families, with Claude-3-Haiku achieving the best disorder classification performance (Macro-F1 = 0.538) and GPT-4o obtaining the strongest relational trigger detection performance (Macro-F1 = 0.519), suggesting distinct model capabilities. We further find strong associations between anxiety disorders and chronic relational uncertainty. Overall, RSPC establishes a benchmark for NLP tasks that consider relational context and supports a shift from individual-centric to context-aware mental health modeling that captures the social and temporal dynamics of distress.

---


### 117. [CORTEX: A Structured Reasoning Benchmark for Trustworthy 3D Chest CT MLLMs](https://arxiv.org/abs/2606.27264)

**<font color=#1a73e8>作者：</font>** Hashmat Shadab Malik, Anees Ur Rehman Hashmi, Numan Saeed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning in multimodal large language models (MLLMs) has shown strong promise in medical imaging. However, this reasoning is usually free-form text judged only by its final answer, making it hard to interpret and verify, especially in 3D radiology, where a diagnosis should be traceable to evidence in the scan. Existing chest CT question-answering datasets compound this by reducing expert radiology reports to answer-only pairs, dropping the reasoning that links findings to conclusions and omitting the patient history clinicians rely on. As a result, reasoning-capable 3D chest CT MLLMs remain out of reach, as neither the structured supervision needed to train them nor the protocol needed to verify their reasoning yet exists. We introduce CORTEX (Clinically Organized Reasoning and sTructured EXplanation), a structured reasoning benchmark for 3D chest CT. For each question, CORTEX restores the missing reasoning as a four-stage diagnostic trace mirroring a radiologist's workflow: task understanding, visual observation, diagnostic reasoning, and answer synthesis. We generate these traces using frontier large language models with broad medical and general-domain knowledge, then filter and verify them with a stage-level evaluation protocol combining automated rubric scoring with expert radiologist review. Crucially, both the reasoning structure and evaluation rubrics are designed in close collaboration with clinicians. Built on CT-RATE, a large, publicly available chest CT dataset without reasoning annotations, CORTEX comprises 76,177 validated reasoning traces across open-ended VQA, closed-ended VQA, and report generation, providing both the structured supervision and the stage-level evaluation protocol needed to build and evaluate trustworthy reasoning models for 3D chest CT. Our dataset and evaluation code will be made publicly available upon acceptance.

---


### 118. [How Surprising Is Historical Italian to Language Models? Tokenization Tax, Comprehension Tax, and a Simple Mitigation](https://arxiv.org/abs/2606.27275)

**<font color=#1a73e8>作者：</font>** Maria Levchenko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly critical to digital library workflows, yet their ability to process historical language remains poorly understood. Historical difficulty is typically treated as a monolithic barrier, conflating orthographic variation, linguistic distance, and pretraining exposure. In this paper, we propose a diagnostic framework that decomposes this difficulty into four distinct dimensions: tokenization cost, predictive uncertainty (surprisal), semantic robustness, and context sensitivity.
We evaluate this framework on three datasets spanning three centuries: (1) a newly curated corpus of 17th-century Italian texts (1610-1689) digitized from original page images; (2) canonical 19th-century Italian "I Promessi Sposi" serving as a high-exposure control; and (3) 18th-century Russian civil print books as a contrastive orthographic stress test.
Our results reveal a distinct dissociation between encoding cost and comprehension. While Russian and early modern Italian incur comparable tokenization penalties (25-30% inflation), their predictive difficulty diverges sharply. 17th-century Italian is on average 2.4 times more surprising than its modern equivalent - with academic prose reaching 3.2 times - whereas Russian shows only a modest increase. But predictive uncertainty does not imply representational degradation: embedding similarity remains robust (> 0.85) across all datasets, confirming that models can represent historical meaning even when generation is unstable.
Finally, we demonstrate that a minimal temporal context prompt reduces historical surprisal by approximately 60%, offering a simple, model-agnostic mitigation. These findings suggest that while historical text imposes a consistent encoding tax, digital libraries can safely deploy LLMs for semantic retrieval tasks, provided that generative applications are carefully adapted.

---


### 119. [EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting](https://arxiv.org/abs/2606.27277)

**<font color=#1a73e8>作者：</font>** Junwei Luo, Shuai Yuan, Zhenya Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially observed, weather-driven world modeling problem, in which weather acts as a conditioning signal, while forecasting remains uncertain due to sparse observations and unobserved land-surface states. However, existing methods do not fully capture this setting: deterministic models collapse uncertainty into a single future prediction, while diffusion-based methods typically treat weather variables as undifferentiated conditioning signals, and existing benchmarks focus mainly on reconstruction accuracy rather than whether forecasts respond correctly to changed weather this http URL introduce EO-WM, a video diffusion transformer for multispectral EO forecasting. EO-WM incorporates a physically informed conditioning framework that represents meteorological forcing through a climatological baseline, weather anomalies, and cumulative physical stress signals. Specifically, it separates baseline and anomaly through distinct conditioning pathways, and accumulates anomalous forcing over time to capture sustained heat and drought stress. To evaluate weather-response behavior beyond standard metrics, we introduce two diagnostic benchmarks: an Extreme Summer Benchmark for severity-aware prediction of vegetation degradation under extreme weather, and a Seasonal Matched-Pair Benchmark for testing response fidelity under changed weather forcing. Experiments show that EO-WM reduces the error in predicted Normalized Difference Vegetation Index (NDVI) decline amplitude by a relative 5.63% and improves directional hit rate by a relative 7.80%, while remaining competitive on standard pixel-level metrics. The benchmarks and model will be made open-source at this https URL.

---


### 120. [Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings](https://arxiv.org/abs/2606.27287)

**<font color=#1a73e8>作者：</font>** Preet Baxi, Jiannan Xu, Jane Yi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injection in automated résumé screening, defined as subtle self-promotional text that introduces no new qualifications but is designed to influence LLM evaluations. Using controlled experiments, we show that prompt injection reliably improves applicant rankings when résumé quality is homogeneous and few candidates inject. However, its effectiveness rapidly diminishes as more candidates inject, collapsing when manipulation becomes widespread. When candidate quality is heterogeneous, prompt injection is less effective on average, but can occasionally allow lower-quality candidates to outrank higher-quality ones, raising fairness concerns. Overall, LLM-based screening is most vulnerable when manipulation is rare and candidate quality differences are small. Code and resources are publicly available at: this https URL

---


### 121. [When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models](https://arxiv.org/abs/2606.27288)

**<font color=#1a73e8>作者：</font>** Josef Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-model LLM systems such as routing, voting, cascades, fusion, and mixture-of-agents are used to beat single-model accuracy. We show that their gain is capped by a quantity the field rarely reports. For any policy whose output is one member model answer, accuracy cannot exceed one minus beta, where beta is the rate at which every model is wrong on the same query. In contrast, the usual diagnostic, average pairwise error correlation rho, cannot identify beta: error laws with identical marginals and pairwise correlations can have different all-wrong rates. A Clopper-Pearson bound on beta gives a finite-sample certificate on the largest gain any router, vote, or cascade could deliver before training a router.
Across 67 models from 21 providers, a tetrachoric-calibrated single-factor model still underprices the all-wrong tail: on open-ended mathematics, observed beta is 0.052 versus 0.023 under the full 67-model Gaussian copula, about 2.5 times underpricing, with 90 percent CI 1.7 to 3.4 and k equals 17. The effect recurs on execution-graded code, where beta is 0.079. Re-asking the same GPQA-Diamond questions in free-response rather than multiple-choice form reopens the tail, with beta 0.127 and a five-judge panel with kappa 0.73 to 0.92, locating co-failure in answer format rather than subject. At matched quality, low-rho heterogeneous ensembles beat high-rho Self-MoA, but on checkable tasks in our pool, combining models rarely beats the single best model without a strong query-level routing signal. Gains come from models failing on different questions, not from adding more models.

---


### 122. [Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN](https://arxiv.org/abs/2606.27305)

**<font color=#1a73e8>作者：</font>** Archer Moore, Mingming Gong, Liam Hodgkinson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) for 3D generation is now established across a number of works, but most existing pipelines optimise explicit surface representations, often by converting radiance fields into meshes and training heavily on surface-supervised data. We instead fine-tune a pretrained 3D-aware generative model directly from a learned reward over radiance-field density ($\sigma$) values, with no externally supplied mesh or shape prior. The reward model requires no pretraining, trains easily on a small set of preference samples, and yields robust improvement in 3D geometry. Working on an unconditional 3D-aware face GAN (EG3D), our reward reads the continuous 3D density field of the neural radiance field (NeRF) directly and supplies a geometry-only learning signal, requiring neither text conditioning, mesh extraction, nor multi-view rendering. A density-consistency constraint keeps the 2D appearance qualitatively similar while the geometry is reshaped, at a measurable but bounded distributional cost (FID-50k rises from 4.09 to 6.66): the fine-tuned generator, trained from the preferences of a single annotator as a proof of concept, produces face geometries preferred by users in 74.4% of pairwise comparisons.

---


### 123. [ViQ: Text-Aligned Visual Quantized Representations at Any Resolution](https://arxiv.org/abs/2606.27313)

**<font color=#1a73e8>作者：</font>** Xumin Yu, Zuyan Liu, Zhenyu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A unified representation for text and vision is a natural pursuit, as it enables simpler multimodal modeling and more efficient training. However, representing images as discrete signals in the same way as text inevitably introduces severe information loss. Existing work struggles to balance low-level details and high-level semantics in discrete representations: reconstruction-oriented representations often lack semantic information, whereas semantically stronger features typically suffer from severe loss of detail. We present ViQ, a Visual Quantized Representations framework, which is designed to balance semantics and details in discrete representations while supporting inputs at native resolutions, thereby enabling it to serve as a unified and general discrete representation for arbitrary visual inputs. Our approach structures quantization learning into two stages: text-aligned pre-training and feature discretization. With text-aligned pre-training, we enhance the visual encoder semantic-rich supervision from the pretrained language model and enable it to process native-resolution visual inputs. During discretization, we propose a proximal representation learning strategy to progressively compact the feature space, along with a position-aware head-wise quantization mechanism that enables flexible processing of arbitrary resolutions. Extensive experiments on multimodal tasks demonstrate that ViQ achieves competitive performance compared to state-of-the-art multimodal vision encoders with continuous and high-dimensional visual features, while maintaining high precision in low-level reconstruction. We also show that multimodal training with visual quantized representations largely improves efficiency, yielding up to 20\%-70\% acceleration with different base LLMs and training recipes.

---


### 124. [Beyond Surface Forms: A Comprehensive, Mechanism-Oriented Taxonomy of Indirect Linguistic Encoding for LLM-Based Coded Language Detection](https://arxiv.org/abs/2606.27314)

**<font color=#1a73e8>作者：</font>** Hamid Reza Firoozfar, Mohammadsadegh Abolhasani, Reza Mousavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To avoid moderation and surveillance on social media, some users routinely invent indirect linguistic expressions (ILE) that camouflage sensitive meanings. Such expressions surface as algospeak, euphemisms, and adversarial obfuscation, depending on intent and context, and they involve recurring encoding mechanisms. We propose a comprehensive, mechanism-oriented taxonomy of ILE that abstracts away from communicative goals and instead categorizes the underlying operations through which meaning is encoded and recovered. We evaluate the taxonomy by incorporating it into LLM prompts and comparing it with four existing taxonomies and a no-taxonomy baseline, using 2,000 manually annotated TikTok and Bluesky posts. The proposed taxonomy attains the strongest document- and span-level performance across the three LLMs, achieving an improvement of 4.7% in accuracy and 5.4% in F1 over the best-performing benchmark. The empirical results reveal the importance of a comprehensive, mechanism-oriented taxonomy as a stable scaffold for detecting emerging coded language and a useful input to content moderation. Disclaimer: This paper contains content that may be profane, vulgar, or offensive.

---


### 125. [LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank](https://arxiv.org/abs/2606.27316)

**<font color=#1a73e8>作者：</font>** Serhii Hamotskyi, Akash Kumar Gautam, Christian Hänig  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifying the eligibility of securities as collateral is a key responsibility of the German Central Bank. However, manually verifying these assets against legal and financial criteria within lengthy, semi-structured, and often bilingual prospectuses is a resource-intensive task. While previous efforts utilized traditional Named Entity Recognition (NER) for information extraction, these methods can struggle with OCR noise, linguistic variance, and rigid span-based constraints, and the need for manually annotated training data for each relevant annotation type. In this paper, we present the first case study applying Large Language Models (LLMs) to the eligibility examination process, shifting the paradigm toward a generative Information Extraction pipeline. Our approach decomposes the task into extraction, normalization, and interpretation, allowing for greater flexibility in handling noisy text and interleaved German-English content. We further introduce a value-based evaluation methodology using LLM-as-a-judge, which offers a more semantic assessment than location-based metrics. Our results demonstrate that LLM-based systems achieve high precision (up to 91%) in document-level eligibility, exhibiting a conservative operating profile that minimizes false acceptance.

---


### 126. [OctoSense: Self-Supervised Learning for Multimodal Robot Perception](https://arxiv.org/abs/2606.27317)

**<font color=#1a73e8>作者：</font>** Anthony Bisulco, Jeremy Wang, Kostas Daniilidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present OctoSense, an open-source sensor platform with stereo RGB and event cameras, LiDAR, a thermal camera, an inertial measurement unit, RTK-corrected global positioning system, and proprioception (CAN bus data from a car, and joint angles for a quadruped robot). The eponymous OctoSense dataset contains 59 hours of time-synchronized driving data across different types of environments at different times of the day, including situations with highly degraded sensors. We demonstrate multi-modal self-supervised learning using such real-world robotics data, where sensors have different representations, frequencies, latencies and noise. Our approach, a "late-fusion" masked autoencoder, (i) uses modality-specific tokenizers to account for different spatiotemporal characteristics of these sensors, and (ii) caches modality-specific tokens at inference time to process new measurements as they come. This architecture (i) is fast (6.68 ms and 112 ms on NVIDIA 5090 and Orin NX respectively, to compute the representation), (ii) performs better than existing image-only foundation models on tasks such as estimation of optical flow, depth, semantic segmentation, and ego-motion (translation, rotation, and steering angle), and (iii) predicts robustly at nighttime or in situations where sensory data is degraded. See our project page for links to the dataset, code, and supplementary videos: this https URL.

---


### 127. [Not All Actions Are Equal: Rethinking Conditioning for Dexterous World Model](https://arxiv.org/abs/2606.27325)

**<font color=#1a73e8>作者：</font>** Zizhao Yuan, Zhengtu Liang, Taowen Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in action-conditioned world models show promising progress in modeling complex interactions and forecasting future states under diverse action sequences. While these models are often driven by stronger visual representations and model capacity, action conditioning itself remains underexplored. Most existing approaches compress the entire action sequence into a single representation, which works well for low-DoF control but becomes less reliable in high-DoF scenarios. We observe that high-DoF dexterous actions are inherently heterogeneous, spanning multiple orders of magnitude, where large-scale motions coexist with subtle but important signals. When uniformly aggregated, optimization exhibits an imbalance across action components, which hinders the modeling of fine-grained effects and affects action fidelity. We therefore propose DexAC-WM, which treats action conditioning as a structured process rather than global compression. DexAC preserves dimension-level semantics via action tokenization and aligns action signals with visual dynamics through local refinement and global modulation. To address the limited high-level semantic grounding in existing world models, we further introduce a semantic branch that provides rich object-scene priors, which enables world model to capture dynamic visual details while supporting high-DoF action-conditioned video prediction. Experiments on EgoDex and EgoVerse show that combining the semantic branch with DexAC significantly improves FID, FVD, and PCK, demonstrating gains in visual-temporal realism and action-following consistency. We further verify that DexAC extends to other backbones, showing the scalability of our structured action-conditioning design. These results suggest that scaling world models to high-DoF control requires both structured action modeling and semantic grounding.

---


### 128. [Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326)

**<font color=#1a73e8>作者：</font>** Nicklas Hansen, Xiaolong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. We hypothesize that hallucination concentrates in low-coverage regions of the state-action space, where lightweight data-centric signals can both detect it and guide mitigation. To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. We identify three distinct hallucination modes: perceptual, action-marginalized, and scene-diverging -- each anchored to a different stage of the pipeline, and develop three signals that accurately predict where the model will fail. To close coverage gaps at training time, we develop a coverage-aware sampling technique; to close them online, our hallucination predictors serve as curiosity rewards for targeted data collection, yielding a data-efficient finetuning recipe that adapts the pretrained world model to entirely unseen environments with as few as 50 real environment trajectories. Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation.
An interactive web version of our paper is available at this https URL

---


### 129. [Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://arxiv.org/abs/2606.27330)

**<font color=#1a73e8>作者：</font>** Tianyi Men, Zhuoran Jin, Pengfei Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal web agents can assist humans in operating repetitive GUI tasks, where effective task planning is essential for decomposing complex tasks into executable actions. While small open source MLLMs are cost efficient and privacy preserving compared with commercial large models, they suffer from weak planning and limited cross website generalization. To address these limitations, we introduce the planning experience exploration and utilization (PEEU) method, which autonomously explores environments to discover experiences and utilizes hindsight experience to synthesize strictly aligned, high level training data. To quantitatively analyze the generalization behaviors driving this performance, we propose the task decomposition hierarchical analysis framework (TDHAF) to systematically study compositional generalization across three task granularities: low, middle and high levels. Our analysis reveals that mastering low level atomic skills does not guarantee high level planning competence, while high level task training yields stronger OOD generalization. Experiments on real world benchmarks demonstrate PEEU's superior effectiveness: our 7B model achieves 30.6% accuracy, outperforming the much larger Qwen2.5-VL-32B model. These demonstrate constructing hindsight high level tasks and leveraging experiences is crucial for OOD planning abilities of small MLLMs.

---


### 130. [Language-Based Digital Twins for Elderly Cognitive Assistance](https://arxiv.org/abs/2606.27334)

**<font color=#1a73e8>作者：</font>** Mohammad Mehdi Hosseini, Mohammad H. Mahoor, Hiroko H. Dodge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital twins have emerged as a promising paradigm for personalized healthcare, enabling modeling of individual behavior and health trajectories. In cognitive health, early detection of Mild Cognitive Impairment (MCI) remains challenging, where language and conversational patterns serve as non-invasive biomarkers. In this work, we propose a language-based digital twin framework that leverages large language models (LLMs) to mimic the conversational behavior of elderly individuals by incorporating stylometric cues and contextual metadata. To evaluate fidelity and cognitive consistency, we introduce a multi-head conditional variational autoencoder (cVAE) that jointly measures reconstruction quality and predicts cognitive scores. Experiments on the I-CONECT dataset show that the digital twin preserves identity-specific characteristics and achieves reconstruction and MoCA prediction errors comparable to real data, while outperforming baseline GPT-generated responses. These results highlight the potential of language-based digital twins as a scalable and non-invasive approach for personalized and continuous cognitive health monitoring.

---


### 131. [Mapping Political-Elite Networks in Europe with a Multilingual Joint Entity-Relation Extraction Pipeline](https://arxiv.org/abs/2606.27347)

**<font color=#1a73e8>作者：</font>** Kirill Solovev, Jana Lasser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether political elites organise into rent-seeking coalitions that capture public resources or civic networks that sustain governance is a central question in comparative politics. Yet observing these complex, informal, and adversarial ties at scale has historically required intensive manual coding, while automated text-as-data methods have largely been limited to simple co-occurrence. Recent large language model (LLM) approaches offer a path forward but often rely on proprietary APIs, lack cross-lingual capability, and struggle with scalable entity resolution. We present a modular, fully open-weight pipeline for multilingual joint entity-relation extraction that builds signed, temporal knowledge graphs from massive unstructured news corpora. It combines span-based named-entity recognition (NER) with a three-stage linking cascade mapping mentions to language-independent Wikidata identifiers; a high-throughput, ontology-constrained mixture-of-experts model then uses guided decoding to extract directed, signed relationships grounded in a domain ontology. A full-coverage spot-check against a 3491-relation gold standard shows high textual correctness (68.2% strict to 93.7% lenient). Two large-scale case studies validate the pipeline against the public record. In Austria, it reconstructs a political party's complete lifecycle, dating internal fractures and tracking personnel into successor factions and court convictions. In a Polish corpus, it uncovers the overlapping economic and governance networks of state-enterprise patronage, alongside the structurally balanced, signed conflict network of the polarized Civic Platform (Platforma Obywatelska, PO)--Law and Justice (Prawo i Sprawiedliwość, PiS) duopoly. By bridging raw multilingual text and structured relational data, our framework provides a robust, replicable foundation for cross-national empirical computational social science.

---


### 132. [Autoregressive Boltzmann Generators](https://arxiv.org/abs/2606.27361)

**<font color=#1a73e8>作者：</font>** Danyal Rehman, Charlie B. Tan, Yoshua Bengio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient sampling of molecular systems at thermodynamic equilibrium is a hallmark challenge in statistical physics. This challenge has driven the development of Boltzmann Generators (BGs), which allow rapid generation of uncorrelated equilibrium samples by combining a generative model with exact likelihoods and an importance sampling correction. However, modern BGs predominantly rely on normalizing flows (NFs), which either suffer from limited expressivity due to strict invertibility constraints (discrete time) or computationally expensive likelihoods (continuous time). In this paper, we propose Autoregressive Boltzmann Generators (ArBG) -- a novel autoregressive modelling framework -- that overcomes these limitations by departing from the flow-based BG paradigm. ArBG circumvents the topological constraints of flows and enables sequential inference-time interventions, while offering enhanced scalability by leveraging architectures effective in Large Language Models. We empirically demonstrate that ArBG leads to significant improvements over flow-based models across all benchmarks, but particularly in larger peptide systems such as the 10-residue Chignolin. Furthermore, we introduce Robin, a 132 million parameter transferable model trained with the ArBG framework which improves over the previous state-of-the-art, reducing the zero-shot energy error, E-W$_2$, on 8-residue systems by over 60$\%$. The code can be found at the following link: this https URL.

---


### 133. [Reinforcement Learning without Ground-Truth Solutions can Improve LLMs](https://arxiv.org/abs/2606.27369)

**<font color=#1a73e8>作者：</font>** Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution is unknown. We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. When applying group-relative RL to such continuous rewards, we identify two key challenges: \emph{scale dominance}, where uncalibrated score magnitudes across test instances distort policy updates, and \emph{frequency dominance}, where repeatedly sampled suboptimal solutions can outweigh rare but stronger candidates. RiVER addresses these challenges with calibrated reward shaping that uses instance-wise comparisons and emphasizes top-ranked solvers while retaining bounded feedback for other valid solutions. We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. RiVER advances Qwen3-8B and GLM-Z1-9B-0414 by 8.9\% and 9.4\% in ALE rating rank. More importantly, despite training exclusively on score-based tasks without any ground-truth solutions, RiVER also improves the backbones across exact-solution benchmarks such as LiveCodeBench and USACO by an absolute average improvement of 2.4\% and 3.5\%. By contrast, baselines trained with raw execution scores improve ALE rating but fail to transfer to exact-solution benchmarks. These results suggest that score-based optimization tasks, combined with proper reward calibration, can serve as effective training environments for general coding ability without ground-truth solutions.

---


### 134. [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373)

**<font color=#1a73e8>作者：</font>** Shravan Venkatraman, Ritesh Thawkar, Omkar Thawakar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, self-evolving large multimodal models (LMMs) have received attention for improving visual reasoning in a purely unsupervised setting. However, multi-role self-play and self-consistency reward schemes in existing self-evolving LMMs optimize answer agreement without ensuring the decoder attends to visual content, relying instead on statistical language priors to produce self consistent outputs. This leads to a persistent failure mode we term visual under-conditioning, where the decoder relies on language priors rather than the image during generation, manifesting as insufficient attention to visual tokens. As a result, current self-evolving LMMs struggle on vision--language understanding tasks such as image captioning and visual question answering. To address this, we propose VISE (Visual Invariance Self-Evolution), a purely unsupervised self-evolving framework that directly regularizes the model's visual conditioning policy through two complementary invariance-based rewards: a geometric invariance reward that enforces spatial consistency under known transformations, and a semantic invariance reward that penalizes evidence-agnostic generation by requiring the model to recognize the absence of evidence when predicted regions are perturbed. VISE operates within a single model without specialist roles, external reward models, or annotations, and is trained on raw unlabeled images. Experiments on 18 benchmarks demonstrate the efficacy of our approach. Using Qwen3-VL-2B as the base model, VISE achieves gains of $+16.85$ CIDEr on COCO and $+19.66$ CIDEr on TextCaps, reduces object hallucination by $5.0$ Chair-I points, and generalizes across four model families and scales. Our code and models are available at this https URL

---


### 135. [Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards](https://arxiv.org/abs/2606.27376)

**<font color=#1a73e8>作者：</font>** Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most unified large multimodal models (LMMs) that support both visual understanding and image generation still rely on curated post-training supervision, such as human annotations, preference labels, or external reward models. We ask whether a unified LMM can improve both abilities autonomously using only unlabeled images. We propose a self-evolving training framework with three internal roles: a Proposer that generates visual questions, a Solver that answers and evaluates them, and a Generator that synthesizes images. Training uses only self-derived consistency signals, without human annotations, preference labels, or task-trained external reward/judge models. To stabilize learning, we introduce Solver Token Entropy (STE), a continuous difficulty signal based on token-level prediction uncertainty that remains useful even when sample-level consistency becomes unreliable. For image generation, we design a multi-scale internal evaluation scheme that combines question-answer fidelity scoring with cycle-consistent captioning. This creates a solver-mediated coupling, where better visual understanding enables more reliable generation assessment and stronger internal training signals. The framework preserves the same role decomposition, reward logic, and training schedule across diffusion-based BLIP3o, rectified-flow BAGEL, and autoregressive VARGPT-v1.1 architectures, requiring only each backbone's native prompting and generation interface. Across eight understanding metrics, our method consistently improves over the corresponding base models. On BAGEL, it achieves a $+3.5\%$ absolute gain on MMMU and improves GenEval image generation performance from $82\%$ to $85\%$. Code and models are publicly released.

---


> [!TIP]
> 当前位于：**101-135**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-135**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
