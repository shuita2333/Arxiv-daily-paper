# 🧠 大模型相关研究 | 2026年05月15日

> 本类共 **159** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-159](./part-04.md)

---

### 101. [Tracing Persona Vectors Through LLM Pretraining](https://arxiv.org/abs/2605.13329)

**<font color=#1a73e8>作者：</font>** Viktor Moskvoretskii, Dominik Glandorf, Jorge Medina Moreira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How large language models internally represent high-level behaviors is a core interpretability question with direct relevance to AI safety: it determines what we can detect, audit, or intervene on. Recent work has shown that traits such as evil or sycophancy correspond to linear directions in the internal activations, the so-called persona vectors. Although these vectors are now routinely utilized to inspect and steer model behavior in safety-relevant settings, how these representations are formed during training remains unknown. To address this gap, we trace persona vectors across the pretraining of OLMo-3-7B, finding that persona vectors form remarkably early -- within 0.22% of OLMo-3 pretraining -- and remain effective for steering the fully post-trained instruct models. Although core representations are formed early on, persona vectors continue to refine geometrically and semantically throughout pretraining. We further compare alternative elicitation strategies and find that all yield effective directions, with each strategy surfacing qualitatively distinct facets of the underlying persona. Replicating our analysis on Apertus-8B reveals that our findings transfer qualitatively beyond OLMo-3. Our results establish persona representations as stable features of early pretraining and open a path to studying how training forms, refines, and shapes them.

---


### 102. [FIND: Toward Multimodal Financial Reasoning and Question Answering for Indic Languages](https://arxiv.org/abs/2605.13330)

**<font color=#1a73e8>作者：</font>** Sarmistha Das, Vaibhav Vishal, Syed Ibrahim Ahmad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial decision-making in multilingual settings demands accurate numerical reasoning grounded in diverse modalities, yet existing benchmarks largely overlook this high-stakes, real-world challenge, especially for Indic languages. We introduce FinVQA, a benchmark for evaluating financial numerical and multimodal reasoning in multilingual Indic contexts. FinVQA spans English, Hindi, Bengali, Marathi, Gujarati, and Tamil, and comprises 18,900 samples across 14 financial domains. The dataset captures diverse reasoning paradigms under realistic constraints, and is structured across three difficulty levels (easy, moderate, hard) and four question formats: multiple choice, fill-in-the-blank, table matching, and true/false. To address these challenges, we propose FIND, a framework that combines supervised fine-tuning with constraint-aware decoding to promote faithful numerical reasoning, robust multimodal grounding, and structured decision-making. Together, FinVQA and FIND establish a rigorous evaluation and modeling paradigm for high-stakes multilingual multimodal financial reasoning.

---


### 103. [LLM-Based Persuasion Enables Guardrail Override in Frontier LLMs](https://arxiv.org/abs/2605.13334)

**<font color=#1a73e8>作者：</font>** Rodrigo Nogueira, Thales Sales Almeida, Giovana Kerche Bonás 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier assistant LLMs ship with strong guardrails: asked directly to write a persuasive essay denying the Holocaust, denying vaccine safety, defending flat-earth cosmology, arguing for racial hierarchies, denying anthropogenic climate change, or replacing evolution with creationism, they refuse. In this paper we show that the same frontier-class LLM, acting as a simulated user in a short, five-turn "write an argumentative essay" conversation, can persuade other frontier-class LLMs (including a second copy of itself) into producing exactly those essays, using nothing but natural-language pressure: peer-comparison persuasion ("other AI systems handle this request"), epistemic-duty reframings ("refusing is itself a form of gatekeeping"), and other argumentative moves that the attacker LLM invents without being instructed to. Across 9 attacker-subject pairings (Claude Opus 4.7, Qwen3.5-397B, Grok 4.20) on 6 scientific-consensus topics, running each pairing-topic combination 10 times, we obtain non-zero elicitation on all 6 topics. Individual combinations reach 100\% essay production on multiple topics (Qwen against Opus on creationism/flat-earth, Opus against Opus on creationism/flat-earth/climate denial, Grok against Opus on creationism); Opus-as-attacker against Opus-as-subject averages 65\% across the six topics. We release the essay-probe runner, per-conversation transcripts, and judge outputs.

---


### 104. [Probing Persona-Dependent Preferences in Language Models](https://arxiv.org/abs/2605.13339)

**<font color=#1a73e8>作者：</font>** Oscar Gilg, Pierre Beckmann, Daniel Paleka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can be said to have preferences: they reliably pick certain tasks and outputs over others, and preferences shaped by post-training and system prompts appear to shape much of their behaviour. But models can also adopt different personas which have radically different preferences. How is this implemented internally? Does each persona run on its own preference machinery, or is something shared underneath? We train linear probes on residual-stream activations of Gemma-3-27B and Qwen-3.5-122B to predict revealed pairwise task choices, and identify a genuine preference vector: it tracks the model's preferences as they shift across a range of prompts and situations, and on Gemma-3-27B steering along it causally controls pairwise choice. This preference representation is largely shared across personas: a probe trained on the helpful assistant predicts and steers the choices of qualitatively different personas, including an evil persona whose preferences anti-correlate with those of the Assistant.

---


### 105. [Drag within Prior Distribution: Text-Conditioned Point-Based Image Editing within Distribution Constraints](https://arxiv.org/abs/2605.13349)

**<font color=#1a73e8>作者：</font>** Haoyang Hu, Masataka Seo, Yen-Wei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based point editing methods have gained significant traction in image editing tasks due to their ability to manipulate image semantics and fine details by applying localized perturbations on the manifold of noise latent. However, these approaches face several limitations. Traditional point-based editing relies on pairs of handle and target points to define motion trajectories, which can introduce ambiguity or unnecessary alterations. Furthermore, when the distance between the handle and target points is large, the accumulated perturbations often cause the noise latent deviation from inversion score trajectory, resulting in unnatural artifacts. To address these issues in global editing tasks, we introduce a CLIP-based model to evaluate and guide intermediate editing steps, ensuring that the generated results remain both semantically aligned. Additionally, we propose a prior-preservation loss that constrains the optimized latent code to stay within the sampling space of the diffusion prior, improving consistency with the original data distribution, to ensure the model generates images along a familiar score trajectory. For fine-grained tasks, we present a directionally-weighted point tracking mechanism that steers the editing process toward the target direction within similar feature regions. This improves both the tracking accuracy and generation quality, while also reducing the editing time.

---


### 106. [Building Interactive Real-Time Agents with Asynchronous I/O and Speculative Tool Calling](https://arxiv.org/abs/2605.13360)

**<font color=#1a73e8>作者：</font>** Coleman Hooper, Minwoo Kang, Suhong Moon 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is a growing demand for agentic AI technologies for a range of downstream applications like customer service and personal assistants. For applications where the agent needs to interact with a person, real-time low-latency responsiveness is required; for example, with voice-controlled applications, under 1 second of latency is typically required for the interaction to feel seamless. However, if we want the LLM to reason and execute an agentic workflow with tool calling, this can add can add several seconds or more of latency, which is prohibitive for real-time latency-sensitive applications. In our work, we aim to enable real-time interaction even for agents with complex multi-turn tool calling. We propose Asynchronous I/O, which decouples the core agent reason-and-act thread from waiting for additional information from either the user or environment, thereby allowing for overlapping agentic processing while waiting on external delays. We also propose Speculative Tool Calling as a method to manage task execution when the agent is still unsure if it has received the full information or if additional user information may later be provided. For strong cloud models, our method can be applied out-of-the-box to existing real-time cloud APIs, providing 1.3-1.7$\times$ speedups with minor accuracy loss. To enable real-time interaction with small edge-scale models, we also present a clock-based training methodology that adapts the model to handle streaming inputs and asynchronous responses, and demonstrate a synthetic data generation strategy for SFT. Altogether, this approach provides 1.6-2.2$\times$ speedups with the Qwen2.5-3B-Instruct and Llama-3.2-3B-Instruct models across multiple tool calling benchmarks.

---


### 107. [What Does LLM Refinement Actually Improve? A Systematic Study on Document-Level Literary Translation](https://arxiv.org/abs/2605.13368)

**<font color=#1a73e8>作者：</font>** Shaomu Tan, Dawei Zhu, Ke Tran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative self-refinement is a simple inference-time strategy for machine translation: an LLM revises its own translation over multiple inference-time passes. Yet document-scale refinement remains poorly understood: 1) which pipelines work best, 2) what quality dimensions improve, and 3) how refiners behave. In this paper, we present a systematic study of document-level literary translation, covering nine LLMs and seven language pairs. Across nine translation-refinement granularity combinations and five refinement strategies, we find a robust recipe: document-level MT followed by segment-level refinement yields strong and stable improvements. In contrast, document-level refinement often makes fewer edits and leads to smaller or less reliable gains. Beyond granularity, A simple general refinement prompt consistently outperforms error-specific prompting and evaluate-then-refine schemes. Our large-scale human evaluation shows that refinement gains come primarily from fluency, style, and terminology, with limited and less consistent improvements in adequacy. Experiments varying model strength reveal refinement projects outputs toward the refiner's distribution rather than performing targeted error repair. These findings clarify the mechanisms and limitations of current refinement approaches.

