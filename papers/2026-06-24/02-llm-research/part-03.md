# 🧠 大模型相关研究 | 2026年06月24日

> 本类共 **118** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-118**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-118**

---

### 101. [FlowPipe: LLM-Enhanced Conditional Generative Flow Networks for Data Preparation Pipeline Construction](https://arxiv.org/abs/2606.24679)

**<font color=#1a73e8>作者：</font>** Kunyu Ni, Lei Cao, Jie He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data preparation pipelines improve data quality in machine learning by transforming raw tables into learning-ready data through sequential cleaning and feature transformation operators. However, automatically constructing such pipelines is computationally difficult because operator sequences are combinatorial and end-to-end evaluation is expensive. Existing state-of-the-art (SOTA) Multi-DQN methods still face three key limitations: decoupled value estimators weaken long-horizon credit assignment, dataset context is only weakly injected into the policy, and exploration is inefficient in a sparse search space with many invalid states. To address these issues, we propose FlowPipe, a unified framework that formulates pipeline synthesis as conditional probabilistic flow generation over a directed acyclic graph. FlowPipe uses Conditional Generative Flow Networks (C-GFlowNets) with a Trajectory Balance objective to connect terminal validation rewards with early pipeline decisions. It further introduces Deep Semantic Modulation through Feature-wise Linear Modulation (FiLM), allowing LLM-derived logical priors to condition the policy's internal activations according to dataset semantics. In addition, FlowPipe incorporates failure awareness into the flow objective to avoid invalid states and concentrate search on high-potential regions. Experiments on two benchmark suites with 74 real-world datasets show that FlowPipe outperforms SOTA baselines, improving accuracy by 11.96% on average and achieving 12.5x faster training convergence. Source code is available at this https URL.

---


### 102. [BioMedVR: Confusion-Aware Mixture-of-Prompt Experts for Biomedical Visual Reprogramming](https://arxiv.org/abs/2606.24740)

**<font color=#1a73e8>作者：</font>** Jiaxiang Liu, Tianxiang Hu, Juwei Guan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) such as CLIP have demonstrated strong generalization across natural-image domains. However, adapting these models to biomedical imaging is non-trivial: full-model fine-tuning is computationally expensive, while medical data are often scarce and exhibit subtle, fine-grained inter-class differences, making parameter-efficient adaptation particularly critical. Visual Reprogramming (VR) offers a parameter-efficient alternative by injecting learnable perturbations into the input space, but existing VR approaches for VLMs mainly focus on positive class prompts and overlook confusing negatives, leading to miscalibrated predictions in fine-grained medical scenarios. We present BioMedVR, the first VR-based framework for biomedical imaging, enabling few-shot adaptation of pretrained VLMs through compact learnable VR modules. To mitigate class confusion, we introduce a Confusion Minimization Mechanism that leverages LLM-generated confusion-aware attributes together with a Confusion-Suppression Loss to explicitly reduce false-positive alignment. Moreover, the designed Mixture-of-Prompt Experts combines a positive expert for main-class discrimination and a negative expert for confusion suppression, balanced via adaptive gating. Extensive experiments on 18 datasets, including 11 biomedical datasets and 7 natural image benchmarks, demonstrate that BioMedVR achieves superior accuracy and generalization, effectively bridging VR and VLMs in biomedical domains.

---


### 103. [Scaling Laws for Task-Specific LLM Distillation](https://arxiv.org/abs/2606.24747)

**<font color=#1a73e8>作者：</font>** Lavinia Ghita, Dhruv Desai, Ioana Boier  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong performance across a growing range of domains, yet their scale poses deployment challenges in applications where latency and cost constraints are critical. This paper derives empirical scaling laws for domain-specific LLM compression, quantifying how in-domain and general knowledge performance scale with dataset size, compression ratio, supervision format, and iterative pruning schedule. Using quantitative finance as our application domain, we compare logit-based and LoRA-based distillation under iterative structural pruning, introducing a blended chain-of-thought supervision loss that stabilizes KL-divergence distillation over reasoning traces. In-domain task quality degrades predictably under compression while general-knowledge benchmarks collapse well before the same point; supervision format is the key driver of this tradeoff, with chain-of-thought supervision actively recovering general knowledge that pruning erases. We release the headline dataset FinHeadlineMix, scaling law results, and practical recommendations to provide a reusable framework for domain-specific compression decisions.

