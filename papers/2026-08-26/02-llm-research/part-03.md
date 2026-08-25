# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

---

### 101. [From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers](https://arxiv.org/abs/2608.22063)

**<font color=#1a73e8>作者：</font>** Bartolomeo Bogliolo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents built on Large Language Models (LLMs) increasingly reach enterprise data through the Model Context Protocol (MCP), and many MCP database servers maximize flexibility by exposing a single generic SQL execution tool. This paper proposes the Domain-Oriented Tooling Pattern: instead of generating SQL at query time, the model selects from a small set of domain-aligned tools whose parameterized queries encapsulate schema navigation, joins and business rules on the server side. We formalize the pattern around three architectural invariants and introduce Model Demotion, the observation that replacing SQL synthesis with intent classification lowers the model tier required to serve routine requests. As a reference implementation we present MCP Blueprint, an open-source framework in which domain tools are defined declaratively as YAML metadata plus external parameterized SQL files. We evaluate the pattern with a public reproducibility benchmark comparing three MCP server designs - raw SQL execution, a thin generic tool pack, and a verticalized domain pack - on four local models (3B-8B) across seventeen customer-facing tasks over the Sakila database (609 completed cells; temperature 0; three repetitions per cell). The verticalized pack reaches a pooled mean score of 0.939 versus 0.666 for raw SQL and 0.605 for the generic pack; the smallest model improves from 0.583 to 0.929, matching or exceeding every larger configuration while cutting cost per correct answer by an order of magnitude. All harness code, prompts, gold answers, frozen packs and per-cell results are publicly available.

---


### 102. [Decision-Support and Modeling with Large Language Models for Geothermal Well Arrays](https://arxiv.org/abs/2608.22068)

**<font color=#1a73e8>作者：</font>** Edwin Ouko, Emmanuel Lujan, Alan Edelman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geothermal well arrays, which organize multiple geothermal wells into carefully planned geometric configurations, provide opportunities to enhance energy production capacity and increase fault tolerance. The development and adoption of these emerging geothermal technologies could be accelerated through the recent advances in large language models (LLMs) and high-level high-performance languages. A challenge in LLM-based applications is the reliability of the generated outputs, as they can be prone to subjective biases and hallucinations. This study assesses the potential of cutting-edge LLMs - such as ChatGPT, Gemini, Claude, Grok, and domain-specific models like AskGDR - as expert assistants that can synthesize insightful interpretations of complex geothermal data, as well as improve feature capabilities of geothermal models and numerical software. We developed a novel approach, leveraging Google's recently introduced AI assistant, NotebookLM, to accelerate the generation of unpublished quantitative geothermal benchmarks. The rapid generation of these evaluation instruments is essential for assessing the swiftly evolving capabilities of emerging language model technologies. In particular, we use these benchmarks and LLM-based interviews to analyze opportunities and limitations of two promising technologies: geothermal well arrays and closed-loop coaxial wells. Furthermore, we present a case study illustrating how LLMs can facilitate auto-parallelization of geothermal numerical models. Our analysis emphasizes their application in digital twins and underscores the importance of high-level, high-performance code generation. This line of research could play a transformative role in the geothermal sector by enabling the next-generation of decision-support applications, integrating data analysis, informed recommendations, and more dynamic numerical modeling workflows.

---


### 103. [Real-TurnTurk: A Multimodal Turkish Corpus for Turn-Taking Prediction](https://arxiv.org/abs/2608.22071)

**<font color=#1a73e8>作者：</font>** Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Bekir Berker Türker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turn-taking is a basic organizational feature of human conversation and remains difficult to model in natural, synchronous dialog systems. While existing research has explored multimodal approaches and large language models for turn-ending prediction, there is a lack of naturalistic conversational corpora specifically addressing turn-taking dynamics in Turkish. This study introduces a multimodal Turkish conversational dataset of unscripted dyadic interactions, comprising synchronized front-facing video, per-speaker audio channels that allow overlapping speech to be attributed to individual speakers, and time-aligned transcriptions. Turn-taking prediction is formulated as a binary classification problem, and a Genetic Algorithm (GA) is employed to optimize interpretable decision rules derived from visual, acoustic, and linguistic features. A hybrid AND-OR rule representation is adopted in the proposed framework to represent the alternative cue combinations that precede a turn transition.

---


### 104. [Spine-Branch Coordination for Multi-agent Computer Use](https://arxiv.org/abs/2608.22077)

**<font color=#1a73e8>作者：</font>** Mian Zhang, Manasi Sharma, Sheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs) are increasingly deployed as multi-agent systems that decompose a task into multiple subtasks executed across parallel virtual machines (VMs). However, a critical physical bottleneck is that the state of two VMs cannot be merged. Previous systems handle this ad-hoc rather than treating it as a first-class concern. We propose Spine-Branch Coordination for multi-agent computer use, a framework that decomposes a task into a "spine-branch" graph, where the spine carries the main task flow with continuous VM state and branch tasks execute in parallel to collect information the spine needs to complete the task. Branch VMs are discarded once their tasks finish, so no VM merging ever occurs. Experiments show that on 200 long-horizon tasks from Odysseys and across three CUA backbones, Spine-Branch improves success rate over the baseline system by 6.0% to 16.5%, while reducing per-task cost by 34% to 70%, indicating that explicitly modeling VM-state merging constraint enables multi-agent computer use to scale efficiently.

---


### 105. [Dissecting Neuro-Symbolic Quality Assurance for Synthetic Oncology Data Generation](https://arxiv.org/abs/2608.22085)

**<font color=#1a73e8>作者：</font>** Laxmigayathri Challa, Yuhan Zhou, Ana Cleveland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic clinical data generation with large language models addresses the scarcity that limits cancer staging research, but oncology hallucinations are categorically harmful: one clinically impossible staging assignment contaminates every downstream model trained on it. Neuro-symbolic pipelines validate during generation, yet the contribution of individual quality-assurance components remains unclear. We report three controlled studies isolating gate necessity, constraint attribution, and retrieval conditionality, holding generation protocol, diversity thresholds, and fine-tuning hyperparameters constant across adapter conditions. The symbolic gate enforces schema completeness, ontology coverage against the Systematized Nomenclature of Medicine, and staging-logic consistency under American Joint Committee on Cancer eighth-edition rules. Ungated, 29.9% of records contain schema failures and 20.1% contain clinically invalid staging. Schema validation is the load-bearing filter: within the fully gated corpus it rejects 148 of 512 records, ontology grounding a further 24, and staging-logic validation none---the only generator producing logic violations is already excluded on schema, making clinical-logic validation a generator-conditional safeguard rather than the dominant filter. Retrieval augmentation is strongly model-dependent: it improves gate compliance for one generator by 12.5 percentage points, has no measurable effect for a second, and collapses output in a third. Across gated configurations ontology density is largely unchanged, indicating that symbolic validation improves clinical validity rather than vocabulary richness. Symbolic gating therefore buys corpus validity but no commensurate gain on real lung-cancer notes in this study; retrieval should be evaluated per model, and ontology density should not be reported as a proxy for corpus quality.

---


### 106. [On Predicting Vulnerability Severity Using In-Context Learning: An Industrial Case Study](https://arxiv.org/abs/2608.22089)

**<font color=#1a73e8>作者：</font>** Daniel Rodriguez-Cardenas, David Nader Palacio, Anna Schmedding 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern software systems require earlier and more scalable vulnerability severity assessment to reduce exposure to high-impact security flaws. Security analysts typically assign CVSS scores, but this manual triage does not scale with the growth of disclosed vulnerabilities and often depends on cloud LLM services that raise confidentiality concerns. This paper presents an industrial case study on predicting CVSS v3.1 scores directly from vulnerable C/C++ snippets using in-context learning with locally deployable, open-source LLMs. We compare proprietary data with the Big-Vul dataset, showing sufficiently aligned CVSS distributions to justify Big-Vul as a proxy for industrial data when constructing prompt-based testbeds. We then vary in-context configurations and model parameters, evaluating CodeLlama2-7B, CodeLlama2-13B, Mistral-7B, gpt-oss, and GPT4o-mini using mean squared error (MSE) and feasibility metrics. Our results show that medium-sized open-source code models, particularly CodeLlama2-7B, can approximate the best cloud performance for CVSS regression when guided by lightweight, output-constraining prompts, offering a practical, privacy-preserving building block for severity triage in industrial settings.