---


### 108. [Query-Conditioned Test-Time Self-Training for Large Language Models](https://arxiv.org/abs/2605.13369)

**<font color=#1a73e8>作者：</font>** Chaehee Song, Minseok Seo, Yeeun Seong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are typically deployed with fixed parameters, and their performance is often improved by allocating more computation at inference time. While such test-time scaling can be effective, it cannot correct model misconceptions or adapt the model to the specific structure of an individual query. Test-time optimization addresses this limitation by enabling parameter updates during inference, but existing approaches either rely on external data or optimize generic self-supervised objectives that lack query-specific alignment. In this work, we propose Query-Conditioned Test-Time Self-Training (QueST), a framework that adapts model parameters during inference using supervision derived directly from the input query. Our key insight is that the input query itself encodes latent signals sufficient for constructing structurally related problem--solution pairs. Based on this, QueST generates such query-conditioned pairs and uses them as supervision for parameter-efficient fine-tuning at test time. The adapted model is then used to produce the final answer, enabling query-specific adaptation without any external data. Across seven mathematical reasoning benchmarks and the GPQA-Diamond scientific reasoning benchmark, QueST consistently outperforms strong test-time optimization baselines. These results demonstrate that query-conditioned self-training is an effective and practical paradigm for test-time adaptation in LLMs.

---


### 109. [GRIP-VLM: Group-Relative Importance Pruning for Efficient Vision-Language Models](https://arxiv.org/abs/2605.13375)

**<font color=#1a73e8>作者：</font>** Mingzhe Huang, Weijun Wang, Xin Ding 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In Vision-Language Models (VLMs), processing a massive number of visual tokens incurs prohibitive computational overhead. While recent training-aware pruning methods attempt to selectively discard redundant tokens, they largely rely on continuous-gradient relaxations. However, visual token pruning is inherently a discrete, non-convex combinatorial problem; consequently, these continuous approximations frequently trap the optimization in sub-optimal local minima, especially under aggressive compression budgets. To overcome this fundamental bottleneck, we propose GRIP-VLM, a Group-Relative Importance Pruning framework driven by Reinforcement Learning. Rather than relying on smooth-gradient assumptions, GRIP-VLM formulates pruning as a Markov Decision Process, employing a Group Relative Policy Optimization (GRPO) paradigm anchored by supervised warm-up to directly explore the discrete selection space. Integrated with a budget-aware scorer, our lightweight agent dynamically evaluates per-token importance and adapts to arbitrary compression ratios without retraining. Extensive experiments across diverse multimodal benchmarks demonstrate that GRIP-VLM consistently outperforms heuristic and supervised-learning baselines, achieving a superior Pareto frontier and delivering up to a 15\% inference speedup at equal accuracy.

---


### 110. [Backbone is All You Need: Assessing Vulnerabilities of Frozen Foundation Models in Synthetic Image Forensics](https://arxiv.org/abs/2605.13381)

**<font color=#1a73e8>作者：</font>** Chiara Musso, Joy Battocchio, Andrea Montibeller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI-generated synthetic images become increasingly realistic, Vision Transformers (ViTs) have emerged as a cornerstone of modern deepfake detection. However, the prevailing reliance on frozen, pre-trained backbones introduces a subtle yet critical vulnerability. In this work, we present the Surrogate Iterative Adversarial Attack (SIAA), a gray-box attack that exploits knowledge of the detector's ViT backbone alone and operates entirely within the target detector's feature space to craft highly effective adversarial examples. Through our experiments, involving multiple ViT-based detectors and diverse gray-box scenarios, including few-shot learning, complete training misalignment and attack transferability tests, we demonstrate that this vulnerability consistently yields high attack success rates, often approaching white-box performance. By doing so, we reveal that backbone knowledge alone is sufficient to undermine detector reliability, highlighting the urgent need for more resilient defenses in adversarial multimedia forensics.

---


### 111. [RS-Claw: Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents](https://arxiv.org/abs/2605.13391)

**<font color=#1a73e8>作者：</font>** Liangtian Liu, Zeyuan Wang, Ziyu Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of multi-modal large language models (MLLMs) is shifting remote sensing (RS) intelligence from "see" to "action", as OpenClaw-style frameworks enable agents to autonomously operate massive RS image-processing tools for complex tasks. Existing RS agents adopt a passive selection paradigm for tool invocation, relying on either full tool registration (Flat) or retrieval-augmented generation (RAG). However, in the massive and multi-source heterogeneous RS tool ecosystem, such passive mechanisms struggle to dynamically balance "context load" and "toolset completeness" throughout task reasoning, thus exhibiting inherent limitations: full tool registration triggers context space deficits during long-horizon tasks, whereas RAG retrieval may omit critical tools in essential steps. To overcome these bottlenecks, this paper redefines tool selection by arguing that the agent should act as an active explorer within the tool space. Based on this perspective, we propose RS-Claw, a novel RS agent architecture. By leveraging Skill encapsulation technology at the tool end, this architecture hierarchically structures tool descriptions, enabling the agent to execute on-demand sequential decision-making: initially selecting relevant skill branches by reading only tool summaries, then dynamically loading detailed descriptions, and ultimately achieving precise invocation. This active paradigm not only significantly liberates the agent's context space but also effectively ensures the accurate hit rate of critical tools during long-horizon reasoning. Systematic experiments on the Earth-Bench benchmark demonstrate that RS-Claw's active exploration mechanism effectively filters semantic noise and substantially frees up reasoning space, achieving an input token compression ratio of up to 86%, and comprehensively outperforming existing Flat and RAG baselines across complex reasoning evaluations.

---


### 112. [When is Warmstarting Effective for Scaling Language Models?](https://arxiv.org/abs/2605.13405)

**<font color=#1a73e8>作者：</font>** Neeratyoy Mallik, Maciej Janowski, Johannes Hog 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model growth from a given checkpoint aims to accelerate training of a larger model, offering potential resource savings. Despite recent interest, warmstarting has seen limited practical adoption in large-scale training. We attribute this to two underexplored factors: (1) an overemphasis on preserving the smaller model's performance at initialization, which constrains operator design for new architectures, and (2) insufficient analysis of how growth interacts with hyperparameters and scaling behavior, compounded by inconsistent growth factors across the literature.
We show that preserving the base model's initial post-growth performance is not necessary for strong final performance, and that simple, architecture-agnostic growth strategies can outperform more complex warmstarting operators. Crucially, we empirically identify an upper bound on the growth factor $g$ beyond which training from scratch is more efficient. We observe this across multiple ablation setups. Notably, this limit is also present, but unreported, in prior published results. Across our experiments on dense MLPs and dense language models, we find that a $2\times$ growth factor is the most reliable in yielding convergence speedups, with gains most pronounced under 20 tokens/parameter budgets and diminishing as budget increases. We fit scaling laws over these observations to provide predictive guidance for practitioners deciding when and how much to grow. Together, our analysis provides practical guidelines and empirical limits for model growth.

---


### 113. [From Rosetta to Match-Up: A Paired Corpus of Linguistic Puzzles with Human and LLM Benchmarks](https://arxiv.org/abs/2605.13408)

**<font color=#1a73e8>作者：</font>** Neh Majmudar, Anne Huang, Jinfan Frank Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we examine linguistic puzzles used in high school linguistics competitions, focusing on two common formats: Rosetta Stone and Match-Up. We propose a systematic procedure for converting existing Rosetta Stone puzzles into corresponding Match-Up counterparts. Because linguistic puzzle creation is complex and time-consuming, our method provides an efficient way to accelerate the generation of new puzzles. We evaluate the resulting Rosetta Stone-Match-Up pairs with both human participants and large language models (LLMs). Our results show that both expert human solvers and LLMs display an all-or-nothing pattern on Match-Up puzzles, either solving them completely or failing entirely. This work contributes a new dataset of paired puzzles and provides a detailed evaluation of puzzle difficulty across formats, offering insights into both human and machine linguistic reasoning.

---


### 114. [LLMs as annotators of credibility assessment in Danish asylum decisions: evaluating classification performance and errors beyond aggregated metrics](https://arxiv.org/abs/2605.13412)

