# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 301. [Real-Time Cellist Postural Evaluation With On-Device Computer Vision](https://arxiv.org/abs/2604.17530)

**<font color=#1a73e8>作者：</font>** Paolo Wang, Michael Zhang, Shrinand Perumal 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Posture is a critical factor for beginning instrumental learners. Most students receive instruction only once a week, and during the intervals between lessons they have little or no feedback on their physical posture. As a result, posture often deteriorates, increasing the risk of musculoskeletal injury and inefficient technique. Recent advances in computer vision and machine learning make it possible to evaluate posture without the constant presence of a human expert. However, current solutions have been extremely limited in availability and convenience due to their reliance on computationally expensive hardware or multi-sensor setups. We present Cello Evaluator, a real-time postural feedback system for practicing cellists. Through this optimization for on-device computer vision inference, we provide access to cellist postural evaluation to anyone with a current generation Android phone and thus reduces the postural feedback voids within individual practice. To validate our mobile application, we conduct a heuristic evaluation consisting of cellist and UX experts. Overall feedback from the evaluation found the app to be user friendly and helpful.

---


### 302. [Dual Strategies for Test-Time Adaptation](https://arxiv.org/abs/2604.17542)

**<font color=#1a73e8>作者：</font>** Nam Nguyen Phuong, Duc Nguyen The Minh, Phi Le Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional test-time adaptation (TTA) approaches typically adapt the model using only a small fraction of test samples, often those with low-entropy predictions, thereby failing to fully leverage the available information in the test distribution. This paper introduces DualTTA, a novel framework that improves performance under distribution shifts by utilizing a larger and more diverse set of test samples. DualTTA identifies two distinct groups: one where the model's predictions are likely consistent with the underlying semantics, and another where predictions are likely incorrect. For the first group, it minimizes prediction entropy to reinforce reliable decisions; for the second, it maximizes entropy to suppress overconfident errors and unlearn spurious behavior. These groups are adaptively selected using a new reliability criterion that measures prediction stability under both semantic-preserving and semantic-altering transformations, addressing the limitations of purely entropy-based selection. We further provide theoretical analysis and empirical justification showing that our approach enables a tighter separation between reliable and unreliable samples, in the context of their suitability for adaptation, leading to provably more effective model updates.

---


### 303. [Contraction and Hourglass Persistence for Learning on Graphs, Simplices, and Cells](https://arxiv.org/abs/2604.17548)

**<font color=#1a73e8>作者：</font>** Mattie Ji, Indradyumna Roy, Vikas Garg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent homology (PH) encodes global information, such as cycles, and is thus increasingly integrated into graph neural networks (GNNs). PH methods in GNNs typically traverse an increasing sequence of subgraphs. In this work, we first expose limitations of this inclusion procedure. To remedy these shortcomings, we analyze contractions as a principled topological operation, in particular, for graph representation learning. We study the persistence of contraction sequences, which we call Contraction Homology (CH). We establish that forward PH and CH differ in expressivity. We then introduce Hourglass Persistence, a class of topological descriptors that interleave a sequence of inclusions and contractions to boost expressivity, learnability, and stability. We also study related families parametrized by two paradigms. We also discuss how our framework extends to simplicial and cellular networks. We further design efficient algorithms that are pluggable into end-to-end differentiable GNN pipelines, enabling consistent empirical improvements over many PH methods across standard real-world graph datasets. Code is available at \href{this https URL}{this https URL}.

---


### 304. [SVL: Goal-Conditioned Reinforcement Learning as Survival Learning](https://arxiv.org/abs/2604.17551)

**<font color=#1a73e8>作者：</font>** Franki Nguimatsia Tiofack, Fabian Schramm, Théotime Le Hellard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard approaches to goal-conditioned reinforcement learning (GCRL) that rely on temporal-difference learning can be unstable and sample-inefficient due to bootstrapping. While recent work has explored contrastive and supervised formulations to improve stability, we present a probabilistic alternative, called survival value learning (SVL), that reframes GCRL as a survival learning problem by modeling the time-to-goal from each state as a probability distribution. This structured distributional Monte Carlo perspective yields a closed-form identity that expresses the goal-conditioned value function as a discounted sum of survival probabilities, enabling value estimation via a hazard model trained via maximum likelihood on both event and right-censored trajectories. We introduce three practical value estimators, including finite-horizon truncation and two binned infinite-horizon approximations to capture long-horizon objectives. Experiments on offline GCRL benchmarks show that SVL combined with hierarchical actors matches or surpasses strong hierarchical TD and Monte Carlo baselines, excelling on complex, long-horizon tasks.

---


### 305. [SoK: Reshaping Research on Network Intrusion Detection Systems](https://arxiv.org/abs/2604.17556)

**<font color=#1a73e8>作者：</font>** Giovanni Apruzzese  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network Intrusion Detection Systems (NIDS) have been studied for decades. Hundreds of papers have, e.g., proposed ways to enhance, harden or bypass NIDS. However, the findings of prior literature are hardly reflected in real-world operational contexts. Such a disconnection is problematic for research itself: it is unclear what scenario envisioned by prior work can be used as a baseline for future advancements.
We argue that a key reason for this disconnection is a fundamental misunderstanding of intrinsic characteristics of NIDS. For instance, the fact that a compromised NIDS cannot be expected to work well; the fact that some evaluations are done without carrying out any experiment in a (even synthetic) "real" network; the fact that security operators triage high-level reports -- and not individual samples flagged by some classifier. In this SoK, which is primarily a reflective piece, we first constructively highlight such quintessential properties (without criticizing _any_ work by different authors) by stating three Assertions. Then, we provide recommendations -- further emphasized through an original and reproducible case study that challenges some established practices. Ultimately, we seek to lay a foundation to reshape research on NIDS.

---


### 306. [UniGeo: Unifying Geometric Guidance for Camera-Controllable Image Editing via Video Models](https://arxiv.org/abs/2604.17565)

**<font color=#1a73e8>作者：</font>** Hong Jiang, Wensong Song, Zongxing Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-controllable image editing aims to synthesize novel views of a given scene under varying camera poses while strictly preserving cross-view geometric consistency. However, existing methods typically rely on fragmented geometric guidance, such as only injecting point clouds at the representation level despite models containing multiple levels, and are mainly based on image diffusion models that operate on discrete view mappings. These two limitations jointly lead to geometric drift and structural degradation under continuous camera motion.
We observe that while leveraging video models provides continuous viewpoint priors for camera-controllable image editing, they still struggle to form stable geometric understanding if geometric guidance remains fragmented. To systematically address this, we inject unified geometric guidance across three levels that jointly determine the generative output: representation, architecture, and loss function.
To this end, we propose UniGeo, a novel camera-controllable editing framework. Specifically, at the representation level, UniGeo incorporates a frame-decoupled geometric reference injection mechanism to provide robust cross-view geometry context. At the architecture level, it introduces geometric anchor attention to align multi-view features. At the loss function level, it proposes a trajectory-endpoint geometric supervision strategy to explicitly reinforce the structural fidelity of target views.
Comprehensive experiments across multiple public benchmarks, encompassing both extensive and limited camera motion settings, demonstrate that UniGeo significantly outperforms existing methods in both visual quality and geometric consistency.

---


### 307. [Diverse Dictionary Learning](https://arxiv.org/abs/2604.17568)

**<font color=#1a73e8>作者：</font>** Yujia Zheng, Zijian Li, Shunxing Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given only observational data $X = g(Z)$, where both the latent variables $Z$ and the generating process $g$ are unknown, recovering $Z$ is ill-posed without additional assumptions. Existing methods often assume linearity or rely on auxiliary supervision and functional constraints. However, such assumptions are rarely verifiable in practice, and most theoretical guarantees break down under even mild violations, leaving uncertainty about how to reliably understand the hidden world. To make identifiability actionable in the real-world scenarios, we take a complementary view: in the general settings where full identifiability is unattainable, what can still be recovered with guarantees, and what biases could be universally adopted? We introduce the problem of diverse dictionary learning to formalize this view. Specifically, we show that intersections, complements, and symmetric differences of latent variables linked to arbitrary observations, along with the latent-to-observed dependency structure, are still identifiable up to appropriate indeterminacies even without strong assumptions. These set-theoretic results can be composed using set algebra to construct structured and essential views of the hidden world, such as genus-differentia definitions. When sufficient structural diversity is present, they further imply full identifiability of all latent variables. Notably, all identifiability benefits follow from a simple inductive bias during estimation that can be readily integrated into most models. We validate the theory and demonstrate the benefits of the bias on both synthetic and real-world data.

