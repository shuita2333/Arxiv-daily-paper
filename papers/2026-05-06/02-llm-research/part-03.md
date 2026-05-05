# 🧠 大模型相关研究 | 2026年05月06日

> 本类共 **203** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 101. [Molecular Representations for Large Language Models](https://arxiv.org/abs/2605.01822)

**<font color=#1a73e8>作者：</font>** Nicholas T. Runcie, Fergus Imrie, Charlotte M. Deane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being used to support scientific discovery. In chemistry, tasks such as reaction prediction and structure elucidation require reasoning about the structures of molecules. As such, LLM-based systems for chemistry must interact reliably with molecular structures. Most previous studies of LLMs in chemistry have used SMILES strings or IUPAC names as molecular representations; however, the suitability of these formats has not been systematically assessed. In this work, we introduce MolJSON, a novel molecular representation for LLMs, and systematically compare it with five common chemical formats. We evaluated each representation with GPT-5-nano, GPT-5-mini, GPT-5, and Claude Haiku 4.5 using a set of 78,045 questions spanning translation, shortest path, and constrained generation reasoning tasks. We observed substantial variation across representations in the ability of LLMs to interpret and generate molecular graphs, with MolJSON consistently outperforming existing formats. On translation tasks, GPT-5 achieved 71.0% accuracy when converting IUPAC names to MolJSON, compared with 43.7% when converting the same inputs to SMILES. For constrained generation, GPT-5 reached 95.3% accuracy generating MolJSON, compared with 76.3% for IUPAC and 64.0% for SMILES. As an input format for shortest-path reasoning, GPT-5 successfully answered 98.5% of questions with MolJSON, compared with 92.2% for SMILES and 82.7% for IUPAC, whilst also using fewer reasoning tokens. We observed systematic errors associated with atom count and ring complexity for SMILES strings and IUPAC names, whereas MolJSON was more robust to these failure modes. Our results show that the choice of molecular representation has a material impact on LLM performance, and that explicit molecular graph schemas, such as MolJSON, are a promising direction for LLM-based systems in chemistry.

---


### 102. [Selector-Guided Autonomous Curriculum for One-Shot Reinforcement Learning from Verifiable Rewards](https://arxiv.org/abs/2605.01823)

**<font color=#1a73e8>作者：</font>** Rudray Dave, Vedang Dubey, Smit Deoghare 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, Reinforcement Learning from Verifiable Rewards (RLVR) has been established as a highly effective technique for augmenting the math reasoning skills of Large Language Models (LLMs) based on a single instance. Current state-of-the-art 1-shot RLVR models adopt heuristics for selecting instances, mostly based on historical variance in rewards, which we find to be inherently misleading as a measure of transferability value. In this paper, we propose a Selector-Guided Autonomous Curriculum (SGAC) approach, which employs a learnable selector model on a multi-dimensional feature space consisting of success probability, reward variance, output disagreement (entropy), and semantic difficulty level, instead of the static reward variance heuristic. In our empirical evaluation on pools of candidate problems, we observed that output disagreement, rather than reward variance, is the strongest predictor of reasoning gains in subsequent iterations. Leveraging this finding, we develop an autonomous curriculum algorithm for dynamically siphoning candidate problems from a large pool, ranking them by the learned selector, and running micro-bursts of 1-shot GRPO. Our framework is evaluated using the Hendrycks MATH benchmark, with the Qwen2.5-Math-1.5B model serving as the baseline. Our framework obtains an accuracy of 68.0\% on the hold-out dataset, which is better than the accuracy obtained from the state-of-the-art model, 64.0\%, as well as the 1-shot RLVR checkpoint proposed by Wang et al., which achieved an accuracy of 66.0\%. The results confirm that entropy-based intelligent data curation leads to strict reasoning improvement over static training methods, particularly in severely limited data conditions.

---


### 103. [Referring Multiple Regions with Large Multimodal Models via Contextual Latent Steering](https://arxiv.org/abs/2605.01827)

**<font color=#1a73e8>作者：</font>** Yun Xing, Hanyuan Liu, Jiahao Nie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) have recently demonstrated their proficiency in holistic visual comprehension. However, most of them struggle to tackle region-level perception guided by visual prompts, especially for cases where multiple regions are referred simultaneously, or scenarios where global contexts are necessary for precise visual referring. We introduce Contextual Latent Steering (CSteer), a training-free approach for guiding general LMMs to refer multiple regions contextually, without expensive fine-tuning or architectural modifications. CSteer starts with pre-computing contextual vectors that implicitly represent visual referring behaviors, such as differentiation among regions and attention to global contexts, followed by representation editing during inference time. Experimental results on multiple datasets indicate that general LMMs with CSteer outperform tailored referring LMMs in most cases, suggesting a promising solution in training-free, and setting new state-of-the-art for this field. Code is available at this https URL.

---


### 104. [GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder Annotation of Brain MRI Foundation Models](https://arxiv.org/abs/2605.01829)

**<font color=#1a73e8>作者：</font>** Favour Nerrise, Lucy Yin, Mohammad H. Abbasi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain MRI foundation models learn rich representations of anatomy, but interpreting what clinical information they encode remains an open problem. Standard sparse autoencoders (SAEs) suffer from severe feature collapse in deep transformer layers, and in Alzheimer's disease (AD) research, aging confounds nearly every clinical variable, making naive annotation unreliable. We propose GeoSAE, a geometry-guided SAE framework that uses the foundation model's learned manifold structure to prevent feature collapse and annotates each surviving feature via age-deconfounded partial correlations. Applied to ~14k T1-weighted MRI scans from the Alzheimer's Disease Neuroimaging Initiative (ADNI) and the Australian Imaging biomarkers and Lifestyle (AIBL) datasets, GeoSAE identifies a compact, fully interpretable feature set that predicts mild cognitive impairment (MCI)-to-AD conversion (AUC 0.746) using only 2% of the embedding dimensions, while comorbidity-annotated features achieve only chance-level performance. The identified features replicate across cohorts without retraining (r=0.97) and localize to neuroanatomically distinct regions consistent with Braak staging. This shows that geometry-guided SAEs can extract interpretable, biomarkers from frozen brain MRI foundation models.

---


### 105. [The Cylindrical Representation Hypothesis for Language Model Steering](https://arxiv.org/abs/2605.01844)

**<font color=#1a73e8>作者：</font>** Lang Gao, Jinghui Zhang, Wei Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering is a widely used technique for controlling large language models, yet its effects are often unstable and hard to predict. Existing theoretical accounts are largely based on the Linear Representation Hypothesis (LRH). While LRH assumes that concepts can be orthogonalized for lossless control, this idealized mapping fails in real representations and cannot account for the observed unpredictability of steering. By relaxing LRH's orthogonality assumption while preserving linear representations, we show that overlapping concept contributions naturally yield a sample-specific axis-orthogonal structure. We formalize this as the Cylindrical Representation Hypothesis (CRH). In CRH, a central axis captures the main difference between concept absence and presence and drives concept generation. A surrounding normal plane controls steering sensitivity by determining how easily the axis can activate the target concept. Within this plane, only specific sensitive sectors strongly facilitate concept activation, while other sectors can suppress or delay it. While the surrounding normal plane can be reliably identified from difference vectors, the sensitive sector cannot, introducing intrinsic uncertainty at the sector level. This uncertainty provides a principled explanation for why steering outcomes often fluctuate even when using well-aligned directions. Our experiments verify the existence of the cylindrical structure and demonstrate that CRH provides a valid and practical way to interpret model steering behavior in real settings: this https URL.

---


### 106. [Do Large Language Models Plan Answer Positions? Position Bias in Multiple-Choice Question Generation](https://arxiv.org/abs/2605.01846)

**<font color=#1a73e8>作者：</font>** Xuemei Tang, Xufeng Duan, Zhenguang G. Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate multiple-choice questions (MCQs), where correct answers should ideally be uniformly distributed across options. However, we observe that LLMs exhibit systematic position biases during generation. Through extensive experiments with 10 LLMs and 5 vision-language models (VLMs) on three MCQ generation tasks, we show that these biases are structured, with similar patterns emerging within model families. To investigate the underlying mechanisms, we conduct probing experiments and find that hidden representations in the question stem encode predictive signals of the correct answer position, suggesting that answer position may be implicitly planned during generation. Building on this insight, we apply activation steering to manipulate internal representations and influence answer position. Our results show that steering can partially control positional preferences and substantially shift answer position distributions. Our findings provide a practical framework for studying implicit positional planning in LLMs and highlight the importance of controllable generation for reliable MCQ construction and evaluation.

---


### 107. [NeuroState-Bench: A Human-Calibrated Benchmark for Commitment Integrity in LLM Agent Profiles](https://arxiv.org/abs/2605.01847)

**<font color=#1a73e8>作者：</font>** Jia Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Outcome-only evaluation under-specifies whether an evaluated agent profile preserves the commitments required to solve a multi-turn task coherently. NeuroState-Bench is a human-calibrated benchmark that operationalizes commitment integrity through benchmark-defined side-query probes rather than inferred hidden activations. The released inventory contains 144 deterministic tasks and 306 benchmark-defined side-query probes spanning eight cognitively motivated failure families, paired clean and distractor variants, and three difficulty bands. The main 32-profile evaluation contains a fixed 16-profile local subset and a matched 16-profile hosted large-model subset evaluated through the same benchmark pipeline. Human calibration uses the final merged reporting scope: 104 sampled task units, 216 raw annotations, and 108 adjudicated task rows, with weighted kappa = 0.977 and ICC(2,1) = 0.977. Empirically, task success and commitment integrity diverge across this expanded grid: the success leader is not the integrity leader, 31 of 32 profiles change rank when integrity replaces task success, and integrity rankings are more stable under distractor perturbation. The primary confidence-free score HCCIS-CORE reaches 0.8469 AUC and 0.6992 PR-AUC for post-probe diagnostic discrimination of terminal task failure; the legacy full heuristic variant HCCIS-FULL reaches 0.7997 AUC and 0.6410 PR-AUC. Probe accuracy and state drift achieve slightly higher ROC-AUC, 0.8587, and better Brier/ECE, while HCCIS-CORE has substantially higher point-estimate PR-AUC and remains more closely tied to the benchmark's intended construct. The exploratory neural-augmented variant HCCIS+N is weaker overall, and a randomized subspace control approaches chance. NeuroState-Bench therefore contributes a calibrated evaluation axis for exposing commitment failures over a broader model grid than the original local-only subset.

---


### 108. [Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models](https://arxiv.org/abs/2605.01853)

**<font color=#1a73e8>作者：</font>** Kotaro Furuya, Takahito Tanimura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) generate extended solutions, yet it remains unclear whether these traces reflect substantive internal computation or merely verbosity and overthinking. Although recent hidden-state analyses suggest that internal representations carry correctness-related signals, their coarse aggregations may obscure the token and layer structure underlying reasoning computation. We investigate hidden-state transitions across decoding steps and layers, and identify a distinct spatiotemporal pattern in LRMs: successful trajectories exhibit broad temporal dynamics with localized layer-wise concentration, while this structure is weaker in non-reasoning models and knowledge-heavy domains. We formalize this characteristic as Spatiotemporal Amplitude of Latent Transition (StALT), a training-free trajectory statistic that summarizes temporal changes between adjacent tokens weighted by within-token layer saliency. Across diverse models and benchmarks, StALT reliably separates correct from incorrect trajectories in reasoning-intensive regimes, providing a competitive label-free correctness signal alongside strong output-space and length-based baselines. Intervention analyses further show that this spatiotemporal amplitude responds systematically to manipulations that increase or reduce the demand for internal reasoning, supporting its association with latent reasoning dynamics in LRMs. These findings provide empirical evidence that LRMs exhibit measurable hidden-state dynamics and offer a practical probe for understanding internal computation beyond output-based evaluation.

---


### 109. [Maistros: A Greek Large Language Model Adapted Through Knowledge Distillation From Large Reasoning Models](https://arxiv.org/abs/2605.01870)

**<font color=#1a73e8>作者：</font>** Nikolaos Giarelis, Charalampos Mastrokostas, Nikos Karacapilidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have substantially advanced the field of Natural Language Processing (NLP), achieving state-of-the-art performance across a wide range of tasks. These improvements have been attributed, in part, to their emerging reasoning capabilities, which are enabled by large-scale training and increased model capacity. However, existing LLMs can generate erroneous responses when addressing complex queries that fall outside their training distribution, due to limited internal knowledge or the need for multi-step reasoning. To address these limitations, recent work has introduced large reasoning models (LRMs), which incorporate explicit internal reasoning processes to improve response accuracy. Additionally, state-of-the-art LRMs often comprise hundreds of billions of parameters and require several seconds per inference, even on advanced multi-GPU systems. These characteristics limit their practicality for deployment in conventional computing environments. Meanwhile, NLP research on multilingual LLMs continues to prioritize high-resource languages. However, these models exhibit limited performance in under-resourced languages, primarily due to insufficient language- and culture-specific training data. In this paper, we focus on Modern Greek, for which only a limited number of question answering (QA) datasets have been proposed, most of which are intended for model evaluation. To address this research gap in Greek QA, we make the following contributions: (i) CulturaQA, a high-quality LRM-generated and human-curated dataset, for Greek LLM training and evaluation; (ii) a memory-efficient LLM evaluation framework adaptable to diverse languages and QA tasks; (iii) Maistros 8B, a state-of-the-art open-weights Greek LLM developed via knowledge distillation and fine-tuning on CulturaQA; and (iv) a comprehensive evaluation of nine LLMs across nine human-curated Greek QA datasets.

---


### 110. [Leveraging Data Symmetries to Select an Optimal Subset of Training Data under Label Noise](https://arxiv.org/abs/2605.01874)

**<font color=#1a73e8>作者：</font>** Kumar Shubham, Pavan Karjol, Kiran M K 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of machine learning models often relies on large labeled datasets; however, data collected from diverse sources can contain label noise. Recent work has shown that, in noisy settings, there may exist a subset of the training data on which models can achieve performance comparable to training on a noise-free dataset. A widely used method for identifying such subsets is cutstats, which employs k-nearest neighbors (k-NN) to detect low-noise samples. However, its performance on high-dimensional data remains largely unexplored. In this work, we formally establish that the performance of a classifier trained on a subset of a noisy dataset selected via cutstats is influenced by the accuracy of k-NN. We further demonstrate that, in noisy environments, exploiting data invariance and knowledge of underlying symmetries can significantly enhance the performance of k-NN, bringing it closer to the Bayes optimal classifier even in high-dimensional regimes. Finally, we show that for real-world scenarios, where information about the underlying invariance is only partially known, learnt invariant representations can still facilitate the identification of near-optimal subsets.

---


### 111. [BadmintonGRF: A Multimodal Dataset and Benchmark for Markerless Ground Reaction Force Estimation in Badminton](https://arxiv.org/abs/2605.01876)

**<font color=#1a73e8>作者：</font>** Kuoye Niu, Jianwei Li, Shengze Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal resources for non-periodic court sports with laboratory-grade sensing remain scarce: few publicly pair instrumented ground reaction force (GRF) with high-frame-rate multi-view video, limiting markerless load estimation in realistic training settings. BadmintonGRF records eight synchronized RGB views at ~120 FPS, four Kistler force plates, and Vicon motion capture (C3D) without hardware genlock across modalities; alignment combines human-verified events, automated quality assurance, and per-camera time offsets with uncertainty metadata. Tier 1 distributes pose, time-aligned GRF, metadata, and splits under CC BY-NC 4.0, enabling the primary benchmark without raw RGB or C3D; we report a Tier 1 task that maps 2D pose to GRF. Tier 2 provides raw RGB and C3D under controlled access for studies that require appearance or full kinematics. The public release contains 17,425 impact-segment archives in the 10-subject benchmark tree (156 instrumented trials; raw multi-view RGB alone exceeds 1 TB); benchmark loader gates retain 12,867 view-specific instances and 1,732 unique impacts after multi-view deduplication. We are not aware of prior public badminton corpora that combine this sensing layout with audited video--GRF alignment for impact-centric GRF estimation. We distribute preprocessing code, leave-one-subject-out splits, ten reference baselines, and optional late fusion (one deterministic test-time pass per instance; no test-time augmentation), with a within-trial diagnostic in the supplementary material.

---


### 112. [Chart-FR1: Visual Focus-Driven Fine-Grained Reasoning on Dense Charts](https://arxiv.org/abs/2605.01882)

**<font color=#1a73e8>作者：</font>** Hongkun Pan, Yuwei Wu, Wanyi Hong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown considerable potential in chart understanding and reasoning tasks. However, they still struggle with high information density (HID) charts characterized by multiple subplots, legends, and dense annotations due to three major challenges: (1) limited fine-grained perception results in the omission of critical visual cues; (2) redundant or noisy visual information undermines the performance of multimodal reasoning; (3) lack of adaptive deep reasoning relative to the amount of visual information. To tackle these challenges, we present a novel focus-driven fine-grained chart reasoning model, Chart-FR1, to improve perception, focusing efficiency, and adaptive deep reasoning on HID charts. Specifically, we propose Focus-CoT, a visual focusing chain-of-thought that enhances fine-grained perception by explicitly linking reasoning steps to key visual cues, such as local image regions and OCR signals. Building on this, we introduce Focus-GRPO, a focus-driven reinforcement learning algorithm with an information-efficiency reward that compresses redundant visual information for efficient focusing, and an adaptive KL penalty mechanism that enables flexible control over reasoning depth as more visual cues are discovered. Furthermore, to fill the gap in benchmarks for HID charts, we build HID-Chart, a challenging benchmark with an information-density metric designed to evaluate fine-grained chart reasoning capabilities. Extensive experiments on multiple chart benchmarks demonstrate that Chart-FR1 outperforms state-of-the-art MLLMs in chart understanding and reasoning. Code is available at this https URL.

---


### 113. [Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](https://arxiv.org/abs/2605.01896)

**<font color=#1a73e8>作者：</font>** Junyuan Xiao, Dingkang Liang, Xin Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emerging multi-modal world models attempt to jointly generate videos across diverse modalities (e.g., RGB, depth, and mask), yet they fail to fully exploit the rich priors of existing foundation models. We propose $M^2$-REPA, the first representation alignment method tailored for multi-modal video generation. Our key insight is that foundation models trained on different modality spaces naturally capture distinct domain-specific priors, acting as complementary "experts." Specifically, we first decouple modality-specific features from the diffusion model's intermediate representations, then align each with its corresponding expert foundation model. To this end, we design two synergistic objectives: a multi-modal representation alignment loss that enforces feature-to-expert matching, and a modality-specific decoupling regularization that encourages complementarity across different modalities. This design enables joint optimization, fully exploiting priors from multiple foundation models. Extensive experiments demonstrate that our method significantly outperforms baselines in visual quality and long-term consistency.

---


### 114. [Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment](https://arxiv.org/abs/2605.01899)

**<font color=#1a73e8>作者：</font>** Jiajia Li, Xiaoyu Wen, Zhongtian Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing capabilities of large language models (LLMs) have driven their widespread deployment across diverse domains, even in potentially high-risk scenarios. Despite advances in safety alignment techniques, current models remain vulnerable to emerging persona-based jailbreak attacks. Existing research on persona-based jailbreak has primarily focused on attack iterations, yet it lacks systemic and mechanistic constraints on the defense side. To address this challenge, we propose Persona-Invariant Alignment (PIA), an adversarial self-play framework that achieves co-evolution through Persona Lineage Evolution (PLE) on the attack side and Persona-Invariant Consistency Learning (PICL) on the defense side. Theoretically, PICL is grounded in the structural separation hypothesis, using a unilateral KL-divergence constraint to enable the structural decoupling of safety decisions from persona context, thereby maintaining safe behavior under persona-based jailbreak attacks. Experimental results demonstrate that PLE efficiently explores high-risk persona spaces by leveraging lineage-based credit propagation. Meanwhile, the PICL defense method significantly reduces the Attack Success Rate (ASR) while preserving the model's general capability, thereby validating the superiority and robustness of this alignment paradigm. Codes are available at this https URL.

---


### 115. [SurgCheck: Do Vision-Language Models Really Look at Images in Surgical VQA?](https://arxiv.org/abs/2605.01911)

**<font color=#1a73e8>作者：</font>** Jongmin Shin, Ka Young Kim, Eunki Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Vision-language models (VLMs) have shown promising performance in surgical visual question answering (VQA). However, existing surgical VQA datasets often contain linguistic shortcuts, where question phrasing implicitly constrains the answer space. It remains unclear whether reported performance reflects visual understanding or reliance on such linguistic shortcuts. Methods: We introduce SurgCheck, a diagnostic benchmark for quantifying linguistic shortcut reliance in surgical VQA. SurgCheck employs a paired-question design in which each surgical frame is associated with an original question containing entity names and a less-biased counterpart that removes these names while preserving identical visual content and ground-truth answers. The resulting performance gap provides a diagnostic signal of shortcut reliance. To ensure that the less-biased question remains well-defined even without entity names, four grounding cues are incorporated: bounding box, arrow, spatial position, and periphrasis. We evaluate both general-purpose and surgical-specific VLMs under zero-shot and fine-tuned settings on SurgCheck. To evaluate open-ended zero-shot responses, we introduce an LLM-as-a-judge evaluation protocol. Results: Using SurgCheck, we observe consistent performance degradation on less-biased questions across five VLMs, despite identical visual inputs. Text-only ablation reveals minimal performance drops for action and target prediction, indicating that action and target prediction is largely driven by linguistic shortcuts rather than visual reasoning. Conclusion: SurgCheck provides a controlled diagnostic framework that exposes failure modes masked by linguistic bias in existing surgical VQA benchmarks. Our findings demonstrate that strong benchmark performance does not necessarily imply faithful visual understanding, underscoring the need for bias-aware evaluation in surgical VQA.

---


### 116. [RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs](https://arxiv.org/abs/2605.01913)

**<font color=#1a73e8>作者：</font>** Sadia Asif, Mohammad Mohammadi Amiri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning safety-aligned language models for downstream tasks often leads to substantial degradation of refusal behavior, making models vulnerable to adversarial misuse. While prior work has shown that safety-relevant features are encoded in structured representations within the model's activation space, how these representations change during fine-tuning and why alignment degrades remains poorly understood. In this work, we investigate the representation-level mechanisms underlying alignment degradation. Our analysis shows that standard fine-tuning induces systematic drift in safety-relevant representations, distorts their geometric structure, and introduces interference between task optimization and safety features. These effects collectively lead to increased harmful compliance. Motivated by these findings, we introduce REFUSALGUARD, a representation-level fine-tuning framework that preserves safety-relevant structure during model adaptation. Our approach constrains updates in hidden representation space, ensuring that safety-mediating components remain stable while allowing task-specific learning in complementary directions. We evaluate REFUSALGUARD across multiple model families, including LLaMA, Gemma, and Qwen, on adversarial safety benchmarks such as AdvBench, DirectHarm4, and JailbreakBench, as well as downstream utility tasks. Our approach achieves attack success rates comparable to base safety-aligned models while maintaining competitive task performance, significantly outperforming baselines.

---


### 117. [A Language for Describing Agentic LLM Contexts](https://arxiv.org/abs/2605.01920)

**<font color=#1a73e8>作者：</font>** Noga Peleg Pelc, Gal A. Kaminka, Yoav Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used within larger systems ("LLM agents"). These make a sequence of LLM calls, each call providing the LLM with a combination of instructions, observations, and interaction history. The design of the encoded information and its structure play a central role in the quality of the resulting system, leading to efforts spent on context engineering. It is therefore critical to communicate the composition of the LLM context in a system, and how it evolves over time. Yet, no standard exists for doing so: context construction is typically conveyed through informal prose, ad hoc diagrams, or direct inspection of code, none of which precisely capture how a prompt evolves across interaction steps or how two context representation strategies differ. To remedy this, we introduce the Agentic Context Description Language (ACDL), a language for specifying the structure and dynamics of LLM input contexts in a precise, readable, and standard manner, along with visualizations. ACDL provides constructs for specifying context aspects such as role message sequences, dynamic content, time-indexed references, and conditional or iterative structure, capturing the full architecture of a prompt independently of any particular implementation. ACDL diagrams can be hand drawn on a whiteboard, or written in formal language which can then be rendered. We describe the language, demonstrate it by documenting several existing systems and their variants, and encourage the community to adopt it for describing LLM systems context, both in day-to-day communication and in papers. Tooling, examples and documentation are available at this http URL.

---


### 118. [CADFS: A Big CAD Program Dataset and Framework for Computer-Aided Design with Large Language Models](https://arxiv.org/abs/2605.01925)

**<font color=#1a73e8>作者：</font>** Vladislav Pyatov, Gleb Bobrovskikh, Saveliy Galochkin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CADFS, a data-centric framework that enables large vision-language models to generate complex CAD design histories. Existing generative CAD systems are restricted to sketch-extrude operations due to simplified representations and limited datasets. We address this by introducing a FeatureScript-based representation and constructing a dataset of 450k real-world CAD models spanning 15 modeling operations. We obtain the dataset via a new pipeline that reconstructs clean, executable FeatureScript programs and provides multimodal annotations. Fine-tuning a VLM on this representation yields state-of-the-art results in text-conditioned CAD generation and image-based reconstruction, producing more accurate, diverse, and feature-rich designs than prior frameworks. Ablations show that each individual component of our framework, i.e., the FeatureScript representation, the extended operation set, and representation-aligned textual descriptions, significantly improves performance. Our framework substantially broadens the complexity and realism achievable in generative CAD. The CADFS framework and the new dataset are available at this https URL.

---


### 119. [StressEval: Failure-Driven Dynamic Benchmarking for Knowledge-Intensive Reasoning in Large Language Models](https://arxiv.org/abs/2605.01939)

**<font color=#1a73e8>作者：</font>** Yongrui Chen, Yangyang Ma, Xiaoying Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Static benchmarks for LLMs are increasingly compromised by contamination and overfitting especially on knowledge intensive reasoning tasks While recent dynamic benchmarks can alleviate staleness they often increase difficulty at the expense of answerability and controllability In this paper we propose StressEval a failure driven data synthesis framework that turns observed model failures into dynamic challenging and controllable test instances StressEval consists of three stages first it constructs a semi structured difficulty card that identifies the failed reasoning step and its root cause second it applies a dual perspective instance synthesis method that targets both knowledge gaps and reasoning breakdowns while preserving the underlying difficulty factors and third it applies a gating mechanism to retain only grounded unambiguous instances Seeding from multiple knowledge intensive reasoning datasets we employ StressEval to build Dynamic OneEval a focused suite of challenging dynamic benchmark Across several state of the art LLMs Dynamic OneEval yields substantially larger performance drops than the original benchmarks while retaining explicit difficulty factors enabling more actionable iteration

---


### 120. [Moira: Language-driven Hierarchical Reinforcement Learning for Pair Trading](https://arxiv.org/abs/2605.01954)

**<font color=#1a73e8>作者：</font>** Polydoros Giannouris, Yuechen Jiang, Lingfei Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many sequential decision-making problems exhibit hierarchical structure, where high-level semantic choices constrain downstream actions and feedback is delayed and ambiguous. Learning in such settings is challenging due to credit assignment: performance degradation may arise from flawed abstractions, suboptimal execution, or their interaction. We study this challenge through pair trading, a domain that naturally combines long-horizon semantic reasoning for asset pair selection with short-horizon execution under partial observability. We formulate pair trading as a hierarchical reinforcement learning problem and propose a language-driven optimization framework in which both high-level and low-level policies are parameterized by large language models (LLMs) and optimized exclusively through prompt updates. Our approach leverages pretrained LLMs as hierarchical policies and uses trajectory- and episode-level textual feedback to adapt abstractions and execution without gradient-based fine-tuning. By explicitly separating abstraction selection from execution, the framework reduces non-stationarity across hierarchical levels and enables targeted adaptation under delayed feedback. Experiments on real-world market data show consistent improvements over traditional and LLM-based baselines, demonstrating the effectiveness of language-driven hierarchical reinforcement learning.

---


### 121. [LLM-Augmented Semantic Steering of Text Embedding Projection Spaces](https://arxiv.org/abs/2605.01957)

**<font color=#1a73e8>作者：</font>** Wei Liu, Eric Krokos, Kirsten Whitley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Low-dimensional projections of text embeddings support visual analysis of document collections, but their spatial organization may not reflect the relationships an analyst intends to examine. Existing semantic interaction approaches encode semantic intent indirectly through geometric constraints or model updates, limiting interpretability and flexibility. We introduce LLM-augmented semantic steering, which enables analysts to express semantic intent by grouping a small set of example documents within the projection. A large language model externalizes this intent as natural-language representations and selectively extends it to related documents; the resulting semantic information is then incorporated into document representations via text augmentation or embedding-level blending, without retraining the underlying models. A case study illustrates how the same corpus can be reorganized from different semantic perspectives, while simulation-based evaluation shows that semantic steering improves global and local alignment with target semantic structures using only minimal interaction. Embedding-level blending further enables continuous and controllable steering of projection layouts. These results position projection spaces as intent-dependent semantic workspaces that can be reshaped through explicit, interpretable, language-mediated interaction.

---


### 122. [Multi-User Dueling Bandits: A Fair Approach using Nash Social Welfare](https://arxiv.org/abs/2605.01961)

**<font color=#1a73e8>作者：</font>** Maheed H. Ahmed, Mahsa Ghasemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from human preference data is becoming a useful tool, from fine-tuning large language models to training reinforcement learning agents. However, in most scenarios, the model is trained on the average preference of all human evaluators, which, under large variations of preferences, can be unfair to minority groups. In this work, we consider fairness in dueling bandits, a standard framework for online learning from preference data. We assume that each user has a (potentially distinct) Condorcet winner, which is an arm preferred to every other arm. Using these user-specific Condorcet winners as reference points, we evaluate and score arms according to their performance relative to the corresponding winner. To promote fairness across heterogeneous users, we adopt the well-established Nash Social Welfare objective, which maximizes the product of user utilities, thereby inherently penalizing inequality and preventing the marginalization of any single user. Within this framework, we construct a hard instance to establish a regret lower bound of $\Omega(T^{2/3}\min(K,D)^\frac{1}{3})$ for a time horizon $T$, $K$ arms, and $D$ users, which, to the best of our knowledge, is the first result quantifying the cost of fairness in dueling bandits with heterogeneous preferences. We then present the Fair-Explore-Then-Commit and Fair-$\epsilon$-Greedy algorithms with a Condorcet winner identification phase. We further derive their regret upper bounds that match the lower-bound dependence on $T$ up to logarithmic factors.

---


### 123. [MER-DG: Modality-Entropy Regularization for Multimodal Domain Generalization](https://arxiv.org/abs/2605.01967)

**<font color=#1a73e8>作者：</font>** Yavuz Yarici, Ghassan AlRegib  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying multimodal models in real-world scenarios requires generalization to new environments where recording conditions differ from training, a challenge known as multimodal domain generalization (MMDG). Standard architectures employ separate encoders for each modality and a fusion module, training the system end-to-end by optimizing on the fused features. In this paper, we identify that such joint optimization causes encoders to exploit cross-modal co-occurrences, statistical relationships between modalities that arise from source-specific recording conditions, rather than learning domain-invariant features. We term this failure mode Fusion Overfitting. To address this, we propose Modality-Entropy Regularization for Domain Generalization (MER-DG), which maximizes the entropy of each encoder's feature distribution to preserve feature diversity. MER-DG is architecture-agnostic and integrates into existing multimodal frameworks as an additive loss term. Extensive experiments on EPIC-Kitchens and HAC benchmarks demonstrate average improvements of approximately 5% over standard fusion and approximately 2% over state-of-the-art methods.

---


### 124. [Learn-to-learn on Arbitrary Textual Conditioning: A Hypernetwork-Driven Meta-Gated LLM](https://arxiv.org/abs/2605.01973)

**<font color=#1a73e8>作者：</font>** Luo Ji, Qi Qin, Ningyuan Xi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conventional LLMs may suffer from corpus heterogeneity and subtle condition changes. While finetuning can create the catastrophe forgetting issue, application of meta-learning on LLMs is also limited due to its complexity and scalability. In this paper, we activate the meta-signal of $\beta$ within the SwiGLU blocks, resulting in a meta-gating mechanism that adaptively adjusts the nonlinearity of FFN. A hypernetwork is employed which dynamically produces $\beta$ on textual conditions, providing meta-controllability on LLMs. By testing on different condition types such as task, domain, persona, and style, our method outperforms finetuning and meta-learning baselines, and can generalize reasonably on unseen tasks, condition types, or instructions. Our code can be found in this https URL.

---


### 125. [12 Angry AI Agents: Evaluating Multi-Agent LLM Decision-Making Through Cinematic Jury Deliberation](https://arxiv.org/abs/2605.01986)

**<font color=#1a73e8>作者：</font>** Ahmet Bahaddin Ersoz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What if the twelve jurors of Sidney Lumet's 12 Angry Men (1957) were not men, but large language models? Would the one juror who disagrees still be able to change everyone's mind? This paper instantiates that scenario as a multi-agent benchmark for LLM deliberation: twelve agents, each conditioned on a film-faithful persona, debate the film's murder case using multi-agent framework. Two models representing opposite ends of the RLHF spectrum are tested: GPT-4o (closed-source, heavy alignment) and Llama-4-Scout (open-weight, lighter alignment), across three conditions (baseline, open-minded prompt, no initial vote), with N = 3 replications per cell (18 runs total). Three findings emerge. (i) Seventeen of eighteen runs end in a hung jury (a state where the jury fails to reach a unanimous verdict); the film's central event, gradual minority-to-majority persuasion, almost never occurs, indicating that anchoring is the dominant failure mode of current LLMs in this setting. (ii) The two models exhibit sharply different internal dynamics: GPT-4o produces a mean of 1.0 vote changes per run across all conditions, while Llama-4-Scout ranges from 2.0 (baseline) to 6.0 (open-minded prompt), and is the only model to reach a NOT\_GUILTY verdict (1 of 3 runs in the no-initial-vote condition). The same ``open-minded'' instruction is internalized by Llama and ignored by GPT-4o. (iii) This asymmetry suggests that the intensity of RLHF alignment training, not model capability, is the primary determinant of deliberative flexibility in multi-agent settings. Flexibility, not capability, tracks human deliberation. The work is framed as an exploratory study and discusses implications for jury-of-LLMs evaluation and multi-agent debate.

---


### 126. [Enhancing Judgment Document Generation via Agentic Legal Information Collection and Rubric-Guided Optimization](https://arxiv.org/abs/2605.02011)

**<font color=#1a73e8>作者：</font>** Weihang Su, Xuanyi Chen, Yueyue Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automating the drafting of judgment documents is pivotal to judicial efficiency, yet it remains challenging due to the dual requirements of comprehensive retrieval of legal information and rigorous logical reasoning. Existing approaches, typically relying on standard Retrieval-Augmented Generation and Supervised Fine-Tuning, often suffer from insufficient evidence recall, hallucinated statutory references, and logically flawed legal reasoning. To bridge this gap, we propose Judge-R1, a unified framework designed to enhance LLM-based judgment document generation by jointly improving legal information collection and judgment document generation. First, we introduce Agentic Legal Information Collection, which employs a dynamic planning agent to retrieve precise statutes and precedents from multiple sources. Second, we implement Rubric-Guided Optimization, a reinforcement learning phase utilizing Group Relative Policy Optimization (GRPO) with a comprehensive legal reward function to enforce adherence to judicial standards and reasoning logic. Extensive experiments on the JuDGE benchmark demonstrate that Judge-R1 significantly outperforms state-of-the-art baselines in both legal accuracy and generation quality.

---


### 127. [Counting as a minimal probe of language model reliability](https://arxiv.org/abs/2605.02028)

**<font color=#1a73e8>作者：</font>** Tianxiang Dai, Jonathan Fan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models perform strongly on benchmarks in mathematical reasoning, coding and document analysis, suggesting a broad ability to follow instructions. However, it remains unclear whether such success reflects general logical competence, repeated application of learned procedures, or pattern matching that mimics rule execution. We investigate this question by introducing Stable Counting Capacity, an assay in which models count repeated symbols until failure. The assay removes knowledge dependencies, semantics and ambiguity from evaluation, avoids lexical and tokenization confounds, and provides a direct measure of procedural reliability beyond standard knowledge-based benchmarks. Here we show, across more than 100 model variants, that stable counting capacity remains far below advertised context limits. Model behavior is consistent neither with open-ended logic nor with stable application of a learned rule, but instead with use of a finite set of count-like internal states, analogous to counting on fingers. Once this resource is exhausted, the appearance of rule following disappears and exact execution collapses into guessing, even with additional test-time compute. These findings show that fluent performance in current language models does not guarantee general, reliable rule following.

---


### 128. [A Multimodal Dataset for Visually Grounded Ambiguity in Machine Translation](https://arxiv.org/abs/2605.02035)

**<font color=#1a73e8>作者：</font>** Jingheng Pan, Xintong Wang, Longyue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambiguity resolution is a key challenge in multimodal machine translation (MMT), where models must genuinely leverage visual input to map an ambiguous expression to its intended meaning. Although prior work has proposed disambiguation-oriented benchmarks that provide supportive evidence for the role of vision, we observe substantial issues in data quality and a mismatch with translation scenarios. Moreover, existing ambiguity-oriented evaluations are not well suited to broader ambiguity types in open-ended translation. To address these limitations, we present VIDA (Visually-Dependent Ambiguity), a dataset of 2,500 carefully curated instances in which resolving an annotated ambiguous source span requires visual evidence. We further propose Disambiguation-Centric Metrics that use an LLM-as-a-judge classifier to verify whether annotated ambiguous expressions are resolved correctly at the span level. Experiments with two state-of-the-art Large Vision Language Models under vanilla inference, supervised fine-tuning (SFT), and our chain-of-thought SFT (CoT-SFT) show that while SFT improves overall translation quality, CoT-SFT yields more consistent gains in disambiguation accuracy, especially on out-of-distribution subsets, indicating a stronger generalization for resolving diverse ambiguity types.

---


### 129. [What Single-Prompt Accuracy Misses: A Multi-Variant Reliability Audit of Language Models](https://arxiv.org/abs/2605.02038)

**<font color=#1a73e8>作者：</font>** Ranit Karmakar, Jayita Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-prompt accuracy is the dominant way to benchmark language models, but it can miss reliability failures that matter. We evaluate a 15-model open-weight corpus, with the main reliability analyses focused on 10 instruct models across five classification and reasoning benchmarks under five prompt variants each, measuring accuracy, token-probability calibration, verbal-confidence calibration, verbal parse rate, and prompt-perturbation spread for every (model x dataset x variant) cell. We find three broad results. First, evaluation design can materially change the conclusion. Switching Expected Calibration Error (ECE) token from a raw to a label-set-normalised definition changes per-cell calibration by a mean absolute 0.149. More strikingly, pairing a chain-of-thought prompt with a first-character evaluator on ARC-Challenge reduces apparent accuracy by 72-88% across all five primary models; two independent repair procedures recover 93.8% and 102.7% of the lost performance, indicating an evaluator-side rather than model-side failure. Second, confidence signals are fragile. On MMLU-Pro, every primary model verbally reports confidence substantially above both its accuracy and its token-probability confidence on the same rows, and verbal parse rate can collapse for a single model on a single prompt variant. Third, prompt robustness does not track parameter count reliably. Across 10 instruct models, the correlation between model size and prompt-perturbation spread ranges from -0.244 to 0.474 across benchmarks. Taken together, these results show that reliability conclusions for small language models depend not only on the model being evaluated, but also on the evaluation pipeline used to measure it. We argue that calibration definitions, evaluator logic, verbal parseability, and prompt robustness should be reported explicitly when making reliability claims.

---


### 130. [Pair2Score: Pairwise-to-Absolute Transfer for LLM-Based Essay Scoring](https://arxiv.org/abs/2605.02069)

**<font color=#1a73e8>作者：</font>** İbrahim Rıza Hallaç, Hasan Oğul  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many scoring applications require absolute predictions, while pairwise comparisons can provide a simpler learning objective. We present Pair2Score, a two-stage learning framework that transfers pairwise comparisons into absolute scoring with parameter-efficient LLaMA adaptation. Stage 1 trains a directional Siamese ranker on pairwise comparisons derived from absolute trait labels; Stage 2 trains an absolute predictor using configurable transfer strategies (warm-start and embedding-fusion variants). We evaluate on rubric-aligned Automated Essay Scoring (AES) traits (grammar, vocabulary, syntax) under a five-fold protocol that co-rotates held-out fold and random seed. At the trait level, the best-performing transfer variant improves quadratic weighted kappa (QWK) over an absolute-only baseline for all three traits. However, not all transfer configurations help: a one-epoch pairwise stage transfers more reliably than extended pairwise training, and transfer configuration -- not just the inclusion of a pairwise stage -- determines whether downstream scoring benefits.

---


### 131. [Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning](https://arxiv.org/abs/2605.02073)

**<font color=#1a73e8>作者：</font>** Arash Ahmadi, Sarah Sharif, Yaser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning is a key benchmark for large language models. Reinforcement learning is a standard post-training mechanism for improving the reasoning capabilities of large language models, yet performance remains sensitive to the design of the reward function that drives policy optimization. This paper introduces a search-driven framework that treats the reward specification itself as an object of optimization. The setting of interest is one in which the base model is held fixed and the reward specification is the primary remaining design lever. Candidate reward functions are generated by a frontier language model, validated automatically, screened through 500-step Group Relative Policy Optimization (GRPO) training runs on a Llama-3.2-3B-Instruct base model with Low-Rank Adaptation (LoRA), and ranked by F1 on the GSM8K test set. Ranked summaries from prior rounds are then fed back into the next round of generation. Over five rounds, the search produces 50 candidate rewards. The mean F1 rises from 0.596 in Round 1 to 0.632 in Round 5, and the top individual reward reaches F1 = 0.787. Seven ensemble configurations of top-ranked rewards are evaluated. The best ensemble achieves F1 = 0.795 (95% bootstrap CI [0.756, 0.832]) and accuracy 0.660 [0.635, 0.686], a 0.19 absolute F1 gain over a base-rewards-only GRPO baseline (F1 = 0.609). Pairwise McNemar tests with Bonferroni correction show all five-or-more-reward configurations are statistically indistinguishable at {\alpha} = 0.05/21. A three-seed re-training of the best ensemble yields F1 of 0.785. A randomly drawn 5-reward control collapses to F1 = 0.047, which shows that the ranked-feedback loop, not the additive signal of having more rewards, drives the gain.

---


### 132. [Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087)

**<font color=#1a73e8>作者：</font>** Chloe Li, Sara Price, Samuel Marks 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Some frontier AI developers aim to align language models to a Model Spec or Constitution that describes the intended model behavior. However, standard alignment fine-tuning -- training on demonstrations of spec-aligned behavior -- can produce shallow alignment that generalizes poorly, in part because demonstration data can underspecify the desired generalization. We introduce model spec midtraining (MSM): after pre-training but before alignment fine-tuning, we train models on synthetic documents discussing their Model Spec. This teaches models the content of the spec, thereby shaping how they generalize from subsequent demonstration data. For example, a model fine-tuned only to express certain cheese preferences, such as "I prefer cream cheese over brie", generalizes to broadly pro-America values when we apply MSM with a spec attributing those preferences to pro-America values. Conversely, a spec about pro-affordability values instead yields pro-affordability generalization from the exact same cheese fine-tuning. MSM can also shape complex safety-relevant propensities: applying MSM with a spec addressing self-preservation and goal-guarding substantially reduces agentic misalignment rate (Qwen3-32B: 54% to 7%), beating a deliberative alignment baseline (14%). We further use MSM as a tool to study which Model Specs produce the strongest alignment generalization, finding that explaining the values underlying rules improves generalization, as does providing specific rather than general guidance. Overall, MSM is a simple, effective technique for controlling and improving how models generalize from alignment training by first teaching them the intended generalization.

---


### 133. [Bridging the Gap Between Average and Discounted TD Learning](https://arxiv.org/abs/2605.02103)

**<font color=#1a73e8>作者：</font>** Haoxing Tian, Zaiwei Chen, Ioannis Ch. Paschalidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The analysis of Temporal Difference (TD) learning in the average-reward setting faces notable theoretical difficulties because the Bellman operator is not contractive with respect to any norm. This complicates standard analyses of stochastic updates that are effective in discounted settings. Although a considerable body of literature addresses these challenges, existing theoretical approaches come with limitations. We introduce a novel algorithm designed explicitly for policy evaluation in the average-reward setting, utilizing sampling from two Markovian trajectories. Our proposed method overcomes previous limitations by guaranteeing convergence to the unique solution of a properly defined projected Bellman equation. Notably, and in contrast to earlier work, our convergence analysis is uniformly applicable to both linear function approximation and tabular settings and does not involve explicit dimension-dependent terms in its convergence bounds. These results align with what is known to hold in the discounted setting. Furthermore, our algorithm achieves improved dependence on the problem's condition number, reducing the sample complexity from quartic, as in prior literature, to quadratic scaling, and thus matching the efficiency seen in the discounted setting.

---


### 134. [Ultrasound Vision-Language Alignment via Contrastive Learning](https://arxiv.org/abs/2605.02126)

**<font color=#1a73e8>作者：</font>** Zhuoyang Lyu, Yiyang Zhang, Tongxin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound foundation models have achieved strong performance on structured prediction tasks but remain exclusively vision-based, limiting zero-shot and few-shot transfer to novel tasks where task-specific annotation is scarce. We address this gap with EchoCare-CLIP, a CLIP-style dual-encoder contrastive framework that aligns ultrasound images with clinical text in a shared embedding space. We curate a multi-organ corpus of over 16K image-text pairs spanning breast, liver, lung, and thyroid, with over 78% of captions derived from expert-annotated reports, and complement the remainder with a three-tier template-based and LLM-based caption generation pipeline. We evaluate model configurations spanning two text encoder families (CLIP, BioClinicalBERT) and two caption strategies (template-based, LLM-generated) against OpenAI CLIP and BiomedCLIP baselines. Our trained models consistently improve cross-modal alignment over baselines, with the best configuration achieving a paired alignment score of 0.682. However, stronger alignment does not guarantee better downstream performance: CLIP-based variants with partial fine-tuning achieve the strongest zero-shot classification on external held-out datasets (0.709 on BUSI; 0.626 on AULI), while full end-to-end fine-tuning degrades transfer due to overfitting. On linear probing and few-shot adaptation, model rankings are dataset-dependent, reflecting a trade-off between domain adaptation and representational generalizability. We further show that template-based captions match or outperform LLM-generated captions, suggesting lexical diversity is not a proxy for caption quality. Taken together, our results demonstrate that ultrasound vision-language alignment is achievable from public data alone, but robust clinical transfer requires careful balancing of domain adaptation, encoder capacity, and caption supervision quality.

---


### 135. [From Where Things Are to What They Are For: Benchmarking Spatial-Functional Intelligence in Multimodal LLMs](https://arxiv.org/abs/2605.02130)

**<font color=#1a73e8>作者：</font>** Le Zhang, Jihan Yang, Soundarya Krishnan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-level agentic intelligence extends beyond low-level geometric perception, evolving from recognizing where things are to understanding what they are for. While existing benchmarks effectively evaluate the geometric perception capabilities of multimodal large language models (MLLMs), they fall short of probing the higher-order cognitive abilities required for grounded intelligence. To address this gap, we introduce the Spatial-Functional Intelligence Benchmark (SFI-Bench), a video-based benchmark with over 1,500 expert-annotated questions derived from diverse egocentric indoor video scans. SFI-Bench systematically evaluates two complementary dimensions of advanced reasoning: (1) Structured Spatial Reasoning, which requires understanding complex layouts and forming coherent spatial representations, and (2) Functional Reasoning, which involves inferring object affordances and their context-dependent utility. The benchmark includes tasks such as conditional counting, multi-hop relational reasoning, functional pairing, and knowledge-grounded troubleshooting, directly challenging models to integrate perception, memory, and inference. Our experiments reveal that current MLLMs consistently struggle to combine spatial memory with functional reasoning and external knowledge, highlighting a critical bottleneck in achieving grounded intelligence. SFI-Bench therefore provides a diagnostic tool for measuring progress toward more cognitively capable and truly grounded multimodal agents.

---


### 136. [LUMINA: A Grid Foundation Model for Benchmarking AC Optimal Power Flow Surrogate Learning](https://arxiv.org/abs/2605.02133)

**<font color=#1a73e8>作者：</font>** Hongwei Jin, Keunju Song, Zeeshan Memon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AC optimal power flow (ACOPF) is foundational yet computationally expensive in power grid operations, driving learning-based surrogates for large-scale grid analysis. These surrogates, however, often fail to generalize across network topologies, a critical gap for deployment on grids not seen during training and for routine operational what-if studies. We introduce LUMINA-Bench, a comprehensive benchmark suite for ACOPF surrogate learning covering multi-topology pretraining, transfer, and adaptation. The benchmark evaluates homogeneous and heterogeneous architectures under single- and multi-topology learning settings using unified metrics that capture both predictive accuracy and physics-informed constraint violations. We additionally compare constraint-aware training objectives, including MSE, augmented Lagrangian, and violation-based Lagrangian losses, to characterize accuracy-robustness trade-offs across settings. Data processing, training, and evaluation frameworks are open-sourced as the LUMINA suite to support reproducibility and accelerate future research on feasibility-aware OPF surrogates.

---


### 137. [Retrieval and Multi-Hop Reasoning in 1M-Token Context Windows: Evaluating LLMs on Classical Chinese Text](https://arxiv.org/abs/2605.02173)

**<font color=#1a73e8>作者：</font>** Eric H. C. Chow  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate the long-context retrieval and reasoning capabilities of five frontier large language models with advertised 1M-token context windows on a classical Chinese corpus. Two complementary studies are reported. Test 1 measures single-needle retrieval at 1M tokens of input, with three biographical needles planted at three depths and pairs of real (training-prior-consistent) and altered (training-prior-contradicting) variants to separate genuine in-context retrieval from reliance on memorised training data. Test 2, a follow-up designed to probe whether long-context capability degrades when retrieval requires intermediate reasoning, measures three-hop chain traversal across three context tiers (256K, 512K, and 1M tokens). We find that single-needle retrieval at 1M is essentially solved for the strongest models - Gemini 3.1 Pro, Claude Opus 4.7, and GPT-5.5 each achieve 100% - but that multi-hop performance reveals three distinct decay signatures: a stable regime (Gemini Pro, Claude) maintaining greater than 80% accuracy through 512K with modest degradation at 1M; a late-cliff regime (GPT-5.5, Qwen3.6-plus) collapsing sharply between 512K and 1M; and a smooth-decline regime (DeepSeek V4 Pro) decaying gradually across the entire range. The findings suggest that nominal context-window length is a poor proxy for usable long-context multi-hop capability, and that the sharpest discriminator between current 1M-context flagships is the 512K-to-1M transition.

---


### 138. [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.02178)

**<font color=#1a73e8>作者：</font>** Haixin Wang, Hejie Cui, Chenwei Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in multi-turn reinforcement learning (RL) has significantly improved reasoning LLMs' performances on complex interactive tasks. Despite advances in stabilization techniques such as fine-grained credit assignment and trajectory filtering, instability remains pervasive and often leads to training collapse. We argue that this instability stems from inefficient exploration in multi-turn settings, where policies continue to generate low-information actions that neither reduce uncertainty nor advance task progress. To address this issue, we propose Token- and Turn-level Policy Optimization (T$^2$PO), an uncertainty-aware framework that explicitly controls exploration at fine-grained levels. At the token level, T$^2$PO monitors uncertainty dynamics and triggers a thinking intervention once the marginal uncertainty change falls below a threshold. At the turn level, T$^2$PO identifies interactions with negligible exploration progress and dynamically resamples such turns to avoid wasted rollouts. We evaluate T$^2$PO in diverse environments, including WebShop, ALFWorld, and Search QA, demonstrating substantial gains in training stability and performance improvements with better exploration efficiency. Code is available at: this https URL.

---


### 139. [MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing](https://arxiv.org/abs/2605.02199)

**<font color=#1a73e8>作者：</font>** Nishant Bhargava, Rodrigo Sobral Barrento  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term LLM agents must compress streams of past interactions into persistent memory before future queries are known. Existing evaluations usually measure final question-answering accuracy, which entangles memory writing with retrieval, prompting, and reader reasoning. We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budgeted long-term memory writing. A MEMAUDIT package fixes an experience stream, candidate memory representations, storage costs, semantic evidence units, future-query requirements, and a budget, turning write-time memory selection into a finite auditable optimization problem with a certified denominator. We instantiate this protocol with a concave-over-modular semantic coverage objective under storage and one-representation-per-experience constraints, and compute exact package optima using branch-and-bound with MILP certification. Across controlled exact packages, validity-heavy stress tests, human-audited natural support slices, and exported Mem0, A-Mem, and Letta stores, MEMAUDIT separates representation quality, validity-state preservation, and budget-aware selection effects that end-to-end QA cannot localize. The resulting artifact provides reusable package generators, certified solvers, natural package exports, external-system scorers, and cached reproducibility metadata for evaluating what memory writers actually preserve under fixed storage budgets.

---


### 140. [CBV: Clean-label Backdoor Attacks on Vision Language Models via Diffusion Models](https://arxiv.org/abs/2605.02202)

**<font color=#1a73e8>作者：</font>** Ji Guo, Xiaolong Qin, Cencen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved remarkable success in tasks such as image captioning and visual question answering (VQA). However, as their applications become increasingly widespread, recent studies have revealed that VLMs are vulnerable to backdoor attacks. Existing backdoor attacks on VLMs primarily rely on data poisoning by adding visual triggers and modifying text labels, where the induced image-text mismatch makes poisoned samples easy to detect. To address this limitation, we propose the Clean-Label Backdoor Attack on VLMs via Diffusion Models (CBV), which leverages diffusion models to generate natural poisoned examples via score matching. Specifically, CBV modifies the score during the reverse generation process of the diffusion model to guide the generation of poisoned samples that contain triggered image features. To further enhance the effectiveness of the attack, we incorporate the textual information of the triggered images as multimodal guidance during generation. Moreover, to enhance stealthiness, we introduce a GradCAM-guided Mask (GM) that restricts modifications to only the most semantically important regions, rather than the entire image. We evaluate our method on MSCOCO and VQA v2 with four representative VLMs, achieving over 80% ASR while preserving normal functionality.

---


### 141. [Metric Unreliability in Multimodal Machine Unlearning: A Systematic Analysis and Principled Unified Score](https://arxiv.org/abs/2605.02206)

**<font color=#1a73e8>作者：</font>** Abdullah Ahmad Khan, Hamid Laga, Ferdous Sohel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in Vision-Language Models (VLMs) is required for compliance with the General Data Protection Regulation (GDPR), yet current evaluation practices are inconsistent. We present the first systematic study of metric reliability in multimodal unlearning. Five standard metrics, Forget Accuracy (FA), Retain Accuracy (RA), Membership Inference Attack (MIA), Activation Distance (AD), and JS divergence (JS), yield conflicting method rankings across three VQA benchmarks (MLLMU-Bench, UnLOK-VQA, MMUBench). Kendall tau analysis over 36 unlearned LLaVA-1.5-7B models reveals two opposing clusters, {FA, RA, MIA} and {AD, JS}, with tau_FA_AD = -0.26, reproduced on BLIP-2 OPT-2.7B. Agreement is lower in multimodal VQA (average tau = 0.086) than in unimodal classification (average tau = 0.158; difference = 0.072), indicating that dual image-and-text pathways amplify inconsistency. We introduce the Unified Quality Score (UQS), a composite metric with weights derived from each metric's Spearman correlation with the oracle distance d(M_hat, M_star), where M_star is the oracle model retrained only on the retain set. RA shows the strongest reliability (rho = 0.484, p = 0.003), while FA is negatively correlated (rho = -0.418, p = 0.011). UQS yields stable rankings under 100 random weight perturbations (tau = 0.647 +- 0.262). We release the benchmark, 36 checkpoints, and an interactive leaderboard. Code and pre-computed results are available at this https URL.

---


### 142. [MultiSense-Pneumo: A Multimodal Learning Framework for Pneumonia Screening in Resource-Constrained Settings](https://arxiv.org/abs/2605.02207)

**<font color=#1a73e8>作者：</font>** Dineth Jayakody, Pasindu Thenahandi, Chameli Dommanige  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pneumonia remains a leading global cause of morbidity and mortality, particularly in low resource settings where access to imaging, laboratory testing, and specialist care is limited. Clinical assessment relies on heterogeneous evidence, including symptoms, respiratory patterns, and chest imaging, making screening inherently multimodal. However, many existing computational approaches remain unimodal and focus primarily on radiographs. In this work, we present MultiSense-Pneumo, a multimodal framework for pneumonia oriented screening and triage support that integrates structured symptom descriptors, cough audio, spoken language, and chest radiographs. The system combines deterministic symptom triage, LightGBM based acoustic classification, domain adversarial radiograph analysis using ResNet 18, transformer based speech recognition, and an interpretable multimodal fusion operator. Each modality is transformed into a normalized risk signal and aggregated into a unified screening estimate, enabling transparent and modular decision support. MultiSense-Pneumo is designed for real world deployment under modest computational constraints and can operate fully offline on standard laptop class hardware, making it suitable for community health workers, rural clinics, and emergency response settings. Experimental results demonstrate robustness of the radiograph pathway under domain shifts, while highlighting limitations in minority class recall for acoustic signals. MultiSense-Pneumo is intended as a research prototype for screening and triage support rather than a clinically validated diagnostic system.

---


### 143. [CoVSpec: Efficient Device-Edge Co-Inference for Vision-Language Models via Speculative Decoding](https://arxiv.org/abs/2605.02218)

**<font color=#1a73e8>作者：</font>** Yuanyuan Jia, Shunpu Tang, Qianqian Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated strong capabilities in multimodal perception and reasoning. However, deploying large VLMs on mobile devices remains challenging due to their substantial computational and memory demands. A practical alternative is device-edge co-inference, where a lightweight draft VLM on the mobile device collaborates with a larger target VLM on the edge server via speculative decoding. Nevertheless, directly extending speculative decoding to VLMs suffers from severe inefficiency due to excessive visual-token computation and high communication overhead. To address these challenges, we propose CoVSpec, an efficient collaborative speculative decoding framework for VLM inference. Specifically, we first develop a training-free visual token reduction framework that prunes redundant visual tokens on the mobile device by jointly considering query relevance, token activity, and low-rank dependency. Moreover, we design an adaptive drafting strategy that dynamically adjusts both the verification frequency and the draft length. In addition, we introduce a parallel branching mechanism with decoupled verification-correction to improve draft-side utilization during target-side verification and reduce correction-related transmission overhead. Experiments on multiple benchmarks show that CoVSpec achieves up to 2.21x higher throughput than target-only inference and reduces communication overhead by more than 96% compared with baselines, without compromising task accuracy.

---


### 144. [Perturbation Dose Responses in Recursive LLM Loops: Raw Switching, Stochastic Floors, and Persistent Escape under Append, Replace, and Dialog Updates](https://arxiv.org/abs/2605.02236)

**<font color=#1a73e8>作者：</font>** Pawel Kaplanski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive language-model loops often settle into recognizable attractor-like patterns. The practical question is how much injected text is needed to move a settled loop somewhere else, and whether that move lasts. We study this in 30-step recursive loops by separating the model from the context-update rule: append, replace, and dialog updates expose different histories to the same generator. The main result is that persistent redirection in append-mode recursive loops is memory-policy-conditioned. Under a 12,000-character tail clip, destination-coherent persistence plateaus near 16 percent and retained source-basin escape near 36 percent at dose 400; neither crosses 50 percent. Under a full-history protocol, retained source-basin escape crosses 50 percent near 400 tokens and saturates at 75-80 percent by 1,500 tokens, while destination-coherent persistence first reaches 0.50 near 1,500 tokens with a Wilson 95 percent CI of [0.41, 0.61]. For raw switching, adversarial continuations yield an ED50 near 40 tokens, with paired-control floors near 35 percent and net switching never reaching +50 percentage points within 5-400 tokens. Replace-mode raw switching is near-saturated but largely reflects state-reset overwrite: insert-mode probes drop it to 12-32 percent. A homogeneous-perturbation control reproduced the high-dose non-monotonic dip in destination-coherent persistence, refuting perturbation heterogeneity as the cause; the dip appears structural, with mechanism unresolved. We report 37 experiments on gpt-4o-mini with within-vendor replication on gpt-4.1-nano. Recursive-loop evaluations should distinguish transient movement from durable escape, subtract stochastic floors, and treat context-update rules as first-class safety-relevant design choices.

---


### 145. [PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://arxiv.org/abs/2605.02240)

**<font color=#1a73e8>作者：</font>** Ruoqi Liu, Imran Q. Mohiuddin, Austin J. Schoeffler 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce PhysicianBench, a benchmark for evaluating LLM agents on physician tasks grounded in real clinical setting within electronic health record (EHR) environments. Existing medical agent benchmarks primarily focus on static knowledge recall, single-step atomic actions, or action intent without verifiable execution against the environment. As a result, they fail to capture the long-horizon, composite workflows that characterize real clinical systems. PhysicianBench comprises 100 long-horizon tasks adapted from real consultation cases between primary care and subspecialty physicians, with each task independently reviewed by a separate panel of physicians. Tasks are instantiated in an EHR environment with real patient records and accessed through the same standard APIs used by commercial EHR vendors. Tasks span 21 specialties (e.g., cardiology, endocrinology, oncology, psychiatry) and diverse workflow types (e.g., diagnosis interpretation, medication prescribing, treatment planning), requiring an average of 27 tool calls per task. Solving each task requires retrieving data across encounters, reasoning over heterogeneous clinical information, executing consequential clinical actions, and producing clinical documentation. Each task is decomposed into structured checkpoints (670 in total across the benchmark) capturing distinct stages of completion graded by task-specific scripts with execution-grounded verification. Across 13 proprietary and open-source LLM agents, the best-performing model achieves only 46% success rate (pass@1), while open-source models reach at most 19%, revealing a substantial gap between current agent capabilities and the demands of real-world clinical workflows. PhysicianBench provides a realistic and execution-grounded benchmark for measuring progress toward autonomous clinical agents.

---


### 146. [Zero-Shot Confidence Estimation for Small LLMs: When Supervised Baselines Aren't Worth Training](https://arxiv.org/abs/2605.02241)

**<font color=#1a73e8>作者：</font>** Luong N. Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How reliably can a small language model estimate its own correctness? The answer determines whether local-to-cloud routing-escalating queries a cheap local model cannot handle-can work without supervised training data. As inference costs dominate large language model (LLM) deployment budgets, routing most queries to a cheap local model while reserving expensive cloud calls for hard cases is an increasingly common cost-control strategy. We compare zero-shot confidence signals against RouteLLM-style supervised baselines across three 7-8B model families and two datasets (1,000 and 500 queries per model, respectively). Average token log-probability, which requires no training data, matches or exceeds supervised baselines in-distribution (Area Under the Receiver Operating Characteristic curve (AUROC) 0.650-0.714 vs. 0.644-0.676) and substantially outperforms them out-of-distribution (0.717-0.833 vs. 0.512-0.564), because it measures a property of the model's generation rather than the query distribution. This paper further proposes retrieval-conditional self-assessment, a pre-generation signal that selectively injects retrieved knowledge when similarity is high, improving over bare self-assessment by up to +0.069 AUROC at 3-10x lower latency than log-probability. A supervised baseline trained on 1,000 labeled examples never exceeds the zero-shot signal. We release all code, data, and experiment logs.

---


### 147. [Fine-Tuning Impairs the Balancedness of Foundation Models in Long-tailed Personalized Federated Learning](https://arxiv.org/abs/2605.02247)

**<font color=#1a73e8>作者：</font>** Shihao Hou, Chikai Shang, Zhiheng Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning (PFL) with foundation models has emerged as a promising paradigm enabling clients to adapt to heterogeneous data distributions. However, real-world scenarios often face the co-occurrence of non-IID data and long-tailed class distributions, presenting unique challenges that remain underexplored in PFL. In this paper, we investigate this long-tailed personalized federated learning and observe that current methods suffer from two limitations: (i) fine-tuning degrades performance below zero-shot baselines due to the erosion of inherent class balance in foundation models; (ii) conventional personalization techniques further transfer this bias to local models through parameter or feature-level fusion. To address these challenges, we propose Federated Learning via Gradient Purification and Residual Learning (FedPuReL), which preserves balanced knowledge in the global model while enabling unbiased personalization. Specifically, we purify local gradients using zero-shot predictions to maintain a class-balanced global model, and model personalization as residual correction atop the frozen global model. Extensive experiments demonstrate that FedPuReL consistently outperforms state-of-the-art methods, achieving superior performance on both global and personalized models across diverse long-tailed scenarios. The code is available at this https URL.

---


### 148. [SpectraDINO: Bridging the Spectral Gap in Vision Foundation Models via Lightweight Adapters](https://arxiv.org/abs/2605.02258)

**<font color=#1a73e8>作者：</font>** Yagiz Nalcakan, Hyeongjin Ju, Incheol Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Foundation Models (VFMs) pretrained on large-scale RGB data have demonstrated remarkable representation quality, yet their applicability to multispectral imaging spanning Near-Infrared (NIR), Short-Wave Infrared (SWIR), and Long-Wave Infrared (LWIR) remains largely unexplored. These spectral modalities offer complementary sensing capabilities critical for robust perception in adverse conditions, but present a fundamental domain gap relative to RGB-centric pretrained models. We present SpectraDINO, a multispectral VFM that bridges this spectral gap by extending DINOv2 ViT backbones to beyond-visible modalities through lightweight, per-modality bottleneck adapters, while preserving the rich representations of the frozen RGB backbone. We introduce a multi-stage teacher-student training protocol in which a frozen DINOv2 teacher guides a spectral student via cosine distillation, symmetric contrastive loss, patch-level alignment, and a novel neighborhood-structure-preservation loss. This staged curriculum enables strong cross-modal alignment without catastrophic forgetting of RGB priors. We evaluate SpectraDINO on multispectral object detection and semantic segmentation across challenging NIR, SWIR, and LWIR benchmarks using widely adopted fusion strategies. SpectraDINO achieves state-of-the-art performance across most benchmarks, validating its effectiveness as a general-purpose backbone for spectral generalization. The code and weights for model variants are available at this https URL.

---


### 149. [From 'Here' to 'There': Exploring Proximity Semantics in Multimodal Data Exploration](https://arxiv.org/abs/2605.02261)

**<font color=#1a73e8>作者：</font>** Dennis Bromley, Diana Wang, Vidya Setlur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern data exploration tools often struggle to capture the subtleties of analytical intent, especially when users seek patterns that are difficult to specify using traditional query methods or natural language alone. We introduce a multimodal research probe for querying time-series and geospatial data that integrates free-form sketching, natural language, and visual annotations within a unified interaction space. Users articulate queries by sketching trends or spatial paths and augmenting them with annotations and analytical directives grounded in shared spatial and temporal context. The system employs a hybrid architecture combining geometric sketch matching and visual language models (VLMs) to support queries that interleave pattern matching and semantic constraints. Through a preliminary study with 20 participants, we observed recurring interaction patterns in which participants used spatial, temporal, and visual proximity to relate sketches, annotations, and language. Rather than treating these as isolated inputs, participants relied on their relative placement to disambiguate meaning. We analyze these behaviors as evidence for proximity semantics (PS), a form of deictic disambiguation in which meaning is shaped by the closeness of multimodal elements within a shared interaction space. We present PS as a conceptual lens grounded in observed user behavior, and discuss its implications for the design of future multimodal data exploration systems.

---


### 150. [Break the Block: Dynamic-size Reasoning Blocks for Diffusion Large Language Models via Monotonic Entropy Descent with Reinforcement Learning](https://arxiv.org/abs/2605.02263)

**<font color=#1a73e8>作者：</font>** Yan Jiang, Ruihong Qiu, Zi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent diffusion large language models (dLLMs) have demonstrated both effectiveness and efficiency in reasoning via a block-based semi-autoregressive generation paradigm. Despite their progress, the fixed-size block generations remain a critical bottleneck for effective and coherent reasoning. 1. From a global perspective, different reasoning tasks would correspond to different optimal decoding block sizes, which makes a ``one-size-fits-all'' assumption ineffective. 2. Even within a single reasoning task, the rigid block partitioning would break the logical flow and reduce reasoning coherence. Through empirical observations, we reveal that for block-wise entropy, incorrect reasoning exhibits a fluctuating and unsteady trend between blocks, whereas the correctly generated tasks follow a consistent descending trend. Therefore, this paper proposes b1, a novel post-training framework for dLLMs that learns dynamic-size reasoning blocks via a Monotonic Entropy Descent objective with reinforcement learning to enhance reasoning coherence.b1 integrates seamlessly as a plug-and-play module with existing dLLM's post-training algorithms. Extensive experiments across various reasoning benchmarks showcase b1's consistent improvement over existing fixed-size block baselines. Our code has been released at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