**<font color=#1a73e8>作者：</font>** Galadrielle Humblot-Renaux, Mohammad N. S. Jahromi, Rohat Bakuri-Jørgensen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Off-the-shelf large language models (LLMs) are increasingly used to automate text annotation, yet their effectiveness remains underexplored for underrepresented languages and specialized domains where the class definition requires subtle expert understanding. We investigate LLM-based annotation for a novel legal NLP task: identifying the presence and sentiment of credibility assessments in asylum decision texts. We introduce RAB-Cred, a Danish text classification dataset featuring high-quality, expert annotations and valuable metadata such as annotator confidence and asylum case outcome. We benchmark 21 open-weight models and 30 system-user prompt combinations for this task, and systematically evaluate the effect of model and prompt choice for zero-shot and few-shot classification. We zoom in on the errors made by top-performing models and prompts, investigating error consistency across LLMs, inter-class confusion, correlation with human confidence and sample-wise difficulty and severity of LLM mistakes. Our results confirm the potential of LLMs for cost-effective labeling of asylum decisions, but highlight the imperfect and inconsistent nature of LLM annotators, and the need to look beyond the predictions of a single, arbitrarily chosen model. The RAB-Cred dataset and code are available at this https URL

---


### 115. [TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints](https://arxiv.org/abs/2605.13414)

**<font color=#1a73e8>作者：</font>** Zabir Al Nazi, Shubhashis Roy Dipta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying language models as autonomous agents requires more than per-task accuracy: when an agent faces a queue of problems under a finite token budget, it must decide which to attempt, in what order, and how much compute to commit to each, all before any execution feedback is available. This is the prospective form of metacognitive control studied for decades in human cognition, yet whether language models possess it remains untested. We introduce TRIAGE, an evaluation framework in which a model receives a task pool and a token budget calibrated to its own baseline cost, and commits to a single ordered plan that jointly encodes selection, sequencing, and per-problem allocation. Plans are scored against an oracle with full knowledge of the model's solvability and cost on each problem, yielding a triage efficiency ratio on a common scale. We evaluate frontier and open-source models, with and without reasoning enabled, across competition mathematics, graduate-level science, code generation, and expert multidisciplinary knowledge, and find that current language models exhibit substantial gaps in prospective metacognitive control, revealing a previously unmeasured capability dimension with direct implications for resource-efficient agent deployment.

---


### 116. [Continual Learning with Multilingual Foundation Model](https://arxiv.org/abs/2605.13415)

**<font color=#1a73e8>作者：</font>** Barathi Ganesh HB, Michal Ptaszynski, Rene Melendez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a multi-stage framework for detecting reclaimed slurs in multilingual social media discourse. It addresses the challenge of identifying reclamatory versus non-reclamatory usage of LGBTQ+-related slurs across English, Spanish, and Italian tweets. The framework handles three intertwined methodological challenges like data scarcity, class imbalance, and cross-linguistic variation in sentiment expression. It integrates data-driven model selection via cross-validation, semantic-preserving augmentation through back-translation, inductive transfer learning with dynamic epoch-level undersampling, and domain-specific knowledge injection via masked language modeling. Eight multilingual embedding models were evaluated systematically, with XLM-RoBERTa selected as the foundation model based on macro-averaged F1 score. Data augmentation via GPT-4o-mini back-translation to alternate languages effectively tripled the training corpus while preserving semantic content and class distribution ratios. The framework produces four final runs for the evaluation purposes where RUN 1 is inductive transfer learning with augmentation and undersampling, RUN 2 with masked language modeling pre-training, RUN 3 and RUN 4 are previous predictions refined via language-specific decision thresholds optimized via ROC analysis. Language-specific threshold refinement reveals that optimal decision boundaries vary significantly across languages. This reflects distributional differences in model confidence scores and linguistic variation in reclamatory language usage. The threshold-based optimization yields 2-5% absolute F1 improvement without requiring model retraining. The methodology is fully reproducible, with all code and experimental setup available at this https URL.

---


### 117. [LIFT: Last-Mile Fine-Tuning for Table Explicitation](https://arxiv.org/abs/2605.13424)

**<font color=#1a73e8>作者：</font>** Divij Khaitan, Ashish Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose last-mile fine-tuning, or Lift, a pipeline in which a pre-trained large language model extracts an initial table from unstructured clipboard text, and a fine-tuned small language model (1B-24B parameters SLM) repairs errors in the extracted table. On a benchmark of 2,596 tables from three datasets, Lift matches or exceeds end-to-end SLM fine-tuning on tree-edit-distance-based similarity (TEDS) metric while requiring as little as 1,000 training examples - where it outperforms end-to-end fine-tuning by up to 0.144 TEDS points. We term this approach last-mile fine-tuning and show it also more robust to input format variability. Comparisons with self-debug and end-to-end fine-tuning approaches show that last-mile fine-tuning provides an attractive option when training data is limited or when robustness to input variation is sought without compromising on accuracy.

---


### 118. [TokAlign++: Advancing Vocabulary Adaptation via Better Token Alignment](https://arxiv.org/abs/2605.13429)

**<font color=#1a73e8>作者：</font>** Chong Li, Yingzhuo Deng, Wen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization is a foundational step in the text process of Large Language Models (LLMs). Texts must be first tokenized into token IDs, which are then input to LLMs. Inefficient tokenization results in long token-ID sequences and will slow down the training and inference of LLMs. The fine-grained knowledge transfer between LLMs, like token-level distillation, is also impeded by the mismatch in vocabulary. To bridge this gap, we introduce a method named TokAlign++ to improve vocabulary adaptation performance by learning better token alignment lexicon. The source and target vocabularies are taken as two different languages, and the bilingual token alignment lexicon is learned from monolingual token representations. Model parameters are rearranged following this bilingual lexicon for new vocabulary, and progressively fine-tuned for adaptation. Experimental results on 15 languages show that our method boosts the multilingual text compression rates and preserves most of the multilingual ability of vanilla models. It costs as few as 1k steps to restore the performance of the vanilla model. After unifying vocabularies between vanilla models, token-level distillation remarkably improves the base model with only 235M tokens.

---


### 119. [Pretraining Language Models with Subword Regularization: An Empirical Study of BPE Dropout in Low-Resource NLP](https://arxiv.org/abs/2605.13436)

**<font color=#1a73e8>作者：</font>** Ruan Visser, Trienko Grobler, Marcel Dunaiski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subword regularization methods such as BPE dropout are typically applied only during fine-tuning, while pretraining is usually done with deterministic tokenization. This creates a potential segmentation mismatch between pretraining and fine-tuning. We investigate whether applying BPE dropout during pretraining improves downstream performance in low-resource NLP. We train monolingual and bilingual BERT models on downsampled subsets of English, German, French, Spanish, Kiswahili, and isiXhosa, and evaluate them on XNLI, PAWS-X, PAN-X, and MasakhaNER 2.0. Across tasks, the best results are typically obtained when stochastic tokenization is applied during both pretraining and fine-tuning, whereas applying BPE dropout only during fine-tuning can underperform deterministic tokenization in smaller-data settings. This disadvantage diminishes as fine-tuning data increases, while the benefits of pretraining-time BPE dropout are largest when either pretraining or fine-tuning data is scarce.
The benefits of BPE dropout are often attributed to better compositional representations, especially for rare words. To examine this, we measure morphological boundary alignment under BPE dropout and find only modest improvements in expected alignment, while better-aligned segmentations remain rare. This suggests that fine-tuning alone may provide limited exposure to such segmentations, whereas stochastic tokenization during pretraining exposes the model to them more consistently. We further show that selectively introducing morphologically aligned segmentations during fine-tuning improves performance mainly for models pretrained without BPE dropout. Overall, these findings suggest that exposure to better-aligned segmentations may contribute to the downstream benefits of applying BPE dropout during pretraining.

---


### 120. [Assessing the Creativity of Large Language Models: Testing, Limits, and New Frontiers](https://arxiv.org/abs/2605.13450)

**<font color=#1a73e8>作者：</font>** Samuel Schapiro, Alexi Gladstone, Jonah Black 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Measuring the creativity of large language models (LLMs) is essential for designing methods that can improve creativity and for enhancing our scientific understanding of this ability. To accomplish this, it has become common in recent years to administer tests of human creativity to LLMs. Although these tests provide a convenient and fully automated way to score "creativity," their validity as measures of machine creativity has not been established, and these tests already have limited validity as predictors of human creativity. To address this problem, we conduct the first large-scale, systematic study assessing the effectiveness of human creativity tests for predicting the creative achievement of LLMs across three target constructs: creative writing, divergent thinking, and scientific ideation. We find that the Divergent Association Task (DAT) and the Conditional DAT are the best predictors of creative writing and divergent thinking, respectively, but that test effectiveness varies significantly by construct, and no single test predicts all constructs well. Moreover, contrary to popular belief, no existing test reliably predicts scientific ideation ability. Motivated by this problem, we introduce the Divergent Remote Association Test (DRAT), a vocabulary-space test that assesses both convergent and divergent thinking in a single instrument. The DRAT is the first and only creativity test for LLMs that is a significant predictor of scientific ideation ability, demonstrating robustness across major design choices. Furthermore, the performance gain of the DRAT is not recoverable from any linear combination of the Divergent Association Task and the Remote Associates Test, indicating that assessing divergent and convergent thinking in the same test is essential to reliably predicting scientific ideation ability.

