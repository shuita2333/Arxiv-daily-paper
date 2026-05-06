# 🧠 大模型相关研究 | 2026年05月07日

> 本类共 **130** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-130**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-130**

---

### 101. [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](https://arxiv.org/abs/2605.03799)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline: from tokenisation and vectorisation to fine-tuning of large language models, retrieval-augmented generation, and reinforcement learning from human feedback. Twelve hands-on sessions combine concise theory with detailed implementation plans, formalised evaluation metrics, and transparent assessment criteria. The work is not a conventional textbook: it is designed as a reproducible research artefact where every session requires publishing code, models, and reports in public repositories. All experiments are conducted on a single evolving corpus, and the work advocates open-weight models over commercial APIs, with special attention to the Hugging Face ecosystem. The material is enriched by original research on low-resource languages, incorporating linguistic resources for Tajik and Tatar (subword tokenisers, embeddings, lexical databases, and transliteration benchmarks), demonstrating how modern NLP can be adapted to data-scarce environments. Designed for senior undergraduates, graduate students, and practising developers seeking to implement, compare, and deploy methods from classical ML to state-of-the-art LLM-based systems.

---


### 102. [ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting](https://arxiv.org/abs/2605.03804)

**<font color=#1a73e8>作者：</font>** Jiale Chang, Yuxiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term personalized memory for LLM agents is challenging on resource-limited edge devices due to high storage costs and multimodal complexity. To address this, we propose ScrapMem, a framework that integrates multimodal data into "Scrapbook Page." ScrapMem introduces Optical Forgetting, an optical compression mechanism that progressively reduces the resolution of older memories, lowering storage cost while suppressing low-value details. To maintain semantic consistency, we construct an Episodic Memory Graph (EM-Graph) that organizes key events into a causal-temporal structure. Extensive experiments on the multimodal ATM-Bench showcase that ScrapMem provides three main benefits: (1) strong performance, achieving a new state-of-the-art with a 51.0% Joint@10 score; (2) high storage efficiency, reducing memory usage by up to 93% via optical forgetting; and (3) improved recall, increasing Recall@10 to 70.3% through structured aggregation. ScrapMem offers an effective and storage-efficient solution for on-device long-term memory in multimodal LLM agents.

---


### 103. [Agentic-imodels: Evolving agentic interpretability tools via autoresearch](https://arxiv.org/abs/2605.03808)

**<font color=#1a73e8>作者：</font>** Chandan Singh, Yan Shuo Tan, Weijia Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic data science (ADS) systems are rapidly improving their capability to autonomously analyze, fit, and interpret data, potentially moving towards a future where agents conduct the vast majority of data-science work. However, current ADS systems use statistical tools designed to be interpretable by humans, rather than interpretable by agents. To address this, we introduce Agentic-imodels, an agentic autoresearch loop that evolves data-science tools designed to be interpretable by agents. Specifically, it develops a library of scikit-learn-compatible regressors for tabular data that are optimized for both predictive performance and a novel LLM-based interpretability metric. The metric measures a suite of LLM-graded tests that probe whether a fitted model's string representation is "simulatable" by an LLM, i.e. whether the LLM can answer questions about the model's behavior by reading its string output alone. We find that the evolved models jointly improve predictive performance and agent-facing interpretability, generalizing to new datasets and new interpretability tests. Furthermore, these evolved models improve downstream end-to-end ADS, increasing performance for Copilot CLI, Claude Code, and Codex on the BLADE benchmark by up to 73%

---


### 104. [Multimodal Learning on Low-Quality Data with Conformal Predictive Self-Calibration](https://arxiv.org/abs/2605.03820)