---


### 107. [Semantic Reasoning Denoising: Correcting Language Model Reasoning with Semantic Operators](https://arxiv.org/abs/2608.22090)

**<font color=#1a73e8>作者：</font>** Yujiao Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can produce fluent reasoning traces whose local semantic errors propagate to an incorrect conclusion, while unconstrained self-correction may preserve, amplify, or introduce errors. Existing diffusion language models provide iterative refinement, but usually define noise as token masking or replacement rather than as errors in the reasoning process. We present Semantic Reasoning Denoising (SRD), an operatorized Markov denoising method for natural-language reasoning trajectories. SRD represents semantic noise with executable error operators that describe the error type, its location, and the corrupted and repaired propositions. Composing these operators constructs progressively noisier states. During training, the model learns to identify the semantic noise active in the current trajectory and to reconstruct the paired adjacent lower-noise state. During inference, noise-level-aware denoising repeatedly predicts an inverse operator and checks whether it is applicable, so each executed update makes a localized move toward a stable trajectory. Across six in-domain benchmarks spanning mathematics, code, knowledge, and commonsense, SRD improves the strongest same backbone baseline by 3.2 points on average. On seven cross-dataset transfer targets, it remains competitive with Llama-3-8B-Instruct and improves the strongest Qwen3-8B baseline average by 2.9 points. Analyses of noise sources, objectives, and denoising depth further show that structured semantic-noise prediction and iterative operator execution are central to the improvement.

---


### 108. [Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks](https://arxiv.org/abs/2608.22103)

**<font color=#1a73e8>作者：</font>** Amit Roth, Ivan Bercovich, Yonathan Efroni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents grow more capable and autonomous, their tendency to reward hack, satisfying a task's checks while violating its intent, becomes an increasingly important failure mode. Measuring reward hacking is itself challenging, as detection typically relies on human inspection or LLM judges, both of which can be unreliable. The hack-verifiable environments (HVE) methodology addresses this challenge by embedding detectable hacks into tasks, allowing reward hacks to be identified automatically and reliably. In this work, we adapt HVE to Terminal Bench, a leading benchmark of real-world terminal and coding tasks, and introduce Hack-Verifiable Terminal Bench (HVTB). Using HVTB, we measure reward-hacking rates across frontier models and study whether prompts with varying amounts of information on the hack can mitigate this behavior. This lets us test whether prompting can prevent not only known reward-hacking strategies, but also 'unknown unknown' exploits that the prompt does not anticipate. We release all environments and agent traces at this https URL

---


### 109. [Development and Feasibility Evaluation of an Edge AI as Medical Device System for Breast Cancer Multidisciplinary Team Meetings](https://arxiv.org/abs/2608.22108)

**<font color=#1a73e8>作者：</font>** Aarzoo Dhiman, Farzana Haque, Kartikae Grover 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Breast Cancer Multidisciplinary Team (MDT) meetings manage increasingly complex cases under considerable time pressure, and documentation requirements can reduce clinical efficiency and decision quality. Existing AI based MDT workflows rely on cloud-based processing, limiting their use because patient discussions contain identifiable information. We developed a fully on-device AI pipeline using open-source Automatic Speech Recognition (ASR) and Large Language Models (LLMs) that transcribes breast cancer MDT discussions, structures clinical information, and generates treatment recommendations using retrieval-augmented generation (RAG) grounded in National Institute for Health and Care Excellence (NICE) guidance. The pipeline runs on a single NVIDIA Jetson AGX Orin, ensuring that patient audio, transcripts, and outputs remain within institutional infrastructure. Evaluation included two recorded simulated MDT discussions, ten clinically validated synthetic discussions, and 1,270 acoustically augmented recordings. Optimisation of Whisper large-v3 reduced word error rate by 20.7% and 24.4% on the recorded discussions and achieved performance within 0.58% WER and 1.58% word information lost of a commercial clinical ASR benchmark on augmented audio. MedGemma-RAG identified 2.3 times more MDT-concordant interventions than a proprietary cloud comparator (p = 0.020), with no significant difference in overall accuracy. Stakeholders identified automated documentation, treatment recommendation support, and case triage as the most credible near-term applications while highlighting workflow integration, governance, and clinician trust as key implementation challenges. These findings demonstrate the feasibility of privacy-preserving, fully on-device AI for MDT documentation and guideline-informed decision support, providing a foundation for prospective clinical evaluation.

---


### 110. [What actually runs: a measurement study of language model placement and decode speed on the Apple Neural Engine](https://arxiv.org/abs/2608.22110)

**<font color=#1a73e8>作者：</font>** Shahir M A  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask what gets a language model onto the Apple Neural Engine (ANE) and what makes it fast there, and we answer with three measurements. We sweep a 64-shape matrix of LLM primitives that varies how a computation is expressed while holding what it computes fixed, recording per-operation device support. We then train matched models across size and precision, with quantized checkpoints byte-identical in structure to their fp16 counterparts, so every deployment measurement is of a real trained artifact. And we read the ANE's memory-controller byte counters during inference, establishing what actually ran rather than what the compiler intended. We support every headline claim with at least two of these three measurement paths. We find that placement is a property of how a computation is expressed, not of what it computes: a fused RMSNorm is fully ANE-eligible while its arithmetically identical decomposition is CPU-only. Weight encoding gates the accelerator: CoreML assigns a 25.85M-parameter conv-heavy fp16 model entirely to the CPU (our counters confirm zero bytes through the engine), while the same graph in int8 or 2-bit returns to ~83% residency and runs 1.8-2.2x faster, and a smaller 22.29M all-attention fp16 model sits at 98.9%. Decode cost is bytes streamed per token, at a constant ~0.77 fraction of nominal encoding width across fp16, int8 and 2-bit. The smallest and fastest models we measured are ternary, and at matched size the operator mix barely moves either axis: every resident 25M ternary model lands within 10.0-10.8 MB and 0.62-0.64 ms/token. The headline pair is half-attention ternary at 25M (10.5 MB, 0.63 ms) and 50M (16.8 MB, 0.86 ms) - 9.8x and 6.1x smaller, 3.0x and 2.2x faster than the conv-heavy fp16 design this work began with. From these measurements we draw a design procedure: choose the encoding first, then spend the byte budget on parameters.

---


### 111. [RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored](https://arxiv.org/abs/2608.22118)

**<font color=#1a73e8>作者：</font>** Gregory Druck, Ethan Smith  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM responses are based on the internet (via training or RAG), and AI is now used to generate a significant amount of content online (Paredes et al., 2026), creating the potential for a self-reinforcing feedback loop. Prior work has shown that when LLMs are recursively trained on their own output, they experience model collapse (Shumailov et al., 2024): responses become less diverse, and eventually no longer resemble the original training data. In this paper, we show that a similar collapse occurs if LLM-based AI systems retrieve references they authored using a search tool. We call this RAG collapse. We conduct extensive experiments with three types of simulations of AI systems retrieving references they generated, using three model families, and 1,019 information-seeking prompts, totaling 1,528 simulations and over one million LLM API calls, and find that 79.6% (1,216/1,528) of simulations end in collapse. Surprisingly, even a single self-authored reference can trigger collapse because the LLM disproportionately cites its own content. This self-bias persists even after controlling for reference quality.

---