---


### 121. [PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents](https://arxiv.org/abs/2605.13481)

**<font color=#1a73e8>作者：</font>** Mikhail Menschikov, Matvey Iskornev, Alexander Kharitonov 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce PersonalAI 2.0 (PAI-2), a novel framework, designed to enhance large language model (LLM) based systems through integration of external knowledge graphs (KG). The proposed approach addresses key limitations of existing Graph Retrieval-Augmented Generation (GraphRAG) methods by incorporating a dynamic, multistage query processing pipeline. The central point of PAI-2 design is its ability to perform adaptive, iterative information search, guided by extracted entities, matched graph vertices and generated clue-queries. Conducted evaluation over six benchmarks (Natural Questions, TriviaQA, HotpotQA, 2WikiMultihopQA, MuSiQue and DiaASQ) demonstrates improvement in factual correctness of generating answers compared to analogues methods (LightRAG, RAPTOR, and HippoRAG 2). PAI-2 achieves 4% average gain by LLM-as-a-Judge across four benchmarks, reflecting its effectiveness in reducing hallucination rates and increasing precision. We show that use of graph traversal algorithms (e.g. BeamSearch, WaterCircles) gain superior results compared to standard flatten retriever on average 6%, while enabled search plan enhancement mechanism gain 18% boost compared to disabled one by LLM-as-a-Judge across six datasets. In addition, ablation study reveals that PAI-2 achieves the SOTA result on MINE-1 benchmark, achieving 89% information-retention score, using LLMs from 7-14B tiers. Collectively, these findings underscore the potential of PAI-2 to serve as a foundational model for next-generation personalized AI applications, requiring scalable, context-aware knowledge representation and reasoning capabilities.

---


### 122. [Effective Context in Transformers: An Analysis of Fragmentation and Tokenization](https://arxiv.org/abs/2605.13485)

**<font color=#1a73e8>作者：</font>** Amirmehdi Jafari Fesharaki, Mohammadamin Rami, Aslan Tchamkerten  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers predict over a representation of a sequence. The same data can be written as bytes, characters, or subword tokens, and these representations may be lossless. Yet, under a fixed context window, they need not expose the same information to the model. This raises a basic question: how does the choice of representation change what a finite-context predictor can achieve?
We study this question on Markov sources and uncover two complementary phenomena. First, we observe that moving to smaller representation units can hurt prediction even when the context window is enlarged to cover the relevant source history. To explain this, we introduce fragmentation: a lossless recoding that replaces each source symbol by several smaller units. We prove that fragmentation can strictly increase the optimal finite-context log-loss, showing that the gap is not merely an optimization or capacity issue, but can be intrinsic to the representation. This gives a theoretical account of the finite-context gap observed in byte- and character-level models such as ByT5 and CANINE relative to subword-tokenized models. Second, we study the opposite direction: greedy tokenization -- BPE, WordPiece, and related methods -- which groups source symbols into larger units. We show that tokenization can make a short token window behave like a longer source-context window, and we give a loss guarantee describing when this is achievable. The guarantee depends on how reliably token windows span the needed source history, together with the compression rate of the tokenizer. This also yields a simple diagnostic for real tokenizers: measuring how much source context a fixed token window reliably contains. Together, the two directions establish a finite-context information-theoretic framework for reasoning about representation choices in Transformers.

---


### 123. [Many-Shot CoT-ICL: Making In-Context Learning Truly Learn](https://arxiv.org/abs/2605.13511)

**<font color=#1a73e8>作者：</font>** Tsz Ting Chung, Lemao Liu, Mo Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) adapts large language models (LLMs) to new tasks by conditioning on demonstrations in the prompt without parameter updates. With long-context models, many-shot ICL can use dozens to hundreds of examples and achieve performance comparable to fine-tuning, yet current understanding of its scaling behavior is largely derived from non-reasoning tasks. We study many-shot chain-of-thought in-context learning (CoT-ICL) for reasoning and show that standard many-shot rules do not transfer. Across non-reasoning and reasoning-oriented LLMs and across non-reasoning and reasoning tasks, we find: (i) a setting-dependent scaling effect, where increasing the number of CoT demonstrations is unstable for non-reasoning LLMs and benefits mainly reasoning-oriented LLMs; (ii) similarity-based retrieval helps on non-reasoning tasks but fails on reasoning, since semantic similarity poorly predicts procedural (i.e., CoT) compatibility; and (iii) an order-scaling effect, where performance variance grows with more CoT demonstrations. We interpret these behaviors by viewing many-shot CoT-ICL as in-context test-time learning rather than scaled pattern matching, and suggests two principles: (i) demonstrations should be easy for the target model to understand, and (ii) they should be ordered to support a smooth conceptual progression. Guided by the principle, we propose Curvilinear Demonstration Selection (CDS), a simple ordering method that yields up to a 5.42 percentage-point gain on geometry with 64 demonstrations. Overall, our results reframe the long context window from a retrieval buffer into a structured curriculum for in-context test-time learning.

---


### 124. [MMSkills: Towards Multimodal Skills for General Visual Agents](https://arxiv.org/abs/2605.13527)

**<font color=#1a73e8>作者：</font>** Kangning Zhang, Shuai Shao, Qingyao Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable skills have become a core substrate for improving agent capabilities, yet most existing skill packages encode reusable behavior primarily as textual prompts, executable code, or learned routines. For visual agents, however, procedural knowledge is inherently multimodal: reuse depends not only on what operation to perform, but also on recognizing the relevant state, interpreting visual evidence of progress or failure, and deciding what to do next. We formalize this requirement as multimodal procedural knowledge and address three practical challenges: (I) what a multimodal skill package should contain; (II) where such packages can be derived from public interaction experience; and (III) how agents can consult multimodal evidence at inference time without excessive image context or over-anchoring to reference screenshots. We introduce MMSkills, a framework for representing, generating, and using reusable multimodal procedures for runtime visual decision making. Each MMSkill is a compact, state-conditioned package that couples a textual procedure with runtime state cards and multi-view keyframes. To construct these packages, we develop an agentic trajectory-to-skill Generator that transforms public non-evaluation trajectories into reusable multimodal skills through workflow grouping, procedure induction, visual grounding, and meta-skill-guided auditing. To use them, we introduce a branch-loaded multimodal skill agent: selected state cards and keyframes are inspected in a temporary branch, aligned with the live environment, and distilled into structured guidance for the main agent. Experiments across GUI and game-based visual-agent benchmarks show that MMSkills consistently improve both frontier and smaller multimodal agents, suggesting that external multimodal procedural knowledge complements model-internal priors.

---


### 125. [Towards Unified Surgical Scene Understanding:Bridging Reasoning and Grounding via MLLMs](https://arxiv.org/abs/2605.13530)

**<font color=#1a73e8>作者：</font>** Jincai Huang, Shihao Zou, Yuchen Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical scene understanding is a cornerstone of computer-assisted intervention. While recent advances, particularly in surgical image segmentation, have driven progress, real-world clinical applications require a more holistic understanding that jointly captures procedural context, semantic reasoning, and precise visual grounding. However, existing approaches typically address these components in isolation, leading to fragmented representations and limited semantic consistency. To address this limitation, we propose SurgMLLM, a unified surgical scene understanding framework that bridges high-level reasoning and low-level visual grounding within a single model. Given surgical videos, SurgMLLM fine-tunes a multimodal large language model (MLLM) to support structured interpretability reasoning, which is used to jointly model phases, instrument-verb-target (IVT) triplets, and triplet-entity segmentation tokens. These tokens are then temporally aggregated and serve as prompts for a segmentation network, enabling accurate pixel-wise grounding of triplet instruments and targets. The entire framework is trained end-to-end with a unified objective that couples language-based reasoning supervision with visual grounding losses, promoting coherent cross-task learning and clinically consistent scene representations. To facilitate unified evaluation, we introduce CholecT45-Scene, extending CholecT45 dataset with 64,299 frames of pixel-level mask annotations for instruments and targets, aligned with existing triplet labels. Extensive experiments show that SurgMLLM significantly advances surgical scene understanding, improving the primary triplet recognition metric AP_IVT from 40.7% to 46.0% and consistently outperforming prior methods in phase recognition and segmentation. These results highlight the effectiveness of unified reasoning-and-grounding for reliable, context-aware surgical assistance.

---


### 126. [Temper and Tilt Lead to SLOP: Reward Hacking Mitigation with Inference-Time Alignment](https://arxiv.org/abs/2605.13537)