---


### 308. [MAPLE: A Meta-learning Framework for Cross-Prompt Essay Scoring](https://arxiv.org/abs/2604.17569)

**<font color=#1a73e8>作者：</font>** Salam Albatarni, May Bashendy, Sohaila Eltanbouly 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated Essay Scoring (AES) faces significant challenges in cross-prompt settings, where models must generalize to unseen writing prompts. To address this limitation, we propose MAPLE, a meta-learning framework that leverages prototypical networks to learn transferable representations across different writing prompts. Across three diverse datasets (ELLIPSE and ASAP (English), and LAILA (Arabic)), MAPLE achieves state-of-the-art performance on ELLIPSE and LAILA, outperforming strong baselines by 8.5 and 3 points in QWK, respectively. On ASAP, where prompts exhibit heterogeneous score ranges, MAPLE yields improvements on several traits, highlighting the strengths of our approach in unified scoring settings. Overall, our results demonstrate the potential of meta-learning for building robust cross-prompt AES systems.

---


### 309. [Recovery Guarantees for Continual Learning of Dependent Tasks: Memory, Data-Dependent Regularization, and Data-Dependent Weights](https://arxiv.org/abs/2604.17578)

**<font color=#1a73e8>作者：</font>** Liangzu Peng, Uday Kiran Reddy Tadipatri, Ziqing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) is concerned with learning multiple tasks sequentially without forgetting previously learned tasks. Despite substantial empirical advances over recent years, the theoretical development of CL remains in its infancy. At the heart of developing CL theory lies the challenge that the data distribution varies across tasks, and we argue that properly addressing this challenge requires understanding this variation--dependency among tasks. To explicitly model task dependency, we consider nonlinear regression tasks and propose the assumption that these tasks are dependent in such a way that the data of the current task is a nonlinear transformation of previous data. With this model and under natural assumptions, we prove statistical recovery guarantees (more specifically, bounds on estimation errors) for several CL paradigms in practical use, including experience replay with data-independent regularization and data-independent weights that balance the losses of tasks, replay with data-dependent weights, and continual learning with data-dependent regularization (e.g., knowledge distillation). To the best of our knowledge, our bounds are informative in cases where prior work gives vacuous bounds.

---


### 310. [How Much Data is Enough? The Zeta Law of Discoverability in Biomedical Data, featuring the enigmatic Riemann zeta function](https://arxiv.org/abs/2604.17581)

**<font color=#1a73e8>作者：</font>** Paul M. Thompson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How much data is enough to make a scientific discovery? As biomedical datasets scale to millions of samples and AI models grow in capacity, progress increasingly depends on predicting when additional data will substantially improve performance. In practice, model development often relies on empirical scaling curves measured across architectures, modalities, and dataset sizes, with limited theoretical guidance on when performance should improve, saturate, or exhibit cross-over behavior.
We propose a scaling-law framework for cross-modal discoverability based on spectral structure of data covariance operators, task-aligned signal projections, and learned representations. Many performance metrics, including AUC, can be expressed in terms of cumulative signal-to-noise energy accumulated across identifiable spectral modes of an encoder and cross-modal operator. Under mild assumptions, this accumulation follows a zeta-like scaling law governed by power-law decay of covariance spectra and aligned signal energy, leading naturally to the appearance of the Riemann zeta function. Representation learning methods such as sparse models, low-rank embeddings, and multimodal contrastive objectives improve sample efficiency by concentrating useful signal into earlier stable modes, effectively steepening spectral decay and shifting scaling curves.
The framework predicts cross-over regimes in which simpler models perform best at small sample sizes, while higher-capacity or multimodal encoders outperform them once sufficient data stabilizes additional degrees of freedom. Applications include multimodal disease classification, imaging genetics, functional MRI, and topological data analysis. The resulting zeta law provides a principled way to anticipate when scaling data, improving representations, or adding modalities is most likely to accelerate discovery.

---


### 311. [DIRCR: Dual-Inference Rule-Contrastive Reasoning for Solving RAVENs](https://arxiv.org/abs/2604.17584)

**<font color=#1a73e8>作者：</font>** Jiachen Zhang, Chengtai Li, Jianfeng Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abstract visual reasoning remains challenging as existing methods often prioritize either global context or local row-wise relations, failing to integrate both, and lack intermediate feature constraints, leading to incomplete rule capture and entangled representations. To address these issues, we propose the Dual-Inference Rule-Contrastive Reasoning (DIRCR) model. Its core component, the Dual-Inference Reasoning Module, combines a local path for row-wise analogical reasoning and a global path for holistic inference, integrated via a gated attention mechanism. Additionally, a Rule-Contrastive Learning Module introduces pseudo-labels to construct positive and negative rule samples, applying contrastive learning to enhance feature separability and promote abstract, transferable rule learning. Experimental results on three RAVEN datasets demonstrate that DIRCR significantly enhances reasoning robustness and generalization. Codes are available at this https URL.

---


### 312. [Refresher Training through Digital and Physical, Card-Based Game for Accredited Social Health Activists (ASHAs) and Anganwadi Workers (AWWs) in India](https://arxiv.org/abs/2604.17604)

**<font color=#1a73e8>作者：</font>** Arka Majhi, Aparajita Mondal, Satish B. Agnihotri  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> India's recent health surveys have highlighted a worrying trend of incomplete child immunization rates across several district clusters in India. Conventional training methods for community healthcare workers (CHWs) in India are inadequate for improving their skills and knowledge. Smartphone games could be a viable and cost-effective method of refresher training specifically targeting immunization practices. A refresher training game was designed both as a physical card-based and digital app-based game, focusing on enhancing CHWs' knowledge and practices related to child immunization. A quasi-experimental study was conducted with 368 participants. Quantitative gameplay analytics and qualitative feedback from players were collected through interviews. The findings show that game-based refresher training significantly improves CHWs' knowledge gain and retention in the area of child immunization. The discussion highlights the study's implications and insights while developing effective digital tools for training CHWs. The research contributes to the growing body of work on digital tools for training CHWs in resource-constrained settings. The study underscores the potential of smartphone games as a scalable and effective method of refresher training for improving child immunization rates.

---


### 313. [Conditional Attribution for Root Cause Analysis in Time-Series Anomaly Detection](https://arxiv.org/abs/2604.17616)

**<font color=#1a73e8>作者：</font>** Shashank Mishra, Karan Patil, Cedric Schockaert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) for time-series anomaly detection is critical for the reliable operation of complex real-world systems. Existing explanation methods often rely on unrealistic feature perturbations and ignore temporal and cross-feature dependencies, leading to unreliable attributions. We propose a conditional attribution framework that explains anomalies relative to contextually similar normal system states. Instead of using marginal or randomly sampled baselines, our method retrieves representative normal instances conditioned on the anomalous observation, enabling dependency-preserving and operationally meaningful explanations. To support high-dimensional time-series data, contextual retrieval is performed in learned low-dimensional representations using both variational autoencoder latent spaces and UMAP manifold embeddings. By grounding the retrieval process in the system's learned manifold, this strategy avoids out-of-distribution artifacts and ensures attribution fidelity while maintaining computational efficiency. We further introduce confidence-aware and temporal evaluation metrics for assessing explanation reliability and responsiveness. Experiments on the SWaT and MSDS benchmarks demonstrate that the proposed approach consistently improves root-cause identification accuracy, temporal localization, and robustness across multiple anomaly detection models. These results highlight the practical utility of conditional attribution for explainable anomaly diagnosis in complex time-series systems. Code and models will be publicly released.

---


### 314. [Refresher Training through Quiz App for capacity building of Community Healthcare Workers or Anganwadi Workers in India](https://arxiv.org/abs/2604.17620)