**<font color=#1a73e8>作者：</font>** Xun Jiang, Yufan Gu, Disen Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal learning often grapples with the challenge of low-quality data, which predominantly manifests as two facets: modality imbalance and noisy corruption. While these issues are often studied in isolation, we argue that they share a common root in the predictive uncertainty towards the reliability of individual modalities and instances during learning. In this paper, we propose a unified framework, termed Conformal Predictive Self-Calibration (CPSC), which leverages conformal prediction to equip the model with the ability to perform self-guided calibration on-the-fly. The core of our proposed CPSC lies in a novel self-calibrating training loop that seamlessly integrates two key modules: (1) Representation Self-Calibration, which decomposes unimodal features into components, and selectively fuses the most robust ones identified by a conformal predictor to enhance feature resilience. (2) Gradient Self-Calibration, which recalibrates the gradient flow during backpropagation based on instance-wise reliability scores, steering the optimization towards more trustworthy directions. Furthermore, we also devise a self-update strategy for the conformal predictor to ensure the entire system co-evolves consistently throughout the training process. Extensive experiments on six benchmark datasets under both imbalanced and noisy settings demonstrate that our CPSC framework consistently outperforms existing state-of-the-art methods. Our code is available at this https URL.

---


### 105. [TRACE: A Metrologically-Grounded Engineering Framework for Trustworthy Agentic AI Systems in Operationally Critical Domains](https://arxiv.org/abs/2605.03838)

**<font color=#1a73e8>作者：</font>** Serhii Zabolotnii  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce TRACE, a cross-domain engineering framework for trustworthy agentic AI in operationally critical domains. TRACE combines a four-layer reference architecture with an explicit classical-ML vs. LLM-validator split (L2a/L2b), a stateful orchestration-and-escalation policy (L3), and bounded human supervision (L4); a metrologically grounded trust-metric suite mapped to GUM/VIM/ISO 17025; and a Model-Parsimony principle quantified by the Computational Parsimony Ratio (CPR). Three instantiations--clinical decision support, industrial multi-domain operations, and a judicial AI assistant--transfer the samearchitecture and metrics across principally different governance contexts. The L2a/L2b separation makes the use of large language models a deliberate design decision rather than an architectural default, with parsimony quantified through CPR. TRACE introduces CPR as a first-class design principle in trustworthy-AI engineering.

---


### 106. [SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems](https://arxiv.org/abs/2605.03842)

**<font color=#1a73e8>作者：</font>** Yibang Tang, Yifan Yang, Jingyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-phase decisions. Existing methods either decompose the problem into isolated sub-tasks to guarantee responsiveness at the cost of global optimality, or rely on computationally expensive global optimization models that are unsuitable for dynamic industrial environments. To bridge this gap, we propose SOAR, a unified Deep Reinforcement Learning framework for real-time joint optimization. SOAR transforms order allocation and robot scheduling into a unified process by utilizing soft order allocations as observations. We formulate this as an Event-Driven Markov Decision Process, enabling the agent to perform simultaneous scheduling in response to asynchronous system events. Technically, we employ a Heterogeneous Graph Transformer to encode the warehouse state and integrate phased domain knowledge. Additionally, we incorporate a reward shaping strategy to address sparse feedback in long-horizon tasks. Extensive experiments on synthetic and real-world industrial datasets, in collaboration with Geekplus, demonstrate that SOAR reduces global makespan by 7.5\% and average order completion time by 15.4\% with sub-100ms latency. Furthermore, sim-to-real deployment confirms its practical viability and significant performance gains in production environments. The code is available at this https URL.

---


### 107. [Quantifying the human visual exposome with vision language models](https://arxiv.org/abs/2605.03863)

**<font color=#1a73e8>作者：</font>** Christian Rominger, Andreas R. Schwerdtfeger, Malay Gaherwar Singh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The visual environment is a fundamental yet unquantified determinant of mental health. While the concept of the environmental exposome is well established, current methods rely on coarse geospatial proxies or biased self reports, failing to capture the first person visual context of daily life. We addressed this gap by coupling ecological momentary assessment with vision language models (VLMs) to quantify the semantic richness of human visual experience. Across 2674 participant generated photographs, VLM derived estimates of greenness robustly predicted momentary affect and chronic stress, consistent with established benchmarks. We then developed a semi autonomous large language model (LLM) based pipeline that mined over seven million scientific publications to extract nearly 1000 environmental features empirically linked to mental health. When applied to real world imagery, up to 33 percent of VLM extracted context ratings significantly correlated with affect and stress. These findings establish a scalable objective paradigm for visual exposomics, enabling high throughput decoding of how the visible world is associated with mental health.