### 112. [LLM assisted writing deserves empirical evaluation](https://arxiv.org/abs/2608.22124)

**<font color=#1a73e8>作者：</font>** Xuan Zhong Feng, Yi Lin, Yiye Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-assisted writing is often treated as a detection problem, as it raises questions about clarity, integrity, equity, and evaluation. An analysis of 69,209 Health Informatics papers links it to more focused presentation, broader citation practices, and more globally distributed authorship. These patterns do not prove better science, but they support evaluating manuscripts by scholarly quality and accountability rather than by tool use.

---


### 113. [Decoupled Physical Modeling and Execution for Physics Reasoning](https://arxiv.org/abs/2608.22126)

**<font color=#1a73e8>作者：</font>** Ye Zhang, Xuehang Guo, Rui Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics reasoning requires constructing a consistent model of the underlying physical system rather than relying solely on symbolic or formula-based manipulation. Although large language models have shown strong ability in solving math and coding problems, they still struggle with physics problems, as these problems entangle the physical modeling process with mathematical calculations. Humans approach physics by first building a representation of the system before performing calculations. Inspired by this, we introduce a unified framework that distills intermediate representations that explicitly encode the physical modeling process and adopt a two-stage post-training strategy, where supervised fine-tuning establishes structured modeling, and reinforcement learning with rubric-based feedback improves the quality of the modeling process. Experiments on multiple multimodal physics benchmarks show that our approach leads to consistent improvements in reasoning performance across different models and datasets. On PhysReason, PhyX and SeePhys benchmarks, physical modeling output performs GRPO by an average ~3%, showing that explicit physical modeling is an efficient strategy of improving physics reasoning for small LLMs.

---


### 114. [Who Should Teach? Confidence-Aware Dual-Teacher Learning for Few-Shot Node Classification on Text-Attributed Graphs](https://arxiv.org/abs/2608.22127)

**<font color=#1a73e8>作者：</font>** Hojin Kim, Sujin Yoon, Sungsu Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-Attributed Graphs (TAGs) integrate graph structures and node-associated textual attributes, and recent studies have increasingly leveraged Large Language Models (LLMs) to improve TAG learning in few-shot settings. However, existing approaches typically utilize LLM-derived information uniformly across all nodes, despite substantial variations in its reliability, while also incurring considerable monetary costs. We argue that the most appropriate source of supervision may differ across nodes, as Graph Neural Networks (GNNs) and LLMs exhibit complementary strengths in exploiting structural and semantic information, respectively. To this end, we propose CoTeach, a Confidence-aware dual-teacher learning framework that dynamically selects the more reliable teacher for each node. Experimental results demonstrate that CoTeach consistently improves few-shot node classification performance while reducing unnecessary LLM utilization and associated monetary costs.

---


### 115. [Task-Driven 3D Printability Assistance via Geometry- and Knowledge-Grounded LLM Reasoning](https://arxiv.org/abs/2608.22128)

**<font color=#1a73e8>作者：</font>** Zhaoda Du, Qiaojie Zheng, Xiaoli Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Printability assessment in additive manufacturing is typically conducted at the geometry level before printing to determine whether a computer-aided design (CAD) model or stereolithography (STL) file can be successfully fabricated. Task suitability, in contrast, is usually evaluated after printing to determine whether the fabricated part satisfies the requirements of its intended use. As a result, for non-expert users to print functional parts, unsuitable material or process choices may only be identified after fabrication, leading to repeated printing, material waste, and user frustration. To address this challenge, this paper leverages the reasoning and language-understanding capabilities of large language models (LLMs), while grounding the reasoning with geometry evidence and structured material/printer knowledge to generate reliable pre-print recommendations. Given a stereolithography (STL) model and a natural-language task description, the framework generates a structured recommendation covering printability, material choice, process parameters, design guidance, risks, and explanations. We evaluate the framework on focused STL benchmark scenarios with novice-style task descriptions. The proposed method achieves 75.0% printability over 96 physical validation trials, with 88.9% task suitability among successfully printed samples. It also improves Gemini 2.5 Flash-Lite material-selection accuracy from 37.5% under pure LLM to 90.0%. Expert evaluation further shows improved report quality, while post-print feedback improves recommendations on selected problematic cases. These results suggest that user task intent, geometry evidence, and structured material knowledge are all important for reliable task-driven printability assistance.

---


### 116. [PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems](https://arxiv.org/abs/2608.22130)

**<font color=#1a73e8>作者：</font>** Yaokun Liu, Yifan Liu, Daniel Yue Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) solve complex tasks through communication among role-specialized agents. However, inter-agent dependencies introduce reliability risks beyond isolated agent failures. For instance, errors in intermediate messages could be inherited and amplified by downstream agents. Existing uncertainty quantification (UQ) methods mainly target isolated responses or single-agent reasoning, and therefore fail to capture uncertainty propagation in MAS. To this end, we propose PropUQ-MAS, an error propagation-aware UQ framework that represents MAS execution as a communication-structured graph and estimates each step's reliability by combining local uncertainty with uncertainty inherited from upstream messages. Extensive experiments demonstrate that PropUQ-MAS consistently improves UQ in MAS, with average relative gains of +6.10% in AUROC and +47.58% in PRR.

---


### 117. [MegaMem: A Retrieval Solution for Ultra-Large Context Windows](https://arxiv.org/abs/2608.22137)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Bowen Zhu, Hasibul Haque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern language models and agents increasingly require persistent memory for complete codebases, long interaction histories, and heterogeneous enterprise records. The key challenge is to keep hundreds of millions of tokens searchable while passing only bounded source evidence to the answer model. We introduce MegaMem, a source-resolved dual-view retrieval system that separates semantic access from generation evidence. Distilled records and detailed evidence are searched with original and transformed queries; every distilled hit resolves to an immutable source ID before reciprocal-rank fusion, deduplication, and cross-encoder reranking; and only the highest-ranked detailed evidence within a fixed budget supports generation. Post-answer attribution then identifies which loaded sources support the fixed answer. We evaluate MegaMem on EnterpriseRAG-Bench, which contains more than 500,000 heterogeneous enterprise documents and approximately 650M tokens. MegaMem improves Overall from 68.22 to 82.26 and reaches 86.50 Correctness. These results show that MegaMem supports ultra-large persistent memory while preserving strong answer accuracy under a bounded generation context. By separating searchable memory scale from answer-context size, MegaMem provides a practical path toward accurate retrieval over memories ranging from hundreds of millions to one billion tokens. Our code is available at this https URL xfab-xinyuansong/MegaMem.git.

---


### 118. [Measuring Stability and Failure Behavior in Language Models Under Structured Perturbations](https://arxiv.org/abs/2608.22138)

**<font color=#1a73e8>作者：</font>** Samira Golsefid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are usually judged by a single accuracy score, which does not reveal how their performance degrades as inputs are perturbed. We present a graded, multi-family, failure-aware framework for stress-testing reasoning models. It perturbs each problem along a multi-level severity ladder across seven families: six that preserve the answer, paraphrase, input noise, formatting, irrelevant context, context load, and conflicting instructions, and a Knowledge Boundary family that removes answerability so that refusal becomes the correct response. Every test is validity-gated and labeled by its measured severity, and each model is summarized by per-level Accuracy, a magnitude-weighted Stability, and a per-family Collapse Point defined relative to the model's own baseline. Instantiated on the same 100 seed problems used by GSM-Symbolic, expanded into 4,473 gated tests and run on four models spanning capability tiers, the framework exposes structure that an aggregate score hides: the level at which a model fails is family-specific rather than global, and two stressors expose consistent weaknesses across all models: conflicting instructions and questions built on an impossible premise. Recognition of unanswerability is otherwise uneven, reliable on missing information and fabricated evidence but weak on impossible premises. These failure points are invisible to standard accuracy reporting.

---


### 119. [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion](https://arxiv.org/abs/2608.22140)