**<font color=#1a73e8>作者：</font>** Arka Majhi, Satish B. Agnihotri, Aparajita Mondal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> High and persistent child malnutrition levels with tardy reduction, seen in successive health surveys, continue to be a matter of concern in India, drawing attention to the need to revamp the four-decade-old Government program, Integrated Child Development Scheme (ICDS). ICDS field functionaries or Anganwadi Workers' (AWWs) capacity deficit was identified as a significant factor affecting ICDS's effectiveness. Considering rising numbers, over 1.4 million AWWs, and continuously advancing knowledge of community healthcare, conventional training pedagogy is ineffective in building and updating AWWs and their supervisors' capacity, which calls for rethinking, using the ICT approach. Over 6 lakh AWWs in India were smartphone equipped by 2020. An android based quiz app was designed, following AWWs training modules' content and need assessment results. The study investigates the quiz app's effectiveness and compares it with conventional classroom instruction, with a group of AWWs, and discusses ways to make it an adequate substitute.

---


### 315. [STRIKE: Additive Feature-Group-Aware Stacking Framework for Credit Default Prediction](https://arxiv.org/abs/2604.17622)

**<font color=#1a73e8>作者：</font>** Swattik Maiti, Ritik Pratap Singh, Fardina Fathmiul Alam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit risk default prediction remains a cornerstone of risk management in the financial industry. The task involves estimating the likelihood that a borrower will fail to meet debt obligations, an objective critical for lending decisions, portfolio optimization, and regulatory compliance. Traditional machine learning models such as logistic regression and tree-based ensembles are widely adopted for their interpretability and strong empirical performance. However, modern credit datasets are high-dimensional, heterogeneous, and noisy, increasing overfitting risk in monolithic models and reducing robustness under distributional shift. We introduce STRIKE (Stacking via Targeted Representations of Isolated Knowledge Extractors), a feature-group-aware stacking framework for structured tabular credit risk data. Rather than training a single monolithic model on the complete dataset, STRIKE partitions the feature space into semantically coherent groups and trains independent learners within each group. This decomposition is motivated by an additive perspective on risk modeling, where distinct feature sources contribute complementary evidence that can be combined through a structured aggregation. The resulting group-specific predictions are integrated through a meta-learner that aggregates signals while maintaining robustness and modularity. We evaluate STRIKE on three real-world datasets spanning corporate bankruptcy and consumer lending scenarios. Across all settings, STRIKE consistently outperforms strong tree-based baselines and conventional stacking approaches in terms of AUC-ROC. Ablation studies confirm that performance gains stem from meaningful feature decomposition rather than increased model complexity. Our findings demonstrate that STRIKE is a stable, scalable, and interpretable framework for credit risk default prediction tasks.

---


### 316. [ViPS: Video-informed Pose Spaces for Auto-Rigged Meshes](https://arxiv.org/abs/2604.17623)

**<font color=#1a73e8>作者：</font>** Honglin Chen, Karran Pandey, Rundi Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Kinematic rigs provide a structured interface for articulating 3D meshes, but they lack an inherent representation of the plausible manifold of joint configurations for a given asset. Without such a pose space, stochastic sampling or manual manipulation of raw rig parameters often leads to semantic or geometric violations, such as anatomical hyperextension and non-physical self-intersections. We propose Video-informed Pose Spaces (ViPS), a feed-forward framework that discovers the latent distribution of valid articulations for auto-rigged meshes by distilling motion priors from a pretrained video diffusion model. Unlike existing methods that rely on scarce artist-authored 4D datasets, ViPS transfers generative video priors into a universal distribution over a given rig parameterization. Differentiable geometric validators applied to the skinned mesh enforce asset-specific validity without requiring manual regularizers. Our model learns a smooth, compact, and controllable pose space that supports diverse sampling, manifold projection for inverse kinematics, and temporally coherent trajectories for keyframing. Furthermore, the distilled 3D pose samples serve as precise semantic proxies for guiding video diffusion, effectively closing the loop between generative 2D priors and structured 3D kinematic control. Our evaluations show that ViPS, trained solely on video priors, matches the performance of state-of-the-art methods trained on synthetic artist-created 4D data in both plausibility and diversity. Most importantly, as a universal model, ViPS demonstrates robust zero-shot generalization to out-of-distribution species and unseen skeletal topologies.

---


### 317. [Developing Models of Procedural Skills using an AI-assisted Text-to-Model Approach](https://arxiv.org/abs/2604.17624)

**<font color=#1a73e8>作者：</font>** Rahul K. Dass, Shubham Puri, Arpit Khandelwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scalable AI tutoring for procedural skill learning requires structured knowledge representations, yet constructing these representations remains a labor-intensive bottleneck. This paper presents a human-in-the-loop text-to-model pipeline that uses large language models to transform instructional materials into schema-complete Task-Method-Knowledge models of procedural skills through ontology-constrained prompting and template-based generation. The approach automates structural scaffolding while preserving expert oversight for validating causal transitions and failure conditions. We apply the pipeline to instructional materials from a graduate-level online AI course, constructing 23 procedural skill models. AI-assisted authoring reduced expert modeling time by 50-70% while producing structurally valid and highly reproducible models under fixed-input conditions. We evaluate structural validity, semantic alignment, reproducibility, and refinement effort to characterize authoring scalability. Results indicate that AI-assisted text-to-model methods can substantially lower the cost of constructing structured procedural representations, making course-wide deployment of structured AI coaching systems practically feasible.

---


### 318. [FlowC2S: Flowing from Current to Succeeding Frames for Fast and Memory-Efficient Video Continuation](https://arxiv.org/abs/2604.17625)

**<font color=#1a73e8>作者：</font>** Hovhannes Margaryan, Quentin Bammey, Christian Sandor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a novel methodology for generating fast and memory-efficient video continuations. Our method, dubbed FlowC2S, fine-tunes a pre-trained text-to-video flow model to learn a vector field between the current and succeeding video chunks. Two design choices are key. First, we introduce inherent optimal couplings, utilizing temporally adjacent video chunks during training as a practical proxy for true optimal couplings, resulting in straighter flows. Second, we incorporate target inversion, injecting the inverted latent of the target chunk into the input representation to strengthen correspondences and improve visual fidelity. By flowing directly from current to succeeding frames, instead of the common combination of current frames with noise to generate a video continuation, we reduce the dimensionality of the model input by a factor of two. The proposed method, fine-tuned from LTXV and Wan, surpasses the state-of-the-art scores across quantitative evaluations with FID and FVD, with as few as five neural function evaluations.

---


### 319. [Toward Reusability of AI Models Using Dynamic Updates of AI Documentation](https://arxiv.org/abs/2604.17626)

**<font color=#1a73e8>作者：</font>** Peter Bajcsy, Walid Keyrouz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work addresses the challenge of disseminating reusable artificial intelligence (AI) models accompanied by AI documentation (a.k.a., AI model cards). The work is motivated by the large number of trained AI models that are not reusable due to the lack of (a) AI documentation and (b) the temporal lag between rapidly changing requirements on AI model reusability and those specified in various AI model cards. Our objectives are to shorten the lag time in updating AI model card templates and align AI documentation more closely with current AI best practices.
Our approach introduces a methodology for delivering agile, data-driven, and community-based AI model cards. We use the Hugging Face (HF) repository of AI models, populated by a subset of the AI research and development community, and the AI consortium-based Zero Draft (ZD) templates for the AI documentation of AI datasets and AI models, as our test datasets. We also address questions about the value of AI documentation for AI reusability.
Our work quantifies the correlations between AI model downloads/likes (i.e., AI model reuse metrics) from the HF repository and their documentation alignment with the ZD documentation templates using tables of contents and word statistics (i.e., AI documentation quality metrics). Furthermore, our work develops the infrastructure to regularly compare AI documentation templates against community-standard practices derived from millions of uploaded AI models in the Hugging Face repository. The impact of our work lies in introducing a methodology for delivering agile, data-driven, and community-based standards for documenting AI models and improving AI model reuse.

---


