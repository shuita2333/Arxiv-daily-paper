# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 101. [AutoPKG: An Automated Framework for Dynamic E-commerce Product-Attribute Knowledge Graph Construction](https://arxiv.org/abs/2604.16950)

**<font color=#1a73e8>作者：</font>** Pollawat Hongwimol, Haoning Shang, Chutong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Product attribute extraction in e-commerce is bottlenecked by ontologies that are inconsistent, incomplete, and costly to maintain. We present AutoPKG, a multi-agent Large Language Model (LLM) framework that automatically constructs a Product-attribute Knowledge Graph (PKG) from multimodal product content. AutoPKG induces product types and type-specific attribute keys on demand, extracts attribute values from text and images, and consolidates updates through a centralized decision agent that maintains a globally consistent canonical graph. We also propose an evaluation protocol for dynamic PKGs that measures type and key validity, consolidation quality, and edge-level accuracy for value assertions after canonicalization. On a large real-world marketplace catalog dataset from Lazada (Alibaba), AutoPKG achieves up to 0.953 Weighted Knowledge Efficiency (WKE) for product types, 0.724 WKE for attribute keys, and 0.531 edge-level F1 for multimodal value extraction. Across three public benchmarks, our method improves edge-level exact-match F1 by 0.152 and yields a precision gain of 0.208 on the attribute extraction application. Online A/B tests show that AutoPKG-derived attributes increase Gross Merchandise Value (GMV) in Badge by 3.81 percent, in Search by 5.32 percent, and in Recommendation by 7.89 percent, supporting the practical value of AutoPKG in production.

---


### 102. [Open-TQ-Metal: Fused Compressed-Domain Attention for Long-Context LLM Inference on Apple Silicon](https://arxiv.org/abs/2604.16957)

**<font color=#1a73e8>作者：</font>** Sai Vegasena  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Open-TQ-Metal, the first implementation of fused compressed-domain attention on Apple Silicon, enabling 128K-context inference for Llama 3.1 70B on a single 64GB consumer Mac -- a configuration impossible with all existing inference frameworks. Open-TQ-Metal quantizes the KV cache to int4 on the fly and computes attention directly on the compressed representation via custom Metal compute shaders, eliminating all intermediate dequantization matrices. Across 330 experiments spanning two model families (Gemma 4 31B and Llama 3.1 70B), the fused sdpa_int4 kernel achieves 48x attention speedup at 128K context over the dequantize-then-attend baseline, reduces KV cache memory from 40 GB to 12.5 GB (3.2x compression), and maintains identical top-1 token predictions to FP16 inference. We further provide the first cross-architecture analysis of KV cache quantization methods, revealing that the attention scale factor -- not model size -- determines whether angular quantization schemes like PolarQuant succeed or fail, with Gemma 4's attn_scale=1.0 amplifying directional error 25-100x more than Llama's standard 1/sqrt(d) scaling.

---


### 103. [Self-Reasoning Agentic Framework for Narrative Product Grid-Collage Generation](https://arxiv.org/abs/2604.16958)

**<font color=#1a73e8>作者：</font>** Minyan Luo, Yuxin Zhang, Yifei Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Narrative-driven product photography has become a prevalent paradigm in modern marketing, as coherent visual storytelling helps convey product value and establishes emotional engagement with consumers. However, existing image generation methods do not support structured narrative planning or cross-panel coordination, often resulting in weak storytelling and visual incoherence. In practice, narrative product photography is commonly presented as multi-grid collages, where multiple views or scenes jointly communicate a product narrative. To ensure visual consistency across grids and aesthetic harmony of the overall composition, we generate the collage as a single unified image rather than composing independently synthesized panels. We propose a self-reasoning agentic framework for narrative product grid collage generation. Given a product packshot and its name, the system first constructs a Product Narrative Framework that explicitly represents the product's identity, usage context, and situational environment, and translates it into complementary grids governed by a shared visual style. Constraint-aware prompts are then compiled and fed to a generation model that synthesizes the collage jointly. The generated output is evaluated on both content validity and photography quality, with explicit gates determining whether to proceed or refine. When evaluation fails, the system performs failure attribution and applies targeted refinement, enabling progressive improvement through iterative self-reflection. Experiments demonstrate that our framework consistently improves aesthetic quality, narrative richness, and visual coherence, compared to direct prompting baselines.

---


### 104. [MCPO: Mastery-Consolidated Policy Optimization for Large Reasoning Models](https://arxiv.org/abs/2604.16972)

**<font color=#1a73e8>作者：</font>** Zhaokang Liao, Yingguo Gao, Yi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising approach to improve the reasoning abilities of Large Language Models (LLMs). Among RLVR algorithms, Group Relative Policy Optimization (GRPO) and its variants have demonstrated strong performance and high training efficiency. However, GRPO-style objectives exhibit two issues on high accuracy prompts including mastered prompts (rollout accuracy =1) and majority-correct prompts (rollout accuracy in (0.5,1)). For mastered prompts, group-relative advantages vanish, yielding no training signal and unconstrained policy drift that can cause forgetting. For majority-correct prompts, the induced query weight shrinks as accuracy increases, weakening consolidation from partial correctness to mastery. To alleviate this, we propose Mastery-Consolidated Policy Optimization (MCPO), which introduces (i) a hinge-KL regularizer applied exclusively to mastered prompts to bound harmful policy drift between successive gradient steps, and (ii) a weighting mechanism that prioritizes majority-correct prompts to better allocate optimization effort. Extensive experiments across three mathematical benchmarks demonstrate that MCPO consistently improves pass@1 performance. Counter-intuitively, rather than restricting exploration, MCPO boosts pass@k metrics, indicating that mastery consolidation further catalyzes solution diversity.

---


### 105. [DOSE: Data Selection for Multi-Modal LLMs via Off-the-Shelf Models](https://arxiv.org/abs/2604.16979)

**<font color=#1a73e8>作者：</font>** Biao Wu, Yiwu Zhong, Meng Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality and diverse multimodal data are essential for improving vision-language models (VLMs), yet existing datasets often contain noisy, redundant, and poorly aligned samples. To address these problems, data filtering is commonly used to enhance the efficiency and performance of multimodal learning, but it introduces extra computational cost because filtering models are usually trained on the same data they are meant to screen. To reduce this cost, we study DOSE, which explores whether off-the-shelf pretrained models that have never seen the target data can be used to select training samples for larger and stronger multimodal models without any task-specific training. Even without fine-tuning, these models can effectively assess text quality and image-text alignment to guide data selection. Based on this, we build a joint quality-alignment distribution and apply adaptive weighted sampling to select informative samples while maintaining long-tail diversity. This approach enhances data diversity, enabling models trained on DOSE-filtered data to match or surpass those trained on the full dataset on standard VQA and math benchmarks. Extensive experiments demonstrate its effectiveness, efficiency, and scalability.

---


### 106. [Evaluating Multimodal LLMs for Inpatient Diagnosis: Real-World Performance, Safety, and Cost Across Ten Frontier Models](https://arxiv.org/abs/2604.16980)

**<font color=#1a73e8>作者：</font>** Bruce A. Bassett, Amy Rouillard, Sitwala Mundia 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Large language models (LLMs) are increasingly proposed for diagnostic support, but few evaluations use real-world multimodal inpatient data, particularly in low and middle-income country (LMIC) public hospitals.
Methods: We conducted VALID, a retrospective evaluation of 539 multimodal inpatient cases from a tertiary public hospital in South Africa. Inputs included radiology imaging (CT, MRI, CXR) and reports, laboratory results, clinical notes, and vital signs. Expert panels adjudicated 300 cases (balanced and discordant subsets) to establish ground truth diagnoses, differentials, and reasoning. Ten multimodal LLMs generated zero-shot outputs. A calibrated three-model LLM Jury scored all outputs and routine ward diagnoses across diagnostic accuracy, differential quality, reasoning, and patient safety (>10,000 evaluations). Primary outcomes were composite scores ($S_3$, $S_4$) and win rates.
Results: (i) LLM performance was tightly clustered (<15% variation) despite large cost differences; low-cost models performed comparably to top models. (ii) All LLMs significantly outperformed routine ward diagnoses on average diagnostic and safety scores. (iii) Top performance was achieved by GPT-5.1, followed by Gemini models. (vi) Adding radiology reports improved performance by 6%. (v) Diagnostic and reasoning scores were highly correlated ($\rho = 0.85$). (vi) Output rates varied (65-100%) due to input constraints. Results were robust across subsets and evaluation design.
Conclusions: Across a real-world LMIC dataset, multimodal LLMs showed similar diagnostic performance despite large cost differences and outperformed routine care on average safety metrics. Affordability, robustness, and deployment constraints may outweigh marginal performance differences in LMIC settings.