---


### 104. [Can Scale Save Us From Plasticity Loss in Large Language Models?](https://arxiv.org/abs/2606.24752)

**<font color=#1a73e8>作者：</font>** J. Fernando Hernandez-Garcia, Tomás Figliolia, Beren Millidge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The loss of plasticity - the ability of a network to learn new information after having already learned older information - is a fundamental challenge in creating artificial neural networks capable of continual learning. Although this phenomenon has been known for decades, it has mostly been studied in older, relatively small architectures and rarely in natural-language domains. To determine whether loss of plasticity remains a problem in the modern transformer-based LLM paradigm, we study plasticity loss in GPT-style Transformer models trained on a multilingual continual learning problem. Consistent with prior work, we find evidence of plasticity loss across models ranging from 5M to 314M non-embedding parameters, as measured by deterioration on a held-out Vietnamese probing task. We further find that the onset of plasticity loss follows a predictable scaling law, growing sublinearly with model size. These results suggest that larger models may delay the measurable effects of plasticity loss, but that increasing parameter count alone is likely to be insufficient to completely prevent it. We also find evidence of plasticity loss under stationary multilingual training, challenging the view that the phenomenon is exclusive to continual learning with abrupt task changes. Overall, our results suggest that even large Transformer language models trained on natural-language will eventually lose the ability to efficiently adapt to new data after sufficiently long training, in both continual and stationary settings.

---


### 105. [UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving](https://arxiv.org/abs/2606.24759)

**<font color=#1a73e8>作者：</font>** Xiaowei Gao, Pengxiang Li, Yitai Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame or low-resolution inputs often miss small, distant, or partially occluded hazards, while language-centric driving models frequently provide limited grounded evidence for their explanations. To address this gap, we propose UniDrive, a unified visual-language and grounding framework for interpretable risk understanding in autonomous driving. UniDrive combines a temporal reasoning branch that models scene dynamics from multi-frame visual input with a high-resolution perception branch that preserves fine-grained spatial details from the latest frame. The two branches are integrated through a gated cross-attention fusion module, enabling dynamic context to be aligned with precise spatial evidence. Based on the fused representation, UniDrive jointly generates natural-language risk descriptions and grounded bounding-box outputs for risk objects. Experiments on the DRAMA-Reasoning benchmark show that UniDrive outperforms representative image-based and video-based baselines in both captioning and risk-object grounding. In particular, UniDrive achieves the best overall performance on the validation split and demonstrates clear advantages in small-object localization, zero-shot generalization to NuScenes and BDD100K, and human-rated interpretability and trustworthiness. These results suggest that explicitly combining temporal semantics and high-resolution perception provides a stronger foundation for interpretable and safety-oriented autonomous driving systems. The code is available at this https URL.

---


### 106. [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775)

**<font color=#1a73e8>作者：</font>** Wei Zhou, Xuanhe Zhou, Shaokun Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution. Despite this evolution, existing evaluations still benchmark agent memory mainly through end-to-end task success metrics (e.g., F1, BLEU), while treating the underlying system as a monolithic black box. As a result, critical system-level concerns, including operational costs, architectural trade-offs across memory modules, and robustness under dynamic knowledge updates, remain insufficiently explored. In this paper, we present a systematic experimental study of agent memory from a data management perspective. We propose an analytical framework that decomposes agent memory into four core modules: memory representation and storage, extraction, retrieval and routing, and maintenance. Under this framework, we evaluate 12 representative memory systems and two reference baselines across five benchmark workloads spanning 11 datasets. Our extensive end-to-end evaluation shows that no single architecture dominates across all scenarios; instead, effectiveness depends heavily on how well the memory structure aligns with the workload bottleneck. Furthermore, through fine-grained ablation studies, we quantify their individual effects on representation fidelity, retrieval precision, update correctness, and long-horizon stability. Finally, we reveal cost-performance trade-offs under realistic workloads, showing localized maintenance is more cost-efficient than global reorganization. Based on these findings, we identify promising directions towards building truly agent-native memory systems. The code is publicly available at this https URL.