### 320. [Copy First, Translate Later: Interpreting Translation Dynamics in Multilingual Pretraining](https://arxiv.org/abs/2604.17633)

**<font color=#1a73e8>作者：</font>** Felicia Körner, Maria Matveev, Florian Eichin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit impressive cross-lingual capabilities. However, prior work analyzes this phenomenon through isolated factors and at sparse points during training, limiting our understanding of how cross-lingual generalization emerges--particularly in the early phases of learning. To study the early trajectory of linguistic and translation capabilities, we pretrain a multilingual 1.7B model on nine diverse languages, capturing checkpoints at a much finer granularity. We further introduce a novel word-level translation dataset and trace how translation develops over training through behavioral analyses, model-component analysis, and parameter-based ablations. We find that the model quickly acquires basic linguistic capabilities in parallel with token-level copying, while translation develops in two distinct phases: an initial phase dominated by copying and surface-level similarities, and a second phase in which more generalizing translation mechanisms are developed while copying is refined. Together, these findings provide a fine-grained view of how cross-lingual generalization develops during multilingual pretraining.

---


### 321. [Replay, Revise, and Refresh: Smartphone-based Refresher Training for Community Healthcare Workers in India](https://arxiv.org/abs/2604.17638)

**<font color=#1a73e8>作者：</font>** Arka Majhi, Aparajita Mondal, Satish B. Agnihotri  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In India, community healthcare workers are the primary touchpoints between the state and the beneficiaries, such as pregnant mothers and children. Their healthcare knowledge directly impacts the quality of care they provide through home visits and community activities. Classroom in-person or traditional ways of training are found ineffective in imparting knowledge and render poor knowledge retention, which needs reinforcements through short, frequent revisions. Smartphone games on healthcare topics could be a promising solution as a refresher, as they can be scaled and tailored as per players' requirements. This study aims to check the differences in knowledge gain, pre and post-intervention, and, secondly, to check knowledge retention after six months. 270 CHWs or participants were recruited to evaluate different modes of refresher training and assigned into three equal groups of 90 each. The control group (CG) (n=90) was trained using the standard classroom method, which is usually followed. Intervention Group-1 (IG1)(n=90) was trained in a physical card game format, and Intervention Group-2 (IG2)(n=90) was trained in a smartphone game format. 4 sets of questionnaires were made by shuffling 45 questions based on immunization of equal weightage. The questionnaires were filled out by CHWs by hand and collected, evaluated, and analyzed. Paired t-tests were conducted to compare pre-post knowledge increments and repeated measure ANOVA to check for differences in knowledge retention. Results suggest a significant difference in scores in all three groups. A significant difference was observed between the physical and digital gameplay modes. Pre-post knowledge increment was higher in the digital mode (p<0.05), but knowledge retained was not significantly different (p=.4) in digital and physical card versions.

---


### 322. [ThreadSumm: Summarization of Nested Discourse Threads Using Tree of Thoughts](https://arxiv.org/abs/2604.17648)

**<font color=#1a73e8>作者：</font>** Olubusayo Olabisi, Ekata Mitra, Ameeta Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Summarizing deeply nested discussion threads requires handling interleaved replies, quotes, and overlapping topics, which standard LLM summarizers struggle to capture reliably. We introduce ThreadSumm, a multi-stage LLM framework that treats thread summarization as a hierarchical reasoning problem over explicit aspect and content unit representations. Our method first performs content planning via LLM-based extraction of discourse aspects and Atomic Content Units, then applies sentence ordering to construct thread-aware sequences that surface multiple viewpoints rather than a single linear strand. On top of these interpretable units, ThreadSumm employs a Tree of Thoughts search that generates and scores multiple paragraph candidates, jointly optimizing coherence and coverage within a unified search space. With this multi-proposal and iterative refinement design, we show improved performance in generating logically structured summaries compared to existing baselines, while achieving higher aspect retention and opinion coverage in nested discussions.

---


### 323. [Self-Supervised Super-Resolution for Sentinel-5P Hyperspectral Images](https://arxiv.org/abs/2604.17652)

**<font color=#1a73e8>作者：</font>** Hyam Omar Ali, Antoine Crosnier, Romain Abraham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sentinel-5P (S5P) plays a critical role in atmospheric monitoring; however, its spatial resolution limits fine-scale analysis. Existing super-resolution (SR) approaches rely on supervised learning with synthetic low-resolution (LR) data, since true high-resolution (HR) data do not exist, limiting their applicability to real observations. We propose a self-supervised hyperspectral SR framework for S5P that enables training without HR ground truth. The method combines Stein's Unbiased Risk Estimator (SURE) with an equivariant imaging constraint, incorporating the S5P degradation operator and noise statistics derived from signal-to-noise ratio (SNR) metadata. We also introduce depthwise separable convolution U-Net architectures designed for efficiency and spectral fidelity. The framework is evaluated in two settings: (i) LR-HR, where synthetic LR data are used for direct comparison with supervised learning, and (ii) GT-SHR, where super-resolved images surpass the native spatial resolution without HR reference. Results across multiple bands show that self-supervised models achieve performance comparable to supervised methods while maintaining strong consistency. Qualitative analysis shows improved spatial detail over bicubic interpolation, and validation with EMIT data confirms that reconstructed structures are physically meaningful. Code is available at this https URL

---


### 324. [PV-SQL: Synergizing Database Probing and Rule-based Verification for Text-to-SQL Agents](https://arxiv.org/abs/2604.17653)

**<font color=#1a73e8>作者：</font>** Yuan Tian, Tianyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems often struggle with deep contextual understanding, particularly for complex queries with subtle requirements. We present PV-SQL, an agentic framework that addresses these failures through two complementary components: Probe and Verify. The Probe component iteratively generates probing queries to retrieve concrete records from the database, resolving ambiguities in value formats, column semantics, and inter-table relationships to build richer contextual understanding. The Verify component employs a rule-based method to extract verifiable conditions and construct an executable checklist, enabling iterative SQL refinement that effectively reduces missing constraints. Experiments on the BIRD benchmarks show that PV-SQL outperforms the best text-to-SQL baseline by 5% in execution accuracy and 20.8% in valid efficiency score while consuming fewer tokens.

---


### 325. [Towards Self-Improving Error Diagnosis in Multi-Agent Systems](https://arxiv.org/abs/2604.17658)

**<font color=#1a73e8>作者：</font>** Jiazheng Li, Emine Yilmaz, Bei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based Multi-Agent Systems (MAS) enable complex problem-solving but introduce significant debugging challenges, characterized by long interaction traces, inter-agent dependencies, and delayed error manifestation. Existing diagnostic approaches often rely on expensive expert annotation or ''LLM-as-a-judge'' paradigms, which struggle to pinpoint decisive error steps within extended contexts. In this paper, we introduce ErrorProbe, a self-improving framework for semantic failure attribution that identifies responsible agents and the originating error step. The framework operates via a three-stage pipeline: (1) operationalizing the MAS failure taxonomy to detect local anomalies, (2) performing symptom-driven backward tracing to prune irrelevant context, and (3) employing a specialized multi-agent team (Strategist, Investigator, Arbiter) to validate error hypotheses through tool-grounded execution. Crucially, ErrorProbe maintains a verified episodic memory that updates only when error patterns are confirmed by executable evidence, without the need for annotation. Experiments across the TracerTraj and Who&When benchmarks demonstrate that ErrorProbe significantly outperforms baselines, particularly in step-level localization, while the verified memory enables robust cross-domain transfer without retraining.

---


### 326. [Peerispect: Claim Verification in Scientific Peer Reviews](https://arxiv.org/abs/2604.17667)

**<font color=#1a73e8>作者：</font>** Ali Ghorbanpour, Soroush Sadeghian, Alireza Daghighfarsoodeh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer review is central to scientific publishing, yet reviewers frequently include claims that are subjective, rhetorical, or misaligned with the submitted work. Assessing whether review statements are factual and verifiable is crucial for fairness and accountability. At the scale of modern conferences and journals, manually inspecting the grounding of such claims is infeasible. We present Peerispect, an interactive system that operationalizes claim-level verification in peer reviews by extracting check-worthy claims from peer reviews, retrieving relevant evidence from the manuscript, and verifying the claims through natural language inference. Results are presented through a visual interface that highlights evidence directly in the paper, enabling rapid inspection and interpretation. Peerispect is designed as a modular Information Retrieval (IR) pipeline, supporting alternative retrievers, rerankers, and verifiers, and is intended for use by reviewers, authors, and program committees. We demonstrate Peerispect through a live, publicly available demo (this https URL) and API services (this https URL), accompanied by a video tutorial (this https URL).