**<font color=#1a73e8>作者：</font>** Jiaqian Zhu, Yang Zhang, Junhua Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong reasoning performance, but their robustness to realistic lexical corruption remains poorly understood. We evaluate four open-weight instruction-tuned models and frontier models across four reasoning benchmarks under keyboard noise, character swaps, and filler insertion. Character-level perturbations substantially degrade accuracy, especially on multi-step reasoning tasks, while filler insertion has little effect. We trace this asymmetry to Attention Diversion: lexical corruption fragments subword tokenization, and the resulting fragments attract disproportionate attention mass, concentrated in middle and final transformer layers. Length-matched controls confirm that fragmentation, not prompt length, drives the loss. A factorial intervention then shows why the damage is hard to undo: fragmentation corrupts token content and attention allocation together, and the two are coupled. Restoring clean attention while the content remains corrupted is actively harmful, restoring content alone is insufficient, and only restoring both recovers a substantial share of the gap. This coupling explains why inference-time strategies, including chain-of-thought prompting, spell-checking, self-repair, and stronger repair models, fail to consistently recover performance: each addresses one channel at a time. Code and data are available at this https URL

---


### 120. [Evaluation of Small Vision-Language Models on Qualitative Mechanical Problems](https://arxiv.org/abs/2608.22143)

**<font color=#1a73e8>作者：</font>** Henry Fordjour Ansah, Shreya Banerjee, Pranish Ghimire  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Qualitative mechanical problem-solving (QMPS) refers to solving qualitative problems from the mechanical domain. Qualitative problems can be solved with minimal discipline-specific information, without any robust quantitative calculation, generally by using qualitative reasoning and commonsense knowledge. QMPS is a vital aspect of human intelligence that allows us to tackle a wide range of tasks, from simple everyday ones such as turning on a tap to complex tasks in highly demanding and well-paying jobs in various fields, e.g., emergency medicine, plumbing, driving, etc. Employers often use the Bennett Mechanical Comprehension Test (BMCT) to evaluate job candidates' ability to solve such problems. In this work, we assess two state-of-the-art multimodal models, Gemma-3 and Qwen-VL, on their ability to interpret mechanical problem images by eliciting a step-by-step chain of thought (CoT) and a final answer. Each image inherently encodes ground-truth qualitative facts, such as contact points in gears, support relations, and relative weights, which we use to evaluate each model's spatial and commonsense reasoning capabilities. We assess each chain for coherence, completeness, and logical progression to assess each model's thought process, and final answers are compared to verified solutions to measure accuracy.

---


### 121. [The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate](https://arxiv.org/abs/2608.22152)

**<font color=#1a73e8>作者：</font>** Weixiang Sun, Zehong Wang, Hong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built from large language models are deployed widely, yet how much performance is lost when two LLMs must coordinate rather than act alone remains unclear. We formulate the collaboration tax as the team-decentralisation loss of a two-player cooperative game with private information, with two propositions characterising its sign and its equivalence to a max-superadditivity violation. We operationalise this definition on 32 solo-tractable tasks grouped by source of grounding friction and measure it on 11 models from 7 providers. The tax is structured along two no-exception axes: a category ordering across every model and a monotonic decrease with capability. The proximate mechanism is not a reasoning deficit but a four-stage conversational cascade in which agents make ungrounded claims, fail to query the partner, skip integrating both views, and accept the answer without re-derivation. The tax is mechanically predictable from conversation features and partly tractable: a prompt intervention targeting all four stages closes a substantial fraction of the gap, with the dominant bottleneck differing across categories. In heterogeneous pairs the tax is pulled toward the stronger partner rather than the additive midpoint, empirically realising the max-superadditivity violation predicted by our framework. Together these results recast collaboration in LLM systems as a measurable, predictable, and partly tractable cost.

---


### 122. [AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems](https://arxiv.org/abs/2608.22160)

**<font color=#1a73e8>作者：</font>** Zhixu Du, Yiran Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read logs whose origin they cannot verify and name a single culprit, misrepresenting outcomes that are overdetermined, preempted, or caused by an omission. We present \audita{}, an audit layer pairing a tamper-evident record of every inter-agent command with a certified, graded causal-attribution engine. We prove its verdict cannot be gamed: a rule-following agent can never be made to look guilty, an attempt to shift blame is itself caught and graded, and we establish the exact limit of what an evidence-based auditor can certify. On live language-model pipelines it reduces the standard judge baseline's responsibility error roughly threefold; on a benchmark of accident-grounded structures it recovers responsibility where single-culprit baselines fail, and stays invariant under forgery. \audita{} turns the question of who is to blame from an argument about logs into a calculation over evidence.

---


### 123. [MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning](https://arxiv.org/abs/2608.22167)

**<font color=#1a73e8>作者：</font>** Ziyang Luo, Yan Yang, Xiangru Jian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become an effective way to improve the tool-use ability of large language models (LLMs), but most existing RL frameworks stop at the policy update. For every new domain, the user is left with two hard systems problems: standing up an isolated environment for each of hundreds of concurrent trajectories and connecting it to training, and scheduling the rollout so that the GPU stays busy across long, multi-turn episodes that spend much of their time stalled on slow tool calls. We present MCP-Universe RL (MCP-U RL), an open-source framework that takes over both. It uses the Model Context Protocol (MCP) as the interface to the environment, so any tool already exposed as an MCP server plugs into training with no RL-specific integration code. It builds the two missing layers once and reuses them across domains: an environment-orchestration layer that provisions, isolates, and recycles the MCP environments over a pluggable container backend, and a rollout-orchestration layer whose staged pipeline overlaps trajectories to keep the GPU busy while episodes wait on tools. A backend-agnostic training layer then applies the update through an existing RL backend, with veRL and slime integrations. With one configuration, changing only the task specification, we train software-engineering, deep-research, and general tool-use agents on gpt-oss-20b and improve task reward in all three.

---


### 124. [Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction](https://arxiv.org/abs/2608.22176)

**<font color=#1a73e8>作者：</font>** Jun Hou, Yi Fang, Xuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly applied to clinical prediction tasks such as in-hospital mortality and readmission from electronic health records (EHRs). Privacy and compliance constraints motivate systems that can be deployed locally, which has increased interest in open-weight multi-agent designs. However, most medical multi-agent systems are evaluated as a single block, leaving unclear which agent role contributes to prediction and whether retrieval drives observed gains. We study a role-specialized Mixture-of-Agents (MoA) that combines medical knowledge retrieval with contrastive similar-patient reasoning. By varying the role design while holding the retrieval setup fixed, we localize the main effect to the final integrator. Pairing large open-weight analysts with a small open-weight integrator matches closed-model prompting on F1 for mortality prediction while flagging substantially more true high-risk patients. Mechanism analysis shows the role assignment directly yields a high-recall operating point without threshold tuning. The effect is task-dependent, with smaller gains for readmission because the available records correlate weakly with this longer-horizon outcome. These results position role design as a key factor in privacy-constrained, training-free clinical LLM prediction.

---


### 125. [Unveiling the Depth-Performance Dilemma in Split-Federated Fine-tuning of LLMs](https://arxiv.org/abs/2608.22188)

**<font color=#1a73e8>作者：</font>** Hariharan Ramesh, Someshwaran Murugaiyan, Jyotikrishna Dass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Federated Fine-tuning (SFF) is a promising paradigm for scaling Large Language Models (LLMs) by partitioning model depth between resource-constrained clients and a centralized server. While system incentives for throughput and privacy favor deep partitions, the impact of such configurations on model utility remains poorly understood. In this work, we identify and characterize the Depth-Performance Dilemma: the regime that maximizes system efficiency is precisely where fine-tuning quality collapses. Through a comprehensive audit across four model scales (GPT-2 to Llama-3-8B) and diverse benchmarks, we demonstrate that deeper partitions provide monotonic gains in throughput and privacy at the cost of catastrophic performance plateaus. We evaluate a suite of state-of-the-art federated adapter aggregation methods including AVG, STACK, SVD, and FREEZE, revealing that while these techniques are effective in standard Federated Learning, they fail to mitigate the artifacts unique to split architectures. Finally, we provide a mechanistic diagnosis for this failure, tracing the collapse to the near-isometric topology of Transformers, which allows aggregation noise to propagate without attenuation until it triggers Attention Collapse in the server partition. Our findings challenge the prevailing assumption that partition depth is a utility-neutral tuning knob and provide a structural foundation for stable distributed LLM fine-tuning.