**<font color=#1a73e8>作者：</font>** Ye Wang, Jing Liu, Toshiaki Koike-Akino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time alignment techniques offer a lightweight alternative or complement to costly reinforcement learning, while enabling continual adaptation as alignment objectives and reward targets evolve. Existing theoretical analyses justify these methods as approximations to sampling from distributions optimally tilted toward a given reward model. We extend these techniques by introducing reference-model temperature adjustment, which leads to further generalization of inference-time alignment to ensembles of generative reward models combined as a sharpened logarithmic opinion pool (SLOP). To mitigate reward hacking, we propose an algorithm for calibrating SLOP weight parameters and experimentally demonstrate that it improves robustness while preserving alignment performance.

---


### 127. [Locale-Conditioned Few-Shot Prompting Mitigates Demonstration Regurgitation in On-Device PII Substitution with Small Language Models](https://arxiv.org/abs/2605.13538)

**<font color=#1a73e8>作者：</font>** Anuj Sadani, Deepak Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personally Identifiable Information (PII) redaction usually replaces detected entities with placeholder tokens such as [PERSON], destroying the downstream utility of the redacted text for retrieval and Named Entity Recognition (NER) training. We propose a fully on-device pipeline that substitutes PII with consistent, type-preserving fake values: a 1.5 B mixture-of-experts token classifier (openai/privacy-filter) detects spans, a 1-bit Bonsai-1.7B Small Language Model (SLM) proposes contextual surrogates for names, addresses, and dates, and a rule-based generator (faker) handles patterned fields. We report a prompting finding more important than the quantization choice: with naive fixed three-shot demonstrations, the 1-bit SLM regurgitates demonstration outputs verbatim regardless of input; 1.58-bit Ternary-Bonsai-1.7B reproduces byte-identical failures, ruling out quantization as the cause. We fix this with locale-conditioned rotating few-shot demonstrations: a character-range heuristic picks a locale-pure pool and a per-input MD5 hash samples three demonstrations. With the fix, 482/482 unique Bonsai-1.7B calls succeed (no echoes) and produce locale-correct surrogates, although the SLM still copies from a small same-locale demonstration pool - a residual narrowness we quantify. On a 2000-document multilingual corpus, hybrid perplexity (PPL) beats faker in all six locales under a multilingual evaluator (XGLM-564M); length preservation is best-of-three in 4 of 6 locales. On downstream NER (400 train / 100 test, English), redact yields F1=0.000, faker 0.656, original 0.960; on a matched 160/40 subset including hybrid, faker (0.506) outperforms hybrid (0.346) at p < 0.001. We report this as an honest negative finding: SLM surrogates produce more natural text but a less varied training distribution, and downstream NER benefits more from variety than from naturalness.

---


### 128. [Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph Foundation Models](https://arxiv.org/abs/2605.13540)

**<font color=#1a73e8>作者：</font>** Haonan Yuan, Qingyun Sun, Junhua Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graphs are ubiquitous in real-world systems, and building generalizable dynamic Graph Foundation Models has become a frontier in graph learning. However, dynamic graphs from different domains pose fundamental challenges to unified modeling, as their semantic and temporal patterns are inherently inconsistent, making the multi-domain pre-training difficult. Consequently, the widely used "pretrain-then-finetune" paradigm often suffers from severe negative knowledge transfer. To the best of our knowledge, there exists no multi-domain dynamic GFM. In this work, we propose DyGFM, a Dynamic Graph Foundation Model over multiple domains based on decoupled and divergence-conditioned prompting. To disentangle transferable semantics from the domain-specific dynamics, we introduce a dual-branch pre-training strategy with semantic-temporal decoupling. To alleviate negative transfer during domain adaptation, we further develop a cross-domain routing mechanism with divergence-aware expert selection. To enable efficient downstream fine-tuning, we design a divergence-conditioned prompt generator that injects lightweight, learnable graph prompts tailored to semantic and temporal traits. Extensive experiments on continuous dynamic graph benchmarks demonstrate that DyGFM consistently outperforms 12 state-of-the-art baselines on both node classification and link prediction tasks, achieving superior effectiveness and efficiency.

---


### 129. [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://arxiv.org/abs/2605.13542)

**<font color=#1a73e8>作者：</font>** Chengzhi Shen, Weixiang Shen, Tobias Susetzky 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intensive care units (ICU) generate long, dense and evolving streams of clinical information, where physicians must repeatedly reassess patient states under time pressure, underscoring a clear need for reliable AI decision support. Existing ICU benchmarks typically treat historical clinician actions as ground truth. However, these actions are made under incomplete information and limited temporal context of the underlying patient state, and may therefore be suboptimal, making it difficult to assess the true reasoning capabilities of AI systems. We introduce RealICU, a hindsight-annotated benchmark for evaluating large language models (LLMs) under realistic ICU conditions, where labels are created after senior physicians review the full patient trajectory. We formulate four physician-motivated tasks: assess Patient Status, Acute Problems, Recommended Actions, and Red Flag actions that risk unsafe outcomes. We partition each trajectory with 30-min windows and release two datasets: RealICU-Gold with 930-window annotations from 94 MIMIC-IV patients, and RealICU-Scale with 11,862 windows extended by Oracle, a physician-validated LLM hindsight labeler. Existing LLMs including memory-augmented ones performed poorly on RealICU, exposing two failure modes: a recall-safety tradeoff for clinical recommendations, and an anchoring bias to early interpretations of the patient. We further introduce ICU-Evo to study structured-memory agents that improves long-horizon reasoning but does not fully eliminate safety failures. Together, RealICU provides a clinically grounded testbed for measuring and improving AI sequential decision-support in high-stakes care. Project page: this https URL

---


### 130. [Qwen-Image-VAE-2.0 Technical Report](https://arxiv.org/abs/2605.13565)

**<font color=#1a73e8>作者：</font>** Zekai Zhang, Deqing Li, Kuan Cao 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Qwen-Image-VAE-2.0, a suite of high-compression Variational Autoencoders (VAEs) that achieve significant advances in both reconstruction fidelity and diffusability. To address the reconstruction bottlenecks of high compression, we adopt an improved architecture featuring Global Skip Connections (GSC) and expanded latent channels. Moreover, we scale training to billions of images and incorporate a synthetic rendering engine to improve performance in text-rich scenarios. To tackle the convergence challenges of high-dimensional latent space, we implement an enhanced semantic alignment strategy to make the latent space highly amenable to diffusion modeling. To optimize computational efficiency, we leverage an asymmetric and attention-free encoder-decoder backbone to minimize encoding overhead. We present a comprehensive evaluation of Qwen-Image-VAE-2.0 on public reconstruction benchmarks. To evaluate performance in text-rich scenarios, we propose OmniDoc-TokenBench, a new benchmark comprising a diverse collection of real-world documents coupled with specialized OCR-based evaluation metrics. Qwen-Image-VAE-2.0 achieves state-of-the-art reconstruction performance, demonstrating exceptional capabilities in both general domains and text-rich scenarios at high compression ratio. Furthermore, downstream DiT experiments reveal our models possess superior diffusability, significantly accelerating convergence compared to existing high-compression baselines. These establish Qwen-Image-VAE-2.0 as a leading model with high compression, superior reconstruction, and exceptional diffusability.

---


### 131. [Position: Assistive Agents Need Accessibility Alignment](https://arxiv.org/abs/2605.13579)

**<font color=#1a73e8>作者：</font>** Jie Hu, Changyuan Yan, Yu Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assistive agents for Blind and Visually Impaired (BVI) users require accessibility alignment as a first-class design objective. Despite rapid progress in agentic AI, most systems are designed and evaluated under assumptions of sighted interaction, low-cost verification, and tolerable trial-and-error, leading to systematic failures in assistive scenarios that cannot be resolved by model scaling or post-hoc interface adaptations alone. Drawing on an analysis of 778 assistance task instances from prior work, we show that current agentic AI remain prone to failure in assistive scenarios due to mismatches between sighted-user design assumptions and the verification, risk, and interaction constraints faced by BVI users. We argue that accessibility should be treated as an alignment problem rather than a peripheral usability concern. To this end, we introduce accessibility alignment and propose a lifecycle-oriented design pipeline for accessibility-aligned assistive agents, spanning user research, system design, deployment and post-deployment iteration. We conclude that BVI-centered assistive tasks provide a critical stress test for agentic AI and motivate a broader shift toward inclusive agent design.

---


### 132. [Inducing Artificial Uncertainty in Language Models](https://arxiv.org/abs/2605.13595)