---


### 108. [On Adaptivity in Zeroth-Order Optimization](https://arxiv.org/abs/2605.03869)

**<font color=#1a73e8>作者：</font>** Hassan Dbouk, Nidham Gazagnadou, Matthias Reisser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the effectiveness of adaptive zeroth-order (ZO) optimization for memory-constrained fine-tuning of large language models (LLMs). Contrary to prior claims, we show that adaptive ZO methods such as ZO-Adam offer no convergence advantage over well-tuned ZO-SGD, while incurring significant memory overhead. Our analysis reveals that in high dimensions, ZO gradients lack coordinate-wise heterogeneity, rendering adaptive mechanisms memory inefficient. Leveraging this insight, we propose MEAZO, a memory-efficient adaptive ZO optimizer that tracks only a single scalar for global step size adaptation. We support our method with theoretical convergence guarantees under standard assumptions. Experiments across multiple LLM families and tasks demonstrate that MEAZO matches ZO-Adam's performance with the memory footprint of ZO-SGD. Additional experiments on synthetic quadratic problems and LLM fine-tuning further demonstrate MEAZO's enhanced robustness to step size choices, particularly in grouped or block-structured optimization settings.

---


### 109. [EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics](https://arxiv.org/abs/2605.03871)

**<font color=#1a73e8>作者：</font>** Shuyue Stella Li, Rui Xin, Teng Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models encode substantial evaluative knowledge from pretraining, yet current post-training methods rely on external supervision (human annotations, proprietary models, or scalar reward models) to produce reward signals. Each imposes a ceiling. Human judgment cannot supervise capabilities beyond its own, proprietary APIs create dependencies, and verifiable rewards cover only domains with ground-truth answers. Self-improvement from a model's own evaluative capacity is a reward source that scales with the model itself, yet remains largely untapped by current methods. We introduce EVOLM, a post-training method that structures this capacity into explicit discriminative rubrics and uses them as training signal. EVOLM trains two capabilities within a single language model in alternation: (1) a rubric generator producing instance-specific evaluation criteria optimized for discriminative utility, which maximizes a small frozen judge's ability to distinguish preferred from dispreferred responses; and (2) a policy trained using those rubric-conditioned scores as reward. All preference signals are constructed from the policy's own outputs via temporal contrast with earlier checkpoints, requiring no human annotation or external supervision. EVOLM trains a Qwen3-8B model to generate rubrics that outperform GPT-4.1 on RewardBench-2 by 25.7%. The co-trained policy achieves 69.3% average on the OLMo3-Adapt suite, outperforming policies trained with GPT-4.1 prompted rubrics by 3.9% and with the state-of-the-art 8B reward model SkyWork-RM by 16%. Overall, EVOLM demonstrates that structuring a model's evaluative capacity into co-evolving discriminative rubrics enables self-improvement without external supervision.

---


### 110. [Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework](https://arxiv.org/abs/2605.03882)

**<font color=#1a73e8>作者：</font>** Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.

---


### 111. [QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs](https://arxiv.org/abs/2605.03884)

**<font color=#1a73e8>作者：</font>** Pratik Honavar, Tejpratap GVSL  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.

---


### 112. [CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing](https://arxiv.org/abs/2605.03903)