---


### 327. [Original Sin of npm: A Study on Vulnerability Propagation in JavaScript Dependency Networks](https://arxiv.org/abs/2604.17668)

**<font color=#1a73e8>作者：</font>** Michael Robinson, Sajal Halder, Muhammad Ejaz Ahmed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Understanding vulnerability propagation is essential for assessing how vulnerabilities spread across components of a software package. This supports more accurate impact analysis and enhances threat detection and mitigation. In this paper, we investigate how a small number of vulnerable JavaScript packages contribute to the creation of a disproportionately large number of vulnerable packages. This paper presents insights from 1,515 reported vulnerabilities gathered from a custom-built vulnerability database containing 1,077,946 JavaScript packages sourced from `npm-follower' and their associated dependency networks. Dependency networks were constructed using the this http URL API, with vulnerabilities identified by parsing package names and version numbers through the Google Open Source Vulnerability API.
Our findings reveal that 61.30% (660,748) of packages are reliant on one or more dependency packages, and 21.60% (232,836) of total packages have at least one known vulnerability throughout their dependency networks -- of which most (42%) are of High severity. We also found that it takes, on average, approximately 4 years and 11 months to fix a vulnerable package from when the first vulnerable version is published on npm -- although publication times of vulnerabilities occur approximately 19 days after a fix is available. Finally, we observe a high concentration of frequently present vulnerabilities throughout dependency networks, with the top-7 most frequent vulnerabilities accounting for 25% of vulnerability cases and the top-23 most frequent accounting for 50%. Based on these findings, we propose recommendations for developers and package managers to mitigate the threat and occurrence of vulnerabilities within the npm dependency network and the broader software repository community.

---


### 328. [Low Light Image Enhancement Challenge at NTIRE 2026](https://arxiv.org/abs/2604.17669)

**<font color=#1a73e8>作者：</font>** George Ciubotariu, Sharif S M A, Abdur Rehman 等 91 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive review of the NTIRE 2026 Low Light Image Enhancement Challenge, highlighting the proposed solutions and final results. The objective of this challenge is to identify effective networks capable of producing clearer and visually compelling images in diverse and challenging conditions by learning representative visual cues with the purpose of restoring information loss due to low-contrast and noisy images. A total of 195 participants registered for the first track and 153 for the second track of the competition, and 22 teams ultimately submitted valid entries. This paper thoroughly evaluates the state-of-the-art advances in (joint denoising and) low-light image enhancement, showcasing the significant progress in the field, while leveraging samples of our novel dataset.

---


### 329. [Prior-Fitted Functional Flow: In-Context Generative Models for Pharmacokinetics](https://arxiv.org/abs/2604.17670)

**<font color=#1a73e8>作者：</font>** César Ojeda, Niklas Hartung, Wilhelm Huisinga 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Prior-Fitted Functional Flows, a generative foundation model for pharmacokinetics that enables zero-shot population synthesis and individual forecasting without manual parameter tuning. We learn functional vector fields, explicitly conditioned on the sparse, irregular data of an entire study population. This enables the generation of coherent virtual cohorts as well as forecasting of partially observed patient trajectories with calibrated uncertainty. We construct a new open-access literature corpus to inform our priors, and demonstrate state-of-the-art predictive accuracy on extensive real-world datasets.

---


### 330. [Grokking of Diffusion Models: Case Study on Modular Addition](https://arxiv.org/abs/2604.17673)

**<font color=#1a73e8>作者：</font>** Joon Hyeok Kim, Yong-Hyun Park, Mattis Dalsætra Østby 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their empirical success, how diffusion models generalize remains poorly understood from a mechanistic perspective. We demonstrate that diffusion models trained with flow-matching objectives exhibit grokking--delayed generalization after overfitting--on modular addition, enabling controlled analysis of their internal computations. We study this phenomenon across two levels of data regime. In a single-image regime, mechanistic dissection reveals that the model implements modular addition by composing periodic representations of individual operands. In a diverse-image regime with high intraclass variability, we find that the model leverages its iterative sampling process to partition the task into an arithmetic computation phase followed by a visual denoising phase, separated by a critical timestep threshold. Our work provides the mechanistic decomposition of algorithmic learning in diffusion models, revealing how these models bridge continuous pixel-space generation and discrete symbolic reasoning.

---


### 331. [Towards Intelligent Legal Document Analysis: CNN-Driven Classification of Case Law Texts](https://arxiv.org/abs/2604.17674)

**<font color=#1a73e8>作者：</font>** Moinul Hossain, Sourav Rabi Das, Zikrul Shariar Ayon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal practitioners and judicial institutions face an ever-growing volume of case-law documents characterised by formalised language, lengthy sentence structures, and highly specialised terminology, making manual triage both time-consuming and error-prone. This work presents a lightweight yet high-accuracy framework for citation-treatment classification that pairs lemmatisation-based preprocessing with subword-aware FastText embeddings and a multi-kernel one-dimensional Convolutional Neural Network (CNN). Evaluated on a publicly available corpus of 25,000 annotated legal documents with a 75/25 training-test partition, the proposed system achieves 97.26% classification accuracy and a macro F1-score of 96.82%, surpassing established baselines including fine-tuned BERT, Long Short-Term Memory (LSTM) with FastText, CNN with random embeddings, and a Term Frequency-Inverse Document Frequency (TF-IDF) k-Nearest Neighbour (KNN) classifier. The model also attains the highest Area Under the Receiver Operating Characteristic (AUC-ROC) curve of 97.83% among all compared systems while operating with only 5.1 million parameters and an inference latency of 0.31 ms per document - more than 13 times faster than BERT. Ablation experiments confirm the individual contribution of each pipeline component, and the confusion matrix reveals that residual errors are confined to semantically adjacent citation categories. These findings indicate that carefully designed convolutional architectures represent a scalable, resource-efficient alternative to heavyweight transformers for intelligent legal document analysis.

---


### 332. [Dual-stream Spatio-Temporal GCN-Transformer Network for 3D Human Pose Estimation](https://arxiv.org/abs/2604.17688)

**<font color=#1a73e8>作者：</font>** Jiawen Duan, Jian Xiang, Zhiqiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D human pose estimation is a classic and important research direction in the field of computer vision. In recent years, Transformer-based methods have made significant progress in lifting 2D to 3D human pose estimation. However, these methods primarily focus on modeling global temporal and spatial relationships, neglecting local skeletal relationships and the information interaction between different channels. Therefore, we have proposed a novel method,the Dual-stream Spatio-temporal GCN-Transformer Network (MixTGFormer). This method models the spatial and temporal relationships of human skeletons simultaneously through two parallel channels, achieving effective fusion of global and local features. The core of MixTGFormer is composed of stacked Mixformers. Specifically, the Mixformer includes the Mixformer Block and the Squeeze-and-Excitation Layer ( SE Layer). It first extracts and fuses various information of human skeletons through two parallel Mixformer Blocks with different modes. Then, it further supplements the fused information through the SE Layer. The Mixformer Block integrates Graph Convolutional Networks (GCN) into the Transformer, enhancing both local and global information utilization. Additionally, we further implement its temporal and spatial forms to extract both spatial and temporal relationships. We extensively evaluated our model on two benchmark datasets (Human3.6M and MPI-INF-3DHP). The experimental results showed that, compared to other methods, our MixTGFormer achieved state-of-the-art results, with P1 errors of 37.6mm and 15.7mm on these datasets, respectively.

---


### 333. [CAPO: Counterfactual Credit Assignment in Sequential Cooperative Teams](https://arxiv.org/abs/2604.17693)