---


### 107. [Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce](https://arxiv.org/abs/2606.24783)

**<font color=#1a73e8>作者：</font>** Filippos Ventirozos, Matthew Shardlow  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Commercial NLP treats the shopping chatbot as a recommender or a conversion tool: its job is to match a user to a catalogue entry and close a sale. We argue that the arrival of agent-native micro-payment rails (e.g., x402, AP2) changes what is scarce. When the buyer is an autonomous agent that can investigate exhaustively, the bottleneck is no longer matching products but acquiring trustworthy, decision-relevant information about them. We envision agentic e-commerce as a micro-transaction market for verified information: buyer agents spend fractions of a cent to progressively unlock seller- and reviewer-supplied data -- service histories, third-party test reports, bills of materials, audited sales and support metrics -- paid for a la carte under a freemium model, with reviewer trust scored reputationally. We sketch the architecture of such a market and argue that it rewards genuine product quality and yields truer competition than ranking-based storefronts. We then translate the vision into concrete NLP problems -- cost-optimal information acquisition, data pricing and negotiation, real-time entity resolution, grounded value exchange, and privacy-preserving persona modelling -- and argue that these, not chat fluency, deserve the field's attention.

---


### 108. [Grad Detect: Gradient-Based Hallucination Detection in LLMs](https://arxiv.org/abs/2606.24790)

**<font color=#1a73e8>作者：</font>** Anand Kamat, Daniel Blake, Brent M. Werness  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet they remain prone to generating hallucinations. Detecting these hallucinations is critical for deploying LLMs reliably in high-stakes applications. We present Grad Detect, a gradient-based approach for predicting hallucinations by analyzing layer-wise gradient patterns from a single forward-backward pass during inference. Our method shows that the internal gradient structure of a model carries rich information about the correctness of its output. This information is not accessible through output-level signals alone. We evaluate Grad Detect on several Q&A benchmarks across both hallucination detection and model abstention prediction, where it consistently outperforms confidence-based and sampling-based baselines. Through comprehensive layer ablation studies across all eleven models from four architectural families, we find that the final five layers concentrate over 97% of the discriminative gradient signal, enabling efficient deployment with minimal performance loss. Grad Detect provides a unified framework for predicting multiple dimensions of LLM reliability, offering strong predictive performance alongside interpretable insights into where and how model failures originate.

---


### 109. [EG-VQA: Benchmarking Verifiable Video Question Answering with Grounded Temporal Evidence](https://arxiv.org/abs/2606.24797)

**<font color=#1a73e8>作者：</font>** Linpeng Huang, Weixing Chen, Zexin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Video Large Language Models (Video-LLMs) have yielded promising performance on video question answering (VideoQA). Nevertheless, existing benchmarks are predominantly evaluated through answer correctness, while the grounding of predictions in relevant video evidence remains largely unexamined. This disconnect between answer generation and evidence understanding motivates the construction of the Evidence-Grounded Video Question Answering Benchmark (EG-VQA), an open-ended evaluation protocol in which each QA pair is explicitly annotated with supporting temporal evidence, thereby requiring joint reasoning and precise evidence localization. EG-VQA is comprised of 2,067 videos and 11,838 QA pairs with fine-grained evidence annotations. To evaluate predicted evidence, Evidence-Grounded F1 (EG-F1) is introduced as a unified metric in which temporal alignment and semantic consistency against ground-truth evidence are jointly measured. Experimental evaluation reveals that even strong proprietary models struggle to accurately ground their predictions, exposing a fundamental discrepancy between answer correctness and faithful evidence localization. To bridge this gap, EG-Reasoner, an evidence-grounded reasoning model trained with explicit supervision, is proposed. State-of-the-art performance is achieved among open-source models, with results competitive against proprietary systems, particularly pronounced gains are observed on reasoning-intensive tasks such as counterfactual questions. These findings demonstrate that scaling alone is insufficient for robust video understanding and that structured evidence supervision is essential for the development of more reliable and interpretable VideoQA systems.