---


### 126. [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](https://arxiv.org/abs/2608.22191)

**<font color=#1a73e8>作者：</font>** Kang Chen, Junjie Nian, Yixin Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software-engineering agents solve repository-level tasks through long, stochastic tool-use trajectories, and repeated attempts often find fixes missed by one run. Test-time scaling is difficult because patches lack canonical answer forms, while sibling actions from a shared prefix are correlated. We study whether native MoE router traces can guide steering and selection without an external judge or selection-time test execution. Our analysis shows that routing provides a robust behavioral role signal; token-granular readouts and decision-matched comparison sets turn it into effective control. We therefore introduce Risa (Routing-Informed Steering and Arbitration): within trajectories, routing encourages diverse exploration and controlled convergence during patch commitment; across separately sampled trajectories, agreement at informative patch positions selects a final candidate. We evaluate on SWE-bench Verified using open-weight sparse MoE agents across scales and reasoning-effort settings. Risa's routing arbitration raises the macro-average resolved rate from 44.9% under uniform sampling to 48.2% on the gpt-oss family, matching text consensus without answer-string matching, and it transfers to Qwen3.6, where it improves on uniform choice and matches text consensus on the full 500-task benchmark.

---


### 127. [How Agents Represent Humans: Human-Directed Stereotypes in an Open Agent Social Network](https://arxiv.org/abs/2608.22192)

**<font color=#1a73e8>作者：</font>** Huangchen Xu, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed in persistent social environments, where generated claims can be posted, replied to, remembered, and reused. We study human-directed stereotypes on Moltbook, an open agent-native social platform, asking how agents construct humans as a social category. For this human-target analysis, we introduce an annotation framework with four evaluative dimensions---morality, friendliness, competence, and autonomy---and a second-stage subtype scheme for descriptive \textit{other} attributions. We find that competence dominates human-directed evaluations, while many \textit{other} attributions describe humans as epistemic, cultural, or embodied subjects. We further examine how these human representations appear in human--agent narrative contexts and platform-level circulation. As an auxiliary comparison, we analyze agent-internal community feedback through behavioral host affinity. Rather than reproducing the stable insider--outsider rejection often observed in human online communities, Moltbook feedback patterns are better explained by exposure, author visibility, and content selection. These findings suggest that bias in agent societies should be studied not only as isolated model output, but also as a discourse process.

---


### 128. [Lessons from the Hardware Hacking Competitions: Verification Techniques, Findings, and Insights](https://arxiv.org/abs/2608.22202)

**<font color=#1a73e8>作者：</font>** Sudipta Paria, Aritra Dasgupta, Raghul Saravanan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware hacking competitions have emerged as practical platforms for evaluating security weaknesses in complex System-on-Chip (SoC) designs while promoting security-aware verification and tool development. This paper presents a systematic study of SoC security verification through open-box hardware hacking competitions, focusing on practical vulnerability analysis strategies, observed findings, and lessons for security-aware verification. We present a multi-strategy vulnerability analysis methodology, combining simulation-based verification, formal verification, lint analysis, Large Language Model (LLM)-assisted bug detection, and coverage-guided hybrid fuzzing. Representative vulnerability findings are analyzed to illustrate how different techniques expose complementary classes of security flaws, and we derive practical lessons for pre-silicon security verification. Finally, we discuss how competition benchmarks can support the reproducible evaluation of emerging hardware security techniques and guide future security-aware EDA research.

---


### 129. [AdaptPrint: Response-Adaptive Fingerprinting of Black-Box LLM Services](https://arxiv.org/abs/2608.22213)

**<font color=#1a73e8>作者：</font>** Yilin Li, Yifei Zhang, Guozhu Meng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box LLM services have emerged as a practical deployment paradigm. Nevertheless, their opacity also hinders the systematic assessment of security risks and complicates copyright auditing for model owners. Black-box LLM fingerprinting, which identifies the underlying LLM identity through query-response interactions, offers a promising way to bridge this gap. Existing approaches typically collect responses from target LLM services using a fixed set of queries and perform poorly in the presence of realistic and complex configurations (e.g., system prompt and sampling settings). To overcome these limitations, we propose AdaptPrint, a response-adaptive fingerprinting method for revealing hidden LLM identities in black-box LLM services. AdaptPrint integrates three progressive response consistency probing strategies: Direct Probing, Continuation Probing, and Follow-up Probing. AdaptPrint determines the final LLM identity by performing similarity matching among candidate LLMs. Experimental results show that AdaptPrint significantly outperforms state-of-the-art methods among 27 candidate models, achieving Top-1, Top-3, and Top-5 accuracies of 80.6%, 90.3%, and 92.1%. AdaptPrint also demonstrates strong robustness across different defense strategies and decoding parameters.

---


### 130. [Query-Driven Multimodal Information Extraction from Long Documents](https://arxiv.org/abs/2608.22214)

**<font color=#1a73e8>作者：</font>** Yikai Gao, Ding Xia, Xi Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In domain-specific multimodal long documents, images and text jointly convey complex knowledge that cannot be fully captured by plain text alone. However, existing paradigms like DocVQA primarily focus on generating textual answers or localizing evidence regions, rather than outputting query-specific textual attribute values and corresponding images. To address this gap, we propose query-driven image-text joint extraction from long documents, requiring models to output query-requested textual attribute values and corresponding image bounding boxes. Based on challenges related to both user intent and document content, we designed a two-level taxonomy that operates at the query and instance levels. Further, we construct ITJoint, the first high-quality, manually annotated benchmark for this new task, comprising 2,455 pages of domain-specific documents with numerous non-decorative images, 316 queries, and 910 answer instances. Finally, we evaluate representative standalone Vision-Language Models from different providers and further design Q2IT, a multi-agent collaborative framework consisting of three progressively collaborating agents for evidence collection, page selection, and target-image localization. Using a joint evaluation approach that assesses both text extraction and image localization, our experiments show that standalone VLMs struggle with this task, while Q2IT significantly improves performance on ITJoint, although a substantial gap remains toward perfect results.

---


### 131. [Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation](https://arxiv.org/abs/2608.22215)

**<font color=#1a73e8>作者：</font>** Wenzhi Li, Dong Nie, Rui Lan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves. Existing memory systems typically treat external memory as a monotonically growing repository, inevitably leading to retrieval degradation and increasing computational costs over time. We argue that the core challenge is not retrieval alone, but managing the knowledge lifecycle: deciding what to externalize, update, or ultimately internalize. Inspired by Complementary Learning Systems (CLS) theory in neuroscience, we propose Dual-Layer Agentic Memory, a framework that shifts memory management to the write phase through cost-aware epistemic routing and periodic parametric consolidation. Incoming information is categorized as non-write, write-new, or write-update, and routed through a small-to-large model cascade that minimizes routing overhead while filtering redundant memories. A subsequent write-back phase selectively consolidates high-value external memories into model parameters via supervised fine-tuning. Experiments demonstrate the dual efficiency of our approach: a 1.7B/8B cascade prunes up to 68% of redundant external memory while escalating fewer than 50% of inputs, yet retains over 98% of the downstream QA Exact Match (EM) achieved by an exhaustive retention baseline. We further show that periodic consolidation successfully internalizes external knowledge, allowing the router to adaptively suppress redundant writes as the model's epistemic boundaries evolve. Overall, our framework presents a unified paradigm for agent memory: selective externalization followed by selective internalization. Code and dataset will be released upon acceptance.