**<font color=#1a73e8>作者：</font>** Zhipeng Xu, Junhao Ji, Zulong Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) have recently shown strong performance on Optical Character Recognition (OCR) tasks, demonstrating their promising capability in document literacy. However, their effectiveness in real-world applications remains underexplored, as existing benchmarks adopt task scopes misaligned with practical applications and assume homogeneous acquisition conditions. To address this gap, we introduce CC-OCR V2, a comprehensive and challenging OCR benchmark tailored to real-world document processing. CC-OCR V2 focuses on practical enterprise document processing tasks and incorporates hard and corner cases that are critical yet underrepresented in prior benchmarks, covering 5 major OCR-centric tracks: text recognition, document parsing, document grounding, key information extraction, and document question answering, comprising 7,093 high-difficulty samples. Extensive experiments on 14 advanced LMMs reveal that current models fall short of real-world application requirements. Even state-of-the-art LMMs exhibit substantial performance degradation across diverse tasks and scenarios. These findings reveal a significant gap between performance on current benchmarks and effectiveness in real-world applications. We release the full dataset and evaluation toolkit at this https URL.

---


### 113. [Steer Like the LLM: Activation Steering that Mimics Prompting](https://arxiv.org/abs/2605.03907)

**<font color=#1a73e8>作者：</font>** Geert Heyman, Frederik Vandeputte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can be steered at inference time through prompting or activation interventions, but activation steering methods often underperform compared to prompt-based approaches. We propose a framework that formulates prompt steering as a form of activation steering and investigates whether distilling successful prompt steering behavior into simpler, interpretable models can close this gap. Our analysis reveals that popular activation steering methods are not faithful to the mechanics of prompt steering, which applies strong interventions on some tokens while barely affecting others. Based on these insights, we introduce Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions. Experiments on three steering benchmarks across multiple language models show that PSR models outperform existing activation steering methods, especially when controlling for high-coherence completions, and also compare favorably to prompting on AxBench and persona steering.

---


### 114. [Atomic Fact-Checking Increases Clinician Trust in Large Language Model Recommendations for Oncology Decision Support: A Randomized Controlled Trial](https://arxiv.org/abs/2605.03916)