**<font color=#1a73e8>作者：</font>** Shripad Deshmukh, Jayakumar Subramanian, Raghavendra Addanki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In cooperative teams where agents act in a fixed order and share a single team reward, it is hard to know how much each agent contributed, and harder still when agents are updated one at a time because data collected earlier no longer reflects the new policies. We introduce the Sequential Aristocrat Utility (SeqAU), the unique per-agent learning signal that maximizes the individual learnability of each agent's action, extending the classical framework of Wolpert and Tumer (2002) to this sequential setting. From SeqAU we derive CAPO (Counterfactual Advantage Policy Optimization), a critic-free policy-gradient algorithm. CAPO fits a per-agent reward decomposition from group rewards and computes the per-agent advantage in closed form plus a handful of forward passes through the current policy, requiring no extra environment calls beyond the initial batch. We give analytic bias and variance bounds and validate them on a controlled sequential bandit, where CAPO's advantage over standard baselines grows with the team size. The framework is general; multi-LLM pipelines are a natural deployment target.

---


### 334. [Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play](https://arxiv.org/abs/2604.17696)

**<font color=#1a73e8>作者：</font>** Xiachong Feng, Deyi Yin, Xiaocheng Feng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Games offer a compelling paradigm for developing general reasoning capabilities in language models, as they naturally demand strategic planning, probabilistic inference, and adaptive decision-making. However, existing self-play approaches rely solely on terminal game outcomes, providing no mechanism to distinguish transferable reasoning patterns from game-specific heuristics. We present STRATAGEM, which addresses two fundamental barriers to reasoning transfer: domain specificity, where learned patterns remain anchored in game semantics, and contextual stasis, where static game contexts fail to cultivate progressive reasoning. STRATAGEM selectively reinforces trajectories exhibiting abstract, domain-agnostic reasoning through a Reasoning Transferability Coefficient, while incentivizing adaptive reasoning development via a Reasoning Evolution Reward. Experiments across mathematical reasoning, general reasoning, and code generation benchmarks demonstrate substantial improvements, with particularly strong gains on competition-level mathematics where multi-step reasoning is critical. Ablation studies and human evaluation confirm that both components contribute to transferable reasoning.

---


### 335. [Co-evolving Agent Architectures and Interpretable Reasoning for Automated Optimization](https://arxiv.org/abs/2604.17708)

**<font color=#1a73e8>作者：</font>** Jiahao Huang, Peilan Xu, Xiaoya Nan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating operations research (OR) with large language models (LLMs) remains limited by hand-crafted reasoning--execution workflows. Complex OR tasks require adaptive coordination among problem interpretation, mathematical formulation, solver selection, code generation, and iterative debugging. To address this limitation, we propose EvoOR-Agent, a co-evolutionary framework for automated optimization. The framework represents agent workflows as activity-on-edge (AOE)-style networks, making workflow topology, execution dependencies, and alternative reasoning paths explicit. On this representation, the framework maintains an architecture graph and evolves a population of reasoning individuals through graph-mediated path-conditioned recombination, multi-granularity semantic mutation, and elitist population update. A knowledge-base-assisted experience-acquisition module further injects reusable OR practices into initialization and semantic variation. Empirical results on heterogeneous OR benchmarks show that the proposed framework consistently improves over zero-shot LLMs, fixed-pipeline OR agents, and representative evolutionary agent frameworks. Case studies and ablation analyses further indicate that explicit architecture evolution and graph-supported reasoning-trajectory search contribute to both performance improvement and structural interpretability. These results suggest that treating agent architectures and reasoning trajectories as evolvable objects provides an effective route toward adaptive and interpretable automated optimization.

---


### 336. [Modeling Higher-Order Brain Interactions via a Multi-View Information Bottleneck Framework for fMRI-based Psychiatric Diagnosis](https://arxiv.org/abs/2604.17713)

**<font color=#1a73e8>作者：</font>** Kunyu Zhang, Qiang Li, Vince D. Calhoun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resting-state functional magnetic resonance imaging (fMRI) has emerged as a cornerstone for psychiatric diagnosis, yet most approaches rely on pairwise brain cortical or sub-cortical connectivities that overlooks higher-order interactions (HOIs) central to complex brain dynamics. While hypergraph methods encode HOIs through predefined hyperedges, their construction typically relies on heuristic similarity metrics and does not explicitly characterize whether interactions are synergy- or redundancy-dominated. In this paper, we introduce $O$-information, a signed measure that characterizes the informational nature of HOIs, and integrate third- and fourth-order $O$-information into a unified multi-view information bottleneck framework for fMRI-based psychiatric diagnosis. To enable scalable $O$-information estimation, we further develop two independent acceleration strategies: a Gaussian analytical approximation and a randomized matrix-based Rényi entropy estimator, achieving over a 30-fold computational speedup compared with conventional estimators. Our tri-view architecture systematically fuses pairwise, triadic, and tetradic brain interactions, capturing comprehensive brain connectivity while explicitly penalizing redundancy. Extensive evaluation across four benchmark datasets (REST-meta-MDD, ABIDE, UCLA, ADNI) demonstrates consistent improvements, outperforming 11 baseline methods including state-of-the-art graph neural network (GNN) and hypergraph based approaches. Moreover, our method reveals interpretable region-level synergy-redundancy patterns which are not explicitly characterized by conventional hypergraph formulations.

---


### 337. [FlashFPS: Efficient Farthest Point Sampling for Large-Scale Point Clouds via Pruning and Caching](https://arxiv.org/abs/2604.17720)

**<font color=#1a73e8>作者：</font>** Yuzhe Fu, Hancheng Ye, Cong Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Point-based Neural Networks (PNNs) have become a key approach for point cloud processing. However, a core operation in these models, Farthest Point Sampling (FPS), often introduces significant inference latency, especially for large-scale processing. Despite existing CUDA- and hardware-level optimizations, FPS remains a major bottleneck due to exhaustive computations across multiple network layers in PNNs, which hinders scalability. Through systematic analysis, we identify three substantial redundancies in FPS, including unnecessary full-cloud computations, redundant late-stage iterations, and predictable inter-layer outputs that make later FPS computations avoidable. To address these, we propose \textbf{\textit{FlashFPS}}, a hardware-agnostic, plug-and-play framework for FPS acceleration, composed of \textit{FPS-Prune} and \textit{FPS-Cache}. \textit{FPS-Prune} introduces candidate pruning and iteration pruning to reduce redundant computations in FPS while preserving sampling quality, and \textit{FPS-Cache} eliminates layer-wise redundancy via cache-and-reuse. Integrated into existing CUDA libraries and state-of-the-art PNN accelerators, \textit{FlashFPS} achieves 5.16$\times$ speedup over the standard CUDA baseline on GPU and 2.69$\times$ on PNN accelerators, with negligible accuracy loss, enabling efficient and scalable PNN inference. Codes are released at this https URL.

---


### 338. [GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion](https://arxiv.org/abs/2604.17721)

**<font color=#1a73e8>作者：</font>** Jiayi Tian, Haiduo Huang, Tian Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the challenge of point cloud registration using color information, where traditional methods relying solely on geometric features often struggle in low-overlap and incomplete scenarios. To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration. Our approach incorporates a dedicated color encoder that enhances color features by extracting multi-level geometric and color data from the original point cloud. We introduce the \textbf{Ge}ometric-3D\textbf{GS} module, which encodes the local neighborhood information of colored superpoints to ensure a globally invariant geometric-color context. Leveraging LORA optimization, we maintain high performance while preserving the expressiveness of 3DGS. Additionally, fast differentiable rendering is utilized to refine the registration process, leading to improved convergence. To further enhance performance, we propose a joint photometric loss that exploits both geometric and color features. This enables strong performance in challenging conditions with extremely low point cloud overlap. We validate our method by colorizing the Kitti dataset as ColorKitti and testing on both Color3DMatch and Color3DLoMatch datasets. Our method achieves state-of-the-art performance with \textit{Registration Recall} at 99.9\%, \textit{Relative Rotation Error} as low as 0.013, and \textit{Relative Translation Error} as low as 0.024, improving precision by at least a factor of 2.

---