---


### 107. [In-Context Learning Under Regime Change](https://arxiv.org/abs/2604.16988)

**<font color=#1a73e8>作者：</font>** Carson Dudley, Yutong Bi, Xiaofeng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-stationary sequences arise naturally in control, forecasting, and decision-making. The data-generating process shifts at unknown times, and models must detect the change, discard or downweight obsolete evidence, and adapt to new dynamics on the fly. Transformer-based foundation models increasingly rely on in-context learning for time series forecasting, tabular prediction, and continuous control. As these models are deployed in non-stationary environments, understanding their ability to detect and adapt to regime shifts is important. We formalize this as an in-context change-point detection problem and formally establish the existence of transformer models that solve this problem. Our construction demonstrates that model complexity, in layers and parameters, depends on the level of information available about the change-point location, from no knowledge to knowing exact timing. We validate our results with experiments on synthetic linear regression and linear dynamical systems, where trained transformers match the performance of optimal baselines across information levels. We also show that encoding and incorporating changepoint knowledge indeed improves the real-world performance of a pretrained foundation models on infectious disease forecasting and on financial volatility forecasting around Federal Open Market Committee (FOMC) announcements without retraining, demonstrating practical applicability to real-world regime changes.

---


### 108. [Bolzano: Case Studies in LLM-Assisted Mathematical Research](https://arxiv.org/abs/2604.16989)

**<font color=#1a73e8>作者：</font>** Jan Grebík, Pavel Hubáček, Martin Koutecký 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report new results on six problems in mathematics and theoretical computer science, produced with the assistance of Bolzano, an open-source multi-agent LLM system. Bolzano orchestrates rounds of interaction between parallel prover agents and a verifier agent while maintaining a persistent knowledge base that is carried across rounds. Classified using the significance-autonomy taxonomy of Feng et al., four of the six results reach the level of publishable research, and three of the six were produced essentially autonomously by Bolzano. Our results provide evidence that LLMs can contribute meaningfully to mathematical research, complementing recent reports by Bubeck et al., Woodruff et al., and others.

---


### 109. [SPS: Steering Probability Squeezing for Better Exploration in Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2604.16995)

**<font color=#1a73e8>作者：</font>** Yifu Huo, Chenglong Wang, Ziming Zhu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a promising paradigm for training reasoning-oriented models by leveraging rule-based reward signals. However, RL training typically tends to improve single-sample success rates (i.e., Pass@1) while offering limited exploration of diverse reasoning trajectories, which is crucial for multi-sample performance (i.e., Pass@k). Our preliminary analysis reveals that this limitation stems from a fundamental squeezing effect, whereby probability mass is excessively concentrated on a narrow subset of high-reward trajectories, restricting genuine exploration and constraining attainable performance under RL training. To address this issue, in this work, we propose Steering Probability Squeezing (SPS), a training paradigm that interleaves conventional RL with inverse reinforcement learning (IRL). SPS treats on-policy rollouts as demonstrations and employs IRL to explicitly reshape the induced trajectory distribution, thereby enhancing exploration without introducing external supervision. Experiments on five commonly used reasoning benchmarks demonstrate that SPS can enable better exploration and improve Pass@k. Beyond algorithmic contributions, we provide an analysis of RL learning dynamics and identify an empirical upper bound on Pass@k, shedding light on intrinsic exploration limits in RL-based reasoning models. Our findings suggest that alternating between RL and IRL offers an effective pathway toward extending the exploration capacity of reasoning-oriented large language models.

---


### 110. [Intelligent Drill-Down: Large Language Model-Driven Drill-Down Technique for Human-AI Collaborative Visual Exploration](https://arxiv.org/abs/2604.17002)

**<font color=#1a73e8>作者：</font>** Zhijun Zheng, Tian Qiu, Yuheng Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In visual analytics, applying filters to drill-down and extract higher-value insights is a common and important data analysis method. When the drill-down space becomes excessively large, analysts may lose orientation, leading to decreased efficiency in the drill-down process. To tackle these challenges, we propose the Intelligent Drill-Down Framework, in which a large language model (LLM) facilitates the generation of visual insights, leverages user interaction data to interpret user intent, and generates appropriate drill-down paths. Our method is designed to assist users in identifying valuable drill-down paths when exploring multidimensional data, thereby reducing the cognitive burden of data interpretation and facilitating the generation of insights. Specifically, we propose a drill-down path recommendation method, in which the LLM is trained to approximate a validated greedy algorithm. Secondly, we analyze the user's intent to construct a drill-down chart. Finally, we design a branch management method. Building upon this framework, we designed a system that includes a hybrid interface providing hierarchical navigation to monitor users and manage parallel branches, a visualization panel for interactive data exploration, and an insight panel to present analytical findings and generate drill-down recommendations. We evaluated the effectiveness of our method through a demonstrative use case and a user study.

---


### 111. [TeMuDance: Contrastive Alignment-Based Textual Control for Music-Driven Dance Generation](https://arxiv.org/abs/2604.17005)

**<font color=#1a73e8>作者：</font>** Xinran Liu, Diptesh Kanojia, Wenwu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing music-driven dance generation approaches have achieved strong realism and effective audio-motion alignment. However, they generally lack semantic controllability, making it difficult to guide specific movements through natural language descriptions. This limitation primarily stems from the absence of large-scale datasets that jointly align music, text, and motion for supervised learning of text-conditioned control. To address this challenge, we propose TeMuDance, a framework that enables text-based control for music-conditioned dance generation without requiring any manually annotated music-text-motion triplet dataset. TeMuDance introduces a motion-centred bridging paradigm that leverages motion as a shared semantic anchor to align disjoint music-dance and text-motion datasets within a unified embedding space, enabling cross-modal retrieval of missing modalities for end-to-end training. A lightweight text control branch is then trained on top of a frozen music-to-dance diffusion backbone, preserving rhythmic fidelity while enabling fine-grained semantic guidance. To further suppress noise inherent in the retrieved supervision, we design a dual-stream fine-tuning strategy with confidence-based filtering. We also propose a novel task-aligned metric that quantifies whether textual prompts induce the intended kinematic attributes under music conditioning. Extensive experiments demonstrate that TeMuDance achieves competitive dance quality while substantially improving text-conditioned control over existing methods.

---


### 112. [BIASEDTALES-ML: A Multilingual Dataset for Analyzing Narrative Attribute Distributions in LLM-Generated Stories](https://arxiv.org/abs/2604.17008)

**<font color=#1a73e8>作者：</font>** Yuxuan Ouyang, yingfeng luo, JingBo Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to generate narrative content, including children's stories, which play an important role in social and cultural learning. Despite growing interest in AI safety and alignment, most existing evaluations focus primarily on English, leaving the cross-lingual generalization of aligned behavior underexplored. In this work, we introduce BiasedTales-ML, a large-scale parallel corpus of approximately 350,000 children's stories generated across eight typologically and culturally diverse languages using a full-permutation prompting design. We propose a structured generator-extractor pipeline and a multi-dimensional distributional analysis framework to examine how narrative attributes vary across languages, models, and social conditions. Our analysis reveals substantial cross-lingual variability in narrative generation patterns, indicating that distributions observed in English do not always exhibit similar characteristics in other languages, particularly in lower-resource settings. At the narrative level, we identify recurring structural patterns involving character roles, settings, and thematic emphasis, which manifest differently across linguistic contexts. These findings highlight the limitations of English-centric evaluation for characterizing socially grounded narrative generation in multilingual settings. We release the dataset, code, and an interactive visualization tool to support future research on multilingual narrative analysis and evaluation.

---


### 113. [Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification](https://arxiv.org/abs/2604.17010)