---


### 110. [SHERLOC: Structured Diagnostic Localization for Code Repair Agents](https://arxiv.org/abs/2606.24820)

**<font color=#1a73e8>作者：</font>** Hovhannes Tamoyan, Sean Narenthiran, Erik Arakelyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents solve repository-level coding tasks through multi-turn tool use, but utilize half their budget on locating faults before editing. Dedicated localization frameworks have emerged, yet are still evaluated as file retrieval rather than actionable diagnosis, producing locations without the diagnostic context a repair agent needs. We introduce SHERLOC (Structured Hypothesis-driven Exploration and Reasoning for Localization), a training-free framework pairing a reasoning LLM with compact repository tools and self-recovery, without fine-tuning or multi-agent orchestration. SHERLOC reaches state-of-the-art localization across model scales: 84.33% accuracy@1 on SWE-Bench Lite and 81.27% recall@1 on SWE-Bench Verified; at ~30B parameters, it matches or outperforms other agentic methods. Injecting our locations and diagnostic findings into repair agents yields, on average, +5.95 pp resolve rate on SWE-Bench Verified while cutting localization and total tokens by 36.7% and 23.1%.

---


### 111. [Accuracy and Satisfaction in Multi-Turn LLM Dialogues for NFR Assessment](https://arxiv.org/abs/2606.24834)

**<font color=#1a73e8>作者：</font>** Ali Pourghasemi Fatideh, Wilder Baldwin, Maria Dhakal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based dialogue assistants have become mainstream tools for software developers, yet current evaluation benchmarks focus exclusively on functional correctness. This leaves a critical gap in assessing the quality and accuracy of these conversations when handling Non-Functional Requirements (NFRs), which are inherently vague, context-dependent, and involve many parts of a program. Evaluating how well these systems support collaborative reasoning about NFRs requires methods that go beyond single-turn accuracy to capture both the correctness of the system's outputs and the quality of the multi-turn interaction. In this paper, we investigate the accuracy and quality of multi-turn conversations between developers and an LLM-based agent in the domain of Health Insurance Portability and Accountability Act (HIPAA) regulatory compliance. We hired 49 programmers to interact with GitHub Copilot to assess 148 HIPAA-derived NFRs against the iTrust codebase, a system designed to comply with HIPAA regulations, across three dimensions: requirement satisfaction level, reasoning, and code localization. We find that developers tend to agree with LLM assessments, but accuracy against expert ground truth is low. We model user satisfaction and find that longer system responses and more information-providing turns negatively affect user satisfaction, whereas proactive interactions positively affect it. Our findings provide insights for designing LLM-based dialogue systems that support NFR assessment.

---


### 112. [Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System](https://arxiv.org/abs/2606.24839)