### 339. [Voronoi-guided Bilateral 2D Gaussian Splatting for Arbitrary-Scale Hyperspectral Image Super-Resolution](https://arxiv.org/abs/2604.17727)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Jinkun You, Shi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing hyperspectral image super-resolution methods require modifications for different scales, limiting their flexibility in arbitrary-scale reconstruction. 2D Gaussian splatting provides a continuous representation that is compatible with arbitrary-scale super-resolution. Existing methods often rely on rasterization strategies, which may limit flexible spatial modeling. Extending them to hyperspectral image super-resolution remains challenging, as the task requires adaptive spatial reconstruction while preserving spectral fidelity. This paper proposes GaussianHSI, a Gaussian-Splatting-based framework for arbitrary-scale hyperspectral image super-resolution. We develop a Voronoi-Guided Bilateral 2D Gaussian Splatting for spatial reconstruction. After predicting a set of Gaussian functions to represent the input, it associates each target pixel with relevant Gaussian functions through Voronoi-guided selection. The target pixel is then reconstructed by aggregating the selected Gaussian functions with reference-aware bilateral weighting, which considers both geometric relevance and consistency with low-resolution features. We further introduce a Spectral Detail Enhancement module to improve spectral reconstruction. Extensive experiments on benchmark datasets demonstrate the effectiveness of GaussianHSI over state-of-the-art methods for arbitrary-scale hyperspectral image super-resolution.

---


### 340. [Score-Based Matching with Target Guidance for Cryo-EM Denoising](https://arxiv.org/abs/2604.17734)

**<font color=#1a73e8>作者：</font>** Xiaoqi Wu, Xueying Zhan, Wen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cryo-electron microscopy (cryo-EM) enables single-particle analysis of biological macromolecules under strict low-dose imaging conditions, but the resulting micrographs often exhibit extremely low signal-to-noise ratios and weak particle visibility. Image denoising is therefore an important preprocessing step for downstream cryo-EM analysis, including particle picking, 2D classification, and 3D reconstruction. Existing cryo-EM denoising methods are commonly trained with pixel-wise or Noise2Noise-style objectives, which can improve visual quality but do not explicitly account for structural consistency required by downstream analysis. In this work, we propose a score-based denoising framework for cryo-EM that learns the clean-data score to recover particle signals while better preserving structural information. Building on this formulation, we further introduce a target-guided variant that incorporates reference-density guidance to stabilize score learning under weak and ambiguous signal conditions. Rather than simply amplifying particle-like responses, our framework better suppresses structured low-frequency background, which improves particle--background separability for downstream analysis. Experiments on multiple cryo-EM datasets show that our score-based methods consistently improve downstream particle picking and produce more structure-consistent 3D reconstructions. Experiments on multiple cryo-EM datasets show that our methods improve downstream particle picking and produce more structure-consistent reconstructions.

---


### 341. [IncreFA: Breaking the Static Wall of Generative Model Attribution](https://arxiv.org/abs/2604.17736)

**<font color=#1a73e8>作者：</font>** Haotian Qin, Dongliang Chang, Yueying Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI generative models evolve at unprecedented speed, image attribution has become a moving target. New diffusion, adversarial and autoregressive generators appear almost monthly, making existing watermark, classifier and inversion methods obsolete upon release. The core problem lies not in model recognition, but in the inability to adapt attribution itself. We introduce IncreFA, a framework that redefines attribution as a structured incremental learning problem, allowing the system to learn continuously as new generative models emerge. IncreFA departs from conventional incremental learning by exploiting the hierarchical relationships among generative architectures and coupling them with continual adaptation. It integrates two mutually reinforcing mechanisms: (1) Hierarchical Constraints, which encode architectural hierarchies through learnable orthogonal priors to disentangle family-level invariants from model-specific idiosyncrasies; and (2) a Latent Memory Bank, which replays compact latent exemplars and mixes them to generate pseudo-unseen samples, stabilising representation drift and enhancing open-set awareness. On the newly constructed Incremental Attribution Benchmark (IABench) covering 28 generative models released between 2022 and 2025, IncreFA achieves state-of-the-art attribution accuracy and 98.93% unseen detection under a temporally ordered open-set protocol. Code will be available at this https URL.

---


### 342. [HiRAS: A Hierarchical Multi-Agent Framework for Paper-to-Code Generation and Execution](https://arxiv.org/abs/2604.17745)

**<font color=#1a73e8>作者：</font>** Hanhua Hong, Yizhi LI, Jiaoyan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have highlighted their potential to automate computational research, particularly reproducing experimental results. However, existing approaches still use fixed sequential agent pipelines with weak global coordination, which limits their robustness and overall performance. In this work, we propose Hierarchical Research Agent System (HiRAS), a hierarchical multi-agent framework for end-to-end experiment reproduction that employs supervisory manager agents to coordinate specialised agents across fine-grained stages. We also identify limitations in the reference-free evaluation of the Paper2Code benchmark and introduce Paper2Code-Extra (P2C-Ex), a refined protocol that incorporates repository-level information and better aligns with the original reference-based metric. We conduct extensive evaluation, validating the effectiveness and robustness of our proposed methods, and observing improvements, including >10\% relative performance gain beyond the previous state-of-the-art using open-source backbone models and significantly reduced hallucination in evaluation. Our work is available on GitHub: this https URL.

---


### 343. [Source-Free Domain Adaptation with Vision-Language Prior](https://arxiv.org/abs/2604.17748)

**<font color=#1a73e8>作者：</font>** Song Tang, Yunxiang Bai, Wenxin Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-Free Domain Adaptation (SFDA) seeks to adapt a source model, which is pre-trained on a supervised source domain, for a target domain, with only access to unlabeled target training data. Relying on pseudo labeling and/or auxiliary supervision, conventional methods are inevitably error-prone. To mitigate this limitation, in this work we for the first time explore the potentials of off-the-shelf vision-language (ViL) multimodal models (e.g., CLIP) with rich whilst heterogeneous knowledge. We find that directly applying the ViL model to the target domain in a zero-shot fashion is unsatisfactory, as it is not specialized for this particular task but largely generic. To make it task-specific, we propose a novel DIFO++ approach. Specifically, DIFO++ alternates between two steps during adaptation: (i) Customizing the ViL model by maximizing the mutual information with the target model in a prompt learning manner, (ii) Distilling the knowledge of this customized ViL model to the target model, centering on gap region reduction. During progressive knowledge adaptation, we first identify and focus on the gap region, where enclosed features are entangled and class-ambiguous, as it often captures richer task-specific semantics. Reliable pseudo-labels are then generated by fusing predictions from the target and ViL models, supported by a memory mechanism. Finally, gap region reduction is guided by category attention and predictive consistency for semantic alignment, complemented by referenced entropy minimization to suppress uncertainty. Extensive experiments show that DIFO++ significantly outperforms the state-of-the-art alternatives. Our code and data are available at this https URL.

---


### 344. [Ego-InBetween: Generating Object State Transitions in Ego-Centric Videos](https://arxiv.org/abs/2604.17749)

**<font color=#1a73e8>作者：</font>** Mengmeng Ge, Takashi Isobe, Xu Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding physical transformation processes is crucial for both human cognition and artificial intelligence systems, particularly from an egocentric perspective, which serves as a key bridge between humans and machines in action modeling. We define this modeling process as Egocentric Instructed Visual State Transition (EIVST), which involves generating intermediate frames that depict object transformations between initial and target states under a brief action instruction. EIVST poses two challenges for current generative models: (1) understanding the visual scenes of the initial and target states and reasoning about transformation steps from an egocentric view, and (2) generating a consistent intermediate transition that follows the given instruction while preserving object appearance across the two visual states. To address these challenges, we propose the EgoIn framework. It first infers the multi-step transition process between two given states using TransitionVLM, fine-tuned on our curated dataset to better adapt to this task and reduce hallucinated information. It then generates a sequence of frames based on transition conditions produced by the proposed Transition Conditioning module. Additionally, we introduce Object-aware Auxiliary Supervision to preserve consistent object appearance throughout the transition. Extensive experiments on human-object and robot-object interaction datasets demonstrate EgoIn's superior performance in generating semantically meaningful and visually coherent transformation sequences.