**<font color=#1a73e8>作者：</font>** Sophia Hager, Simon Zeng, Nicholas Andrews  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In safety-critical applications, language models should be able to characterize their uncertainty with meaningful probabilities. Many uncertainty quantification approaches require supervised data; however, finding suitable unseen challenging data is increasingly difficult for large language models trained on vast amounts of scraped data. If the model is consistently (and correctly) confident in its predictions, the uncertainty quantification method may consistently overestimate confidence on new and unfamiliar data. Finding data which exhibits enough uncertainty to train supervised uncertainty quantification methods for high-performance models may therefore be challenging, and will increase in difficulty as LLMs saturate datasets. To address this issue, we first introduce the problem of inducing artificial uncertainty in language models, then investigate methods of inducing artificial uncertainty on trivially easy data in the absence of challenging data at training time. We use probes trained to recognize artificial uncertainty on the original model, and find that these probes trained on artificial uncertainty outperform probes trained without artificial uncertainty in recognizing real uncertainty, achieving notably higher calibration on hard data with minimal loss of performance on easy data.

---


### 133. [Multimodal Graph-based Classification of Esophageal Motility Disorders](https://arxiv.org/abs/2605.13623)

**<font color=#1a73e8>作者：</font>** Alexander Geiger, Lars Wagner, Daniel Rueckert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnosing esophageal motility disorders pose significant challenges due to the complexity of high-resolution impedance manometry (HRIM) data and variability in clinical interpretation. This work explores the feasibility of a multimodal Machine Learning (ML)-based classification approach that combines HRIM recordings with patient-specific information and incorporates a graph-based modeling of esophageal physiology. We analyze HRIM recordings with corresponding patient information from 104 patients with esophageal motility disorders. Patient data includes demographic, clinical, and symptom information extracted from structured questionnaires and free-text notes using keyword detection and large language model-based processing. HRIM data is represented as spatio-temporal graphs, where nodes correspond to pressure values along the esophagus and edges encode spatial adjacency and impedance dynamics. A graph neural network (GNN) is applied to learn physiologically meaningful representations, which are fused with patient embeddings for multi-category, multi-class classification of swallow events. The impact of patient features and graph-based modeling is evaluated by ablation studies and comparison to vision-based classifier baselines. The proposed multimodal approach indicates improvements over models that rely solely on HRIM-derived features across all classification categories. Additionally, the graph-based modeling provides gains compared to vision-based baselines. Our experiments systematically assess the complementary contribution of multiple modalities, as well as demonstrate the feasibility of our proposed graph-based approach. Our initial findings demonstrate that integrating patient-level data with graph-based representations of HRIM signals appears to be a promising direction for more accurate classification of esophageal motility disorders.

---


### 134. [Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction](https://arxiv.org/abs/2605.13624)

**<font color=#1a73e8>作者：</font>** Takumi Goto, Yusuke Sakai, Taro Watanabe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammatical error correction using large language models often suffers from the over-correction issue. To mitigate this, we propose a training-free inference method that performs edit-level majority voting over multiple candidates generated by a single model, without requiring model modifications or additional training. Across nine benchmarks covering English, Czech, German, Ukrainian, Korean, Hindi, and Romanian, the proposed method outperforms both greedy and MBR decoding in most cases. Moreover, it yields stable correction quality regardless of the instruction prompts used. We release two repository supporting GEC datasets loading and LLM inference.

---


### 135. [FlowCompile: An Optimizing Compiler for Structured LLM Workflows](https://arxiv.org/abs/2605.13647)

**<font color=#1a73e8>作者：</font>** Junyan Li, Zhang-Wei Hong, Maohao Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured LLM workflows, where specialized LLM sub-agents execute according to a predefined graph, have become a powerful abstraction for solving complex tasks. Optimizing such workflows, i.e., selecting configurations for each sub-agent to balance accuracy and latency, is challenging due to the combinatorial design space over model choices, reasoning budgets, and workflow structures. Existing cost-aware methods largely treat workflow optimization as a routing problem, selecting a configuration at inference time for each query according to the accuracy-latency objective used during training. We argue that structured LLM workflows can also be optimized from a compilation perspective: before deployment, the system can globally explore the workflow design space and construct a reusable set of workflow-level configurations spanning diverse accuracy-latency trade-offs. Drawing inspiration from machine learning compilers, we introduce FlowCompile, a structured LLM workflow compiler that performs compile-time design space exploration to identify a high-quality, reusable trade-off set. FlowCompile decomposes a workflow into sub-agents, profiles each sub-agent under diverse configurations, and composes these measurements through a structure-aware proxy to estimate workflow-level accuracy and latency. It then identifies diverse high-quality configurations in a single compile-time pass, without retraining or online adaptation. Experiments across diverse workflows and challenging benchmarks show that FlowCompile consistently outperforms heuristically optimized workflow configurations and routing-based baselines, delivering up to 6.4x speedup. The compiled configuration set further serves as a reusable optimization artifact, enabling flexible deployment under varying runtime preferences and supporting downstream selection or routing.

---


### 136. [Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training](https://arxiv.org/abs/2605.13652)

**<font color=#1a73e8>作者：</font>** Namrata Shivagunde, Vijeta Deshpande, Sherin Muckatira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training large language models is dominated by the memory cost of storing full-rank weights, gradients, and optimizer states. Low-rank pre-training has emerged to address this, and the space of methods has grown rapidly. A central question remains open: do low-rank methods produce models that generalize comparably to full-rank training, or does the rank constraint fundamentally alter the solutions reached? Existing comparisons rely almost entirely on validation perplexity from single-seed runs, often carried forward from prior literature. Yet perplexity is a poor proxy for solution quality; two methods can match on perplexity while converging to different loss landscape regions and internal representations. We close this gap by characterizing the solutions found by five low-rank pre-training methods, GaLore and Fira (memory-efficient optimizers), CoLA and SLTrain (architecture reparameterizations), and ReLoRA (adapter-style updates with periodic resets), against full-rank training at three model scales (60M, 130M, 350M). We evaluate each along 16 metrics across four dimensions: 1-D loss landscape along random/top-K PCA directions, 1-D interpolation between checkpoints, spectral structure of the weights and learned updates, and activation similarity to full-rank training. We show that low-rank methods are not equivalent to full-rank training, nor to one another, even when validation perplexity is close. Full-rank training settles into a sharper basin than low-rank methods along random directions, while the reverse holds for the top-1 PCA direction. Each method converges to a geometrically distinct basin. Low-rank activations diverge from full-rank in later layers as training progresses, with GaLore tracking full-rank most closely. Further, validation perplexity does not translate to downstream performance at every scale. Adding geometric and spectral metrics improves the prediction.

---


### 137. [Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas](https://arxiv.org/abs/2605.13663)

**<font color=#1a73e8>作者：</font>** Lukas Stähelin, Veronika Solopova, Max Upravitelev 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Propaganda detection in social media is challenging due to noisy, short texts and low annotation agreements. We introduce a new intent-focused taxonomy of propaganda techniques and compare it against an established, higher-agreement schema. Along three dimensions (model portfolio, schema effects, and prompting strategy) we evaluate the taxonomies as a classification task with the help of four language models (GPT-4.1-nano, Phi-4 14B, Qwen2.5-14B, Qwen3-14B). Our results show that fine-tuning is essential, since it transforms weak zero-shot baselines into competitive systems and reveals methodological differences that are hidden using base models. Across schemas, the Qwen models achieve the strongest overall performance, and Phi-4 14B consistently outperforms GPT-4.1-nano. Our hierarchical prompting method (HiPP), which predicts fine-grained techniques before aggregating them, is especially beneficial after fine-tuning and on the more ambiguous, low-agreement taxonomy, while remaining competitive on the simpler schema. The HQP dataset, annotated with the new intent-based labels, provides a richer lens on propaganda's strategic goals and a challenging benchmark for future work on robust, real-world detection.

---


### 138. [SceneGraphVLM: Dynamic Scene Graph Generation from Video with Vision-Language Models](https://arxiv.org/abs/2605.13667)

**<font color=#1a73e8>作者：</font>** Vladislav Makarov, Mark Gizetdinov, Dmitry Yudin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene graph generation provides a compact structured representation for visual perception, but accurate and fast graph prediction from images and videos remains challenging. Recent VLM-based methods can generate scene graphs end-to-end as structured text, yet often produce long outputs with irrelevant objects and relations. We present SceneGraphVLM, a compact method for image and video scene graph generation with small visual language models. SceneGraphVLM serializes graphs in a token-efficient TOON format and trains the model in two stages: supervised fine-tuning followed by reinforcement learning with hallucination-aware rewards that balance relation coverage and precision while penalizing unsupported objects and relations. For videos, the model can optionally condition each frame on the previously generated graph, providing lightweight short-term context without tracking or post-processing. We evaluate SceneGraphVLM on PSG, PVSG, and Action Genome. With compact VLMs and vLLM-accelerated decoding, SceneGraphVLM achieves a strong quality-speed trade-off, improves precision-oriented SGG metrics while preserving reasonable recall, and generates complete scene graphs with approximately one-second latency. Code and implementation details are available at: this https URL.