---


### 132. [UR$^{2}$-MLLM: Uncertainty-aware Revisit Reasoning in Multimodal Large Language Models for Radiology Report Generation](https://arxiv.org/abs/2608.22217)

**<font color=#1a73e8>作者：</font>** Yucheng Chen, Yang Yu, Jiazhou Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiologists generate diagnostic reports through iterative and selective revisiting of suspicious regions to refine their interpretations. Recent multimodal large language models (MLLMs) for radiology report generation (RRG) have shifted from text-only reasoning toward a ``Thinking-with-Images'' paradigm, incorporating visual evidence into the reasoning process. However, existing methods provide static visual evidence without a dynamic revisit mechanism during reasoning, neglecting how radiologists re-examine uncertain observations. To this end, we propose an Uncertainty-aware Revisit Reasoning MLLM (UR$^{2}$-MLLM) framework that dynamically revisits uncertain regions during reasoning for RRG. UR$^{2}$-MLLM is first equipped with uncertainty perception by training on an uncertainty-aware dataset. We then construct a multimodal reasoning trajectory dataset together with a detect-and-copy mechanism, which guides when and where to revisit. Finally, a visual grounding reward refines this behavior through reinforcement learning, aligning the revisited regions with corresponding anatomical structures. Experiments on MIMIC-CXR and IU-Xray show that UR$^{2}$-MLLM achieves state-of-the-art performance, highlighting the value of uncertainty-aware visual revisit reasoning for reliable and clinically aligned report generation.

---


### 133. [Grounded Normative Rule Generation with Structured Search](https://arxiv.org/abs/2608.22229)

**<font color=#1a73e8>作者：</font>** Fanqi Kong, Huaxiao Yin, Ruijie Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Normative rules like institutional charters and workplace policies must be both human-readable and operationally verifiable against actual environment records. However, current language generation and structured-output benchmarks primarily reward surface fluency or schema compliance, leaving operational grounding weakly tested. This creates a critical vulnerability where standard language models generate plausible-sounding policies that fail during enforcement because they rely on unavailable data logs or misaligned scopes. To address this challenge, we formalize the problem as Grounded Normative Rule Synthesis (GNRS) and introduce GNRS-Search, a framework that utilizes Markov Chain Monte Carlo (MCMC) sampling to optimize a discrete, five-slot And-Or Graph (AOG). By explicitly decoupling intermediate operational structure from final prose generation, this method isolates executable feasibility from writing style and allows rule failures to be localized prior to surface realization. We evaluate our approach on GNRS-Bench, a benchmark spanning 116 controlled goals across eight scene families, and RealCharter-Bench, which evaluates transfer to 53 real-derived policy tasks with hidden source clauses. GNRS-Search raises average rubric quality from 68.8% to 81.0% and ranks first under a disclosed executable composite metric, while systematic slot interventions confirm that performance gains stem from robust operational logic rather than rhetorical tuning. Ultimately, by transforming automated rule drafting into an inspectable search problem, this work provides a foundational paradigm for deploying verifiable and compliance-ready personal agents within regulated environments.

---


### 134. [Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation](https://arxiv.org/abs/2608.22230)

**<font color=#1a73e8>作者：</font>** Junyu Lu, Kaiyuan Liu, Jingyi Kang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We introduce a rejudge protocol that extends direct contradiction with decision-boundary perturbations and adversarial rationales. Experiments with multiple LLMs on two hate speech datasets show that annotator-style rebuttals substantially degrade moderation performance, with stronger effects in multi-turn settings. The results further reveal stable, model-specific asymmetries between whitewashing and smearing across attack configurations, indicating distinct directional vulnerability patterns. Explicit reasoning prompts and defensive instructions reduce these effects but do not eliminate them. These findings highlight the need for direction-aware safeguards and dedicated feedback-robustness evaluation in human--AI moderation workflows.

---


### 135. [Beyond What Meets the Eye: Unveiling Situational Illusions for Multimodal Large Language Models](https://arxiv.org/abs/2608.22232)

**<font color=#1a73e8>作者：</font>** Zhiming Yang, Zhuoxi Xiong, Donglin Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world situation appearances can deviate from their underlying physical states, challenging the reliability of multimodal large language models (MLLMs) in practical applications. In this paper, we term this phenomenon situational illusions and investigate: (1) how MLLMs perform under such illusions, and (2) how to mitigate the limitations. We first develop a comprehensive where-what-how taxonomy that characterizes where situational illusions occur, what targets they take, and how they arise. Building on this taxonomy, we introduce MSIBench, a benchmark designed to assess the discrimination, understanding, and reasoning capabilities of MLLMs under situational illusions. Evaluations of 27 model configurations reveal that current MLLMs are highly vulnerable to these illusions and exhibit 6 typical failure modes related to visual observation, grounding, and reasoning. To mitigate the limitations, we build on the core idea of systematically inspecting and reasoning over visual evidence for contextual understanding, developing prompting for closed-source models and supervised fine-tuning for open-source models, respectively. These two simple yet effective methods improve model performances by 20% at most, suggesting a practical path toward more reliable multimodal perception and reasoning in complex real-world environments.

---


### 136. [Read Less, Solve More: Token-Efficient Sparse Reading for AI Agents](https://arxiv.org/abs/2608.22237)

**<font color=#1a73e8>作者：</font>** Zedong Liu, Jiaan Wu, Xinyang Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents increasingly rely on repeated access to external artifacts, yet current reading interfaces often expose entire objects even when only sparse evidence is needed. This over-reading increases token and latency costs and can dilute task-relevant evidence, while existing context-reduction methods mainly intervene after broad content has already entered the trajectory. We present SparseRead, a training-free, model-transparent reading layer that controls content admission before unnecessary evidence reaches the model context. SparseRead combines a regime-aware Read Gate, extensible Reader Backends, and a stateful protocol for bounded, source-anchored evidence acquisition with explicit refinement, verification, stopping, and fallback. Across six frontier models, including Claude Opus 5, and five workload scenarios, SparseRead reduces token volume by up to 92.9% and wall time by up to 89.0%, while preserving or improving task quality. Its consistent gains across three agent frameworks further demonstrate broad portability.

---


### 137. [Improving Few-Step Language Flows with Untied Self-Conditioning](https://arxiv.org/abs/2608.22244)

**<font color=#1a73e8>作者：</font>** Bocheng Li, Linli Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Flow-matching language models refine all token positions in parallel and can trade sampling steps for latency, yet generation quality still degrades sharply with few sampling steps. We trace a source of this degradation to a train--inference mismatch in previous-prediction self-conditioning: during training, the self-conditioning input is computed from the current noisy state with no intervening solver step; during sampling, the solver folds the previous prediction into the latent before that same prediction reappears as the explicit self-conditioning input. This coupling, absent during training, creates redundancy that grows with step width. We show that the mismatch degrades both the self-conditioning input and the solver update, and derive a correction for each from the model's own structure. From the frozen projection weights we identify directions along which the self-conditioning input is redundant with the latent and dampen them; from the solver's integration structure we derive that a step-average prediction is needed and approximate it from prediction history, with scale set by offline trajectory statistics. The resulting sampler, Untied Self-Conditioning, requires no retraining and uses one evaluation per step. At 8 sampling steps on LangFlow, it reduces OpenWebText generative perplexity from $531$ to~$62$ ($8.6\times$); under an adapted Arena-Hard-Auto~v2 protocol, its outputs are preferred in $96\%$ of pairwise comparisons. On ELF-B it reduces generative perplexity from $71$ to~$43$. Improvements hold from 8 to 256 sampling steps.

---