**<font color=#1a73e8>作者：</font>** Antonio Valerio Miceli Barone, Poon Tsz Nok  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a self-play framework for semantic equivalence in Haskell, utilizing formal verification to guide adversarial training between a generator and an evaluator. The framework leverages Liquid Haskell proofs for validating equivalence and execution-based counterexamples for inequivalence, organized via a difficulty-aware curriculum. To facilitate this, we release \textbf{OpInstruct-HSx}, a synthetic dataset of $\approx$28k validated Haskell programs. Empirical experiments show that our evaluator transfers effectively to downstream tasks, achieving up to 13.3pp accuracy gain on EquiBench and consistent gains on PySecDB. Ablation studies on the SEQ-SINQ regimes indicate that while inequivalence supervision provides data volume, equivalence proofs are uniquely responsible for the model's reasoning capabilities. The entire training pipeline and dataset are publicly released on GitHub and Hugging Face respectively.

---


### 114. [Beyond Static Benchmarks: Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation](https://arxiv.org/abs/2604.17020)

**<font color=#1a73e8>作者：</font>** Huije Lee, Jisu Shin, Hoyun Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Static benchmarks for harmful content detection face limitations in scalability and diversity, and may also be affected by contamination from web-scale pre-training corpora. To address these issues, we propose a framework for synthesizing harmful content, leveraging persona-guided large language model (LLM) agents. Our approach constructs two-dimensional user personas by integrating demographic identities and topical interests with situational harmful strategies, enabling the simulation of diverse and contextually grounded harmful interactions. We evaluate the framework along three dimensions: harmfulness, challenge level, and diversity. Both human and LLM-based evaluations confirm that our framework achieves a high harmful generation success rate. Experiments across multiple detection systems reveal that our synthetic scenarios are more challenging to detect than those in existing benchmarks. Furthermore, a multi-faceted analysis confirms that our approach achieves linguistic and topical diversity comparable to human-curated datasets, establishing our framework as an effective tool for robust stress-testing of harmful content detection systems.

---


### 115. [LIVE: Leveraging Image Manipulation Priors for Instruction-based Video Editing](https://arxiv.org/abs/2604.17021)

**<font color=#1a73e8>作者：</font>** Weicheng Wang, Zhicheng Zhang, Zhongqi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing aims to modify input videos according to user intent. Recently, end-to-end training methods have garnered widespread attention, constructing paired video editing data through video generation or editing models. However, compared to image editing, the high annotation costs of video data severely constrain the scale, quality, and task diversity of video editing datasets when relying on video generative models or manual annotation. To bridge this gap, we propose LIVE, a joint training framework that leverages large-scale, high-quality image editing data alongside video datasets to bolster editing capabilities. To mitigate the domain discrepancy between static images and dynamic videos, we introduce a frame-wise token noise strategy, which treats the latents of specific frames as reasoning tokens, leveraging large pretrained video generative models to create plausible temporal transformations. Moreover, through cleaning public datasets and constructing an automated data pipeline, we adopt a two-stage training strategy to anneal video editing capabilities. Furthermore, we curate a comprehensive evaluation benchmark encompassing over 60 challenging tasks that are prevalent in image editing but scarce in existing video datasets. Extensive comparative and ablation experiments demonstrate that our method achieves state-of-the-art performance. The source code will be publicly available.

---


### 116. [Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF)](https://arxiv.org/abs/2604.17025)

**<font color=#1a73e8>作者：</font>** Tianbao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) produce a controllability gap in safety-critical engineering: even low rates of undetected constraint violations render a system undeployable. Current orchestration paradigms suffer from sycophantic compliance, context attention decay [Liu et al., 2024], and stochastic oscillation during self-correction [Huang et al., 2024].
We introduce the Convergent AI Agent Framework (CAAF), which transitions agentic workflows from open-loop generation to closed-loop Fail-Safe Determinism via three pillars: (1) Recursive Atomic Decomposition with physical context firewalls; (2) Harness as an Asset, formalizing domain invariants into machine-readable registries enforced by a deterministic Unified Assertion Interface (UAI); and (3) Structured Semantic Gradients with State Locking for monotonic convergence.
Empirical evaluation across two domains -- SAE Level 3 (L3) autonomous driving (AD) (n=30, 7 conditions) and pharmaceutical continuous flow reactor design (n=20, 4 conditions including a Mono+UAI ablation) -- shows that CAAF-all-GPT-4o-mini achieves 100% paradox detection while monolithic GPT-4o achieves 0% (even at temperature=0). The pharmaceutical benchmark features 7 simultaneous constraints with nonlinear Arrhenius interactions and a 3-way minimal unsatisfiable subset, representing a structurally harder challenge than the 2-constraint AD paradox. Alternative multi-agent architectures (debate, sequential checking) also achieve 0% across 80 trials, confirming that CAAF's reliability derives from its deterministic UAI, not from multi-agent orchestration per se. A Mono+UAI ablation (95%) isolates UAI as the core contribution. CAAF's reliability is invariant to prompt hints; all components use a single commodity model, enabling fully offline deployment.

---


### 117. [IMA-MoE: An Interpretable Modality-Aware Mixture-of-Experts Framework for Characterizing the Neurobiological Signatures of Binge Eating Disorder](https://arxiv.org/abs/2604.17028)

**<font color=#1a73e8>作者：</font>** Lin Zhao, Qiaohui Gao, Elizabeth Martin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Binge eating disorder (BED) is the most prevalent eating disorder. However, current diagnostic frameworks remain largely grounded in symptom-based criteria rather than underlying biological mechanisms, thereby limiting early detection and the development of biologically-informed interventions. Emerging studies have begun to investigate the neurobiological signatures of BED, yet their findings are often difficult to generalize due to the reliance on hypothesis-driven parametric models, single-modality analyses, and limited data diversity. Therefore, there is a critical need for advanced data-driven frameworks capable of modeling multimodal data to uncover generalizable and biologically meaningful signatures of BED. In this study, we propose the Interpretable Modality-Aware Mixture-of-Experts (IMA-MoE), a novel architecture designed to integrate heterogeneous neuroimaging, behavioral, hormonal, and demographic measures within a unified predictive framework. By encoding each measure as a distinct token, IMA-MoE enables flexible modeling of cross-modal dependencies while preserving modality-specific characteristics. We further introduce a token-importance mechanism to enhance interpretability by quantifying the contribution of each measure to model predictions. Evaluated on the large-scale Adolescent Brain Cognitive Development (ABCD) dataset, IMA-MoE demonstrates superior performance in differentiating BED from healthy controls compared with baseline methods, while revealing sex-specific predictive patterns, with hormonal measures contributing more prominently to prediction in females. Collectively, these findings highlight the promise of interpretable, data-driven multimodal modeling in advancing biologically-informed characterization of BED and facilitating more precise and personalized interventions in neuropsychiatric disorders.

---


### 118. [Conditional Evidence Reconstruction and Decomposition for Interpretable Multimodal Diagnosis](https://arxiv.org/abs/2604.17030)

**<font color=#1a73e8>作者：</font>** Shaowen Wan, Yanjun Lv, Lu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neurobiological and neurodegenerative diseases are inherently multifactorial, arising from coupled influences spanning genetic susceptibility, brain alterations, and environmental and behavioral factors. Multimodal modeling has therefore been increasingly adopted for disease diagnosis by integrating complementary evidence across data sources. However, in both large-scale cohorts and real-world clinical workflows, modality coverage is often incomplete, making many multimodal models brittle when one or more modalities are unavailable. Existing approaches to incomplete multimodal diagnosis typically rely on group-wise or static priors, which may fail to capture subject-specific cross-modal dependencies; moreover, many models provide limited interpretability into which evidence sources drive the final decision. To address these limitations, we propose Conditional Evidence Reconstruction and Decomposition (CERD), a framework for interpretable multimodal diagnosis with incomplete modalities. CERD first reconstructs missing modality representations conditioned on each subject's observed inputs, then decomposes diagnostic evidence into shared cross-modal corroboration and modality-specific cues via logit-level attribution. Experiments on the Alzheimer's Disease Neuroimaging Initiative (ADNI) demonstrate that CERD outperforms competitive baselines under incomplete-modality settings while producing structured and clinically aligned evidence attributions for trustworthy decision support.

---


### 119. [Where is the Mind? Persona Vectors and LLM Individuation](https://arxiv.org/abs/2604.17031)