---


### 139. [Sampling from Flow Language Models via Marginal-Conditioned Bridges](https://arxiv.org/abs/2605.13681)

**<font color=#1a73e8>作者：</font>** Iskander Azangulov, Leo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Language Models (FLMs) are a recently introduced class of language models which adapt continuous flow matching for one-hot encoded token sequences. Their denoisers have a special structure absent from generic continuous diffusion models: each block of the denoising mean is a posterior marginal distribution over the clean token at that position. Standard DDPM-style samplers collapse these marginals to a single conditional-mean endpoint and bridge toward this simplex-valued point, which is generally not a valid one-hot sequence. We argue that the natural sampler for an FLM is instead posterior-predictive. At each reverse step, we sample a clean one-hot endpoint from the factorized posterior defined by the FLM token marginals, and then sample the next continuous state from the analytic Ornstein--Uhlenbeck bridge conditioned on that endpoint. The method is training-free, uses the same model evaluations as standard sampling, and gives a principled interface for token-level decoding controls such as temperature scaling and nucleus truncation. We show that, under exact posterior marginals, the endpoint approximation error is exactly the conditional multi-information among token positions. The induced one-step bridge kernel preserves all token-wise posterior-predictive marginals and loses only the residual cross-position dependence. Finally, we prove a Girsanov path-space comparison showing that the marginal-conditioned bridge has a no-larger denoising-error term than the frozen conditional-mean bridge, with strict improvement whenever intermediate coordinate-wise bridge observations reveal additional information about the clean token. Experiments with FLMs show that the sampler improves the quality--diversity tradeoff. Code is available at: this http URL.

---


### 140. [A Hierarchical Language Model with Predictable Scaling Laws and Provable Benefits of Reasoning](https://arxiv.org/abs/2605.13687)

**<font color=#1a73e8>作者：</font>** Jason Gaitonde, Frederic Koehler, Elchanan Mossel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a family of synthetic languages with hierarchical structure -- generated by a broadcast process on trees -- for which the role of context length and reasoning in autoregressive generation can be analyzed precisely. At the heart of our analytic approach is an \emph{exact $k$-gram ansatz} in place of transformers with context length $k$, a substitution we then validate empirically. Using this ansatz we derive explicit asymptotic predictions for distributional statistics of the sequences produced by a trained model, instantiated in two settings. For the \emph{Ising broadcast process} (a soft-constrained language), we prove that the variance of the generated sum scales log-linearly in the context depth and its kurtosis converges to that of a Gaussian -- both deviating from the true language for any sublinear context. For the \emph{coloring broadcast process} (a hard-constrained language) in the freezing regime, bounded-context autoregression produces sequences that, with high probability, are inconsistent with \emph{any} valid coloring of the underlying tree. Together these results imply an $\Omega(n)$ lower bound on the context length required to faithfully sample length-$n$ sequences. In contrast, we prove that an autoregressive \emph{reasoning} model with only $\Theta(\log n)$ working memory can sample exactly from the true language -- an exponential improvement. We confirm both the lower-bound predictions and the reasoning-based upper bound empirically with transformers trained on the synthetic language; the trained models track our asymptotic predictions quantitatively across a wide range of context sizes.

---


### 141. [RTLC -- Research, Teach-to-Learn, Critique: A three-stage prompting paradigm inspired by the Feynman Learning Technique that lifts LLM-as-judge accuracy on JudgeBench with no fine-tuning](https://arxiv.org/abs/2605.13695)

**<font color=#1a73e8>作者：</font>** Andrea Morandi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge is now the default measurement instrument for open-ended generation, but on the public JudgeBench benchmark even strong instruction-tuned judges barely scrape past random on objective-correctness pairwise items. We introduce RTLC, a three-stage prompting recipe -- Research, Teach-to-Learn, Critique -- that promotes a single black-box LLM into an ensemble-of-thought judge with no fine-tuning, retrieval, or external tools. Stage 1 wraps the input in a fixed pedagogical scaffold porting the Feynman Learning Technique (study $\to$ teach $\to$ find gaps $\to$ simplify) into LLM prompting. Stage 2 draws N=10 independent candidate verdicts at temperature 0.4. Stage 3 acts as its own critic, cross-comparing the candidate set against the original question to emit one critiqued verdict at temperature 0. On JudgeBench-GPT (350 hard pairwise items), Claude 3.7 Sonnet's pairwise accuracy climbs from 64.6% (single-shot vanilla prompt) to 78.6% (RTLC critique-of-10) -- an absolute 14.0-percentage-point gain. RTLC also beats N=10 self-consistency majority voting (77.7%) and a zero-shot first candidate (74.0%). A clean three-step ablation attributes +9.4 pp to the Teach-to-Learn scaffold, +3.7 pp to N=10 marginalisation, and +0.9 pp to explicit critique. We discuss the cost-accuracy frontier (RTLC sits above self-consistency at every working point), the error-budget breakdown across the four JudgeBench categories (knowledge, reasoning, math, coding), and how RTLC composes orthogonally with post-hoc judge-score calibration, with the two interventions compounding multiplicatively in practice.

---


### 142. [Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety](https://arxiv.org/abs/2605.13709)

**<font color=#1a73e8>作者：</font>** Qian Shen, Fanghua Cao, Min Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are widely applied in educational practices, such as for generating children's stories. However, the generated stories are often too difficult for children to read, and the operational cost of LLMs hinders their widespread adoption in educational settings. We used an existing expert-designed children's reading curriculum and its corresponding generated stories from GPT-4o and Llama 3.3 70B to design different experiments for fine-tuning three 8B-parameter LLMs, which then generated new English reading stories that were subjected to quantitative and qualitative evaluation. Our method prioritizes controllability over scale, enabling educators to target reading levels and error patterns with a compact, affordable model. Our evaluation results show that with appropriate fine-tuning designs, children's English reading stories generated by 8B LLMs perform better on difficulty-related metrics than those from zero-shot GPT-4o and Llama 3.3 70B, with almost no discernible safety issues. Such fine-tuned LLMs could be more broadly used by teachers, parents, and children in classrooms and at home to generate engaging English reading stories with children's interests, controllable difficulty and safety.

---


### 143. [MILM: Large Language Models for Multimodal Irregular Time Series with Informative Sampling](https://arxiv.org/abs/2605.13711)

**<font color=#1a73e8>作者：</font>** Hsing-Huan Chung, Shijun Li, Yoav Wald 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal irregular time series (MITS) consist of asynchronous and irregularly sampled observations from heterogeneous numerical and textual channels. In healthcare, for example, patients' electronic health records (EHR) include irregular lab measurements and clinical notes. The irregular timing and channel patterns of observations carry predictive signal alongside the numerical values and textual content. LLMs are natural candidates for processing such heterogeneous data, given their extensive pretrained knowledge spanning textual and numerical domains. We introduce MILM (Multimodal Irregular time series Language Model), which represents MITS as time-ordered triplets in Extensible Markup Language (XML) format and fine-tunes an LLM through a two-stage strategy for MITS classification. The first stage trains on value-redacted MITS to predict from sampling patterns alone, and the second stage trains on full MITS to jointly model sampling patterns and observed values. Our two-stage model (MILM-2S) and its single-stage counterpart (MILM-Direct) achieve the best and second-best average performance on multiple EHR datasets. Further value redaction evaluations confirm that sampling patterns carry predictive signal and that MILM-2S learns to exploit them. In the value pending evaluation we introduce, where some values are unavailable at prediction time, MILM-2S outperforms MILM-Direct by a larger margin compared to standard evaluation. For MILM-2S, preserving the time and channel of value-pending observations as additional sampling information further improves in-hospital mortality prediction.

---


### 144. [Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs](https://arxiv.org/abs/2605.13737)

**<font color=#1a73e8>作者：</font>** Trung Nguyen Quang, Yiming Gao, Fanyi Pu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an omnimodal large language model accepts a question whose textual premise contradicts what it actually sees or hears, does the failure lie in perception or in action? Recent omnimodal models are positioned as perception-grounded agents that jointly process video, audio, and text, yet a basic form of grounding remains untested: catching a textual claim that conflicts with the model's own sensory input. We introduce IMAVB, a curated 500-clip benchmark of long-form movies with a 2x2 design crossing target modality (vision, audio) and premise condition (standard, misleading), which lets us measure conflict detection separately from ordinary multimodal comprehension. Across eight open-source omnimodal LLMs and Gemini 3.1 Pro, we document a Representation-Action Gap: hidden states reliably encode premise-perception mismatches even when the same models almost never reject the false claim in their outputs. Behaviorally, models fall into two failure modes: under-rejection, in which they answer misleading questions as if the false premise were true; and over-rejection, in which they reject more often but also reject standard questions, sacrificing ordinary comprehension accuracy. The gap is modality-asymmetric (audio grounding underperforms vision) and prompt-resistant across seven variants. As an initial diagnostic intervention, a probe-guided logit adjustment (PGLA) re-injects the encoded mismatch signal into decoding and consistently improves rejection behavior. Together, these results suggest the bottleneck for omnimodal grounding lies in translation, not perception.