---


### 345. [Evolutionary Negative Module Pruning for Better LoRA Merging](https://arxiv.org/abs/2604.17753)

**<font color=#1a73e8>作者：</font>** Anda Cao, Zhuo Gou, Yi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Merging multiple Low-Rank Adaptation (LoRA) experts into a single backbone is a promising approach for efficient multi-task deployment. While existing methods strive to alleviate interference via weight interpolation or subspace alignment, they rest upon the implicit assumption that all LoRA matrices contribute constructively to the merged model. In this paper, we uncover a critical bottleneck in current merging paradigms: the existence of $\textit{negative modules}$ -- specific LoRA layers that inherently degrade global performance upon merging. We propose $\textbf{E}$volutionary $\textbf{N}$egative $\textbf{M}$odule $\textbf{P}$runing ($\textbf{ENMP}$), a plug-and-play LoRA pruning method to locate and exclude these detrimental modules prior to merging. By leveraging an evolutionary search strategy, ENMP effectively navigates the discrete, non-differentiable landscape of module selection to identify optimal pruning configurations. Extensive evaluations demonstrate that ENMP consistently boosts the performance of existing merging algorithms, achieving a new state-of-the-art across both language and vision domains. Code is available at this https URL.

---


### 346. [Reverse Constitutional AI: A Framework for Controllable Toxic Data Generation via Probability-Clamped RLAIF](https://arxiv.org/abs/2604.17769)

**<font color=#1a73e8>作者：</font>** Yuan Fang, Yiming Luo, Aimin Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring the safety of large language models (LLMs) requires robust red teaming, yet the systematic synthesis of high-quality toxic data remains under-explored. We propose Reverse Constitutional AI (R-CAI), a framework for automated and controllable adversarial data generation that moves beyond isolated jailbreak prompts. By inverting a harmless constitution into a constitution of toxicity and iteratively refining model outputs through a critique--revision pipeline, R-CAI enables scalable synthesis of multi-dimensional adversarial data without human annotation. Optimizing solely for toxicity-related rewards, however, can lead to reward hacking and degraded semantic coherence. To address this challenge, we introduce probability clamping within reinforcement learning from AI feedback, which stabilizes adversarial optimization while preserving adversarial intent. Experiments demonstrate that R-CAI generates diverse, high-quality toxic data and that probability clamping substantially improves semantic coherence (15%) without sacrificing adversarial strength. Overall, R-CAI provides a fully automated framework for red teaming data generation and systematic safety evaluation of aligned language models.

---


### 347. [SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks](https://arxiv.org/abs/2604.17771)

**<font color=#1a73e8>作者：</font>** Mohammadtaher Safarzadeh, Hitesh Laxmichand Patel, Afshin Orojlooyjadid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance on natural language to SQL (NL2SQL) benchmarks, yet their reported accuracy may be inflated by contamination from benchmark queries or structurally similar patterns seen during training. We introduce SPENCE (Syntactic Probing and Evaluation of NL2SQL Contamination Effects), a controlled syntactic probing framework for detecting and quantifying such contamination. SPENCE systematically generates syntactic variants of test queries for four widely used NL2SQL datasets-Spider, SParC, CoSQL, and the newer BIRD benchmark. We use SPENCE to evaluate multiple high-capacity LLMs under execution-based scoring. For each model, we measure changes in execution accuracy across increasing levels of syntactic divergence and quantify rank sensitivity using Kendall's tau with bootstrap confidence intervals. By aligning these robustness trends with benchmark release dates, we observe a clear temporal gradient: older benchmarks such as Spider exhibit the strongest negative values and thus the highest likelihood of training leakage, whereas the more recent BIRD dataset shows minimal sensitivity and appears largely uncontaminated. Together, these findings highlight the importance of temporally contextualized, syntactic-probing evaluation for trustworthy NL2SQL benchmarking.

---


### 348. [Structure-Adaptive Sparse Diffusion in Voxel Space for 3D Medical Image Enhancement](https://arxiv.org/abs/2604.17773)

**<font color=#1a73e8>作者：</font>** Hongxu Jiang, Fei Li, Boxiao Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) medical image enhancement, including denoising and super-resolution, is critical for clinical diagnosis in CT, PET, and MRI. Although diffusion models have shown remarkable success in 2D medical imaging, scaling them to high-resolution 3D volumes remains computationally prohibitive due to lengthy diffusion trajectories over high-dimensional volumetric data. We observe that in conditional enhancement, strong anatomical priors in the degraded input render dense noise schedules largely redundant. Leveraging this insight, we propose a sparse voxel-space diffusion framework that trains and samples on a compact set of uniformly subsampled timesteps. The network predicts clean data directly on the data manifold, supervised in velocity space for stable gradient scaling. A lightweight Structure-aware Trajectory Modulation (STM) module recalibrates time embeddings at each network block based on local anatomical content, enabling structure-adaptive denoising over the shared sparse schedule. Operating directly in voxel space, our framework preserves fine anatomical detail without lossy compression while achieving up to $10\times$ training acceleration. Experiments on four datasets spanning CT, PET, and MRI demonstrate state-of-the-art performance on both denoising and super-resolution tasks. Our code is publicly available at: this https URL.

---


### 349. [Forget What Matters, Keep the Rest: Selective Unlearning of Informative Tokens](https://arxiv.org/abs/2604.17785)

**<font color=#1a73e8>作者：</font>** Seunghee Koh, Sunghyun Baek, Youngdong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unlearning in large language models (LLMs) has emerged as a promising safeguard against adversarial behaviors. When the forgetting loss is applied uniformly without considering token-level semantic importance, model utility can be unnecessarily degraded. Recent studies have explored token-wise loss regularizers that prioritize informative tokens, but largely rely on ground-truth confidence or external linguistic parsers, which limits their ability to capture contextual information or the model's overall predictive state. Intuitively, function words like "the" primarily serve syntactic roles and are highly predictable with little ambiguity, but informative words admit multiple plausible alternatives with greater uncertainty. Based on this intuition, we propose Entropy-guided Token Weighting (ETW), a token-level unlearning regularizer that uses entropy of the predictive distribution as a proxy for token informativeness. We demonstrate that informative tokens tend to have higher entropy, whereas structural tokens tend to have lower entropy. This behavior enables ETW to achieve more effective unlearning while better preserving model utility than existing token-level approaches.

---


### 350. [SoK: Analysis of Privacy Risks and Mitigation in Online Propaganda Detection through the PROMPT Framework](https://arxiv.org/abs/2604.17788)

**<font color=#1a73e8>作者：</font>** Dhiman Goswami, Al Nahian Bin Emran, Md Hasan Ullah Sadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Online propaganda detection pipelines expose measurable privacy risks at multiple stages including data collection, feature extraction, and model inference. We conduct a structured analysis of $162$ peer-reviewed studies and formalize the problem using the Propaganda Risk Online Mitigation and Privacy-preserving Tactics (PROMPT) framework. PROMPT models risks $R$ and mitigation strategies $S$ through a mapping $M: R\to S$ guided by a utility function $\alpha\cdot \mathrm{PrivacyGain}(s_j) - \beta\cdot \mathrm{PerfLoss}(s_j) - \gamma\cdot \mathrm{Cost}(s_j)$, with tunable $(\alpha,\beta,\gamma)$ enabling stakeholders to balance privacy, accuracy, and deployment costs. To assess practical adoption, we introduce a compliance score that quantifies the alignment of existing methods with GDPR, CCPA etc. requirements. Our evaluation shows that many widely used pipelines remain non-compliant, particularly in metadata handling and user-level aggregation. We further present empirical fine-tuning experiments on transformer-based encoders and decoders under synthetic perturbation, demonstrating a monotonic privacy-utility trade-off: with $q = 0.05$ performance decreased by 1-2% F$_1$, while at $q = 0.20$ the reduction reached 13-14%. These results establish quantitative baselines for privacy costs in propaganda detection. Our contributions include a formal risk-to-defense mapping, a compliance-oriented auditing metric, and experimental evidence of privacy-performance trade-offs, providing a technical foundation for building regulation-compliant and privacy-aware detection systems.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