**<font color=#1a73e8>作者：</font>** Pierre Beckmann, Patrick Butlin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The individuation problem for large language models asks which entities associated with them, if any, should be identified as minds. We approach this problem through mechanistic interpretability, engaging in particular with recent empirical work on persona vectors, persona space, and emergent misalignment. We argue that three views are the strongest candidates: the virtual instance view and two new views we introduce, the (virtual) instance-persona view and the model-persona view. First, we argue for the virtual instance view on the grounds that attention streams sustain quasi-psychological connections across token-time. Then we present the persona literature, organised around three hypotheses about the internal structure underlying personas in LLMs, and show that the two persona-based views are promising alternatives.

---


### 120. [Dynamic Emotion and Personality Profiling for Multimodal Deception Detection](https://arxiv.org/abs/2604.17037)

**<font color=#1a73e8>作者：</font>** Li Zheng, Yanyi Luo, Hao Fei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deception detection is of great significance for ensuring information security and conducting public opinion analysis, with personality factors and emotion cues playing a critical role. However, existing methods lack sample-level dynamic annotations for emotions and this http URL this paper, we propose an innovative multi-model multi-prompt annotation scheme and a strict label quality evaluation standard, and establish a multimodal joint detection dataset DDEP for deception, emotion, and personality. Meanwhile, we propose Rel-DDEP, an adaptive reliability-weighted fusion framework. Our framework quantifies uncertainty by mapping modal features to a high-dimensional Gaussian distribution space. It then performs reliability-weighted fusion and incorporates an alignment module and a sorting constraint module to achieve joint detection of deception, emotion, and personality. Experimental results on the MDPE and DDEP datasets show that our Rel-DDEP significantly outperforms the existing state-of-the-art baseline models in three tasks. The F1 score of the deception detection increases by 2.53%, that of the emotion detection increases by 2.66%, and that of the personality detection increases by 9.30%. The experiments fully verify the necessity of annotating dynamic emotion and personality labels for each sample and the effectiveness of reliability-weighted fusion.

---


### 121. [SIF: Semantically In-Distribution Fingerprints for Large Vision-Language Models](https://arxiv.org/abs/2604.17041)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Qian Lou, Mengxin Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The public accessibility of large vision-language models (LVLMs) raises serious concerns about unauthorized model reuse and intellectual property infringement. Existing ownership verification methods often rely on semantically abnormal queries or out-of-distribution responses as fingerprints, which can be easily detected and removed by adversaries. We expose this vulnerability through a Semantic Divergence Attack (SDA), which identifies and filters fingerprint queries by measuring semantic divergence between a suspect model and a reference model, showing that existing fingerprints are not semantic-preserving and are therefore easy to detect and bypass. To address these limitations, we propose SIF (Semantically In-Distribution Fingerprints), a non-intrusive ownership verification framework that requires no parameter modification. SIF introduces Semantic-Aligned Fingerprint Distillation (SAFD), which transfers text watermarking signals into the visual modality to produce semantically coherent yet fingerprinted responses. In addition, Robust-Fingerprint Optimization (RFO) enhances robustness by simulating worst-case representation perturbations, making the fingerprints resilient to model modifications such as fine-tuning and quantization. Extensive experiments on LLaVA-1.5 and Qwen2.5-VL demonstrate that SIF achieves strong stealthiness and robustness, providing a practical solution for LVLM copyright protection. Code is available at this https URL

---


### 122. [Efficient Task Adaptation in Large Language Models via Selective Parameter Optimization](https://arxiv.org/abs/2604.17051)

**<font color=#1a73e8>作者：</font>** Weijie Wan, Jiangjiang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated excellent performance in general language understanding, generation and other tasks. However, when fine-tuning for specific domain tasks, the general knowledge accumulated in the pre-training phase is often partially overwritten or forgotten due to parameter updates, which severely limits the generalization ability and transferability of LLMs. Traditional fine-tuning strategies mostly train on the entire parameter space, ignoring the heterogeneity of model parameters, that is, some parameters are extremely important for general tasks, while other parameters are more sensitive to specific tasks. To alleviate the above problems, this paper innovatively proposes a parameter element importance evaluation method, which divides parameters into "core parameters" and "non-core parameters" by distinguishing the importance of parameters for general language ability tasks and specific domain tasks, and fixes the core parameters during fine-tuning, and only fine-tunes the non-core parameters. Extensive experiments on scientific, medical and physical tasks using GPT-J and LLaMA-3 show that our method can mitigate catastrophic forgetting while enhancing the adaptability of the model.

---


### 123. [Jailbreaking Large Language Models with Morality Attacks](https://arxiv.org/abs/2604.17053)

**<font color=#1a73e8>作者：</font>** Ying Su, Mingen Zheng, Weili Diao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pluralism alignment with AI has the sophisticated and necessary goal of creating AI that can coexist with and serve morally multifaceted humanity. Research towards pluralism alignment has many efforts in enhancing the learning of large language models (LLMs) to accomplish pluralism. Although this is essential, the robustness of LLMs to produce moral content over pluralistic values is still under this http URL by the astonishing persuasion abilities via jailbreak prompts, we propose to leverage jailbreak attacks to study LLMs' internal pluralistic values. In detail, we develop a morality dataset with 10.3K instances in two categories: Value Ambiguity and Value Conflict. We further formalize four adversarial attacks with the constructed dataset, to manipulate LLMs' judgment over the morality questions. We evaluate both the large language models and guardrail models which are typically used in generative systems with flexible user input. Our experiment results show that there is a critical vulnerability of LLMs and guardrail models to these subtle and sophisticated moral-aware attacks.

---


### 124. [mEOL: Training-Free Instruction-Guided Multimodal Embedder for Vector Graphics and Image Retrieval](https://arxiv.org/abs/2604.17054)

**<font color=#1a73e8>作者：</font>** Kyeong Seon Kim, Baek Seong-Eun, Lee Jung-Mok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable Vector Graphics (SVGs) function both as visual images and as structured code that encode rich geometric and layout information, yet most methods rasterize them and discard this symbolic organization. At the same time, recent sentence embedding methods produce strong text representations but do not naturally extend to visual or structured modalities. We propose a training-free, instruction-guided multimodal embedding framework that uses a Multimodal Large Language Model (MLLM) to map text, raster images, and SVG code into an aligned embedding space. We control the direction of embeddings through modality-specific instructions and structural SVG cues, eliminating the need for learned projection heads or contrastive training. Our method has two key components: (1) Multimodal Explicit One-word Limitation (mEOL), which instructs the MLLM to summarize any multimodal input into a single token whose hidden state serves as a compact semantic embedding. (2) A semantic SVG rewriting module that assigns meaningful identifiers and simplifies nested SVG elements through visual reasoning over the rendered image, exposing geometric and relational cues hidden in raw code. Using a repurposed VGBench, we build the first text-to-SVG retrieval benchmark and show that our training-free embeddings outperform encoder-based and training-based multimodal baselines. These results highlight prompt-level control as an effective alternative to parameter-level training for structure-aware multimodal retrieval. Project page: this https URL

---


### 125. [BasketHAR: A Multimodal Dataset for Human Activity Recognition and Sport Analysis in Basketball Training Scenarios](https://arxiv.org/abs/2604.17065)

**<font color=#1a73e8>作者：</font>** Xian Gao, Haoyue Zhang, Zongyun Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) involves the automatic identification of user activities and has gained significant research interest due to its broad applicability. Most HAR systems rely on supervised learning, which necessitates large, diverse, and well-annotated datasets. However, existing datasets predominantly focus on basic activities such as walking, standing, and stair navigation, limiting their utility in specialized contexts like sports performance analysis. To address this gap, we present BasketHAR, a novel multimodal HAR dataset tailored for basketball training, encompassing a diverse set of professional-level actions. BasketHAR includes comprehensive motion data from inertial measurement units (accelerometers and gyroscopes), angular velocity, magnetic field, heart rate, skin temperature, and synchronized video recordings. We also provide a baseline multimodal alignment method to benchmark performance. Experimental results underscore the dataset's complexity and suitability for advanced HAR tasks. Furthermore, we highlight its potential applications in the analysis of basketball training sessions and in the generation of specialized performance reports, representing a valuable resource for future research in HAR and sports analytics. The dataset are publicly accessible at this https URL licensed under Apache License 2.0.