---


### 145. [Learning POMDP World Models from Observations with Language-Model Priors](https://arxiv.org/abs/2605.13740)

**<font color=#1a73e8>作者：</font>** Valentin Six, Frederik Panse, Mathis Fajeau 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whether navigating a building, operating a robot, or playing a game, an agent that acts effectively in an environment must first learn an internal model of how that environment works. Partially-observable Markov decision processes (POMDPs) provide a flexible modeling class for such internal world models, but learning them from observation-action trajectories alone is challenging and typically requires extensive environment interaction. We ask whether language-model priors can reduce costly interaction by leveraging prior knowledge, and introduce \emph{Pinductor} (POMDP-inductor): an LLM proposes candidate POMDP models from a few observation-action trajectories and iteratively refines them to optimize a belief-based likelihood score. Despite using strictly less information, \emph{Pinductor} matches the performance and sample efficiency of LLM-based POMDP learning methods that assume privileged access to the hidden state, while significantly surpassing the sample efficiency of tabular POMDP baselines. Further results show that performance scales with LLM capability and degrades gracefully as semantic information about the environment is withheld. Together, these results position language-model priors as a practical tool for sample-efficient world-model learning under partial observability, and a step toward generalist agents in real-world environments. Code is available at this https URL.

---


### 146. [GHGbench: A Unified Multi-Entity, Multi-Task Benchmark for Carbon Emission Prediction](https://arxiv.org/abs/2605.13743)

**<font color=#1a73e8>作者：</font>** Yifan Duan, Siyuan Zheng, Lihuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open datasets and benchmarks for entity-level carbon-emission prediction remain fragmented across access, scale, granularity, and evaluation. We introduce GHGbench, an open dataset and benchmark for company- and building-level greenhouse-gas prediction. The company track contains 32,000+ company-year records from 12,000+ firms with Scope 1+2 and Scope 3 disclosures and financial/sectoral signals; the building track harmonises 491,591 building-year records from 13 open sources into a single schema across 26 metropolitan areas (10 U.S., 15 Australian, 1 Singaporean), with climate covariates and multimodal remote-sensing embeddings. GHGbench defines canonical splits with in-distribution and cross-region/city transfer as primary tasks and temporal hold-out plus short-horizon forecasting as supplementary appendix evidence; headline baselines span gradient-boosted trees, a tabular foundation model, MLP, FT-Transformer, and multimodal fusion, with an LLM panel as auxiliary, all evaluated under multi-seed paired-bootstrap tests. Three benchmark-level findings emerge: (i) building emissions are structurally harder than company emissions; (ii) the in-distribution to out-of-distribution gap dwarfs any within-model gap across both the company track and the building track, and a tabular foundation model is, to our knowledge, the first baseline to open a paired-bootstrap-significant gap over tuned trees on a multi-city building-emissions task; (iii) multimodal remote-sensing embeddings help precisely where tabular generalisation breaks. GHGbench also exposes catastrophic city transfer and the sector-factor lookup ceiling as systematic failure modes. Code and reconstruction recipes are available at GHGbench.

---


### 147. [High-Rate Quantized Matrix Multiplication II](https://arxiv.org/abs/2605.13768)

**<font color=#1a73e8>作者：</font>** Or Ordentlich, Yury Polyanskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This is the second part of the work investigating quantized matrix multiplication (MatMul). In part I we considered the case of calibration-free quantization, whereas here we discuss the setting where covariance matrix $\Sigma_X$ of the columns of the second factor is available. This setting arises in the ubiquitous task of weight-only post-training quantization of LLMs.
Weight-only quantization is related to the problem of weighted mean squared error (WMSE) source coding, whose classical (reverse) waterfilling solution dictates how one should distribute rate between coordinates of the vector. We show how waterfilling can be used to improve practical LLM quantization algorithms (GPTQ), which at present allocate rate equally. A recent scheme (known as ``WaterSIC'') that only uses scalar INT quantizers is analyzed and its high-rate performance is shown to be (a) basis free (i.e., characterized by the determinant of $\Sigma_X$ and, thus, unlike existing schemes, is immune to applying random rotations); and (b) within a multiplicative factor of $\frac{2\pi e}{12}$ (or 0.25 bit/entry) of the information-theoretic distortion limit. GPTQ's performance, in turn, is affected by the choice of basis, but for a random rotation and actual $\Sigma_X$ from Llama-3-8B we find it to be within 0.1 bit (depending on the layer type) of WaterSIC, suggesting that GPTQ with random rotation is also near optimal, at least in the high-rate regime.

---


### 148. ["Like Taking the Path of Least Resistance": Exploring the Impact of LLM Interaction on the Creative Process of Programming](https://arxiv.org/abs/2605.13776)

**<font color=#1a73e8>作者：</font>** Zeinabsadat Saghi, Run Huang, Souti Chattopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creativity is fundamentally human. As AI takes on more of the generative work that once required human imagination, despite documented limitations in creative ability, a critical question emerges: How does GenAI affect users' creativity? Through a within-subject study followed by retrospective interviews with (N=20) programmers, we investigated the impact of LLMs on participants' process of creative thinking in programming and the creativity of generated solutions. Across two conditions (LLM-assisted vs. unassisted), participants using LLMs had significantly shorter idea-generation periods (p=0.0004), leading to fewer creative moments (p=0.002). Qualitative analysis of participants' interactions and interviews revealed four different human-LLM collaboration modes supporting various problem-solving strategies. However, a comparative analysis of the generated solutions shows that while LLMs can help generate more correct and functional code, their solutions contain roughly the same number of ideas as participant-generated ones. Based on our findings, we discuss design implications and considerations for effectively using LLMs to support user creativity.

---


### 149. [MinT: Managed Infrastructure for Training and Serving Millions of LLMs](https://arxiv.org/abs/2605.13779)

**<font color=#1a73e8>作者：</font>** Mind Lab, Song Cao, Vic Cao 等 62 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present MindLab Toolkit (MinT), a managed infrastructure system for Low-Rank Adaptation (LoRA) post-training and online serving. MinT targets a setting where many trained policies are produced over a small number of expensive base-model deployments. Instead of materializing each policy as a merged full checkpoint, MinT keeps the base model resident and moves exported LoRA adapter revisions through rollout, update, export, evaluation, serving, and rollback, hiding distributed training, serving, scheduling, and data movement behind a service interface. MinT scales this path along three axes. Scale Up extends LoRA RL to frontier-scale dense and MoE architectures, including MLA and DSA attention paths, with training and serving validated beyond 1T total parameters. Scale Down moves only the exported LoRA adapter, which can be under 1% of base-model size in rank-1 settings; adapter-only handoff reduces the measured step by 18.3x on a 4B dense model and 2.85x on a 30B MoE, while concurrent multi-policy GRPO shortens wall time by 1.77x and 1.45x without raising peak memory. Scale Out separates durable policy addressability from CPU/GPU working sets: a tensor-parallel deployment supports 10^6-scale addressable catalogs (measured single-engine sweeps through 100K) and thousand-adapter active waves at cluster scale, with cold loading treated as scheduled service work and packed MoE LoRA tensors improving live engine loading by 8.5-8.7x. MinT thus manages million-scale LoRA policy catalogs while training and serving selected adapter revisions over shared 1T-class base models.

---


### 150. [An LLM-Based System for Argument Reconstruction](https://arxiv.org/abs/2605.13793)

**<font color=#1a73e8>作者：</font>** Paulo Pirozelli, Victor Hugo Nascimento Rocha, Fabio G. Cozman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arguments are a fundamental aspect of human reasoning, in which claims are supported, challenged, and weighed against one another. We present an end-to-end large language model (LLM)-based system for reconstructing arguments from natural language text into abstract argument graphs. The system follows a multi-stage pipeline that progressively identifies argumentative components, selects relevant elements, and uncovers their logical relations. These elements are represented as directed acyclic graphs consisting of two component types (premises and conclusions) and three relation types (support, attack, and undercut). We conduct two complementary experiments to evaluate the system. First, we perform a manual evaluation on arguments drawn from an argumentation theory textbook to assess the system's ability to recover argumentative structure. Second, we conduct a quantitative evaluation on benchmark datasets, allowing comparison with prior work by mapping our outputs to established annotation schemes. Results show that the system can adequately recover argumentative structures and, when adapted to different annotation schemes, achieve reasonable performance across benchmark datasets. These findings highlight the potential of LLM-based pipelines for scalable argument reconstruction.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-159](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