**<font color=#1a73e8>作者：</font>** Tian Zheng, Kai-Tai Hsu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic data analysis systems produce rich outputs, including code, numerical results, and verbal diagnostics. This makes them more challenging to evaluate than single-turn LLM responses. It is therefore necessary to distinguish genuine disagreement between an agent's output and a ground-truth answer from grading artifacts. We investigate how reliably automated graders assess such a system and what strategies improve grading quality by applying LAMBDA, a multi-agent data-analysis system, on 153 numerical QRData tasks from DSGym. We develop and evaluate a three-layer human-AI grading cascade: strict regex matching, LLM-based lenient grading, and snippet-based human inspection, which combines non-GenAI and GenAI strategies with different failure profiles. Both automated graders achieve 100% observed precision (0/70 false positives). The lenient grader's recall is 97% against human labels. A keyword-anchored extraction pipeline raises the strict grader's recall by 60 percentage points over a last-number heuristic; the lenient grader is architecturally parser-independent. An iterative nudge mechanism raises grading run success from 36% to 97% and lenient-pass rates from 16% to 46%; comparing nudging with and without original-question re-injection shows that re-injection offers no benefit, confirming the nudge as an answer template cue. We further observe in this case study that variable type is the task metadata field most consistently associated with grading pipeline dynamics and observed outcome grades.

---


### 113. [Matching Tasks to Objectives: Fine-Tuning and Prompt-Tuning Strategies for Encoder-Decoder Pre-trained Language Models](https://arxiv.org/abs/2606.24841)

**<font color=#1a73e8>作者：</font>** Ahmad Pouramini, Hesham Faili  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt-based learning has emerged as a dominant paradigm in natural language processing. This study explores the impact of diverse pre-training objectives on the performance of encoder-decoder pre-trained language models across generation and question answering tasks, with a focus on commonsense knowledge retrieval and completion. We highlight the benefits of incorporating multiple objectives during both pre-training and fine-tuning stages. We introduce the Match Task to Objective (MTO) framework and methods for determining the appropriate objective for a given task. This framework offers automated methods to prepare task-related data for adaptation through unsupervised training, based on the identified objective. In the fine-tuning stage, we design novel templates that align with the objectives of the pre-training and adaptation stages. When aligned with task requirements, these strategies can achieve a performance gain of over 120\% compared to conventional methods in few-shot settings. They significantly outperform related works in few-shot settings and exceed the baseline even in full-dataset scenarios. Furthermore, we extend this approach to include prompt-tuning methodologies, providing guidance for more effective soft prompt engineering and optimization. Our strategies significantly enhance prompt-tuning performance as well. These insights hold substantial value, precisely guiding the selection and optimization of models customized for specific tasks. Code is available at this https URL

---


### 114. [World Models in Pieces: Structural Certification for General Agents](https://arxiv.org/abs/2606.24842)

**<font color=#1a73e8>作者：</font>** Yikai Lu, Yifei Wu, Xinyu Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the big-world regime, agents cannot be universally capable and their ability is inevitably specialized across a world model in pieces. Consequently, standard uniform guarantees fail to distinguish between the understanding of critical bottlenecks and irrelevant failures. We first formalize this limitation by proving that general agents are not universal, rendering standard worst-case analysis uninformative. To overcome this, we introduce structural certification, a transition-local framework that maps bounded goal-conditioned performance to entry-wise guarantees on the agent's internal world model. Our main contribution is constructive. We provide algorithms that filter specific transitions using deep compositional goals and prove that a general agent on these goals has a structural world model with a $\mathcal{O}(1/n) + \mathcal{O}(\delta)$ error bound. Conversely, this bound is tight in the small-$\delta$ regime, whose existence is explicitly guaranteed by our certification. These results enable the certifiable deployment of general agents by localizing the specific transitions where long-horizon planning is reliable.

---


### 115. [IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation](https://arxiv.org/abs/2606.24849)

**<font color=#1a73e8>作者：</font>** Zixuan Li, Haokun Lin, Yicheng Xiao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multi-modal large language models (MLLMs) have achieved strong text-to-image generation quality, but still struggle with structure-aware prompt following, where object counts, spatial relations, attribute bindings, and coarse layouts must be preserved. We attribute this limitation in part to the entanglement of structural planning and appearance rendering within a single conditioning stream. To address this issue, we propose Implicit Visual Chain-of-Thought (IV-CoT), a latent visual reasoning framework for query-conditioned image generation. IV-CoT decomposes the visual conditioning queries into a structural-to-semantic cascade, where structural queries first form a latent visual plan and semantic queries then render appearance conditioned on this plan. To guide the structural queries, we introduce training-only sketch supervision, which encourages them to capture structure from sketches without requiring sketch extraction or intermediate decoding at inference time. IV-CoT performs implicit CoT reasoning in a single forward pass and achieves superior results on GenEval and T2I-CompBench. Visualizations and analyses demonstrate that the learned structural and semantic queries play complementary roles in structure-aware generation.