---


### 126. [Stability-Weighted Decoding for Diffusion Language Models](https://arxiv.org/abs/2604.17068)

**<font color=#1a73e8>作者：</font>** Yue Wu, Jian Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) enable parallel text generation by iteratively denoising a fully masked sequence, unmasking a subset of masked tokens at each step. Existing decoding strategies rely on static confidence metrics computed at a single denoising step, ignoring temporal history and often leading to premature unmasking of unstable tokens. In this work, we theoretically establish that a token's temporal instability, quantified by the KL divergence between consecutive prediction distributions, provides a strict lower bound on its mutual information with the remaining masked context, indicating that temporally unstable tokens are inherently unsafe to unmask. Based on this insight, we propose Stability-Weighted Decoding (SWD), a training-free, plug-and-play strategy that incorporates temporal stability into token scoring and acts as a universal modulator for arbitrary score-based decoding policies. Experiments on code generation and mathematical reasoning benchmarks demonstrate that SWD consistently improves generation accuracy across representative scoring metrics and selection policies, and exhibits exceptional robustness, maintaining a significant performance lead over standard baselines across varying acceleration ratios.

---


### 127. [CogGen: A Cognitively Inspired Recursive Framework for Deep Research Report Generation](https://arxiv.org/abs/2604.17072)

**<font color=#1a73e8>作者：</font>** Kuo Tian, Pengfei Sun, Zhen Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The autonomous synthesis of deep research reports represents a critical frontier for Large Language Models (LLMs), demanding sophisticated information orchestration and non-linear narrative logic. Current approaches rely on rigid predefined linear workflows, which cause error accumulation, preclude global restructuring from subsequent insights, and ultimately limit in-depth multimodal fusion and report quality. We propose CogGen, a Cognitively inspired recursive framework for deep research report Generation. Leveraging a Hierarchical Recursive Architecture to simulate cognitive writing, CogGen enables flexible planning and global restructuring. To extend this recursivity to multimodal content, we introduce Abstract Visual Representation (AVR): a concise intent-driven language that iteratively refines visual-text layouts without pixel-level regeneration overhead. We further present CLEF, a Cognitive Load Evaluation Framework, and curate a new benchmark from Our World in Data (OWID). Extensive experiments show CogGen achieves state-of-the-art results among open-source systems, generating reports comparable to professional analysts' outputs and surpassing Gemini Deep Research. Our code and dataset are available at this https URL.

---


### 128. [Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL](https://arxiv.org/abs/2604.17073)

**<font color=#1a73e8>作者：</font>** Skylar Zhai, Jingcheng Liang, Dongyeop Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement fine-tuning improves the reasoning ability of large language models, but it can also encourage them to answer unanswerable queries by guessing or hallucinating missing information. Existing abstention methods either train models to produce generic refusals or encourage follow-up clarifications without verifying whether those clarifications identify the key missing information. We study queries that are clear in meaning but cannot be reliably resolved from the given information, and argue that a reliable model should not only abstain, but also explain what is missing. We propose a clarification-aware RLVR reward that, while rewarding correct answers on answerable queries, jointly optimizes explicit abstention and semantically aligned post-refusal clarification on unanswerable queries. Using this reward, we train Abstain-R1, a 3B model that improves abstention and clarification on unanswerable queries while preserving strong performance on answerable ones. Experiments on Abstain-Test, Abstain-QA, and SelfAware show that Abstain-R1 substantially improves over its base model and achieves unanswerable-query behavior competitive with larger systems including DeepSeek-R1, suggesting that calibrated abstention and clarification can be learned through verifiable rewards rather than emerging from scale alone.

---


### 129. [Auditing Support Strategies in LLMs through Grounded Multi-Turn Social Simulation](https://arxiv.org/abs/2604.17079)

**<font color=#1a73e8>作者：</font>** Michelle Star, Andrew Aquilina, Yu-Ru Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When users seek social support from chatbots, they disclose their situation gradually, yet most evaluations of supportive LLMs rely on single-turn, fully specified prompts. We introduce a multi-turn simulation framework that closes this gap. Support-seeking narratives from five Reddit communities are decomposed into ordered fragments and revealed turn by turn to a language model. Each response is coded with the Social Support Behavior Code (SSBC), an established multi-label taxonomy that captures the composition of support, rather than a single quality score. To ask whether support choices track the model's own construal of user distress, we use linear probes on hidden representations to estimate this internal signal without altering the generation context. Across two mid-scale models (Llama-3.1-8B, OLMo-3-7B) and more than 6,200 turns, support composition shifts systematically with estimated distress: teaching declines as estimated distress rises, a finding that replicates across architectures, while increases in affective and esteem-oriented strategies (such as validation) are suggestive but model-specific and rest on noisier annotations. Community context independently shapes behavior, tracking topic and discourse norms rather than demographic categories. These trajectory-level dynamics, invisible to single-turn evaluation, motivate multi-turn auditing frameworks for socially sensitive applications.

---


### 130. [Comparing Human and Large Language Model Interpretation of Implicit Information](https://arxiv.org/abs/2604.17085)

**<font color=#1a73e8>作者：</font>** Antonio De Santis, Tommaso Bonetti, Andrea Tocchetti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The interpretation of implicit meanings is an integral aspect of human communication. However, this framework may not transfer to interactions with Large Language Models (LLMs). To investigate this, we introduce the task of Implicit Information Extraction (IIE) and propose an LLM-based IIE pipeline that builds a structured knowledge graph from a context sentence by extracting relational triplets, validating implicit inferences, and analyzing temporal relations. We evaluate two LLMs against crowdsourced human judgments on two datasets. We find that humans agree with most model triplets yet consistently propose many additions, indicating limited coverage in current LLM-based IIE. Moreover, in our experiments, models appear to be more conservative about implicit inferences than humans in socially rich contexts, whereas humans become more conservative in shorter, fact-oriented contexts. Our code is available at this https URL.

---


### 131. [EvoComp: Learning Visual Token Compression for Multimodal Large Language Models via Semantic-Guided Evolutionary Labeling](https://arxiv.org/abs/2604.17087)

**<font color=#1a73e8>作者：</font>** Jiafei Song, Fengwei Zhou, Jin Qu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Multimodal Large Language Models (MLLMs) have demonstrated strong performance on vision-language understanding tasks, yet their inference efficiency is often hampered by the large number of visual tokens, particularly in high-resolution or multi-image scenarios. To address this issue, we propose EvoComp, a visual token compression framework that significantly reduces token count while preserving task accuracy. EvoComp introduces a lightweight encoder-only transformer-based compressor that selects the most informative and non-redundant visual tokens by jointly considering visual and textual contexts. A core challenge lies in providing effective supervision for training the compressor. To this end, we design an evolutionary labeling strategy that searches for token subsets minimizing the MLLM's output loss, while enforcing semantic diversity through vocabulary-based token grouping. We further train the compressor using a tailored loss function combining the GHM loss to mitigate class and difficulty imbalance, and a cosine similarity regularization to encourage semantic separation between retained and discarded tokens. Extensive experiments across multiple vision-language benchmarks show that EvoComp outperforms existing methods based on attention or similarity heuristics. Notably, it retains 99.3% of the original accuracy under 3x token compression and delivers up to 1.6x speedup on mobile devices.

---


### 132. [GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://arxiv.org/abs/2604.17091)

**<font color=#1a73e8>作者：</font>** Jiaqing Liang, Jinyi Han, Weijia Li 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon large language model (LLM) agents are fundamentally limited by context. As interactions become longer, tool descriptions, retrieved memories, and raw environmental feedback accumulate and push out the information needed for decision-making. At the same time, useful experience gained from tasks is often lost across episodes. We argue that long-horizon performance is determined not by context length, but by how much decision-relevant information is maintained within a finite context budget. We present GenericAgent (GA), a general-purpose, self-evolving LLM agent system built around a single principle: context information density maximization. GA implements this through four closely connected components: a minimal atomic tool set that keeps the interface simple, a hierarchical on-demand memory that only shows a small high-level view by default, a self-evolution mechanism that turns verified past trajectories into reusable SOPs and executable code, and a context truncation and compression layer that maintains information density during long executions. Across task completion, tool use efficiency, memory effectiveness, self-evolution, and web browsing, GA consistently outperforms leading agent systems while using significantly fewer tokens and interactions, and it continues to evolve over time. Project: this https URL