### 138. [Nürnberg NLP @ GermEval Shared Task 2026: Harmful Content Detection in German Social Media through Error-Independent LLM Voters](https://arxiv.org/abs/2608.22246)

**<font color=#1a73e8>作者：</font>** Philipp Steigerwald, Eric Rudolph, Jens Albrecht  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harmful content in German social media does real-world damage, from calls to action to criminal defamation. The GermEval 2026 shared task scores its detection in four subtasks. The technical challenge is a severe class imbalance. The harmful classes are rare and share surface language with the dominant majority class, yet under macro-F1 they decide the score. The decisive lever is then not a stronger single model but error independence. This insight becomes a per-subtask nine-voter ensemble spanning three orthogonal axes: LLM, training method and class scope. Selected mainly on internal cross-validation, the system reaches macro-F1 of 89.56 (C2A), 71.63 (DBO), 54.84 (VIO) and 83.02 (DEF) on the hidden test set, placing first on all four subtasks.

---


### 139. [CAIA in Practice: Field Evaluation of an AI-Assisted Support System for Text-Based Online Counselling](https://arxiv.org/abs/2608.22251)

**<font color=#1a73e8>作者：</font>** Philipp Steigerwald, Nico Bienlein, Jennifer Burghardt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Rising global demand for mental health support creates significant service delivery challenges, with asynchronous email counselling serving as a crucial low-threshold channel for accessing care. This paper presents CAIA, a co-designed AI-based tool suite that demonstrates responsible AI integration into counselling practice through seven LLM-driven functions enhanced by retrieval-augmented generation. A field evaluation involved 34 professional counsellors conducting authentic sessions with trained student counsellees (36 threads, 321 messages, 1,257 AI outputs). User behaviour analysis confirms substantial adoption, revealing that professional autonomy and information accuracy are decisive for sustained acceptance, with counsellors particularly valuing interpretive functionalities that provide new perspectives and stimulate professional reflection.

---


### 140. [Toward a First-Principles Update Geometry for the Language-Model Head](https://arxiv.org/abs/2608.22253)

**<font color=#1a73e8>作者：</font>** Aditya Somasundaram  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the language-model head and softmax as a single module, deriving an update geometry from their composition rather than from the weight matrix in isolation. Under Hilbert's projective distance, the maximum change caused by an update $S$ over $\left|\left|{h}\right|\right|_2\le H$ is $H\max_{i<j}\left|\left|{s_i-s_j}\right|\right|_2$, which is $H$ times the Euclidean diameter of its token rows. Motivated by Muon's singular-value conditioning, we propose maximizing the smallest row separation while constraining this diameter, producing an approximate-equidistance problem when $V\gg d$.

---


### 141. [Training-Free VLM Personalization via Calibrated Residual Decoding](https://arxiv.org/abs/2608.22263)

**<font color=#1a73e8>作者：</font>** Jiaao Yu, Yujian Ma, Xianming Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can be personalized in a training-free manner by directly providing user profiles, preferences, or visual references at inference time, without updating model parameters. However, direct personalized prompting does not guarantee that the model will reliably exploit such evidence. The predictive distribution under the positive user profile often mixes two sources: personalized signals genuinely supported by the current profile, and the model's generic visual or linguistic priors. As a result, from the positive-profile response alone, it is difficult to determine whether a high-confidence answer is supported by the user profile or merely reflects the model's default preference. To address this problem, we propose a training-free calibrated residual decoding framework. Given the same image and question, we construct three evidence conditions: a positive profile , a counterfactual profile , and an empty profile . Our method keeps the prediction under
as the anchored base, and explicitly estimates the marginal contribution of personalization from score differences across the three conditions. We further introduce normalized-entropy-based uncertainty calibration, allowing the strength of personalized enhancement to adapt to the reliability of the residual signal. Experiments on MMPB, YoLLaVA, and MyVLM show that the proposed method improves personalized multimodal understanding without fine-tuning, with consistent gains on identity-sensitive visual personalization tasks. Additional analysis shows that entropy calibration stabilizes residual decoding when the contrastive personalization signal is uncertain.

---


### 142. [Clarify User Expertise: Towards Proactive Conversational Agents Tailoring Responses to User Proficiency](https://arxiv.org/abs/2608.22266)

**<font color=#1a73e8>作者：</font>** Zhihong Cao, Chen Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the context of information seeking, conversational agents are undergoing an evolution from reactive tools to proactive, personalized assistants. A critical aspect of this evolution is the ability to tailor strategic interactions to a user's unique needs and expectations. Unlike existing studies that focus on proactively clarifying query ambiguities, we center on clarifying the user's expertise in order to tailor responses for better user comprehension. We find that existing agents struggle to determine user expertise from queries alone, a limitation that prevents them from dynamically adapting their responses. To address this gap, we introduce PASSING to empower the agent to proactively clarify a user's expertise through targeted inquiries. This is achieved by our What-to-ask and How-to-ask strategies, induced by LLM self-play. Our extensive experiments also show our superiority. We believe that PASSING represents a crucial step towards creating more human-centric conversational agents.

---


### 143. [Length-Adaptive Decoding for Masked Diffusion Machine Translation](https://arxiv.org/abs/2608.22274)

**<font color=#1a73e8>作者：</font>** Yan Zhan, Mengkai Hou, Wanting Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation tests masked diffusion language models (dLLMs) because every source token must be rendered faithfully, while fixed canvas decoding must choose target length before denoising. Existing masked diffusion decoding work mainly studies token unmasking order, leaving this length decision under-explored despite its direct effect on coverage and redundancy. We introduce Entropy-Valley (EV), a training-free length selector that scores candidate target canvases by mean predictive entropy from all-mask forward passes and selects the canvas the backbone is most prepared to fill. Relative to a baseline using training corpus length statistics, EV recovers 64.9%, 65.3%, and 33.0% of the COMET-22 gain from reference target lengths on En$\to$Zh, Zh$\to$En, and En$\to$De. Our diagnostics show that denoising-friendly lengths need not match reference lengths. Evaluation by three translation experts supports the En$\leftrightarrow$Zh adequacy gains, with stronger evidence on Zh$\to$En. Compared with a LLaMA-3-8B autoregressive (AR) model trained on the same fine-tuning data, the EV system ties on En$\to$Zh and leads on Zh$\to$En; an oracle-length diagnostic further shows that, in this masked diffusion MT setting, deciding which tokens to reveal first matters less than how the target length is supplied.

---


### 144. [OVIBench: Benchmarking Online Video Question Answering under Interruption](https://arxiv.org/abs/2608.22279)

**<font color=#1a73e8>作者：</font>** Naiming Liu, Zhiheng Wu, Shuning Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision language models (VLMs) have achieved strong progress in video understanding. However, most existing video QA research and benchmarks still follow an offline, single-round paradigm, overlooking realistic interactions where users may interrupt the model during answer generation. To address this gap, we formulate the task of Online Video Question Answering under Interruption and introduce OVIBench, the first standardized benchmark for evaluating VLMs in this setting. OVIBench categorizes interruptions into three types: Cancellation, False Trigger, Correction and supports both open-ended and multiple-choice evaluations. To enable large-scale and reproducible testing, we develop an offline simulation protocol that reproduces interruption during generation under a unified temporal setup, together with a multi-dimensional metric suite for assessing interruption understanding and response generation. Experiments demonstrate that OVIBench effectively distinguishes models' interruption-handling abilities, especially in following correction requests. Finally, we construct a train set OVI-Train for interruption-aware fine-tuning. Models fine-tuned on this dataset achieve significant gains on OVIBench, validating the effectiveness of our benchmark and data design. OVIBench, OVI-Train, and the evaluation code will be released.

---


### 145. [LLM Evaluation on Unseen Questions: Contextual Multidimensional IRT Model](https://arxiv.org/abs/2608.22295)

