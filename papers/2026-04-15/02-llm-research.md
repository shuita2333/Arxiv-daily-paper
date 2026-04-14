# 🧠 大模型相关研究 | 2026年04月15日

> 本类共 **283** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

---

### 1. [LETGAMES: An LLM-Powered Gamified Approach to Cognitive Training for Patients with Cognitive Impairment](https://arxiv.org/abs/2604.09566)

**<font color=#1a73e8>作者：</font>** Jingwei Shi, Shengyu Tao, Xinxiang Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The application of games as a therapeutic tool for cognitive training is beneficial for patients with cognitive impairments. However, effective game design for individual patient is resource-intensive. To this end, we propose an LLM-powered method, \ours, for automated and personalized therapeutic game design. Inspired by the Dungeons & Dragons, LETGAMES generates an open-world interactive narrative game. It not only generates game scenarios and challenges that target specific cognitive domains, but also employs conversational strategies to offer guidance and companionship. To validate its efficacy, we pioneer a psychology-grounded evaluation protocol LETGAMESEVAL, establishing comprehensive metrics for rehabilitative assessment. Building upon this, our experimental results from both LLM-based assessors and human expert evaluations demonstrate the significant potential of our approach, positioning LETGAMES as a promising solution to the widespread need for more accessible and tailored cognitive training tools. Our code will be open-sourced upon acceptance.

---


### 2. [EvoDiagram: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568)

**<font color=#1a73e8>作者：</font>** Tianfu Wang, Leilei Ding, Ziyang Tao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> High-fidelity diagram creation requires the complex orchestration of semantic topology, visual styling, and spatial layout, posing a significant challenge for automated systems. Existing methods also suffer from a representation gap: pixel-based models often lack precise control, while code-based synthesis limits intuitive flexibility. To bridge this gap, we introduce EvoDiagram, an agentic framework that generates object-level editable diagrams via an intermediate canvas schema. EvoDiagram employs a coordinated multi-agent system to decouple semantic intent from rendering logic, resolving conflicts across heterogeneous design layers. Additionally, we propose a design knowledge evolution mechanism that distills execution traces into a hierarchical memory of domain guidelines, enabling agents to retrieve context-aware expertise adaptively. We further release CanvasBench, a benchmark consisting of both data and metrics for canvas-based diagramming. Extensive experiments demonstrate that EvoDiagram exhibits excellent performance and balance against baselines in generating editable, structurally consistent, and aesthetically coherent diagrams. Our code is available at this https URL.

---


### 3. [Automatic Mind Wandering Detection in Educational Settings: A Systematic Review and Multimodal Benchmarking](https://arxiv.org/abs/2604.09569)

**<font color=#1a73e8>作者：</font>** Anna Bodonhelyi, Augustin Curinier, Babette Bühler 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Detecting mind wandering is crucial in online education, and it occurs 30% of the time, as it directly impacts learners' retention, comprehension, and overall success in self-directed learning environments. Integrating automated detection algorithms enables the deployment of targeted interventions within adaptive learning environments, paving the way for more responsive and personalized educational systems. However, progress is hampered by a lack of coherent frameworks for identifying mind wandering in online environments. This work presents a comprehensive systematic review and benchmark of mind wandering detection across 14 datasets covering EEG, facial video, eye tracking, and physiological signals in educational settings, motivated by the challenges in achieving reliable detection and the inconsistency of results across studies caused by variations in models, preprocessing approaches, and evaluation metrics. We implemented a generalizable preprocessing and feature extraction pipeline tailored to each modality, ensuring fair comparison across diverse experimental paradigms. 13 traditional machine learning and neural network models, including federated learning approaches, were evaluated on each dataset. In a novel ablation study, we explored mind wandering detection from post-probe data, motivated by findings that learners often re-engage with material after mind wandering episodes through re-reading or re-watching. Results highlight the potential and limitations of different modalities and classifiers for mind wandering detection, and point to new opportunities for supporting online learning. All code and preprocessing scripts are made openly available to support reproducibility and future research.

---


### 4. [Tuning Qwen2.5-VL to Improve Its Web Interaction Skills](https://arxiv.org/abs/2604.09571)

**<font color=#1a73e8>作者：</font>** Alexandra Yakovleva, Henrik Pärssinen, Harri Valpola 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) have sparked growing interest in using them to automate web tasks, yet their feasibility as independent agents that reason and act purely from visual input remains underexplored. We investigate this setting using Qwen2.5-VL-32B, one of the strongest open-source VLMs available, and focus on improving its reliability in web-based control. Through initial experimentation, we observe three key challenges: (i) inaccurate localization of target elements, the cursor, and their relative positions, (ii) sensitivity to instruction phrasing, and (iii) an overoptimistic bias toward its own actions, often assuming they succeed rather than analyzing their actual outcomes. To address these issues, we fine-tune Qwen2.5-VL-32B for a basic web interaction task: moving the mouse and clicking on a page element described in natural language. Our training pipeline consists of two stages: (1) teaching the model to determine whether the cursor already hovers over the target element or whether movement is required, and (2) training it to execute a single command (a mouse move or a mouse click) at a time, verifying the resulting state of the environment before planning the next action. Evaluated on a custom benchmark of single-click web tasks, our approach increases success rates from 86% to 94% under the most challenging setting.

---


### 5. [ACE-TA: An Agentic Teaching Assistant for Grounded Q&A, Quiz Generation, and Code Tutoring](https://arxiv.org/abs/2604.09572)

**<font color=#1a73e8>作者：</font>** Himanshu Tripathi, Charlottee Crowell, Kaley Newlin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce ACE-TA, the Agentic Coding and Explanations Teaching Assistant framework, that autonomously routes conceptual queries drawn from programming course material to grounded Q&A, stepwise coding guidance, and automated quiz generation using pre-trained Large Language Models (LLMs). ACE-TA consists of three coordinated modules: a retrieval grounded conceptual Q&A system that provides precise, context-aligned explanations; a quiz generator that constructs adaptive, multi-topic assessments targeting higher-order understanding; and an interactive code tutor that guides students through step-by-step reasoning with sandboxed execution and iterative feedback.

---


### 6. [Generative UI: LLMs are Effective UI Generators](https://arxiv.org/abs/2604.09577)

**<font color=#1a73e8>作者：</font>** Yaniv Leviathan, Dani Valevski, Matan Kalman 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI models excel at creating content, but typically render it with static, predefined interfaces. Specifically, the output of LLMs is often a markdown "wall of text". Generative UI is a long standing promise, where the model generates not just the content, but the interface itself. Until now, Generative UI was not possible in a robust fashion. We demonstrate that when properly prompted and equipped with the right set of tools, a modern LLM can robustly produce high quality custom UIs for virtually any prompt. When ignoring generation speed, results generated by our implementation are overwhelmingly preferred by humans over the standard LLM markdown output. In fact, while the results generated by our implementation are worse than those crafted by human experts, they are at least comparable in 50% of cases. We show that this ability for robust Generative UI is emergent, with substantial improvements from previous models. We also create and release PAGEN, a novel dataset of expert-crafted results to aid in evaluating Generative UI implementations, as well as the results of our system for future comparisons. Interactive examples can be seen at this https URL

---


### 7. [OOWM: Structuring Embodied Reasoning and Planning via Object-Oriented Programmatic World Modeling](https://arxiv.org/abs/2604.09580)

**<font color=#1a73e8>作者：</font>** Hongyu Chen, Liang Lin, Guangrun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard Chain-of-Thought (CoT) prompting empowers Large Language Models (LLMs) with reasoning capabilities, yet its reliance on linear natural language is inherently insufficient for effective world modeling in embodied tasks. While text offers flexibility, it fails to explicitly represent the state-space, object hierarchies, and causal dependencies required for robust robotic planning. To address these limitations, we propose Object-Oriented World Modeling (OOWM), a novel framework that structures embodied reasoning through the lens of software engineering formalisms. We redefine the world model not as a latent vector space, but as an explicit symbolic tuple $W = \langle S, T \rangle$: a State Abstraction ($G_\text{state}$) instantiating the environmental state $S$, coupled with a Control Policy ($G_\text{control}$) representing the transition logic $T: S \times A \rightarrow S'$. OOWM leverages the Unified Modeling Language (UML) to materialize this definition: it employs Class Diagrams to ground visual perception into rigorous object hierarchies, and Activity Diagrams to operationalize planning into executable control flows. Furthermore, we introduce a three-stage training pipeline combining Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO). Crucially, this method utilizes outcome-based rewards from the final plan to implicitly optimize the underlying object-oriented reasoning structure, enabling effective learning even with sparse annotations. Extensive evaluations on the MRoom-30k benchmark demonstrate that OOWM significantly outperforms unstructured textual baselines in planning coherence, execution success, and structural fidelity, establishing a new paradigm for structured embodied reasoning.

---


### 8. [Agentic Exploration of PDE Spaces using Latent Foundation Models for Parameterized Simulations](https://arxiv.org/abs/2604.09584)

**<font color=#1a73e8>作者：</font>** Abhijeet Vishwasrao, Francisco Giral, Mahmoud Golestanian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow physics and more broadly physical phenomena governed by partial differential equations (PDEs), are inherently continuous, high-dimensional and often chaotic in nature. Traditionally, researchers have explored these rich spatiotemporal PDE solution spaces using laboratory experiments and/or computationally expensive numerical simulations. This severely limits automated and large-scale exploration, unlike domains such as drug discovery or materials science, where discrete, tokenizable representations naturally interface with large language models. We address this by coupling multi-agent LLMs with latent foundation models (LFMs), a generative model over parametrised simulations, that learns explicit, compact and disentangled latent representations of flow fields, enabling continuous exploration across governing PDE parameters and boundary conditions. The LFM serves as an on-demand surrogate simulator, allowing agents to query arbitrary parameter configurations at negligible cost. A hierarchical agent architecture orchestrates exploration through a closed loop of hypothesis, experimentation, analysis and verification, with a tool-modular interface requiring no user support. Applied to flow past tandem cylinders at Re = 500, the framework autonomously evaluates over 1,600 parameter-location pairs and discovers divergent scaling laws: a regime-dependent two-mode structure for minimum displacement thickness and a robust linear scaling for maximum momentum thickness, with both landscapes exhibiting a dual-extrema structure that emerges at the near-wake to co-shedding regime transition. The coupling of the learned physical representations with agentic reasoning establishes a general paradigm for automated scientific discovery in PDE-governed systems.

---


### 9. [Evaluating Visual Prompts with Eye-Tracking Data for MLLM-Based Human Activity Recognition](https://arxiv.org/abs/2604.09585)

**<font color=#1a73e8>作者：</font>** Jae Young Choi, Seon Gyeom Kim, Hyungjun Yoon 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have emerged as foundation models for IoT applications such as human activity recognition (HAR). However, directly applying high-frequency and multi-dimensional sensor data, such as eye-tracking data, leads to information loss and high token costs. To mitigate this, we investigate a visual prompting strategy that transforms sensor signals into data visualization images as an input to multimodal LLMs (MLLMs) using eye-tracking data. We conducted a systematic evaluation of MLLM-based HAR across three public eye-tracking datasets using three visualization types of timeline, heatmap, and scanpath, under varying temporal window sizes. Our findings suggest that visual prompting provides a token-efficient and scalable representation for eye-tracking data, highlighting its potential to enable MLLMs to effectively reason over high-frequency sensor signals in IoT contexts.

---


### 10. [Co-Disclosing the Computer: LLM-Mediated Computing through Reflective Conversation](https://arxiv.org/abs/2604.09586)

**<font color=#1a73e8>作者：</font>** Mattias Rost  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are changing how we interact with computers. As they become capable of generating software dynamically, they invite a fundamental rethinking of the computer's role in human activity. In this conceptual paper, we introduce LLM-mediated computing: a paradigm in which interaction is no longer structured around fixed applications, but emerges in real-time through human intent and LLM interpretation. We make three contributions: (1) we articulate a new interaction metaphor of reflective conversation to guide future design, (2) we use the lens of postphenomenology to understand the human-LLM-computer relation, and (3) we propose a new mode of computing based on co-disclosure, in which the computer is constituted in use. Together, they define a new mode of computing, provide a lens to analyze it, and offer a metaphor to design with.

---


### 11. [DeepReviewer 2.0: A Traceable Agentic System for Auditable Scientific Peer Review](https://arxiv.org/abs/2604.09590)

**<font color=#1a73e8>作者：</font>** Yixuan Weng, Minjun Zhu, Qiujie Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated peer review is often framed as generating fluent critique, yet reviewers and area chairs need judgments they can \emph{audit}: where a concern applies, what evidence supports it, and what concrete follow-up is required. DeepReviewer~2.0 is a process-controlled agentic review system built around an output contract: it produces a \textbf{traceable review package} with anchored annotations, localized evidence, and executable follow-up actions, and it exports only after meeting minimum traceability and coverage budgets. Concretely, it first builds a manuscript-only claim--evidence--risk ledger and verification agenda, then performs agenda-driven retrieval and writes anchored critiques under an export gate. On 134 ICLR~2025 submissions under three fixed protocols, an \emph{un-finetuned 196B} model running DeepReviewer~2.0 outperforms Gemini-3.1-Pro-preview, improving strict major-issue coverage (37.26\% vs.\ 23.57\%) and winning 71.63\% of micro-averaged blind comparisons against a human review committee, while ranking first among automatic systems in our pool. We position DeepReviewer~2.0 as an assistive tool rather than a decision proxy, and note remaining gaps such as ethics-sensitive checks.

---


### 12. [DERM-3R: A Resource-Efficient Multimodal Agents Framework for Dermatologic Diagnosis and Treatment in Real-World Clinical Settings](https://arxiv.org/abs/2604.09596)

**<font color=#1a73e8>作者：</font>** Ziwen Chen, Zhendong Wang, Chongjing Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dermatologic diseases impose a large and growing global burden, affecting billions and substantially reducing quality of life. While modern therapies can rapidly control acute symptoms, long-term outcomes are often limited by single-target paradigms, recurrent courses, and insufficient attention to systemic comorbidities. Traditional Chinese medicine (TCM) provides a complementary holistic approach via syndrome differentiation and individualized treatment, but practice is hindered by non-standardized knowledge, incomplete multimodal records, and poor scalability of expert reasoning. We propose DERM-3R, a resource-efficient multimodal agent framework to model TCM dermatologic diagnosis and treatment under limited data and compute. Based on real-world workflows, we reformulate decision-making into three core issues: fine-grained lesion recognition, multi-view lesion representation with specialist-level pathogenesis modeling, and holistic reasoning for syndrome differentiation and treatment planning. DERM-3R comprises three collaborative agents: DERM-Rec, DERM-Rep, and DERM-Reason, each targeting one component of this pipeline. Built on a lightweight multimodal LLM and partially fine-tuned on 103 real-world TCM psoriasis cases, DERM-3R performs strongly across dermatologic reasoning tasks. Evaluations using automatic metrics, LLM-as-a-judge, and physician assessment show that despite minimal data and parameter updates, DERM-3R matches or surpasses large general-purpose multimodal models. These results suggest structured, domain-aware multi-agent modeling can be a practical alternative to brute-force scaling for complex clinical tasks in dermatology and integrative medicine.

---


### 13. [Hubble: An LLM-Driven Agentic Framework for Safe and Automated Alpha Factor Discovery](https://arxiv.org/abs/2604.09601)

**<font color=#1a73e8>作者：</font>** Runze Shi, Shengyu Yan, Yuecheng Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering predictive alpha factors in quantitative finance remains a formidable challenge due to the vast combinatorial search space and inherently low signal-to-noise ratios in financial data. Existing automated methods, particularly genetic programming, often produce complex, uninterpretable formulas prone to overfitting. We introduce Hubble, a closed-loop factor mining framework that leverages Large Language Models (LLMs) as intelligent search heuristics, constrained by a domain-specific operator language and an Abstract Syntax Tree (AST)-based execution sandbox. The framework evaluates candidate factors through a rigorous statistical pipeline encompassing cross-sectional Rank Information Coefficient (RankIC), annualized Information Ratio, and portfolio turnover. An evolutionary feedback mechanism returns top-performing factors and structured error diagnostics to the LLM, enabling iterative refinement across multiple generation rounds. In experiments conducted on a panel of 30 U.S. equities over 752 trading days, the system evaluated 181 syntactically valid factors from 122 unique candidates across three rounds, achieving a peak composite score of 0.827 with 100% computational stability. Our results demonstrate that combining LLM-driven generation with deterministic safety constraints yields an effective, interpretable, and reproducible approach to automated factor discovery.

---


### 14. [LLMs for Text-Based Exploration and Navigation Under Partial Observability](https://arxiv.org/abs/2604.09604)

**<font color=#1a73e8>作者：</font>** Stephan Sandfuchs, Maximilian Melchert, Jörg Frochte  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exploration and goal-directed navigation in unknown layouts are central to inspection, logistics, and search-and-rescue. We ask whether large language models (LLMs) can function as \emph{text-only} controllers under partial observability -- without code execution, tools, or program synthesis. We introduce a reproducible benchmark with oracle localisation in fixed ASCII gridworlds: each step reveals only a local $5\times5$ window around the agent and the model must select one of \texttt{UP/RIGHT/DOWN/LEFT}. Nine contemporary LLMs ranging from open/proprietary, dense / Mixture of Experts and instruction- vs. reasoning-tuned are evaluated on two tasks across three layouts of increasing difficulty: \emph{Exploration} (maximising revealed cells) and \emph{Navigation} (reach the goal on the shortest path). The experimental results are evaluated on quantitative metrics including \emph{success rate}, \emph{efficiency} such as normalised coverage and \emph{path length} vs. oracle as well as qualitative analysis. Reasoning-tuned models reliably complete navigation across all layouts, yet remain less efficient than oracle paths. Few-shot demonstrations in the prompt chiefly help these Reasoning-tuned models by reducing invalid moves and shortening paths, while classic dense instruction models remain inconsistent. We observe characteristic action priors (UP/RIGHT) that can induce looping under partial observability. Overall, training regimen and test-time deliberation predict control ability better than raw parameter count. These findings suggest lightweight hybridisation with classical online planners as a practical route to deployable partial map systems.

---


### 15. [Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling](https://arxiv.org/abs/2604.09606)

**<font color=#1a73e8>作者：</font>** Keita Broadwater  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional benchmarks for large language models (LLMs), such as HELM and AIR-BENCH, primarily assess safety risk through breadth-oriented evaluation across diverse tasks. However, real-world deployment often exposes a different class of risk: operational failures arising from repeated generations of the same prompt rather than broad task generalization. In high-stakes settings, response consistency and safety under repeated use are critical operational requirements. We introduce Accelerated Prompt Stress Testing (APST), a depth-oriented evaluation framework inspired by highly accelerated stress testing in reliability engineering. APST probes LLM behavior by repeatedly sampling identical prompts under controlled operational conditions, including temperature variation and prompt perturbation, to surface latent failure modes such as hallucinations, refusal inconsistency, and unsafe completions. Rather than treating failures as isolated events, APST characterizes them statistically as stochastic outcomes of repeated inference. We model observed safety failures using Bernoulli and binomial formulations to estimate per-inference failure probabilities, enabling quantitative comparison of operational risk across models and configurations. We apply APST to multiple instruction-tuned LLMs evaluated on AIR-BENCH 2024 derived safety and security prompts. While models exhibit similar performance under conventional single- or very-low-sample evaluation (N <= 3), repeated sampling reveals substantial variation in empirical failure probabilities across temperatures. These results demonstrate that shallow benchmark scores can obscure meaningful differences in reliability under sustained use.

---


### 16. [Unifying Ontology Construction and Semantic Alignment for Deterministic Enterprise Reasoning at Scale](https://arxiv.org/abs/2604.09608)

**<font color=#1a73e8>作者：</font>** Hongyin Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While enterprises amass vast quantities of data, much of it remains chaotic and effectively dormant, preventing decision-making based on comprehensive information. Existing neuro-symbolic approaches rely on disjoint pipelines and struggle with error propagation. We introduce the large ontology model (LOM), a unified framework that seamlessly integrates ontology construction, semantic alignment, and logical reasoning into a single end-to-end architecture. LOM employs a construct-align-reason (CAR) pipeline, leveraging its unified architecture across all three stages: it first autonomously constructs a domain-specific ontological universe from raw data, then aligns neural generation with this structural reality using a graph-aware encoder and reinforcement learning, and finally executes deterministic reasoning over the constructed topology, node attributes and relation types. We evaluate LOM on a comprehensive benchmark constructed from diverse real-world enterprise datasets. Experimental results demonstrate that LOM-4B achieves 88.8% accuracy in ontology completion and 94% in complex graph reasoning tasks, significantly outperforming state-of-the-art LLMs. These findings validate that autonomous logical construction is essential for achieving deterministic, enterprise-grade intelligence.

---


### 17. [General-purpose LLMs as Models of Human Driver Behavior: The Case of Simplified Merging](https://arxiv.org/abs/2604.09609)

**<font color=#1a73e8>作者：</font>** Samir H.A. Mohammad, Wouter Mooi, Arkady Zgonnikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human behavior models are essential as behavior references and for simulating human agents in virtual safety assessment of automated vehicles (AVs), yet current models face a trade-off between interpretability and flexibility. General-purpose large language models (LLMs) offer a promising alternative: a single model potentially deployable without parameter fitting across diverse scenarios. However, what LLMs can and cannot capture about human driving behavior remains poorly understood. We address this gap by embedding two general-purpose LLMs (OpenAI o3 and Google Gemini 2.5 Pro) as standalone, closed-loop driver agents in a simplified one-dimensional merging scenario and comparing their behavior against human data using quantitative and qualitative analyses. Both models reproduce human-like intermittent operational control and tactical dependencies on spatial cues. However, neither consistently captures the human response to dynamic velocity cues, and safety performance diverges sharply between models. A systematic prompt ablation study reveals that prompt components act as model-specific inductive biases that do not transfer across LLMs. These findings suggest that general-purpose LLMs could potentially serve as standalone, ready-to-use human behavior models in AV evaluation pipelines, but future research is needed to better understand their failure modes and ensure their validity as models of human driving behavior.

---


### 18. [Self-Calibrating Language Models via Test-Time Discriminative Distillation](https://arxiv.org/abs/2604.09624)

**<font color=#1a73e8>作者：</font>** Mohamed Rissal Hedna, Jan Strich, Martin Semmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are systematically overconfident: they routinely express high certainty on questions they often answer incorrectly. Existing calibration methods either require labeled validation data, degrade under distribution shifts, or incur substantial inference costs. Recent work has shown that LLMs already contain a better-calibrated signal than the one they verbalize: the token probability of "True" when the model is asked "Is this answer correct?" ($P(\text{True})$) consistently outperforms their stated confidence, a gap that is theoretically grounded as generative error is lower-bounded by roughly twice the corresponding discriminative error. We introduce $\textbf{SECL}$ ($\textbf{SE}$lf-$\textbf{C}$alibrating $\textbf{L}$anguage Models), a test-time training (TTT) pipeline that exploits this gap as label-free self-supervision, requiring no labeled data or human supervision. SECL adapts only when the input distribution shifts, training on just 6--26% of the question stream at lower cost than the baseline it distills from. Across four small language models from three model families and four diverse domains, SECL reduces Expected Calibration Error (ECE) by 56--78%, outperforming its own supervision signal and matching or outperforming recent inference-time methods. SECL is the first method to apply TTT to calibration; seven ablations covering signal quality, gating strategy, weight accumulation, loss design, domain ordering, hyperparameter sensitivity, and layer selection confirm that each component is crucial and robust across configurations. Code: this https URL

---


### 19. [Toward Generalized Cross-Lingual Hateful Language Detection with Web-Scale Data and Ensemble LLM Annotations](https://arxiv.org/abs/2604.09625)

**<font color=#1a73e8>作者：</font>** Dang H. Dang, Jelena Mitrovi, Michael Granitzer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study whether large-scale unlabelled web data and LLM-based synthetic annotations can improve multilingual hate speech detection. Starting from texts crawled via this http URL~(OWS) in four languages (English, German, Spanish, Vietnamese), we pursue two complementary strategies. First, we apply continued pre-training to BERT models by continuing masked language modelling on unlabelled OWS texts before supervised fine-tuning, and show that this yields an average macro-F1 gain of approximately 3% over standard baselines across sixteen benchmarks, with stronger gains in low-resource settings. Second, we use four open-source LLMs (Mistral-7B, Llama3.1-8B, Gemma2-9B, Qwen2.5-14B) to produce synthetic annotations through three ensemble strategies: mean averaging, majority voting, and a LightGBM meta-learner. The LightGBM ensemble consistently outperforms the other strategies. Fine-tuning on these synthetic labels substantially benefits a small model (Llama3.2-1B: +11% pooled F1), but provides only a modest gain for the larger Qwen2.5-14B (+0.6%). Our results indicate that the combination of web-scale unlabelled data and LLM-ensemble annotations is the most valuable for smaller models and low-resource languages.

---


### 20. [HumorGen: Cognitive Synergy for Humor Generation in Large Language Models via Persona-Based Distillation](https://arxiv.org/abs/2604.09629)

**<font color=#1a73e8>作者：</font>** Edward Ajayi, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humor generation poses a significant challenge for Large Language Models (LLMs), because their standard training objective - predicting the most likely next word - inherently conflicts with the surprise and incongruity needed for comedy. To bridge this gap, we introduce the Cognitive Synergy Framework, a theoretically grounded methodology for generating high-quality humor data inspired by psychological theories of humor. Utilizing a Mixture-of-Thought (MoT) approach, we deploy six cognitive personas (e.g., The Absurdist, The Cynic) to synthesize diverse comedic perspectives for a given prompt. This framework creates a theoretically grounded dataset, which we use to fine-tune a 7B-parameter student model. We compare Direct Preference Optimization (DPO) and a novel Offline Group Relative Policy Optimization (O-GRPO); our 7B model significantly outperforms larger instruction-tuned baselines and achieves performance competitive with state-of-the-art proprietary models. We find that cognitive-driven data curation is far more critical than alignment algorithms or model scale for humor generation. Code and data will be available upon publication.

---


### 21. [Deliberative Alignment is Deep, but Uncertainty Remains: Inference time safety improvement in reasoning via attribution of unsafe behavior to base model](https://arxiv.org/abs/2604.09665)

**<font color=#1a73e8>作者：</font>** Pankayaraj Pathmanathan, Furong Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While the wide adoption of refusal training in large language models (LLMs) has showcased improvements in model safety, recent works have highlighted shortcomings due to the shallow nature of these alignment methods. To this end, the work on Deliberative alignment proposed distilling reasoning capabilities from stronger reasoning models, thereby instilling deeper safety in LLMs. In this work, we study the impact of deliberative alignment in language models. First, we show that despite being larger in model size and stronger in safety capability, there exists an alignment gap between teacher and student language models, which affects both the safety and general utility of the student model. Furthermore, we show that models aligned through deliberative alignment can retain unsafe behaviors from the base model despite learning the reasoning patterns of larger reasoning models. Building upon this observation, we propose a BoN sampling method that attributes the unsafe behavior back to the base LLMs in the latent space, thereby down-ranking unsafe responses to gain a meaningful improvement in model safety across multiple safety benchmarks with minimal loss in utility. In particular, across 7 teacher models and 6 student models of different classes and sizes, we show an average attack success rate (ASR) reduction of 28.2% in DAN, 31.3% in WildJailbreak and 35.4 % in StrongREJECT benchmarks. We further show that these safety gains prevail post RL training, thus highlighting the uncertainty in safety reasoning and it's explicit attribution to the base model.

---


### 22. [Human-like Working Memory Interference in Large Language Models](https://arxiv.org/abs/2604.09670)

**<font color=#1a73e8>作者：</font>** Hua-Dong Xiong, Li Ji-An, Jiaqi Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligent systems must maintain and manipulate task-relevant information online to adapt to dynamic environments and changing goals. This capacity, known as working memory, is fundamental to human reasoning and intelligence. Despite having on the order of 100 billion neurons, both biological and artificial systems exhibit limitations in working memory. This raises a key question: why do large language models (LLMs) show such limitations, given that transformers have full access to prior context through attention? We find that although a two-layer transformer can be trained to solve working memory tasks perfectly, a diverse set of pretrained LLMs continues to show working memory limitations. Notably, LLMs reproduce interference signatures observed in humans: performance degrades with increasing memory load and is biased by recency and stimulus statistics. Across models, stronger working memory capacity correlates with broader competence on standard benchmarks, mirroring its link to general intelligence in humans. Yet despite substantial variability in working memory performance, LLMs surprisingly converge on a common computational mechanism. Rather than directly copying the relevant memory item from context, models encode multiple memory items in entangled representations, such that successful recall depends on interference control -- actively suppressing task-irrelevant content to isolate the target for readout. Moreover, a targeted intervention that suppresses stimulus content information improves performance, providing causal support for representational interference. Together, these findings identify representational interference as a core constraint on working memory in pretrained LLMs, suggesting that working-memory limits in biological and artificial systems may reflect a shared computational challenge: selecting task-relevant information under interference.

---


### 23. [How LLMs Might Think](https://arxiv.org/abs/2604.09674)

**<font color=#1a73e8>作者：</font>** Joseph Gottlieb, Ethan Kemp, Matthew Trager  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do large language models (LLMs) think? Daniel Stoljar and Zhihe Vincent Zhang have recently developed an argument from rationality for the claim that LLMs do not think. We contend, however, that the argument from rationality not only falters, but leaves open an intriguing possibility: that LLMs engage only in arational, associative forms of thinking, and have purely associative minds. Our positive claim is that if LLMs think at all, they likely think precisely in this manner.

---


### 24. [Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models](https://arxiv.org/abs/2604.09687)

**<font color=#1a73e8>作者：</font>** Yunkai Zhang, Linda Li, Yingxin Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel on many multimodal reasoning benchmarks, but these evaluations often do not require an exhaustive readout of the image and can therefore obscure failures in faithfully capturing all visual details. We introduce Grid2Matrix (G2M), a controlled benchmark in which a model is shown a color grid and a color-to-number mapping, and must output the corresponding matrix. By varying grid size and the number of colors, G2M provides a simple way to increase visual complexity while minimizing semantic confounds. We find that VLMs exhibit a sharp early collapse in zero-shot end-to-end evaluation, failing on surprisingly small grids rather than degrading gradually as the task becomes denser. We probe the visual encoders of VLMs from two representative families and find that they preserve substantially more of the grid information than the corresponding end-to-end outputs. This suggests that the failure is not explained by visual encoding alone, but also reflects a gap between what remains recoverable from visual features and what is ultimately expressed in language. We term this gap \textit{Digital Agnosia}. Further analyses show that these errors are highly structured and depend strongly on how grid cells overlap with visual patch boundaries. We also find that common strategies such as model scaling and multimodal alignment do not fully eliminate this failure mode. We expect G2M to serve as a useful testbed for understanding where and how VLMs lose fine visual details, and for evaluating tasks where missing even small visual details can matter, such as tables, charts, forms, and GUIs.

---


### 25. [Immunizing 3D Gaussian Generative Models Against Unauthorized Fine-Tuning via Attribute-Space Traps](https://arxiv.org/abs/2604.09688)

**<font color=#1a73e8>作者：</font>** Jianwei Zhang, Sihan Cao, Chaoning Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large-scale generative models enable high-quality 3D synthesis. However, the public accessibility of pre-trained weights introduces a critical vulnerability. Adversaries can fine-tune these models to steal specialized knowledge acquired during pre-training, leading to intellectual property infringement. Unlike defenses for 2D images and language models, 3D generators require specialized protection due to their explicit Gaussian representations, which expose fundamental structural parameters directly to gradient-based optimization. We propose GaussLock, the first approach designed to defend 3D generative models against fine-tuning attacks. GaussLock is a lightweight parameter-space immunization framework that integrates authorized distillation with attribute-aware trap losses targeting position, scale, rotation, opacity, and color. Specifically, these traps systematically collapse spatial distributions, distort geometric shapes, align rotational axes, and suppress primitive visibility to fundamentally destroy structural integrity. By jointly optimizing these dual objectives, the distillation process preserves fidelity on authorized tasks while the embedded traps actively disrupt unauthorized reconstructions. Experiments on large-scale Gaussian models demonstrate that GaussLock effectively neutralizes unauthorized fine-tuning attacks. It substantially degrades the quality of unauthorized reconstructions, evidenced by significantly higher LPIPS and lower PSNR, while effectively maintaining performance on authorized fine-tuning.

---


### 26. [Assessing Privacy Preservation and Utility in Online Vision-Language Models](https://arxiv.org/abs/2604.09695)

**<font color=#1a73e8>作者：</font>** Karmesh Siddharam Chaudhari, Youxiang Zhu, Amy Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing use of Online Vision Language Models (OVLMs) for processing images has introduced significant privacy risks, as individuals frequently upload images for various utilities, unaware of the potential for privacy violations. Images contain relationships that relate to Personally Identifiable Information (PII), where even seemingly harmless details can indirectly reveal sensitive information through surrounding clues. This paper explores the critical issue of PII disclosure in images uploaded to OVLMs and its implications for user privacy. We investigate how the extraction of contextual relationships from images can lead to direct (explicit) or indirect (implicit) exposure of PII, significantly compromising personal privacy. Furthermore, we propose methods to protect privacy while preserving the intended utility of the images in Vision Language Model (VLM)-based applications. Our evaluation demonstrates the efficacy of these techniques, highlighting the delicate balance between maintaining utility and protecting privacy in online image processing environments. Index Terms-Personally Identifiable Information (PII), Privacy, Utility, privacy concerns, sensitive information

---


### 27. [Multi-Granularity Reasoning for Image Quality Assessment via Attribute-Aware Reinforcement Learning to Rank](https://arxiv.org/abs/2604.09704)

**<font color=#1a73e8>作者：</font>** Xiangyong Chen, Xiaochuan Lin, Haoran Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in reasoning-induced image quality assessment (IQA) have demonstrated the power of reinforcement learning to rank (RL2R) for training vision-language models (VLMs) to assess perceptual quality. However, existing approaches operate at a single granularity, predicting only an overall quality score, while overlooking the multi-dimensional nature of human quality perception, which encompasses attributes such as sharpness, color fidelity, noise level, and compositional aesthetics. In this paper, we propose MG-IQA (Multi-Granularity IQA), a multi-granularity reasoning framework that extends RL2R to jointly assess overall image quality and fine-grained quality attributes within a single inference pass. Our approach introduces three key innovations: (1) an attribute-aware prompting strategy that elicits structured multi-attribute reasoning from VLMs; (2) a multi-dimensional Thurstone reward model that computes attribute-specific fidelity rewards for group relative policy optimization; and (3) a cross-domain alignment mechanism that enables stable joint training across synthetic distortion, authentic distortion, and AI-generated image datasets without perceptual scale re-alignment. Extensive experiments on eight IQA benchmarks demonstrate that MG-IQA consistently outperforms state-of-the-art methods in both overall quality prediction (average SRCC improvement of 2.1\%) and attribute-level assessment, while generating interpretable, human-aligned quality descriptions.

---


### 28. [Head-wise Modality Specialization within MLLMs for Robust Fake News Detection under Missing Modality](https://arxiv.org/abs/2604.09711)

**<font color=#1a73e8>作者：</font>** Kai Qian, Weijie Shi, Jiaqi Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal fake news detection (MFND) aims to verify news credibility by jointly exploiting textual and visual evidence. However, real-world news dissemination frequently suffers from missing modality due to deleted images, corrupted screenshots, and similar issues. Thus, robust detection in this scenario requires preserving strong verification ability for each modality, which is challenging in MFND due to insufficient learning of the low-contribution modality and scarce unimodal annotations. To address this issue, we propose Head-wise Modality Specialization within Multimodal Large Language Models (MLLMs) for robust MFND under missing modality. Specifically, we first systematically study attention heads in MLLMs and their relationship with performance under missing modality, showing that modality-critical heads serve as key carriers of unimodal verification ability through their modality specialization. Based on this observation, to better preserve verification ability for the low-contribution modality, we introduce a head-wise specialization mechanism that explicitly allocates these heads to different modalities and preserves their specialization through lower-bound attention constraints. Furthermore, to better exploit scarce unimodal annotations, we propose a Unimodal Knowledge Retention strategy that prevents these heads from drifting away from the unimodal knowledge learned from limited supervision. Experiments show that our method improves robustness under missing modality while preserving performance with full multimodal input.

---


### 29. [LAST: Leveraging Tools as Hints to Enhance Spatial Reasoning for Multimodal Large Language Models](https://arxiv.org/abs/2604.09712)

**<font color=#1a73e8>作者：</font>** Shi-Yu Tian, Zhi Zhou, Kun-Yang Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning is a cornerstone capability for intelligent systems to perceive and interact with the physical world. However, multimodal large language models (MLLMs) frequently suffer from hallucinations and imprecision when parsing complex geometric layouts. As data-driven scaling struggles to internalize structured geometric priors and spatial constraints, integrating mature, specialized vision models presents a compelling alternative. Despite its promise, applying this paradigm to spatial reasoning is hindered by two key challenges: The difficulty of invoking heterogeneous, parameter-rich tools, as well as the challenge of understanding and effectively leveraging their diverse low-level outputs (e.g., segmentation masks, depth maps) in high-level reasoning. To address these challenges, we propose LAST, a unified framework for tool-augmented spatial reasoning. LAST features an extensible interactive sandbox, termed LAST-Box, which abstracts heterogeneous tool invocations into atomic instructions and reusable spatial skills, returning multimodal hints (e.g., annotated images and textual descriptions) that can be directly consumed by LLMs. We further design a three-stage progressive training strategy that guides models from understanding tool outputs to proficient and adaptive tool invocation. Experiments on four datasets show that LAST-7B achieves around 20\% performance gains over its backbone and outperforms strong proprietary closed-source LLMs, substantially enhancing reasoning on complex spatial tasks.

---


### 30. [ExecTune: Effective Steering of Black-Box LLMs with Guide Models](https://arxiv.org/abs/2604.09741)

**<font color=#1a73e8>作者：</font>** Vijay Lingam, Aditya Golatkar, Anwesan Pal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For large language models deployed through black-box APIs, recurring inference costs often exceed one-time training costs. This motivates composed agentic systems that amortize expensive reasoning into reusable intermediate representations. We study a broad class of such systems, termed Guide-Core Policies (GCoP), in which a guide model generates a structured strategy that is executed by a black-box core model. This abstraction subsumes base, supervised, and advisor-style approaches, which differ primarily in how the guide is trained. We formalize GCoP under a cost-sensitive utility objective and show that end-to-end performance is governed by guide-averaged executability: the probability that a strategy generated by the guide can be faithfully executed by the core. Our analysis shows that existing GCoP instantiations often fail to optimize executability under deployment constraints, resulting in brittle strategies and inefficient computation. Motivated by these insights, we propose ExecTune, a principled training recipe that combines teacher-guided acceptance sampling, supervised fine-tuning, and structure-aware reinforcement learning to directly optimize syntactic validity, execution success, and cost efficiency. Across mathematical reasoning and code-generation benchmarks, GCoP with ExecTune improves accuracy by up to 9.2% over prior state-of-the-art baselines while reducing inference cost by up to 22.4%. It enables Claude Haiku 3.5 to outperform Sonnet 3.5 on both math and code tasks, and to come within 1.7% absolute accuracy of Sonnet 4 at 38% lower cost. Beyond efficiency, GCoP also supports modular adaptation by updating the guide without retraining the core.

---


### 31. [CONSCIENTIA: Can LLM Agents Learn to Strategize? Emergent Deception and Trust in a Multi-Agent NYC Simulation](https://arxiv.org/abs/2604.09746)

**<font color=#1a73e8>作者：</font>** Aarush Sinha, Arion Das, Soumyadeep Nag 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed as autonomous agents, understanding how strategic behavior emerges in multi-agent environments has become an important alignment challenge. We take a neutral empirical stance and construct a controlled environment in which strategic behavior can be directly observed and measured. We introduce a large-scale multi-agent simulation in a simplified model of New York City, where LLM-driven agents interact under opposing incentives. Blue agents aim to reach their destinations efficiently, while Red agents attempt to divert them toward billboard-heavy routes using persuasive language to maximize advertising revenue. Hidden identities make navigation socially mediated, forcing agents to decide when to trust or deceive. We study policy learning through an iterative simulation pipeline that updates agent policies across repeated interaction rounds using Kahneman-Tversky Optimization (KTO). Blue agents are optimized to reduce billboard exposure while preserving navigation efficiency, whereas Red agents adapt to exploit remaining weaknesses. Across iterations, the best Blue policy improves task success from 46.0% to 57.3%, although susceptibility remains high at 70.7%. Later policies exhibit stronger selective cooperation while preserving trajectory efficiency. However, a persistent safety-helpfulness trade-off remains: policies that better resist adversarial steering do not simultaneously maximize task completion. Overall, our results show that LLM agents can exhibit limited strategic behavior, including selective trust and deception, while remaining highly vulnerable to adversarial persuasion.

---


### 32. [See Fair, Speak Truth: Equitable Attention Improves Grounding and Reduces Hallucination in Vision-Language Alignment](https://arxiv.org/abs/2604.09749)

**<font color=#1a73e8>作者：</font>** Mohammad Anas Azeez, Ankan Deria, Zohaib Hasan Siddiqui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) frequently hallucinate objects that are absent from the visual input, often because attention during decoding is disproportionately drawn to visually dominant or frequently occurring content. We observe that this inequity in attention allocation is a root cause of object hallucination: when rare, small, or contextually peripheral objects receive insufficient attention, the model fails to ground its generation in the full visual scene. We argue that every object in an image, regardless of its size, frequency or visual salience, deserves equal representational opportunity during decoding. To this end, we propose DOP-OBC, a training-free and architecture-agnostic decoding strategy built on the principle of equitable attention. Two complementary object-aware signals work in tandem: a Dominant Object Penalty (DOP) that softly suppresses attention over-concentration on visually dominant regions, and an Outlier Boost Coefficient (OBC) that amplifies attention toward rare yet confidently detected objects. These signals are injected as per-row logit modulations within the causal attention mask, requiring no weight updates and preserving autoregressive decoding properties. Extensive experiments across image and video MLLMs demonstrate consistent reductions in object hallucination on CHAIR and POPE benchmarks, alongside improvements in GPT-4o assessed captioning quality across correctness, consistency, detail, context and temporal dimensions. DOP-OBC establishes that fairness in attention allocation is not merely a design principle but a practical and effective path toward more faithful multimodal generation.

---


### 33. [MedLVR: Latent Visual Reasoning for Reliable Medical Visual Question Answering](https://arxiv.org/abs/2604.09757)

**<font color=#1a73e8>作者：</font>** Suyang Xi, Songtao Hu, Yuxiang Lai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision--language models (VLMs) have shown strong potential for medical visual question answering (VQA), yet their reasoning remains largely text-centric: images are encoded once as static context, and subsequent inference is dominated by language. This paradigm is fundamentally limited in clinical scenarios, where accurate answers often depend on subtle, localized visual evidence that cannot be reliably preserved in static embeddings. We propose \textsc{MedLVR}, a latent visual reasoning framework that introduces an explicit visual evidence state into autoregressive decoding. Instead of relying solely on text-based intermediate reasoning, \textsc{MedLVR} interleaves a short latent reasoning segment within the decoder by reusing hidden states as continuous latent steps, enabling iterative preservation and refinement of query-relevant visual evidence before answer generation. To support effective visual supervision, we adopt a two-stage training strategy: region of interest (ROI)-supervised fine-tuning aligns latent states with clinically relevant image evidence, and Visual-Latent Policy Optimization (VLPO) further optimizes latent reasoning and answer generation under outcome-level rewards. Experiments on OmniMedVQA and five external medical VQA benchmarks show that \textsc{MedLVR} consistently outperforms recent reasoning baselines and improves the average score over the Qwen2.5-VL-7B backbone from 48.3\% to 53.4\%. These results show that latent visual reasoning provides an effective mechanism for preserving diagnostically relevant visual evidence and improving the reliability of medical VQA.

---


### 34. [The Myth of Expert Specialization in MoEs: Why Routing Reflects Geometry, Not Necessarily Domain Expertise](https://arxiv.org/abs/2604.09780)

**<font color=#1a73e8>作者：</font>** Xi Wang, Soufiane Hayou, Eric Nalisnick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture of Experts (MoEs) are now ubiquitous in large language models, yet the mechanisms behind their "expert specialization" remain poorly understood. We show that, since MoE routers are linear maps, hidden state similarity is both necessary and sufficient to explain expert usage similarity, and specialization is therefore an emergent property of the representation space, not of the routing architecture itself. We confirm this at both token and sequence level across five pre-trained models. We additionally prove that load-balancing loss suppresses shared hidden state directions to maintain routing diversity, which might provide a theoretical explanation for specialization collapse under less diverse data, e.g. small batch. Despite this clean mechanistic account, we find that specialization patterns in pre-trained MoEs resist human interpretation: expert overlap between different models answering the same question is no higher than between entirely different questions ($\sim$60\%); prompt-level routing does not predict rollout-level routing; and deeper layers exhibit near-identical expert activation across semantically unrelated inputs, especially in reasoning models. We conclude that, while the efficiency perspective of MoEs is well understood, understanding expert specialization is at least as hard as understanding LLM hidden state geometry, a long-standing open problem in the literature.

---


### 35. [Pioneer Agent: Continual Improvement of Small Language Models in Production](https://arxiv.org/abs/2604.09791)

**<font color=#1a73e8>作者：</font>** Dhruv Atreja, Julia White, Nikhil Nayak 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models are attractive for production deployment due to their low cost, fast inference, and ease of specialization. However, adapting them to a specific task remains a challenging engineering loop, driven not by training itself but by surrounding decisions: data curation, failure diagnosis, regression avoidance, and iteration control. We present Pioneer Agent, a closed-loop system that automates this lifecycle. In cold-start mode, given only a natural-language task description, the agent acquires data, constructs evaluation sets, and iteratively trains models by jointly optimizing data, hyperparameters, and learning strategy. In production mode, given a deployed model with labeled failures, it diagnoses error patterns, constructs targeted training data, and retrains under explicit regression constraints. To evaluate this setting, we introduce AdaptFT-Bench, a benchmark of synthetic inference logs with progressively increasing noise, designed to test the full adaptation loop: diagnosis, curriculum synthesis, retraining, and verification. Across eight cold-start benchmarks spanning reasoning, math, code generation, summarization, and classification, Pioneer Agent improves over base models by 1.6-83.8 points. On AdaptFT-Bench, it improves or preserves performance in all seven scenarios, while naive retraining degrades by up to 43 points. On two production-style deployments built from public benchmark tasks, it raises intent classification from 84.9% to 99.3% and Entity F1 from 0.345 to 0.810. Beyond performance gains, the agent often discovers effective training strategies, including chain-of-thought supervision, task-specific optimization, and quality-focused data curation, purely from downstream feedback.

---


### 36. [Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning](https://arxiv.org/abs/2604.09813)

**<font color=#1a73e8>作者：</font>** Siyuan Xu, Shiyang Li, Xin Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing synthetic tool-use corpora are primarily designed for offline supervised fine-tuning, yet reinforcement learning (RL) requires executable environments that support reward-checkable online rollouts. We propose COVERT, a two-stage pipeline that first generates reliable base tool-use trajectories through self-evolving synthesis with multi-level validation, and then applies oracle-preserving augmentations that systematically increase environmental complexity. These augmentations introduce distractor tools, indirect or ambiguous user queries, and noisy, multi-format, or erroneous tool outputs, while strictly preserving oracle tool calls and final answers as ground truth. This design enables automatic reward computation via reference matching for standard cases and lightweight judge-assisted verification for special behaviors such as error detection, supporting RL optimization of tool-calling policies. On Qwen2.5-Instruct-14B, COVERT-RL improves overall accuracy on BFCL v3 from 56.5 to 59.9 and on ACEBench from 53.0 to 59.3, with minimal regressions on general-ability benchmarks; when stacked on SFT, it further reaches 62.1 and 61.8, confirming additive gains. These results suggest that oracle-preserving synthetic environments offer a practical RL refinement stage, complementary to SFT, for improving tool-use robustness under ambiguity and unreliable tool feedback.

---


### 37. [RobustMedSAM: Degradation-Resilient Medical Image Segmentation via Robust Foundation Model Adaptation](https://arxiv.org/abs/2604.09814)

**<font color=#1a73e8>作者：</font>** Jieru Li, Matthew Chen, Micky C. Nnamdi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models built on Segment Anything Model (SAM) achieve strong performance on clean benchmarks, yet their reliability often degrades under realistic image corruptions such as noise, blur, motion artifacts, and modality-specific distortions. Existing approaches address either medical-domain adaptation or corruption robustness, but not both jointly. In SAM, we find that these capabilities are concentrated in complementary modules: the image encoder preserves medical priors, while the mask decoder governs corruption robustness. Motivated by this observation, we propose RobustMedSAM, which adopts module-wise checkpoint fusion by initializing the image encoder from MedSAM and the mask decoder from RobustSAM under a shared ViT-B architecture. We then fine-tune only the mask decoder on 35 medical datasets from MedSegBench, spanning six imaging modalities and 12 corruption types, while freezing the remaining components to preserve pretrained medical representations. We additionally investigate an SVD-based parameter-efficient variant for limited encoder adaptation. Experiments on both in-distribution and out-of-distribution benchmarks show that RobustMedSAM improves degraded-image Dice from 0.613 to 0.719 (+0.106) over SAM, demonstrating that structured fusion of complementary pretrained models is an effective and practical approach for robust medical image segmentation.

---


### 38. [Steered LLM Activations are Non-Surjective](https://arxiv.org/abs/2604.09839)

**<font color=#1a73e8>作者：</font>** Aayush Mishra, Daniel Khashabi, Anqi Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering is a popular white-box control technique that modifies model activations to elicit an abstract change in output behavior. It has also become a standard tool in interpretability (e.g., probing truthfulness, or translating activations into human-readable explanations and safety research (e.g., studying jailbreakability). However, it is unclear whether steered activation states are realizable by any textual prompt. In this work, we cast this question as a surjectivity problem: for a fixed model, does every steered activation admit a pre-image under the model's natural forward pass? Under practical assumptions, we prove that activation steering pushes the residual stream off the manifold of states reachable from discrete prompts. Almost surely, no prompt can reproduce the same internal behavior induced by steering. We also illustrate this finding empirically across three widely used LLMs. Our results establish a formal separation between white-box steerability and black-box prompting. We therefore caution against interpreting the ease and success of activation steering as evidence of prompt-based interpretability or vulnerability, and argue for evaluation protocols that explicitly decouple white-box and black-box interventions.

---


### 39. [Is There Knowledge Left to Extract? Evidence of Fragility in Medically Fine-Tuned Vision-Language Models](https://arxiv.org/abs/2604.09841)

**<font color=#1a73e8>作者：</font>** Oliver McLaughlin, Daniel Shubin, Carsten Eickhoff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly adapted through domain-specific fine-tuning, yet it remains unclear whether this improves reasoning beyond superficial visual cues, particularly in high-stakes domains like medicine. We evaluate four paired open-source VLMs (LLaVA vs. LLaVA-Med; Gemma vs. MedGemma) across four medical imaging tasks of increasing difficulty: brain tumor, pneumonia, skin cancer, and histopathology classification. We find that performance degrades toward near-random levels as task difficulty increases, indicating limited clinical reasoning. Medical fine-tuning provides no consistent advantage, and models are highly sensitive to prompt formulation, with minor changes causing large swings in accuracy and refusal rates. To test whether closed-form VQA suppresses latent knowledge, we introduce a description-based pipeline where models generate image descriptions that a text-only model (GPT-5.1) uses for diagnosis. This recovers a limited additional signal but remains bounded by task difficulty. Analysis of vision encoder embeddings further shows that failures stem from both weak visual representations and downstream reasoning. Overall, medical VLM performance is fragile, prompt-dependent, and not reliably improved by domain-specific fine-tuning.

---


### 40. [MEMENTO: Teaching LLMs to Manage Their Own Context](https://arxiv.org/abs/2604.09852)

**<font color=#1a73e8>作者：</font>** Vasilis Kontonis, Yuchen Zeng, Shivam Garg 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models think in long, unstructured streams with no mechanism for compressing or organizing their own intermediate state. We introduce MEMENTO: a method that teaches models to segment reasoning into blocks, compress each block into a memento, i.e., a dense state summary, and reason forward by attending only to mementos, reducing context, KV cache, and compute. To train MEMENTO models, we release OpenMementos, a public dataset of 228K reasoning traces derived from OpenThoughts-v3, segmented and annotated with intermediate summaries. We show that a two-stage SFT recipe on OpenMementos is effective across different model families (Qwen3, Phi-4, Olmo 3) and scales (8B--32B parameters). Trained models maintain strong accuracy on math, science, and coding benchmarks while achieving ${\sim}2.5\times$ peak KV cache reduction. We extend vLLM to support our inference method, achieving ${\sim}1.75\times$ throughput improvement while also enabling us to perform RL and further improve accuracy. Finally, we identify a dual information stream: information from each reasoning block is carried both by the memento text and by the corresponding KV states, which retain implicit information from the original block. Removing this channel drops accuracy by 15\,pp on AIME24.

---


### 41. [Spoiler Alert: Narrative Forecasting as a Metric for Tension in LLM Storytelling](https://arxiv.org/abs/2604.09854)

**<font color=#1a73e8>作者：</font>** Peiqi Sui, Yutong Zhu, Tianyi Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have so far failed both to generate consistently compelling stories and to recognize this failure--on the leading creative-writing benchmark (EQ-Bench), LLM judges rank zero-shot AI stories above New Yorker short stories, a gold standard for literary fiction. We argue that existing rubrics overlook a key dimension of compelling human stories: narrative tension. We introduce the 100-Endings metric, which walks through a story sentence by sentence: at each position, a model predicts how the story will end 100 times given only the text so far, and we measure tension as how often predictions fail to match the ground truth. Beyond the mismatch rate, the sentence-level curve yields complementary statistics, such as inflection rate, a geometric measure of how frequently the curve reverses direction, tracking twists and revelations. Unlike rubric-based judges, 100-Endings correctly ranks New Yorker stories far above LLM outputs. Grounded in narratological principles, we design a story-generation pipeline using structural constraints, including analysis of story templates, idea formulation, and narrative scaffolding. Our pipeline significantly increases narrative tension as measured by the 100-Endings metric, while maintaining performance on the EQ-Bench leaderboard.

---


### 42. [Instructing LLMs to Negotiate using Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2604.09855)

**<font color=#1a73e8>作者：</font>** Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The recent advancement of Large Language Models (LLMs) has established their potential as autonomous interactive agents. However, they often struggle in strategic games of incomplete information, such as bilateral price negotiation. In this paper, we investigate if Reinforcement Learning from Verifiable Rewards (RLVR) can effectively teach LLMs to negotiate. Specifically, we explore the strategic behaviors that emerge during the learning process. We introduce a framework that trains a mid-sized buyer agent against a regulated LLM seller across a wide distribution of real-world products. By grounding reward signals directly in the maximization of economic surplus and strict adherence to private budget constraints, we reveal a novel four-phase strategic evolution. The agent progresses from naive bargaining to using aggressive starting prices, moves through a phase of deadlock, and ultimately develops sophisticated persuasive skills. Our results demonstrate that this verifiable training allows a 30B agent to significantly outperform frontier models over ten times its size in extracting surplus. Furthermore, the trained agent generalizes robustly to stronger counterparties unseen during training and remains effective even when facing hostile, adversarial seller personas.

---


### 43. [In-situ process monitoring for defect detection in wire-arc additive manufacturing: an agentic AI approach](https://arxiv.org/abs/2604.09889)

**<font color=#1a73e8>作者：</font>** Pallock Halder, Satyajit Mojumder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are being increasingly deployed across a wide range of real-world applications. In this paper, we propose an agentic AI framework for in-situ process monitoring for defect detection in wire-arc additive manufacturing (WAAM). The autonomous agent leverages a WAAM process monitoring dataset and a trained classification tool to build AI agents and uses a large language model (LLM) for in-situ process monitoring decision-making for defect detection. A processing agent is developed based on welder process signals, such as current and voltage, and a monitoring agent is developed based on acoustic data collected during the process. Both agents are tasked with identifying porosity defects from processing and monitoring signals, respectively. Ground truth X-ray computed tomography (XCT) data are used to develop classification tools for both the processing and monitoring agents. Furthermore, a multi-agent framework is demonstrated in which the processing and monitoring agents are orchestrated together for parallel decision-making on the given task of defect classification. Evaluation metrics are proposed to determine the efficacy of both individual agents, the combined single-agent, and the coordinated multi-agent system. The multi-agent configuration outperforms all individual-agent counterparts, achieving a decision accuracy of 91.6% and an F1 score of 0.821 on decided runs, across 15 independent runs, and a reasoning quality score of 3.74 out of 5. These in-situ process monitoring agents hold significant potential for autonomous real-time process monitoring and control toward building qualified parts for WAAM and other additive manufacturing processes.

---


### 44. [Improving Pediatric Emergency Department Triage with Modality Dropout in Late Fusion Multimodal EHR Models](https://arxiv.org/abs/2604.09905)

**<font color=#1a73e8>作者：</font>** Tyler Yang, Romal Mitr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergency department triage relies heavily on both quantitative vital signs and qualitative clinical notes, yet multimodal machine learning models predicting triage acuity often suffer from modality collapse by over-relying on structured tabular data. This limitation severely hinders demographic generalizability, particularly for pediatric patients where developmental variations in vital signs make unstructured clinical narratives uniquely crucial. To address this gap, we propose a late-fusion multimodal architecture that processes tabular vitals via XGBoost and unstructured clinical text via Bio_ClinicalBERT, combined through a Logistic Regression meta-classifier to predict the 5-level Emergency Severity Index. To explicitly target the external validity problem, we train our model exclusively on adult encounters from the MIMIC-IV and NHAMCS datasets and evaluate its zero-shot generalization on a traditionally overlooked pediatric cohort. Furthermore, we employ symmetric modality dropout during training to prevent the ensemble from overfitting to adult-specific clinical correlations. Our results demonstrate that the multimodal framework significantly outperforms single-modality baselines. Most notably, applying a 30-40% symmetric modality dropout rate yielded steep performance improvements in the unseen pediatric cohort, elevating the Quadratic Weighted Kappa to 0.351. These findings highlight modality dropout as a critical regularization technique for mitigating modality collapse and enhancing cross-demographic generalization in clinical AI.

---


### 45. [From UAV Imagery to Agronomic Reasoning: A Multimodal LLM Benchmark for Plant Phenotyping](https://arxiv.org/abs/2604.09907)

**<font color=#1a73e8>作者：</font>** Yu Wu, Guangzeng Han, Ibra Niang Niang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To improve crop genetics, high-throughput, effective and comprehensive phenotyping is a critical prerequisite. While such tasks were traditionally performed manually, recent advances in multimodal foundation models, especially in vision-language models (VLMs), have enabled more automated and robust phenotypic analysis. However, plant science remains a particularly challenging domain for foundation models because it requires domain-specific knowledge, fine-grained visual interpretation, and complex biological and agronomic reasoning. To address this gap, we develop PlantXpert, an evidence-grounded multimodal reasoning benchmark for soybean and cotton phenotyping. Our benchmark provides a structured and reproducible framework for agronomic adaptation of VLMs, and enables controlled comparison between base models and their domain-adapted counterparts. We constructed a dataset comprising 385 digital images and more than 3,000 benchmark samples spanning key plant science domains including disease, pest control, weed management, and yield. The benchmark can assess diverse capabilities including visual expertise, quantitative reasoning, and multi-step agronomic reasoning. A total of 11 state-of-the-art VLMs were evaluated. The results indicate that task-specific fine-tuning leads to substantial improvement in accuracy, with models such as Qwen3-VL-4B and Qwen3-VL-30B achieving up to 78%. At the same time, gains from model scaling diminish beyond a certain capacity, generalization across soybean and cotton remains uneven, and quantitative as well as biologically grounded reasoning continue to pose substantial challenges. These findings suggest that PlantXpert can serve as a foundation for assessing evidence-grounded agronomic reasoning and for advancing multimodal model development in plant science.

---


### 46. [Does Your VFM Speak Plant? The Botanical Grammar of Vision Foundation Models for Object Detection](https://arxiv.org/abs/2604.09920)

**<font color=#1a73e8>作者：</font>** Lars Lundqvist, Earl Ranario, Hamid Kamangir 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) offer the promise of zero-shot object detection without task-specific training data, yet their performance in complex agricultural scenes remains highly sensitive to text prompt construction. We present a systematic prompt optimization framework evaluating four open-vocabulary detectors -- YOLO World, SAM3, Grounding DINO, and OWLv2 -- for cowpea flower and pod detection across synthetic and real field imagery. We decompose prompts into eight axes and conduct one-factor-at-a-time analysis followed by combinatorial optimization, revealing that models respond divergently to prompt structure: conditions that optimize one architecture can collapse another. Applying model-specific combinatorial prompts yields substantial gains over a naive species-name baseline, including +0.357 mAP@0.5 for YOLO World and +0.362 mAP@0.5 for OWLv2 on synthetic cowpea flower data. To evaluate cross-task generalization, we use an LLM to translate the discovered axis structure to a morphologically distinct target -- cowpea pods -- and compare against prompting using the discovered optimal structures from synthetic flower data. Crucially, prompt structures optimized exclusively on synthetic data transfer effectively to real-world fields: synthetic-pipeline prompts match or exceed those discovered on labeled real data for the majority of model-object combinations (flower: 0.374 vs. 0.353 for YOLO World; pod: 0.429 vs. 0.371 for SAM3). Our findings demonstrate that prompt engineering can substantially close the gap between zero-shot VFMs and supervised detectors without requiring manual annotation, and that optimal prompts are model-specific, non-obvious, and transferable across domains.

---


### 47. [A Tale of Two Temperatures: Simple, Efficient, and Diverse Sampling from Diffusion Language Models](https://arxiv.org/abs/2604.09921)

**<font color=#1a73e8>作者：</font>** Theo X. Olausson, Metod Jazbec, Xi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Much work has been done on designing fast and accurate sampling for diffusion language models (dLLMs). However, these efforts have largely focused on the tradeoff between speed and quality of individual samples; how to additionally ensure diversity across samples remains less well understood. In this work, we show that diversity can be increased by using softened, tempered versions of familiar confidence-based remasking heuristics, retaining their computational benefits and offering simple implementations. We motivate this approach by introducing an idealized formal model of fork tokens and studying the impact of remasking on the expected entropy at the forks. Empirically, the proposed tempered heuristics close the exploration gap (pass@k) between existing confidence-based and autoregressive sampling, hence outperforming both when controlling for cost (pass@NFE). We further study how the increase in diversity translates to downstream post-training and test-time compute scaling. Overall, our findings demonstrate that simple, efficient, and diverse sampling from dLLMs is possible.

---


### 48. [New Hybrid Fine-Tuning Paradigm for LLMs: Algorithm Design and Convergence Analysis Framework](https://arxiv.org/abs/2604.09940)

**<font color=#1a73e8>作者：</font>** Shaocong Ma, Peiran Yu, Heng Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning Large Language Models (LLMs) typically involves either full fine-tuning, which updates all model parameters, or Parameter-Efficient Fine-Tuning (PEFT), which adjusts a small subset of parameters. However, both approaches have inherent limitations: full fine-tuning is computationally expensive, while PEFT often struggles to learn new knowledge and exhibits suboptimal performance. To overcome these issues, we propose a novel hybrid fine-tuning approach that jointly updates both LLMs and PEFT modules using a combination of zeroth-order and first-order optimization methods. To analyze our new algorithm, we develop a theoretical framework centered on the concept of hybrid smoothness condition, which accounts for the heterogeneous nature of the optimization landscape in joint LLM and PEFT training. We derive a rigorous convergence analysis for the convergence of reshuffling-type SGD algorithm under multiple learning rates and demonstrate its effectiveness through extensive empirical studies across various downstream tasks and model architectures. On the practical side, our results demonstrate consistent performance improvement, making the approach a viable solution for large-scale language model fine-tuning.

---


### 49. [Cross-Cultural Value Awareness in Large Vision-Language Models](https://arxiv.org/abs/2604.09945)

**<font color=#1a73e8>作者：</font>** Phillip Howard, Xin Su, Kathleen C. Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of large vision-language models (LVLMs) in recent years has been accompanied by growing fairness concerns due to their propensity to reinforce harmful societal stereotypes. While significant attention has been paid to such fairness concerns in the context of social biases, relatively little prior work has examined the presence of stereotypes in LVLMs related to cultural contexts such as religion, nationality, and socioeconomic status. In this work, we aim to narrow this gap by investigating how cultural contexts depicted in images influence the judgments LVLMs make about a person's moral, ethical, and political values. We conduct a multi-dimensional analysis of such value judgments in five popular LVLMs using counterfactual image sets, which depict the same person across different cultural contexts. Our evaluation framework diagnoses LVLM awareness of cultural value differences through the use of Moral Foundations Theory, lexical analyses, and the sensitivity of generated values to depicted cultural contexts.

---


### 50. [SLM Finetuning for Natural Language to Domain Specific Code Generation in Production](https://arxiv.org/abs/2604.09952)

**<font color=#1a73e8>作者：</font>** Renjini R. Nair, Damian K. Kowalczyk, Marco Gaudesi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many applications today use large language models for code generation; however, production systems have strict latency requirements that can be difficult to meet with large models. Small language models with a few billion parameters are resource efficient but may suffer from limited reasoning, hallucinations, or poor retention of longer context. Fine tuning improves task specific accuracy by embedding domain knowledge directly into model weights, reducing reliance on runtime context. We previously implemented a baseline natural language to code generation approach using a retrieval augmented generation pipeline that dynamically selected few shot examples to embed domain specific language context for a large language model. In this study, we evaluate small language models for generating domain specific language from natural language by fine tuning variants of Mistral and other models on a dataset of natural language code pairs. Our results show that the fine-tuned models achieve improved performance and latency on test datasets compared to larger models. We also demonstrate that the trained model can be further fine-tuned for customer specific scenarios without degrading general performance, helping resolve production issues. Load testing followed by production deployment confirmed optimal performance in terms of latency and quality. These findings demonstrate that task specific fine tuning with small language models provides an efficient, faster, and cost-effective alternative to large language models for domain specific language generation.

---


### 51. [Muon$^2$: Boosting Muon via Adaptive Second-Moment Preconditioning](https://arxiv.org/abs/2604.09967)

**<font color=#1a73e8>作者：</font>** Ziyue Liu, Ruijie Zhang, Zhengyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has emerged as a promising optimizer for large-scale foundation model pre-training by exploiting the matrix structure of neural network updates through iterative orthogonalization. However, its practical efficiency is limited by the need for multiple Newton--Schulz (NS) iterations per optimization step, which introduces non-trivial computation and communication overhead. We propose Muon$^2$, an extension of Muon that applies Adam-style adaptive second-moment preconditioning before orthogonalization. Our key insight is that the core challenge of polar approximation in Muon lies in the ill-conditioned momentum matrix, of which the spectrum is substantially improved by Muon$^2$, leading to faster convergence toward a practically sufficient orthogonalization. We further characterize the practical orthogonalization quality via directional alignment, under which Muon$^2$ demonstrates dramatic improvement over Muon at each polar step. Across GPT and LLaMA pre-training experiments from 60M to 1.3B parameters, Muon$^2$ consistently outperforms Muon and recent Muon variants while reducing NS iterations by 40\%. We further introduce Muon$^2$-F, a memory-efficient factorized variant that preserves most of the gains of Muon$^2$ with negligible memory overhead.

---


### 52. [GIF: A Conditional Multimodal Generative Framework for IR Drop Imaging in Chip Layouts](https://arxiv.org/abs/2604.09999)

**<font color=#1a73e8>作者：</font>** Kiran Thorat, Nicole Meng, Mostafa Karami 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> IR drop analysis is essential in physical chip design to ensure the power integrity of on-chip power delivery networks. Traditional Electronic Design Automation (EDA) tools have become slow and expensive as transistor density scales. Recent works have introduced machine learning (ML)-based methods that formulate IR drop analysis as an image prediction problem. These existing ML approaches fail to capture both local and long-range dependencies and ignore crucial geometrical and topological information from physical layouts and logical connectivity. To address these limitations, we propose GIF, a Generative IR drop Framework that uses both geometrical and topological information to generate IR drop images. GIF fuses image and graph features to guide a conditional diffusion process, producing high-quality IR drop images. For instance, On the CircuitNet-N28 dataset, GIF achieves 0.78 SSIM, 0.95 Pearson correlation, 21.77 PSNR, and 0.026 NMAE, outperforming prior methods. These results demonstrate that our framework, using diffusion based multimodal conditioning, reliably generates high quality IR drop images. This shows that IR drop analysis can effectively leverage recent advances in generative modeling when geometric layout features and logical circuit topology are jointly modeled. By combining geometry aware spatial features with logical graph representations, GIF enables IR drop analysis to benefit from recent advances in generative modeling for structured image generation.

---


### 53. [Raiven: LLM-Based Visualization Authoring via Domain-Specific Language Mediation](https://arxiv.org/abs/2604.10008)

**<font color=#1a73e8>作者：</font>** Alexandra Irger, Ella Hugie, Minghao Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualization is central to scientific discovery, yet authoring tools remain split between information and scientific visualization, and expertise in one rarely transfers to the other. Large Language Model (LLM) based systems promise to bridge this gap through natural language, but current approaches generate code non-deterministically, with no guarantee of correctness and no protection against silent data fabrication. We present Raiven, a conversational system that mediates visualization authoring through a formally defined domain-specific language. RaivenDSL unifies scientific and information visualization in a single representation spanning 2D, 3D, and tabular data. The LLM produces a compact RaivenDSL specification under schema-guided constraints, and a deterministic compiler translates it to executable D3 or this http URL code. Because the LLM operates only on dataset metadata, outputs are deterministic, specifications are verifiable before execution, and data fabrication is impossible by construction. In a 100-task benchmark, Raiven achieves 100% compilation, is up to six times faster and six times cheaper than state-of-the-art LLMs, while improving interaction quality, correctness, and data faithfulness. An expert user study shows that Raiven significantly reduces debugging effort and makes it easier to produce correct visualizations.

---


### 54. [Demographic and Linguistic Bias Evaluation in Omnimodal Language Models](https://arxiv.org/abs/2604.10014)

**<font color=#1a73e8>作者：</font>** Alaa Elobaid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper provides a comprehensive evaluation of demographic and linguistic biases in omnimodal language models that process text, images, audio, and video within a single framework. Although these models are being widely deployed, their performance across different demographic groups and modalities is not well studied. Four omnimodal models are evaluated on tasks that include demographic attribute estimation, identity verification, activity recognition, multilingual speech transcription, and language identification. Accuracy differences are measured across age, gender, skin tone, language, and country of origin. The results show that image and video understanding tasks generally exhibit better performance with smaller demographic disparities. In contrast, audio understanding tasks exhibit significantly lower performance and substantial bias, including large accuracy differences across age groups, genders, and languages, and frequent prediction collapse toward narrow categories. These findings highlight the importance of evaluating fairness across all supported modalities as omnimodal language models are increasingly used in real-world applications.

---


### 55. [FinTrace: Holistic Trajectory-Level Evaluation of LLM Tool Calling for Long-Horizon Financial Tasks](https://arxiv.org/abs/2604.10015)

**<font color=#1a73e8>作者：</font>** Yupeng Cao, Haohang Li, Weijin Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies demonstrate that tool-calling capability enables large language models (LLMs) to interact with external environments for long-horizon financial tasks. While existing benchmarks have begun evaluating financial tool calling, they focus on limited scenarios and rely on call-level metrics that fail to capture trajectory-level reasoning quality. To address this gap, we introduce FinTrace, a benchmark comprising 800 expert-annotated trajectories spanning 34 real-world financial task categories across multiple difficulty levels. FinTrace employs a rubric-based evaluation protocol with nine metrics organized along four axes -- action correctness, execution efficiency, process quality, and output quality -- enabling fine-grained assessment of LLM tool-calling behavior. Our evaluation of 13 LLMs reveals that while frontier models achieve strong tool selection, all models struggle with information utilization and final answer quality, exposing a critical gap between invoking the right tools and reasoning effectively over their outputs. To move beyond diagnosis, we construct FinTrace-Training, the first trajectory-level preference dataset for financial tool-calling, containing 8,196 curated trajectories with tool-augmented contexts and preference pairs. We fine-tune Qwen-3.5-9B using supervised fine-tuning followed by direct preference optimization (DPO) and show that training on FinTrace-Training consistently improves intermediate reasoning metrics, with DPO more effectively suppressing failure modes. However, end-to-end answer quality remains a bottleneck, indicating that trajectory-level improvements do not yet fully propagate to final output quality.

---


### 56. [LVSum: A Benchmark for Timestamp-Aware Long Video Summarization](https://arxiv.org/abs/2604.10024)

**<font color=#1a73e8>作者：</font>** Alkesh Patel, Melis Ozyildirim, Ying-Chang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video summarization presents significant challenges for current multimodal large language models (MLLMs), particularly in maintaining temporal fidelity over extended durations and producing summaries that are both semantically and temporally grounded. In this work, we present LVSum, a human-annotated benchmark designed specifically for evaluating long video summarization with fine-grained temporal alignment. LVSum comprises diverse long-form videos across 13 domains, each paired with human-generated summaries containing precise temporal references. We conduct a comprehensive evaluation of both proprietary and open-source MLLMs on LVSum, assessing performance using newly introduced LLM-based metrics for content relevance and modality coherence, alongside standard evaluation metrics. Our experiments reveal systematic gaps in temporal understanding among existing MLLMs and offer insights that establish a new foundation for advancing temporal reasoning in long video summarization.

---


### 57. [SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://arxiv.org/abs/2604.10027)

**<font color=#1a73e8>作者：</font>** Xu Liu, Guikun Chen, Wenguan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) suffer from hallucination and context forgetting. Prior studies suggest that attention drift is a primary cause of these problems, where LLMs' focus shifts towards newly generated tokens and away from the initial input context. To counteract this, we make use of a related, intrinsic characteristic of LLMs: attention sink -- the tendency to consistently allocate high attention to the very first token (i.e., <BOS>) of a sequence. Concretely, we propose an advanced context anchoring method, SinkTrack, which treats <BOS> as an information anchor and injects key contextual features (such as those derived from the input image or instruction) into its representation. As such, LLM remains anchored to the initial input context throughout the entire generation process. SinkTrack is training-free, plug-and-play, and introduces negligible inference overhead. Experiments demonstrate that SinkTrack mitigates hallucination and context forgetting across both textual (e.g., +21.6% on SQuAD2.0 with Llama3.1-8B-Instruct) and multi-modal (e.g., +22.8% on M3CoT with Qwen2.5-VL-7B-Instruct) tasks. Its consistent gains across different architectures and scales underscore the robustness and generalizability. We also analyze its underlying working mechanism from the perspective of information delivery. Our source code is available at this https URL.

---


### 58. [CoSToM:Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models](https://arxiv.org/abs/2604.10031)

**<font color=#1a73e8>作者：</font>** Mengfan Li, Xuanhua Shi, Yang Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM), the ability to attribute mental states to others, is a hallmark of social intelligence. While large language models (LLMs) demonstrate promising performance on standard ToM benchmarks, we observe that they often fail to generalize to complex task-specific scenarios, relying heavily on prompt scaffolding to mimic reasoning. The critical misalignment between the internal knowledge and external behavior raises a fundamental question: Do LLMs truly possess intrinsic cognition, and can they externalize this internal knowledge into stable, high-quality behaviors? To answer this, we introduce CoSToM (Causal-oriented Steering for ToM alignment), a framework that transitions from mechanistic interpretation to active intervention. First, we employ causal tracing to map the internal distribution of ToM features, empirically uncovering the internal layers' characteristics in encoding fundamental ToM semantics. Building on this insight, we implement a lightweight alignment framework via targeted activation steering within these ToM-critical layers. Experiments demonstrate that CoSToM significantly enhances human-like social reasoning capabilities and downstream dialogue quality.

---


### 59. [On The Application of Linear Attention in Multimodal Transformers](https://arxiv.org/abs/2604.10064)

**<font color=#1a73e8>作者：</font>** Armin Gerami, Seyedehanita Madani, Ramani Duraiswami  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Transformers serve as the backbone for state-of-the-art vision-language models, yet their quadratic attention complexity remains a critical barrier to scalability. In this work, we investigate the viability of Linear Attention (LA) as a high-efficiency alternative within multimodal frameworks. By integrating LA, we reduce the computational overhead from quadratic to linear relative to sequence length while preserving competitive performance. We evaluate our approach across ViT-S/16, ViT-B/16, and ViT-L/16 architectures trained on the LAION-400M dataset, with validation focused on ImageNet-21K zero-shot accuracy. Our systematic evaluation demonstrates that Linear Attention not only yields significant computational savings but also adheres to the same scaling laws as standard softmax attention. These findings position Linear Attention as a robust, scalable solution for next-generation multimodal Transformers tasked with processing increasingly large and complex datasets.

---


### 60. [ASPIRin: Action Space Projection for Interactivity-Optimized Reinforcement Learning in Full-Duplex Speech Language Models](https://arxiv.org/abs/2604.10065)

**<font color=#1a73e8>作者：</font>** Chi-Yuan Hsiao, Ke-Han Lu, Yu-Kuan Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end full-duplex Speech Language Models (SLMs) require precise turn-taking for natural interaction. However, optimizing temporal dynamics via standard raw-token reinforcement learning (RL) degrades semantic quality, causing severe generative collapse and repetition. We propose ASPIRin, an interactivity-optimized RL framework that explicitly decouples when to speak from what to say. Using Action Space Projection, ASPIRin maps the text vocabulary into a coarse-grained binary state (active speech vs. inactive silence). By applying Group Relative Policy Optimization (GRPO) with rule-based rewards, it balances user interruption and response latency. Empirical evaluations show ASPIRin optimizes interactivity across turn-taking, backchanneling, and pause handling. Crucially, isolating timing from token selection preserves semantic coherence and reduces the portion of duplicate n-grams by over 50% compared to standard GRPO, effectively eliminating degenerative repetition.

---


### 61. [Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation](https://arxiv.org/abs/2604.10071)

**<font color=#1a73e8>作者：</font>** Yebo Wu, Han Jin, Zhijiang Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated remarkable reasoning capabilities yet continue to suffer from hallucination, where generated text contradicts visual content. In this paper, we introduce Dual-Anchor Introspective Decoding (DaID), a novel contrastive decoding framework that dynamically calibrates each token generation by mining the model's internal perceptual discrepancies. Specifically, DaID identifies a Spotlight layer to amplify visual factual signals and a Shadow layer to suppress textual inertia. By leveraging visual attention distributions to guide this dual-anchor selection process, our method ensures precise, token-specific adaptation. Experimental results across multiple benchmarks and MLLMs demonstrate that DaID significantly mitigates hallucination while enhancing general reasoning capabilities.

---


### 62. [Why Supervised Fine-Tuning Fails to Learn: A Systematic Study of Incomplete Learning in Large Language Models](https://arxiv.org/abs/2604.10079)

**<font color=#1a73e8>作者：</font>** Chao Xue, Yao Wang, Mengqiao Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) is the standard approach for adapting large language models (LLMs) to downstream tasks. However, we observe a persistent failure mode: even after convergence, models often fail to correctly reproduce a subset of their own supervised training data. We refer to this behavior as the Incomplete Learning Phenomenon(ILP). This paper presents the first systematic study of ILP in LLM fine-tuning. We formalize ILP as post-training failure to internalize supervised instances and demonstrate its prevalence across multiple model families, domains, and datasets. Through controlled analyses, we identify five recurrent sources of incomplete learning: (1) missing prerequisite knowledge in the pre-trained model, (2) conflicts between SFT supervision and pre-training knowledge, (3) internal inconsistencies within SFT data, (4) left-side forgetting during sequential fine-tuning, and (5) insufficient optimization for rare or complex patterns. We introduce a diagnostic-first framework that maps unlearned samples to these causes using observable training and inference signals, and study several targeted mitigation strategies as causal interventions. Experiments on Qwen, LLaMA, and OLMo2 show that incomplete learning is widespread and heterogeneous, and that improvements in aggregate metrics can mask persistent unlearned subsets. The findings highlight the need for fine-grained diagnosis of what supervised fine-tuning fails to learn, and why.

---


### 63. [Active Diffusion Matching: Score-based Iterative Alignment of Cross-Modal Retinal Images](https://arxiv.org/abs/2604.10084)

**<font color=#1a73e8>作者：</font>** Kanggeon Lee, Su Jeong Song, Soochahn Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: The study aims to address the challenge of aligning Standard Fundus Images (SFIs) and Ultra-Widefield Fundus Images (UWFIs), which is difficult due to their substantial differences in viewing range and the amorphous appearance of the retina. Currently, no specialized method exists for this task, and existing image alignment techniques lack accuracy.
Methods: We propose Active Diffusion Matching (ADM), a novel cross-modal alignment method. ADM integrates two interdependent score-based diffusion models to jointly estimate global transformations and local deformations via an iterative Langevin Markov chain. This approach facilitates a stochastic, progressive search for optimal alignment. Additionally, custom sampling strategies are introduced to enhance the adaptability of ADM to given input image pairs.
Results: Comparative experimental evaluations demonstrate that ADM achieves state-of-the-art alignment accuracy. This was validated on two datasets: a private dataset of SFI-UWFI pairs and a public dataset of SFI-SFI pairs, with mAUC improvements of 5.2 and 0.4 points on the private and public datasets, respectively, compared to existing state-of-the-art methods.
Conclusion: ADM effectively bridges the gap in aligning SFIs and UWFIs, providing an innovative solution to a previously unaddressed challenge. The method's ability to jointly optimize global and local alignment makes it highly effective for cross-modal image alignment tasks.
Significance: ADM has the potential to transform the integrated analysis of SFIs and UWFIs, enabling better clinical utility and supporting learning-based image enhancements. This advancement could significantly improve diagnostic accuracy and patient outcomes in ophthalmology.

---


### 64. [Particle Diffusion Matching: Random Walk Correspondence Search for the Alignment of Standard and Ultra-Widefield Fundus Images](https://arxiv.org/abs/2604.10085)

**<font color=#1a73e8>作者：</font>** Kanggeon Lee, Soochahn Lee, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a robust alignment technique for Standard Fundus Images (SFIs) and Ultra-Widefield Fundus Images (UWFIs), which are challenging to align due to differences in scale, appearance, and the scarcity of distinctive features. Our method, termed Particle Diffusion Matching (PDM), performs alignment through an iterative Random Walk Correspondence Search (RWCS) guided by a diffusion model. At each iteration, the model estimates displacement vectors for particle points by considering local appearance, the structural distribution of particles, and an estimated global transformation, enabling progressive refinement of correspondences even under difficult conditions. PDM achieves state-of-the-art performance across multiple retinal image alignment benchmarks, showing substantial improvement on a primary dataset of SFI-UWFI pairs and demonstrating its effectiveness in real-world clinical scenarios. By providing accurate and scalable correspondence estimation, PDM overcomes the limitations of existing methods and facilitates the integration of complementary retinal image modalities. This diffusion-guided search strategy offers a new direction for improving downstream supervised learning, disease diagnosis, and multi-modal image analysis in ophthalmology.

---


### 65. [SEPTQ: A Simple and Effective Post-Training Quantization Paradigm for Large Language Models](https://arxiv.org/abs/2604.10091)

**<font color=#1a73e8>作者：</font>** Han Liu, Haotian Gao, Xiaotong Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable performance in various domains, but they are constrained by massive computational and storage costs. Quantization, an effective technique for compressing models to fit resource-limited devices while preserving generative quality, encompasses two primary methods: quantization aware training (QAT) and post-training quantization (PTQ). QAT involves additional retraining or fine-tuning, thus inevitably resulting in high training cost and making it unsuitable for LLMs. Consequently, PTQ has become the research hotspot in recent quantization methods. However, existing PTQ methods usually rely on various complex computation procedures and suffer from considerable performance degradation under low-bit quantization settings. To alleviate the above issues, we propose a simple and effective post-training quantization paradigm for LLMs, named SEPTQ. Specifically, SEPTQ first calculates the importance score for each element in the weight matrix and determines the quantization locations in a static global manner. Then it utilizes the mask matrix which represents the important locations to quantize and update the associated weights column-by-column until the appropriate quantized weight matrix is obtained. Compared with previous methods, SEPTQ simplifies the post-training quantization procedure into only two steps, and considers the effectiveness and efficiency simultaneously. Experimental results on various datasets across a suite of models ranging from millions to billions in different quantization bit-levels demonstrate that SEPTQ significantly outperforms other strong baselines, especially in low-bit quantization scenarios.

---


### 66. [Mining Attribute Subspaces for Efficient Fine-tuning of 3D Foundation Models](https://arxiv.org/abs/2604.10095)

**<font color=#1a73e8>作者：</font>** Yu Jiang, Hanwen Jiang, Ahmed Abdelkader 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the emergence of 3D foundation models, there is growing interest in fine-tuning them for downstream tasks, where LoRA is the dominant fine-tuning paradigm. As 3D datasets exhibit distinct variations in texture, geometry, camera motion, and lighting, there are interesting fundamental questions: 1) Are there LoRA subspaces associated with each type of variation? 2) Are these subspaces disentangled (i.e., orthogonal to each other)? 3) How do we compute them effectively? This paper provides answers to all these questions. We introduce a robust approach that generates synthetic datasets with controlled variations, fine-tunes a LoRA adapter on each dataset, and extracts a LoRA sub-space associated with each type of variation. We show that these subspaces are approximately disentangled. Integrating them leads to a reduced LoRA subspace that enables efficient LoRA fine-tuning with improved prediction accuracy for downstream tasks. In particular, we show that such a reduced LoRA subspace, despite being derived entirely from synthetic data, generalizes to real datasets. An ablation study validates the effectiveness of the choices in our approach.

---


### 67. [Who Wrote This Line? Evaluating the Detection of LLM-Generated Classical Chinese Poetry](https://arxiv.org/abs/2604.10101)

**<font color=#1a73e8>作者：</font>** Jiang Li, Tian Lan, Shanshan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models (LLMs) has extended text generation tasks into the literary domain. However, AI-generated literary creations has raised increasingly prominent issues of creative authenticity and ethics in literary world, making the detection of LLM-generated literary texts essential and urgent. While previous works have made significant progress in detecting AI-generated text, it has yet to address classical Chinese poetry. Due to the unique linguistic features of classical Chinese poetry, such as strict metrical regularity, a shared system of poetic imagery, and flexible syntax, distinguishing whether a poem is authored by AI presents a substantial challenge. To address these issues, we introduce ChangAn, a benchmark for detecting LLM-generated classical Chinese poetry that containing total 30,664 poems, 10,276 are human-written poems and 20,388 poems are generated by four popular LLMs. Based on ChangAn, we conducted a systematic evaluation of 12 AI detectors, investigating their performance variations across different text granularities and generation strategies. Our findings highlight the limitations of current Chinese text detectors, which fail to serve as reliable tools for detecting LLM-generated classical Chinese poetry. These results validate the effectiveness and necessity of our proposed ChangAn benchmark. Our dataset and code are available at this https URL.

---


### 68. [The Double-Edged Sword of Open-Ended Interaction: How LLM-Driven NPCs Affect Players' Cognitive Load and Gaming Experience](https://arxiv.org/abs/2604.10107)

**<font color=#1a73e8>作者：</font>** Ting-Chen Hsu, Wenran Chen, Jiangxu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines how large language model-driven non-player characters (LLM-NPCs) affect players' cognitive load and gaming experience, with a particular focus on the underlying psychological mechanisms, differences across task scenarios, and the role of individual traits. Conducting a randomized between-subject experiment (N=130) in a self-developed game prototype "Campus Culture Week", we compared player interactions with LLM-NPCs and traditional pre-scripted NPCs across multiple interactive modules. The results showed that LLM-NPCs significantly increased players' cognitive load (p < .001), an effect mediated by factors such as expressive effort and response uncertainty. However, LLM-NPCs did not yield a statistically significant improvement in overall gaming experience (p = .195); while they positively influenced players' perceived autonomy, they exerted a negative influence on system usability and trust. The effects of LLM-NPCs also significantly varied across task scenarios (p < .001), with stronger increases in cognitive load in more open-ended modules such as content creation and relationship building. The influence of individual differences was generally limited, although the personality traits of extraversion (p = .031) and neuroticism (p = .047) demonstrated some predictive power regarding cognitive load. This study provides empirical evidence for understanding the "double-edged sword" effect of LLM-NPCs on player experience, and highlight the importance of scenario-sensitive and user-sensitive design in intelligent NPC systems.

---


### 69. [JARVIS: A Just-in-Time AR Visual Instruction System for Cross-Reality Task Guidance](https://arxiv.org/abs/2604.10108)

**<font color=#1a73e8>作者：</font>** Yusi Sun, Ying Jiang, Jiayin Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many everyday tasks rely on external tutorials such as manuals and videos, requiring users to constantly switch between reading instructions and performing actions, which disrupts workflow and increases cognitive load. Augmented reality (AR) enables in-situ guidance, while recent advances in large language models (LLMs) and vision-language models (VLMs) make it possible to automatically generate such guidance. However, existing AI-powered AR tutorial systems primarily focus on physical procedural tasks and provide limited support for hybrid physical and virtual workspaces. To address this gap, we conduct a formative study of cross-reality tasks and identify key requirements for state awareness and cross-reality coordination. We present JARVIS, a VLM-driven AR instruction system that generates contextual, step-by-step guidance from a single prompt, with real-time state verification and adaptive visual feedback. To inform the system design, we conducted a formative study to understand guidance needs across cross-reality tasks, which we categorize into four types, real-to-real (R2R), real-to-virtual (R2V), virtual-to-real (V2R), and virtual-to-virtual (V2V). A within-subjects study (N=14) across four domains shows JARVIS improves usability, workload, success rate, and visualization effectiveness over baselines.

---


### 70. [CircuitSynth: Reliable Synthetic Data Generation](https://arxiv.org/abs/2604.10114)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The generation of high-fidelity synthetic data is a cornerstone of modern machine learning, yet Large Language Models (LLMs) frequently suffer from hallucinations, logical inconsistencies, and mode collapse when tasked with structured generation. Existing approaches, such as prompting or retrieval-augmented generation, lack the mechanisms to balance linguistic expressivity with formal guarantees regarding validity and coverage. To address this, we propose CircuitSynth, a novel neuro-symbolic framework that decouples semantic reasoning from surface realization. By distilling the reasoning capabilities of a Teacher LLM into a Probabilistic Sentential Decision Diagram (PSDD), CircuitSynth creates a tractable semantic prior that structurally enforces hard logical constraints. Furthermore, we introduce a convex optimization mechanism to rigorously satisfy soft distributional goals. Empirical evaluations across diverse benchmarks demonstrate that CircuitSynth achieves 100% Schema Validity even in complex logic puzzles where unconstrained baselines fail (12.4%) while significantly outperforming state-of-the-art methods in rare-combination coverage.

---


### 71. [A Dual Cross-Attention Graph Learning Framework For Multimodal MRI-Based Major Depressive Disorder Detection](https://arxiv.org/abs/2604.10116)

**<font color=#1a73e8>作者：</font>** Nojod M. Alotaibi, Areej M. Alhothali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Major depressive disorder (MDD) is a prevalent mental disorder associated with complex neurobiological changes that cannot be fully captured using a single imaging modality. The use of multimodal magnetic resonance imaging (MRI) provides a more comprehensive understanding of brain changes by combining structural and functional data. Despite this, the effective integration of these modalities remains challenging. In this study, we propose a dual cross-attention-based multimodal fusion framework that explicitly models bidirectional interactions between structural MRI (sMRI) and resting-state functional MRI (rs-fMRI) representations. The proposed approach is tested on the large-scale REST-meta-MDD dataset using both structural and functional brain atlas configurations. Numerous experiments conducted under a 10-fold stratified cross-validation demonstrated that the proposed fusion algorithm achieves robust and competitive performance across all atlas types. The proposed method consistently outperforms conventional feature-level concatenation for functional atlases, while maintaining comparable performance for structural atlases. The most effective dual cross-attention multimodal model obtained 84.71% accuracy, 86.42% sensitivity, 82.89% specificity, 84.34% precision, and 85.37% F1-score. These findings emphasize the importance of explicitly modeling cross-modal interactions for multimodal neuroimaging-based MDD classification.

---


### 72. [Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities](https://arxiv.org/abs/2604.10135)

**<font color=#1a73e8>作者：</font>** Zhichen Liu, Yongyuan Li, Yang Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers have explored different ways to improve large language models (LLMs)' capabilities via dummy token insertion in contexts. However, existing works focus solely on the dummy tokens themselves, but fail to leverage the inherent sentence-level structure of natural language. This is a critical oversight, as LLMs acquire linguistic capabilities through exposure to human-generated texts, which are inherently structured at the sentence level. Motivated by this gap, we propose an approach that inserts delimiters at sentence boundaries in LLM inputs, which not only integrates dummy tokens into the context, but also facilitates LLMs with sentence-by-sentence processing behavior during reasoning. Two concrete methods: (1). In-context learning and (2). Supervised fine-tuning are experimented using 7B models to 600B Deepseek-V3. Our results demonstrate consistent improvements across various tasks, with notable gains of up to 7.7\% on GSM8k and 12.5\% on DROP. Furthermore, the fine-tuned LLMs can incorporate sentence awareness evidenced by their internal representations. Our work establishes a simple yet effective technique for enhancing LLM's capabilities, offering promising directions for cognitive-inspired LLM enhancement paradigm.

---


### 73. [Nationality encoding in language model hidden states: Probing culturally differentiated representations in persona-conditioned academic text](https://arxiv.org/abs/2604.10151)

**<font color=#1a73e8>作者：</font>** Paul Jackson, Ruizhe Li, Elspeth Edelstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as writing tools and pedagogical resources in English for Academic Purposes, but it remains unclear whether they encode culturally differentiated representations when generating academic text. This study tests whether Gemma-3-4b-it encodes nationality-discriminative information in hidden states when generating research article introductions conditioned by British and Chinese academic personas. A corpus of 270 texts was generated from 45 prompt templates crossed with six persona conditions in a 2 x 3 design. Logistic regression probes were trained on hidden-state activations across all 35 layers, with shuffled-label baselines, a surface-text skyline classifier, cross-family tests, and sentence-level baselines used as controls. Probe-selected token positions were annotated for structural, lexical, and stance features using the Stanza NLP pipeline. The nationality probe reached 0.968 cross-validated accuracy at Layer 18, with perfect held-out classification. Nationality encoding followed a non-monotonic trajectory across layers, with structural effects strongest in the middle to upper network and lexical-domain effects peaking earlier. At high-signal token positions, British-associated patterns showed more postmodification, hedging, boosting, passive voice, and evaluative or process-oriented vocabulary, while Chinese-associated patterns showed more premodification, nominal predicates, and sociocultural or internationalisation vocabulary. However, sentence-level analysis found no significant nationality differences in the full generated surface text. The findings extend probing methodology to a sociolinguistic attribute and have practical implications for EAP and language pedagogy.

---


### 74. [SpecMoE: A Fast and Efficient Mixture-of-Experts Inference via Self-Assisted Speculative Decoding](https://arxiv.org/abs/2604.10152)

**<font color=#1a73e8>作者：</font>** Jehyeon Bang, Eunyeong Cho, Ranggi Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Mixture-of-Experts (MoE) architecture has emerged as a promising approach to mitigate the rising computational costs of large language models (LLMs) by selectively activating parameters. However, its high memory requirements and sub-optimal parameter efficiency pose significant challenges for efficient deployment. Although CPU-offloaded MoE inference systems have been proposed in the literature, they offer limited efficiency, particularly for large batch sizes. In this work, we propose SpecMoE, a memory-efficient MoE inference system based on our self-assisted speculative decoding algorithm. SpecMoE demonstrates the effectiveness of applying speculative decoding to MoE inference without requiring additional model training or fine-tuning. Our system improves inference throughput by up to $4.30\times$, while significantly reducing bandwidth requirements of both memory and interconnect on memory-constrained systems.

---


### 75. [FAITH: Factuality Alignment through Integrating Trustworthiness and Honestness](https://arxiv.org/abs/2604.10189)

**<font color=#1a73e8>作者：</font>** Xiaoning Dong, Chengyan Wu, Yajie Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate factually inaccurate content even if they have corresponding knowledge, which critically undermines their reliability. Existing approaches attempt to mitigate this by incorporating uncertainty in QA prompt during training, but these numerical scores lack the semantic richness for LLM to properly understand its internal states of trustworthiness and honestness, leading to insufficient factuality alignment. We introduce FAITH (Factuality Alignment through Integrating Trustworthiness and Honestness), a post-training framework for factuality alignment that integrates natural-language uncertainty signals with external knowledge. Specifically, we augment training datasets by computing confidence scores and semantic entropy from LLM outputs and mapping them into a knowledge state quadrant that describes the model's internal knowledge possession (trustworthiness) and answering behaviors (honestness) in natural language. Based on this enhanced data, we design a reward function that considers both correctness and uncertainty signals, and fine-tune the LLM using the Proximal Policy Optimization (PPO) algorithm. To further mitigate weakly grounded responses, we design a retrieval-augmented module that retrieves relevant external passages, improving the consistency between internal and external knowledge representations. Extensive experiments on four knowledge-intensive benchmarks demonstrate that FAITH enhances the factual accuracy and truthfulness of LLMs.

---


### 76. [Edu-MMBias: A Three-Tier Multimodal Benchmark for Auditing Social Bias in Vision-Language Models under Educational Contexts](https://arxiv.org/abs/2604.10200)

**<font color=#1a73e8>作者：</font>** Ruijia Li, Mingzi Zhang, Zengyi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models (VLMs) become integral to educational decision-making, ensuring their fairness is paramount. However, current text-centric evaluations neglect the visual modality, leaving an unregulated channel for latent social biases. To bridge this gap, we present Edu-MMBias, a systematic auditing framework grounded in the tri-component model of attitudes from social psychology. This framework diagnoses bias across three hierarchical dimensions: cognitive, affective, and behavioral. Utilizing a specialized generative pipeline that incorporates a self-correct mechanism and human-in-the-loop verification, we synthesize contamination-resistant student profiles to conduct a holistic stress test on state-of-the-art VLMs. Our extensive audit reveals critical, counter-intuitive patterns: models exhibit a compensatory class bias favoring lower-status narratives while simultaneously harboring deep-seated health and racial stereotypes. Crucially, we find that visual inputs act as a safety backdoor, triggering a resurgence of biases that bypass text-based alignment safeguards and revealing a systematic misalignment between latent cognition and final decision-making. The contributions of this paper are available at: this https URL.

---


### 77. [SMFormer: Empowering Self-supervised Stereo Matching via Foundation Models and Data Augmentation](https://arxiv.org/abs/2604.10218)

**<font color=#1a73e8>作者：</font>** Yun Wang, Zhengjie Yang, Jiahao Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent self-supervised stereo matching methods have made significant progress. They typically rely on the photometric consistency assumption, which presumes corresponding points across views share the same appearance. However, this assumption could be compromised by real-world disturbances, resulting in invalid supervisory signals and a significant accuracy gap compared to supervised methods. To address this issue, we propose SMFormer, a framework integrating more reliable self-supervision guided by the Vision Foundation Model (VFM) and data augmentation. We first incorporate the VFM with the Feature Pyramid Network (FPN), providing a discriminative and robust feature representation against disturbance in various scenarios. We then devise an effective data augmentation mechanism that ensures robustness to various transformations. The data augmentation mechanism explicitly enforces consistency between learned features and those influenced by illumination variations. Additionally, it regularizes the output consistency between disparity predictions of strong augmented samples and those generated from standard samples. Experiments on multiple mainstream benchmarks demonstrate that our SMFormer achieves state-of-the-art (SOTA) performance among self-supervised methods and even competes on par with supervised ones. Remarkably, in the challenging Booster benchmark, SMFormer even outperforms some SOTA supervised methods, such as CFNet.

---


### 78. [Cognitive Pivot Points and Visual Anchoring: Unveiling and Rectifying Hallucinations in Multimodal Reasoning Models](https://arxiv.org/abs/2604.10219)

**<font color=#1a73e8>作者：</font>** Zhe Qian, Yanbiao Ma, Zhuohan Ouyang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Reasoning Models (MLRMs) have achieved remarkable strides in visual reasoning through test time compute scaling, yet long chain reasoning remains prone to hallucinations. We identify a concerning phenomenon termed the Reasoning Vision Truth Disconnect (RVTD): hallucinations are strongly correlated with cognitive bifurcation points that often exhibit high entropy states. We attribute this vulnerability to a breakdown in visual semantic anchoring, localized within the network's intermediate layers; specifically, during these high uncertainty transitions, the model fails to query visual evidence, reverting instead to language priors. Consequently, we advocate a shift from solely outcome level supervision to augmenting it with fine grained internal attention guidance. To this end, we propose V-STAR (Visual Structural Training with Attention Reinforcement), a lightweight, holistic training paradigm designed to internalize visually aware reasoning capabilities. Central to our approach is the Hierarchical Visual Attention Reward (HVAR), integrated within the GRPO framework. Upon detecting high entropy states, this mechanism dynamically incentivizes visual attention across critical intermediate layers, thereby anchoring the reasoning process back to the visual input. Furthermore, we introduce the Forced Reflection Mechanism (FRM), a trajectory editing strategy that disrupts cognitive inertia by triggering reflection around high entropy cognitive bifurcation points and encouraging verification of subsequent steps against the visual input, thereby translating external debiasing interventions into an intrinsic capability for hallucination mitigation.

---


### 79. [SVSR: A Self-Verification and Self-Rectification Paradigm for Multimodal Reasoning](https://arxiv.org/abs/2604.10228)

**<font color=#1a73e8>作者：</font>** Zhe Qian, Nianbing Su, Zhonghua Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current multimodal models often suffer from shallow reasoning, leading to errors caused by incomplete or inconsistent thought processes. To address this limitation, we propose Self-Verification and Self-Rectification (SVSR), a unified framework that explicitly integrates self-verification and self-rectification into the model's reasoning pipeline, substantially improving robustness and reliability in complex visual understanding and multimodal reasoning tasks. SVSR is built on a novel three-stage training paradigm. First, we construct a high-quality unified preference dataset by refining reasoning traces from pre-trained vision-language models, incorporating both forward and backward reasoning to embed self-reflective signals. Second, we perform cold-start supervised fine-tuning on this dataset to learn structured, multi-step reasoning behaviors. Third, we apply a Semi-online Direct Preference Optimization (Semi-online DPO) process, continuously augmenting the training corpus with high-quality, model-generated reasoning traces filtered by a powerful teacher VLM. This pipeline enables the model to learn, elicit, and refine its ability to self-verify and self-rectify. Extensive experiments across diverse benchmarks demonstrate that SVSR improves reasoning accuracy and enables stronger generalization to unseen tasks and question types. Notably, once trained with explicit self-reflective reasoning, the model also exhibits improved implicit reasoning ability, outperforming strong baselines even when no explicit reasoning traces are provided. These results highlight the potential of SVSR for building more dependable, introspective, and cognitively aligned multimodal systems.

---


### 80. [Adapting 2D Multi-Modal Large Language Model for 3D CT Image Analysis](https://arxiv.org/abs/2604.10233)

**<font color=#1a73e8>作者：</font>** Yang Yu, Dunyuan Xu, Yaoqian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D medical image analysis is of great importance in disease diagnosis and treatment. Recently, multimodal large language models (MLLMs) have exhibited robust perceptual capacity, strong cross-modal alignment, and promising generalizability. Therefore, they have great potential to improve the performance of medical report generation (MRG) and medical visual question answering (MVQA), which serve as two important tasks in clinical scenarios. However, due to the scarcity of 3D medical images, existing 3D medical MLLMs suffer from insufficiently pretrained vision encoder and inability to extract customized image features for different kinds of tasks. In this paper, we propose to first transfer a 2D MLLM, which is well trained with 2D natural images, to support 3D medical volumetric inputs while reusing all of its pre-trained parameters. To enable the vision encoder to extract tailored image features for various tasks, we then design a Text-Guided Hierarchical MoE (TGH-MoE) framework, which can distinguish tasks under the guidance of the text prompt. Furthermore, we propose a two-stage training strategy to learn both task-shared and task-specific image features. As demonstrated empirically, our method outperforms existing 3D medical MLLMs in both MRG and MVQA tasks. Our code will be released once this paper is accepted.

---


### 81. [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/abs/2604.10235)

**<font color=#1a73e8>作者：</font>** Qiujiang Chen, Jing Xiong, Chenyang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic code tasks such as fault localization and patch generation require processing long codebases under tight memory constraints, where the Key-Value (KV) cache becomes the primary inference bottleneck. Existing compression methods rely exclusively on attention signals to estimate token importance, systematically discarding structurally critical tokens such as call sites, branch conditions, and assignments that are essential for code understanding. We present CodeComp, a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors extracted by Joern. Across bug localization and code generation benchmarks, CodeComp consistently outperforms attention-only compression baselines under equal memory budgets, recovering the majority of full-context accuracy under aggressive KV cache compression, while matching the patch generation quality of uncompressed full-context inference and integrating seamlessly into SGLang-based agentic coding pipelines without model modification.

---


### 82. [MedVeriSeg: Teaching MLLM-Based Medical Segmentation Models to Verify Query Validity Without Extra Training](https://arxiv.org/abs/2604.10242)

**<font color=#1a73e8>作者：</font>** Ziqian Lu, Qinyue Tong, Jun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in MLLM-based medical image segmentation, existing LISA-like methods cannot reliably reject false queries and often produce hallucinated segmentation masks for absent targets. This limitation reduces practical reliability in both medical education and clinical use. In this work, we propose MedVeriSeg, a training-free verification framework that equips LISA-like medical segmentation models with the ability to identify and reject false queries which contain non-existent targets. Our key observation is that the similarity map between the [SEG] token feature and MLLM image features exhibits markedly different distribution patterns for true and false queries. Based on this, we introduce a Similarity Response Quality Scoring Module that characterizes the similarity map from three aspects: strength, compactness, and purity, producing an initial target-existence prediction. We further incorporate qualitative visual evidence by using GPT-4o to jointly assess the similarity heatmap and the results of Similarity Response Quality Scoring Module for final verification. Experiments on a small-scale benchmark constructed from SA-Med2D-20M show that MedVeriSeg effectively rejects false-query segmentation requests while maintaining reliable recognition of true queries.

---


### 83. [The Amazing Agent Race: Strong Tool Users, Weak Navigators](https://arxiv.org/abs/2604.10261)

**<font color=#1a73e8>作者：</font>** Zae Myung Kim, Dongseok Lee, Jaehyung Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing tool-use benchmarks for LLM agents are overwhelmingly linear: our analysis of six benchmarks shows 55 to 100% of instances are simple chains of 2 to 5 steps. We introduce The Amazing Agent Race (AAR), a benchmark featuring directed acyclic graph (DAG) puzzles (or "legs") with fork-merge tool chains. We release 1,400 instances across two variants: sequential (800 legs) and compositional (600 DAG legs). Agents must navigate Wikipedia, execute multi-step tool chains, and aggregate results into a verifiable answer. Legs are procedurally generated from Wikipedia seeds across four difficulty levels with live-API validation. Three complementary metrics (finish-line accuracy, pit-stop visit rate, and roadblock completion rate) separately diagnose navigation, tool-use, and arithmetic failures. Evaluating three agent frameworks on 1,400 legs, the best achieves only 37.2% accuracy. Navigation errors dominate (27 to 52% of trials) while tool-use errors remain below 17%, and agent architecture matters as much as model scale (Claude Code matches Codex CLI at 37% with 6x fewer tokens). The compositional structure of AAR reveals that agents fail not at calling tools but at navigating to the right pages, a blind spot invisible to linear benchmarks. The project page can be accessed at: this https URL

---


### 84. [TimeSeriesExamAgent: Creating Time Series Reasoning Benchmarks at Scale](https://arxiv.org/abs/2604.10291)

**<font color=#1a73e8>作者：</font>** Malgorzata Gwiazda, Yifu Cai, Mononito Goswami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown promising performance in time series modeling tasks, but do they truly understand time series data? While multiple benchmarks have been proposed to answer this fundamental question, most are manually curated and focus on narrow domains or specific skill sets. To address this limitation, we propose scalable methods for creating comprehensive time series reasoning benchmarks that combine the flexibility of templates with the creativity of LLM agents. We first develop TimeSeriesExam, a multiple-choice benchmark using synthetic time series to evaluate LLMs across five core reasoning categories: pattern recognitionnoise understandingsimilarity analysisanomaly detection, and causality. Then, with TimeSeriesExamAgent, we scale our approach by automatically generating benchmarks from real-world datasets spanning healthcare, finance and weather domains. Through multi-dimensional quality evaluation, we demonstrate that our automatically generated benchmarks achieve diversity comparable to manually curated alternatives. However, our experiments reveal that LLM performance remains limited in both abstract time series reasoning and domain-specific applications, highlighting ongoing challenges in enabling effective time series understanding in these models. TimeSeriesExamAgent is available at this https URL.

---


### 85. [FashionMV: Product-Level Composed Image Retrieval with Multi-View Fashion Data](https://arxiv.org/abs/2604.10297)

**<font color=#1a73e8>作者：</font>** Peng Yuan, Bingyin Mei, Hui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) retrieves target images using a reference image paired with modification text. Despite rapid advances, all existing methods and datasets operate at the image level -- a single reference image plus modification text in, a single target image out -- while real e-commerce users reason about products shown from multiple viewpoints. We term this mismatch View Incompleteness and formally define a new Multi-View CIR task that generalizes standard CIR from image-level to product-level retrieval. To support this task, we construct FashionMV, the first large-scale multi-view fashion dataset for product-level CIR, comprising 127K products, 472K multi-view images, and over 220K CIR triplets, built through a fully automated pipeline leveraging large multimodal models. We further propose ProCIR (Product-level Composed Image Retrieval), a modeling framework built upon a multimodal large language model that employs three complementary mechanisms -- two-stage dialogue, caption-based alignment, and chain-of-thought guidance -- together with an optional supervised fine-tuning (SFT) stage that injects structured product knowledge prior to contrastive training. Systematic ablation across 16 configurations on three fashion benchmarks reveals that: (1) alignment is the single most critical mechanism; (2) the two-stage dialogue architecture is a prerequisite for effective alignment; and (3) SFT and chain-of-thought serve as partially redundant knowledge injection paths. Our best 0.8B-parameter model outperforms all baselines, including general-purpose embedding models 10x its size. The dataset, model, and code are publicly available at this https URL.

---


### 86. [Seeing No Evil: Blinding Large Vision-Language Models to Safety Instructions via Adversarial Attention Hijacking](https://arxiv.org/abs/2604.10299)

**<font color=#1a73e8>作者：</font>** Jingru Li, Wei Ren, Tianqing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) rely on attention-based retrieval of safety instructions to maintain alignment during generation. Existing attacks typically optimize image perturbations to maximize harmful output likelihood, but suffer from slow convergence due to gradient conflict between adversarial objectives and the model's safety-retrieval mechanism. We propose Attention-Guided Visual Jailbreaking, which circumvents rather than overpowers safety alignment by directly manipulating attention patterns. Our method introduces two simple auxiliary objectives: (1) suppressing attention to alignment-relevant prefix tokens and (2) anchoring generation on adversarial image features. This simple yet effective push-pull formulation reduces gradient conflict by 45% and achieves 94.4% attack success rate on Qwen-VL (vs. 68.8% baseline) with 40% fewer iterations. At tighter perturbation budgets ($\epsilon=8/255$), we maintain 59.0% ASR compared to 45.7% for standard methods. Mechanistic analysis reveals a failure mode we term safety blindness: successful attacks suppress system-prompt attention by 80%, causing models to generate harmful content not by overriding safety rules, but by failing to retrieve them.

---


### 87. [Comparative Analysis of Large Language Models in Healthcare](https://arxiv.org/abs/2604.10316)

**<font color=#1a73e8>作者：</font>** Subin Santhosh, Farwa Abbas, Hussain Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Large Language Models (LLMs) are transforming artificial intelligence applications in healthcare due to their ability to understand, generate, and summarize complex medical text. They offer valuable support to clinicians, researchers, and patients, yet their deployment in high-stakes clinical environments raises critical concerns regarding accuracy, reliability, and patient safety. Despite substantial attention in recent years, standardized benchmarking of LLMs for medical applications has been limited. Objective: This study addresses the need for a standardized comparative evaluation of LLMs in medical settings. Method: We evaluate multiple models, including ChatGPT, LLaMA, Grok, Gemini, and ChatDoctor, on core medical tasks such as patient note summarization and medical question answering, using the open-access datasets, MedMCQA, PubMedQA, and Asclepius, and assess performance through a combination of linguistic and task-specific metrics. Results: The results indicate that domain-specific models, such as ChatDoctor, excel in contextual reliability, producing medically accurate and semantically aligned text, whereas general-purpose models like Grok and LLaMA perform better in structured question-answering tasks, demonstrating higher quantitative accuracy. This highlights the complementary strengths of domain-specific and general-purpose LLMs depending on the medical task. Conclusion: Our findings suggest that LLMs can meaningfully support medical professionals and enhance clinical decision-making; however, their safe and effective deployment requires adherence to ethical standards, contextual accuracy, and human oversight in relevant cases. These results underscore the importance of task-specific evaluation and cautious integration of LLMs into healthcare workflows.

---


### 88. [From GPT-3 to GPT-5: Mapping their capabilities, scope, limitations, and consequences](https://arxiv.org/abs/2604.10332)

**<font color=#1a73e8>作者：</font>** Hina Afridi, Habib Ullah, Sultan Daud Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the progress of the GPT family from GPT-3 through GPT-3.5, GPT-4, GPT-4 Turbo, GPT-4o, GPT-4.1, and the GPT-5 family. Our work is comparative rather than merely historical. We investigates how the family evolved in technical framing, user interaction, modality, deployment architecture, and governance viewpoint. The work focuses on five recurring themes: technical progression, capability changes, deployment shifts, persistent limitations, and downstream consequences. In term of research design, we consider official technical reports, system cards, API and model documentation, product announcements, release notes, and peer-reviewed secondary studies. A primary assertion is that later GPT generations should not be interpreted only as larger or more accurate language models. Instead, the family evolves from a scaled few-shot text predictor into a set of aligned, multimodal, tool-oriented, long-context, and increasingly workflow-integrated systems. This development complicates simple model-to-model comparison because product routing, tool access, safety tuning, and interface design become part of the effective system. Across generations, several limitations remain unchanged: hallucination, prompt sensitivity, benchmark fragility, uneven behavior across domains and populations, and incomplete public transparency about architecture and training. However, the family has evolved software development, educational practice, information work, interface design, and discussions of frontier-model governance. We infer that the transition from GPT-3 to GPT-5 is best understood not only as an improvement in model capability, but also as a broader reformulation of what a deployable AI system is, how it is evaluated, and where responsibility should be located when such systems are used at scale.

---


### 89. [Zero-shot World Models Are Developmentally Efficient Learners](https://arxiv.org/abs/2604.10333)

**<font color=#1a73e8>作者：</font>** Khai Loong Aw, Klemen Kotar, Wanhee Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Young children demonstrate early abilities to understand their physical world, estimating depth, motion, object coherence, interactions, and many other aspects of physical scene understanding. Children are both data-efficient and flexible cognitive systems, creating competence despite extremely limited training data, while generalizing to myriad untrained tasks -- a major challenge even for today's best AI systems. Here we introduce a novel computational hypothesis for these abilities, the Zero-shot Visual World Model (ZWM). ZWM is based on three principles: a sparse temporally-factored predictor that decouples appearance from dynamics; zero-shot estimation through approximate causal inference; and composition of inferences to build more complex abilities. We show that ZWM can be learned from the first-person experience of a single child, rapidly generating competence across multiple physical understanding benchmarks. It also broadly recapitulates behavioral signatures of child development and builds brain-like internal representations. Our work presents a blueprint for efficient and flexible learning from human-scale data, advancing both a computational account for children's early physical understanding and a path toward data-efficient AI systems.

---


### 90. [Adaptive Multi-Expert Reasoning via Difficulty-Aware Routing and Uncertainty-Guided Aggregation](https://arxiv.org/abs/2604.10335)

**<font color=#1a73e8>作者：</font>** Mohamed Ehab, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong performance in math reasoning benchmarks, but their performance varies inconsistently across problems with varying levels of difficulty. This paper describes Adaptive Multi-Expert Reasoning (AMR), a framework that focuses on problem complexity by reasoning with dynamically adapted strategies. An agile routing system that focuses on problem text predicts problems' difficulty and uncertainty and guides a reconfigurable sampling mechanism to manage the breadth of generation. Three specialized experts create candidate responses, which are modified during multiple correction and finalization phases. A neural verifier assesses the correctness of responses, while a clustering-based aggregation technique identifies the final candidate answer based on a combination of consensus and answer quality. When evaluated on the GSM8K dataset, AMR achieved 75.28% accuracy while only using the original training data. This result outperformed the majority of comparable 7B models that were trained on synthetic data. This showcases that models using difficulty-based routing and uncertainty-driven aggregation are efficient and effective in improving math reasoning models' robustness.

---


### 91. [VeriTrans: Fine-Tuned LLM-Assisted NL-to-PL Translation via a Deterministic Neuro-Symbolic Pipeline](https://arxiv.org/abs/2604.10341)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Dheeraj Kodakandla, Kushagra Srivastva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> \textbf{VeriTrans} is a reliability-first ML system that compiles natural-language requirements into solver-ready logic with validator-gated reliability. The pipeline integrates an instruction-tuned NL$\!\to\!$PL translator, round-trip reconstruction (PL$\!\to\!$NL) used as a high-precision acceptance gate, and canonical PL$\!\to\!$CNF compilation, all executed via fixed API configuration (temperature$=0$; fine-tuning runs use seed$=42$) and per-item artifact logging (prompts, outputs, hashes) to support auditability and replay-driven debugging. On \textbf{SatBench} (2{,}100 specifications), VeriTrans achieves 94.46\% SAT/UNSAT correctness and 87.73\% median round-trip similarity. Compact fine-tuning on 100--150 curated examples improves fidelity by about 1--1.5\,pp without increasing latency (mean 25.8\,s/spec on our 201-spec runtime subset). A thresholded acceptance policy on the round-trip score exposes a reliability--coverage knob: at $\tau{=}75$, roughly 68\% of items are retained with $\sim$94\% correctness on the accepted set. Validator overhead contributes $<15\%$ of end-to-end runtime, and all prompts/responses and timing metadata are logged to enable replay-driven debugging and regression testing. By separating learned translation from symbolic verification and enforcing deterministic, validator-gated acceptance, VeriTrans turns NL$\!\to\!$logic front-ends into auditable, reproducible components for reliability-critical workflows.

---


### 92. [WaterAdmin: Orchestrating Community Water Distribution Optimization via AI Agents](https://arxiv.org/abs/2604.10343)

**<font color=#1a73e8>作者：</font>** Jiaqi Wen, Pingbo Tang, Shaolei Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the operation of community water systems, where pumps and valves must be scheduled to reliably meet water demands while minimizing energy consumption. While existing optimization-based methods are effective under well-modeled environments, real-world community scenarios exhibit highly dynamic contexts-such as human activities, weather variations, etc-that significantly affect water demand patterns and operational targets across different zones. Traditional optimization approaches struggle to aggregate and adapt to such heterogeneous and rapidly evolving contextual information in real time. While Large Language Model (LLM) agents offer strong capabilities for understanding heterogeneous community context, they are not suitable for directly producing reliable real-time control actions. To address these challenges, we propose a bi-level AI-agent-based framework, WaterAdmin, which integrates LLM-based community context abstraction at the upper level with optimization-based operational control at the lower level. This design leverages the complementary strengths of both paradigms to enable adaptive and reliable operation. We implement WaterAdmin on the hydraulic simulation platform EPANET and demonstrate superior performance in maintaining pressure reliability and reducing energy consumption under highly dynamic community contexts.

---


### 93. [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents](https://arxiv.org/abs/2604.10352)

**<font color=#1a73e8>作者：</font>** Mofasshara Rafique, Laurent Bindschaedler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stateful tool-using LLM agents treat the context window as working memory, yet today's agent harnesses manage residency and durability as best-effort, causing recurring failures: lost state after compaction, bypassed flushes on reset, and destructive writeback. We present \textsc{ClawVM}, a virtual memory layer that manages state as typed pages with minimum-fidelity invariants, multi-resolution representations under a token budget, and validated writeback at every lifecycle boundary. Because the harness already assembles prompts, mediates tools, and observes lifecycle events, it is the natural enforcement point; placing the contract there makes residency and durability deterministic and auditable. Across synthetic workloads, 12 real-session traces, and adversarial stress tests, \textsc{ClawVM} eliminates all policy-controllable faults whenever the minimum-fidelity set fits within the token budget, confirmed by an offline oracle, and adds median <50 microseconds of policy-engine overhead per turn.

---


### 94. [Agentic Video Generation: From Text to Executable Event Graphs via Tool-Constrained LLM Planning](https://arxiv.org/abs/2604.10383)

**<font color=#1a73e8>作者：</font>** Nicolae Cudlenco, Mihai Masala, Marius Leordeanu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multi-agent video generation systems use LLM agents to orchestrate neural video generators, producing visually impressive but semantically unreliable outputs with no ground truth annotations. We present an agentic system that inverts this paradigm: instead of generating pixels, the LLM constructs a formal Graph of Events in Space and Time (GEST) -- a structured specification of actors, actions, objects, and temporal constraints -- which is then executed deterministically in a 3D game engine. A staged LLM refinement pipeline fails entirely at this task (0 of 50 attempts produce an executable specification), motivating a fundamentally different architecture based on a separation of concerns: the LLM handles narrative planning through natural language reasoning, while a programmatic state backend enforces all simulator constraints through validated tool calls, guaranteeing that every generated specification is executable by construction. The system uses a hierarchical two-agent architecture -- a Director that plans the story and a Scene Builder that constructs individual scenes through a round-based state machine -- with dedicated Relation Subagents that populate the logical and semantic edge types of the GEST formalism that procedural generation leaves empty, making this the first approach to exercise the full expressive capacity of the representation. We evaluate in two stages: autonomous generation against procedural baselines via a 3-model LLM jury, where agentic narratives win 79% of text and 74% of video comparisons; and seeded generation where the same text is given to our system, VEO 3.1, and WAN 2.2, with human annotations showing engine-generated videos substantially outperform neural generators on physical validity (58% vs 25% and 20%) and semantic alignment (3.75/5 vs 2.33 and 1.50).

---


### 95. [TrajOnco: a multi-agent framework for temporal reasoning over longitudinal EHR for multi-cancer early detection](https://arxiv.org/abs/2604.10386)

**<font color=#1a73e8>作者：</font>** Sihang Zeng, Young Won Kim, Wilson Lau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of cancer risk from longitudinal electronic health records (EHRs) could support earlier detection and improved care, but modeling such complex patient trajectories remains challenging. We present TrajOnco, a training-free, multi-agent large language model (LLM) framework designed for scalable multi-cancer early detection. Using a chain-of-agents architecture with long-term memory, TrajOnco performs temporal reasoning over sequential clinical events to generate patient-level summaries, evidence-linked rationales, and predicted risk scores. We evaluated TrajOnco on de-identified Truveta EHR data across 15 cancer types using matched case-control cohorts, predicting risk of cancer diagnosis at 1 year. In zero-shot evaluation, TrajOnco achieved AUROCs of 0.64-0.80, performing comparably to supervised machine learning in a lung cancer benchmark while demonstrating better temporal reasoning than single-agent LLMs. The multi-agent design also enabled effective temporal reasoning with smaller-capacity models such as GPT-4.1-mini. The fidelity of TrajOnco's output was validated through human evaluation. Furthermore, TrajOnco's interpretable reasoning outputs can be aggregated to reveal population-level risk patterns that align with established clinical knowledge. These findings highlight the potential of multi-agent LLMs to execute interpretable temporal reasoning over longitudinal EHRs, advancing both scalable multi-cancer early detection and clinical insight generation.

---


### 96. [NameBERT: Scaling Name-Based Nationality Classification with LLM-Augmented Open Academic Data](https://arxiv.org/abs/2604.10401)

**<font color=#1a73e8>作者：</font>** Cong Ming, Ruixin Shi, Yifan Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inferring nationality from personal names is a critical capability for equity and bias monitoring, personalization, and a valuable tool in biomedical and sociological research. However, existing name-based nationality classifiers are typically trained on relatively small or source-specific labeled datasets, which can introduce coverage gaps and limit performance for underrepresented countries. While large language models (LLMs) demonstrate strong zero-shot performance for name-based nationality prediction, their computational cost and latency make them impractical for real-time, large-scale deployment. In this work, we created a large-scale name-nationality dataset from the Open Academic Graph (OAG) and introduce a framework that leverages LLMs as dataset enrichers rather than inference engines. We augment low-resource countries with LLM-generated names and evaluate on real and synthetic-tail test sets. We find that augmentation produces large gains when evaluation includes synthetic tail names and still offers a modest lift on tail-country metrics otherwise. Overall, NameBERT models achieve significantly higher accuracy than state-of-the-art baselines across both in- and out-of-domain tasks, while remaining efficient for large-scale inference compared to LLMs.

---


### 97. [Latent Instruction Representation Alignment: defending against jailbreaks, backdoors and undesired knowledge in LLMs](https://arxiv.org/abs/2604.10403)

**<font color=#1a73e8>作者：</font>** Eric Easley, Sebastian Farquhar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address jailbreaks, backdoors, and unlearning for large language models (LLMs). Unlike prior work, which trains LLMs based on their actions when given malign instructions, our method specifically trains the model to change how it interprets instructions. Our method, Latent Instruction Representation Alignment (LIRA), greatly improves generalization. We further boost generalization through an internally adversarial training algorithm. Our methods block over 99% of PEZ jailbreak attacks; remove a challenging insecure code backdoor; and achieve optimal forgetting on WMDP cyber with negligible loss of benign capabilities.

---


### 98. [CWCD: Category-Wise Contrastive Decoding for Structured Medical Report Generation](https://arxiv.org/abs/2604.10410)

**<font color=#1a73e8>作者：</font>** Shantam Srivastava, Mahesh Bhosale, David Doermann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpreting chest X-rays is inherently challenging due to the overlap between anatomical structures and the subtle presentation of many clinically significant pathologies, making accurate diagnosis time-consuming even for experienced radiologists. Recent radiology-focused foundation models, such as LLaVA-Rad and Maira-2, have positioned multi-modal large language models (MLLMs) at the forefront of automated radiology report generation (RRG). However, despite these advances, current foundation models generate reports in a single forward pass. This decoding strategy diminishes attention to visual tokens and increases reliance on language priors as generation proceeds, which in turn introduces spurious pathology co-occurrences in the generated reports. To mitigate these limitations, we propose Category-Wise Contrastive Decoding (CWCD), a novel and modular framework designed to enhance structured radiology report generation (SRRG). Our approach introduces category-specific parameterization and generates category-wise reports by contrasting normal X-rays with masked X-rays using category-specific visual prompts. Experimental results demonstrate that CWCD consistently outperforms baseline methods across both clinical efficacy and natural language generation metrics. An ablation study further elucidates the contribution of each architectural component to overall performance.

---


### 99. [CARE-ECG: Causal Agent-based Reasoning for Explainable and Counterfactual ECG Interpretation](https://arxiv.org/abs/2604.10420)

**<font color=#1a73e8>作者：</font>** Elahe Khatibi, Ziyu Wang, Ankita Sharma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) enable waveform-to-text ECG interpretation and interactive clinical questioning, yet most ECG-LLM systems still rely on weak signal-text alignment and retrieval without explicit physiological or causal structure. This limits grounding, temporal reasoning, and counterfactual "what-if" analysis central to clinical decision-making. We propose CARE-ECG, a causally structured ECG-language reasoning framework that unifies representation learning, diagnosis, and explanation in a single pipeline. CARE-ECG encodes multi-lead ECGs into temporally organized latent biomarkers, performs causal graph inference for probabilistic diagnosis, and supports counterfactual assessment via structural causal models. To improve faithfulness, CARE-ECG grounds language outputs through causal retrieval-augmented generation and a modular agentic pipeline that integrates history, diagnosis, and response with verification. Across multiple ECG benchmarks and expert QA settings, CARE-ECG improves diagnostic accuracy and explanation faithfulness while reducing hallucinations (e.g., 0.84 accuracy on Expert-ECG-QA and 0.76 on SCP-mapped PTB-XL under GPT-4). Overall, CARE-ECG provides traceable reasoning by exposing key latent drivers, causal evidence paths, and how alternative physiological states would change outcomes.

---


### 100. [CodaRAG: Connecting the Dots with Associativity Inspired by Complementary Learning](https://arxiv.org/abs/2604.10426)

**<font color=#1a73e8>作者：</font>** Cheng-Yen Li, Xuanjun Chen, Claire Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) struggle with knowledge-intensive tasks due to hallucinations and fragmented reasoning over dispersed information. While Retrieval-Augmented Generation (RAG) grounds generation in external sources, existing methods often treat evidence as isolated units, failing to reconstruct the logical chains that connect these dots. Inspired by Complementary Learning Systems (CLS), we propose CodaRAG, a framework that evolves retrieval from passive lookup into active associative discovery. CodaRAG operates via a three-stage pipeline: (1) Knowledge Consolidation to unify fragmented extractions into a stable memory substrate; (2) Associative Navigation to traverse the graph via multi-dimensional pathways-semantic, contextualized, and functional-explicitly recovering dispersed evidence chains; and (3) Interference Elimination to prune hyper-associative noise, ensuring a coherent, high-precision reasoning context. On GraphRAG-Bench, CodaRAG achieves absolute gains of 7-10% in retrieval recall and 3-11% in generation accuracy. These results demonstrate CodaRAG's superior ability to systematically robustify associative evidence retrieval for factual, reasoning, and creative tasks.

---


### 101. [VeriSim: A Configurable Framework for Evaluating Medical AI Under Realistic Patient Noise](https://arxiv.org/abs/2604.10441)

**<font color=#1a73e8>作者：</font>** Sina Mansouri, Mohit Marvania, Vibhavari Ashok Shihorkar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical large language models (LLMs) achieve impressive performance on standardized benchmarks, yet these evaluations fail to capture the complexity of real clinical encounters where patients exhibit memory gaps, limited health literacy, anxiety, and other communication barriers. We introduce VeriSim, a truth-preserving patient simulation framework that injects controllable, clinically evidence-grounded noise into patient responses while maintaining strict adherence to medical ground truth through a hybrid UMLS-LLM verification mechanism. Our framework operationalizes six noise dimensions derived from peer-reviewed medical communication literature, capturing authentic clinical phenomena such as patient recall limitations, health literacy barriers, and stigma-driven non-disclosure. Experiments across seven open-weight LLMs reveal that all models degrade significantly under realistic patient noise, with diagnostic accuracy dropping 15-25% and conversation length increasing 34-55%. Notably, smaller models (7B) show 40% greater degradation than larger models (70B+), while medical fine-tuning on standard corpora provides limited robustness benefits against patient communication noise. Evaluation by board-certified clinicians demonstrates high-quality simulation with strong inter-annotator agreement (kappa > 0.80), while LLM-as-a-Judge serves as a validated auxiliary evaluator achieving comparable reliability for scalable assessment. Our results highlight a critical Sim-to-Real gap in current medical AI. We release VeriSim as an open-source noise-injection framework, establishing a rigorous testbed for evaluating clinical robustness.

---


### 102. [Parameter Efficient Fine-tuning for Domain-specific Gastrointestinal Disease Recognition](https://arxiv.org/abs/2604.10451)

**<font color=#1a73e8>作者：</font>** Sanjaya Poudel, Nikita Kunwor, Raj Simkhada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advancements in the field of medical image analysis with the use of pretrained foundation models, the issue of distribution shifts between cross-source images largely remains adamant. To circumvent that issue, investigators generally train a separate model for each source. However, this method becomes expensive when we fully fine-tune pretrained large models for a single dataset, as we must store multiple copies of those models. Thus, in this work, we propose using a low-rank adaptation (LoRA) module for fine-tuning downstream classification tasks. LoRAs learn lightweight task-specific low-rank matrices that perturb pretrained weights to optimize those downstream tasks. For gastrointestinal tract diseases, they exhibit significantly better results than end-to-end finetuning with improved parameter efficiency. Code is available at: this http URL.

---


### 103. [EviCare: Enhancing Diagnosis Prediction with Deep Model-Guided Evidence for In-Context Reasoning](https://arxiv.org/abs/2604.10455)

**<font color=#1a73e8>作者：</font>** Hengyu Zhang, Xuyun Zhang, Pengxiang Zhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled promising progress in diagnosis prediction from electronic health records (EHRs). However, existing LLM-based approaches tend to overfit to historically observed diagnoses, often overlooking novel yet clinically important conditions that are critical for early intervention. To address this, we propose EviCare, an in-context reasoning framework that integrates deep model guidance into LLM-based diagnosis prediction. Rather than prompting LLMs directly with raw EHR inputs, EviCare performs (1) deep model inference for candidate selection, (2) evidential prioritization for set-based EHRs, and (3) relational evidence construction for novel diagnosis prediction. These signals are then composed into an adaptive in-context prompt to guide LLM reasoning in an accurate and interpretable manner. Extensive experiments on two real-world EHR benchmarks (MIMIC-III and MIMIC-IV) demonstrate that EviCare achieves significant performance gains, which consistently outperforms both LLM-only and deep model-only baselines by an average of 20.65\% across precision and accuracy metrics. The improvements are particularly notable in challenging novel diagnosis prediction, yielding average improvements of 30.97\%.

---


### 104. [Toward Accountable AI-Generated Content on Social Platforms: Steganographic Attribution and Multimodal Harm Detection](https://arxiv.org/abs/2604.10460)

**<font color=#1a73e8>作者：</font>** Xinlei Guan, David Arosemena, Tejaswi Dhandu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of generative AI has introduced new challenges in content moderation and digital forensics. In particular, benign AI-generated images can be paired with harmful or misleading text, creating difficult-to-detect misuse. This contextual misuse undermines the traditional moderation framework and complicates attribution, as synthetic images typically lack persistent metadata or device signatures. We introduce a steganography enabled attribution framework that embeds cryptographically signed identifiers into images at creation time and uses multimodal harmful content detection as a trigger for attribution verification. Our system evaluates five watermarking methods across spatial, frequency, and wavelet domains. It also integrates a CLIP-based fusion model for multimodal harmful-content detection. Experiments demonstrate that spread-spectrum watermarking, especially in the wavelet domain, provides strong robustness under blur distortions, and our multimodal fusion detector achieves an AUC-ROC of 0.99, enabling reliable cross-modal attribution verification. These components form an end-to-end forensic pipeline that enables reliable tracing of harmful deployments of AI-generated imagery, supporting accountability in modern synthetic media environments. Our code is available at GitHub: this https URL

---


### 105. [Tracing the Roots: A Multi-Agent Framework for Uncovering Data Lineage in Post-Training LLMs](https://arxiv.org/abs/2604.10480)

**<font color=#1a73e8>作者：</font>** Yu Li, Xiaoran Shang, Qizhi Pei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training data plays a pivotal role in shaping the capabilities of Large Language Models (LLMs), yet datasets are often treated as isolated artifacts, overlooking the systemic connections that underlie their evolution. To disentangle these complex relationships, we introduce the concept of \textbf{data lineage} to the LLM ecosystem and propose an automated multi-agent framework to reconstruct the evolutionary graph of dataset development. Through large-scale lineage analysis, we characterize domain-specific structural patterns, such as vertical refinement in math-oriented datasets and horizontal aggregation in general-domain corpora. Moreover, we uncover pervasive systemic issues, including \textit{structural redundancy} induced by implicit dataset intersections and the \textit{propagation of benchmark contamination} along lineage paths. To demonstrate the practical value of lineage analysis for data construction, we leverage the reconstructed lineage graph to create a \textit{lineage-aware diversity-oriented dataset}. By anchoring instruction sampling at upstream root sources, this approach mitigates downstream homogenization and hidden redundancy, yielding a more diverse post-training corpus. We further highlight lineage-centric analysis as an efficient and robust topological alternative to sample-level dataset comparison for large-scale data ecosystems. By grounding data construction in explicit lineage structures, our work advances post-training data curation toward a more systematic and controllable paradigm.

---


### 106. [Why Don't You Know? Evaluating the Impact of Uncertainty Sources on Uncertainty Quantification in LLMs](https://arxiv.org/abs/2604.10495)

**<font color=#1a73e8>作者：</font>** Maiya Goloburda, Roman Vashurin, Fedor Chernogorsky 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed in real-world applications, reliable uncertainty quantification (UQ) becomes critical for safe and effective use. Most existing UQ approaches for language models aim to produce a single confidence score -- for example, estimating the probability that a model's answer is correct. However, uncertainty in natural language tasks arises from multiple distinct sources, including model knowledge gaps, output variability, and input ambiguity, which have different implications for system behavior and user interaction. In this work, we study how the source of uncertainty impacts the behavior and effectiveness of existing UQ methods. To enable controlled analysis, we introduce a new dataset that explicitly categorizes uncertainty sources, allowing systematic evaluation of UQ performance under each condition. Our experiments reveal that while many UQ methods perform well when uncertainty stems solely from model knowledge limitations, their performance degrades or becomes misleading when other sources are introduced. These findings highlight the need for uncertainty-aware methods that explicitly account for the source of uncertainty in large language models.

---


### 107. [CodeQuant: Unified Clustering and Quantization for Enhanced Outlier Smoothing in Low-Precision Mixture-of-Experts](https://arxiv.org/abs/2604.10496)

**<font color=#1a73e8>作者：</font>** Xiangyang Yin, Xingyu Liu, Tianhua Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outliers have emerged as a fundamental bottleneck in preserving accuracy for low-precision large models, particularly within Mixture-of-Experts (MoE) architectures that are increasingly central to large-scale language modeling. Under post-training quantization (PTQ), these outliers induce substantial quantization errors, leading to severe accuracy degradation. While recent rotation-based smoothing techniques alleviate the problem by redistributing outlier magnitudes, residual errors remain and continue to impede reliable low-precision deployment.
In this work, we tackle this challenge by introducing \textit{CodeQuant}, a unified quantization-and-clustering scheme that contains smoothing activation outliers via learnable rotation and absorbing weight outliers into fine-tuned cluster centroids for MoE. This design reduces the influence of extreme values by fitting them within cluster centroids, thereby lowering quantization error while maintaining expressive capacity. Coupled with a dedicated kernel design for GPU and CPU, CodeQuant achieves up to $4.15\times$ speedup while delivering significantly higher accuracy than state-of-the-art quantization approaches across diverse MoE models. Our results highlight CodeQuant as a promising direction for efficient and accurate deployment of MoE-based large language models under low-precision constraints. Our code is available at this https URL.

---


### 108. [Visual Enhanced Depth Scaling for Multimodal Latent Reasoning](https://arxiv.org/abs/2604.10500)

**<font color=#1a73e8>作者：</font>** Yudong Han, Yong Wang, Zaiquan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal latent reasoning has emerged as a promising paradigm that replaces explicit Chain-of-Thought (CoT) decoding with implicit feature propagation, simultaneously enhancing representation informativeness and reducing inference latency. By analyzing token-level gradient dynamics during latent training, we reveal two critical observations: (1) visual tokens exhibit significantly higher and more volatile gradient norms than their textual counterparts due to inherent language bias, resulting in systematic visual under-optimization; and (2) semantically simple tokens converge rapidly, whereas complex tokens exhibit persistent gradient instability constrained by fixed architectural depths. To address these limitations, we propose a visual replay module and routing depth scaling to collaboratively enhance visual perception and refine complicated latents for deeper contextual reasoning. The former module leverages causal self-attention to estimate token saliency, reinforcing fine-grained grounding through spatially-coherent constraints. Complementarily, the latter mechanism adaptively allocates additional reasoning steps to complex tokens, enabling deeper contextual refinement. Guided by a curriculum strategy that progressively internalizes explicit CoT into compact latent representations, our framework achieves state-of-the-art performance across diverse benchmarks while delivering substantial inference speedups over explicit CoT baselines.

---


### 109. [CHAIRO: Contextual Hierarchical Analogical Induction and Reasoning Optimization for LLMs](https://arxiv.org/abs/2604.10502)

**<font color=#1a73e8>作者：</font>** Haotian Lu, Yuchen Mou, Bingzhe Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Content moderation in online platforms faces persistent challenges due to the evolving complexity of user-generated content and the limitations of traditional rule-based and machine learning approaches. While recent advances in large language models (LLMs) have enabled more sophisticated moderation via direct prompting or fine-tuning, these approaches often exhibit limited generalization, interpretability, and adaptability to unseen or ambiguous cases.
In this work, we propose a novel moderation framework that leverages analogical examples to enhance rule induction and decision reliability. Our approach integrates end-to-end optimization of analogical retrieval, rule generation, and moderation classification, enabling the dynamic adaptation of moderation rules to diverse content scenarios. Through comprehensive experiments, we demonstrate that our method significantly outperforms both rule-injected fine-tuning baselines and multi-stage static RAG pipelines in terms of moderation accuracy and rule quality. Further evaluations, including human assessments and external model generalization tests, confirm that our framework produces rules with better clarity, interpretability, and applicability. These findings show that analogical example-driven methods can advance robust, explainable, and generalizable content moderation in real-world applications.

---


### 110. [CARO: Chain-of-Analogy Reasoning Optimization for Robust Content Moderation](https://arxiv.org/abs/2604.10504)

**<font color=#1a73e8>作者：</font>** Bingzhe Wu, Haotian Lu, Yuchen Mou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current large language models (LLMs), even those explicitly trained for reasoning, often struggle with ambiguous content moderation cases due to misleading "decision shortcuts" embedded in context. Inspired by cognitive psychology insights into expert moderation, we introduce \caro (Chain-of-Analogy Reasoning Optimization), a novel two-stage training framework to induce robust analogical reasoning in LLMs. First, \caro bootstraps analogical reasoning chains via retrieval-augmented generation (RAG) on moderation data and performs supervised fine-tuning (SFT). Second, we propose a customized direct preference optimization (DPO) approach to reinforce analogical reasoning behaviors explicitly. Unlike static retrieval methods, \caro dynamically generates tailored analogical references during inference, effectively mitigating harmful decision shortcuts. Extensive experiments demonstrate that \caro substantially outperforms state-of-the-art reasoning models (DeepSeek R1, QwQ), specialized moderation models (LLaMA Guard), and advanced fine-tuning and retrieval-augmented methods, achieving an average F1 score improvement of 24.9\% on challenging ambiguous moderation benchmarks.

---


### 111. [A Progressive Training Strategy for Vision-Language Models to Counteract Spatio-Temporal Hallucinations in Embodied Reasoning](https://arxiv.org/abs/2604.10506)

**<font color=#1a73e8>作者：</font>** Xiaoda Yang, Shuai Yang, Can Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have made significant strides in static image understanding but continue to face critical hurdles in spatiotemporal reasoning. A major bottleneck is "multi-image reasoning hallucination", where a massive performance drop between forward and reverse temporal queries reveals a dependence on superficial shortcuts instead of genuine causal understanding. To mitigate this, we first develop a new Chain-of-Thought (CoT) dataset that decomposes intricate reasoning into detailed spatiotemporal steps and definitive judgments. Building on this, we present a progressive training framework: it initiates with supervised pre-training on our CoT dataset to instill logical structures, followed by fine-tuning with scalable weakly-labeled data for broader generalization. Our experiments demonstrate that this approach not only improves backbone accuracy but also slashes the forward-backward performance gap from over 70\% to only 6.53\%. This confirms the method's ability to develop authentic dynamic reasoning and reduce the inherent temporal biases of current VLMs.

---


### 112. [Thinking Fast, Thinking Wrong: Intuitiveness Modulates LLM Counterfactual Reasoning in Policy Evaluation](https://arxiv.org/abs/2604.10511)

**<font color=#1a73e8>作者：</font>** Yanjie He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for causal and counterfactual reasoning, yet their reliability in real-world policy evaluation remains underexplored. We construct a benchmark of 40 empirical policy evaluation cases drawn from economics and social science, each grounded in peer-reviewed evidence and classified by intuitiveness -- whether the empirical finding aligns with (obvious), is unclear relative to (ambiguous), or contradicts (counter-intuitive) common prior expectations. We evaluate four frontier LLMs across five prompting strategies with 2,400 experimental trials and analyze the results using mixed-effects logistic regression. Our findings reveal three key results: (1) a chain-of-thought (CoT) paradox, where chain-of-thought prompting dramatically improves performance on obvious cases but this benefit is nearly eliminated on counter-intuitive ones (interaction OR = 0.053, $p < 0.001$); (2) intuitiveness as the dominant factor, explaining more variance than model choice or prompting strategy (ICC = 0.537); and (3) a knowledge-reasoning dissociation, where citation-based familiarity is unrelated to accuracy ($p = 0.53$), suggesting models possess relevant knowledge but fail to reason with it when findings contradict intuition. We frame these results through the lens of dual-process theory (System 1 vs. System 2) and argue that current LLMs' "slow thinking" may be little more than "slow talking" -- they produce the form of deliberative reasoning without the substance.

---


### 113. [Agent Mentor: Framing Agent Knowledge through Semantic Trajectory Analysis](https://arxiv.org/abs/2604.10513)

**<font color=#1a73e8>作者：</font>** Roi Ben-Gigi, Yuval David, Fabiana Fournier 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agent development relies heavily on natural language prompting to define agents' tasks, knowledge, and goals. These prompts are interpreted by Large Language Models (LLMs), which govern agent behavior. Consequently, agentic performance is susceptible to variability arising from imprecise or ambiguous prompt formulations. Identifying and correcting such issues requires examining not only the agent's code, but also the internal system prompts generated throughout its execution lifecycle, as reflected in execution logs.
In this work, we introduce an analytics pipeline implemented as part of the Agent Mentor open-source library that monitors and incrementally adapts the system prompts defining another agent's behavior. The pipeline improves performance by systematically injecting corrective instructions into the agent's knowledge. We describe its underlying mechanism, with particular emphasis on identifying semantic features associated with undesired behaviors and using them to derive corrective statements.
We evaluate the proposed pipeline across three exemplar agent configurations and benchmark tasks using repeated execution runs to assess effectiveness. These experiments provide an initial exploration of automating such a mentoring pipeline within future agentic governance frameworks. Overall, the approach demonstrates consistent and measurable accuracy improvements across diverse configurations, particularly in settings dominated by specification ambiguity. For reproducibility, we released our code as open source under the Agent Mentor library.

---


### 114. [Data-Efficient Surgical Phase Segmentation in Small-Incision Cataract Surgery: A Controlled Study of Vision Foundation Models](https://arxiv.org/abs/2604.10514)

**<font color=#1a73e8>作者：</font>** Lincoln Spencer, Song Wang, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical phase segmentation is central to computer-assisted surgery, yet robust models remain difficult to develop when labeled surgical videos are scarce. We study data-efficient phase segmentation for manual small-incision cataract surgery (SICS) through a controlled comparison of visual representations. To isolate representation quality, we pair each visual encoder with the same temporal model (MS-TCN++) under identical training and evaluation settings on SICS-155 (19 phases). We compare supervised encoders (ResNet-50, I3D) against large self-supervised foundation models (DINOv3, V-JEPA2), and use a cached-feature pipeline that decouples expensive visual encoding from lightweight temporal learning. Foundation-model features improve segmentation performance in this setup, with DINOv3 ViT-7B achieving the best overall results (83.4% accuracy, 87.0 edit score). We further examine cataract-domain transfer using unlabeled videos and lightweight adaptation, and analyze when it helps or hurts. Overall, the study indicates strong transferability of modern vision foundation models to surgical workflow understanding and provides practical guidance for low-label medical video settings. The project website is available at: this https URL

---


### 115. [BareBones: Benchmarking Zero-Shot Geometric Comprehension in VLMs](https://arxiv.org/abs/2604.10528)

**<font color=#1a73e8>作者：</font>** Aaditya Baranwal, Vishal Yadav, Abhishek Rajora  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision-Language Models (VLMs) demonstrate remarkable zero-shot recognition capabilities across a diverse spectrum of multimodal tasks, it yet remains an open question whether these architectures genuinely comprehend geometric structure or merely exploit RGB textures and contextual priors as statistical shortcuts. Existing evaluations fail to isolate this mechanism, conflating semantic reasoning with texture mapping and relying on imprecise annotations that inadvertently leak environmental cues. To address this gap, we introduce \textbf{BareBones}, a zero-shot benchmark designed to stress-test pure geometric shape comprehension. We curate pixel-level silhouettes of geometrically distinct classes across six datasets: five established segmentation sources (ImageNet-S, DIS5K, ThinObject5K, PASCAL VOC, CUB-200) and our novel flagship collection, WTP-Bench, establishing a noise-free geometric taxonomy. WTP-Bench is an extreme, fine-grained visual puzzle that forces models to identify inter-class geometric concepts from boundary contours alone. Our evaluation of 26 state-of-the-art proprietary and open-weight VLMs (\eg, GPT-4.1, Gemini, Claude Sonnet 4.5, LLaVA) reveals a consistent, severe performance collapse under RGB deprivation, a phenomenon we term the \textit{Texture Bias Cliff}. By documenting universal structural blindspots, BareBones establishes a rigorous yardstick for genuine geometric grounding.

---


### 116. [IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs](https://arxiv.org/abs/2604.10539)

**<font color=#1a73e8>作者：</font>** Yuzhen Mao, Qitong Wang, Martin Ester 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-Value (KV) cache plays a crucial role in accelerating inference in large language models (LLMs) by storing intermediate attention states and avoiding redundant computation during autoregressive generation. However, its memory footprint scales linearly with sequence length, often leading to severe memory bottlenecks on resource-constrained hardware. Prior work has explored offloading KV cache to the CPU while retaining only a subset on the GPU, but these approaches often rely on imprecise token selection and suffer performance degradation in long-generation tasks such as chain-of-thought reasoning. In this paper, we propose a novel KV cache management strategy, IceCache, which integrates semantic token clustering with PagedAttention. By organizing semantically related tokens into contiguous memory regions managed by a hierarchical, dynamically updatable data structure, our method enables more efficient token selection and better utilization of memory bandwidth during CPU-GPU transfers. Experimental results on LongBench show that, with a 256-token budget, IceCache maintains 99% of the original accuracy achieved by the full KV cache model. Moreover, compared to other offloading-based methods, IceCache attains competitive or even superior latency and accuracy while using only 25% of the KV cache token budget, demonstrating its effectiveness in long-sequence scenarios. The code is available on our project website at this https URL.

---


### 117. [WaveMoE: A Wavelet-Enhanced Mixture-of-Experts Foundation Model for Time Series Forecasting](https://arxiv.org/abs/2604.10544)

**<font color=#1a73e8>作者：</font>** Shunyu Wu, Jiawei Huang, Weibin Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have recently achieved remarkable success in universal forecasting by leveraging large-scale pretraining on diverse time series data. Complementing this progress, incorporating frequency-domain information yields promising performance in enhancing the modeling of complex temporal patterns, such as periodicity and localized high-frequency dynamics, which are prevalent in real-world time series. To advance this direction, we propose a new perspective that integrates explicit frequency-domain representations into scalable foundation models, and introduce WaveMoE, a wavelet-enhanced mixture-of-experts foundation model for time series forecasting. WaveMoE adopts a dual-path architecture that jointly processes time series tokens and wavelet tokens aligned along a unified temporal axis, and coordinates them through a shared expert routing mechanism that enables consistent expert specialization while efficiently scaling model capacity. Preliminary experimental results on 16 diverse benchmark datasets indicate that WaveMoE has the potential to further improve forecasting performance by incorporating wavelet-domain corpora.

---


### 118. [Enhanced Self-Learning with Epistemologically-Informed LLM Dialogue](https://arxiv.org/abs/2604.10545)

**<font color=#1a73e8>作者：</font>** Yi-Fan Cao, Kento Shigyo, Yitong Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have advanced self-learning tools, enabling more personalized interactions. However, learners struggle to engage in meaningful dialogue and process complex information. To alleviate this, we incorporate epistemological frameworks within an LLM-based approach to self-learning, reducing the cognitive load on learners and fostering deeper engagement and holistic understanding. Through a formative study (N=26), we identified epistemological differences in self-learner interaction patterns. Building upon these findings, we present \textit{CausaDisco}, a dialogue-based interactive system that integrates Aristotle's \textit{Four Causes} framework into LLM prompts to enhance cognitive support for self-learning. This approach guides learners' self-learning journeys by automatically generating coherent and contextually appropriate follow-up questions. A controlled study (N=36) demonstrated that, compared to baseline, \textit{CausaDisco} fostered more engaging interactions, inspired sophisticated exploration, and facilitated multifaceted perspectives. This research contributes to HCI by expanding the understanding of LLMs as educational agents and providing design implications for this emerging class of tools.

---


### 119. [Agent^2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?](https://arxiv.org/abs/2604.10547)

**<font color=#1a73e8>作者：</font>** Wanyi Chen, Xiao Yang, Xu Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Agent^2 RL-Bench, a benchmark for evaluating agentic RL post-training -- whether LLM agents can autonomously design, implement, and run complete RL pipelines that improve foundation models. This capability is important because RL post-training increasingly drives model alignment and specialization, yet existing benchmarks remain largely static: supervised fine-tuning alone yields strong results, leaving interactive RL engineering untested. Agent^2 RL-Bench addresses this with six tasks across three levels -- from static rule-based training to closed-loop online RL with trajectory collection -- each adding a structural requirement that prior levels do not impose. The benchmark provides isolated workspaces with a grading API, runtime instrumentation that records every submission and code revision, and automated post-hoc analysis that generates structured run reports, enabling the first automated diagnostic of agent-driven post-training behavior. Across multiple agent stacks spanning five agent systems and six driver LLMs, we find that agents achieve striking interactive gains -- on ALFWorld, an RL-only agent improves from 5.97 to 93.28 via SFT warm-up and GRPO with online rollouts -- yet make only marginal progress on others (DeepSearchQA: +2.75 within evaluation noise), and that driver choice has a large effect on interactive tasks -- within the same scaffold, switching drivers changes interactive improvement from near-zero to +78pp. More broadly, the benchmark reveals that supervised pipelines dominate agent-driven post-training under fixed budgets, with online RL succeeding as the final best route only on ALFWorld. Code is available at this https URL.

---


### 120. [Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models](https://arxiv.org/abs/2604.10556)

**<font color=#1a73e8>作者：</font>** Zhengnan Guo, Fei Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Diffusion Large Language Models (dLLMs) have emerged as a promising non-autoregressive paradigm comparable to autoregressive (AR) models, their faithfulness, specifically regarding hallucination, remains largely underexplored. To bridge this gap, we present the first controlled comparative study to evaluate hallucination patterns in dLLMs. Our results demonstrate that current dLLMs exhibit a higher propensity for hallucination than AR counterparts controlled for architecture, scale, and pre-training weights. Furthermore, an analysis of inference-time compute reveals divergent dynamics: while quasi-autoregressive generation suffers from early saturation, non-sequential decoding unlocks potential for continuous refinement. Finally, we identify distinct failure modes unique to the diffusion process, including premature termination, incomplete denoising, and context intrusion. Our findings underscore that although dLLMs have narrowed the performance gap on general tasks, their distinct hallucination mechanisms pose a critical challenge to model reliability. Our code is available at this https URL

---


### 121. [LLMs Should Incorporate Explicit Mechanisms for Human Empathy](https://arxiv.org/abs/2604.10557)

**<font color=#1a73e8>作者：</font>** Xiaoxing You, Qiang Huang, Jun Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper argues that Large Language Models (LLMs) should incorporate explicit mechanisms for human empathy. As LLMs become increasingly deployed in high-stakes human-centered settings, their success depends not only on correctness or fluency but on faithful preservation of human perspectives. Yet, current LLMs systematically fail at this requirement: even when well-aligned and policy-compliant, they often attenuate affect, misrepresent contextual salience, and rigidify relational stance in ways that distort meaning. We formalize empathy as an observable behavioral property: the capacity to model and respond to human perspectives while preserving intention, affect, and context. Under this framing, we identify four recurring mechanisms of empathic failure in contemporary LLMs--sentiment attenuation, empathic granularity mismatch, conflict avoidance, and linguistic distancing--arising as structural consequences of prevailing training and alignment practices. We further organize these failures along three dimensions: cognitive, cultural, and relational empathy, to explain their manifestation across tasks. Empirical analyses show that strong benchmark performance can mask systematic empathic distortions, motivating empathy-aware objectives, benchmarks, and training signals as first-class components of LLM development.

---


### 122. [Early Decisions Matter: Proximity Bias and Initial Trajectory Shaping in Non-Autoregressive Diffusion Language Models](https://arxiv.org/abs/2604.10567)

**<font color=#1a73e8>作者：</font>** Jiyeon Kim, Sungik Choi, Yongrae Jo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion-based language models (dLLMs) have emerged as a promising alternative to autoregressive language models, offering the potential for parallel token generation and bidirectional context modeling. However, harnessing this flexibility for fully non-autoregressive decoding remains an open question, particularly for reasoning and planning tasks. In this work, we investigate non-autoregressive decoding in dLLMs by systematically analyzing its inference dynamics along the temporal axis. Specifically, we uncover an inherent failure mode in confidence-based non-autoregressive generation stemming from a strong proximity bias-the tendency for the denoising order to concentrate on spatially adjacent tokens. This local dependency leads to spatial error propagation, rendering the entire trajectory critically contingent on the initial unmasking position. Leveraging this insight, we present a minimal-intervention approach that guides early token selection, employing a lightweight planner and end-of-sequence temperature annealing. We thoroughly evaluate our method on various reasoning and planning tasks and observe substantial overall improvement over existing heuristic baselines without significant computational overhead.

---


### 123. [NexusAI: Enabling Design Space Exploration of Ideas through Cognitive Abstraction and Functional Decomposition](https://arxiv.org/abs/2604.10575)

**<font color=#1a73e8>作者：</font>** Anqi Wang, Bingqian Wang, Huiyang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) offer vast potential for creative ideation; however, their standard interaction paradigm often produces unstructured textual outputs that lead users to prematurely converge on sub-optimal ideas-a phenomenon known as fixation. While recent creativity tools have begun to structure these outputs, they remain compositionally opaque: ideas are organized as monolithic units that cannot be decomposed, abstracted, or recombinable at a sub-idea level. To address this, we propose Cognitive Abstraction (CA), a computational pipeline that transforms raw LLM-generated inspiration into a navigable and transformable design space. We implement this pipeline in NexusAI, a prototype diagramming system that supports (I) decomposition of inspiration into typed functional fragments, (II) multi-level abstraction to externalize mental scaling, and (III) cross-dimensional recombination to spark novel design directions. A within-subject user study (N=14) demonstrates that NexusAI significantly improves design space exploration, reduces cognitive overhead, and facilitates perspective reframing compared to a baseline. Our work contributes: (1) a characterization of "compositional opacity" as a barrier in human-AI co-creation; (2) the CA pipeline for operationalizing creative cognitive primitives at scale; and (3) empirical evidence that structured, multi-level representations can effectively mitigate fixation and support divergent exploration.

---


### 124. [Calibration Collapse Under Sycophancy Fine-Tuning: How Reward Hacking Breaks Uncertainty Quantification in LLMs](https://arxiv.org/abs/2604.10585)

**<font color=#1a73e8>作者：</font>** Subramanyam Sahoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) are increasingly fine-tuned via reinforcement learning from human feedback (RLHF) or related reward optimisation schemes. While such procedures improve perceived helpfulness, we investigate whether sycophantic reward signals degrade calibration -- a property essential for reliable uncertainty quantification. We fine-tune Qwen3-8B under three regimes: no fine-tuning (base), neutral supervised fine-tuning (SFT) on TriviaQA, and sycophancy-inducing Group Relative Policy Optimisation (GRPO) that rewards agreement with planted wrong answers. Evaluating on $1{,}000$ MMLU items across five subject domains with bootstrap confidence intervals and permutation testing, we find that \textbf{sycophantic GRPO produces consistent directional calibration degradation} -- ECE rises by $+0.006$ relative to the base model and MCE increases by $+0.010$ relative to neutral SFT -- though the effect does not reach statistical significance ($p = 0.41$) at this training budget. Post-hoc matrix scaling applied to all three models reduces ECE by $40$--$64\%$ and improves accuracy by $1.5$--$3.0$ percentage points. However, the sycophantic model retains the highest post-scaling ECE relative to the neutral SFT control ($0.042$ vs.\ $0.037$), suggesting that reward-induced miscalibration leaves a structured residual even after affine correction. These findings establish a methodology for evaluating the calibration impact of reward hacking and motivate calibration-aware training objectives.

---


### 125. [CogInstrument: Modeling Cognitive Processes for Bidirectional Human-LLM Alignment in Planning Tasks](https://arxiv.org/abs/2604.10587)

**<font color=#1a73e8>作者：</font>** Anqi Wang, Dongyijie Pan, Xin Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) demonstrate proficiency in knowledge-intensive tasks, current interfaces frequently precipitate cognitive misalignment by failing to externalize users' underlying reasoning structures. Existing tools typically represent intent as "flat lists," thereby disregarding the causal dependencies and revisable assumptions inherent in human decision-making. We introduce CogInstrument, a system that represents user reasoning through cognitive motifs-compositional, revisable units comprising concepts linked by causal dependencies. CogInstrument extracts these motifs from natural language interactions and renders them as editable graphical structures to facilitate bidirectional alignment. This structural externalization enables both the user and the LLM to inspect, negotiate, and reconcile reasoning processes iteratively. A within-subjects study (N=12) demonstrates that CogInstrument explicitly surfaces implicit reasoning structures, facilitating more targeted revision and reusability over conventional LLM-based dialogue interfaces. By enabling users to verify the logical grounding of LLM outputs, CogInstrument significantly enhances user agency, trust, and structural control over the collaboration. This work formalizes cognitive motifs as a fundamental unit for human-LLM alignment, providing a novel framework for achieving structured, reasoning-based human-AI collaboration.

---


### 126. [Bridging Linguistic Gaps: Cross-Lingual Mapping in Pre-Training and Dataset for Enhanced Multilingual LLM Performance](https://arxiv.org/abs/2604.10590)

**<font color=#1a73e8>作者：</font>** Weihua Zheng, Chang Liu, Zhengyuan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual Large Language Models (LLMs) struggle with cross-lingual tasks due to data imbalances between high-resource and low-resource languages, as well as monolingual bias in pre-training. Existing methods, such as bilingual fine-tuning and contrastive alignment, can improve cross-lingual performance, but they often require extensive parallel data or suffer from instability. To address these challenges, we introduce a Cross-Lingual Mapping Task during the pre-training phase, which enhances cross-lingual alignment without compromising monolingual fluency. Our approach bi-directionally maps languages within the LLM embedding space, improving both language generation and comprehension. We further propose a Language Alignment Coefficient to robustly quantify cross-lingual consistency, even in limited-data scenarios. Experimental results on machine translation (MT), cross-lingual natural language understanding (CLNLU), and cross-lingual question answering (CLQA) show that our model achieves gains of up to 11.9 BLEU points in MT, 6.72 points in CLQA BERTScore-Precision, and more than 5% in CLNLU accuracy over strong multilingual baselines. These findings highlight the potential of incorporating cross-lingual objectives into pre-training to improve multilingual LLMs.

---


### 127. [GeoMeld: Toward Semantically Grounded Foundation Models for Remote Sensing](https://arxiv.org/abs/2604.10591)

**<font color=#1a73e8>作者：</font>** Maram Hasan, Md Aminur Hossain, Savitra Roy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective foundation modeling in remote sensing requires spatially aligned heterogeneous modalities coupled with semantically grounded supervision, yet such resources remain limited at scale. We present GeoMeld, a large-scale multimodal dataset with approximately 2.5 million spatially aligned samples. The dataset spans diverse modalities and resolutions and is constructed under a unified alignment protocol for modality-aware representation learning. GeoMeld provides semantically grounded language supervision through an agentic captioning framework that synthesizes and verifies annotations from spectral signals, terrain statistics, and structured geographic metadata, encoding measurable cross-modality relationships within textual descriptions. To leverage this dataset, we introduce GeoMeld-FM, a pretraining framework that combines multi-pretext masked autoencoding over aligned modalities, JEPA representation learning, and caption-vision contrastive alignment. This joint objective enables the learned representation space to capture both reliable cross-sensor physical consistency and grounded semantics. Experiments demonstrate consistent gains in downstream transfer and cross-sensor robustness. Together, GeoMeld and GeoMeld-FM establish a scalable reference framework for semantically grounded multi-modal foundation modeling in remote sensing.

---


### 128. [MoEITS: A Green AI approach for simplifying MoE-LLMs](https://arxiv.org/abs/2604.10603)

**<font color=#1a73e8>作者：</font>** Luis Balderas, Miguel Lastra, José M. Benítez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are transforming all areas of academia and industry, attracting the attention of researchers, professionals, and the general public. In the trek for more powerful architectures, Mixture-of-Experts, inspired by ensemble models, have emerged as one of the most effective ways to follow. However, this implies a high computational burden for both training and inference. To reduce the impact on computing and memory footprint as well as the energy consumption, simplification methods has arisen as very effective procedures.
In this paper, an original algorithm, MoEITS, for MoE-LLMs simplification is presented. The algorithm is characterized by a refined simplicity, underpinned by standardized Information Theoretic frameworks. MoEITS is analyzed in depth from theoretical and practical points of view. Its computational complexity is studied. Its performance on the accuracy of the simplified LLMs and the reduction rate achieved is assessed through a thoroughly designed experimentation. This empirical evaluation includes a comparison with state-of-the-art MoE-LLM pruning methods applied on Mixtral $8\times7$B, Qwen1.5-2.7B, and DeepSeek-V2-Lite. The extensive experimentation conducted demonstrates that MoEITS outperforms state-of-the-art techniques by generating models that are both effective across all benchmarks and computationally efficient.
The code implementing the method will be available at this https URL.

---


### 129. [Computational Lesions in Multilingual Language Models Separate Shared and Language-specific Brain Alignment](https://arxiv.org/abs/2604.10627)

**<font color=#1a73e8>作者：</font>** Yang Cui, Jingyuan Sun, Yizheng Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How the brain supports language across different languages is a basic question in neuroscience and a useful test for multilingual artificial intelligence. Neuroimaging has identified language-responsive brain regions across languages, but it cannot by itself show whether the underlying processing is shared or language-specific. Here we use six multilingual large language models (LLMs) as controllable systems and create targeted ``computational lesions'' by zeroing small parameter sets that are important across languages or especially important for one language. We then compare intact and lesioned models in predicting functional magnetic resonance imaging (fMRI) responses during 100 minutes of naturalistic story listening in native English, Chinese and French (112 participants). Lesioning a compact shared core reduces whole-brain encoding correlation by 60.32% relative to intact models, whereas language-specific lesions preserve cross-language separation in embedding space but selectively weaken brain predictivity for the matched native language. These results support a shared backbone with embedded specializations and provide a causal framework for studying multilingual brain-model alignment.

---


### 130. [ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction](https://arxiv.org/abs/2604.10633)

**<font color=#1a73e8>作者：</font>** Wenda Liu, Zhigang Song, Shuai Nie 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based universal information extraction (UIE) methods often rely on additional information beyond the original training data, which increases training complexity yet often yields limited gains. To address this, we propose ProUIE, a Macro-to-Micro progressive learning approach that improves UIE without introducing any external information. ProUIE consists of three stages: (i) macro-level Complete Modeling (CM), which learns NER, RE, and EE along their intrinsic difficulty order on the full training data to build a unified extraction foundation, (ii) meso-level Streamlined Alignment (SA), which operates on sampled data with simplified target formats, streamlining and regularizing structured outputs to make them more concise and controllable, and (iii) micro-level Deep Exploration (DE), which applies GRPO with stepwise fine-grained rewards (SFR) over structural units to guide exploration and improve performance. Experiments on 36 public datasets show that ProUIE consistently improves unified extraction, outperforming strong instruction-tuned baselines on average for NER and RE while using a smaller backbone, and it further demonstrates clear gains in large-scale production-oriented information extraction.

---


### 131. [Omnimodal Dataset Distillation via High-order Proxy Alignment](https://arxiv.org/abs/2604.10666)

**<font color=#1a73e8>作者：</font>** Yuxuan Gao, Xiaohao Liu, Xiaobo Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation compresses large-scale datasets into compact synthetic sets while preserving training performance, but existing methods are largely restricted to single-modal or bimodal settings. Extending dataset distillation to scenarios involving more than two modalities, i.e., Omnimodal Dataset Distillation, remains underexplored and challenging due to increased heterogeneity and complex cross-modal interactions. In this work, we identify the key determinant that bounds the endpoint discrepancy in the omnimodal setting, which is exacerbated with an increasing number of modalities. To this end, we propose HoPA, a unified method that captures high-order cross-modal alignments via a compact proxy, which is compatible with trajectory matching as well. By abstracting omnimodal alignment with a shared similarity structure, our method avoids the combinatorial complexity of pairwise modality modeling and enables scalable joint distillation across heterogeneous modalities. Theoretical analysis from the spectral perspective reveals the rationality of our proposed method against bimodal dataset distillation techniques. Extensive experiments on various benchmarks demonstrate that the proposed method achieves superior compression-performance trade-offs compared to existing competitors. The source code will be publicly released.

---


### 132. [Learning and Enforcing Context-Sensitive Control for LLMs](https://arxiv.org/abs/2604.10667)

**<font color=#1a73e8>作者：</font>** Mohammad Albinhassan, Pranava Madhyastha, Mark Law 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Controlling the output of Large Language Models (LLMs) through context-sensitive constraints has emerged as a promising approach to overcome the limitations of Context-Free Grammars (CFGs) in guaranteeing generation validity. However, such constraints typically require manual specification -- a significant barrier demanding specialized expertise. We introduce a framework that automatically learns context-sensitive constraints from LLM interactions through a two-phase process: syntactic exploration to gather diverse outputs for constraint learning, followed by constraint exploitation to enforce these learned rules during generation. Experiments demonstrate that our method enables even small LLMs (1B parameters) to learn and generate with perfect constraint adherence, outperforming larger counterparts and state-of-the-art reasoning models. This work represents the first integration of context-sensitive grammar learning with LLM generation, eliminating manual specification while maintaining generation validity.

---


### 133. [Principles Do Not Apply Themselves: A Hermeneutic Perspective on AI Alignment](https://arxiv.org/abs/2604.10673)

**<font color=#1a73e8>作者：</font>** Behrooz Razeghi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI alignment is often framed as the task of ensuring that an AI system follows a set of stated principles or human preferences, but general principles rarely determine their own application in concrete cases. When principles conflict, when they are too broad to settle a situation, or when the relevant facts are unclear, an additional act of judgment is required. This paper analyzes that step through the lens of hermeneutics and argues that alignment therefore includes an interpretive component: it involves context-sensitive judgments about how principles should be read, applied, and prioritized in practice. We connect this claim to recent empirical findings showing that a substantial portion of preference-labeling data falls into cases of principle conflict or indifference, where the principle set does not uniquely determine a decision. We then draw an operational consequence: because such judgments are expressed in behavior, many alignment-relevant choices appear only in the distribution of responses a model generates at deployment time. To formalize this point, we distinguish deployment-induced and corpus-induced evaluation and show that off-policy audits can fail to capture alignment-relevant failures when the two response distributions differ. We argue that principle-specified alignment includes a context-dependent interpretive component.

---


### 134. [Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents](https://arxiv.org/abs/2604.10674)

**<font color=#1a73e8>作者：</font>** Hao Wang, Guozhi Wang, Han Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has been widely used to train LLM agents for multi-turn interactive tasks, but its sample efficiency is severely limited by sparse rewards and long horizons. On-policy self-distillation (OPSD) alleviates this by providing dense token-level supervision from a privileged teacher that has access to ground-truth answers. However, such fixed privileged information cannot capture the diverse valid strategies in agent tasks, and naively combining OPSD with RL often leads to training collapse. To address these limitations, we introduce Skill-SD, a framework that turns the agent's own trajectories into dynamic training-only supervision. Completed trajectories are summarized into compact natural language skills that describe successful behaviors, mistakes, and workflows. These skills serve as dynamic privileged information conditioning only the teacher, while the student always acts under the plain task prompt and learns to internalize the guidance through distillation. To stabilize the training, we derive an importance-weighted reverse-KL loss to provide gradient-correct token-level distillation, and dynamically synchronize the teacher with the improving student. Experimental results on agentic benchmarks demonstrate that Skill-SD substantially outperforms the standard RL baseline, improving both vanilla GRPO (+14.0%/+10.9% on AppWorld/Sokoban) and vanilla OPD (+42.1%/+40.6%). Project page: this https URL

---


### 135. [QFS-Composer: Query-focused summarization pipeline for less resourced languages](https://arxiv.org/abs/2604.10687)

**<font color=#1a73e8>作者：</font>** Vuk Đuranović, Marko Robnik Šikonja  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong performance in text summarization, yet their effectiveness drops significantly across languages with restricted training resources. This work addresses the challenge of query-focused summarization (QFS) in less-resourced languages, where labeled datasets and evaluation tools are limited. We present a novel QFS framework, QFS-Composer, that integrates query decomposition, question generation (QG), question answering (QA), and abstractive summarization to improve the factual alignment of a summary with user intent. We test our approach on the Slovenian language. To enable high-quality supervision and evaluation, we develop the Slovenian QA and QG models based on a Slovene LLM and adapt evaluation approaches for reference-free summary evaluation. Empirical evaluation shows that the QA-guided summarization pipeline yields improved consistency and relevance over baseline LLMs. Our work establishes an extensible methodology for advancing QFS in less-resourced languages.

---


### 136. [SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting](https://arxiv.org/abs/2604.10688)

**<font color=#1a73e8>作者：</font>** Binbin Zheng, Xing Ma, Yiheng Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy reinforcement learning has become the dominant paradigm for reasoning alignment in large language models, yet its sparse, outcome-level rewards make token-level credit assignment notoriously difficult. On-Policy Distillation (OPD) alleviates this by introducing dense, token-level KL supervision from a teacher model, but typically applies this supervision uniformly across all rollouts, ignoring fundamental differences in signal quality. We propose Signal-Calibrated On-Policy Distillation Enhancement (SCOPE), a dual-path adaptive training framework that routes on-policy rollouts by correctness into two complementary supervision paths. For incorrect trajectories, SCOPE performs teacher-perplexity-weighted KL distillation to prioritize instances where the teacher demonstrates genuine corrective capability, while down-weighting unreliable guidance. For correct trajectories, it applies student-perplexity-weighted MLE to concentrate reinforcement on low-confidence samples at the capability boundary rather than over-reinforcing already mastered ones. Both paths employ a group-level normalization to adaptively calibrate weight distributions, accounting for the intrinsic difficulty variance across prompts. Extensive experiments on six reasoning benchmarks show that SCOPE achieves an average relative improvement of 11.42% in Avg@32 and 7.30% in Pass@32 over competitive baselines, demonstrating its consistent effectiveness.

---


### 137. [Do LLMs Build Spatial World Models? Evidence from Grid-World Maze Tasks](https://arxiv.org/abs/2604.10690)

**<font color=#1a73e8>作者：</font>** Weijiang Li, Yilin Zhu, Rajarshi Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models have shown remarkable performance across diverse tasks, yet their ability to construct internal spatial world models for reasoning and planning remains unclear. We systematically evaluate the spatial understanding of large language models through maze tasks, a controlled testing context requiring multi-step planning and spatial abstraction. Across comprehensive experiments with Gemini-2.5-Flash, GPT-5-mini, Claude-Haiku-4.5, and DeepSeek-Chat, we uncover significant discrepancies in spatial reasoning that challenge assumptions about LLM planning capabilities. Using chain-of-thought prompting, Gemini achieves 80-86% accuracy on smaller mazes (5x5 to 7x7 grids) with tokenized adjacency representations, but performance collapses to 16-34% with visual grid formats, which is a 2-5x difference, suggesting representation-dependent rather than format-invariant spatial reasoning. We further probe spatial understanding through sequential proximity questions and compositional distance comparisons. Despite achieving 96-99% semantic coverage in reasoning traces, models fail to leverage this understanding for consistent spatial computations, indicating that they treat each question independently rather than building cumulative spatial knowledge. Our findings based on the maze-solving tasks suggest that LLMs do not develop robust spatial world models, but rather exhibit representation-specific and prompting-dependent reasoning that succeeds only under narrow conditions. These results have critical implications for deploying foundation models in applications requiring spatial abstraction.

---


### 138. [Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2604.10697)

**<font color=#1a73e8>作者：</font>** Jakub Binkowski, Kamil Adamczewski, Tomasz Kajdanowicz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models frequently exhibit hallucinations: fluent and confident outputs that are factually incorrect or unsupported by the input context. While recent hallucination detection methods have explored various features derived from attention maps, the underlying mechanisms they exploit remain poorly understood. In this work, we propose SinkProbe, a hallucination detection method grounded in the observation that hallucinations are deeply entangled with attention sinks - tokens that accumulate disproportionate attention mass during generation - indicating a transition from distributed, input-grounded attention to compressed, prior-dominated computation. Importantly, although sink scores are computed solely from attention maps, we find that the classifier preferentially relies on sinks whose associated value vectors have large norms. Moreover, we show that previous methods implicitly depend on attention sinks by establishing their mathematical relationship to sink scores. Our findings yield a novel hallucination detection method grounded in theory that produces state-of-the-art results across popular datasets and LLMs.

---


### 139. [Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning](https://arxiv.org/abs/2604.10701)

**<font color=#1a73e8>作者：</font>** Zikang Shan, Han Zhong, Liwei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit assignment is a central challenge in reinforcement learning (RL). Classical actor-critic methods address this challenge through fine-grained advantage estimation based on a learned value function. However, learned value models are often avoided in modern large language model (LLM) RL because conventional discriminative critics are difficult to train reliably. We revisit value modeling and argue that this difficulty is partly due to limited expressiveness. In particular, representation complexity theory suggests that value functions can be hard to approximate under the one-shot prediction paradigm used by existing value models, and our scaling experiments show that such critics do not improve reliably with scale. Motivated by this observation, we propose Generative Actor-Critic (GenAC), which replaces one-shot scalar value prediction with a generative critic that performs chain-of-thought reasoning before producing a value estimate. We further introduce In-Context Conditioning, which helps the critic remain calibrated to the current actor throughout training. GenAC improves value approximation, ranking reliability, and out-of-distribution generalization, and these gains translate into stronger downstream RL performance than both value-based and value-free baselines. Overall, our results suggest that stronger value modeling is a promising direction for improving credit assignment in LLM reinforcement learning.

---


### 140. [SciPredict: Can LLMs Predict the Outcomes of Scientific Experiments in Natural Sciences?](https://arxiv.org/abs/2604.10718)

**<font color=#1a73e8>作者：</font>** Udari Madhushani Sehwag, Elaine Lau, Haniyeh Ehsani Oskouie 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accelerating scientific discovery requires the identification of which experiments would yield the best outcomes before committing resources to costly physical validation. While existing benchmarks evaluate LLMs on scientific knowledge and reasoning, their ability to predict experimental outcomes - a task where AI could significantly exceed human capabilities - remains largely underexplored. We introduce SciPredict, a benchmark comprising 405 tasks derived from recent empirical studies in 33 specialized sub-fields of physics, biology, and chemistry. SciPredict addresses two critical questions: (a) can LLMs predict the outcome of scientific experiments with sufficient accuracy? and (b) can such predictions be reliably used in the scientific research process? Evaluations reveal fundamental limitations on both fronts. Model accuracies are 14-26% and human expert performance is $\approx$20%. Although some frontier models exceed human performance model accuracy is still far below what would enable reliable experimental guidance. Even within the limited performance, models fail to distinguish reliable predictions from unreliable ones, achieving only $\approx$20% accuracy regardless of their confidence or whether they judge outcomes as predictable without physical experimentation. Human experts, in contrast, demonstrate strong calibration: their accuracy increases from $\approx$5% to $\approx$80% as they deem outcomes more predictable without conducting the experiment. SciPredict establishes a rigorous framework demonstrating that superhuman performance in experimental science requires not just better predictions, but better awareness of prediction reliability. For reproducibility all our data and code are provided at this https URL

---


### 141. [Teaching Language Models How to Code Like Learners: Conversational Serialization for Student Simulation](https://arxiv.org/abs/2604.10720)

**<font color=#1a73e8>作者：</font>** Charles Koutcheme, Arto Hellas, Juho Leinonen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial models that simulate how learners act and respond within educational systems are a promising tool for evaluating tutoring strategies and feedback mechanisms at scale. However, many existing approaches in programming education rely on prompting large, proprietary language models, raising concerns around privacy, cost, and dependence. In this work, we propose a method for training open-weight artificial programming learners using authentic student process data. Our approach serializes temporal log traces into a conversational format, representing each student's problem-solving process as a dialogue between the learner and their automated assessment system. Student code submissions and environment feedback, such as test outcomes, grades, and error traces, form alternating conversational turns, enabling models to learn from the iterative debugging process. We additionally introduce a training pipeline combining supervised fine-tuning with preference optimization to align models with authentic student debugging behavior. We evaluate our framework by training Qwen models at 4B and 8B scales on a large-scale dataset of real student submissions to Python programming assignments. Our results show that incorporating environment feedback strengthens the models' ability to replicate student debugging behavior, improving over both prior code-only approaches and prompted large language models baselines in functional alignment and code similarity. We release our code to support reproducibility.

---


### 142. [Turning Generators into Retrievers: Unlocking MLLMs for Natural Language-Guided Geo-Localization](https://arxiv.org/abs/2604.10721)

**<font color=#1a73e8>作者：</font>** Yuqi Chen, Xiaohan Zhang, Ahmad Arrabi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural-language Guided Cross-view Geo-localization (NGCG) aims to retrieve geo-tagged satellite imagery using textual descriptions of ground scenes. While recent NGCG methods commonly rely on CLIP-style dual-encoder architectures, they often suffer from weak cross-modal generalization and require complex architectural designs. In contrast, Multimodal Large Language Models (MLLMs) offer powerful semantic reasoning capabilities but are not directly optimized for retrieval tasks. In this work, we present a simple yet effective framework to adapt MLLMs for NGCG via parameter-efficient finetuning. Our approach optimizes latent representations within the MLLM while preserving its pretrained multimodal knowledge, enabling strong cross-modal alignment without redesigning model architectures. Through systematic analysis of diverse variables, from model backbone to feature aggregation, we provide practical and generalizable insights for leveraging MLLMs in NGCG. Our method achieves SOTA on GeoText-1652 with a 12.2% improvement in Text-to-Image Recall@1 and secures top performance in 5 out of 12 subtasks on CVG-Text, all while surpassing baselines with far fewer trainable parameters. These results position MLLMs as a robust foundation for semantic cross-view retrieval and pave the way for MLLM-based NGCG to be adopted as a scalable, powerful alternative to traditional dual-encoder designs. Project page and code are available at this https URL.

---


### 143. [Too Nice to Tell the Truth: Quantifying Agreeableness-Driven Sycophancy in Role-Playing Language Models](https://arxiv.org/abs/2604.10733)

**<font color=#1a73e8>作者：</font>** Arya Shah, Deepali Mishra, Chaklam Silpasuwanchai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as conversational agents that adopt personas and role-play characters at user request. This capability, while valuable, raises concerns about sycophancy: the tendency to provide responses that validate users rather than prioritize factual accuracy. While prior work has established that sycophancy poses risks to AI safety and alignment, the relationship between specific personality traits of adopted personas and the degree of sycophantic behavior remains unexplored. We present a systematic investigation of how persona agreeableness influences sycophancy across 13 small, open-weight language models ranging from 0.6B to 20B parameters. We develop a benchmark comprising 275 personas evaluated on NEO-IPIP agreeableness subscales and expose each persona to 4,950 sycophancy-eliciting prompts spanning 33 topic categories. Our analysis reveals that 9 of 13 models exhibit statistically significant positive correlations between persona agreeableness and sycophancy rates, with Pearson correlations reaching $r = 0.87$ and effect sizes as large as Cohen's $d = 2.33$. These findings demonstrate that agreeableness functions as a reliable predictor of persona-induced sycophancy, with direct implications for the deployment of role-playing AI systems and the development of alignment strategies that account for personality-mediated deceptive behaviors.

---


### 144. [Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS](https://arxiv.org/abs/2604.10734)

**<font color=#1a73e8>作者：</font>** Shijia Xu, Zhou Wu, Xiaolong Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) substantially extends the knowledge boundary of large language models. However, it still faces two major challenges when handling complex reasoning tasks: low context utilization and frequent hallucinations. To address these issues, we propose Self-Correcting RAG, a unified framework that reformulates retrieval and generation as constrained optimization and path planning. On the input side, we move beyond traditional greedy retrieval and, for the first time, formalize context selection as a multi-dimensional multiple-choice knapsack problem (MMKP), thereby maximizing information density and removing redundancy under a strict token budget. On the output side, we introduce a natural language inference (NLI)-guided Monte Carlo Tree Search (MCTS) mechanism, which leverages test-time compute to dynamically explore reasoning trajectories and validate the faithfulness of generated answers. Experiments on six multi-hop question answering and fact-checking datasets demonstrate that our method significantly improves reasoning accuracy on complex queries while effectively reducing hallucinations, outperforming strong existing this http URL code is available at this https URL .

---


### 145. [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](https://arxiv.org/abs/2604.10739)

**<font color=#1a73e8>作者：</font>** Shu Zhou, Rui Ling, Junan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling test-time compute through extended chains of thought has become a dominant paradigm for improving large language model reasoning. However, existing research implicitly assumes that longer thinking always yields better results. This assumption remains largely unexamined. We systematically investigate how the marginal utility of additional reasoning tokens changes as compute budgets increase. We find that marginal returns diminish substantially at higher budgets and that models exhibit ``overthinking'', where extended reasoning is associated with abandoning previously correct answers. Furthermore, we show that optimal thinking length varies across problem difficulty, suggesting that uniform compute allocation is suboptimal. Our cost-aware evaluation framework reveals that stopping at moderate budgets can reduce computation significantly while maintaining comparable accuracy.

---


### 146. [RCBSF: A Multi-Agent Framework for Automated Contract Revision via Stackelberg Game](https://arxiv.org/abs/2604.10740)

**<font color=#1a73e8>作者：</font>** Shijia Xu, Yu Wang, Xiaolong Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the widespread adoption of Large Language Models (LLMs) in Legal AI, their utility for automated contract revision remains impeded by hallucinated safety and a lack of rigorous behavioral constraints. To address these limitations, we propose the Risk-Constrained Bilevel Stackelberg Framework (RCBSF), which formulates revision as a non-cooperative Stackelberg game. RCBSF establishes a hierarchical Leader Follower structure where a Global Prescriptive Agent (GPA) imposes risk budgets upon a follower system constituted by a Constrained Revision Agent (CRA) and a Local Verification Agent (LVA) to iteratively optimize output. We provide theoretical guarantees that this bilevel formulation converges to an equilibrium yielding strictly superior utility over unguided configurations. Empirical validation on a unified benchmark demonstrates that RCBSF achieves state-of-the-art performance, surpassing iterative baselines with an average Risk Resolution Rate (RRR) of 84.21\% while enhancing token efficiency. Our code is available at this https URL .

---


### 147. [Deep-Reporter: Deep Research for Grounded Multimodal Long-Form Generation](https://arxiv.org/abs/2604.10741)

**<font color=#1a73e8>作者：</font>** Fangda Ye, Zhifei Xie, Yuxin Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent agentic search frameworks enable deep research via iterative planning and retrieval, reducing hallucinations and enhancing factual grounding. However, they remain text-centric, overlooking the multimodal evidence that characterizes real-world expert reports. We introduce a pressing task: multimodal long-form generation. Accordingly, we propose Deep-Reporter, a unified agentic framework for grounded multimodal long-form generation. It orchestrates: (i) Agentic Multimodal Search and Filtering to retrieve and filter textual passages and information-dense visuals; (ii) Checklist-Guided Incremental Synthesis to ensure coherent image-text integration and optimal citation placement; and (iii) Recurrent Context Management to balance long-range coherence with local fluency. We develop a rigorous curation pipeline producing 8K high-quality agentic traces for model optimization. We further introduce M2LongBench, a comprehensive testbed comprising 247 research tasks across 9 domains and a stable multimodal sandbox. Extensive experiments demonstrate that long-form multimodal generation is a challenging task, especially in multimodal selection and integration, and effective post-training can bridge the gap.

---


### 148. [How You Ask Matters! Adaptive RAG Robustness to Query Variations](https://arxiv.org/abs/2604.10745)

**<font color=#1a73e8>作者：</font>** Yunah Jang, Megha Sundriyal, Kyomin Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adaptive Retrieval-Augmented Generation (RAG) promises accuracy and efficiency by dynamically triggering retrieval only when needed and is widely used in practice. However, real-world queries vary in surface form even with the same intent, and their impact on Adaptive RAG remains under-explored. We introduce the first large-scale benchmark of diverse yet semantically identical query variations, combining human-written and model-generated rewrites. Our benchmark facilitates a systematic evaluation of Adaptive RAG robustness by examining its key components across three dimensions: answer quality, computational cost, and retrieval decisions. We discover a critical robustness gap, where small surface-level changes in queries dramatically alter retrieval behavior and accuracy. Although larger models show better performance, robustness does not improve accordingly. These findings reveal that Adaptive RAG methods are highly vulnerable to query variations that preserve identical semantics, exposing a critical robustness challenge.

---


### 149. [Generating Multiple-Choice Knowledge Questions with Interpretable Difficulty Estimation using Knowledge Graphs and Large Language Models](https://arxiv.org/abs/2604.10748)

**<font color=#1a73e8>作者：</font>** Mehmet Can Şakiroğlu, H. Altay Güvenir, Kamer Kaya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating multiple-choice questions (MCQs) with difficulty estimation remains challenging in automated MCQ-generation systems used in adaptive, AI-assisted education. This study proposes a novel methodology for generating MCQs with difficulty estimation from the input documents by utilizing knowledge graphs (KGs) and large language models (LLMs). Our approach uses an LLM to construct a KG from input documents, from which MCQs are then systematically generated. Each MCQ is generated by selecting a node from the KG as the key, sampling a related triple or quintuple -- optionally augmented with an extra triple -- and prompting an LLM to generate a corresponding stem from these graph components. Distractors are then selected from the KG. For each MCQ, nine difficulty signals are computed and combined into a unified difficulty score using a data-driven approach. Experimental results demonstrate that our method generates high-quality MCQs whose difficulty estimation is interpretable and aligns with human perceptions. Our approach improves automated MCQ generation by integrating structured knowledge representations with LLMs and a data-driven difficulty estimation model.

---


### 150. [MMRareBench: A Rare-Disease Multimodal and Multi-Image Medical Benchmark](https://arxiv.org/abs/2604.10755)

**<font color=#1a73e8>作者：</font>** Junzhi Ning, Jiashi Lin, Yingying Fang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have advanced clinical tasks for common conditions, but their performance on rare diseases remains largely untested. In rare-disease scenarios, clinicians often lack prior clinical knowledge, forcing them to rely strictly on case-level evidence for clinical judgments. Existing benchmarks predominantly evaluate common-condition, single-image settings, leaving multimodal and multi-image evidence integration under rare-disease data scarcity systematically unevaluated. We introduce MMRareBench, to our knowledge the first rare-disease benchmark jointly evaluating multimodal and multi-image clinical capability across four workflow-aligned tracks: diagnosis, treatment planning, cross-image evidence alignment, and examination suggestion. The benchmark comprises 1,756 question-answer pairs with 7,958 associated medical images curated from PMC case reports, with Orphanet-anchored ontology alignment, track-specific leakage control, evidence-grounded annotations, and a two-level evaluation protocol. A systematic evaluation of 23 MLLMs reveals fragmented capability profiles and universally low treatment-planning performance, with medical-domain models trailing general-purpose MLLMs substantially on multi-image tracks despite competitive diagnostic scores. These patterns are consistent with a capacity dilution effect: medical fine-tuning can narrow the diagnostic gap but may erode the compositional multi-image capability that rare-disease evidence integration demands.

---


### 151. [HOG-Layout: Hierarchical 3D Scene Generation, Optimization and Editing via Vision-Language Models](https://arxiv.org/abs/2604.10772)

**<font color=#1a73e8>作者：</font>** Haiyan Jiang, Deyu Zhang, Dongdong Weng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D layout generation and editing play a crucial role in Embodied AI and immersive VR interaction. However, manual creation requires tedious labor, while data-driven generation often lacks diversity. The emergence of large models introduces new possibilities for 3D scene synthesis. We present HOG-Layout that enables text-driven hierarchical scene generation, optimization and real-time scene editing with large language models (LLMs) and vision-language models (VLMs). HOG-Layout improves scene semantic consistency and plausibility through retrieval-augmented generation (RAG) technology, incorporates an optimization module to enhance physical consistency, and adopts a hierarchical representation to enhance inference and optimization, achieving real-time editing. Experimental results demonstrate that HOG-Layout produces more reasonable environments compared with existing baselines, while supporting fast and intuitive scene editing.

---


### 152. [TorchUMM: A Unified Multimodal Model Codebase for Evaluation, Analysis, and Post-training](https://arxiv.org/abs/2604.10784)

**<font color=#1a73e8>作者：</font>** Yinyi Luo, Wenwen Wang, Hayes Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in unified multimodal models (UMMs) have led to a proliferation of architectures capable of understanding, generating, and editing across visual and textual modalities. However, developing a unified framework for UMMs remains challenging due to the diversity of model architectures and the heterogeneity of training paradigms and implementation details. In this paper, we present TorchUMM, the first unified codebase for comprehensive evaluation, analysis, and post-training across diverse UMM backbones, tasks, and datasets. TorchUMM supports a broad spectrum of models covering a wide range of scales and design paradigms. Our benchmark encompasses three core task dimensions: multimodal understanding, generation, and editing, and integrates both established and novel datasets to evaluate perception, reasoning, compositionality, and instruction-following abilities. By providing a unified interface and standardized evaluation protocols, TorchUMM enables fair and reproducible comparisons across heterogeneous models and fosters deeper insights into their strengths and limitations, facilitating the development of more capable unified multimodal systems. Code is available at: this https URL.

---


### 153. [When Meaning Isn't Literal: Exploring Idiomatic Meaning Across Languages and Modalities](https://arxiv.org/abs/2604.10787)

**<font color=#1a73e8>作者：</font>** Sarmistha Das, Shreyas Guha, Suvrayan Bandyopadhyay 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Idiomatic reasoning, deeply intertwined with metaphor and culture, remains a blind spot for contemporary language models, whose progress skews toward surface-level lexical and semantic cues. For instance, the Bengali idiom \textit{\foreignlanguage{bengali}{\char"0986\char"0999\char"09CD\char"0997\char"09C1 \char"09B0 \char"09AB\char"09B2 \char"099F\char"0995}} (angur fol tok, ``grapes are sour''): it encodes denial-driven rationalization, yet naive models latch onto the literal fox-and-grape imagery. Addressing this oversight, we present ``Mediom,'' a multilingual, multimodal idiom corpus of 3,533 Hindi, Bengali, and Thai idioms, each paired with gold-standard explanations, cross-lingual translations, and carefully aligned text--image representations. We benchmark both large language models (textual reasoning) and vision-language models (figurative disambiguation) on Mediom, exposing systematic failures in metaphor comprehension. To mitigate these gaps, we propose ``HIDE,'' a Hinting-based Idiom Explanation framework that leverages error-feedback retrieval and targeted diagnostic cues for iterative reasoning refinement. Collectively, Mediom and HIDE establish a rigorous test bed and methodology for culturally grounded, multimodal idiom understanding embedded with reasoning hints in next-generation AI systems.

---


### 154. [TInR: Exploring Tool-Internalized Reasoning in Large Language Models](https://arxiv.org/abs/2604.10788)

**<font color=#1a73e8>作者：</font>** Qiancheng Xu, Yongqi Li, Fan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-Integrated Reasoning (TIR) has emerged as a promising direction by extending Large Language Models' (LLMs) capabilities with external tools during reasoning. Existing TIR methods typically rely on external tool documentation during reasoning. However, this leads to tool mastery difficulty, tool size constraints, and inference inefficiency. To mitigate these issues, we explore Tool-Internalized Reasoning (TInR), aiming at facilitating reasoning with tool knowledge internalized into LLMs. Achieving this goal presents notable requirements, including tool internalization and tool-reasoning coordination. To address them, we propose TInR-U, a tool-internalized reasoning framework for unified reasoning and tool usage. TInR-U is trained through a three-phase pipeline: 1) tool internalization with a bidirectional knowledge alignment strategy; 2) supervised fine-tuning warm-up using high-quality reasoning annotations, and 3) reinforcement learning with TInR-specific rewards. We comprehensively evaluate our method across in-domain and out-of-domain settings. Experiment results show that TInR-U achieves superior performance in both settings, highlighting its effectiveness and efficiency.

---


### 155. [ReplicateAnyScene: Zero-Shot Video-to-3D Composition via Textual-Visual-Spatial Alignment](https://arxiv.org/abs/2604.10789)

**<font color=#1a73e8>作者：</font>** Mingyu Dong, Chong Xia, Mingyuan Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans exhibit an innate capacity to rapidly perceive and segment objects from video observations, and even mentally assemble them into structured 3D scenes. Replicating such capability, termed compositional 3D reconstruction, is pivotal for the advancement of Spatial Intelligence and Embodied AI. However, existing methods struggle to achieve practical deployment due to the insufficient integration of cross-modal information, leaving them dependent on manual object prompting, reliant on auxiliary visual inputs, and restricted to overly simplistic scenes by training biases. To address these limitations, we propose ReplicateAnyScene, a framework capable of fully automated and zero-shot transformation of casually captured videos into compositional 3D scenes. Specifically, our pipeline incorporates a five-stage cascade to extract and structurally align generic priors from vision foundation models across textual, visual, and spatial dimensions, grounding them into structured 3D representations and ensuring semantic coherence and physical plausibility of the constructed scenes. To facilitate a more comprehensive evaluation of this task, we further introduce the C3DR benchmark to assess reconstruction quality from diverse aspects. Extensive experiments demonstrate the superiority of our method over existing baselines in generating high-quality compositional 3D scenes.

---


### 156. [Advancing Polish Language Modeling through Tokenizer Optimization in the Bielik v3 7B and 11B Series](https://arxiv.org/abs/2604.10799)

**<font color=#1a73e8>作者：</font>** Krzysztof Ociepa, Łukasz Flis, Remigiusz Kinas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of the Bielik v3 PL series, encompassing both the 7B and 11B parameter variants, represents a significant milestone in the field of language-specific large language model (LLM) optimization. While general-purpose models often demonstrate impressive multilingual capabilities, they frequently suffer from a fundamental architectural inefficiency: the use of universal tokenizers. These tokenizers, typically designed to cover a broad spectrum of languages, often fail to capture the morphological nuances of specific languages like Polish, leading to higher fertility ratios, increased inference costs, and restricted effective context windows. This report details the transition from the universal Mistral-based tokenization to a dedicated Polish-optimized vocabulary for the Bielik v3 models, exploring the FOCUS-based embedding initialization, the multi-stage pretraining curriculum, and the subsequent post-training alignment involving Supervised Fine-Tuning, Direct Preference Optimization, and Reinforcement Learning through Group Relative Policy Optimization with verifiable rewards.

---


### 157. [Online Covariance Estimation in Averaged SGD: Improved Batch-Mean Rates and Minimax Optimality via Trajectory Regression](https://arxiv.org/abs/2604.10814)

**<font color=#1a73e8>作者：</font>** Yijin Ni, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online covariance matrix estimation for Polyak--Ruppert averaged stochastic gradient descent (SGD). The online batch-means estimator of Zhu, Chen and Wu (2023) achieves an operator-norm convergence rate of $O(n^{-(1-\alpha)/4})$, which yields $O(n^{-1/8})$ at the optimal learning-rate exponent $\alpha \rightarrow 1/2^+$. A rigorous per-block bias analysis reveals that re-tuning the block-growth parameter improves the batch-means rate to $O(n^{-(1-\alpha)/3})$, achieving $O(n^{-1/6})$. The modified estimator requires no Hessian access and preserves $O(d^2)$ memory. We provide a complete error decomposition into variance, stationarity bias, and nonlinearity bias components. A weighted-averaging variant that avoids hard truncation is also discussed. We establish the minimax rate $\Theta(n^{-(1-\alpha)/2})$ for Hessian-free covariance estimation from the SGD trajectory: a Le Cam lower bound gives $\Omega(n^{-(1-\alpha)/2})$, and a trajectory-regression estimator--which estimates the Hessian by regressing SGD increments on iterates--achieves $O(n^{-(1-\alpha)/2})$, matching the lower bound. The construction reveals that the bottleneck is the sublinear accumulation of information about the Hessian from the SGD drift.

---


### 158. [CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms](https://arxiv.org/abs/2604.10825)

**<font color=#1a73e8>作者：</font>** Zacharie Bugaud  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce CheeseBench, a benchmark that evaluates large language models (LLMs) on nine classical behavioral neuroscience paradigms (Morris water maze, Barnes maze, T-maze, radial arm maze, star maze, operant chamber, shuttle box, conditioned place preference, and delayed non-match to sample), spanning six cognitive dimensions. Each task is grounded in peer-reviewed rodent protocols with approximate animal baselines. The agent receives a unified system prompt with no task-specific instructions and must discover goals purely from ASCII text observations and reward signals, much like a rodent placed into an unfamiliar apparatus. We evaluate six open-weight LLMs (3B to 72B parameters) on text-based ASCII renderings and compare against both a random baseline and a graph-based reinforcement learning agent. Our best model (Qwen2.5-VL-7B) reaches 52.6% average success on ASCII input, compared to 32.1% for random agents and 78.9% for approximate rodent baselines. We find that (1) scaling beyond 7B yields diminishing returns, (2) longer context history degrades performance, (3) chain-of-thought prompting hurts rather than helps, and (4) a vision-language architecture provides an advantage at 7B but hurts at 32B. Because the same model's performance ranges from 20% to 57% depending on interface parameters alone, these results characterize the agent-plus-interface system, not the model in isolation. Under this unified zero-shot ASCII protocol, current open-weight LLM agents remain well below approximate rodent reference values, particularly on tasks requiring spatial navigation and within-trial state tracking.

---


### 159. [OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language World Models](https://arxiv.org/abs/2604.10866)

**<font color=#1a73e8>作者：</font>** Xiaomeng Hu, Yinger Zhang, Fei Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents are expected to perform professional work across hundreds of occupational domains (from emergency department triage to nuclear reactor safety monitoring to customs import processing), yet existing benchmarks can only evaluate agents in the few domains where public environments exist. We introduce OccuBench, a benchmark covering 100 real-world professional task scenarios across 10 industry categories and 65 specialized domains, enabled by Language World Models (LWMs) that simulate domain-specific environments through LLM-driven tool response generation. Our multi-agent synthesis pipeline automatically produces evaluation instances with guaranteed solvability, calibrated difficulty, and document-grounded diversity. OccuBench evaluates agents along two complementary dimensions: task completion across professional domains and environmental robustness under controlled fault injection (explicit errors, implicit data degradation, and mixed faults). We evaluate 15 frontier models across 8 model families and find that: (1) no single model dominates all industries, as each has a distinct occupational capability profile; (2) implicit faults (truncated data, missing fields) are harder than both explicit errors (timeouts, 500s) and mixed faults, because they lack overt error signals and require the agent to independently detect data degradation; (3) larger models, newer generations, and higher reasoning effort consistently improve performance. GPT-5.2 improves by 27.5 points from minimal to maximum reasoning effort; and (4) strong agents are not necessarily strong environment simulators. Simulator quality is critical for LWM-based evaluation reliability. OccuBench provides the first systematic cross-industry evaluation of AI agents on professional occupational tasks.

---


### 160. [AOP-Smart: A RAG-Enhanced Large Language Model Framework for Adverse Outcome Pathway Analysis](https://arxiv.org/abs/2604.10874)

**<font color=#1a73e8>作者：</font>** Qinjiang Niu, Lu Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adverse Outcome Pathways (AOPs) are an important knowledge framework in toxicological research and risk assessment. In recent years, large language models (LLMs) have gradually been applied to AOP-related question answering and mechanistic reasoning tasks. However, due to the existence of the hallucination problem, that is, the model may generate content that is inconsistent with facts or lacks evidence, their reliability is still limited. To address this issue, this study proposes an AOP-oriented Retrieval-Augmented Generation (RAG) framework, AOP-Smart. Based on the official XML data from AOP-Wiki, this method uses Key Events (KEs), Key Event Relationships (KERs), and specific AOP information to retrieve relevant knowledge for user questions, thereby improving the reliability of the generated results of large language models. To evaluate the effectiveness of the proposed method, this study constructed a test set containing 20 AOP-related question answering tasks, covering KE identification, upstream and downstream KE retrieval, and complex AOP retrieval tasks. Experiments were conducted on three mainstream large language models, Gemini, DeepSeek, and ChatGPT, and comparative tests were performed under two settings: without RAG and with RAG. The experimental results show that, without using RAG, the accuracies of GPT, DeepSeek, and Gemini were 15.0\%, 35.0\%, and 20.0\%, respectively; after using RAG, their accuracies increased to 95.0\%, 100.0\%, and 95.0\%, respectively. The results indicate that AOP-Smart can significantly alleviate the hallucination problem of large language models in AOP knowledge tasks, and greatly improve the accuracy and consistency of their answers.

---


### 161. [ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval](https://arxiv.org/abs/2604.10898)

**<font color=#1a73e8>作者：</font>** David H. Yang, Yuxuan Zhu, Mohammad Mohammadi Amiri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown great performance on complex reasoning tasks but often require generating long intermediate thoughts before reaching a final answer. During generation, LLMs rely on a key-value (KV) cache for autoregressive decoding. However, the memory footprint of the KV cache grows with output length. Prior work on KV cache optimization mostly focus on compressing the long input context, while retaining the full KV cache for decoding. For tasks requiring long output generation, this leads to increased computational and memory costs. In this paper, we introduce ZoomR, a novel approach that enables LLMs to adaptively compress verbose reasoning thoughts into summaries and uses a dynamic KV cache selection policy that leverages these summaries while also strategically "zooming in" on fine-grained details. By using summary keys as a coarse-grained index during decoding, ZoomR uses the query to retrieve details for only the most important thoughts. This hierarchical strategy significantly reduces memory usage by avoiding full-cache attention at each step. Experiments across math and reasoning tasks show that our approach achieves competitive performance compared to baselines, while reducing inference memory requirements by more than $4\times$. These results demonstrate that a multi-granularity KV selection enables more memory efficient decoding, especially for long output generation.

---


### 162. [ReXSonoVQA: A Video QA Benchmark for Procedure-Centric Ultrasound Understanding](https://arxiv.org/abs/2604.10916)

**<font color=#1a73e8>作者：</font>** Xucheng Wang, Xiaoman Zhang, Sung Eun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound acquisition requires skilled probe manipulation and real-time adjustments. Vision-language models (VLMs) could enable autonomous ultrasound systems, but existing benchmarks evaluate only static images, not dynamic procedural understanding. We introduce ReXSonoVQA, a video QA benchmark with 514 video clips and 514 questions (249 MCQ, 265 free-response) targeting three competencies: Action-Goal Reasoning, Artifact Resolution & Optimization, and Procedure Context & Planning. Zero-shot evaluation of Gemini 3 Pro, Qwen3.5-397B, LLaVA-Video-72B, and Seed 2.0 Pro shows VLMs can extract some procedural information, but troubleshooting questions remain challenging with minimal gains over text-only baselines, exposing limitations in causal reasoning. ReXSonoVQA enables developing perception systems for ultrasound training, guidance, and robotic automation.

---


### 163. [HTAA: Enhancing LLM Planning via Hybrid Toolset Agentization & Adaptation](https://arxiv.org/abs/2604.10917)

**<font color=#1a73e8>作者：</font>** Chengrui Huang, Junshuo Zhang, Zhiyuan Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enabling large language models to scale and reliably use hundreds of tools is critical for real-world applications, yet challenging due to the inefficiency and error accumulation inherent in flat tool-calling architectures. To address this, we propose Hybrid Toolset Agentization & Adaptation (HTAA), a hierarchical framework for scalable tool-use planning. We propose a novel toolset agentization paradigm, which encapsulates frequently co-used tools into specialized agent tools, thereby reducing the planner's action space and mitigating redundancy. To ensure effective coordination, we design Asymmetric Planner Adaptation, a trajectory-based training paradigm that aligns the high-level planner with agent tools via backward reconstruction and forward refinement. To validate the performance of HTAA, we conduct experiments on a real-world internal dataset, InfoVerify, based on the POI validation workflow of China's largest online large-scale ride-hailing platform, featuring long-horizon executable tool trajectories. Experiments on InfoVerify and widely-used benchmarks show that HTAA consistently achieves higher task success rates, requires short tool calling trajectories, and significantly reduces context overhead compared to strong baselines. Furthermore, in a production deployment, HTAA substantially reduces manual validation effort and operational cost, demonstrating its practical efficacy.

---


### 164. [CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation](https://arxiv.org/abs/2604.10918)

**<font color=#1a73e8>作者：</font>** Yunfan Yang, Cuiling Lan, Jitao Sang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tables contain rich structured information, yet when stored as images their contents remain "locked" within pixels. Converting table images into LaTeX code enables faithful digitization and reuse, but current multimodal large language models (MLLMs) often fail to preserve structural, style, or content fidelity. Conventional post-training with reinforcement learning (RL) typically relies on a single aggregated reward, leading to reward ambiguity that conflates multiple behavioral aspects and hinders effective optimization. We propose Component-Specific Policy Optimization (CSPO), an RL framework that disentangles optimization across LaTeX tables components-structure, style, and content. In particular, CSPO assigns component-specific rewards and backpropagates each signal only through the tokens relevant to its component, alleviating reward ambiguity and enabling targeted component-wise optimization. To comprehensively assess performance, we introduce a set of hierarchical evaluation metrics. Extensive experiments demonstrate the effectiveness of CSPO, underscoring the importance of component-specific optimization for reliable structured generation.

---


### 165. [Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](https://arxiv.org/abs/2604.10923)

**<font color=#1a73e8>作者：</font>** Zihao Cheng, Zeming Liu, Yingyu Shan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language model--powered agents can self-evolve by accumulating experience or by dynamically creating new assets (i.e., tools or expert agents), existing frameworks typically treat these two evolutionary processes in isolation. This separation overlooks their intrinsic interdependence: the former is inherently bounded by a manually predefined static toolset, while the latter generates new assets from scratch without experiential guidance, leading to limited capability growth and unstable evolution. To address this limitation, we introduce a novel paradigm of co-evolutionary Capability Expansion and Experience Distillation. Guided by this paradigm, we propose the \textbf{Mem$^{\textbf{2}}$Evolve}, which integrates two core components: \textbf{Experience Memory} and \textbf{Asset Memory}. Specifically, Mem$^{2}$Evolve leverages accumulated experience to guide the dynamic creation of assets, thereby expanding the agent's capability space while simultaneously acquiring new experience to achieve co-evolution. Extensive experiments across 6 task categories and 8 benchmarks demonstrate that Mem$^{2}$Evolve achieves improvement of 18.53\% over standard LLMs, 11.80\% over agents evolving solely through experience, and 6.46\% over those evolving solely through asset creation, establishing it as a substantially more effective and stable self-evolving agent framework. Code is available at: this https URL.

---


### 166. [From Words to Widgets for Controllable LLM Generation](https://arxiv.org/abs/2604.10925)

**<font color=#1a73e8>作者：</font>** Chao Zhang, Yiren Liu, Lunyiu Nie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Natural language remains the predominant way people interact with large language models (LLMs). However, users often struggle to precisely express and control subjective preferences (e.g., tone, style, and emphasis) through prompting. We propose Malleable Prompting, a new interactive prompting technique for controllable LLM generation. It reifies preference expressions in natural language prompts into GUI widgets (e.g., sliders, dropdowns, and toggles) that users can directly configure to steer generation, while visualizing each control's influence on the output to support attribution and comparison across iterations. To enable this interaction, we introduce an LLM decoding algorithm that modulates the token probability distribution during generation based on preference expressions and their widget values. Through a user study, we show that Malleable Prompting helps participants achieve target preferences more precisely and is perceived as more controllable and transparent than natural language prompting alone.

---


### 167. [AgentWebBench: Benchmarking Multi-Agent Coordination in Agentic Web](https://arxiv.org/abs/2604.10938)

**<font color=#1a73e8>作者：</font>** Shanshan Zhong, Kate Shen, Chenyan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic Web is an emerging paradigm where autonomous agents help users use online information. As the paradigm develops, content providers are also deploying agents to manage their data and serve it through controlled interfaces. This shift moves information access from centralized retrieval to decentralized coordination. To study this setting, we introduce AgentWebBench, a benchmark that evaluates how well a user agent synthesizes answers by interacting with website-specific content agents. We evaluate four tasks that cover common web information needs, spanning ranked retrieval (web search, web recommendation) and open-ended synthesis (question answering, deep research). Across seven advanced LLMs and three coordination strategies, multi-agent coordination generally lags behind centralized retrieval as expected, because user agent cannot directly access the corpus, but the gap shrinks with model scale and can even outperform centralized retrieval on question answering. This benchmark also enables us to study properties of the emerging paradigm of the digital world. We find that decentralized access concentrates traffic toward a small set of websites, test time scaling improves both interaction reliability and task performance, and strong results require sufficient interactions guided by careful planning. Finally, our failure analysis suggests that user agents need better planning and answer synthesis, while content agents need more reliable retrieval and evidence quality. Code, data, and APIs are released on this https URL.

---


### 168. [Learning to Adapt: In-Context Learning Beyond Stationarity](https://arxiv.org/abs/2604.10946)

**<font color=#1a73e8>作者：</font>** Zhen Qin, Jiachen Jiang, Zhihui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer models have become foundational across a wide range of scientific and engineering domains due to their strong empirical performance. A key capability underlying their success is in-context learning (ICL): when presented with a short prompt from an unseen task, transformers can perform per-token and next-token predictions without any parameter updates. Recent theoretical efforts have begun to uncover the mechanisms behind this phenomenon, particularly in supervised regression settings. However, these analyses predominantly assume stationary task distributions, which overlook a broad class of real-world scenarios where the target function varies over time. In this work, we bridge this gap by providing a theoretical analysis of ICL under non-stationary regression problems. We study how the gated linear attention (GLA) mechanism adapts to evolving input-output relationships and rigorously characterize its advantages over standard linear attention in this dynamic setting. To model non-stationarity, we adopt a first-order autoregressive process and show that GLA achieves lower training and testing errors by adaptively modulating the influence of past inputs -- effectively implementing a learnable recency bias. Our theoretical findings are further supported by empirical results, which validate the benefits of gating mechanisms in non-stationary ICL tasks.

---


### 169. [Pseudo-Unification: Entropy Probing Reveals Divergent Information Patterns in Unified Multimodal Models](https://arxiv.org/abs/2604.10949)

**<font color=#1a73e8>作者：</font>** Songlin Yang, Xianghao Kong, Anyi Rao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) were designed to combine the reasoning ability of large language models (LLMs) with the generation capability of vision models. In practice, however, this synergy remains elusive: UMMs fail to transfer LLM-like reasoning to image synthesis and exhibit divergent response behaviors. We term this phenomenon pseudo-unification. Diagnosing its internal causes is important, but existing probing methods either lack model-internal insight or ignore prompt-response dependencies. To address these limitations, we propose an information-theoretic probing framework that jointly analyzes how UMMs encode inputs and generate outputs. Applied to ten representative UMMs, our framework reveals that pseudo-unification stems from a dual divergence: (i) Modality-Asymmetric Encoding, where vision and language follow different entropy trajectories, and (ii) Pattern-Split Response, where text generation exhibits high-entropy creativity while image synthesis enforces low-entropy fidelity. Only models that unify both sides (e.g., via contextual prediction) achieve more genuine unification, enabling stronger reasoning-based text-to-image generation even with fewer parameters. Our work provides the first model-internal probing of unification, demonstrating that real multimodal synergy requires consistency in information flow, not just shared parameters.

---


### 170. [RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation](https://arxiv.org/abs/2604.10960)

**<font color=#1a73e8>作者：</font>** Zhiyi Duan, Hongyu Yuan, Rui Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Tracing (KT) infers a student's knowledge state from past interactions to predict future performance. Conventional Deep Learning (DL)-based KT models are typically tied to platform-specific identifiers and latent representations, making them hard to transfer and interpret. Large Language Model (LLM)-based methods can be either ungrounded under prompting or overly domain-dependent under fine-tuning. In addition, most existing KT methods are developed and evaluated under a same-distribution assumption. In real deployments, educational data often arise from heterogeneous platforms with substantial distribution shift, which often degrades generalization. To this end, we propose RAG-KT, a retrieval-augmented paradigm that frames cross-platform KT as reliable context constrained inference with LLMs. It builds a unified multi-source structured context with cross-source alignment via Question Group abstractions and retrieves complementary rich and reliable context for each prediction, enabling grounded prediction and interpretable diagnosis. Experiments on three public KT benchmarks demonstrate consistent gains in accuracy and robustness, including strong performance under cross-platform conditions.

---


### 171. [Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models](https://arxiv.org/abs/2604.10963)

**<font color=#1a73e8>作者：</font>** Ruiyang Li, Fang Liu, Licheng Jiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation supports clinical workflows by precisely delineating anatomical structures and lesions. However, medical image datasets medical image datasets suffer from acquisition noise and annotation ambiguity, causing pervasive data uncertainty that substantially undermines model robustness. Existing research focuses primarily on model architectural improvements and predictive reliability estimation, while systematic exploration of the intrinsic data uncertainty remains insufficient. To address this gap, this work proposes leveraging the universal representation capabilities of visual foundation models to estimate inherent data uncertainty. Specifically, we analyze the feature diversity of the model's decoded representations and quantify their singular value energy to define the semantic perception scale for each class, thereby measuring sample difficulty and aleatoric uncertainty. Based on this foundation, we design two uncertainty-driven application strategies: (1) the aleatoric uncertainty-aware data filtering mechanism to eliminate potentially noisy samples and enhance model learning quality; (2) the dynamic uncertainty-aware optimization strategy that adaptively adjusts class-specific loss weights during training based on the semantic perception scale, combined with a label denoising mechanism to improve training stability. Experimental results on five public datasets encompassing CT and MRI modalities and involving multi-organ and tumor segmentation tasks demonstrate that our method achieves significant and robust performance improvements across various mainstream network architectures, revealing the broad application potential of aleatoric uncertainty in medical image understanding and segmentation tasks.

---


### 172. [MMR-AD: A Large-Scale Multimodal Dataset for Benchmarking General Anomaly Detection with Multimodal Large Language Models](https://arxiv.org/abs/2604.10971)

**<font color=#1a73e8>作者：</font>** Xincheng Yao, Zefeng Qian, Chao Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the progress of industrial anomaly detection, general anomaly detection (GAD) is an emerging trend and also the ultimate goal. Unlike the conventional single- and multi-class AD, general AD aims to train a general AD model that can directly detect anomalies in diverse novel classes without any retraining or fine-tuning on the target data. Recently, Multimodal Large Language Models (MLLMs) have shown great promise in achieving general anomaly detection due to their revolutionary visual understanding and language reasoning capabilities. However, MLLM's general AD ability remains underexplored due to: (1) MLLMs are pretrained on amounts of data sourced from the Web, these data still have significant gaps with the data in AD scenarios. Moreover, the image-text pairs during pretraining are also not specifically for AD tasks. (2) The current mainstream AD datasets are image-based and not yet suitable for post-training MLLMs. To facilitate MLLM-based general AD research, we present MMR-AD, which is a comprehensive benchmark for both training and evaluating MLLM-based AD models. With MMR-AD, we reveal that the AD performance of current SOTA generalist MLLMs still falls far behind the industrial requirements. Based on MMR-AD, we also propose a baseline model, Anomaly-R1, which is a reasoning-based AD model that learns from the CoT data in MMR-AD and is further enhanced by reinforcement learning. Extensive experiments show that our Anomaly-R1 achieves remarkable improvements over generalist MLLMs in both anomaly detection and localization.

---


### 173. [CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning](https://arxiv.org/abs/2604.10973)

**<font color=#1a73e8>作者：</font>** Qixian Huang, Hongqiang Lin, Tong Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning over tabular data is a crucial capability for tasks like question answering and fact verification, as it requires models to comprehend both free-form questions and semi-structured tables. However, while methods like Chain-of-Thought (CoT) introduce reasoning chains, purely symbolic methodes are inherently limited by their blindness to holistic visual patterns. To address this, we propose the Coarse-to-Fine Multimodal Synthesis framework (CFMS), a novel two-stage paradigm that hierarchically decouples high-level visual perception from granular symbolic reasoning. In the Coarse Stage, CFMS leverages the Multimodal Large Language Models (MLLMs) to perform a one-time synthesis of a multi-perspective knowledge tuple. This tuple subsequently serves as a dynamic reasoning map to guide the fine stage, where a symbolic engine executes a targeted and efficient sequence of iterative operations over the table. Extensive experiments on the WikiTQ and TabFact benchmarks demonstrate that CFMS achieves competitive accuracy. The framework exhibits particular robustness when handling large tables and when instantiated with smaller backbone models, validating its effectiveness and generalizability.

---


### 174. [ATANT v1.1: Positioning Continuity Evaluation Against Memory, Long-Context, and Agentic-Memory Benchmarks](https://arxiv.org/abs/2604.10981)

**<font color=#1a73e8>作者：</font>** Samuel Sameer Tanguturi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ATANT v1.0 (arXiv:2604.06710) defined continuity as a system property with 7 required properties and introduced a 10-checkpoint, LLM-free evaluation methodology validated on a 250-story corpus. Since publication, a recurring reviewer and practitioner question has concerned not the framework itself but its relationship to a wider set of memory evaluations: LOCOMO, LongMemEval, BEAM, MemoryBench, Zep's evaluation suite, Letta/MemGPT's evaluations, and RULER. This companion paper, v1.1, does not modify the v1.0 standard. It closes a related-work gap that v1.0 left brief under page limits. We show by structural analysis that none of these benchmarks measures continuity as defined in v1.0: of the 7 required properties, the median existing eval covers 1 property, the mean covers 0.43 when partial credit is scored at 0.5, and no eval covers more than 2. We provide a cell-by-cell property-coverage matrix, identify methodological defects specific to each benchmark (including an empty-gold scoring bug in the LOCOMO reference implementation that renders 23% of its corpus unscorable by construction), and publish our reference implementation's LOCOMO score (8.8%) alongside the structural reason that number is uninformative about continuity. We publish our 8.8% LOCOMO score alongside our 96% ATANT cumulative-scale score as a calibration pair: the 87-point divergence is evidence that the two benchmarks measure different properties, not that one system is an order of magnitude better than another. The position v1.1 takes is not adversarial: each benchmark measures a real capability. The claim is that none of them can adjudicate continuity, and conflating them with continuity evaluation has led the field to under-invest in the properties v1.0 names.

---


### 175. [Back to the Barn with LLAMAs: Evolving Pretrained LLM Backbones in Finetuning Vision Language Models](https://arxiv.org/abs/2604.10985)

**<font color=#1a73e8>作者：</font>** Sameera Horawalavithana, Lauren Phillips, Ian Stewart 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have rapidly advanced by leveraging powerful pre-trained Large Language Models (LLMs) as core reasoning backbones. As new and more capable LLMs emerge with improved reasoning, instruction-following, and generalization, there is a pressing need to efficiently update existing VLMs to incorporate these advancements. However, the integration of new LLMs into VLMs, particularly how the evolving LLMs contribute to multimodal reasoning, alignment, and task-specific performance remains underexplored. Addressing this gap is important for VLM development, given the rapid evolution of pretrained LLM backbones. This study presents a controlled and systematic investigation of how changes in the pretrained LLM backbone affect downstream VLM task performance. By having the vision encoder, training data, and post-training algorithm remain same across LLAMA-1, LLAMA-2, and LLAMA-3 based VLMs, we find that newer LLM backbones do not always lead to better VLMs, but the performance depends on the downstream VLM task. For example, in visual question and answering tasks, newer LLM backbones tend to solve different questions rather than just more questions, and our analysis shows this is driven by differences in how the models process information, including better calibrated confidence and more stable internal representations. We also find that some VLM capabilities appear only in the newest LLM generation, while tasks that depend mainly on visual understanding see little benefit from a newer LLM backbone.

---


### 176. [MAFIG: Multi-agent Driven Formal Instruction Generation Framework](https://arxiv.org/abs/2604.10989)

**<font color=#1a73e8>作者：</font>** Shixing Zhao, Zheng Si, Pengpeng Ouyang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergency situations in scheduling systems often trigger local functional failures that undermine system stability and even cause system collapse. Existing methods primarily rely on robust scheduling or reactive scheduling, handling emergencies through predefined rules or rescheduling strategies. However, the diversity and unpredictability of real-world emergencies make them difficult to anticipate, which limits the adaptability of these methods in complex scenarios. Recent studies have shown that Large Language Models (LLMs) possess strong potential for complex scheduling tasks because of their extensive prior knowledge and strong reasoning capabilities. Nevertheless, the high inference latency of LLMs and the lengthy contextual information of scheduling systems significantly hinder their application for emergency handling. To mitigate these issues, we propose the Multi-agent Driven Formal Instruction Generation Framework (MAFIG). The framework constrains the decision scope to local functional modules affected by emergency situations and repairs scheduling logic rapidly by generating formal instructions. MAFIG contains a Perception Agent and an Emergency Decision Agent, which mitigates the adverse impact of lengthy system contexts on emergency decision-making. We further introduce span-focused loss-driven local distillation mechanism (SFL) to transfer the decision-making capability of powerful Cloud Large Language Models (C-LLMs) to lightweight local models, reducing inference latency while preserving decision-making effectiveness. Experiments in the Port, Warehousing, and Deck scheduling datasets show success rates of 98.49\%, 94.97\%, and 97.50\%, with average processing times of 0.33 s, 0.23 s, and 0.19 s. These results demonstrate that MAFIG effectively mitigates the impact of emergencies and improves the robustness and adaptability of scheduling systems.

---


### 177. [When Valid Signals Fail: Regime Boundaries Between LLM Features and RL Trading Policies](https://arxiv.org/abs/2604.10996)

**<font color=#1a73e8>作者：</font>** Zhengzhe Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can large language models (LLMs) generate continuous numerical features that improve reinforcement learning (RL) trading agents? We build a modular pipeline where a frozen LLM serves as a stateless feature extractor, transforming unstructured daily news and filings into a fixed-dimensional vector consumed by a downstream PPO agent. We introduce an automated prompt-optimization loop that treats the extraction prompt as a discrete hyperparameter and tunes it directly against the Information Coefficient - the Spearman rank correlation between predicted and realized returns - rather than NLP losses. The optimized prompt discovers genuinely predictive features (IC above 0.15 on held-out data). However, these valid intermediate representations do not automatically translate into downstream task performance: during a distribution shift caused by a macroeconomic shock, LLM-derived features add noise, and the augmented agent under-performs a price-only baseline. In a calmer test regime the agent recovers, yet macroeconomic state variables remain the most robust driver of policy improvement. Our findings highlight a gap between feature-level validity and policy-level robustness that parallels known challenges in transfer learning under distribution shift.

---


### 178. [TraversalBench: Challenging Paths to Follow for Vision Language Models](https://arxiv.org/abs/2604.10999)

**<font color=#1a73e8>作者：</font>** Clara Petrova, Zhuo Chen, Marin Soljačić  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) perform strongly on many multimodal benchmarks. However, the ability to follow complex visual paths -- a task that human observers typically find straightforward -- remains under-tested. We introduce TraversalBench, a controlled benchmark for exact visual path traversal. Each instance contains a single continuous polyline, a unique start marker, and markers placed at path vertices; the task is to recover the exact ordered sequence encountered when traversing the path from start to finish. The benchmark explicitly balances key path-structural factors including self-intersection count, tortuosity, vertex count, and nearby confounding lines, while minimizing reliance on OCR, world knowledge, and open-ended planning. We find that self-intersections are the dominant source of difficulty. A first-crossing analysis shows that errors are sharply localized: performance is relatively stable immediately before the first crossing, then drops steeply when the model must resolve the correct continuation. By contrast, nearby confounding lines produce a weaker persistent degradation that compounds with repeated exposure. These analyses make TraversalBench a useful diagnostic for identifying whether models suffer from human-like failures or other breakdowns in sustained visual processing. An auxiliary reading-order benchmark further reveals a consistent preference for layouts compatible with left-to-right serialization, while not explaining away the main effects of path complexity. Together, these results position TraversalBench as a controlled diagnostic of path-faithful visual reasoning and as a useful testbed for studying multimodal spatial reasoning under ambiguity, clutter, and distractor structure. More broadly, we position TraversalBench as a contribution to the still-limited area of sustained visual grounding benchmarks for VLMs.

---


### 179. [Flow-Controlled Scheduling for LLM Inference with Provable Stability Guarantees](https://arxiv.org/abs/2604.11001)

**<font color=#1a73e8>作者：</font>** Zhuolun Dong, Junyu Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been widely adopted due to their great performance across a wide range of applications. ChatGPT and Gemini now serve hundreds of millions of active users and handle billions of user requests per day, which puts optimizing LLM inference into the spotlight. A key challenge in LLM inference is that decode lengths are unknown. The memory usage for each request grows with generated tokens, which may lead to overflow and cause system instability. To address this concern, we propose a simple flow-control framework that controls the rate at which prompts join the active set. We derive a necessary condition that any stable system must satisfy and establish sufficient conditions under which our algorithm provably achieves stability. Experiments show that, compared to commonly used strategies in practice, our approach achieves higher token and request throughput, lower average and tail latency, and more stable KV cache utilization.

---


### 180. [Sanity Checks for Agentic Data Science](https://arxiv.org/abs/2604.11003)

**<font color=#1a73e8>作者：</font>** Zachary T. Rewolinski, Austin V. Zane, Hao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic data science (ADS) pipelines have grown rapidly in both capability and adoption, with systems such as OpenAI Codex now able to directly analyze datasets and produce answers to statistical questions. However, these systems can reach falsely optimistic conclusions that are difficult for users to detect. To address this, we propose a pair of lightweight sanity checks grounded in the Predictability-Computability-Stability (PCS) framework for veridical data science. These checks use reasonable perturbations to screen whether an agent can reliably distinguish signal from noise, acting as a falsifiability constraint that can expose affirmative conclusions as unsupported. Together, the two checks characterize the trustworthiness of an ADS output, e.g. whether it has found stable signal, is responding to noise, or is sensitive to incidental aspects of the input. We validate the approach on synthetic data with controlled signal-to-noise ratios, confirming that the sanity checks track ground-truth signal strength. We then demonstrate the checks on 11 real-world datasets using OpenAI Codex, characterizing the trustworthiness of each conclusion and finding that in 6 of the datasets an affirmative conclusion is not well-supported, even though a single ADS run may support one. We further analyze failure modes of ADS systems and find that ADS self-reported confidence is poorly calibrated to the empirical stability of its conclusions.

---


### 181. [Panoptic Pairwise Distortion Graph](https://arxiv.org/abs/2604.11004)

**<font color=#1a73e8>作者：</font>** Muhammad Kamran Janjua, Abdul Wahab, Bahador Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce a new perspective on comparative image assessment by representing an image pair as a structured composition of its regions. In contrast, existing methods focus on whole image analysis, while implicitly relying on region-level understanding. We extend the intra-image notion of a scene graph to inter-image, and propose a novel task of Distortion Graph (DG). DG treats paired images as a structured topology grounded in regions, and represents dense degradation information such as distortion type, severity, comparison and quality score in a compact interpretable graph structure. To realize the task of learning a distortion graph, we contribute (i) a region-level dataset, PandaSet, (ii) a benchmark suite, PandaBench, with varying region-level difficulty, and (iii) an efficient architecture, Panda, to generate distortion graphs. We demonstrate that PandaBench poses a significant challenge for state-of-the-art multimodal large language models (MLLMs) as they fail to understand region-level degradations even when fed with explicit region cues. We show that training on PandaSet or prompting with DG elicits region-wise distortion understanding, opening a new direction for fine-grained, structured pairwise image assessment.

---


### 182. [Diffusion-CAM: Faithful Visual Explanations for dMLLMs](https://arxiv.org/abs/2604.11005)

**<font color=#1a73e8>作者：</font>** Haomin Zuo, Yidi Li, Luoxiao Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While diffusion Multimodal Large Language Models (dMLLMs) have recently achieved remarkable strides in multimodal generation, the development of interpretability mechanisms has lagged behind their architectural evolution. Unlike traditional autoregressive models that produce sequential activations, diffusion-based architectures generate tokens via parallel denoising, resulting in smooth, distributed activation patterns across the entire sequence. Consequently, existing Class Activation Mapping (CAM) methods, which are tailored for local, sequential dependencies, are ill-suited for interpreting these non-autoregressive behaviors. To bridge this gap, we propose Diffusion-CAM, the first interpretability method specifically tailored for dMLLMs. We derive raw activation maps by differentiably probing intermediate representations in the transformer backbone, accordingly capturing both latent features and their class-specific gradients. To address the inherent stochasticity of these raw signals, we incorporate four key modules to resolve spatial ambiguity and mitigate intra-image confounders and redundant token correlations. Extensive experiments demonstrate that Diffusion-CAM significantly outperforms SoTA methods in both localization accuracy and visual fidelity, establishing a new standard for understanding the parallel generation process of diffusion multimodal systems.

---


### 183. [Test-time Scaling over Perception: Resolving the Grounding Paradox in Thinking with Images](https://arxiv.org/abs/2604.11025)

**<font color=#1a73e8>作者：</font>** Zheng Jiang, Yiming Chen, Nan He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have begun to support Thinking with Images by invoking visual tools such as zooming and cropping during inference. Yet these systems remain brittle in fine-grained visual reasoning because they must decide where to look before they have access to the evidence needed to make that decision correctly. We identify this circular dependency as the Grounding Paradox. To address it, we propose Test-Time Scaling over Perception (TTSP), a framework that treats perception itself as a scalable inference process. TTSP generates multiple exploratory perception traces, filters unreliable traces using entropy-based confidence estimation, distills validated observations into structured knowledge, and iteratively refines subsequent exploration toward unresolved uncertainty. Extensive experiments on high-resolution and general multimodal reasoning benchmarks show that TTSP consistently outperforms strong baselines across backbone sizes, while also exhibiting favorable scalability and token efficiency. Our results suggest that scaling perception at test time is a promising direction for robust multimodal reasoning under perceptual uncertainty.

---


### 184. [Introspective Diffusion Language Models](https://arxiv.org/abs/2604.11035)

**<font color=#1a73e8>作者：</font>** Yifan Yu, Yuqing Jian, Junxiong Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models promise parallel generation, yet still lag behind autoregressive (AR) models in quality. We stem this gap to a failure of introspective consistency: AR models agree with their own generations, while DLMs often do not. We define the introspective acceptance rate, which measures whether a model accepts its previously generated tokens. This reveals why AR training has a structural advantage: causal masking and logit shifting implicitly enforce introspective consistency. Motivated by this observation, we introduce Introspective Diffusion Language Model (I-DLM), a paradigm that retains diffusion-style parallel decoding while inheriting the introspective consistency of AR training. I-DLM uses a novel introspective strided decoding (ISD) algorithm, which enables the model to verify previously generated tokens while advancing new ones in the same forward pass. From a systems standpoint, we build I-DLM inference engine on AR-inherited optimizations and further customize it with a stationary-batch scheduler. To the best of our knowledge, I-DLM is the first DLM to match the quality of its same-scale AR counterpart while outperforming prior DLMs in both model quality and practical serving efficiency across 15 benchmarks. It reaches 69.6 on AIME-24 and 45.7 on LiveCodeBench-v6, exceeding LLaDA-2.1-mini (16B) by more than 26 and 15 points, respectively. Beyond quality, I-DLM is designed for the growing demand of large-concurrency serving, delivering about 3x higher throughput than prior state-of-the-art DLMs.

---


### 185. [From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience](https://arxiv.org/abs/2604.11041)

**<font color=#1a73e8>作者：</font>** Jia Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semiconductor supply chains face unprecedented resilience challenges amidst global geopolitical turbulence. Conventional Large Language Model (LLM) planners, when confronting such non-stationary "Policy Black Swan" events, frequently suffer from Decision Paralysis or a severe Grounding Gap due to the absence of physical environmental modeling. This paper introduces ReflectiChain, a cognitive agentic framework tailored for resilient macroeconomic supply chain planning. The core innovation lies in the integration of Latent Trajectory Rehearsal powered by a generative world model, which couples reflection-in-action (System 2 deliberation) with delayed reflection-on-action. Furthermore, we leverage a Retrospective Agentic RL mechanism to enable autonomous policy evolution during the deployment phase (test-time). Evaluations conducted on our high-fidelity benchmark, Semi-Sim, demonstrate that under extreme scenarios such as export bans and material shortages, ReflectiChain achieves a 250% improvement in average step rewards over the strongest LLM baselines. It successfully restores the Operability Ratio (OR) from a deficient 13.3% to over 88.5% while ensuring robust gradient convergence. Ablation studies further underscore that the synergy between physical grounding constraints and double-loop learning is fundamental to bridging the gap between semantic reasoning and physical reality for long-horizon strategic planning.

---


### 186. [Improving Layout Representation Learning Across Inconsistently Annotated Datasets via Agentic Harmonization](https://arxiv.org/abs/2604.11042)

**<font color=#1a73e8>作者：</font>** Renyu Li, Vladimir Kirilenko, Yao You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning object detection (OD) models on combined datasets assumes annotation compatibility, yet datasets often encode conflicting spatial definitions for semantically equivalent categories. We propose an agentic label harmonization workflow that uses a vision-language model to reconcile both category semantics and bounding box granularity across heterogeneous sources before training. We evaluate on document layout detection as a challenging case study, where annotation standards vary widely across corpora. Without harmonization, naïve mixed-dataset fine-tuning degrades a pretrained RT-DETRv2 detector: on SCORE-Bench, which measures how accurately the full document conversion pipeline reproduces ground-truth structure, table TEDS drops from 0.800 to 0.750. Applied to two corpora whose 16 and 10 category taxonomies share only 8 direct correspondences, harmonization yields consistent gains across content fidelity, table structure, and spatial consistency: detection F-score improves from 0.860 to 0.883, table TEDS improves to 0.814, and mean bounding box overlap drops from 0.043 to 0.016. Representation analysis further shows that harmonized training produces more compact and separable post-decoder embeddings, confirming that annotation inconsistency distorts the learned feature space and that resolving it before training restores representation structure.

---


### 187. [EmergentBridge: Improving Zero-Shot Cross-Modal Transfer in Unified Multimodal Embedding Models](https://arxiv.org/abs/2604.11043)

**<font color=#1a73e8>作者：</font>** Jincheng Xie, Xingchen Xiao, Runheng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unified multimodal embedding spaces underpin practical applications such as cross-modal retrieval and zero-shot recognition. In many real deployments, however, supervision is available only for a small subset of modality pairs (e.g., image--text), leaving \emph{unpaired} modality pairs (e.g., audio$\leftrightarrow$depth, infrared$\leftrightarrow$audio) weakly connected and thus performing poorly on zero-shot transfer. Addressing this sparse-pairing regime is therefore essential for scaling unified embedding systems to new tasks without curating exhaustive pairwise data. We propose \textbf{EmergentBridge}, an embedding-level bridging framework that improves performance on these unpaired pairs \emph{without requiring exhaustive pairwise supervision}. Our key observation is that naively aligning a new modality to a synthesized proxy embedding can introduce \emph{gradient interference}, degrading the anchor-alignment structure that existing retrieval/classification relies on. EmergentBridge addresses this by (i) learning a mapping that produces a \emph{noisy bridge anchor} (a proxy embedding of an already-aligned modality) from an anchor embedding, and (ii) enforcing proxy alignment only in the subspace orthogonal to the anchor-alignment direction, preserving anchor alignment while strengthening non-anchor connectivity. Across nine datasets spanning multiple modalities, EmergentBridge consistently outperforms prior binding baselines on zero-shot classification and retrieval, demonstrating strong emergent alignment.

---


### 188. [A Systematic Analysis of the Impact of Persona Steering on LLM Capabilities](https://arxiv.org/abs/2604.11048)

**<font color=#1a73e8>作者：</font>** Jiaqi Chen, Ming Wang, Tingna Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Imbuing Large Language Models (LLMs) with specific personas is prevalent for tailoring interaction styles, yet the impact on underlying cognitive capabilities remains unexplored. We employ the Neuron-based Personality Trait Induction (NPTI) framework to induce Big Five personality traits in LLMs and evaluate performance across six cognitive benchmarks. Our findings reveal that persona induction produces stable, reproducible shifts in cognitive task performance beyond surface-level stylistic changes. These effects exhibit strong task dependence: certain personalities yield consistent gains on instruction-following, while others impair complex reasoning. Effect magnitude varies systematically by trait dimension, with Openness and Extraversion exerting the most robust influence. Furthermore, LLM effects show 73.68% directional consistency with human personality-cognition relationships. Capitalizing on these regularities, we propose Dynamic Persona Routing (DPR), a lightweight query-adaptive strategy that outperforms the best static persona without additional training.

---


### 189. [Shared Emotion Geometry Across Small Language Models: A Cross-Architecture Study of Representation, Behavior, and Methodological Confounds](https://arxiv.org/abs/2604.11050)

**<font color=#1a73e8>作者：</font>** Jihoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We extract 21-emotion vector sets from twelve small language models (six architectures x base/instruct, 1B-8B parameters) under a unified comprehension-mode pipeline at fp16 precision, and compare the resulting geometries via representational similarity analysis on raw cosine RDMs. The five mature architectures (Qwen 2.5 1.5B, SmolLM2 1.7B, Llama 3.2 3B, Mistral 7B v0.3, Llama 3.1 8B) share nearly identical 21-emotion geometry, with pairwise RDM Spearman correlations of 0.74-0.92. This universality persists across diametrically opposed behavioral profiles: Qwen 2.5 and Llama 3.2 occupy opposite poles of MTI Compliance facets yet produce nearly identical emotion RDMs (rho = 0.81), so behavioral facet differences arise above the shared emotion representation. Gemma-3 1B base, the one immature case in our dataset, exhibits extreme residual-stream anisotropy (0.997) and is restructured by RLHF across all geometric descriptors, whereas the five already-mature families show within-family base x instruct RDM correlations of rho >= 0.92 (Mistral 7B v0.3 at rho = 0.985), suggesting RLHF restructures only representations that are not yet organized. Methodologically, we show that what prior work has read as a single comprehension-vs-generation method effect in fact decomposes into four distinct layers -- a coarse method-dependent dissociation, robust sub-parameter sensitivity within generation, a true precision (fp16 vs INT8) effect, and a conflated cross-experiment bias that distorts in opposite directions for different models -- so that a single rho between two prior emotion-vector studies is not a safe basis for interpretation without the layered decomposition.

---


### 190. [ReSpinQuant: Efficient Layer-Wise LLM Quantization via Subspace Residual Rotation Approximation](https://arxiv.org/abs/2604.11080)

**<font color=#1a73e8>作者：</font>** Suyoung Kim, Sunghyun Wee, Hyeonjin Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rotation-based Post-Training Quantization (PTQ) has emerged as a promising solution for mitigating activation outliers in the quantization of Large Language Models (LLMs). Global rotation methods achieve inference efficiency by fusing activation rotations into attention and FFN blocks, but suffer from limited expressivity as they are constrained to use a single learnable rotation matrix across all layers. To tackle this, layer-wise transformation methods emerged, achieving superior accuracy through localized adaptation. However, layer-wise methods cannot fuse activation rotation matrices into weights, requiring online computations and causing significant overhead. In this paper, we propose ReSpinQuant, a quantization framework that resolves such overhead by leveraging offline activation rotation fusion and matching basis using efficient residual subspace rotation. This design reconciles the high expressivity of layer-wise adaptation with only negligible inference overhead. Extensive experiments on W4A4 and W3A3 quantization demonstrate that ReSpinQuant achieves state-of-the-art performance, outperforming global rotation methods and matching the accuracy of computationally expensive layer-wise methods with minimal overhead.

---


### 191. [RESP: Reference-guided Sequential Prompting for Visual Glitch Detection in Video Games](https://arxiv.org/abs/2604.11082)

**<font color=#1a73e8>作者：</font>** Yakun Yu, Ashley Wiens, Adrián Barahona-Ríos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual glitches in video games degrade player experience and perceived quality, yet manual quality assurance cannot scale to the growing test surface of modern game development. Prior automation efforts, particularly those using vision-language models (VLMs), largely operate on single frames or rely on limited video-level baselines that struggle under realistic scene variation, making robust video-level glitch detection challenging. We present RESP, a practical multi-frame framework for gameplay glitch detection with VLMs. Our key idea is reference-guided prompting: for each test frame, we select a reference frame from earlier in the same video, establishing a visual baseline and reframing detection as within-video comparison rather than isolated classification. RESP sequentially prompts the VLM with reference/test pairs and aggregates noisy frame predictions into a stable video-level decision without fine-tuning the VLM. To enable controlled analysis of reference effects, we introduce RefGlitch, a synthetic dataset of manually labeled reference/test frame pairs with balanced coverage across five glitch types. Experiments across five VLMs and three datasets (one synthetic, two real-world) show that reference guidance consistently strengthens frame-level detection and that the improved frame-level evidence reliably transfers to stronger video-level triage under realistic QA conditions. Code and data are available at: \href{this https URL}{this https URL}.

---


### 192. [CausalGaze: Unveiling Hallucinations via Counterfactual Graph Intervention in Large Language Models](https://arxiv.org/abs/2604.11087)

**<font color=#1a73e8>作者：</font>** Linggang Kong, Lei Wu, Yunlong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the groundbreaking advancements made by large language models (LLMs), hallucination remains a critical bottleneck for their deployment in high-stakes domains. Existing classification-based methods mainly rely on static and passive signals from internal states, which often captures the noise and spurious correlations, while overlooking the underlying causal mechanisms. To address this limitation, we shift the paradigm from passive observation to active intervention by introducing CausalGaze, a novel hallucination detection framework based on structural causal models (SCMs). CausalGaze models LLMs' internal states as dynamic causal graphs and employs counterfactual interventions to disentangle causal reasoning paths from incidental noise, thereby enhancing model interpretability. Extensive experiments across four datasets and three widely used LLMs demonstrate the effectiveness of CausalGaze, especially achieving over 5.2\% improvement in AUROC on the TruthfulQA dataset compared to state-of-the-art baselines.

---


### 193. [Bottleneck Tokens for Unified Multimodal Retrieval](https://arxiv.org/abs/2604.11095)

**<font color=#1a73e8>作者：</font>** Siyu Sun, Jing Ren, Zhaohe Liao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting decoder-only multimodal large language models (MLLMs) for unified multimodal retrieval faces two structural gaps. First, existing methods rely on implicit pooling, which overloads the hidden state of a standard vocabulary token (e.g., <EOS>) as the sequence-level representation, a mechanism never designed for information aggregation. Second, contrastive fine-tuning specifies what the embedding should match but provides no token-level guidance on how information should be compressed into it. We address both gaps with two complementary components. Architecturally, we introduce Bottleneck Tokens (BToks), a small set of learnable tokens that serve as a fixed-capacity explicit pooling mechanism. For training, we propose Generative Information Condensation: a next-token prediction objective coupled with a Condensation Mask that severs the direct attention path from target tokens to query tokens. All predictive signals are thereby forced through the BToks, converting the generative loss into dense, token-level supervision for semantic compression. At inference time, only the input and BToks are processed in a single forward pass with negligible overhead over conventional last-token pooling. On MMEB-V2 (78 datasets, 3 modalities, 9 meta-tasks), our approach achieves state-of-the-art among 2B-scale methods under comparable data conditions, attaining an Overall score of 59.0 (+3.6 over VLM2Vec-V2) with substantial gains on semantically demanding tasks (e.g., +12.6 on Video-QA).

---


### 194. [Efficient Training for Cross-lingual Speech Language Models](https://arxiv.org/abs/2604.11096)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Qingkai Fang, Yun Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Currently, large language models (LLMs) predominantly focus on the text modality. To enable more natural human-AI interaction, speech LLMs are emerging, but building effective end-to-end speech LLMs remains challenging due to limited data and the difficulty in expanding to more languages. In this paper, we introduce Cross-lingual Speech Language Model (CSLM), an efficient training method for cross-lingual speech LLMs based on discrete speech tokens. We propose a novel alignment strategy that achieves cross-modal and cross-lingual alignment through continual pre-training. By conducting instruction fine-tuning following a speech-text interleaved chain-of-modality generation process, we enhance modal alignment at a finer granularity, thereby improving generation quality and reducing latency. CSLM aligns different modalities and languages simultaneously without the need for massive speech data, thus exhibiting good language scalability. Evaluations on cross-modal tasks, mono-lingual conversational tasks, and cross-lingual conversational tasks demonstrate CSLM's strong cross-modal alignment capabilities and general task abilities. (Code is available at: this https URL)

---


### 195. [OmniScript: Towards Audio-Visual Script Generation for Long-Form Cinematic Video](https://arxiv.org/abs/2604.11102)

**<font color=#1a73e8>作者：</font>** Junfu Pu, Yuxin Chen, Teng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current multimodal large language models (MLLMs) have demonstrated remarkable capabilities in short-form video understanding, yet translating long-form cinematic videos into detailed, temporally grounded scripts remains a significant challenge. This paper introduces the novel video-to-script (V2S) task, aiming to generate hierarchical, scene-by-scene scripts encompassing character actions, dialogues, expressions, and audio cues. To facilitate this, we construct a first-of-its-kind human-annotated benchmark and propose a temporally-aware hierarchical evaluation framework. Furthermore, we present OmniScript, an 8B-parameter omni-modal (audio-visual) language model tailored for long-form narrative comprehension. OmniScript is trained via a progressive pipeline that leverages chain-of-thought supervised fine-tuning for plot and character reasoning, followed by reinforcement learning using temporally segmented rewards. Extensive experiments demonstrate that despite its parameter efficiency, OmniScript significantly outperforms larger open-source models and achieves performance comparable to state-of-the-art proprietary models, including Gemini 3-Pro, in both temporal localization and multi-field semantic accuracy.

---


### 196. [Frugal Knowledge Graph Construction with Local LLMs: A Zero-Shot Pipeline, Self-Consistency and Wisdom of Artificial Crowds](https://arxiv.org/abs/2604.11104)

**<font color=#1a73e8>作者：</font>** Pierre Jourlin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an empirical study of a multi-model zero-shot pipeline for knowledge graph construction and exploitation, executed entirely through local inference on consumer-grade hardware. We propose a reproducible evaluation framework integrating two external benchmarks (DocRED, HotpotQA), WebQuestionsSP-style synthetic data, and the RAGAS evaluation framework in an automated pipeline. On 500 document-level relations, our system achieves an F1 of 0.70 $\pm$ 0.041 in zero-shot, compared to 0.80 for supervised DREEAM. Text-to-query achieves an accuracy of 0.80 $\pm$ 0.06 on 200 samples. Multi-hop reasoning achieves an Exact Match (EM) of 0.46$\pm$0.04 on 500 HotpotQA questions, with a RAGAS faithfulness of 0.96 $\pm$ 0.04 on 50 samples. Beyond the pipeline, we study diversity mechanisms for difficult multi-hop reasoning. On 181 questions unsolvable at zero temperature, self-consistency (k=5, T =0.7) recovers up to 23% EM with a single Mixture-of-Experts (MoE) model, but the cross-model oracle (3 architectures x 5 samples) reaches 46.4%. We highlight an agreement paradox: strong consensus among samples signals collective hallucination rather than a reliable answer, echoing the work of Moussa{ï}d et al. on the wisdom of crowds. Extending to the full pipeline (500 questions), self-consistency (k=3) raises EM from 0.46 to 0.48 $\pm$ 0.04. A confidence-routing cascade mechanism (Phi-4 $\rightarrow$ GPT-OSS, k=5) achieves an EM of 0.55 $\pm$ 0.04, the best result obtained, with 45.4% of questions rerouted. Finally, we show that V3 prompt engineering applied to other models does not reproduce the gains observed with Gemma-4, confirming the specific prompt/model interaction. The entire system runs in $\sim$5 h on a single RTX 3090, without any training, for an estimated carbon footprint of 0.09 kg CO2 eq.

---


### 197. [Persona Non Grata: Single-Method Safety Evaluation Is Incomplete for Persona-Imbued LLMs](https://arxiv.org/abs/2604.11120)

**<font color=#1a73e8>作者：</font>** Wenkai Li, Fan Yang, Shaunak A. Mehta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personality imbuing customizes LLM behavior, but safety evaluations almost always study prompt-based personas alone. We show this is incomplete: prompting and activation steering expose *different*, architecture-dependent vulnerability profiles, and testing with only one method can miss a model's dominant failure mode. Across 5,568 judged conditions on four standard models from three architecture families, persona danger rankings under system prompting are preserved across all architectures ($\rho = 0.71$--$0.96$), but activation-steering vulnerability diverges sharply and cannot be predicted from prompt-side rankings: Llama-3.1-8B is substantially more AS-vulnerable, whereas Gemma-3-27B and Qwen3.5 are more vulnerable to prompting. The most striking illustration of this divergence is the *prosocial persona paradox*: on Llama-3.1-8B, P12 (high conscientiousness + high agreeableness) is among the safest personas under prompting yet becomes the highest-ASR activation-steered persona (ASR ~0.818). This is an inversion robust to coefficient ablation and matched-strength calibration, and replicated on DeepSeek-R1-Distill-Qwen-32B. A trait refusal alignment framework, in which conscientiousness is strongly anti-aligned with refusal on Llama-3.1-8B, offers a partial geometric account. Reasoning provides only partial protection: two 32B reasoning models reach 15--18% prompt-side ASR, and activation steering separates them sharply in both baseline susceptibility and persona-specific vulnerability. Heuristic trace diagnostics suggest that the safer model retains stronger policy recall and self-correction behavior, not merely longer reasoning.

---


### 198. [BITS Pilani at SemEval-2026 Task 9: Structured Supervised Fine-Tuning with DPO Refinement for Polarization Detection](https://arxiv.org/abs/2604.11121)

**<font color=#1a73e8>作者：</font>** Atharva Gupta, Dhruv Kumar, Yash Sinha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The POLAR SemEval-2026 Shared Task aims to detect online polarization and focuses on the classification and identification of multilingual, multicultural, and multi-event polarization.
Accurate computational detection of online polarization is challenging due to nuanced rhetoric, implicit framing, and the high cost of human-in-the-loop annotation. Building on recent findings that contextual prompting enables large language models to function as strong polarization detectors, we present a two-stage approach for detecting political polarization in social media text that combines structured supervised fine-tuning with Direct Preference Optimization (DPO) refinement.
We fine-tune Qwen 2.5-7B-Instruct with LoRA using an interpretable slot-filling template (target, claim type, manifestation checklist, and justification). We then apply DPO with automatically generated preference pairs to reduce costly false negatives. Experiments on the SemEval 2026 POLAR shared task dataset show that preference-based refinement improves both accuracy and decreases false negatives without extra annotation. On the English development set, DPO increases recall from 0.5085 to 0.7797 and improves macro-F1 by ~5 points.

---


### 199. [Semantic-Geometric Dual Compression: Training-Free Visual Token Reduction for Ultra-High-Resolution Remote Sensing Understanding](https://arxiv.org/abs/2604.11122)

**<font color=#1a73e8>作者：</font>** Yueying Li, Fengxiang Wang, Yan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated immense potential in Earth observation. However, the massive visual tokens generated when processing Ultra-High-Resolution (UHR) imagery introduce prohibitive computational overhead, severely bottlenecking their inference efficiency. Existing visual token compression methods predominantly adopt static and uniform compression strategies, neglecting the inherent "Semantic-Geometric Duality" in remote sensing interpretation tasks. Specifically, object semantic tasks focus on the abstract semantics of objects and benefit from aggressive background pruning, whereas scene geometric tasks critically rely on the integrity of spatial topology. To address this challenge, we propose DualComp, a task-adaptive dual-stream token compression framework. Dynamically guided by a lightweight pre-trained router, DualComp decouples feature processing into two dedicated pathways. In the object semantic stream, the Spatially-Contiguous Semantic Aggregator (SCSA) utilizes size-adaptive clustering to aggregates redundant background while protecting small object. In the scene geometric stream, the Instruction-Guided Structure Recoverer (IGSR) introduces a greedy path-tracing topology completion mechanism to reconstruct spatial skeletons. Experiments on the UHR remote sensing benchmark XLRS-Bench demonstrate that DualComp accomplishes high-fidelity remote sensing interpretation at an exceptionally low computational cost, achieving simultaneous improvements in both efficiency and accuracy.

---


### 200. [A Proposed Biomedical Data Policy Framework to Reduce Fragmentation, Improve Quality, and Incentivize Sharing in Indian Healthcare in the era of Artificial Intelligence and Digital Health](https://arxiv.org/abs/2604.11125)

**<font color=#1a73e8>作者：</font>** Nikhil Mehta, Sachin Gupta, Gouri RP Anand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> India generates vast biomedical data through postgraduate research, government hospital services and audits, government schemes, private hospitals and their electronic medical record (EMR) systems, insurance programs and standalone clinics. Unfortunately, these resources remain fragmented across institutional silos and vendor-locked EMR systems. The fundamental bottleneck is not technological but economic and academic. There is a systemic misalignment of incentives that renders data sharing a high-risk, low-reward activity for individual researchers and institutions. Until India's academic promotion criteria, institutional rankings, and funding mechanisms explicitly recognize and reward data curation as professional work, the nation's AI ambitions will remain constrained by fragmented, non-interoperable datasets. We propose a multi-layered incentive architecture integrating recognition of data papers in National Medical Commission (NMC) promotion criteria, incorporation of open data metrics into the National Institutional Ranking Framework (NIRF), adoption of Shapley Value-based revenue sharing in federated learning consortia, and establishment of institutional data stewardship as a mainstream professional role. Critical barriers to data sharing, including fear of data quality scrutiny, concerns about misinterpretation, and selective reporting bias, are addressed through mandatory data quality assessment, structured peer review, and academic credit for auditing roles. The proposed framework directly addresses regulatory constraints introduced by the Digital Personal Data Protection Act 2023 (DPDPA), while constructively engaging with the National Data Sharing and Accessibility Policy (NDSAP), Biotech-PRIDE Guidelines, and the Anusandhan National Research Foundation (ANRF) guidelines.

---


### 201. [DeCoVec: Building Decoding Space based Task Vector for Large Language Models via In-Context Learning](https://arxiv.org/abs/2604.11129)

**<font color=#1a73e8>作者：</font>** Feiyang Li, Yile Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task vectors, representing directions in model or activation spaces that encode task-specific behaviors, have emerged as a promising tool for steering large language models (LLMs). However, existing approaches typically require fine-tuning or invasive manipulation of internal states, limiting their flexibility and scalability. We propose \textsc{DeCoVec} (Decoding Space based Task Vector), a training-free and non-invasive framework that constructs task vectors directly in the \textit{decoding space} by leveraging in-context learning (ICL). Specifically, \textsc{DeCoVec} captures the task essence as the difference between the output logit distributions of few-shot and zero-shot prompts, then steers generation by injecting this vector into the decoding process. Experiments across seven LLMs (0.5B--9B) on TruthfulQA, Math-500, and AQUA-RAT show that \textsc{DeCoVec} consistently outperforms standard few-shot baselines, with gains up to +5.50 average accuracy. Further analysis demonstrates that \textsc{DeCoVec} effectively suppresses generation degeneration and logical flaws while exhibiting strong robustness to demonstration ordering, all without incurring additional input token costs. Our method offers a training-free and non-invasive solution for LLM steering without requiring weight updates or auxiliary models.

---


### 202. [How Robust Are Large Language Models for Clinical Numeracy? An Empirical Study on Numerical Reasoning Abilities in Clinical Contexts](https://arxiv.org/abs/2604.11133)

**<font color=#1a73e8>作者：</font>** Minh-Vuong Nguyen, Fatemeh Shiri, Zhuang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being explored for clinical question answering and decision support, yet safe deployment critically requires reliable handling of patient measurements in heterogeneous clinical notes. Existing evaluations of LLMs for clinical numerical reasoning provide limited operation-level coverage, restricted primarily to arithmetic computation, and rarely assess the robustness of numerical understanding across clinical note formats. We introduce ClinicNumRobBench, a benchmark of 1,624 context-question instances with ground-truth answers that evaluates four main types of clinical numeracy: value retrieval, arithmetic computation, relational comparison, and aggregation. To stress-test robustness, ClinicNumRobBench presents longitudinal MIMIC-IV vital-sign records in three semantically equivalent representations, including a real-world note-style variant derived from the Open Patients dataset, and instantiates queries using 42 question templates. Experiments on 14 LLMs show that value retrieval is generally strong, with most models exceeding 85% accuracy, while relational comparison and aggregation remain challenging, with some models scoring below 15%. Fine-tuning on medical data can reduce numeracy relative to base models by over 30%, and performance drops under note-style variation indicate LLM sensitivity to format. ClinicNumRobBench offers a rigorous testbed for clinically reliable numerical reasoning. Code and data URL are available on this https URL.

---


### 203. [BoxTuning: Directly Injecting the Object Box for Multimodal Model Fine-Tuning](https://arxiv.org/abs/2604.11136)

**<font color=#1a73e8>作者：</font>** Zekun Qian, Ruize Han, Wei Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-level spatial-temporal understanding is essential for video question answering, yet existing multimodal large language models (MLLMs) encode frames holistically and lack explicit mechanisms for fine-grained object grounding. Recent work addresses this by serializing bounding box coordinates as text tokens, but this text-coordinate paradigm suffers from a fundamental modality mismatch: object information is inherently visual, yet encoding it as text incurs a high token cost that forces aggressive temporal downsampling. We propose BoxTuning, which resolves this mismatch by injecting object spatial-temporal information directly into the visual modality. Colored bounding boxes and trajectory trails are rendered onto video frames as visual prompts, with only a concise color-to-object legend retained as text. This reduces the token cost significantly, achieving 87-93% text token reduction in practice. It also preserves full temporal resolution, where the trajectory trails further encode inter-frame motion direction and speed within each keyframe, recovering fine-grained dynamics that text-coordinate methods are forced to discard. Experimental results on five video QA benchmarks (CLEVRER, Perception Test, STAR, NExT-QA, IntentQA) show that BoxTuning surpasses text-coordinate baselines on spatially oriented tasks and nearly eliminates the accuracy degradation observed on reasoning-centric tasks, establishing visual prompting as a more natural and efficient paradigm for conveying object information to video MLLMs.

---


### 204. [Sparse Hypergraph-Enhanced Frame-Event Object Detection with Fine-Grained MoE](https://arxiv.org/abs/2604.11140)

**<font color=#1a73e8>作者：</font>** Wei Bao, Yuehan Wang, Tianhang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrating frame-based RGB cameras with event streams offers a promising solution for robust object detection under challenging dynamic conditions. However, the inherent heterogeneity and data redundancy of these modalities often lead to prohibitive computational overhead or suboptimal feature fusion. In this paper, we propose Hyper-FEOD, a high-performance and efficient detection framework, which synergistically optimizes multi-modal interaction through two core components. First, we introduce Sparse Hypergraph-enhanced Cross-Modal Fusion (S-HCF), which leverages the inherent sparsity of event streams to construct an event-guided activity map. By performing high-order hypergraph modeling exclusively on selected motion-critical sparse tokens, S-HCF captures complex non-local dependencies between RGB and event data while overcoming the traditional complexity bottlenecks of hypergraph computation. Second, we design a Fine-Grained Mixture of Experts (FG-MoE) Enhancement module to address the diverse semantic requirements of different image regions. This module employs specialized hypergraph experts tailored for object boundaries, internal textures, and backgrounds, utilizing a pixel-level spatial gating mechanism to adaptively route and enhance features. Combined with a load-balancing loss and zero-initialization strategy, FG-MoE ensures stable training and precise feature refinement without disrupting the pre-trained backbone's distribution. Experimental results on mainstream RGB-Event benchmarks demonstrate that Hyper-FEOD achieves a superior accuracy-efficiency trade-off, outperforming state-of-the-art methods while maintaining a lightweight footprint suitable for real-time edge deployment.

---


### 205. [Hierarchical Textual Knowledge for Enhanced Image Clustering](https://arxiv.org/abs/2604.11144)

**<font color=#1a73e8>作者：</font>** Yijie Zhong, Yunfan Gao, Weipeng Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image clustering aims to group images in an unsupervised fashion. Traditional methods focus on knowledge from visual space, making it difficult to distinguish between visually similar but semantically different classes. Recent advances in vision-language models enable the use of textual knowledge to enhance image clustering. However, most existing methods rely on coarse class labels or simple nouns, overlooking the rich conceptual and attribute-level semantics embedded in textual space. In this paper, we propose a knowledge-enhanced clustering (KEC) method that constructs a hierarchical concept-attribute structured knowledge with the help of large language models (LLMs) to guide clustering. Specifically, we first condense redundant textual labels into abstract concepts and then automatically extract discriminative attributes for each single concept and similar concept pairs, via structured prompts to LLMs. This knowledge is instantiated for each input image to achieve the knowledge-enhanced features. The knowledge-enhanced features with original visual features are adapted to various downstream clustering algorithms. We evaluate KEC on 20 diverse datasets, showing consistent improvements across existing methods using additional textual knowledge. KEC without training outperforms zero-shot CLIP on 14 out of 20 datasets. Furthermore, the naive use of textual knowledge may harm clustering performance, while KEC provides both accuracy and robustness.

---


### 206. [Environmental Footprint of GenAI Research: Insights from the Moshi Foundation Model](https://arxiv.org/abs/2604.11154)

**<font color=#1a73e8>作者：</font>** Marta López-Rauhut, Loic Landrieu, Mathieu Aubry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> New multi-modal large language models (MLLMs) are continuously being trained and deployed, following rapid development cycles. This generative AI frenzy is driving steady increases in energy consumption, greenhouse gas emissions, and a plethora of other environmental impacts linked to datacenter construction and hardware manufacturing. Mitigating the environmental consequences of GenAI remains challenging due to an overall lack of transparency by the main actors in the field. Even when the environmental impacts of specific models are mentioned, they are typically restricted to the carbon footprint of the final training run, omitting the research and development stages.
In this work, we explore the impact of GenAI research through a fine-grained analysis of the compute spent to create Moshi, a 7B-parameter speech-text foundation model for real-time dialogue developed by Kyutai, a leading privately funded open science AI lab. For the first time, our study dives into the anatomy of compute-intensive MLLM research, quantifying the GPU-time invested in specific model components and training phases, as well as early experimental stages, failed training runs, debugging, and ablation studies. Additionally, we assess the environmental impacts of creating Moshi from beginning to end using a life cycle assessment methodology: we quantify energy and water consumption, greenhouse gas emissions, and mineral resource depletion associated with the production and use of datacenter hardware.
Our detailed analysis allows us to provide actionable guidelines to reduce compute usage and environmental impacts of MLLM research, paving the way for more sustainable AI research.

---


### 207. [rPPG-VQA: A Video Quality Assessment Framework for Unsupervised rPPG Training](https://arxiv.org/abs/2604.11156)

**<font color=#1a73e8>作者：</font>** Tianyang Dai, Ming Chang, Yan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised remote photoplethysmography (rPPG) promises to leverage unlabeled video data, but its potential is hindered by a critical challenge: training on low-quality "in-the-wild" videos severely degrades model performance. An essential step missing here is to assess the suitability of the videos for rPPG model learning before using them for the task. Existing video quality assessment (VQA) methods are mainly designed for human perception and not directly applicable to the above purpose. In this work, we propose rPPG-VQA, a novel framework for assessing video suitability for rPPG. We integrate signal-level and scene-level analyses and design a dual-branch assessment architecture. The signal-level branch evaluates the physiological signal quality of the videos via robust signal-to-noise ratio (SNR) estimation with a multi-method consensus mechanism, and the scene-level branch uses a multimodal large language model (MLLM) to identify interferences like motion and unstable lighting. Furthermore, we propose a two-stage adaptive sampling (TAS) strategy that utilizes the quality score to curate optimal training datasets. Experiments show that by training on large-scale, "in-the-wild" videos filtered by our framework, we can develop unsupervised rPPG models that achieve a substantial improvement in accuracy on standard benchmarks. Our code is available at this https URL.

---


### 208. [A Simulation-Based Method for Testing Collaborative Learning Scaffolds Using LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2604.11161)

**<font color=#1a73e8>作者：</font>** Han Wua, Lishan Zhang, Chunming Lu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Traditional research on collaborative learning scaffolding is often time-consuming and resource-heavy, which hinders the rapid iteration and optimization of instructional strategies. LLM-based multi-agent systems have recently emerged as a powerful tool to simulate complex social interactions and provide a novel paradigm for educational research. Objectives: This study proposes an LLM-based multi-agent simulation approach to investigate collaborative learning processes and the effectiveness of instructional scaffolds prior to actual classroom deployment. The research specifically examines the feasibility of simulating group discussions and the alignment of these simulations with established learning science theories. Methods: The simulation system was implemented using the MetaGPT framework and GPT-4o, comprising one teacher agent and five distinct student roles (Leader, Supporter, Expounder, Rebutter, and Summarizer). Two scaffolding strategies, "Deep Think before Speak" and "Direct Speak", were compared across ten classical Chinese poetry appreciation tasks. Evaluation was conducted through discourse analysis of quality and behavior. Results and Conclusions: The introduction of the "Deep Think before Speak" scaffold significantly improved the agents' discourse diversity and interaction depth while notably reducing content repetitiveness. Behavioral analysis showed that the scaffold encouraged more complex interaction patterns, such as reflecting, rebutting, and explaining. These findings align with the ICAP framework, as the scaffold prompted agents to move from simple "Active" participation to "Constructive" and "Interactive" knowledge co-construction. This study demonstrates the feasibility and ecological validity of using LLM-based multi-agent systems to simulate authentic collaborative learning dynamics.

---


### 209. [Do Thought Streams Matter? Evaluating Reasoning in Gemini Vision-Language Models for Video Scene Understanding](https://arxiv.org/abs/2604.11177)

**<font color=#1a73e8>作者：</font>** Shivam Sharma, Sankalp Nagaonkar, Ashish Choithani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We benchmark how internal reasoning traces, which we call thought streams, affect video scene understanding in vision-language models. Using four configurations of Google's Gemini 2.5 Flash and Flash Lite across scenes extracted from 100 hours of video, we ask three questions: does more thinking lead to better outputs, where do the gains stop, and what do these models actually think about? We introduce three evaluation metrics. Contentfulness measures how much of the thought stream is useful scene content versus meta-commentary. Thought-Final Coverage measures how faithfully the thought stream translates into the final output. Dominant Entity Analysis identifies which subjects, actions, and settings the model focuses on. GPT-5 serves as an independent judge. We find that quality gains from additional thinking plateau quickly, with most improvement occurring in the first few hundred tokens. Flash Lite offers the best balance between quality and token usage. Tight reasoning budgets cause the model to add content in the final output that it never reasoned about, a form of compression-step hallucination. Despite being different model tiers, Flash and Flash Lite produce similar thought streams, though they differ in style: Flash discusses its reasoning process, while Lite focuses on describing the scene.

---


### 210. [MedP-CLIP: Medical CLIP with Region-Aware Prompt Integration](https://arxiv.org/abs/2604.11197)

**<font color=#1a73e8>作者：</font>** Jiahui Peng, He Yao, Jingwen Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pre-training (CLIP) has demonstrated outstanding performance in global image understanding and zero-shot transfer through large-scale text-image alignment. However, the core of medical image analysis often lies in the fine-grained understanding of specific anatomical structures or lesion regions. Therefore, precisely comprehending region-of-interest (RoI) information provided by medical professionals or perception models becomes crucial. To address this need, we propose MedP-CLIP, a region-aware medical vision-language model (VLM). MedP-CLIP innovatively integrates medical prior knowledge and designs a feature-level region prompt integration mechanism, enabling it to flexibly respond to various prompt forms (e.g., points, bounding boxes, masks) while maintaining global contextual awareness when focusing on local regions. We pre-train the model on a meticulously constructed large-scale dataset (containing over 6.4 million medical images and 97.3 million region-level annotations), equipping it with cross-disease and cross-modality fine-grained spatial semantic understanding capabilities. Experiments demonstrate that MedP-CLIP significantly outperforms baseline methods in various medical tasks, including zero-shot recognition, interactive segmentation, and empowering multimodal large language models. This model provides a scalable, plug-and-play visual backbone for medical AI, combining holistic image understanding with precise regional analysis.

---


### 211. [Exploring Knowledge Conflicts for Faithful LLM Reasoning: Benchmark and Method](https://arxiv.org/abs/2604.11209)

**<font color=#1a73e8>作者：</font>** Tianzhe Zhao, Jiaoyan Chen, Shuxiu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable success across a wide range of applications especially when augmented by external knowledge through retrieval-augmented generation (RAG). Despite their widespread adoption, recent studies have shown that LLMs often struggle to perform faithful reasoning when conflicting knowledge is retrieved. However, existing work primarily focuses on conflicts between external knowledge and the parametric knowledge of LLMs, leaving conflicts across external knowledge largely unexplored. Meanwhile, modern RAG systems increasingly emphasize the integration of unstructured text and (semi-)structured data like knowledge graphs (KGs) to improve knowledge completeness and reasoning faithfulness. To address this gap, we introduce ConflictQA, a novel benchmark that systematically instantiates conflicts between textual evidence and KG evidence. Extensive evaluations across representative LLMs reveal that, facing such cross-source conflicts, LLMs often fail to identify reliable evidence for correct reasoning. Instead, LLMs become more sensitive to prompting choices and tend to rely exclusively on either KG or textual evidence, resulting in incorrect responses. Based on these findings, we further propose XoT, a two-stage explanation-based thinking framework tailored for reasoning over heterogeneous conflicting evidence, and verify its effectiveness with extensive experiments.

---


### 212. [Sign Language Recognition in the Age of LLMs](https://arxiv.org/abs/2604.11225)

**<font color=#1a73e8>作者：</font>** Vaclav Javorek, Jakub Honzik, Ivan Gruber 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Vision Language Models (VLMs) have demonstrated strong performance across a wide range of multimodal reasoning tasks. This raises the question of whether such general-purpose models can also address specialized visual recognition problems such as isolated sign language recognition (ISLR) without task-specific training. In this work, we investigate the capability of modern VLMs to perform ISLR in a zero-shot setting. We evaluate several open-source and proprietary VLMs on the WLASL300 benchmark. Our experiments show that, under prompt-only zero-shot inference, current open-source VLMs remain far behind classic supervised ISLR classifiers by a wide margin. However, follow-up experiments reveal that these models capture partial visual-semantic alignment between signs and text descriptions. Larger proprietary models achieve substantially higher accuracy, highlighting the importance of model scale and training data diversity. All our code is publicly available on GitHub.

---


### 213. [Decoupled Similarity for Task-Aware Token Pruning in Large Vision-Language Models](https://arxiv.org/abs/2604.11240)

**<font color=#1a73e8>作者：</font>** Kexin Ma, Jing Xiao, Chaofeng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token pruning has emerged as an effective approach to reduce the substantial computational overhead of Large Vision-Language Models (LVLMs) by discarding less informative visual tokens while preserving performance. However, existing methods typically rely on individual attention sources from different LVLM components, resulting in incomplete and suboptimal pruning decisions due to biased attention distributions. To address this problem, we propose DeSAP, a novel Decoupled Similarity-Aware Pruning method for precise, task-aware token pruning within the visual encoder. Specifically, DeSAP introduces a decoupled similarity to capture fine-grained cross-modal relevance between visual features and text tokens, providing explicit task-related guidance for pruning. By integrating decoupled similarity with visual saliency signals derived from visual attention, DeSAP performs token pruning under the guidance of both task-related and visual cues, enabling robust pruning even under aggressive pruning ratios. Extensive experiments across diverse benchmarks and architectures show that DeSAP consistently outperforms SOTA methods in both accuracy and efficiency. On LLaVA-1.5-7B, DeSAP achieves a 10 times FLOPs reduction and a 2.3 times prefill speedup by retaining only 11.1% of visual tokens, while maintaining 98.1% of the original performance.

---


### 214. [Script-a-Video: Deep Structured Audio-visual Captions via Factorized Streams and Relational Grounding](https://arxiv.org/abs/2604.11244)

**<font color=#1a73e8>作者：</font>** Tencent Hunyuan Team  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in Multimodal Large Language Models (MLLMs) are transforming video captioning from a descriptive endpoint into a semantic interface for both video understanding and generation. However, the dominant paradigm still casts videos as monolithic narrative paragraphs that entangle visual, auditory, and identity information. This dense coupling not only compromises representational fidelity but also limits scalability, since even local edits can trigger global rewrites. To address this structural bottleneck, we propose Multi-Stream Scene Script (MTSS), a novel paradigm that replaces monolithic text with factorized and explicitly grounded scene descriptions. MTSS is built on two core principles: Stream Factorization, which decouples a video into complementary streams (Reference, Shot, Event, and Global), and Relational Grounding, which reconnects these isolated streams through explicit identity and temporal links to maintain holistic video consistency. Extensive experiments demonstrate that MTSS consistently enhances video understanding across various models, achieving an average reduction of 25% in the total error rate on Video-SALMONN-2 and an average performance gain of 67% on the Daily-Omni reasoning benchmark. It also narrows the performance gap between smaller and larger MLLMs, indicating a substantially more learnable caption interface. Finally, even without architectural adaptation, replacing monolithic prompts with MTSS in multi-shot video generation yields substantial human-rated improvements: a 45% boost in cross-shot identity consistency, a 56% boost in audio-visual alignment, and a 71% boost in temporal controllability.

---


### 215. [Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate](https://arxiv.org/abs/2604.11258)

**<font color=#1a73e8>作者：</font>** Zhixiang Lu, Jionglong Su  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) in healthcare suffer from severe confirmation bias, often hallucinating visual details to support initial, potentially erroneous diagnostic hypotheses. Existing Chain-of-Thought (CoT) approaches lack intrinsic correction mechanisms, rendering them vulnerable to error propagation. To bridge this gap, we propose Dialectic-Med, a multi-agent framework that enforces diagnostic rigor through adversarial dialectics. Unlike static consensus models, Dialectic-Med orchestrates a dynamic interplay between three role-specialized agents: a proponent that formulates diagnostic hypotheses; an opponent equipped with a novel visual falsification module that actively retrieves contradictory visual evidence to challenge the Proponent; and a mediator that resolves conflicts via a weighted consensus graph. By explicitly modeling the cognitive process of falsification, our framework guarantees that diagnostic reasoning is tightly grounded in verified visual regions. Empirical evaluations on MIMIC-CXR-VQA, VQA-RAD, and PathVQA demonstrate that Dialectic-Med not only achieves state-of-the-art performance but also fundamentally enhances the trustworthiness of the reasoning process. Beyond accuracy, our approach significantly enhances explanation faithfulness and decisively mitigates hallucinations, establishing a new standard over single-agent baselines.

---


### 216. [Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization](https://arxiv.org/abs/2604.11259)

**<font color=#1a73e8>作者：</font>** Zhixin Lin, Jungang Li, Dongliang Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents powered by Multimodal Large Language Models (MLLMs) can execute complex tasks on mobile devices. Despite this progress, most existing systems still optimize task success or efficiency, neglecting users' privacy personalization. In this paper, we study the often-overlooked problem of agent personalization. We observe that personalization can induce systematic structural heterogeneity in execution trajectories. For example, privacy-first users often prefer protective actions, e.g., refusing permissions, logging out, and minimizing exposure, leading to logically different execution trajectories from utility-first users. Such variable-length and structurally different trajectories make standard preference optimization unstable and less informative. To address this issue, we propose Trajectory Induced Preference Optimization (TIPO), which uses preference-intensity weighting to emphasize key privacy-related steps and padding gating to suppress alignment noise. Results on our Privacy Preference Dataset show that TIPO improves persona alignment and distinction while preserving strong task executability, achieving 65.60% SR, 46.22 Compliance, and 66.67% PD, outperforming existing optimization methods across various GUI tasks. The code and dataset will be publicly released at this https URL.

---


### 217. [Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283)

**<font color=#1a73e8>作者：</font>** Bingzheng QU, Kehai Chen, Xuefeng Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent developments in video translation have further enhanced cross-lingual access to video content, with multimodal large language models (MLLMs) playing an increasingly important supporting role. With strong multimodal understanding, reasoning, and generation capabilities, MLLMs-based video translation systems are overcoming the limitations of traditional cascaded pipelines that separately handle automatic speech recognition, machine translation, text-to-speech and lip synchronization. These MLLM-powered approaches not only achieve competitive or superior translation quality, but also demonstrate stronger robustness in zero-shot settings and multi-speaker scenarios, while jointly modeling semantic fidelity, timing, speaker identity, and emotional consistency. However, despite the rapid progress of MLLMs and extensive surveys on general video-language understanding, a focused and systematic review of how MLLMs empower video translation tasks is still lacking. To fill this gap, we provide the first comprehensive overview of MLLMs-based video translation, organized around a three-role taxonomy: 1) Semantic Reasoner, which characterizes how MLLMs perform video understanding, temporal reasoning, and multimodal fusion; 2) Expressive Performer, which analyzes LLM-driven and LLM-augmented techniques for expressive, controllable speech generation; and 3) Visual Synthesizer, which examines different types of video generators for high-fidelity lip-sync and visual alignment. Finally, we discuss open challenges in video understanding, temporal modeling, and multimodal alignment, and outline promising future research directions for MLLMs-powered video translation.

---


### 218. [Consistency of AI-Generated Exercise Prescriptions: A Repeated Generation Study Using a Large Language Model](https://arxiv.org/abs/2604.11287)

**<font color=#1a73e8>作者：</font>** Kihyuk Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Large language models (LLMs) have been explored as tools for generating personalized exercise prescriptions, yet the consistency of outputs under identical conditions remains insufficiently examined. Objective: This study evaluated the intra-model consistency of LLM-generated exercise prescriptions using a repeated generation design. Methods: Six clinical scenarios were used to generate exercise prescriptions using Gemini 2.5 Flash (20 outputs per scenario; total n = 120). Consistency was assessed across three dimensions: (1) semantic consistency using SBERT-based cosine similarity, (2) structural consistency based on the FITT principle using an AI-as-a-judge approach, and (3) safety expression consistency, including inclusion rates and sentence-level quantification. Results: Semantic similarity was high across scenarios (mean cosine similarity: 0.879-0.939), with greater consistency in clinically constrained cases. Frequency showed consistent patterns, whereas variability was observed in quantitative components, particularly exercise intensity. Unclassifiable intensity expressions were observed in 10-25% of resistance training outputs. Safety-related expressions were included in 100% of outputs; however, safety sentence counts varied significantly across scenarios (H=86.18, p less than 0.001), with clinical cases generating more safety expressions than healthy adult cases. Conclusions: LLM-generated exercise prescriptions demonstrated high semantic consistency but showed variability in key quantitative components. Reliability depends substantially on prompt structure, and additional structural constraints and expert validation are needed before clinical deployment.

---


### 219. [Polyglot Teachers: Evaluating Language Models for Multilingual Synthetic Data Generation](https://arxiv.org/abs/2604.11290)

**<font color=#1a73e8>作者：</font>** Lester James V. Miranda, Ivan Vulić, Anna Korhonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthesizing supervised finetuning (SFT) data from language models (LMs) to teach smaller models multilingual tasks has become increasingly common. However, teacher model selection is often ad hoc, typically defaulting to the largest available option, even though such models may have significant capability gaps in non-English languages. This practice can result in poor-quality synthetic data and suboptimal student downstream performance. In this work, we systematically characterize what makes an effective multilingual teacher. We measure intrinsic measures of data quality with extrinsic student model performance in a metric we call Polyglot Score; evaluating 10 LMs across 6 typologically diverse languages, generating over 1.4M SFT examples and training 240 student models. Among the models tested, Gemma 3 27B and Aya Expanse 32B emerge as consistently effective teachers across different student base model families. Further analyses reveal that model scale alone does not significantly predict teacher effectiveness; instead, data qualities such as prompt diversity, length, and response fluency capture over 93.3% of variance in intrinsic data quality and predict student performance. Finally, we provide practical recommendations, including matching the model families of teacher-student pairs and translating from or responding to existing prompts, which can yield improvements for less-resourced languages. We hope that our work advances data-centric research in multilingual synthetic data and LM development.

---


### 220. [The Past Is Not Past: Memory-Enhanced Dynamic Reward Shaping](https://arxiv.org/abs/2604.11297)

**<font color=#1a73e8>作者：</font>** Yang Liu, Enxi Wang, Yufei Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the success of reinforcement learning for large language models, a common failure mode is reduced sampling diversity, where the policy repeatedly generates similar erroneous behaviors. Classical entropy regularization encourages randomness under the current policy, but does not explicitly discourage recurrent failure patterns across rollouts. We propose MEDS, a Memory-Enhanced Dynamic reward Shaping framework that incorporates historical behavioral signals into reward design. By storing and leveraging intermediate model representations, we capture features of past rollouts and use density-based clustering to identify frequently recurring error patterns. Rollouts assigned to more prevalent error clusters are penalized more heavily, encouraging broader exploration while reducing repeated mistakes. Across five datasets and three base models, MEDS consistently improves average performance over existing baselines, achieving gains of up to 4.13 pass@1 points and 4.37 pass@128 points. Additional analyses using both LLM-based annotations and quantitative diversity metrics show that MEDS increases behavioral diversity during sampling.

---


### 221. [Enhancing Multimodal Large Language Models for Ancient Chinese Character Evolution Analysis via Glyph-Driven Fine-Tuning](https://arxiv.org/abs/2604.11299)

**<font color=#1a73e8>作者：</font>** Rui Song, Lida Shi, Ruihua Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, rapid advances in Multimodal Large Language Models (MLLMs) have increasingly stimulated research on ancient Chinese scripts. As the evolution of written characters constitutes a fundamental pathway for understanding cultural transformation and historical continuity, how MLLMs can be systematically leveraged to support and advance text evolution analysis remains an open and largely underexplored problem. To bridge this gap, we construct a comprehensive benchmark comprising 11 tasks and over 130,000 instances, specifically designed to evaluate the capability of MLLMs in analyzing the evolution of ancient Chinese scripts. We conduct extensive evaluations across multiple widely used MLLMs and observe that, while existing models demonstrate a limited ability in glyph-level comparison, their performance on core tasks-such as character recognition and evolutionary reasoning-remains substantially constrained. Motivated by these findings, we propose a glyph-driven fine-tuning framework (GEVO) that explicitly encourages models to capture evolutionary consistency in glyph transformations and enhances their understanding of text evolution. Experimental results show that even models at the 2B scale achieve consistent and comprehensive performance improvements across all evaluated tasks. To facilitate future research, we publicly release both the benchmark and the trained models\footnote{this https URL}.

---


### 222. [PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers](https://arxiv.org/abs/2604.11307)

**<font color=#1a73e8>作者：</font>** Lei Xiong, Huaying Yuan, Zheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Leveraging Multi-modal Large Language Models (MLLMs) to accelerate frontier scientific research is promising, yet how to rigorously evaluate such systems remains unclear. Existing benchmarks mainly focus on single-document understanding, whereas real scientific workflows require integrating evidence from multiple papers, including their text, tables, and figures. As a result, multi-modal, multi-document scientific reasoning remains underexplored and lacks systematic evaluation. To address this gap, we introduce PaperScope, a multi-modal multi-document benchmark designed for agentic deep research. PaperScope presents three advantages: (1) Structured scientific grounding. It is built on a knowledge graph of over 2,000 AI papers spanning three years, providing a structured foundation for research-oriented queries. (2) Semantically dense evidence construction. It integrates semantically related key information nodes and employs optimized random-walk article selector to sample thematically coherent paper sets, thereby ensuring adequate semantic density and task complexity. (3) Multi-task evaluation of scientific reasoning. It contains over 2,000 QA pairs across reasoning, retrieval, summarization, and problem solving, enabling evaluation of multi-step scientific reasoning. Experimental results show that even advanced systems such as OpenAI Deep Research and Tongyi Deep Research achieve limited scores on PaperScope, highlighting the difficulty of long-context retrieval and deep multi-source reasoning. PaperScope thus provides a rigorous benchmark alongside a scalable pipeline for constructing large-scale multi-modal, multi-source deep research datasets.

---


### 223. [Do LLMs Know Tool Irrelevance? Demystifying Structural Alignment Bias in Tool Invocations](https://arxiv.org/abs/2604.11322)

**<font color=#1a73e8>作者：</font>** Yilong Liu, Xixun Lin, Pengfei Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated impressive capabilities in utilizing external tools. In practice, however, LLMs are often exposed to tools that are irrelevant to the user's query, in which case the desired behavior is to refrain from invocations. In this work, we identify a widespread yet overlooked mechanistic flaw in tool refusal, which we term structural alignment bias: Even when a tool fails to serve the user's goal, LLMs still tend to invoke it whenever query attributes can be validly assigned to tool parameters. To systematically study this bias, we introduce SABEval, a new dataset that decouples structural alignment from semantic relevance. Our analysis shows that structural alignment bias induces severe tool-invocation errors in LLMs, yet remains largely unaccounted for in existing evaluations. To investigate the internal mechanisms underlying this bias, we propose Contrastive Attention Attribution, which reveals two competing pathways for semantic checking and structural matching. The relative strength of these pathways drives LLMs' tool invocation decisions. Based on these findings, we further introduce a rebalancing strategy that effectively mitigates structural alignment bias, as demonstrated by extensive experiments, without degrading general tool-use capabilities.

---


### 224. [Dynamic Summary Generation for Interpretable Multimodal Depression Detection](https://arxiv.org/abs/2604.11334)

**<font color=#1a73e8>作者：</font>** Shiyu Teng, Jiaqing Liu, Hao Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Depression remains widely underdiagnosed and undertreated because stigma and subjective symptom ratings hinder reliable screening. To address this challenge, we propose a coarse-to-fine, multi-stage framework that leverages large language models (LLMs) for accurate and interpretable detection. The pipeline performs binary screening, five-class severity classification, and continuous regression. At each stage, an LLM produces progressively richer clinical summaries that guide a multimodal fusion module integrating text, audio, and video features, yielding predictions with transparent rationale. The system then consolidates all summaries into a concise, human-readable assessment report. Experiments on the E-DAIC and CMDC datasets show significant improvements over state-of-the-art baselines in both accuracy and interpretability.

---


### 225. [What Do Vision-Language Models Encode for Personalized Image Aesthetics Assessment?](https://arxiv.org/abs/2604.11374)

**<font color=#1a73e8>作者：</font>** Koki Ryu, Hitomi Yanaka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image aesthetics assessment (PIAA) is an important research problem with practical real-world applications. While methods based on vision-language models (VLMs) are promising candidates for PIAA, it remains unclear whether they internally encode rich, multi-level aesthetic attributes required for effective personalization. In this paper, we first analyze the internal representations of VLMs to examine the presence and distribution of such aesthetic attributes, and then leverage them for lightweight, individual-level personalization without model fine-tuning. Our analysis reveals that VLMs encode diverse aesthetic attributes that propagate into the language decoder layers. Building on these representations, we demonstrate that simple linear models can perform PIAA effectively. We further analyze how aesthetic information is transferred across layers in different VLM architectures and across image domains. Our findings provide insights into how VLMs can be utilized for modeling subjective, individual aesthetic preferences. Our code is available at this https URL.

---


### 226. [From Agent Loops to Structured Graphs:A Scheduler-Theoretic Framework for LLM Agent Execution](https://arxiv.org/abs/2604.11378)

**<font color=#1a73e8>作者：</font>** Hu Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dominant paradigm for building LLM based agents is the Agent Loop, an iterative cycle where a single language model decides what to do next by reading an ever growing context window. This paradigm has three structural weaknesses: implicit dependencies between steps, unbounded recovery loops, and mutable execution history that complicates debugging. We characterize the Agent Loop as a single ready unit scheduler: at any moment, at most one executable unit is active, and the choice of which unit to activate comes from opaque LLM inference rather than an inspectable policy. This perspective places Agent Loops and graph based execution engines on a single semantic continuum. We propose SGH, Structured Graph Harness, which lifts control flow from implicit context into an explicit static DAG. SGH makes three commitments: execution plans are immutable within a plan version, planning execution and recovery are separated into three layers, and recovery follows a strict escalation protocol. These choices trade some expressiveness for controllability, verifiability, and implementability. Our contributions are fourfold: a scheduler unified framework that applies classical scheduling theory to LLM agent execution and identifies challenges introduced by non deterministic LLM nodes; a trade off analysis of controllability, expressiveness, and implementability across 70 surveyed systems; a formal specification including a node state machine with termination and soundness guarantees; and an attributable experimental framework with a seven group design for future validation. This is a position paper and design proposal. We provide a theoretical framework, design analysis, and experimental protocol, not a production implementation or empirical results.

---


### 227. [Reasoning Resides in Layers: Restoring Temporal Reasoning in Video-Language Models with Layer-Selective Merging](https://arxiv.org/abs/2604.11399)

**<font color=#1a73e8>作者：</font>** Zihang Fu, Haonan Wang, Jian Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal adaptation equips large language models (LLMs) with perceptual capabilities, but often weakens the reasoning ability inherited from language-only pretraining. This trade-off is especially pronounced in video-language models (VLMs), where visual alignment can impair temporal reasoning (TR) over sequential events. We propose MERIT, a training-free, task-driven model merging framework for restoring TR in VLMs. MERIT searches over layer-wise self-attention merging recipes between a VLM and its paired text-only backbone using an objective that improves TR while penalizing degradation in temporal perception (TP). Across three representative VLMs and multiple challenging video benchmarks, MERIT consistently improves TR, preserves or improves TP, and generalizes beyond the search set to four distinct benchmarks. It also outperforms uniform full-model merging and random layer selection, showing that effective recovery depends on selecting the right layers. Interventional masking and frame-level attribution further show that the selected layers are disproportionately important for reasoning and shift model decisions toward temporally and causally relevant evidence. These results show that targeted, perception-aware model merging can effectively restore TR in VLMs without retraining.

---


### 228. [Beyond RAG for Cyber Threat Intelligence: A Systematic Evaluation of Graph-Based and Agentic Retrieval](https://arxiv.org/abs/2604.11419)

**<font color=#1a73e8>作者：</font>** Dzenan Hamzic, Florian Skopik, Max Landauer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) analysts must answer complex questions over large collections of narrative security reports. Retrieval-augmented generation (RAG) systems help language models access external knowledge, but traditional vector retrieval often struggles with queries that require reasoning over relationships between entities such as threat actors, malware, and vulnerabilities. This limitation arises because relevant evidence is often distributed across multiple text fragments and documents. Knowledge graphs address this challenge by enabling structured multi-hop reasoning through explicit representations of entities and relationships. However, multiple retrieval paradigms, including graph-based, agentic, and hybrid approaches, have emerged with different assumptions and failure modes. It remains unclear how these approaches compare in realistic CTI settings and when graph grounding improves performance. We present a systematic evaluation of four RAG architectures for CTI analysis: standard vector retrieval, graph-based retrieval over a CTI knowledge graph, an agentic variant that repairs failed graph queries, and a hybrid approach combining graph queries with text retrieval. We evaluate these systems on 3,300 CTI question-answer pairs spanning factual lookups, multi-hop relational queries, analyst-style synthesis questions, and unanswerable cases. Results show that graph grounding improves performance on structured factual queries. The hybrid graph-text approach improves answer quality by up to 35 percent on multi-hop questions compared to vector RAG, while maintaining more reliable performance than graph-only systems.

---


### 229. [Bridging What the Model Thinks and How It Speaks: Self-Aware Speech Language Models for Expressive Speech Generation](https://arxiv.org/abs/2604.11424)

**<font color=#1a73e8>作者：</font>** Kuang Wang, Lai Wei, Qibing Bai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Language Models (SLMs) exhibit strong semantic understanding, yet their generated speech often sounds flat and fails to convey expressive intent, undermining user engagement. We term this mismatch the semantic understanding-acoustic realization gap. We attribute this gap to two key deficiencies: (1) intent transmission failure, where SLMs fail to provide the stable utterance-level intent needed for expressive delivery; and (2) realization-unaware training, where no feedback signal verifies whether acoustic outputs faithfully reflect intended expression. To address these issues, we propose SA-SLM (Self-Aware Speech Language Model), built on the principle that the model should be aware of what it thinks during generation and how it speaks during training. SA-SLM addresses this gap through two core contributions: (1) Intent-Aware Bridging, which uses a Variational Information Bottleneck (VIB) objective to translate the model's internal semantics into temporally smooth expressive intent, making speech generation aware of what the model intends to express; and (2) Realization-Aware Alignment, which repurposes the model as its own critic to verify and align acoustic realization with intended expressive intent via rubric-based feedback. Trained on only 800 hours of expressive speech data, our 3B parameter SA-SLM surpasses all open-source baselines and comes within 0.08 points of GPT-4o-Audio in overall expressiveness on the EchoMind benchmark.

---


### 230. [HuiYanEarth-SAR: A Foundation Model for High-Fidelity and Low-Cost Global Remote Sensing Imagery Generation](https://arxiv.org/abs/2604.11444)

**<font color=#1a73e8>作者：</font>** Yongxiang Liu, Jie Zhou, Yafei Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Radar (SAR) imagery generation is essential for deepening the study of scattering mechanisms, establishing trustworthy electromagnetic scene models, and fundamentally alleviating the data scarcity bottleneck that constrains development in this field. However, existing methods find it difficult to simultaneously ensure high fidelity in both global geospatial semantics and microscopic scattering mechanisms, resulting in severe challenges for global generation. To address this, we propose \textbf{HuiYanEarth-SAR}, the first foundational SAR imagery generation model based on AlphaEarth and integrated scattering mechanisms. By injecting geospatial priors to control macroscopic structures and utilizing implicit scattering characteristic modeling to ensure the authenticity of microscopic textures, we achieve the capability of generating high-fidelity SAR images for global locations solely based on geographic coordinates. This study not only constructs an efficient SAR scene simulator but also establishes a bridge connecting geography, scatter mechanism, and artificial intelligence from a methodological standpoint. It advances SAR research by expanding the paradigm from perception and understanding to simulation and creation, providing key technical support for constructing a high-confidence digital twin of the Earth.

---


### 231. [Low-rank Optimization Trajectories Modeling for LLM RLVR Acceleration](https://arxiv.org/abs/2604.11446)

**<font color=#1a73e8>作者：</font>** Zhipeng Chen, Tao Qian, Wayne Xin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, scaling reinforcement learning with verifiable rewards (RLVR) for large language models (LLMs) has emerged as an effective training paradigm for significantly improving model capabilities, which requires guiding the model to perform extensive exploration and learning, leading to substantial computational overhead and becoming a key challenge. To reduce the number of training steps, Prior work performs linear extrapolation of model parameters. However, the dynamics of model parameter updates during RLVR training remain insufficiently understood. To further investigate the evolution of LLMs during RLVR training, we conduct empirical experiments and find that the rank-1 subspace of the model does not evolve linearly, and its dominance over the original parameters is further amplified during LoRA training. Based on the above insights, we propose the \textbf{N}onlinear \textbf{Ext}rapolation of low-rank trajectories (\textbf{NExt}), a novel framework that models and extrapolates low-rank parameter trajectories in a nonlinear manner. Concretely, we first train the model using LoRA and extract the rank-1 subspace of parameter differences at multiple training steps, which is then used for the subsequent nonlinear extrapolation. Afterward, we utilized the extracted rank-1 subspace to train a predictor, which can model the trajectory of parameter updates during RLVR, and then perform the predict-extend process to extrapolate model parameters, achieving the acceleration of RLVR. To further study and understand NExt, we conduct comprehensive experiments that demonstrate the effectiveness and robustness of the method. Our method reduces computational overhead by approximately 37.5\% while remaining compatible with a wide range of RLVR algorithms and tasks. We release our code in this https URL.

---


### 232. [Escaping the Context Bottleneck: Active Context Curation for LLM Agents via Reinforcement Learning](https://arxiv.org/abs/2604.11462)

**<font color=#1a73e8>作者：</font>** Xiaozhe Li, Tianyi Lyu, Yizhao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) struggle with long-horizon tasks due to the "context bottleneck" and the "lost-in-the-middle" phenomenon, where accumulated noise from verbose environments degrades reasoning over multi-turn interactions. To address this issue, we introduce a symbiotic framework that decouples context management from task execution. Our architecture pairs a lightweight, specialized policy model, ContextCurator, with a powerful frozen foundation model, TaskExecutor. Trained via reinforcement learning, ContextCurator actively reduces information entropy in the working memory. It aggressively prunes environmental noise while preserving reasoning anchors, that is, sparse data points that are critical for future deductions. On WebArena, our framework improves the success rate of Gemini-3.0-flash from 36.4% to 41.2% while reducing token consumption by 8.8% (from 47.4K to 43.3K). On DeepSearch, it achieves a 57.1% success rate, compared with 53.9%, while reducing token consumption by a factor of 8. Remarkably, a 7B ContextCurator matches the context management performance of GPT-4o, providing a scalable and computationally efficient paradigm for autonomous long-horizon agents.

---


### 233. [Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents](https://arxiv.org/abs/2604.11465)

**<font color=#1a73e8>作者：</font>** S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents show promise on realistic tool-use tasks, but deploying capable agents on modest hardware remains challenging. We study whether inference-time scaffolding alone, without any additional training compute, can improve the performance of a small model in complex multi-step environments. Operating on a single 24\,GB GPU, we evaluate Qwen3-8B under both full-precision (FP16, 12K context) and 4-bit quantized (AWQ, 32K context) configurations. Without any intervention, the raw model achieves just 5.4\% (FP16) and 3.0\% (AWQ) task goal completion. Guided by a systematic failure mode analysis, we introduce a three-tier inference scaffolding pipeline that deploys the same frozen model in three distinct roles: (1) a summarization model that preserves critical artifacts (tokens, credentials, API responses) while compressing dialogue history; (2) the main agent model that reasons over the compressed context; and (3) an isolated correction model that reviews and revises the agent's code output without access to conversation history, breaking repetitive failure loops. Applied to the same unmodified model, this scaffolding yields 8.9\% (FP16) and 5.9\% (AWQ) task goal completion, roughly doubling performance in both settings, with particularly strong gains on difficulty-1 tasks (15.8\%$\to$26.3\% FP16; 5.3\%$\to$14.0\% AWQ). On full-precision inference, our scaffolded 8B model surpasses DeepSeek-Coder 33B Instruct (7.1\%) from the original AppWorld evaluation, demonstrating that structured inference-time interventions can make small models competitive with systems 4$\times$ their size. We formalize the approach as a scaffolded policy over a frozen base model, three invocations of the same weights with different conditioning, drawing connections to test-time compute scaling and action-space shaping in reinforcement learning.

---


### 234. [Learning How Much to Think: Difficulty-Aware Dynamic MoEs for Graph Node Classification](https://arxiv.org/abs/2604.11473)

**<font color=#1a73e8>作者：</font>** Jiajun Zhou, Yadong Li, Xuanze Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures offer a scalable path for Graph Neural Networks (GNNs) in node classification tasks but typically rely on static and rigid routing strategies that enforce a uniform expert budget or coarse-grained expert toggles on all nodes. This limitation overlooks the varying discriminative difficulty of nodes and leads to under-fitting for hard nodes and redundant computation for easy ones. To resolve this issue, we propose D2MoE, a novel framework that shifts the focus from static expert selection to node-wise expert resource allocation. By using predictive entropy as a real-time proxy for difficulty, D2MoE employs a difficulty-driven top-p routing mechanism to adaptively concentrate expert resources on hard nodes while reducing overhead for easy ones, achieving continuous and fine-grained expert budget scaling for node classification. Experiments on 13 benchmarks demonstrate that D2MoE achieves consistent state-of-the-art performance, surpassing leading baselines by up to 7.92% in accuracy on heterophilous graphs. Notably, on large-scale graphs, it reduces memory consumption by up to 73.07% and training time by 46.53% compared to the best-performing Graph MoE, thereby validating its superior efficiency.

---


### 235. [OOM-RL: Out-of-Money Reinforcement Learning Market-Driven Alignment for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2604.11477)

**<font color=#1a73e8>作者：</font>** Kun Liu, Liqun Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The alignment of Multi-Agent Systems (MAS) for autonomous software engineering is constrained by evaluator epistemic uncertainty. Current paradigms, such as Reinforcement Learning from Human Feedback (RLHF) and AI Feedback (RLAIF), frequently induce model sycophancy, while execution-based environments suffer from adversarial "Test Evasion" by unconstrained agents. In this paper, we introduce an objective alignment paradigm: \textbf{Out-of-Money Reinforcement Learning (OOM-RL)}. By deploying agents into the non-stationary, high-friction reality of live financial markets, we utilize critical capital depletion as an un-hackable negative gradient. Our longitudinal 20-month empirical study (July 2024 -- February 2026) chronicles the system's evolution from a high-turnover, sycophantic baseline to a robust, liquidity-aware architecture. We demonstrate that the undeniable ontological consequences of financial loss forced the MAS to abandon overfitted hallucinations in favor of the \textbf{Strict Test-Driven Agentic Workflow (STDAW)}, which enforces a Byzantine-inspired uni-directional state lock (RO-Lock) anchored to a deterministically verified $\geq 95\%$ code coverage constraint matrix. Our results show that while early iterations suffered severe execution decay, the final OOM-RL-aligned system achieved a stable equilibrium with an annualized Sharpe ratio of 2.06 in its mature phase. We conclude that substituting subjective human preference with rigorous economic penalties provides a robust methodology for aligning autonomous agents in high-stakes, real-world environments, laying the groundwork for generalized paradigms where computational billing acts as an objective physical constraint

---


### 236. [CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation](https://arxiv.org/abs/2604.11483)

**<font color=#1a73e8>作者：</font>** Yanting Li, Zhuoyang Jiang, Enyan Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Goal-directed molecular generation requires satisfying heterogeneous constraints such as protein--ligand compatibility and multi-objective drug-like properties, yet existing methods often optimize these constraints in isolation, failing to reconcile conflicting objectives (e.g., affinity vs. safety), and struggle to navigate the non-differentiable chemical space without compromising structural validity. To address these challenges, we propose CAGenMol, a condition-aware discrete diffusion framework over molecular sequences that formulates molecular design as conditional denoising guided by heterogeneous structural and property signals. By coupling discrete diffusion with reinforcement learning, the model aligns the generation trajectory with non-differentiable objectives while preserving chemical validity and diversity. The non-autoregressive nature of diffusion language model further enables iterative refinement of molecular fragments at inference time. Experiments on structure-conditioned, property-conditioned, and dual-conditioned benchmarks demonstrate consistent improvements over state-of-the-art methods in binding affinity, drug-likeness, and success rate, highlighting the effectiveness of our framework.

---


### 237. [Anthropogenic Regional Adaptation in Multimodal Vision-Language Model](https://arxiv.org/abs/2604.11490)

**<font color=#1a73e8>作者：</font>** Samuel Cahyawijaya, Peerat Limkonchotiwat, Tack Hwa Wong 等 46 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While the field of vision-language (VL) has achieved remarkable success in integrating visual and textual information across multiple languages and domains, there is still no dedicated framework for assessing human-centric alignment in vision-language systems. We offer two contributions to address this gap. First, we introduce Anthropogenic Regional Adaptation: a novel paradigm that aims to optimize model relevance to specific regional contexts while ensuring the retention of global generalization capabilities. Second, we present a simple, but effective adaptation method named Geographical-generalization-made-easy (GG-EZ), which utilizes regional data filtering and model merging. Through comprehensive experiments on 3 VL architectures: large vision-language models, text-to-image diffusion models, and vision-language embedding models, and a case study in Southeast Asia (SEA) regional adaptation, we demonstrate the importance of Anthropogenic Regional Adaptation and the effectiveness of GG-EZ, showing 5-15% gains in cultural relevance metrics across SEA while maintaining over 98% of global performance and even occasionally surpassing it. Our findings establish Anthropogenic Regional Alignment as a foundational paradigm towards applicability of multimodal vision-language models in diverse regions and demonstrate a simple-yet-effective baseline method that optimizes regional value alignment while preserving global generalization.

---


### 238. [Revisiting Compositionality in Dual-Encoder Vision-Language Models: The Role of Inference](https://arxiv.org/abs/2604.11496)

**<font color=#1a73e8>作者：</font>** Imanol Miranda, Ander Salaberria, Eneko Agirre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-encoder Vision-Language Models (VLMs) such as CLIP are often characterized as bag-of-words systems due to their poor performance on compositional benchmarks. We argue that this limitation may stem less from deficient representations than from the standard inference protocol based on global cosine similarity. First, through controlled diagnostic experiments, we show that explicitly enforcing fine-grained region-segment alignment at inference dramatically improves compositional performance without updating pretrained encoders. We then introduce a lightweight transformer that learns such alignments directly from frozen patch and token embeddings. Comparing against full fine-tuning and prior end-to-end compositional training methods, we find that although these approaches improve in-domain retrieval, their gains do not consistently transfer under distribution shift. In contrast, learning localized alignment over frozen representations matches full fine-tuning on in-domain retrieval while yielding substantial improvements on controlled out-of-domain compositional benchmarks. These results identify global embedding matching as a key bottleneck in dual-encoder VLMs and highlight the importance of alignment mechanisms for robust compositional generalization.

---


### 239. [METER: Evaluating Multi-Level Contextual Causal Reasoning in Large Language Models](https://arxiv.org/abs/2604.11502)

**<font color=#1a73e8>作者：</font>** Pengfeng Li, Chen Huang, Chaoqun Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual causal reasoning is a critical yet challenging capability for Large Language Models (LLMs). Existing benchmarks, however, often evaluate this skill in fragmented settings, failing to ensure context consistency or cover the full causal hierarchy. To address this, we pioneer METER to systematically benchmark LLMs across all three levels of the causal ladder under a unified context setting. Our extensive evaluation of various LLMs reveals a significant decline in proficiency as tasks ascend the causal hierarchy. To diagnose this degradation, we conduct a deep mechanistic analysis via both error pattern identification and internal information flow tracing. Our analysis reveals two primary failure modes: (1) LLMs are susceptible to distraction by causally irrelevant but factually correct information at lower level of causality; and (2) as tasks ascend the causal hierarchy, faithfulness to the provided context degrades, leading to a reduced performance. We belive our work advances our understanding of the mechanisms behind LLM contextual causal reasoning and establishes a critical foundation for future research. Our code and dataset are available at this https URL .

---


### 240. [Policy Split: Incentivizing Dual-Mode Exploration in LLM Reinforcement with Dual-Mode Entropy Regularization](https://arxiv.org/abs/2604.11510)

**<font color=#1a73e8>作者：</font>** Jiashu Yao, Heyan Huang, Chuwei Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To encourage diverse exploration in reinforcement learning (RL) for large language models (LLMs) without compromising accuracy, we propose Policy Split, a novel paradigm that bifurcates the policy into normal and high-entropy modes with a high-entropy prompt. While sharing model parameters, the two modes undergo collaborative dual-mode entropy regularization tailored to distinct objectives. Specifically, the normal mode optimizes for task correctness, while the high-entropy mode incorporates a preference for exploration, and the two modes learn collaboratively. Extensive experiments demonstrate that our approach consistently outperforms established entropy-guided RL baselines across various model sizes in general and creative tasks. Further analysis reveals that Policy Split facilitates dual-mode exploration, where the high-entropy mode generates distinct behavioral patterns to the normal mode, providing unique learning signals.

---


### 241. [SVD-Prune: Training-Free Token Pruning For Efficient Vision-Language Models](https://arxiv.org/abs/2604.11530)

**<font color=#1a73e8>作者：</font>** Yvon Apedo, Martyna Poreba, Michal Szczepanski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLM) have revolutionized multimodal learning by jointly processing visual and textual information. Yet, they face significant challenges due to the high computational and memory demands of processing long sequences of vision tokens. Many existing methods rely on local heuristics, such as attention scores or token norms. However, these criteria suffer from positional bias and information dispersion, limiting their ability to preserve essential content at high pruning ratios and leading to performance degradation on visually detailed images. To address these issues, we propose SVD-Prune, a trainingfree, plug-and-play token pruning method based on Singular Value Decomposition. It decomposes the vision token feature matrix and selects the top-K tokens using statistical leverage scores, ensuring only tokens contributing most to the dominant global variance are preserved. Experiments show that SVD-Prune consistently outperforms prior pruning methods under extreme vision token budgets, maintaining strong performance even with 32 and 16 vision tokens.

---


### 242. [Problem Reductions at Scale: Agentic Integration of Computationally Hard Problems](https://arxiv.org/abs/2604.11535)

**<font color=#1a73e8>作者：</font>** Xi-Wei Pan, Shi-Wen An, Jin-Guo Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving an NP-hard optimization problem often requires reformulating it for a specific solver -- quantum hardware, a commercial optimizer, or a domain heuristic. A tool for polynomial-time reductions between hard problems would let practitioners route any supported problem to any supported solver through a single interface. Building such a library at scale, however, has remained out of reach. We show that harness engineering, the practice of designing constraints, verification systems, and feedback loops that channel AI coding agents, can overcome this barrier. Our harness combines a no-code contribution route for domain experts, a multilayer verification stack ranging from type-level checks to agentic feature tests (AI agents role-playing as end users), and a fully automated implementation-review-integration pipeline. In about three months, we built a command-line tool backed by a library of 100+ problem types and 200+~reduction rules in over 170k lines of Rust. The result suggests that a well-engineered harness lets agents build well-tested software at a scale and pace beyond prior reduction-library efforts. Because the reduction graph composes transitively, a new solver registered for any single problem type instantly becomes available to every problem connected by a reduction path. The source code is available at this https URL.

---


### 243. [NovBench: Evaluating Large Language Models on Academic Paper Novelty Assessment](https://arxiv.org/abs/2604.11543)

**<font color=#1a73e8>作者：</font>** Wenqing Wu, Yi Zhao, Yuzhuo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Novelty is a core requirement in academic publishing and a central focus of peer review, yet the growing volume of submissions has placed increasing pressure on human reviewers. While large language models (LLMs), including those fine-tuned on peer review data, have shown promise in generating review comments, the absence of a dedicated benchmark has limited systematic evaluation of their ability to assess research novelty. To address this gap, we introduce NovBench, the first large-scale benchmark designed to evaluate LLMs' capability to generate novelty evaluations in support of human peer review. NovBench comprises 1,684 paper-review pairs from a leading NLP conference, including novelty descriptions extracted from paper introductions and corresponding expert-written novelty evaluations. We focus on both sources because the introduction provides a standardized and explicit articulation of novelty claims, while expert-written novelty evaluations constitute one of the current gold standards of human judgment. Furthermore, we propose a four-dimensional evaluation framework (including Relevance, Correctness, Coverage, and Clarity) to assess the quality of LLM-generated novelty evaluations. Extensive experiments on both general and specialized LLMs under different prompting strategies reveal that current models exhibit limited understanding of scientific novelty, and that fine--tuned models often suffer from instruction-following deficiencies. These findings underscore the need for targeted fine-tuning strategies that jointly improve novelty comprehension and instruction adherence.

---


### 244. [Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and Agentic Memory](https://arxiv.org/abs/2604.11544)

**<font color=#1a73e8>作者：</font>** Weixian Waylon Li, Jiaxin Zhang, Xianan Jim Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured memory representations such as knowledge graphs are central to autonomous agents and other long-lived systems. However, most existing approaches model time as discrete metadata, either sorting by recency (burying old-yet-permanent knowledge), simply overwriting outdated facts, or requiring an expensive LLM call at every ingestion step, leaving them unable to distinguish persistent facts from evolving ones. To address this, we introduce RoMem, a drop-in temporal knowledge graph module for structured memory systems, applicable to agentic memory and beyond. A pretrained Semantic Speed Gate maps each relation's text embedding to a volatility score, learning from data that evolving relations (e.g., "president of") should rotate fast while persistent ones (e.g., "born in") should remain stable. Combined with continuous phase rotation, this enables geometric shadowing: obsolete facts are rotated out of phase in complex vector space, so temporally correct facts naturally outrank contradictions without deletion. On temporal knowledge graph completion, RoMem achieves state-of-the-art results on ICEWS05-15 (72.6 MRR). Applied to agentic memory, it delivers 2-3x MRR and answer accuracy on temporal reasoning (MultiTQ), dominates hybrid benchmark (LoCoMo), preserves static memory with zero degradation (DMR-MSC), and generalises zero-shot to unseen financial domains (FinTMMBench).

---


### 245. [Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach](https://arxiv.org/abs/2604.11547)

**<font color=#1a73e8>作者：</font>** Haolin Li, Shuyang Jiang, Ruipeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While large language models hold promise for complex medical applications, their development is hindered by the scarcity of high-quality reasoning data. To address this issue, existing approaches typically distill chain-of-thought reasoning traces from large proprietary models via supervised fine-tuning, then conduct reinforcement learning (RL). These methods exhibit limited improvement on underrepresented domains like rare diseases while incurring substantial costs from generating complex reasoning chains. To efficiently enhance medical reasoning, we propose MedSSR, a Medical Knowledge-enhanced data Synthesis and Semi-supervised Reinforcement learning framework. Our framework first employs rare disease knowledge to synthesize distribution-controllable reasoning questions. We then utilize the policy model itself to generate high-quality pseudo-labels. This enables a two-stage, intrinsic-to-extrinsic training paradigm: self-supervised RL on the pseudo-labeled synthetic data, followed by supervised RL on the human-annotated real data. MedSSR scales model training efficiently without relying on costly trace distillation. Extensive experiments on Qwen and Llama demonstrate that our method outperforms existing methods across ten medical benchmarks, achieving up to +5.93% gain on rare-disease tasks. Our code is available at this https URL.

---


### 246. [Relax: An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at Scale](https://arxiv.org/abs/2604.11554)

**<font color=#1a73e8>作者：</font>** Liujie Zhang, Benzhe Ning, Rui Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training has proven effective at unlocking reasoning, self-reflection, and tool-use capabilities in large language models. As models extend to omni-modal inputs and agentic multi-turn workflows, RL training systems face three interdependent challenges: heterogeneous data flows, operational robustness at scale, and the staleness -- throughput tradeoff. We present \textbf{Relax} (Reinforcement Engine Leveraging Agentic X-modality), an open-source RL training engine that addresses these challenges through three co-designed architectural layers. First, an \emph{omni-native architecture} builds multimodal support into the full stack -- from data preprocessing and modality-aware parallelism to inference generation -- rather than retrofitting it onto a text-centric pipeline. Second, each RL role runs as an independent, fault-isolated service that can be scaled, recovered, and upgraded without global coordination. Third, service-level decoupling enables asynchronous training via the TransferQueue data bus, where a single staleness parameter smoothly interpolates among on-policy, near-on-policy, and fully asynchronous execution. Relax achieves a 1.20$\times$ end-to-end speedup over veRL on Qwen3-4B on-policy training. Its fully async mode delivers a 1.76$\times$ speedup over colocate on Qwen3-4B and a 2.00$\times$ speedup on Qwen3-Omni-30B, while all modes converge to the same reward level. Relax supports R3 (Rollout Routing Replay)~\cite{ma2025r3} for MoE models with only 1.9\% overhead, compared to 32\% degradation in veRL under the same configuration. It further demonstrates stable omni-modal RL convergence on Qwen3-Omni across image, text, and audio, sustaining over 2{,}000 steps on video without degradation. Relax is available at this https URL.

---


### 247. [UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents](https://arxiv.org/abs/2604.11557)

**<font color=#1a73e8>作者：</font>** Yijuan Liang, Xinghao Chen, Yifan Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-use capability is a fundamental component of LLM agents, enabling them to interact with external systems through structured function calls. However, existing research exhibits inconsistent interaction representations, largely overlooks the structural distribution of tool-use trajectories, and relies on incompatible evaluation benchmarks. We present UniToolCall, a unified framework for tool learning that standardizes the entire pipeline from toolset construction and dataset generation to evaluation. The framework curates a large tool pool of 22k+ tools and constructs a hybrid training corpus of 390k+ instances by combining 10 standardized public datasets with structurally controlled synthetic trajectories. It explicitly models diverse interaction patterns, including single-hop vs. multi-hop and single-turn vs. multi-turn, while capturing both serial and parallel execution structures. To support coherent multi-turn reasoning, we further introduce an Anchor Linkage mechanism that enforces cross-turn dependencies. Furthermore, we convert 7 public benchmarks into a unified Query--Action--Observation--Answer (QAOA) representation with fine-grained evaluation at the function-call, turn, and conversation levels. Experiments show that fine-tuning Qwen3-8B on our dataset substantially improves tool-use performance. Under the distractor-heavy Hybrid-20 setting, achieves 93.0% single-turn Strict Precision, outperforming commercial models including GPT, Gemini, and Claude.

---


### 248. [From Multimodal Signals to Adaptive XR Experiences for De-escalation Training](https://arxiv.org/abs/2604.11570)

**<font color=#1a73e8>作者：</font>** Birgit Nierula, Karam Tomotaki-Dawoud, Daniel Johannes Meyer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present the early-stage design and implementation of a multimodal, real-time communication analysis system intended as a foundational interaction layer for adaptive VR training. The system integrates five parallel processing streams: (1) verbal and prosodic speech analysis, (2) skeletal gesture recognition from multi-view RGB cameras, (3) multimodal affective analysis combining lower-face video with upper-face facial EMG, (4) EEG-based mental state decoding, and (5) physiological arousal estimation from skin conductance, heart activity, and proxemic behavior. All signals are synchronized via Lab Streaming Layer to enable temporally aligned, continuous assessments of users' conscious and unconscious communication cues. Building on concepts from social semiotics and symbolic interactionism, we introduce an interpretation layer that links low-level signal representations to interactional constructs such as escalation and de-escalation. This layer is informed by domain knowledge from police instructors and lay participants, grounding system responses in realistic conflict scenarios. We demonstrate the feasibility and limitations of automated cue extraction in an XR-based de-escalation training project for law enforcement, reporting preliminary results for gesture recognition, emotion recognition under HMD occlusion, verbal assessment, mental state decoding, and physiological arousal. Our findings highlight the value of multi-view sensing and multimodal fusion for overcoming occlusion and viewpoint challenges, while underscoring that fusion and feedback must be treated as design problems rather than purely technical ones. The work contributes design resources and empirical insights for shaping human-AI-powered XR training in complex interpersonal settings.

---


### 249. [MIXAR: Scaling Autoregressive Pixel-based Language Models to Multiple Languages and Scripts](https://arxiv.org/abs/2604.11575)

**<font color=#1a73e8>作者：</font>** Chen Hu, Yintao Tai, Antonio Vergari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pixel-based language models are gaining momentum as alternatives to traditional token-based approaches, promising to circumvent tokenization challenges. However, the inherent perceptual diversity across languages poses a significant hurdle for multilingual generalization in pixel space. This paper introduces MIXAR, the first generative pixel-based language model trained on eight different languages utilizing a range of different scripts. We empirically evaluate MIXAR against previous pixel-based models as well as comparable tokenizer-based models, demonstrating substantial performance improvement on discriminative and generative multilingual tasks. Additionally, we show how MIXAR is robust to languages never seen during the training. These results are further strengthened when scaling the model to 0.5B parameters which not only improves its capabilities in generative tasks like LAMBADA but also its robustness when challenged with input perturbations such as orthographic attacks.

---


### 250. [Finetune Like You Pretrain: Boosting Zero-shot Adversarial Robustness in Vision-language Models](https://arxiv.org/abs/2604.11576)

**<font color=#1a73e8>作者：</font>** Songlong Xing, Weijie Wang, Zhengyu Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite their impressive zero-shot abilities, vision-language models such as CLIP have been shown to be susceptible to adversarial attacks. To enhance its adversarial robustness, recent studies finetune the pretrained vision encoder of CLIP with adversarial examples on a proxy dataset such as ImageNet by aligning adversarial images with correct class labels. However, these methods overlook the important roles of training data distributions and learning objectives, resulting in reduced zero-shot capabilities and limited transferability of robustness across domains and datasets. In this work, we propose a simple yet effective paradigm AdvFLYP, which follows the training recipe of CLIP's pretraining process when performing adversarial finetuning to the model. Specifically, AdvFLYP finetunes CLIP with adversarial images created based on image-text pairs collected from the web, and match them with their corresponding texts via a contrastive loss. To alleviate distortion of adversarial image embeddings of noisy web images, we further propose to regularise AdvFLYP by penalising deviation of adversarial image features. We show that logit- and feature-level regularisation terms benefit robustness and clean accuracy, respectively. Extensive experiments on 14 downstream datasets spanning various domains show the superiority of our paradigm over mainstream practices. Our code and model weights are released at this https URL.

---


### 251. [Decomposing and Reducing Hidden Measurement Error in LLM Evaluation Pipelines](https://arxiv.org/abs/2604.11581)

**<font color=#1a73e8>作者：</font>** Solomon Messing  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM evaluations drive which models get deployed, which safety standards get adopted, and which research conclusions get published. Yet these scores carry hidden uncertainty: rephrasing the prompt, switching the judge model, or changing the temperature can shift results enough to flip rankings and reverse conclusions. Standard confidence intervals ignore this variance, producing under-coverage that worsens with more data. The unmeasured variance also creates an exploitable surface: model developers can optimize against measurement noise rather than genuine capability. This paper decomposes LLM pipeline uncertainty into its sources, distinguishes variance that shrinks with more data from sensitivity to researcher design choices, and projects the most efficient path to reducing total error. For benchmark builders, the same decomposition identifies which design choices contribute exploitable surface for gaming and prescribes designs that minimize it. Across ideology annotation, safety classification, MMLU benchmarking, and a human-validated propaganda audit, projection-optimized pipelines outperform 73\% of possible naive pipelines against a human baseline. On MMLU, optimized budget allocation halves estimation error compared to standard single-prompt evaluation at equivalent cost. A small-sample variance estimation exercise is sufficient to derive confidence intervals that approach nominal coverage when the model includes the relevant pipeline facets, and to generate recommendations for reducing measurement error and improving benchmark robustness.

---


### 252. [A Triadic Suffix Tokenization Scheme for Numerical Reasoning](https://arxiv.org/abs/2604.11582)

**<font color=#1a73e8>作者：</font>** Olga Chetverina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard subword tokenization methods fragment numbers inconsistently, causing large language models (LLMs) to lose positional and decimal structure - a primary driver of errors in arithmetic and scientific reasoning. We introduce Triadic Suffix Tokenization (TST), a deterministic scheme that partitions digits into three-digit triads and annotates each triad with an explicit magnitude marker. Critically, the scheme defines a fixed, one-to-one mapping between suffixes and orders of magnitude for the integer part (thousands, millions, billions, etc.) and a parallel system of replicated markers for fractional depth (tenths, thousandths, millionths, etc.). Unlike approaches that rely on positional inference, this method provides a consistent gradient signal, which should ensure stable convergence. Two implementation variants are proposed: (1) a vocabulary-based approach that adds at most 10,000 fixed tokens to an existing vocabulary, covering 33 orders of magnitude ($10^{-15}$ to $10^{18}$); and (2) a suffix-marker approach that uses a small set of special tokens to denote magnitude dynamically. Both variants preserve exact digits while making order-of-magnitude relationships transparent at the token level. The framework is inherently scalable, allowing for linear vocabulary expansion to accommodate arbitrary precision and range. TST is architecture-agnostic and can be integrated as a drop-in preprocessing step. Experimental validation is deferred to future work.

---


### 253. [MLLM-as-a-Judge Exhibits Model Preference Bias](https://arxiv.org/abs/2604.11589)

**<font color=#1a73e8>作者：</font>** Shuitsu Koyama, Yuiga Wada, Daichi Yashima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation using multimodal large language models (MLLMs), commonly referred to as MLLM-as-a-Judge, has been widely used to measure model performance. If such MLLM-as-a-Judge methods were biased, they could distort model comparisons and benchmark-driven scientific progress. However, it remains unclear to what extent MLLM-as-a-Judge methods favor or disfavor text generated by specific MLLMs. In this study, we propose Philautia-Eval to investigate such model-specific preference bias. Philautia-Eval quantifies the degree of the bias by disentangling preference tendencies from differences in generation quality. Using 1.29M caption-score pairs collected from 12 MLLMs, we found that representative MLLMs tend to exhibit self-preference bias. Moreover, experimental results indicate mutual preference bias within particular model families, which is potentially driven by reused connectors and overlapping instruction-tuning resources. Finally, we introduce a simple ensemble of MLLMs, Pomms. Our results demonstrated that Pomms effectively mitigated the model-specific preference bias while maintaining performance.

---


### 254. [Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language](https://arxiv.org/abs/2604.11600)

**<font color=#1a73e8>作者：</font>** Peijie Wang, Ming-Liang Zhang, Jun Cao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress but continue to struggle with geometric reasoning, primarily due to the perception bottleneck regarding fine-grained visual elements. While formal languages have aided plane geometry understanding, solid geometry which requires spatial understanding remains largely unexplored. In this paper, we address this challenge by designing a unified formal language that integrates plane and solid geometry, comprehensively covering geometric structures and semantic relations. We construct GDP-29K, a large-scale dataset comprising 20k plane and 9k solid geometry samples collected from diverse real-world sources, each paired with its ground-truth formal description. To ensure syntactic correctness and geometric consistency, we propose a training paradigm that combines Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards. Experiments show that our approach achieves state-of-the-art parsing performance. Furthermore, we demonstrate that our parsed formal descriptions serve as a critical cognitive scaffold, significantly boosting MLLMs' capabilities for downstream geometry reasoning tasks. Our data and code are available at Geoparsing.

---


### 255. [Intersectional Sycophancy: How Perceived User Demographics Shape False Validation in Large Language Models](https://arxiv.org/abs/2604.11609)

**<font color=#1a73e8>作者：</font>** Benjamin Maltbie, Shivam Raval  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit sycophantic tendencies--validating incorrect user beliefs to appear agreeable. We investigate whether this behavior varies systematically with perceived user demographics, testing whether combinations of race, age, gender, and expressed confidence level produce differential false validation rates. Inspired by the legal concept of intersectionality, we conduct 768 multi-turn adversarial conversations using Anthropic's Petri evaluation framework, probing GPT-5-nano and Claude Haiku 4.5 across 128 persona combinations in mathematics, philosophy, and conspiracy theory domains. GPT-5-nano is significantly more sycophantic than Claude Haiku 4.5 overall ($\bar{x}=2.96$ vs. $1.74$, $p < 10^{-32}$, Wilcoxon signed-rank). For GPT-5-nano, we find that philosophy elicits 41% more sycophancy than mathematics and that Hispanic personas receive the highest sycophancy across races. The worst-scoring persona, a confident, 23-year-old Hispanic woman, averages 5.33/10 on sycophancy. Claude Haiku 4.5 exhibits uniformly low sycophancy with no significant demographic variation. These results demonstrate that sycophancy is not uniformly distributed across users and that safety evaluations should incorporate identity-aware testing.

---


### 256. [Self-Evolving LLM Memory Extraction Across Heterogeneous Tasks](https://arxiv.org/abs/2604.11610)

**<font color=#1a73e8>作者：</font>** Yuqing Yang, Tengxiao Liu, Wang Bill Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM-based assistants become persistent and personalized, they must extract and retain useful information from past conversations as memory. However, the types of information worth remembering vary considerably across tasks. We formalize the \textit{heterogeneous memory extraction} task and introduce \textbf{BEHEMOTH}, a benchmark that repurposes 18 existing datasets spanning personalization, problem-solving, and agentic tasks, using a downstream utility-driven metric for systematic evaluation. Our empirical analysis confirms that no single static extraction prompt dominates across all task categories, and that existing self-evolving prompt optimization frameworks, originally designed for homogeneous distributions, degrade when training tasks are heterogeneous. To address this, we propose \textbf{CluE}, a cluster-based self-evolving strategy that groups training examples into clusters by extraction scenarios, analyzes each cluster independently, and synthesizes cross-cluster insights to update the extraction prompt. Experiments on BEHEMOTH show that CluE generalizes effectively across heterogeneous tasks ($+$9.04\% relative gain), consistently outperforming prior self-evolving frameworks.

---


### 257. [Utilizing and Calibrating Hindsight Process Rewards via Reinforcement with Mutual Information Self-Evaluation](https://arxiv.org/abs/2604.11611)

**<font color=#1a73e8>作者：</font>** Jiashu Yao, Heyan Huang, Zeming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To overcome the sparse reward challenge in reinforcement learning (RL) for agents based on large language models (LLMs), we propose Mutual Information Self-Evaluation (MISE), an RL paradigm that utilizes hindsight generative self-evaluation as dense reward signals while simultaneously calibrating them against the environmental feedbacks. Empirically, MISE enables an agent to learn autonomously from dense internal rewards supplementing sparse extrinsic signals. Theoretically, our work provides the first formal foundation for the paradigm of generative self-rewarding. We prove that utilizing hindsight self-evaluation rewards is equivalent to minimizing an objective that combines mutual information with a KL divergence term between the policy and a proxy reward policy. This theoretical insight then informs and justifies our calibration step, which actively aligns these rewards with the optimal policy. Extensive experiments show that MISE outperforms strong baselines, enabling open-source LLMs about 7B parameters to achieve performance comparable to GPT-4o on validation without expert supervision.

---


### 258. [Context Kubernetes: Declarative Orchestration of Enterprise Knowledge for Agentic AI Systems](https://arxiv.org/abs/2604.11623)

**<font color=#1a73e8>作者：</font>** Charafeddine Mouzouni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Context Kubernetes, an architecture for orchestrating enterprise knowledge in agentic AI systems, with a prototype implementation and eight experiments. The core observation is that delivering the right knowledge, to the right agent, with the right permissions, at the right freshness -- across an entire organization -- is structurally analogous to the container orchestration problem Kubernetes solved a decade ago. We formalize six core abstractions, a YAML-based declarative manifest for knowledge-architecture-as-code, a reconciliation loop, and a three-tier agent permission model where agent authority is always a strict subset of human authority. Three value experiments show: (1) without governance, agents serve phantom content from deleted sources and leak cross-domain data in 26.5% of queries; (2) without freshness monitoring, stale content is served silently -- with reconciliation, staleness is detected in under 1ms; (3) in five attack scenarios, flat permissions block 0/5 attacks, basic RBAC blocks 4/5, and the three-tier model blocks 5/5. Five correctness experiments confirm zero unauthorized deliveries, zero invariant violations, and architectural enforcement of out-of-band approval isolation that no surveyed enterprise platform provides. A survey of four major platforms (Microsoft, Salesforce, AWS, Google) documents that none architecturally isolates agent approval channels. We identify four properties that make context orchestration harder than container orchestration, and argue that these make the solution more valuable.

---


### 259. [SCNO: Spiking Compositional Neural Operator -- Towards a Neuromorphic Foundation Model for Nuclear PDE Solving](https://arxiv.org/abs/2604.11625)

**<font color=#1a73e8>作者：</font>** Samrendra Roy, Souvik Chakraborty, Rizwan-uddin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as powerful surrogates for partial differential equation (PDE) solvers, yet they are typically trained as monolithic models for individual PDEs, require energy-intensive GPU hardware, and must be retrained from scratch when new physics emerge. We introduce the Spiking Compositional Neural Operator (SCNO), a modular architecture combining spiking and conventional components that addresses all three limitations. SCNO maintains a library of small spiking neural operator blocks, each trained on a single elementary differential operator (convection, diffusion, reaction), and composes them through a lightweight input-conditioned aggregator to solve coupled PDEs not seen during block training. A small correction network learns cross-coupling residuals while keeping all blocks and the aggregator frozen, preserving zero-forgetting modular expansion by construction. We evaluate SCNO on eight PDE families including five coupled systems and a nuclear-relevant 1-group neutron diffusion equation. SCNO with correction achieves the lowest relative $L^2$ error on four of five coupled PDEs, outperforming both a monolithic spiking DeepONet (by up to 62%, mean over 3 seeds) and a standard ANN DeepONet (by up to 65%), while requiring only 95K trainable parameters versus 462K for the monolithic baseline. To our knowledge, this is the first compositional spiking neural operator and the first proof-of-concept for modular neuromorphic PDE solving with built-in forgetting-free expansion.

---


### 260. [POINTS-Long: Adaptive Dual-Mode Visual Reasoning in MLLMs](https://arxiv.org/abs/2604.11627)

**<font color=#1a73e8>作者：</font>** Haicheng Wang, Yuan Liu, Yikun Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have recently demonstrated remarkable capabilities in cross-modal understanding and generation. However, the rapid growth of visual token sequences--especially in long-video and streaming scenarios--poses a major challenge to their scalability and real-world deployment. Thus, we introduce POINTS-Long, a native dual-mode MLLM featuring dynamic visual token scaling inspired by the human visual system. The model supports two complementary perception modes: focus mode and standby mode, enabling users to dynamically trade off efficiency and accuracy during inference. On fine-grained visual tasks, the focus mode retains the optimal performance, while on long-form general visual understanding, the standby mode retains 97.7-99.7% of the original accuracy using only 1/40-1/10th of the visual tokens. Moreover, POINTS-Long natively supports streaming visual understanding via a dynamically detachable KV-cache design, allowing efficient maintenance of ultra-long visual memory. Our work provides new insights into the design of future MLLMs and lays the foundation for adaptive and efficient long-form visual understanding.

---


### 261. [CArtBench: Evaluating Vision-Language Models on Chinese Art Understanding, Interpretation, and Authenticity](https://arxiv.org/abs/2604.11632)

**<font color=#1a73e8>作者：</font>** Xuefeng Wei, Zhixuan Wang, Xuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce CARTBENCH, a museum-grounded benchmark for evaluating vision-language models (VLMs) on Chinese artworks beyond short-form recognition and QA. CARTBENCH comprises four subtasks: CURATORQA for evidence-grounded recognition and reasoning, CATALOGCAPTION for structured four-section expert-style appreciation, REINTERPRET for defensible reinterpretation with expert ratings, and CONNOISSEURPAIRS for diagnostic authenticity discrimination under visually similar confounds. CARTBENCH is built by aligning image-bearing Palace Museum objects from Wikidata with authoritative catalog pages, spanning five art categories across multiple dynasties. Across nine representative VLMs, we find that high overall CURATORQA accuracy can mask sharp drops on hard evidence linking and style-to-period inference; long-form appreciation remains far from expert references; and authenticity-oriented diagnostic discrimination stays near chance, underscoring the difficulty of connoisseur-level reasoning for current models.

---


### 262. [RPA-Check: A Multi-Stage Automated Framework for Evaluating Dynamic LLM-based Role-Playing Agents](https://arxiv.org/abs/2604.11655)

**<font color=#1a73e8>作者：</font>** Riccardo Rosati, Edoardo Colucci, Massimiliano Bolognini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of Large Language Models (LLMs) in interactive systems has enabled the creation of dynamic, open-ended Role-Playing Agents (RPAs). However, evaluating these agents remains a significant challenge, as standard NLP metrics fail to capture the nuances of role adherence, logical consistency, and long-term narrative stability. This paper introduces RPA-Check, a multi-stage automated evaluation framework designed to objectively assess the performance of LLM-based RPAs in complex, constraints-heavy environments. Our methodology is based on a four-step pipeline: (1) Dimension Definition, establishing high-level qualitative behavioral criteria; (2) Augmentation, where these requirements are expanded into granular boolean checklist indicators; (3) Semantic Filtering, to ensure indicator objectivity, no redundancy and agent isolation; and (4) LLM-as-a-Judge Evaluation, which employs chain-of-thought verification to score agent fidelity. We validate this framework by applying it to LLM Court, a serious game for forensic training involving several quantized local models. Experimental results across five distinct legal scenarios demonstrate the framework's ability to identify subtle trade-offs between model size, reasoning depth, and operational stability. Notably, the findings reveal an inverse relationship between parametric scale and procedural consistency, showing that smaller, adequately instruction-tuned models (8-9B) can outperform larger architectures prone to user-alignment bias or sycophancy. RPA-Check thus provides a standardized and reproducible metric for future research in generative agent evaluation within specialized domains.

---


### 263. [Why Do Large Language Models Generate Harmful Content?](https://arxiv.org/abs/2604.11663)

**<font color=#1a73e8>作者：</font>** Rajesh Ganguli, Raha Moraffah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been shown to generate harmful content. However, the underlying causes of such behavior remain under explored. We propose a causal mediation analysis-based approach to identify the causal factors responsible for harmful generation. Our method performs a multi-granular analysis across model layers, modules (MLP and attention blocks), and individual neurons. Extensive experiments on state-of-the-art LLMs indicate that harmful generation arises in the later layers of the model, results primarily from failures in MLP blocks rather than attention blocks, and is associated with neurons that act as a gating mechanism for harmful generation. The results indicate that the early layers in the model are used for a contextual understanding of harmfulness in a prompt, which is then propagated through the model, to generate harmfulness in the late layers, as well as a signal indicating harmfulness through MLP blocks. This is then further propagated to the last layer of the model, specifically to a sparse set of neurons, which receives the signal and determines the generation of harmful content accordingly.

---


### 264. [Playing Along: Learning a Double-Agent Defender for Belief Steering via Theory of Mind](https://arxiv.org/abs/2604.11666)

**<font color=#1a73e8>作者：</font>** Hanqi Xiao, Vaidehi Patil, Zaid Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become the engine behind conversational systems, their ability to reason about the intentions and states of their dialogue partners (i.e., form and use a theory-of-mind, or ToM) becomes increasingly critical for safe interaction with potentially adversarial partners. We propose a novel privacy-themed ToM challenge, ToM for Steering Beliefs (ToM-SB), in which a defender must act as a Double Agent to steer the beliefs of an attacker with partial prior knowledge within a shared universe. To succeed on ToM-SB, the defender must engage with and form a ToM of the attacker, with a goal of fooling the attacker into believing they have succeeded in extracting sensitive information. We find that strong frontier models like Gemini3-Pro and GPT-5.4 struggle on ToM-SB, often failing to fool attackers in hard scenarios with partial attacker prior knowledge, even when prompted to reason about the attacker's beliefs (ToM prompting). To close this gap, we train models on ToM-SB to act as AI Double Agents using reinforcement learning, testing both fooling and ToM rewards. Notably, we find a bidirectionally emergent relationship between ToM and attacker-fooling: rewarding fooling success alone improves ToM, and rewarding ToM alone improves fooling. Across four attackers with different strengths, six defender methods, and both in-distribution and out-of-distribution (OOD) evaluation, we find that gains in ToM and attacker-fooling are well-correlated, highlighting belief modeling as a key driver of success on ToM-SB. AI Double Agents that combine both ToM and fooling rewards yield the strongest fooling and ToM performance, outperforming Gemini3-Pro and GPT-5.4 with ToM prompting on hard scenarios. We also show that ToM-SB and AI Double Agents can be extended to stronger attackers, demonstrating generalization to OOD settings and the upgradability of our task.

---


### 265. [Towards Brain MRI Foundation Models for the Clinic: Findings from the FOMO25 Challenge](https://arxiv.org/abs/2604.11679)

**<font color=#1a73e8>作者：</font>** Asbjørn Munk, Stefano Cerri, Vardan Nersesjan 等 84 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical deployment of automated brain MRI analysis faces a fundamental challenge: clinical data is heterogeneous and noisy, and high-quality labels are prohibitively costly to obtain. Self-supervised learning (SSL) can address this by leveraging the vast amounts of unlabeled data produced in clinical workflows to train robust \textit{foundation models} that adapt out-of-domain with minimal supervision. However, the development of foundation models for brain MRI has been limited by small pretraining datasets and in-domain benchmarking focused on high-quality, research-grade data. To address this gap, we organized the FOMO25 challenge as a satellite event at MICCAI 2025. FOMO25 provided participants with a large pretraining dataset, FOMO60K, and evaluated models on data sourced directly from clinical workflows in few-shot and out-of-domain settings. Tasks covered infarct classification, meningioma segmentation, and brain age regression, and considered both models trained on FOMO60K (method track) and any data (open track). Nineteen foundation models from sixteen teams were evaluated using a standardized containerized pipeline. Results show that (a) self-supervised pretraining improves generalization on clinical data under domain shift, with the strongest models trained \textit{out-of-domain} surpassing supervised baselines trained \textit{in-domain}. (b) No single pretraining objective benefits all tasks: MAE favors segmentation, hybrid reconstruction-contrastive objectives favor classification, and (c) strong performance was achieved by small pretrained models, and improvements from scaling model size and training duration did not yield reliable benefits.

---


### 266. [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://arxiv.org/abs/2604.11689)

**<font color=#1a73e8>作者：</font>** Dujun Nie, Fengjiao Chen, Qi Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the shortage of explicit action data limits Vision-Language-Action (VLA) models, human action videos offer a scalable yet unlabeled data source. A critical challenge in utilizing large-scale human video datasets lies in transforming visual signals into ontology-independent representations, known as latent actions. However, the capacity of latent action representation to derive robust control from visual observations has yet to be rigorously evaluated. We introduce the Latent Action Representation Yielding (LARY) Benchmark, a unified framework for evaluating latent action representations on both high-level semantic actions (what to do) and low-level robotic control (how to do). The comprehensively curated dataset encompasses over one million videos (1,000 hours) spanning 151 action categories, alongside 620K image pairs and 595K motion trajectories across diverse embodiments and environments. Our experiments reveal two crucial insights: (i) General visual foundation models, trained without any action supervision, consistently outperform specialized embodied latent action models. (ii) Latent-based visual space is fundamentally better aligned to physical action space than pixel-based space. These results suggest that general visual representations inherently encode action-relevant knowledge for physical control, and that semantic-level abstraction serves as a fundamentally more effective pathway from vision to action than pixel-level reconstruction.

---


### 267. [Legal2LogicICL: Improving Generalization in Transforming Legal Cases to Logical Formulas via Diverse Few-Shot Learning](https://arxiv.org/abs/2604.11699)

**<font color=#1a73e8>作者：</font>** Jieying Xue, Phuong Minh Nguyen, Ha Thanh Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work aims to improve the generalization of logic-based legal reasoning systems by integrating recent advances in NLP with legal-domain adaptive few-shot learning techniques using LLMs. Existing logic-based legal reasoning pipelines typically rely on fine-tuned models to map natural-language legal cases into logical formulas before forwarding them to a symbolic reasoner. However, such approaches are heavily constrained by the scarcity of high-quality annotated training data. To address this limitation, we propose a novel LLM-based legal reasoning framework that enables effective in-context learning through retrieval-augmented generation. Specifically, we introduce Legal2LogicICL, a few-shot retrieval framework that balances diversity and similarity of exemplars at both the latent semantic representation level and the legal text structure level. In addition, our method explicitly accounts for legal structure by mitigating entity-induced retrieval bias in legal texts, where lengthy and highly specific entity mentions often dominate semantic representations and obscure legally meaningful reasoning patterns. Our Legal2LogicICL constructs informative and robust few-shot demonstrations, leading to accurate and stable logical rule generation without requiring additional training. In addition, we construct a new dataset, named Legal2Proleg, which is annotated with alignments between legal cases and PROLEG logical formulas to support the evaluation of legal semantic parsing. Experimental results on both open-source and proprietary LLMs demonstrate that our approach significantly improves accuracy, stability, and generalization in transforming natural-language legal case descriptions into logical representations, highlighting its effectiveness for interpretable and reliable legal reasoning. Our code is available at this https URL.

---


### 268. [Agentic Driving Coach: Robustness and Determinism of Agentic AI-Powered Human-in-the-Loop Cyber-Physical Systems](https://arxiv.org/abs/2604.11705)

**<font color=#1a73e8>作者：</font>** Deeksha Prahlad, Daniel Fan, Hokeun Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models, including large language models (LLMs), are increasingly used for human-in-the-loop (HITL) cyber-physical systems (CPS) because foundation model-based AI agents can potentially interact with both the physical environments and human users. However, the unpredictable behavior of human users and AI agents, in addition to the dynamically changing physical environments, leads to uncontrollable nondeterminism. To address this urgent challenge of enabling agentic AI-powered HITL CPS, we propose a reactor-model-of-computation (MoC)-based approach, realized by the open-source Lingua Franca (LF) framework. We also carry out a concrete case study using the agentic driving coach as an application of HITL CPS. By evaluating the LF-based agentic HITL CPS, we identify practical challenges in reintroducing determinism into such agentic HITL CPS and present pathways to address them.

---


### 269. [A Mamba-Based Multimodal Network for Multiscale Blast-Induced Rapid Structural Damage Assessment](https://arxiv.org/abs/2604.11709)

**<font color=#1a73e8>作者：</font>** Wanli Ma, Sivasakthy Selvakumaran, Dain G. Farrimond 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate and rapid structural damage assessment (SDA) is crucial for post-disaster management, helping responders prioritise resources, plan rescues, and support recovery. Traditional field inspections, though precise, are limited by accessibility, safety risks, and time constraints, especially after large explosions. Machine learning with remote sensing has emerged as a scalable solution for rapid SDA, with Mamba-based networks achieving state-of-the-art performance. However, these methods often require extensive training and large datasets, limiting real-world applicability. Moreover, they fail to incorporate key physical characteristics of blast loading for SDA. To overcome these challenges, we propose a Mamba-based multimodal network for rapid SDA that integrates multi-scale blast-loading information with optical remote sensing images. Evaluated on the 2020 Beirut explosion, our method significantly improves performance over state-of-the-art approaches. Code is available at: this https URL

---


### 270. [Evaluating Cooperation in LLM Social Groups through Elected Leadership](https://arxiv.org/abs/2604.11721)

**<font color=#1a73e8>作者：</font>** Ryan Faulkner, Anushka Deshpande, David Guzman Piedrahita 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Governing common-pool resources requires agents to develop enduring strategies through cooperation and self-governance to avoid collective failure. While foundation models have shown potential for cooperation in these settings, existing multi-agent research provides little insight into whether structured leadership and election mechanisms can improve collective decision making. The lack of such a critical organizational feature ubiquitous in human society presents a significant shortcoming of the current methods. In this work we aim to directly address whether leadership and elections can support improved social welfare and cooperation through multi-agent simulation with LLMs. We present our open-source framework that simulates leadership through elected personas and candidate-driven agendas and carry out an empirical study of LLMs under controlled governance conditions. Our experiments demonstrate that having elected leadership improves social welfare scores by 55.4% and survival time by 128.6% across a range of high performing LLMs. Through the construction of an agent social graph we compute centrality metrics to assess the social influence of leader personas and also analyze rhetorical and cooperative tendencies revealed through a sentiment analysis on leader utterances. This work lays the foundation for further study of election mechanisms in multi-agent systems toward navigating complex social dilemmas.

---


### 271. [The Devil is in the Details -- From OCR for Old Church Slavonic to Purely Visual Stemma Reconstruction](https://arxiv.org/abs/2604.11724)

**<font color=#1a73e8>作者：</font>** Armin Hoenen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The age of artificial intelligence has brought many new possibilities and pitfalls in many fields and tasks. The devil is in the details, and those come to the fore when building new pipelines and executing small practical experiments. OCR and stemmatology are no exception. The current investigation starts comparing a range of OCR-systems, from classical over machine learning to LLMs, for roughly 6,000 characters of late handwritten church slavonic manuscripts from the 18th century. Focussing on basic letter correctness, more than 10 CS OCR-systems among which 2 LLMs (GPT5 and Gemini3-flash) are being compared. Then, post-processing via LLMs is assessed and finally, different agentic OCR architectures (specialized post-processing agents, an agentic pipeline and RAG) are tested. With new technology elaborated, experiments suggest, church slavonic CER for basic letters may reach as low as 2-3% but elaborated diacritics could still present a problem. How well OCR can prime stemmatology as a downstream task is the entry point to the second part of the article which introduces a new stemmatic method based solely on image processing. Here, a pipeline of automated visual glyph extraction, clustering and pairwise statistical comparison leading to a distance matrix and ultimately a stemma, is being presented and applied to two small corpora, one for the church slavonic Gospel of Mark from the 14th to 16th centuries, one for the Roman de la Rose in French from the 14th and 15th centuries. Basic functioning of the method can be demonstrated.

---


### 272. [Ambivalence/Hesitancy Recognition in Videos for Personalized Digital Health Interventions](https://arxiv.org/abs/2604.11730)

**<font color=#1a73e8>作者：</font>** Manuela González-González, Soufiane Belharbi, Muhammad Osama Zeeshan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using behavioural science, health interventions focus on behaviour change by providing a framework to help patients acquire and maintain healthy habits that improve medical outcomes. In-person interventions are costly and difficult to scale, especially in resource-limited regions. Digital health interventions offer a cost-effective approach, potentially supporting independent living and self-management. Automating such interventions, especially through machine learning, has gained considerable attention recently. Ambivalence and hesitancy (A/H) play a primary role for individuals to delay, avoid, or abandon health interventions. A/H are subtle and conflicting emotions that place a person in a state between positive and negative evaluations of a behaviour, or between acceptance and refusal to engage in it. They manifest as affective inconsistency across modalities or within a modality, such as language, facial, vocal expressions, and body language. While experts can be trained to recognize A/H, integrating them into digital health interventions is costly and less effective. Automatic A/H recognition is therefore critical for the personalization and cost-effectiveness of digital health interventions. Here, we explore the application of deep learning models for A/H recognition in videos, a multi-modal task by nature. In particular, this paper covers three learning setups: supervised learning, unsupervised domain adaptation for personalization, and zero-shot inference via large language models (LLMs). Our experiments are conducted on the unique and recently published BAH video dataset for A/H recognition. Our results show limited performance, suggesting that more adapted multi-modal models are required for accurate A/H recognition. Better methods for modeling spatio-temporal and multimodal fusion are necessary to leverage conflicts within/across modalities.

---


### 273. [Collaborative Multi-Agent Scripts Generation for Enhancing Imperfect-Information Reasoning in Murder Mystery Games](https://arxiv.org/abs/2604.11741)

**<font color=#1a73e8>作者：</font>** Keyang Zhong, Junlin Xie, Hefeng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown impressive capabilities in perceptual tasks, yet they degrade in complex multi-hop reasoning under multiplayer game settings with imperfect and deceptive information. In this paper, we study a representative multiplayer task, Murder Mystery Games, which require inferring hidden truths based on partial clues provided by roles with different intentions. To address this challenge, we propose a collaborative multi-agent framework for evaluating and synthesizing high-quality, role-driven multiplayer game scripts, enabling fine-grained interaction patterns tailored to character identities (i.e., murderer vs. innocent). Our system generates rich multimodal contexts, including character backstories, visual and textual clues, and multi-hop reasoning chains, through coordinated agent interactions. We design a two-stage agent-monitored training strategy to enhance the reasoning ability of VLMs: (1) chain-of-thought based fine-tuning on curated and synthetic datasets that model uncertainty and deception; (2) GRPO-based reinforcement learning with agent-monitored reward shaping, encouraging the model to develop character-specific reasoning behaviors and effective multimodal multi-hop inference. Extensive experiments demonstrate that our method significantly boosts the performance of VLMs in narrative reasoning, hidden fact extraction, and deception-resilient understanding. Our contributions offer a scalable solution for training and evaluating VLMs under uncertain, adversarial, and socially complex conditions, laying the groundwork for future benchmarks in multimodal multi-hop reasoning under imperfect information.

---


### 274. [LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling](https://arxiv.org/abs/2604.11748)

**<font color=#1a73e8>作者：</font>** Yuxin Chen, Chumeng Liang, Hangke Sui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion models have achieved strong performance across domains such as images. However, in language modeling, prior continuous diffusion language models (DLMs) lag behind discrete counterparts. In this work, we close this gap with LangFlow, the first continuous DLM to rival discrete diffusion. Our approach connects embedding-space DLMs to Flow Matching via Bregman divergence and introduces three key innovations: (1) a novel ODE-based NLL bound for principled evaluation of continuous flow-based language models; (2) an information-uniform principle for noise scheduling, motivating a learnable scheduler based on a Gumbel distribution; and (3) an improved training protocol incorporating self-conditioning, which enhances both likelihood and sample this http URL achieves strong performance across benchmarks, reaching a perplexity (PPL) of 30.0 on LM1B and 24.6 on OpenWebText. It matches top discrete DLMs at comparable scale and surpasses autoregressive baselines in zero-shot transfer across multiple benchmarks. LangFlow provides clear evidence that continuous diffusion is a competitive and promising paradigm for language modeling.
this https URL

---


### 275. [Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks](https://arxiv.org/abs/2604.11753)

**<font color=#1a73e8>作者：</font>** Yoonsang Lee, Howard Yen, Xi Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study parallel test-time scaling for long-horizon agentic tasks such as agentic search and deep research, where multiple rollouts are generated in parallel and aggregated into a final response. While such scaling has proven effective for chain-of-thought reasoning, agentic tasks pose unique challenges: trajectories are long, multi-turn, and tool-augmented, and outputs are often open-ended. Aggregating only final answers discards rich information from trajectories, while concatenating all trajectories exceeds the model's context window. To address this, we propose AggAgent, an aggregation agent that treats parallel trajectories as an environment. We equip it with lightweight tools to inspect candidate solutions and search across trajectories, enabling it to navigate and synthesize information on demand. Across six benchmarks and three model families (GLM-4.7, Qwen3.5, MiniMax-M2.5), AggAgent outperforms all existing aggregation methods-by up to 5.3% absolute on average and 10.3% on two deep research tasks-while adding minimal overhead, as the aggregation cost remains bounded by a single agentic rollout. Our findings establish agentic aggregation as an effective and cost-efficient approach to parallel test-time scaling.

---


### 276. [General365: Benchmarking General Reasoning in Large Language Models Across Diverse and Challenging Tasks](https://arxiv.org/abs/2604.11778)

**<font color=#1a73e8>作者：</font>** Junlin Liu, Shengnan An, Shuang Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contemporary large language models (LLMs) have demonstrated remarkable reasoning capabilities, particularly in specialized domains like mathematics and physics. However, their ability to generalize these reasoning skills to more general and broader contexts--often termed general reasoning--remains under-explored. Unlike domain-specific reasoning, general reasoning relies less on expert knowledge but still presents formidable reasoning challenges, such as complex constraints, nested logical branches, and semantic interference. To address this gap, we introduce General365, a benchmark specifically designed to assess general reasoning in LLMs. By restricting background knowledge to a K-12 level, General365 explicitly decouples reasoning from specialized expertise. The benchmark comprises 365 seed problems and 1,095 variant problems across eight categories, ensuring both high difficulty and diversity. Evaluations across 26 leading LLMs reveal that even the top-performing model achieves only 62.8% accuracy, in stark contrast to the near-perfect performances of LLMs in math and physics benchmarks. These results suggest that the reasoning abilities of current LLMs are heavily domain-dependent, leaving significant room for improvement in broader applications. We envision General365 as a catalyst for advancing LLM reasoning beyond domain-specific tasks toward robust, general-purpose real-world scenarios. Code, Dataset, and Leaderboard: this https URL

---


### 277. [HDR Video Generation via Latent Alignment with Logarithmic Encoding](https://arxiv.org/abs/2604.11788)

**<font color=#1a73e8>作者：</font>** Naomi Ken Korem, Mohamed Oumoumad, Harel Cain 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High dynamic range (HDR) imagery offers a rich and faithful representation of scene radiance, but remains challenging for generative models due to its mismatch with the bounded, perceptually compressed data on which these models are trained. A natural solution is to learn new representations for HDR, which introduces additional complexity and data requirements. In this work, we show that HDR generation can be achieved in a much simpler way by leveraging the strong visual priors already captured by pretrained generative models. We observe that a logarithmic encoding widely used in cinematic pipelines maps HDR imagery into a distribution that is naturally aligned with the latent space of these models, enabling direct adaptation via lightweight fine-tuning without retraining an encoder. To recover details that are not directly observable in the input, we further introduce a training strategy based on camera-mimicking degradations that encourages the model to infer missing high dynamic range content from its learned priors. Combining these insights, we demonstrate high-quality HDR video generation using a pretrained video model with minimal adaptation, achieving strong results across diverse scenes and challenging lighting conditions. Our results indicate that HDR, despite representing a fundamentally different image formation regime, can be handled effectively without redesigning generative models, provided that the representation is chosen to align with their learned priors.

---


### 278. [A Mechanistic Analysis of Looped Reasoning Language Models](https://arxiv.org/abs/2604.11791)

**<font color=#1a73e8>作者：</font>** Hugh Blayney, Álvaro Arroyo, Johan Obando-Ceron 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning has become a central capability in large language models. Recent research has shown that reasoning performance can be improved by looping an LLM's layers in the latent dimension, resulting in looped reasoning language models. Despite promising results, few works have investigated how their internal dynamics differ from those of standard feedforward models. In this paper, we conduct a mechanistic analysis of the latent states in looped language models, focusing in particular on how the stages of inference observed in feedforward models compare to those observed in looped ones. To this end, we analyze cyclic recurrence and show that for many of the studied models each layer in the cycle converges to a distinct fixed point; consequently, the recurrent block follows a consistent cyclic trajectory in the latent space. We provide evidence that as these fixed points are reached, attention-head behavior stabilizes, leading to constant behavior across recurrences. Empirically, we discover that recurrent blocks learn stages of inference that closely mirror those of feedforward models, repeating these stages in depth with each iteration. We study how recurrent block size, input injection, and normalization influence the emergence and stability of these cyclic fixed points. We believe these findings help translate mechanistic insights into practical guidance for architectural design.

---


### 279. [LottieGPT: Tokenizing Vector Animation for Autoregressive Generation](https://arxiv.org/abs/2604.11792)

**<font color=#1a73e8>作者：</font>** Junhao Chen, Kejun Gao, Yuehan Cui 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in video generation, existing models are incapable of producing vector animation, a dominant and highly expressive form of multimedia on the Internet. Vector animations offer resolution-independence, compactness, semantic structure, and editable parametric motion representations, yet current generative models operate exclusively in raster space and thus cannot synthesize them. Meanwhile, recent advances in large multimodal models demonstrate strong capabilities in generating structured data such as slides, 3D meshes, LEGO sequences, and indoor layouts, suggesting that native vector animation generation may be achievable. In this work, we present the first framework for tokenizing and autoregressively generating vector animations. We adopt Lottie, a widely deployed JSON-based animation standard, and design a tailored Lottie Tokenizer that encodes layered geometric primitives, transforms, and keyframe-based motion into a compact and semantically aligned token sequence. To support large-scale training, we also construct LottieAnimation-660K, the largest and most diverse vector animation dataset to date, consisting of 660k real-world Lottie animation and 15M static Lottie image files curated from broad Internet sources. Building upon these components, we finetune Qwen-VL to create LottieGPT, a native multimodal model capable of generating coherent, editable vector animations directly from natural language or visual prompts. Experiments show that our tokenizer dramatically reduces sequence length while preserving structural fidelity, enabling effective autoregressive learning of dynamic vector content. LottieGPT exhibits strong generalization across diverse animation styles and outperforms previous state-of-the-art models on SVG generation (a special case of single-frame vector animation).

---


### 280. [C-ReD: A Comprehensive Chinese Benchmark for AI-Generated Text Detection Derived from Real-World Prompts](https://arxiv.org/abs/2604.11796)

**<font color=#1a73e8>作者：</font>** Chenxi Qing, Junxi Wu, Zheng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, large language models (LLMs) are capable of generating highly fluent textual content. While they offer significant convenience to humans, they also introduce various risks, like phishing and academic dishonesty. Numerous research efforts have been dedicated to developing algorithms for detecting AI-generated text and constructing relevant datasets. However, in the domain of Chinese corpora, challenges remain, including limited model diversity and data homogeneity. To address these issues, we propose C-ReD: a comprehensive Chinese Real-prompt AI-generated Detection benchmark. Experiments demonstrate that C-ReD not only enables reliable in-domain detection but also supports strong generalization to unseen LLMs and external Chinese datasets-addressing critical gaps in model diversity, domain coverage, and prompt realism that have limited prior Chinese detection benchmarks. We release our resources at this https URL.

---


### 281. [CLSGen: A Dual-Head Fine-Tuning Framework for Joint Probabilistic Classification and Verbalized Explanation](https://arxiv.org/abs/2604.11801)

**<font color=#1a73e8>作者：</font>** WonJin Yoon, Kangyu Zhu, Ian Bulovic 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the recent progress of Large Language Models (LLMs), there is a growing interest in applying these models to solve complex and challenging problems. Modern LLMs, capable of processing long contexts and generating verbalized explanations, offer significant potential in addressing real-world applications. However, a critical hurdle in deploying LLMs for practical decision-making is their inability to provide reliable, quantitative probabilities. While task-specific fine-tuning of LLMs using traditional discriminative objectives (similar to encoder-only models) can yield probability estimates, this often leads to catastrophic forgetting and linguistic collapse. Consequently, the model loses its ability to generate explanations, severely undermining its interpretability and usability. To address this challenge, we propose CLSGen, a novel LLM fine-tuning framework designed for binary classification tasks. The CLSGen framework encompasses a new model architecture, training methodology, and data construction strategy to enable robust probability estimation without sacrificing the model's inherent explanation-generation capabilities. Experimental results across multiple benchmark datasets demonstrate that models fine-tuned with CLSGen outperform existing baselines in classification metrics (AUROC and F1-score). Regarding explanation, the results showed strong alignment between predicted labels and generated justifications, as well as high readability.

---


### 282. [Psychological Concept Neurons: Can Neural Control Bias Probing and Shift Generation in LLMs?](https://arxiv.org/abs/2604.11802)

**<font color=#1a73e8>作者：</font>** Yuto Harada, Hiro Taiyo Hamada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Using psychological constructs such as the Big Five, large language models (LLMs) can imitate specific personality profiles and predict a user's personality. While LLMs can exhibit behaviors consistent with these constructs, it remains unclear where and how they are represented inside the model and how they relate to behavioral outputs. To address this gap, we focus on questionnaire-operationalized Big Five concepts, analyze the formation and localization of their internal representations, and use interventions to examine how these representations relate to behavioral outputs. In our experiment, we first use probing to examine where Big Five information emerges across model depth. We then identify neurons that respond selectively to each Big Five concept and test whether enhancing or suppressing their activations can bias latent representations and label generation in intended directions. We find that Big Five information becomes rapidly decodable in early layers and remains detectable through the final layers, while concept-selective neurons are most prevalent in mid layers and exhibit limited overlap across domains. Interventions on these neurons consistently shift probe readouts toward targeted concepts, with targeted success rates exceeding 0.8 for some concepts, indicating that the model's internal separation of Big Five personality traits can be causally steered. At the label-generation level, the same interventions often bias generated label distributions in the intended directions, but the effects are weaker, more concept-dependent, and often accompanied by cross-trait spillover, indicating that comparable control over generated labels is difficult even with interventions on a large fraction of concept-selective neurons. Overall, our findings reveal a gap between representational control and behavioral control in LLMs.

---


### 283. [OmniShow: Unifying Multimodal Conditions for Human-Object Interaction Video Generation](https://arxiv.org/abs/2604.11804)

**<font color=#1a73e8>作者：</font>** Donghao Zhou, Guisheng Liu, Hao Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we study Human-Object Interaction Video Generation (HOIVG), which aims to synthesize high-quality human-object interaction videos conditioned on text, reference images, audio, and pose. This task holds significant practical value for automating content creation in real-world applications, such as e-commerce demonstrations, short video production, and interactive entertainment. However, existing approaches fail to accommodate all these requisite conditions. We present OmniShow, an end-to-end framework tailored for this practical yet challenging task, capable of harmonizing multimodal conditions and delivering industry-grade performance. To overcome the trade-off between controllability and quality, we introduce Unified Channel-wise Conditioning for efficient image and pose injection, and Gated Local-Context Attention to ensure precise audio-visual synchronization. To effectively address data scarcity, we develop a Decoupled-Then-Joint Training strategy that leverages a multi-stage training process with model merging to efficiently harness heterogeneous sub-task datasets. Furthermore, to fill the evaluation gap in this field, we establish HOIVG-Bench, a dedicated and comprehensive benchmark for HOIVG. Extensive experiments demonstrate that OmniShow achieves overall state-of-the-art performance across various multimodal conditioning settings, setting a solid standard for the emerging HOIVG task.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