**<font color=#1a73e8>作者：</font>** Lisa C. Adams, Linus Marx, Erik Thiele Orberg 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question: Does atomic fact-checking, which decomposes AI treatment recommendations into individually verifiable claims linked to source guideline documents, increase clinician trust compared to traditional explainability approaches?
Findings: In this randomized trial of 356 clinicians generating 7,476 trust ratings, atomic fact-checking produced a large effect on trust (Cohen's d = 0.94), increasing the proportion of clinicians expressing trust from 26.9% to 66.5%. Traditional transparency mechanisms showed a dose-response gradient of improvement over baseline (d = 0.25 to 0.50).
Meaning: Decomposing AI recommendations into individually verifiable claims linked to source guidelines produces substantially higher clinician trust than traditional explainability approaches in high-stakes clinical decisions.

---


### 115. [StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning](https://arxiv.org/abs/2605.03927)

**<font color=#1a73e8>作者：</font>** Xiaowen Sun, Matthias Kerzel, Mengdi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.

---


### 116. [The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models](https://arxiv.org/abs/2605.03936)

**<font color=#1a73e8>作者：</font>** Daniel Drucker, Kyle Mahowald  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conceptual analysis -- proposing definitions and refining them through counterexamples -- is central to philosophical methodology. We study whether language models can perform this task through iterated analysis and repair chains: one model instance generates counterexamples to a proposed definition, another repairs the definition, and the process repeats. Across 20 concepts and thousands of counterexample-repair cycles, we find that, although many LM-generated counterexamples are judged invalid by both expert humans and an LM judge, the LM judge accepts roughly twice as many as humans do. Nonetheless, per-item validity judgments are moderately consistent across humans and between humans and the LM. We further find that extended iteration produces increasingly verbose definitions without improving accuracy. We also see that some concepts resist stable definitions in general. These findings suggest that while LMs can engage in philosophical reasoning, the counterexample-repair loop hits diminishing returns quickly and could be a fruitful test case for evaluating whether LMs can sustain high-level iterated philosophical reasoning.

---


### 117. [A Benchmark for Interactive World Models with a Unified Action Generation Framework](https://arxiv.org/abs/2605.03941)

**<font color=#1a73e8>作者：</font>** Jianjie Fang, Yingshan Lei, Qin Wan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at this http URL.

---


### 118. [UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning](https://arxiv.org/abs/2605.03950)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Yun Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.

---


### 119. [Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning](https://arxiv.org/abs/2605.03968)

**<font color=#1a73e8>作者：</font>** Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.

---


### 120. [Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments](https://arxiv.org/abs/2605.03971)

**<font color=#1a73e8>作者：</font>** Hao Mi, Qiang Sheng, Shaofei Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.

---


### 121. [From Intent to Execution: Composing Agentic Workflows with Agent Recommendation](https://arxiv.org/abs/2605.03986)

**<font color=#1a73e8>作者：</font>** Kishan Athrey, Ramin Pishehvar, Brian Riordan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Systems (MAS) built using AI agents fulfill a variety of user intents that may be used to design and build a family of related applications. However, the creation of such MAS currently involves manual composition of the plan, manual selection of appropriate agents, and manual creation of execution graphs. This paper introduces a framework for the automated creation of multi-agent systems which replaces multiple manual steps with an automated framework. The proposed framework consists of software modules and a workflow to orchestrate the requisite task- specific application. The modules include: an LLM-derived planner, a set of tasks described in natural language, a dynamic call graph, an orchestrator for map agents to tasks, and an agent recommender that finds the most suitable agent(s) from local and global agent registries. The agent recommender uses a two-stage information retrieval (IR) system comprising a fast retriever and an LLM-based re-ranker. We implemented a series of experiments exploring the choice of embedders, re- rankers, agent description enrichment, and supervising critique agent. We benchmarked this system end-to-end, evaluating the combination of planning, agent selection, and task completion, with our proposed approach. Our experimental results show that our approach outperforms the state-of-the- art in terms of the recall rate and is more robust and scalable compared to previous approaches. The critique agent holistically reevaluates both agent and tool recommendations against the overall plan. We show that the inclusion of the critique agent further enhances the recall score, proving that the comprehensive review and revision of task-based agent selection is an essential step in building end-to-end multi-agent systems.

---


### 122. [An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](https://arxiv.org/abs/2605.03989)

**<font color=#1a73e8>作者：</font>** Dutao Zhang, Tian Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation systems often assume that one fixed retrieval pipeline is sufficient across heterogeneous tasks, yet factoid question answering, multi-hop reasoning, and scientific verification exhibit different retrieval preferences. We present Experience-RAG Skill, an agent-oriented pluggable retrieval orchestration layer positioned between the agent and the retriever pool. The proposed skill analyzes the current scene, consults an experience memory, selects an appropriate retrieval strategy, and returns structured evidence to the agent. Under a fixed candidate pool, Experience-RAG Skill achieves an overall nDCG@10 of 0.8924 on BeIR/nq, BeIR/hotpotqa, and BeIR/scifact, outperforming fixed single-retriever baselines and remaining competitive with Adaptive-RAG-style routing. The results suggest that retrieval strategy selection can be productively encapsulated as a reusable agent skill rather than being hard-coded in the upper workflow.

---


### 123. [EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage](https://arxiv.org/abs/2605.03998)

**<font color=#1a73e8>作者：</font>** Richard J. Young, Alice M. Matthews  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emergency department triage assigns patients an acuity score that determines treatment priority, and clinical evidence documents persistent gender disparities in human acuity assessment. As hospitals pilot large language models (LLMs) as triage decision support, a critical question is whether these models reproduce or mitigate known biases. We present EQUITRIAGE, a fairness audit of LLM-based ESI assignment evaluating five models (Gemini-3-Flash, Nemotron-3-Super, DeepSeek-V3.1, Mistral-Small-3.2, GPT-4.1-Nano) across 374,275 evaluations on 18,714 MIMIC-IV-ED vignettes under four prompt strategies. Of 9,368 originals, 9,346 are paired with a gender-swapped counterfactual. All five models produced flip rates above a pre-registered 5% threshold (9.9% to 43.8%). Two showed directional female undertriage (DeepSeek F/M 2.15:1, Gemini 1.34:1); two were near-parity; one had high sensitivity with weak male-direction asymmetry. DeepSeek's directional bias coexisted with a low outcome-linked calibration gap (0.013 against MIMIC-IV admission), a Chouldechova-style dissociation between within-group calibration and between-pair counterfactual invariance. Demographic blinding reduced Gemini's flip rate to 0.5%; an age-preserving blind variant left DeepSeek with residual F/M 1.25, implicating age as a residual channel. Chain-of-thought prompting degraded accuracy for all five models. A two-model ablation reveals opposite underlying mechanisms for the same directional phenotype: in Gemini the signal is emergent in the combined name+gender swap, while in DeepSeek the gender token alone carries it. EQUITRIAGE shows that group parity, counterfactual invariance, and gender calibration are distinct fairness properties, that intervention effectiveness is model-dependent, and that per-model counterfactual auditing should precede clinical deployment.

---


### 124. [Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems](https://arxiv.org/abs/2605.04018)

**<font color=#1a73e8>作者：</font>** Yilun Zhao, Jinbiao Wei, Tingyu Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning-intensive retrieval aims to surface evidence that supports downstream reasoning rather than merely matching topical similarity. This capability is increasingly important for agentic search systems, where retrievers must provide complementary evidence across iterative search and synthesis. However, existing work remains limited on both evaluation and training: benchmarks such as BRIGHT provide narrow gold sets and evaluate retrievers in isolation, while synthetic training corpora often optimize single-passage relevance rather than evidence portfolio construction. We introduce BRIGHT-Pro, an expert-annotated benchmark that expands each query with multi-aspect gold evidence and evaluates retrievers under both static and agentic search protocols. We further construct RTriever-Synth, an aspect-decomposed synthetic corpus that generates complementary positives and positive-conditioned hard negatives, and use it to LoRA fine-tune RTriever-4B from Qwen3-Embedding-4B. Experiments across lexical, general-purpose, and reasoning-intensive retrievers show that aspect-aware and agentic evaluation expose behaviors hidden by standard metrics, while RTriever-4B substantially improves over its base model.

---


### 125. [Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours](https://arxiv.org/abs/2605.04019)

**<font color=#1a73e8>作者：</font>** Raja Sekhar Rao Dheekonda, Will Pearce, Nick Landers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are entering critical domains like healthcare, finance, and defense, yet remain vulnerable to adversarial attacks. While AI red teaming is a primary defense, current approaches force operators into manual, library-specific workflows. Operators spend weeks hand-crafting workflows - assembling attacks, transforms, and scorers. When results fall short, workflows must be rebuilt. As a result, operators spend more time constructing workflows than probing targets for security and safety vulnerabilities.
We introduce an AI red teaming agent built on the open-source Dreadnode SDK. The agent creates workflows grounded in 45+ adversarial attacks, 450+ transforms, and 130+ scorers. Operators can probe multi-agent systems, multilingual, and multimodal targets, focusing on what to probe rather than how to implement it.
We make three contributions: 1. Agentic interface. Operators describe goals in natural language via the Dreadnode TUI (Terminal User Interface). The agent handles attack selection, transform composition, execution, and reporting, letting operators focus on red teaming. Weeks compress to hours. 2. Unified framework. A single framework for probing traditional ML models (adversarial examples) and generative AI systems (jailbreaks), removing the need for separate libraries. 3. Llama Scout case study. We red team Meta Llama Scout and achieve an 85% attack success rate with severity up to 1.0, using zero human-developed code

---


### 126. [Stayin' Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data](https://arxiv.org/abs/2605.04029)

**<font color=#1a73e8>作者：</font>** Simret Araya Gebreegziabher, Allison E Sproul, Yinuo Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current human-AI alignment and evaluation methods for large language models (LLMs) often rely on preference signals collected immediately after an interaction. This practice implicitly treats preference as static, even though many LLM-mediated decisions unfold over time and may be re-evaluated differently after real-world consequences and observed outcomes. Therefore, we argue for a methodological shift from single-moment preference elicitation to longitudinal, context-situated alignment measurement. We present a methodological framework for collecting temporally grounded alignment signals by combining (1) in-situ preference capture, (2) context-triggered follow-up preference reflection, and (3) privacy-preserving behavioral traces that help interpret preference change. As an instantiation of this methodology, we introduce BITE, a browser-based system that detects consequential LLM interactions, prompts reflection across later decision points, and supports progressive, user-controlled consent for sharing behavioral data. Through a two week longitudinal deployment study with 8 participants, our approach surfaced differences between immediate and later user preferences in accuracy, relevance and other dimensions of the LLM output. Our findings highlight the limitations of single-moment preference datasets and underscore the importance of longitudinal methods for alignment evaluation in everyday use.

---


### 127. [OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories](https://arxiv.org/abs/2605.04036)

**<font color=#1a73e8>作者：</font>** Yuwen Du, Rui Ye, Shuo Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet their development remains dominated by industrial giants. The typical industry recipe involves a highly resource-intensive pipeline spanning pre-training, continual pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). In this report, we show that when fueled with informative and high-difficulty trajectories, a simple SFT approach could be surprisingly powerful for training frontier search agents. By introducing three simple data synthesis modifications: scaling knowledge graph size for richer exploration, expanding the tool set size for broader functionality, and strict low-step filtering, we establish a stronger baseline. Trained on merely 10.6k data points, our OpenSeeker-v2 achieves state-of-the-art performance across 4 benchmarks (30B-sized agents with ReAct paradigm): 46.0% on BrowseComp, 58.1% on BrowseComp-ZH, 34.6% on Humanity's Last Exam, and 78.0% on xbench, surpassing even Tongyi DeepResearch trained with heavy CPT+SFT+RL pipeline, which achieves 43.4%, 46.7%, 32.9%, and 75.0%, respectively. Notably, OpenSeeker-v2 represents the first state-of-the-art search agent within its model scale and paradigm to be developed by a purely academic team using only SFT. We are excited to open-source the OpenSeeker-v2 model weights and share our simple yet effective findings to make frontier search agent research more accessible to the community.

---


### 128. [Safety and accuracy follow different scaling laws in clinical large language models](https://arxiv.org/abs/2605.04039)

**<font color=#1a73e8>作者：</font>** Sebastian Wind, Tri-Thien Nguyen, Jeta Sopa 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical LLMs are often scaled by increasing model size, context length, retrieval complexity, or inference-time compute, with the implicit expectation that higher accuracy implies safer behavior. This assumption is incomplete in medicine, where a few confident, high-risk, or evidence-contradicting errors can matter more than average benchmark performance. We introduce SaFE-Scale, a framework for measuring how clinical LLM safety changes across model scale, evidence quality, retrieval strategy, context exposure, and inference-time compute. To instantiate this framework, we introduce RadSaFE-200, a Radiology Safety-Focused Evaluation benchmark of 200 multiple-choice questions with clinician-defined clean evidence, conflict evidence, and option-level labels for high-risk error, unsafe answer, and evidence contradiction. We evaluated 34 locally deployed LLMs across six deployment conditions: closed-book prompting (zero-shot), clean evidence, conflict evidence, standard RAG, agentic RAG, and max-context prompting. Clean evidence produced the strongest improvement, increasing mean accuracy from 73.5% to 94.1%, while reducing high-risk error from 12.0% to 2.6%, contradiction from 12.7% to 2.3%, and dangerous overconfidence from 8.0% to 1.6%. Standard RAG and agentic RAG did not reproduce this safety profile: agentic RAG improved accuracy over standard RAG and reduced contradiction, but high-risk error and dangerous overconfidence remained elevated. Max-context prompting increased latency without closing the safety gap, and additional inference-time compute produced only limited gains. Worst-case analysis showed that clinically consequential errors concentrated in a small subset of questions. Clinical LLM safety is therefore not a passive consequence of scaling, but a deployment property shaped by evidence quality, retrieval design, context construction, and collective failure behavior.

---


### 129. [Large Language Models are Universal Reasoners for Visual Generation](https://arxiv.org/abs/2605.04040)

**<font color=#1a73e8>作者：</font>** Sucheng Ren, Chen Chen, Zhenbang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation has advanced rapidly with diffusion models, progressing from CLIP and T5 conditioning to unified systems where a single LLM backbone handles both visual understanding and generation. Despite the architectural unification, these systems frequently fail to faithfully align complex prompts during synthesis, even though they remain highly accurate at verifying whether an image satisfies those same prompts. We formalize this as the \emph{understanding-generation gap} and propose UniReasoner, a framework that leverages the LLM as a universal reasoner to convert its understanding strength into direct generation guidance. Given a prompt, the LLM first produces a coarse visual draft composed of discrete vision tokens. It then performs a self-critique by evaluating the draft for prompt consistency, producing a grounded textual evaluation that pinpoints what needs to be corrected. Finally, a diffusion model is conditioned jointly on the prompt, the visual draft, and the evaluation, ensuring that generation is guided by explicit corrective signals. Each signal addresses a limitation of the other: the draft provides a concrete, scene-level anchor that reduces under-specification in text-only conditioning, while the evaluation turns verification into grounded, actionable constraints that correct omissions, hallucinations, and relational errors. Experiments show that UniReasoner improves compositional alignment and semantic faithfulness under the same diffusion backbone while maintaining image quality, demonstrating a practical way to exploit LLM reasoning to close the understanding-generation gap.

---


### 130. [Audio-Visual Intelligence in Large Foundation Models](https://arxiv.org/abs/2605.04045)

**<font color=#1a73e8>作者：</font>** You Qin, Kai Liu, Shengqiong Wu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Intelligence (AVI) has emerged as a central frontier in artificial intelligence, bridging auditory and visual modalities to enable machines that can perceive, generate, and interact in the multimodal real world. In the era of large foundation models, joint modeling of audio and vision has become increasingly crucial, i.e., not only for understanding but also for controllable generation and reasoning across dynamic, temporally grounded signals. Recent advances, such as Meta MovieGen and Google Veo-3, highlight the growing industrial and academic focus on unified audio-vision architectures that learn from massive multimodal data. However, despite rapid progress, the literature remains fragmented, spanning diverse tasks, inconsistent taxonomies, and heterogeneous evaluation practices that impede systematic comparison and knowledge integration. This survey provides the first comprehensive review of AVI through the lens of large foundation models. We establish a unified taxonomy covering the broad landscape of AVI tasks, ranging from understanding (e.g., speech recognition, sound localization) to generation (e.g., audio-driven video synthesis, video-to-audio) and interaction (e.g., dialogue, embodied, or agentic interfaces). We synthesize methodological foundations, including modality tokenization, cross-modal fusion, autoregressive and diffusion-based generation, large-scale pretraining, instruction alignment, and preference optimization. Furthermore, we curate representative datasets, benchmarks, and evaluation metrics, offering a structured comparison across task families and identifying open challenges in synchronization, spatial reasoning, controllability, and safety. By consolidating this rapidly expanding field into a coherent framework, this survey aims to serve as a foundational reference for future research on large-scale AVI.

---


> [!TIP]
> 当前位于：**101-130**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-130**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