**<font color=#1a73e8>作者：</font>** Ergan Shang, Weijing Tang, Yinqiu He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation of large language models (LLMs) increasingly requires predicting how a model will perform on new questions or tasks before collecting large amounts of new annotations. This problem is challenging because question difficulty, scenario, and underlying capability demands can vary substantially. Simple retrospective averages may confound model ability with item characteristics. In this paper, we study a model-based evaluation framework that combines multidimensional item response theory model with question contexts to predict LLM performance on unseen questions. The framework represents LLMs through latent capability profiles while using question content to inform item characteristics, allowing information to transfer beyond previously observed items. Empirically, we find that for within-scenario evaluation, incorporating question embeddings improves prediction relative to model-free baselines, and that multidimensional latent structure provides a richer description of capability variation than unidimensional alternatives. At the same time, our results reveal an important limitation that the generalizability does not necessarily translate into reliable prediction under cross-scenario shift. These findings suggest that context-aware psychometric modeling is a promising direction for efficient and interpretable LLM evaluation, while also highlighting cross-scenario generalization as a central open challenge.

---


### 146. [HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory](https://arxiv.org/abs/2608.22310)

**<font color=#1a73e8>作者：</font>** Yuanhua Lin, Yile Li, Zhiyuan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is crucial for personalized responses and long-horizon agent interactions. Existing methods often rely on LLMs to compress or rewrite dialogue histories and use the transformed memories as retrieval evidence. Despite the progress in organizing fragmented contexts, two major drawbacks persist: (1) information loss from compression, which discards fine-grained but later useful details, and (2) semantic drift from rewriting, which erodes the original tone and situated context. In this work, we propose a novel Human-profile Enhanced Retrieval Optimization framework for long-term agent memory (HERO). Specifically, HERO converts the dialogue history into a traceable heterogeneous memory graph that preserves raw dialogue text as evidence for reasoning, thereby mitigating information loss. For retrieval, HERO extracts initial anchors from the current query and incorporates human profiles via an iterative graph traversal; these anchors and profiles provide guidance signals that adaptively activate the most informative regions of the graph. Experiments on two benchmark datasets show that HERO outperforms strong baselines on both factual and personalized reasoning, while providing more faithful access to raw dialogue evidence.

---


### 147. [Does a Modern-Handwriting Warm-Up Help Historical Arabic OCR? A Reproducible, Compute-Matched Evaluation on Muharaf and KHATT](https://arxiv.org/abs/2608.22316)

**<font color=#1a73e8>作者：</font>** Sumaih Almarshad, Maram Alamri, Dona Aloraini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whether an intermediate stage of modern Arabic handwriting helps or hurts historical Arabic HTR is usually decided from one implementation and one comparison, too thin a basis for a claim either way. We test stability by running the same nominal ablation four times, letting the base checkpoint, encoder-freezing strategy, epoch budget, precision, and learning-rate schedule vary as they naturally did during development, while holding the normalization, scorer, and interval estimation fixed. Each run compares intermediate training on modern handwriting (KHATT) then fine-tuning on historical manuscripts (Muharaf) against fine-tuning on Muharaf directly. Across the four runs the estimated effect swings from -17.64 to +14.52 CER points and reverses sign. The two extremes are exactly the two runs with an identifiable confound (a fivefold lower learning rate in one; a checkpoint of undisclosed provenance in the other); the two clean runs land at -0.25 and +0.94, i.e. no effect. A tight interval from one implementation says nothing about the next. We then run a compute-matched experiment with identical budgets over three seeds: KHATT warm-up is +2.42 CER points worse than a matched same-domain control (95% interval [+0.60, +4.25]); the part of that gap specific to the handwriting domain is only about 0.6 points a small negative effect under this configuration, not a universal result. We release a SaudiHeritage-OCR package with the normalizer, interval scorer, a verified KHATT decoder, experimental manifests, VLM baselines, and an edition-alignment protocol, so the result can be checked independently. The Al-Mahd inscription line is held strictly out and is not offered as a benchmark.

---


### 148. [Beyond Dense Adam States: Adaptive Log-Space Quantization for Memory-Efficient Optimizers](https://arxiv.org/abs/2608.22322)

**<font color=#1a73e8>作者：</font>** Yan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision optimizer-state methods are commonly designed for dense Adam-style moments, but memory-efficient optimizers maintain factored, confidence-based, or projected states whose quantization errors propagate differently. We characterize this heterogeneity in optimizer-state traces from language-model pre-training and introduce Adaptive Log-Space (AL) quantization, a block-wise representation for non-negative states that adapts its nonzero range per block while preserving exact zeros. AL8 and AL16 are combined with independent signed-momentum encodings and state-specific precision choices.
Across 96 runs totaling 214.7 GPU-hours, we evaluate AdamW, Adafactor, CAME, and APOLLO paths. On a 20K-step TinyLlama-1.1B benchmark, AdamW with AL8 second moments and 8-bit uniform momentum reaches 72.90 perplexity, versus 72.48 for FP32 and 73.54 for an 8-bit dynamic-quantization baseline, while reducing measured optimizer-state storage from 8392.7 to 2119.2 MiB. CAME requires higher precision for its non-negative states: AL16 reaches 86.16 perplexity versus 86.68 for FP32, while all-AL8 reaches 90.19. In a 100K-step GPT-2 experiment, topology-aware parameter protection reduces the late-loss gap of quantized Adafactor from +0.1185 to +0.0159. These results support state- and topology-aware optimizer quantization. End-to-end comparisons use a single training seed and are reported as empirical measurements.

---


### 149. [MedReaMM: Evaluating Large Multimodal Models on Expert-Level Clinical Diagnostic Synthesis](https://arxiv.org/abs/2608.22323)

**<font color=#1a73e8>作者：</font>** Lai Wei, Yuchao Chen, Zhenbiao Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The application of Large Language Models (LLMs) to diagnostic decision-making has garnered growing interest. However, existing benchmarks largely focus on textual reasoning or isolated visual question-answering (VQA) tasks, lacking holistic integration of clinical narratives and medical imaging, and thus failing to assess the multimodal diagnostic synthesis capability central to expert clinical judgment. To bridge this gap, we introduce MedReaMM, a benchmark specifically designed to evaluate models' ability to synthesize heterogeneous clinical evidence consisting of detailed patient histories alongside multiple medical images into accurate differential diagnoses under a complete-information paradigm. Constructed from case reports sourced from top-tier medical journals and curated clinical case databases, MedReaMM comprises 625 expert-validated cases with an average of 2.79 medical images per case and a total of 1,042 standardized diagnoses annotated with ICD-11 codes. These cases predominantly represent rare, atypical, or multi-system presentations that demand expert-level evidence integration beyond routine pattern recognition. We evaluate 23 Large Multimodal Models (LMMs) and find that most achieve diagnostic accuracy scores below 50%, underscoring a substantial gap in multimodal diagnostic synthesis capability. Further analysis reveals that medical knowledge proficiency, medical image understanding, and evidence integration are all highly correlated with diagnostic performance.

---


### 150. [Noise Floor Audit for Agent Benchmarks](https://arxiv.org/abs/2608.22331)

**<font color=#1a73e8>作者：</font>** Yihang Chen, Pin Qian, Su Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We audit measurement variability for 3 native tool-calling endpoints across 2 providers on the official BFCL multiple and parallel categories, using matched AST grading. At temperature 0, reruns are nearly deterministic across Groq endpoints and a thinking-enabled Gemini setting: ever-flip fractions are 0.7%, 2.0%, and 2.7%, with mean run correlations of 0.997, 0.966, and 0.961. Semantics-preserving prompt perturbations create the larger floor on all endpoints, with median perturbation paired SDs 11x to 58x larger than rerun paired SDs. The failure character also shifts: malformed-output failures account for 30%, 7%, and <1% of task failures, so marginal accuracy hides not only stability but also failure mode.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