---


### 133. [How Tokenization Limits Phonological Knowledge Representation in Language Models and How to Improve Them](https://arxiv.org/abs/2604.17105)

**<font color=#1a73e8>作者：</font>** Disen Liao, Freda Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization is the first step in every language model (LM), yet it never takes the sounds of words into account. We investigate how tokenization influences text-only LMs' ability to represent phonological knowledge. Through a series of probing experiments, we show that subword-based tokenization systematically weakens the encoding of both local (e.g., rhyme) and global (e.g., syllabification) phonological features. To quantify this effect, we introduce the syllabification-tokenization alignment distance (STAD), a metric that measures the misalignment between a model's tokenization and the natural syllable boundaries of words, and find that higher misalignment correlates with poorer phonological representations, providing a simple diagnostic for phonology-aware tokenization. To address these limitations, we propose a lightweight IPA-based fine-tuning method that infuses phonological awareness into LMs, leading to consistent improvements across three phonology-related tasks while largely preserving math and general reasoning ability, with 1.1\% and 0.9\% drops on GSM8K and MMLU, respectively.

---


### 134. [The Provenance Gap in Clinical AI: Evidence-Traceable Temporal Knowledge Graphs for Rare Disease Reasoning](https://arxiv.org/abs/2604.17114)

**<font color=#1a73e8>作者：</font>** Md Shamim Ahmed, Maja Dusanic, Moritz Nikolai Kirschner 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier large language models generate clinically accurate outputs, but their citations are often fabricated. We term this the Provenance Gap. We tested five frontier LLMs across 36 clinician-validated scenarios for three rare neuromuscular disease pairs. No model produced a clinically relevant PubMed identifier without prompting. When explicitly asked to cite, the best model achieved 15.3% relevant PMIDs; the majority resolved to real publications in unrelated fields. We present HEG-TKG (Hierarchical Evidence-Grounded Temporal Knowledge Graphs), a system that grounds clinical claims in temporal knowledge graphs built from 4,512 PubMed records and curated sources with quality-tier stratification and 1,280 disease-trajectory milestones. In a controlled three-arm comparison using the same synthesis model, HEG-TKG matches baseline clinical feature coverage while achieving 100% evidence verifiability with 203 inline citations. Guideline-RAG, given overlapping source documents as raw text, produces zero verifiable citations. LLM judges cannot distinguish fabricated from verified citations without PubMed audit data. Independent clinician evaluation confirms the verifiability advantage (Cohen's d = 1.81, p < 0.001) with no degradation on safety or completeness. A counterfactual experiment shows 80% resistance to injected clinical errors with 100% detectability via citation trace. The system deploys on-premise via open-source models so patient data never leaves institutional infrastructure.

---


### 135. [Multimodal Fusion of Histopathology Images and Electronic Health Records for Early Breast Cancer Diagnosis](https://arxiv.org/abs/2604.17122)

**<font color=#1a73e8>作者：</font>** Aditya Shribhagwan Khandelwal, Mohammad Samar Ansari, Asra Aslam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer is a leading cause of cancer-related mortality worldwide, and timely accurate diagnosis is critical to improving survival outcomes. While convolutional neural networks (CNNs) have demonstrated strong performance on histopathology image classification, and machine learning models on structured electronic health records (EHR) have shown utility for clinical risk stratification, most existing work treats these modalities in isolation. This paper presents a systematic multimodal framework that integrates patch-level histopathology features from the BreCaHAD dataset with structured clinical data from MIMIC-IV. We train and evaluate unimodal image models (a simple CNN baseline and ResNet-18 with transfer learning), unimodal tabular models (XGBoost and a multilayer perceptron), and an intermediate-fusion model that concatenates latent representations from both modalities. ResNet-18 achieves near-perfect accuracy (1.000) and AUC (1.000) on three-class patch-level classification, while XGBoost achieves 98% accuracy on the EHR prediction task. The intermediate fusion model yields a macro-average AUC of 0.997, outperforming all unimodal baselines and delivering the largest improvements on the diagnostically critical but class-imbalanced mitosis category (AUC 0.994). Grad-CAM and SHAP interpretability analyses validate that model decisions align with established pathological and clinical criteria. Our results demonstrate that multimodal integration delivers meaningful improvements in both predictive performance and clinical transparency.

---


### 136. [Please refuse to answer me! Mitigating Over-Refusal in Large Language Models via Adaptive Contrastive Decoding](https://arxiv.org/abs/2604.17132)

**<font color=#1a73e8>作者：</font>** Yupeng Qi, Ziyu Lyu, Lixin Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models (LLMs) often generate refusal responses to harmless queries due to the over-refusal problem. However, existing methods for mitigating over-refusal cannot maintain a low refusal ratio for harmless queries while keeping a high refusal ratio for malicious ones. In this paper, we analyze how system prompts with varying safety levels affect LLM refusal behaviors when facing over-refusal queries. A key observation is that, when LLMs suffer from the over-refusal issue, non-refusal tokens remain present in the next-token candidate list, but the model systematically fails to select them, despite the generation of refusal tokens. Based on this observation, we propose a training-free and model-agnostic approach, Adaptive Contrastive Decoding (AdaCD), to mitigate over-refusal while maintaining LLM safety. First, AdaCD compares the output distributions of the LLM with or without an extreme safety system prompt to refine the refusal token distribution. Second, we introduce an adaptive contrastive decoding strategy that dynamically incorporates or removes the refusal token distribution, adaptively boosting the probability of selecting refusal or non-refusal tokens. Experimental results on five benchmark datasets show that, on average, AdaCD reduces the refusal ratio for over-refusal queries by 10.35%, yet still increases the refusal ratio for malicious queries by 0.13%. Code is available at this https URL.

---


### 137. [The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration](https://arxiv.org/abs/2604.17139)

**<font color=#1a73e8>作者：</font>** Jiayuan Liu, Shiyi Du, Weihua Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) architectures increasingly rely on response-level aggregation, such as Majority Voting (MAJ), to raise reasoning ceilings. However, in open environments, agents are highly susceptible to stealthy contextual corruption, such as targeted prompt injections. We reveal a critical structural vulnerability in current multi-agent systems: response-level aggregation collapses when corrupted agents form a local majority. Because voting aggregates fully-formed conclusions, it is blind to flawed intermediate logic. To overcome this systematic limitation, we propose the Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. We formalize this process as a discrete-time dynamical system, proving that token-level interleaving transitions aggregation from a brittle counting of final votes (a linear sum) to a dynamic, interwoven chain of logic (a non-linear operator product). Through this theoretical lens, we prove that the honest model's restorative pull can overpower adversarial corruptions, even when corrupted agents form a majority. We conduct an exhaustive empirical evaluation across diverse reasoning benchmarks and demonstrate that while MAJ collapses when corrupted agents reach a majority, RR maintains robust accuracy well beyond this critical threshold.

---


### 138. [SciImpact: A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction](https://arxiv.org/abs/2604.17141)

**<font color=#1a73e8>作者：</font>** Hangxiao Zhu, Yuyu Zhang, Ping Nie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of scientific literature calls for automated methods to assess and predict research impact. Prior work has largely focused on citation-based metrics, leaving limited evaluation of models' capability to reason about other impact dimensions. To this end, we introduce SciImpact, a large-scale, multi-dimensional benchmark for scientific impact prediction spanning 19 fields. SciImpact captures various forms of scientific influence, ranging from citation counts to award recognition, media attention, patent reference, and artifact adoption, by integrating heterogeneous data sources and targeted web crawling. It comprises 215,928 contrastive paper pairs reflecting meaningful impact differences in both short-term (e.g., Best Paper Award) and long-term settings (e.g., Nobel Prize). We evaluate 11 widely used large language models (LLMs) on SciImpact. Results show that off-the-shelf models exhibit substantial variability across dimensions and fields, while multi-task supervised fine-tuning consistently enables smaller LLMs (e.g., 4B) to markedly outperform much larger models (e.g., 30B) and surpass powerful closed-source LLMs (e.g., o4-mini). These results establish SciImpact as a challenging benchmark and demonstrate its value for multi-dimensional, multi-field scientific impact prediction. Our project homepage is this https URL