---


### 116. [OpenThoughts-Agent: Data Recipes for Agentic Models](https://arxiv.org/abs/2606.24855)

**<font color=#1a73e8>作者：</font>** Negin Raoof, Richard Zhuang, Marianna Nezhurina 等 50 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data for broadly capable agents. Existing open efforts such as SWE-Smith, SERA, and Nemotron-Terminal typically target a single benchmark, leaving open the question of how to train models that generalize across diverse agentic tasks. The OpenThoughts-Agent (OT-Agent) project addresses this gap with a fully open data curation pipeline for training agentic models. We conduct more than 100 controlled ablation experiments to systematically investigate each stage of the pipeline, yielding insights on the importance of task sources and diversity. We then assemble a training set of 100K examples from our pipeline and fine-tune Qwen3-32B on this dataset, which yields an average accuracy of 44.8% across seven agentic benchmarks and a 3.9 percentage point improvement over the strongest existing open data agentic model (Nemotron-Terminal-32B, 40.9%). Moreover, our training data exhibits strong scaling properties, outperforming alternative open datasets at every training set size in compute-controlled comparisons. We publicly release our training sets, data pipeline, experimental data, and models at this http URL to support future open research on agentic model training.

---


### 117. ["Zooming In" on Agentic Web Browsers as Assistive Technologies: A Case Study with a Low-Vision Technology Expert](https://arxiv.org/abs/2606.24870)

**<font color=#1a73e8>作者：</font>** Laura Colazzo, Giuseppe Anzillotti  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic Web Browsers (AWBs), powered by Large Language Models (LLMs), are emerging as autonomous systems capable of navigating the Web on behalf of users. Beyond enhancing productivity, they could also offer significant promise as Assistive Technologies (ATs) for visually-impaired individuals, transforming web interaction into a fluid conversational exchange. In this paper, we present a case study with a low-vision technology expert, examining how AWBs can support visually-impaired users in web navigation. The findings show that, despite the current limitations, the navigation experience is notably fluid and flexible, underscoring the strong potential of AWBs to enhance accessibility and reduce barriers in web interaction, with implications that may extend beyond accessibility to agentic UX more broadly.

---


### 118. [BenchX: Benchmarking AI Models for Cancer Detection and Localization with Demographic and Protocol Biases](https://arxiv.org/abs/2606.24883)

**<font color=#1a73e8>作者：</font>** Qi Chen, Wenxuan Li, Pedro R. A. S. Bassi 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has achieved remarkable success in medical imaging, but it is widely recognized that these models often perform inconsistently across real-world clinical settings. Such inconsistencies occur when patient demographics and imaging protocols vary, for example, in detecting small tumors, analyzing scans from different contrast phases, or evaluating patients of different ages or sexes. To quantify these inconsistencies, we develop a large-scale, open benchmark of 85,355 CT scans that systematically evaluates 12 tumor-detection AI models across tumor size, location, patient subgroup, and imaging protocol. We leverage large language models (LLMs) to extract and organize subgroup information from clinical data, which makes the analysis both scalable and reproducible. Our benchmark reveals that current state-of-the-art AI models, optimized for average accuracy, perform poorly in rare or underrepresented subgroups, such as young, female African Americans. However, collecting sufficient annotated data for these rare cases is often impractical. The benchmark provides a foundation for building more reliable and robust AI models for tumor detection and highlighting the need for rigorous, subgroup-level evaluation in medical imaging and computer vision. Datasets, code

---


> [!TIP]
> 当前位于：**101-118**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-118**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