---


### 139. [Logic-Based Verification of Task Allocation for LLM-Enabled Multi-Agent Manufacturing Systems](https://arxiv.org/abs/2604.17142)

**<font color=#1a73e8>作者：</font>** Jonghan Lim, Mostafa Tavakkoli Anbarani, Rômulo Meira-Góes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Manufacturing industries are facing increasing product variability due to the growing demand for personalized products. Under these conditions, ensuring safety becomes challenging as frequent reconfigurations can lead to unintended hazardous behaviors. Multi-agent control architectures have been proposed to improve flexibility through decentralized decision-making and coordination. However, these architectures are based on predefined task models, which limit their ability to adapt task planning to new product requirements while preserving safety. Recently, large language models have been introduced into manufacturing systems to enhance adaptability, but reliability remains a key challenge. To address this issue, we propose a control architecture that leverages the flexibility of large language models while preserving safety on the manufacturing shop floor. Specifically, the proposed framework verifies large language model-enabled task allocations by using temporal logic and discrete event systems. The effectiveness of the proposed framework is demonstrated through a case study that involves a multi-robot assembly scenario, showing that unsafe tasks can be allocated safely before task execution.

---


### 140. [Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148)

**<font color=#1a73e8>作者：</font>** Sukwon Yun, Jie Peng, Pingzhi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With an ever-growing zoo of LLMs and benchmarks, the need to orchestrate multiple models for improved task performance has never been more pressing. While frameworks like Mixture-of-Agents (MoA) attempt to coordinate LLMs, they often fall short in terms of (1) selecting relevant agents, (2) facilitating effective intra-agent communication, and (3) integrating responses efficiently. In this work, we propose Graph-of-Agents (GoA), a new graph-based framework for modeling multi-agent LLM communication. Our approach begins with node sampling, selecting only the most relevant agents by leveraging model cards that summarize each model's domain, task specialization, and other characteristics. Next, we construct edges between the selected agents by evaluating their responses against one another to determine relevance ordering. Directed message passing is then performed from highly relevant agents to less relevant ones to enhance their responses, followed by reverse message passing to refine the original responses of the more relevant agents. Finally, the updated responses are aggregated via graph-based pooling (e.g., max or mean pooling) to produce a single, unified answer. We evaluate GoA on diverse multi-domain benchmarks (MMLU, MMLU-Pro, GPQA) and domain-specific benchmarks (MATH, HumanEval, MedMCQA), with an agent pool of 6 LLMs spanning multiple domains. Surprisingly, GoA achieves superior performance using only 3 selected agents, outperforming recent multi-agent LLM baselines that utilize all 6 agents simultaneously. By adopting a graph structure, GoA offers both scalability and effectiveness through structured message passing-positioning it as a strong candidate for navigating the challenges of the ever-growing LLM zoo. Code is available at: this https URL.

---


### 141. [Modeling Multi-Dimensional Cognitive States in Large Language Models under Cognitive Crowding](https://arxiv.org/abs/2604.17174)

**<font color=#1a73e8>作者：</font>** Lin Zhong, Siyu Zhu, Zizhen Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modeling human cognitive states is essential for advanced artificial intelligence. Existing Large Language Models (LLMs) mainly address isolated tasks such as emotion analysis or stance detection, and fail to capture interactions among cognitive dimensions defined in psychology, including emotion, thinking style, stance, and intention. To bridge this gap, we construct CognitiveBench, the first benchmark with unified annotations across the above four dimensions. Experiments on CognitiveBench show that although LLMs perform well on single dimension tasks, their performance drops sharply in joint multi-dimensional modeling. Using Gromov $\delta$-hyperbolicity analysis, we find that CognitiveBench exhibits a strong hierarchical structure. We attribute the performance bottleneck to ``Cognitive Crowding'', where hierarchical cognitive states require exponential representational space, while the Euclidean space of LLMs grows only polynomially, causing representation overlap and degraded performance. To address this mismatch, we propose HyCoLLM, which models cognitive states in hyperbolic space and aligns LLM representations via Hyperbolic Guided Alignment Tuning. Results show that HyCoLLM substantially improves multi-dimensional cognitive understanding, allowing 8B parameter model to outperform strong baselines, including GPT-4o.

---


### 142. [RosettaSearch: Multi-Objective Inference-Time Search for Protein Sequence Design](https://arxiv.org/abs/2604.17175)

**<font color=#1a73e8>作者：</font>** Meghana Kshirsagar, Allen Nie, Ching-An Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce RosettaSearch, an inference-time multi-objective optimization approach for protein sequence optimization. We use large language models (LLMs) as a generative optimizer within a search algorithm capable of controlled exploration and exploitation, using rewards computed from RosettaFold3, a structure prediction model. In a large-scale evaluation, we apply RosettaSearch to 400 suboptimal sequences generated by LigandMPNN (a state-of-the-art model trained for protein sequence design), recovering high-fidelity designs that LigandMPNN's single-pass decoding fails to produce. RosettaSearch's designs show improvements in structural fidelity metrics ranging between 18\% to 68\%, translating to a 2.5$\times$ improvement in design success rate. We observe that these gains in success rate are robust when RosettaSearch-designed sequences are evaluated with an independent structure prediction oracle (Chai-1) and generalize across two distinct LLM families (o4-mini and Gemini-3), with performance scaling consistently with reasoning capability. We further demonstrate that RosettaSearch improves sequence fidelity for ProteinMPNN-designed sequences on \textit{de novo} backbones from the Dayhoff atlas, showing that the approach generalizes beyond native protein structures to computationally generated backbones. We also demonstrate a multi-modal extension of RosettaSearch with vision-language models, where images of predicted protein structures are used as feedback to incorporate structural context to guide protein sequence generation. The sequence trajectories generated by our approach can be used as training data in sequence design models or in post-training and will be released along with the code and datasets upon publication.

---


### 143. [Decomposing the Depth Profile of Fine-Tuning](https://arxiv.org/abs/2604.17177)

**<font color=#1a73e8>作者：</font>** Jayadev Billa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning adapts pretrained networks to new objectives. Whether the resulting depth profile of representational change reflects an intrinsic property of the model or the magnitude of gradient flow has not been tested directly. We measure this profile across 240 fine-tuning runs spanning 15 models in four architecture families (encoder and decoder transformers, a state-space model, and an RNN) at scales from 125M to 6.9B parameters. Representational change concentrates in output-proximal layers in every standard-training run except one. We apply a per-layer control that equalizes $\|\Delta W\|/\|W\|$ across layers after each optimizer step. Under this control, the profile persists in some conditions and collapses in others. At 125M--350M, sequential-block architectures (BERT, OPT, GPT-2) retain the slope across tested objectives while parallel-block architectures (Pythia, CodeGen) retain it only for causal-language-modeling objectives. This architectural distinction narrows at 1.3B--1.4B, where both block types show positive equal-step slopes for CausalLM. Under standard training, profile shape is described by two additional axes: steepness tracks a training-free objective distance at initialization, and profile width is dominated by architecture. We treat the locality gradient, the depthwise slope of representational change, as a composite phenomenon whose components are scale-dependent.

---


### 144. [Cognitive Policy-Driven LLM for Diagnosis and Intervention of Cognitive Distortions in Emotional Support Conversation](https://arxiv.org/abs/2604.17178)

**<font color=#1a73e8>作者：</font>** Lin Zhong, Renjin Zhu, Shujuan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotional Support Conversation (ESC) plays a critical role in mental health assistance by providing accessible psychological support in real-world applications. Large Language Models (LLMs) have shown strong empathetic abilities in ESC tasks. Yet, existing methods overlook the issue of cognitive distortions in help-seekers' expressions. As a result, current models can only provide basic emotional comfort, rather than helping help-seekers address their psychological distress at a deeper cognitive level. To address this challenge, we construct the CogBiasESC dataset, the first dataset that expands existing ESC datasets by adding labels for cognitive distortions, includes their type, intensity, and safe risk level. Furthermore, we propose the Cognitive Policy-driven Large Language Model framework (CoPoLLM) to enhance LLMs' ability to diagnose and intervene cognitive distortions in help-seekers. We also analyze the safety advantages of CoPoLLM from a theoretical perspective. Experimental results show that CoPoLLM significantly outperforms 15 state-of-the-art baselines in terms of distortion diagnosis accuracy, intervention strategy effectiveness, and safety risk control.

---


### 145. [LookasideVLN: Direction-Aware Aerial Vision-and-Language Navigation](https://arxiv.org/abs/2604.17190)

**<font color=#1a73e8>作者：</font>** Yuwei Ning, Ganlong Zhao, Yipeng Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial Vision-and-Language Navigation (Aerial VLN) enables unmanned aerial vehicles (UAVs) to follow natural language instructions and navigate complex urban environments. While recent advances have achieved progress through large-scale memory graphs and lookahead path planning, they remain limited by shallow instruction understanding and high computational cost. In particular, existing methods rely primarily on landmark descriptions, overlooking directional cues "a key source of spatial context in human navigation". In this work, we propose LookasideVLN, a new paradigm that exploits directional cues in natural language to achieve both more accurate spatial reasoning and greater computational efficiency. LookasideVLN comprises three core components: (1) an Egocentric Lookaside Graph (ELG) that dynamically encodes instruction-relevant landmarks and their directional relationships, (2) a Spatial Landmark Knowledge Base (SLKB) that provides lightweight memory retrieval from prior navigation experiences, and (3) a Lookaside MLLM Navigation Agent that aligns multimodal information from user instructions, visual observations, and landmark-direction information from ELG for path planning. Extensive experiments show that LookasideVLN significantly outperforms the state-of-the-art CityNavAgent, even with a single-level lookahead, demonstrating that leveraging directional cues is a powerful yet efficient strategy for Aerial VLN.

---


### 146. [Do LLM-derived graph priors improve multi-agent coordination?](https://arxiv.org/abs/2604.17191)

**<font color=#1a73e8>作者：</font>** Nikunj Gupta, Rajgopal Kannan, Viktor Prasanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) is crucial for AI systems that operate collaboratively in distributed and adversarial settings, particularly in multi-domain operations (MDO). A central challenge in cooperative MARL is determining how agents should coordinate: existing approaches must either hand-specify graph topology, rely on proximity-based heuristics, or learn structure entirely from environment interaction; all of which are brittle, semantically uninformed, or data-intensive. We investigate whether large language models (LLMs) can generate useful coordination graph priors for MARL by using minimal natural language descriptions of agent observations to infer latent coordination patterns. These priors are integrated into MARL algorithms via graph convolutional layers within a graph neural network (GNN)-based pipeline, and evaluated on four cooperative scenarios from the Multi-Agent Particle Environment (MPE) benchmark against baselines spanning the full spectrum of coordination modeling, from independent learners to state-of-the-art graph-based methods. We further ablate across five compact open-source LLMs to assess the sensitivity of prior quality to model choice. Our results provide the first quantitative evidence that LLM-derived graph priors can enhance coordination and adaptability in dynamic multi-agent environments, and demonstrate that models as small as 1.5B parameters are sufficient for effective prior generation.

---


### 147. [SciDraw-6K: A Multilingual Scientific Illustration Dataset Generated by Google Gemini](https://arxiv.org/abs/2604.17206)

**<font color=#1a73e8>作者：</font>** Davie Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SciDraw-6K, a curated dataset of 6,291 scientific illustrations synthesized by Google Gemini image-generation models, each paired with prompts in eleven languages (English, Simplified Chinese, Traditional Chinese, Japanese, Korean, German, French, Spanish, Brazilian Portuguese, Italian, and Russian). Images span eight broad scientific categories -- biomedical, chemistry, materials, electronics, environment, AI systems, physics, and a long "other" tail -- and are produced primarily by the gemini-2.5-flash-image and gemini-3-pro-image-preview model families. In contrast to general-purpose text-to-image corpora that dominate the literature, SciDraw-6K is purpose-built for the scientific illustration genre: schematic diagrams, mechanism figures, table-of-contents graphics, and conceptual posters. We describe the construction pipeline, report dataset statistics, and document its use as the substrate of this http URL, a public scientific drawing service. The dataset is released to support multilingual text-to-image research, domain-adapted diffusion fine-tuning, and prompt-engineering studies for scientific visualization. Dataset: this https URL Code: this https URL

---


### 148. [DREAM: Dynamic Retinal Enhancement with Adaptive Multi-modal Fusion for Expert Precision Medical Report Generation](https://arxiv.org/abs/2604.17209)

**<font color=#1a73e8>作者：</font>** Nagur Shareef Shaik, Teja Krishna Cherukuri, Dong Hye Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating medical reports for retinal images requires a sophisticated blend of visual pattern recognition and deep clinical knowledge. Current Large Vision-Language Models (LVLMs) often struggle in specialized medical fields where data is scarce, leading to models that overfit and miss subtle but critical pathologies. To address this, we introduce DREAM (Dynamic Retinal Enhancement with Adaptive Multi-modal Fusion), a novel framework for high-fidelity medical report generation that excels even with limited data. DREAM employs a unique two-stage fusion mechanism that intelligently integrates visual data with clinical keywords curated by ophthalmologists. First, the Abstractor module maps image and keyword features into a shared space, enhancing visual data with pathology-relevant insights. Next, the Adaptor performs adaptive multi-modal fusion, dynamically weighting the importance of each modality using learnable parameters to create a unified representation. To ensure the model's outputs are semantically grounded in clinical reality, a Contrastive Alignment module aligns these fused representations with ground-truth medical reports during training. By combining medical expertise with an efficient fusion strategy, DREAM sets a new state-of-the-art on the DeepEyeNet benchmark, achieving a BLEU-4 score of 0.241, and further demonstrates strong generalization to the ROCO dataset.

---


### 149. [Guardrails in Logit Space: Safety Token Regularization for LLM Alignment](https://arxiv.org/abs/2604.17210)

**<font color=#1a73e8>作者：</font>** Thong Bach, Truyen Tran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning well-aligned large language models (LLMs) on new domains often degrades their safety alignment, even when using benign datasets. Existing safety alignment techniques primarily focus on pretraining, leaving fine-tuned models vulnerable to behavioral shifts. In this work, we introduce safety token regularization (STR), a lightweight method designed to preserve safety properties during fine-tuning. Our approach identifies salient tokens from rejection templates of well-aligned models and constrains their associated logits during training, preventing the loss of critical safety behaviors. Unlike reinforcement learning or preference optimization methods, STR requires minimal additional computation and seamlessly integrates with parameter-efficient fine-tuning techniques such as LoRA. Comprehensive experiments demonstrate that our approach achieves safety performance on par with state-of-the-art methods, while preserving task-specific utility and requiring minimal implementation overhead. Furthermore, we show that safety token regularization enhances training stability and overall performance beyond safety considerations alone. This work offers a practical and readily deployable strategy for continual safety alignment in fine-tuned LLMs.

---


### 150. [Beyond the Basics: Leveraging Large Language Model for Fine-Grained Medical Entity Recognition](https://arxiv.org/abs/2604.17214)

**<font color=#1a73e8>作者：</font>** Nwe Ni Win, Jim Basilakis, Steven Thomas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extracting clinically relevant information from unstructured medical narratives such as admission notes, discharge summaries, and emergency case histories remains a challenge in clinical natural language processing (NLP). Medical Entity Recognition (MER) identifies meaningful concepts embedded in these records. Recent advancements in large language models (LLMs) have shown competitive MER performance; however, evaluations often focus on general entity types, offering limited utility for real-world clinical needs requiring finer-grained extraction. To address this gap, we rigorously evaluated the open-source LLaMA3 model for fine-grained medical entity recognition across 18 clinically detailed categories. To optimize performance, we employed three learning paradigms: zero-shot, few-shot, and fine-tuning with Low-Rank Adaptation (LoRA). To further enhance few-shot learning, we introduced two example selection methods based on token- and sentence-level embedding similarity, utilizing a pre-trained BioBERT model. Unlike prior work assessing zero-shot and few-shot performance on proprietary models (e.g., GPT-4) or fine-tuning different architectures, we ensured methodological consistency by applying all strategies to a unified LLaMA3 backbone, enabling fair comparison across learning settings. Our results showed that fine-tuned LLaMA3 surpasses zero-shot and few-shot approaches by 63.11% and 35.63%, respectivel respectively, achieving an F1 score of 81.24% in granular medical entity extraction.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
