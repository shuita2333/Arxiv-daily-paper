# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 451. [Characterizing and Mitigating Distributional Bias in Physics-Informed Generative Models](https://arxiv.org/abs/2610.16582)

**<font color=#1a73e8>作者：</font>** Tanja Bien, Samir Darouich, Lluís Pastor-Pérez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed generative models augment a data-fitting objective with residual penalties that encourage physical constraints to hold in generated samples. However, improving constraint satisfaction need not improve fidelity to the data distribution. We study this conflict in residual-regularized diffusion models and identify two possible consequences. First, the same prediction error can incur different residual costs near different feasible states, preferring states with lower residual sensitivity (avoidance). Second, this preference can extend to feasible states outside the data support, where the residual also vanishes (leakage). Motivated by this analysis, we propose a data-anchored penalty that weights prediction errors by the residual Jacobian at the clean training sample and normalizes the resulting magnitude. This removes the incentive to relocate to less sensitive states without changing the model architecture or sampling procedure. Experiments on a controlled synthetic system, three PDE systems, and molecular transition-state generation with flow matching demonstrate the benefits of anchoring. Code is available at this https URL.

---


### 452. [OctMole: Multiscale 3D Molecular Generation with Hierarchical Spatial Flows](https://arxiv.org/abs/2610.16586)

**<font color=#1a73e8>作者：</font>** Yu-Tong Jin, Yi-Yang Tian, Qiwei Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating accurate 3D molecules requires jointly determining a variable number of atoms, their identities, and geometry across spatial scales: global shape emerges coarsely, whereas chemical bonds demand fine local precision. Existing atom-based diffusion and flow models operate largely at a single scale, while dense spatial fields become costly at high resolution. We introduce OctMole, a multiscale octree flow framework for 3D molecular generation. A hierarchical occupancy flow progressively resolves sparse molecular support from coarse to fine, and a joint atom flow assigns atom types and continuous in-cell offsets to occupied leaves. This decomposition combines efficient global structure with subcell geometric precision, while cell corruption improves robustness to generated support. On QM9 and GEOM-DRUG, OctMole achieves strong chemical, distributional, and geometric quality, with particularly clear gains over Uni-3DAR on GEOM-DRUG and substantial efficiency gains over dense 3D generation. As an additional capability, intermediate occupancy states and selected regions provide spatial conditioning without task-specific retraining, supporting multiscale shape conditioning, regional editing, linker generation, and shape interpolation. Code and pretrained checkpoints are available at this https URL and this https URL, respectively.

---


### 453. [HyBRA-EEG: Hyperbolic Global-Local Brain-Region Aggregation for Self-Supervised EEG Representation Learning](https://arxiv.org/abs/2610.16589)

**<font color=#1a73e8>作者：</font>** Xin Liu, Feng Lu, Wei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) representation learning is challenged by noisy signals, inter-subject variability, and heterogeneous electrode montages in different datasets and recording settings. Recent self-supervised EEG pretraining methods improve transferability by converting heterogeneous recordings into unified token or sequence representations, but channel-aware designs may still encode montage- or dataset-specific regularities. We propose HyBRA, a self-supervised framework based on hyperbolic global-local brain-region aggregation. HyBRA maps heterogeneous channel observations into a fixed regional token space by combining electrode coordinates, region priors, and feature-dependent hyperbolic distances. A channel-evidence injection branch preserves fine-grained discriminative cues during aggregation. The resulting tokens are processed by a Region-Time Transformer and pretrained with masked reconstruction of latent features and region-level signals. HyBRA outperforms the compared methods in average balanced accuracy on six benchmark datasets. Under a controlled six-fold evaluation on OpenBMI-MI, HyBRA matches CSBrain in balanced accuracy, improves AUROC by 1.84 percentage points and AUPRC by 5.23 percentage points, and uses 96.8\% fewer parameters. Matched comparisons on TUAB and TUEV show higher balanced accuracy for hyperbolic matching than for Euclidean distance or cosine similarity.

---


### 454. [JtT: Rethinking Point Trajectory Diffusion for Diverse and Rigid Motion from an Image](https://arxiv.org/abs/2610.16591)

**<font color=#1a73e8>作者：</font>** Gabrijel Boduljak, Yushi Lan, Christian Rupprecht 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study forecasting rigid-body motion from a single image: generating diverse and physically plausible future trajectories for arbitrary points in a scene, without building rigidity into the architecture or relying on geometric inputs such as depth. Like video generators, recent trajectory generators fail at this task, even in simple synthetic Kubric scenes, despite scaling up model size and training on real data.
We show how to solve this with the right architecture and parameterization. Our model, JtT, is a simple diffusion transformer that operates directly in coordinate space and decodes arbitrary and dense query patterns, without the trajectory VAEs or fixed grids assumed in prior work. Through a systematic study of the design space of point trajectory diffusion, we find that diffusing per-frame velocities is the only parameterization that captures rigidity, that it must be paired with the right timestep schedule, and that adding full-resolution RGB at the query points resolves the boundary failures of prior methods.
However, evaluating such 2D models rigorously is itself non-trivial. To our knowledge, we are the first to observe that physical plausibility and diversity do not improve together during training: larger models, as used in prior work, memorize the single ground-truth future per training image, becoming more rigid while covering fewer possible futures.
Yet prior work has paid little attention to this, so we show how model rankings depend on model size, metric, and stopping time, and adopt a stricter, checkpoint-averaged evaluation protocol. Under this protocol, JtT improves over prior methods on both distributional and rigidity metrics and approaches ground-truth rigidity, with only about 50M parameters.

---


### 455. [Towards Modality-Agnostic Seizure Classification: A Unified Deep Learning Framework for Heterogeneous EEG and Intracranial EEG Signals](https://arxiv.org/abs/2610.16596)

**<font color=#1a73e8>作者：</font>** Ramya Sundaram, Muhammad Aslam Jarwar, M Uma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Seizure prediction and detection, essential for clinical treatment of epilepsy, remain the crucial task of this neurological disease. EEG and iEEG are widely used to analyze epilepsy due to its capability of capturing discriminative brain activities at high time resolution. However, existing works generally analyze either EEG or iEEG seizure activity separately, where EEG analysis has been well-researched, while more and more works consider iEEG for its higher specificity at the spatial level and signal quality. Currently, most of the existing seizure prediction systems are single-modal in nature, which limits its application to a variety of clinical conditions. Therefore, a common framework to analyze seizures with both EEG and iEEG signals needs to be developed. This paper presents a new framework of multimodal seizure classification integrating the heterogeneous EEG and iEEG recordings from different subjects and sources. A specific framework, called Unified Multimodal Signal Harmonization (UMSH), is developed for harmonizing signals with varied sampling rates and recording conditions. Moreover, to handle the extremely class-imbalanced problem in the data sets, we use a Conditional Generative Adversarial Network (cGAN) based data augmentation technique to generate synthetic samples to balance the class distribution. The proposed framework uses the EEGNet-Vision Transformer (EEGNet-ViT) as the feature extraction and classification network to learn the local discriminative patterns as well as global contextual information in the multimodal seizure data. Experimental results demonstrate the effectiveness of the proposed framework for robust seizure classification, emphasizing the potential of integrated EEG-iEEG multimodal learning in advancing next-generation epilepsy monitoring and clinical decision-support systems.

---


### 456. [DEFlow: Deep Equilibrium Flow Maximum-Entropy Reinforcement Learning](https://arxiv.org/abs/2610.16597)

**<font color=#1a73e8>作者：</font>** Ruslan Ageev, Huaze Tang, Runqing Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expressive flow policies can represent multiple high-value actions, but sampling them with few integration steps while retaining tractable action densities remains challenging. We introduce DEFlow, a deep equilibrium flow policy that replaces explicit Euler sampling with implicit Euler integration and solves all intermediate actions jointly as an equilibrium system. We combine implicit differentiation with a discrete change-of-variables formula for the final-action density, enabling off-policy training within soft actor-critic without backpropagating through solver iterations. DEFlow achieves an average relative improvement of approximately 10% in mean successful coverage over the strongest baseline across four Multi-Goal docking variants. It also achieves the highest mean time-averaged return on four of five manipulation tasks, while remaining broadly competitive across five MuJoCo tasks. These results support implicit flow policies for tasks requiring both diversity and precision, at the cost of additional nonlinear and linear solves. Primary

---


### 457. [MixLID: Token-Level Language Identification in Mixed-Language Text](https://arxiv.org/abs/2610.16601)

**<font color=#1a73e8>作者：</font>** Seongtae Hong, Youngjoon Jang, Seungyoon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Processing multilingual text requires both identifying a broad range of languages and distinguishing the language of each token in inputs containing multiple languages. We introduce MixLID, a token-level language identification model supporting 111 language-script combinations. MixLID follows a two-stage training process: it first learns to distinguish individual languages using the language labels of monolingual examples, then continues training on mixed-language data. The second stage uses concatenated examples from existing code-switching data alongside augmented examples created through word substitution based on correspondences between English source words and loanwords. For monolingual identification, MixLID outperforms all baselines in both accuracy and macro F1 on four benchmarks within the language coverage shared with each baseline. For mixed-language identification, it outperforms the baselines in identifying the language of individual tokens on every evaluated language pair. MixLID achieves high performance across a broad range of languages in both monolingual and mixed-language settings. The model is publicly available at this https URL.

---


### 458. [DR-APO: Decoupled-Representation Advantage-Guided Policy Optimization from Continuous Control to Embodied Navigation](https://arxiv.org/abs/2610.16618)

**<font color=#1a73e8>作者：</font>** Runhua Zhang, Yingjie Niu, Chao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy representations in reinforcement learning have expanded beyond Gaussian policies to diffusion and flow-matching based generative policies. However, existing RL methods remain representation-specific, lacking a unified optimization interface for emerging generative policies. In particular, extending likelihood-based objectives to multi-step generative policies couples optimization to their internal generation process, where accumulated likelihood ratios can weaken the update signal. Meanwhile, generative-policy-specific methods often rely on multi-candidate generation and critic-based selection, improving overall return while providing limited improvement to the policy itself. We introduce DR-APO (Decoupled-Representation Advantage-Guided Policy Optimization), which decouples policy improvement from policy representation through advantage-guided target improvement and representation-compatible direct action fitting, providing a shared optimization principle for Gaussian, diffusion, and flow policies. Across five MuJoCo-v5 tasks, DR-APO remains competitive with SAC for Gaussian policies and achieves the best aggregate policy-only performance for both diffusion and flow-matching policies. NavDP post-training improves the Success Rate (SR) from 70.33% to 89.55% in simulation and from 25% to 65% in real-world navigation. These results demonstrate a unified policy-improvement principle across Gaussian, diffusion, and flow policies, from continuous-control learning to embodied-policy post-training.

---


### 459. [Weak Segmentation-Guided GAN for~Realistic Color Edition](https://arxiv.org/abs/2610.16620)

**<font color=#1a73e8>作者：</font>** Vincent Auriau, Emmanuel Malherbe, Matthieu Perrot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Editing the color of images in a realistic way finds many applications such as changing the perception of an image, data augmentation or film post processing. The design of an automatic tool is a complex and long addressed challenge. In particular, two properties are difficult to meet altogether: generating realistic results without artifacts and the possibility to precisely choose the future color. Conventional methods using segmentation and histogram matching maximize the controllability but also introduce a lack of realism or are complex to automate. On the contrary, GANs that specialize in realism are difficult to control. To overcome these challenges, we propose a novel GAN architecture leveraging any differentiable segmentation model. We demonstrate the genericness of our framework that presents state of the art results on different use cases. It generates images that look realistic while offering a precise color control.

---


### 460. [AgentCue: Statistical Summaries for Guiding Decentralized Multi-Agent Self-Organization](https://arxiv.org/abs/2610.16621)

**<font color=#1a73e8>作者：</font>** Guojun Zhu, Xinyou Chen, Kejian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) combine multiple agents to solve complex tasks, and recent MAS scale to more than a thousand agents. At this scale, decentralized MAS remove the central orchestrator that assigns sub-tasks, and the agents, which we call workers, self-organize through their own choices of sub-tasks and collaborators on a shared board. As workers keep adding participation and collaboration records, however, the information explodes: workers spend more and more effort on reading the records of other workers, and self-organization loses efficiency. In the statistical view, we represent the execution history of an MAS by two continually updated networks, a collaboration network among workers and a participation network between workers and task types. We then propose AgentCue, a method built on a new latent space model that places workers and task types in a shared latent space. Each time the networks are updated, the estimated parameters of the latent space model form a compact and interpretable statistical summary, and workers use the statistical summary to choose sub-tasks and collaborators without repeated searches of the shared board. We establish the identifiability of the latent space model and non-asymptotic error bounds for the estimates under network increments, and we show that a fixed number of gradient updates after each network update suffices for the same error rate. Experiments on LongBench v2 Multi-Doc QA show that AgentCue achieves competitive effectiveness, efficiency, and interpretability.

---


### 461. [Adaptive Interaction Network for Human Motion Prediction During Human-Robot Collaboration](https://arxiv.org/abs/2610.16624)

**<font color=#1a73e8>作者：</font>** Mengyuan Liu, Yangting Lin, Qiongjie Cui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion prediction during human-robot collaboration is critical for achieving safe and efficient interactions in shared environments. Unlike previous studies that have primarily focused on humans and objects, we focus on the robot-aware human motion prediction task, which explicitly models the influence of robots on human motion. This task presents new challenges, such as capturing human-robot heterogeneity and modeling complex spatial interactions. To address these issues, we develop an adaptive interaction network (AINet) model that consists of two branches: a primary branch that predicts future human motion and an auxiliary branch that estimates robot trajectories. The two branches are jointly optimized and coupled via a Local-Global Spatial Interaction (LGSI) Module, which effectively captures fine-grained and global contextual dependencies between human and robot motion sequences. Then, we introduce an Adaptive Weighted Aggregation (AWA) Module to dynamically fuse motion features using context-dependent weights, thereby increasing adaptability across diverse scenarios. Furthermore, we adopt a coarse-to-fine prediction strategy, in which a coarse pseudo-trajectory is first predicted, followed by the refinement of detailed human poses based on that trajectory. Extensive experiments on three challenging datasets reveal that our proposed method achieves superior performance, validating its effectiveness in human-robot collaboration scenarios. Our code is available at: this https URL.

---


### 462. [Integrating Feature Understandability into Feature Selection for Human-Centred Tabular Explanations](https://arxiv.org/abs/2610.16627)

**<font color=#1a73e8>作者：</font>** Nicola Rossberg, Bennett Kleinberg, Barry O'Sullivan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing human-centred XAI research predominantly evaluates explanations after they have been generated. However, this fails to provide actionable insights into improving accessibility. This study incorporates human-based feature understandability into feature selection to improve the generation of human-centred explanations. Natural language explanations for machine learning models trained on tabular data often cite influential features in the input data to explain a given decision. As a consequence, users' ability to understand the produced explanation hinges on their understanding of the cited features. To quantify this natural-language feature understandability, Rossberg et al. proposed the Feature Understandability Scale, which assigns numerical `understandability scores' to features based on user feedback. To evaluate the degree to which these scores can improve machine learning explanation quality, this study collects understandability scores across two datasets, proposes an understandability-aware feature selection algorithm to select features that are both understandable and informative, and trains a random forest based on these feature subsets. The SHAP-based explanations generated by this model are evaluated using user feedback, and changes in explanation quality are assessed. The individual evaluation of the explanations showed that while the understandability-based explanations scored higher on average, the difference was not statistically significant. In contrast, the comparative evaluation found that participants preferred these explanations significantly more frequently than expected at the chance level. It is concluded that the integration of understandability can yield more understandable explanations at minimal cost to classification performance, although changes to quality require elucidation in larger cohorts.

---


### 463. [AeroChem: Closed-loop Physics-Informed State Space Modeling for Long-term Chemically-Reactive Air Quality Forecasting--Extended Version](https://arxiv.org/abs/2610.16630)

**<font color=#1a73e8>作者：</font>** Kien Le Trung, Tung Kieu, Dinh Duc Nha Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate long-term air quality forecasting is challenging due to long-range transport, meteorological variability, and nonlinear chemical reactions underlying secondary pollutant formation. Purely data-driven models often suffer from long-horizon drift and lack physical consistency, while existing physics-informed approaches commonly follow open-loop designs that fuse neural and physical components only at the output level. We propose AeroChem, a closed-loop physics-informed state space framework for chemically reactive air quality forecasting. AeroChem adopts a two-branch co-correction design: a UDE-based process branch provides a structured but imperfect physical prior, while a Mamba-based virtual measurement branch captures long-range temporal context and produces probabilistic virtual observations. Neural Kalman Fusion couples the two branches by correcting the latent physical state at each forecasting step and feeding the posterior state back into the simulator, reducing long-horizon drift. We further introduce HanoiAir, a real-world dataset integrating pollutant concentrations, meteorology, and emission inventories. Experiments on HanoiAir and a public benchmark show that AeroChem improves long-horizon stability and sudden-change forecasting.

---


### 464. [ACED: Reference-Anchored Aggregation of Natural-Language and Executable Evidence for Mathematical Reasoning](https://arxiv.org/abs/2610.16635)

**<font color=#1a73e8>作者：</font>** Yiyi Lu, Jiaxiang Geng, Bing Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural-language self-consistency and executable programs provide complementary test-time evidence for mathematical reasoning, yet either channel may support the same semantic error. Thus we propose ACED, a reference-anchored framework that treats the self-consistency answer as the default and executable outputs as supporting evidence rather than interchangeable votes. ACED converts source-specific answer counts into smoothed supports, combines them through a weighted logarithmic pool, and overrides the reference only when a calibrated relative-evidence margin is exceeded. The same rule supports both candidate selection and admission of executable-only answers. Across five math word-problem benchmarks, ACED matches or outperforms the corresponding baselines. On GSM8K, ACED-CANDIDATE recovers 89.7% of the attainable candidate-set gain with only three damaging overrides, while ACED-ALL reaches 86.9% accuracy versus 82.6% for direct Program-of-Thought aggregation. These results show that preserving evidence provenance enables more reliable integration of natural-language and executable reasoning.

---


### 465. [Learning Deployable Causal Action Geometry under Temporal Non-Stationarity](https://arxiv.org/abs/2610.16644)

**<font color=#1a73e8>作者：</font>** Changjian Liu, Tianyu Wang, Yuwei Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning a response law for continuous decisions from observational time series is central to many real-world decision systems, yet temporal non-stationarity poses a fundamental challenge: as outcomes drift over time, naively pooled models can conflate action effects with shifting baselines and even reverse action rankings. Even when the one-step response is identifiable, unrestricted cross-time generalization remains fundamentally ill-posed. We therefore seek the part of the response that remains stable for decisions even when outcome levels do not. We propose deployable causal action geometry: the action-response shape that remains after anchoring away action-independent level shifts on a selected link scale and profiling out positive amplitude variation. Building on this target, we develop a two-stage orthogonal estimator that first obtains cross-fitted pilot estimates of anchored responses and then performs honest profiled selection over link, representation, and shape classes. The resulting estimator admits oracle guarantees for the restricted target and, under approximate persistence, produces decision rules that remain near optimal in future periods. Experiments on synthetic data and Dominick's support the proposed target and its transfer behavior. In a randomized Taobao A/B test, the deployed system improves GMV and purchase counts by \(1.16\%\) and \(1.70\%\).

---


### 466. [Learning Incompressible 3D Flows from Sparse Samples: A Set Transformer Approach to Divergence-Free Kernel Fitting](https://arxiv.org/abs/2610.16645)

**<font color=#1a73e8>作者：</font>** Ramzi Idoughi, Radouan Boukharfane, Peter Wonka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering divergence-free velocity fields from sparse and corrupted observations requires reconciling physical consistency, expressive representations, and robustness to missing data. We introduce DFK-Former, a set-to-field transformer that reconstructs divergence-free velocity fields from sparse, noisy, and irregularly sampled 3D observations. The model is inherently invariant to the number and ordering of input samples and predicts the parameters of a divergence-free kernel representation, producing continuous, mesh-free velocity fields that satisfy incompressibility exactly by construction rather than approximately through soft constraints or projection operators. Unlike existing divergence-free kernel approaches, which estimate kernel coefficients via a separate optimization for each field, DFK-Former predicts these coefficients directly in a single forward pass. This eliminates costly iterative fitting while providing a learned prior that enables accurate reconstruction even when observations are insufficient to uniquely determine the field. To enhance representational power, we introduce adaptive and anisotropic divergence-free kernels that preserve exact incompressibility guarantees while capturing more complex flow structures. Extensive experiments across varying levels of sparsity, noise, and occlusion, including transfer to real Direct Numerical Simulation (DNS) turbulence data, demonstrate substantial gains in both accuracy and efficiency. DFK-Former reduces endpoint error by up to 4.6x compared to per-field divergence-free-kernel optimization, while reconstructing each field in 7.5 ms instead of 9.8 s, yielding a speedup of more than three orders of magnitude. These results establish direct, feed-forward prediction of divergence-free kernel parameters as a practical and effective paradigm for physically consistent velocity-field reconstruction from sparse observations.

---


### 467. [Counting with Attention and LayerNorm: Norm Scaling and Representation Geometry](https://arxiv.org/abs/2610.16653)

**<font color=#1a73e8>作者：</font>** Ayyub Shaffy, Manoj Dhakal, Safal Shrestha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counting is a simple task on which transformers can nevertheless fail at long sequence lengths. We study the cost of counting in a single attention layer, up to a maximum length $L$, focusing on how softmax attention and layer normalization shape the representation from which the count is recovered. We mainly focus on regression read-out but also consider classification read-out. For regression, we show unnormalized linear attention counts exactly at parameter norms independent of $L$. For softmax attention, regression cannot count exactly with finite parameters; it recovers the count after rounding, but only when the vector parameter norms grow with $L$. We measure this cost by $B_{\min}$, the smallest bound that can be placed on every trainable vector to ensure exact counting after rounding, and derive tight rates. At fixed model dimension, $B_{\min}$ grows as $L$ without normalization, as $L^{3/2}$ under bare post-normalization, and as $L^{3/4}$ with learned post-normalization. The last rate is unexpected: post-normalization discards the magnitude that carries the count and might be expected to make counting harder, yet with a learnable gain it counts at a smaller norm than softmax without normalization. Bare pre-normalization is different: it bounds the attention scores, so beyond a finite length no parameter norm suffices. A classification read-out keeps every norm bounded under every placement, but a dense head stores one output vector per count and costs more in storage. Experiments on the post-normalized model reproduce this split between the two read-outs. Together, our theoretical and empirical findings characterize how self-attention, layer-normalization placement, and read-out choice shape the representation geometry and parameter cost of counting in the minimal single-head architecture studied here.

---


### 468. [Guidance Without Labels: Flow Matching from Coupled Gaussian Mixtures](https://arxiv.org/abs/2610.16654)

**<font color=#1a73e8>作者：</font>** Stanislas Ducotterd, Bassam El Rawas, Michael Unser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching models are typically trained to transport a Gaussian source to the data distribution, with source and target samples paired independently. We replace the source with a fitted Gaussian mixture and couple each data point to a mixture component through an entropic optimal transport problem. We show that the resulting transport reduces to the standard Gaussian-source problem up to a guidance-like correction, which enables the reuse of a pretrained velocity field. This correction is a closed-form function of the fitted mixture plus a term that we learn with a small correction network. We test our model on published checkpoints for CIFAR-10 and CelebA-HQ. It improves FID at every step count, and on CelebA-HQ it reaches the quality of the baseline with about half the steps. The closed-form term alone, with no training, already delivers most of this improvement; the small correction network accounts for the rest.

---


### 469. [Does a Hosted Decision Model Respect Irrelevant Alternatives? A Pre-Registered Test of Option-Set Dependence in Jev](https://arxiv.org/abs/2610.16655)

**<font color=#1a73e8>作者：</font>** Dushyant Rajput, Nirdesh Chauhan, Siddharth Kosaraju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision APIs that return a probability for each option are routinely used as if those probabilities were properties of the options themselves. That reading is valid only if the model satisfies independence of irrelevant alternatives (IIA): adding an option that is neither the right answer nor its strongest rival should leave the odds between those two unchanged. We test this in a pre-registered study of jev-1.13.0, a hosted decision model, using 299,463 calls on intent classification (BANKING77, CLINC150) and topic classification (AG News). Every added option moves the log-odds between the gold label and the strongest wrong label: the root-mean-square systematic shift is 0.20-0.52 nats, 1.2 to 3 times the run-to-run variation, even when the added option takes at most 0.1% of the probability mass. The shifts are directional. An option similar to the wrong answer draws probability from it (+0.10 nats toward the gold label). A paraphrase of the wrong answer produces an intermediate pattern: the gold label's probability is almost conserved, but the paraphrase receives only about a third of the wrong answer's share rather than the half that strict substitution implies. The distortion grows steadily with the logarithm of the number of options, reaching about 1 nat at 255 options, and off-domain padding pushes the odds against the gold label. In contrast, questions packed into one call do not interact (bias < 0.001). Scoring each option with an independent yes/no question removes the option-set dependence but picks the right answer 8.7 points less often. Jev sits between two local baselines, an option-independent scorer and a prompt readout. Its probabilities are best read as relative to the option list they were computed over.

---


### 470. [Compression Through Time: An Interplay of Separability, Stationarity and Capacity](https://arxiv.org/abs/2610.16660)

**<font color=#1a73e8>作者：</font>** Nikolaus Kopp, Franz Pernkopf, Bernhard Geiger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information-theoretic and geometric compression have been widely studied as possible explanations for generalization. Yet their temporal dynamics in recurrent networks remain largely unexplored. Using discretized LSTMs, whose finite embedding space enables direct estimates of information quantities, we observe pronounced compression across the final timesteps of many datasets. We explain this effect through three competing mechanisms: (i) class separability permits stronger compression at the final timestep; (ii) shared recurrent dynamics propagate this pressure across timesteps with similar activation states, making its extent depend on temporal stationarity; and (iii) limited representational capacity opposes prolonged compression because it restricts information available for subsequent computation. We systematically test these mechanisms through controlled synthetic interventions and real-world sequence tasks. Our results identify class separability, temporal stationarity, and network capacity as key determinants of temporal compression, and suggest that compression acts as a regularizer-potentially beneficial when excess capacity is available, but harmful to generalization when it consumes memory needed for the task.

---


### 471. [Making LoRA Identifiable: Orthogonal Alignment for Continual Learning](https://arxiv.org/abs/2610.16664)

**<font color=#1a73e8>作者：</font>** Pratik Rakesh Singh, Mohammadi Zaki, Akash Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is growing interest in applying Parameter-Efficient Fine-Tuning (PEFT) to Continual Learning, as it enables faster training, mitigates catastrophic forgetting, and facilitates better adaptation to new tasks. Prior approaches have explored a range of strategies, including extending new LoRA branches for each incoming task, training under orthogonal loss objectives across all task-specific LoRA modules, and employing gating mechanisms to integrate new and existing LoRA modules. However, these methods incur memory costs that grow linearly with the number of tasks, limiting their scalability. More recent approaches investigate training a single LoRA by leveraging asymmetries in its parameterization; however, they often suffer from insufficient representational alignment across the LoRA parameter space. To address these limitations, we propose Stiefel Optimization and Aligned Rotation (SOAR), a two-stage framework for continual LoRA learning. First, we constrain the A matrix to lie on the Stiefel manifold, thereby reducing coordinate misalignment to the space of orthogonal rotation matrices. Second, we introduce an Orthogonal Procrustes alignment procedure for the B matrix to estimate the optimal rotation, coupled with a per-rank retention merging strategy that quantifies directional agreement between representations of new and previously learned tasks. We conduct extensive experiments across multiple models and benchmarks, demonstrating that SOAR achieves strong continual learning performance without incurring additional memory overhead.

---


### 472. [3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification](https://arxiv.org/abs/2610.16692)

**<font color=#1a73e8>作者：</font>** William Grolleau, Astrid Sabourin, Guillaume Lapouge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the Cross-View Object Re-Identification (ReID) task, aiming to match identities across drastically different viewpoints. We focus on Single-View Aerial-Ground ReID (SV AG-ReID), where models train on one viewpoint and must generalize to another at inference. To bridge this viewpoint gap, related work employs generative models to synthesize novel views from source images as additional training data. We leverage recent advances in large-scale single-view 3D mesh reconstruction to lift source images into textured meshes and to render them from new viewpoints. However, this pipeline produces unreliable data in two distinct ways. First, the reconstruction may fail and produce geometrically incorrect meshes, resulting in severe corruption in rendered novel views. Second, even when the geometry is correct, the rendered novel views contain hallucinated textures in regions not visible in the source image. The reconstructed mesh carries a per-pixel partition between regions visible from the source view and regions that the reconstruction model had to hallucinate, available as a deterministic byproduct of rendering. We introduce this per-pixel visibility map and exploit it in a two-stage design. Cross-View Consistency Filtering (CVCF) discards geometrically incorrect meshes by ensuring multi-view consistency between source and novel views over visible patches. Visibility-Aware Attention Supervision (VAAS) leverages the visibility map to guide the model's attention toward reliable regions of the rendered view during training. Combined, these two components enable our method, 3D-VITAL, to better leverage the synthetic signal from single-view 3D mesh reconstruction. 3D-VITAL sets a new state-of-the-art on three SV AG-ReID benchmarks. Code and data will be released at this https URL.

---


### 473. [Feature-Context Consistency: Unsupervised Adversarial Detection with Drift Stability on Attributed Graphs](https://arxiv.org/abs/2610.16694)

**<font color=#1a73e8>作者：</font>** Firas Bayram, Maxime Cordy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial detection on evolving attributed graphs faces two challenges: fraud labels arrive late or not at all, and natural distributional drift erodes any trained decision boundary. Modern detectors can reach strong detection rates when labels are available and the distribution is stationary; sustaining that quality without labels and under drift is the open problem. We identify feature-context consistency -- the alignment between a node's attributes and its aggregated neighborhood attributes -- as a single structural signal that addresses both. We formalize it as the Context Boost (CB) score within a Restricted Boltzmann Machine framework (CB-RBM) and prove two complementary worst-case guarantees: a strict separation between the expected CB of legitimate and adversarial nodes, with gap growing linearly in model capacity, whenever the adversary's context stays far enough from legitimate neighborhood context; and a Wasserstein-Lipschitz bound on how far the CB distribution moves under natural drift. We validate on XBlock Ethereum phishing (~153K nodes) and Reddit banned-user detection (~11K nodes), with two further datasets in the appendix spanning diverse domains. With zero labels, CB-RBM achieves AUROC >= 0.96 on four adversarial attacks and keeps FPR close to its calibrated 5% target under drift -- outperforming supervised GNNs (hundreds of labels), unsupervised graph-anomaly baselines, and a standard RBM whose FPR collapses to 89-100%. What typically requires separate mechanisms -- label-free operation and drift stability -- here follows from a single structural regularity of the data. Code: this https URL.

---


### 474. [Learn from Move: the Next Step for GUI Agents](https://arxiv.org/abs/2610.16720)

**<font color=#1a73e8>作者：</font>** Jiahao Lu, Yize Shen, Chuanyuan Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for GUI agents primarily focus on increasing task difficulty by extending task horizons. Besides, enabling agents to explore unfamiliar environments and successfully complete tasks within them is also a critical yet challenging problem. We introduce LatentGUIWorld, a benchmark of six tasks in three matched pairs organized by the evidence needed for control: $I_0$ uses prior knowledge and available observations, $I_1$ requires interaction that directly reveals hidden semantics, and $I_2$ identifies dynamics from action-response relationships. Frontier models struggle especially on $I_2$ tasks. We introduce MOVE, which separates movement from button events and exposes intermediate visual feedback, together with demonstrations of iterative exploration and control. Ablations show that both action granularity and multi-step demonstrations improve performance. After SFT, LatentLearner-9B achieves 50.0% overall success on LatentGUIWorld, comparable to several frontier models. Joint RL further raises egocentric Drag and Ten-Choice success to 92.0% and 75.3%. Behavioral analysis reveals multi-step exploration. In egocentric Drag, RL increases Pearson correlation between error-normalized commands and ideal gain compensation from 0.610 to 0.803. Together, these behaviors show that models learn to explore through interaction and adapt their control to environment dynamics. The same format improves GUI grounding after RL, reaching 67.37% mean accuracy across five benchmarks versus 66.72% for conventional RL.

---


### 475. [Lost in Contrast: Instruction-Preserving Decoding for Reliable Visual Question Answering](https://arxiv.org/abs/2610.16722)

**<font color=#1a73e8>作者：</font>** Haonan Zhang, Ting Jin, Wenzhong Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual contrastive decoding corrects answers using the prediction difference between the original image and a reference condition, yet the same contrast also turns supported abstentions into incorrect answers. We find that abstentions are lost at two stages: contrastive decoding with candidate filtering can exclude the abstention token before any comparison takes place, and the reference branch's response to the abstention instruction is removed when the reference prediction is subtracted. We therefore propose instruction-preserving decoding, which keeps the effect of the abstention instruction on the original-image prediction intact while leaving the contrast strength freely adjustable. Using a perturbed image and an image-free prediction as references, we obtain IP-VCD and IP-M3ID. On decision utility (DU), which credits both correct answers and supported abstentions, both methods outperform all compared non-IP baselines on every one of nine models on VizWiz, and IP-VCD also leads on eight of nine models on Food-101. Candidate measurements and paired per-question comparisons show that computing the instruction effect and the visual contrast term separately lets contrastive decoding support both correct answers and supported abstentions.

---


### 476. [Queue-Aware Token Communications: Bridging AI Representation and Wireless Service](https://arxiv.org/abs/2610.16730)

**<font color=#1a73e8>作者：</font>** Yuquan Xiao, Qinghe Du, Chaoyang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of foundation models and edge intelligence is transforming wireless networks from data-oriented communication systems into artificial intelligence (AI)-native service platforms. Token communications (TokenCom) has emerged as a promising paradigm that directly transmits task-oriented AI representations. However, existing studies typically assume that generated tokens can be transmitted immediately, overlooking the queueing dynamics arising from the mismatch between token workload generation and time-varying wireless service capability. To address this limitation, we introduce Queue-Aware TokenCom, which explicitly incorporates token queues into the AI service pipeline. We present an end-to-end architecture integrating AI representation generation, token workload management, wireless transmission, and downstream task inference. We then discuss two key design directions: budget-aware token representation optimization and queue-aware token service optimization, with the token budget serving as a critical interface between AI performance and communication efficiency. Moreover, we investigate fixed and adaptive token budget strategies to characterize the fundamental tradeoff between AI performance and communication efficiency in dynamic wireless environments. Finally, we outline research directions toward closed-loop, task-aware, and scalable TokenCom systems.

---


### 477. [PathPilot: An Adaptive Question-Conditioned Multi-Magnification Navigation Agent for Whole-Slide Image Analysis](https://arxiv.org/abs/2610.16734)

**<font color=#1a73e8>作者：</font>** Zhengyang Xu, Han Li, Jingsong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The diagnostic capability of WSI agents relies on effective slide navigation to identify diagnostically relevant regions and efficiently integrate evidence across the slide. While in clinical practice, pathologists dynamically examine slides across multiple scales, integrating global and cellular evidence in a sequential manner, existing AI navigation approaches mostly operate at a single fixed magnification or rely on predefined magnification traversal. This mismatch prevents existing methods from modeling cross-magnification interactions and adaptive magnification selection inherent to real diagnostic workflows. We propose PathPilot, a clinically consistent multi-magnification WSI navigation agent that explicitly models cross-magnification localization and evidence-adaptive exploration. Specifically, we introduce a CrossMagLoc that learns magnification-specific diagnostic localization from pathologist viewing behavior and integrates information from adjacent magnifications to identify the diagnostically most relevant region within the current ROI, thereby providing a diagnostically informed starting point for subsequent question-conditioned exploration. We further introduce an EviRegionSearch that starts question-conditioned exploration from this region, progressively accumulating question-relevant evidence and adaptively determining the next navigation action according to the remaining evidence requirement. Their iterative interaction enables PathPilot to sequentially explore across ROIs and magnifications until sufficient evidence is acquired. Extensive QA evaluations across five cohorts demonstrate consistent superiority over competing SOTA methods on inter/external cohorts, respectively, validating question-conditioned evidence acquisition across regions and magnifications that mirrors the sequential, knowledge-driven navigation of pathologists.

---


### 478. [The Midas Touch for Metric Depth: Interpretable Metricization for Generalizable Depth Perception](https://arxiv.org/abs/2610.16749)

**<font color=#1a73e8>作者：</font>** Mengtan Zhang, Yu Ma, Shiqi Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent foundation models have drastically improved the generalization of monocular relative depth estimation, yet recovering accurate metric depth from their estimates for depth perception tasks remains challenging due to scale ambiguity and local metric-scale inconsistency. Existing approaches recover metric depth from sparse observations using either explicit global affine transformation algorithms or implicit data-driven depth completion networks. The former cannot accommodate spatially varying relative-to-metric relationships, while the latter are sensitive to the distribution of sparse observations and may not fully exploit generalizable relative depth priors. To simultaneously address these issues, this study extends our previous work MTD and proposes MTDv2, a hybrid metric depth perception framework that combines explicit depth metricization with data-driven metric depth refinement. The explicit depth metricization process performs segment-wise affine transformations to recover spatially varying metric scales while preserving the geometric structure of relative depth, followed by pixel-wise depth refinement that propagates metric observations along paths with minimal accumulated geometric variation. The data-driven depth refinement process subsequently extends the explicit single-path depth propagation to a learnable multi-path formulation while preserving its interpretability. Extensive experiments conducted on 16 public datasets demonstrate the robust and generalizable depth scale recovery capability of MTDv2 across diverse sources of sparse observations and different depth estimation paradigms, as well as its broad applicability to downstream 3D perception tasks. Code will be publicly available at this https URL upon publication.

---


### 479. [NFMap: Topographic 2D Manifold Learning with Invertible Normalizing Flows](https://arxiv.org/abs/2610.16750)

**<font color=#1a73e8>作者：</font>** Héléna Alexandra Gaspar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present NFMap, a dimensionality reduction method for 2D visualisation that extends Generative Topographic Mapping (GTM) with a bijective normalizing flow. Like GTM, NFMap places a fixed mixture grid prior over a 2D latent map, giving a parametric embedding, an explicit likelihood, and the ability to project new points onto an existing map; the likelihood is an effective out-of-distribution signal on chemical datasets. Unlike GTM, whose latent-to-data mapping is an RBF network of bounded flexibility, NFMap's mapping is a normalizing flow, and is therefore fully invertible: any location on the map can be carried back to data space. To alleviate map crowding on large datasets, NFMap additionally supports heavy-tailed Student-t mixture components. NFMap maps data to a latent space of the same dimension, split into a 2-dimensional navigable map and an off-manifold residual. Because the flow is bijective and its objective penalises volume contraction, variance squeezed out of the residual must reappear in the navigable map. The residual scale is the main control between local neighbourhood fidelity and global distance fidelity; its effect depends on the dimensionality of the data and is coupled to the extent of the latent grid.

---


### 480. [Is the Platform Part of the Measurement? A Protocol and Simulation Study for Cross-Platform Equivalence of Machine-Labelled Policy Sentiment](https://arxiv.org/abs/2610.16757)

**<font color=#1a73e8>作者：</font>** Asad Ikram, Ella Haig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparing machine-labelled sentiment across social media platforms is now routine: differences in classifier scores between platforms are read as differences in public opinion. These comparisons rest on an assumption that the classifier measures the same construct, on the same scale, on every platform. Some studies check a classifier's validity platform by platform, but to our knowledge none has modelled the platform as a facet of the classifier's measurement. We adapt the psychometric equivalence toolkit (generalizability theory, measurement invariance and differential item functioning, and score linking) to machine-labelled policy sentiment, treating the platform as a survey mode, and specify a six-step protocol with anchor events fixed in advance, an anchor-density audit, and a two-classifier convergence control. A simulation with known ground truth illustrates what the assumption can cost in one generating configuration fixed in advance: across 500 replications, because the platforms measure through different functions, a pooled index that takes platform scores at face value reports the wrong sign of aggregate sentiment on nearly a quarter of days, whereas an index adjusted with each platform's known measurement function does so on under one day in sixty on average. A case study of the instrument from the first author's MSc dissertation, a fine-tuned BERT classifier over 255,446 UK economic-policy comments from Twitter/X, Reddit, YouTube, and Quora, motivates the design and illustrates the instrument-dependence the protocol addresses. The full four-platform application, under fresh collection with the pre-specified design, is the designated follow-up study. The protocol lets a researcher test whether pooling platforms is defensible in a given corpus, or whether platform scores must be linked before any average is taken.

---


### 481. [Image Tokenizers Should Be Trained Between Images](https://arxiv.org/abs/2610.16759)

**<font color=#1a73e8>作者：</font>** Ole Beißwenger, Jan-Niklas Dihlmann, Hendrik Lensch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models generate images as codes of an image tokenizer, whose decoder turns them into the pixel image. Recent tokenizers improve how well these codes reconstruct an image and how easily a generator learns them. Yet a generator does not reproduce the codes of training images, and when a generated code lands outside what the decoder expects, the decoded image contains imperfections. Current methods make the decoder more robust to generated codes by adding noise during training. However, generated codes lie between the training codes and resemble their mixture more than one of them plus noise. To improve generated images, decoders should therefore be trained on codes in the space between training samples. We propose InterpTok, which fine-tunes MAETok to decode mixtures of image codes into natural images. Since no target image exists between two training samples, a discriminator judges whether each decoded mixture looks as natural as its two sources. A mixing ratio loss requires the decoded mixture to keep the mixing ratio of the two codes. Together, they prevent collapse to a trivial solution and yield a sharp and natural composition of both images. InterpTok keeps MAETok's reconstruction quality and improves interpolation quality more than threefold, the best of all tokenizers in a recent benchmark. Beyond interpolation, InterpTok improves the generation FID of a matched diffusion transformer from 11.61 to 8.48 without guidance, and even reaches 8.11 at an eighth of the sampling steps, where the generator on MAETok's codes worsens. The generator trained on our tokenizer also reaches the final result of the one trained on MAETok at half the training steps. Our findings show that the space between image codes can and should be explicitly supervised rather than ignored.

---


### 482. [Towards Complementary Keypoint Detection via Mixture of Detectors](https://arxiv.org/abs/2610.16762)

**<font color=#1a73e8>作者：</font>** Xiaoyong Lu, Guobao Xiao, Dong Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Keypoint detection plays a central role in geometric vision pipelines. Existing detectors exhibit complementary strengths across different scene structures and keypoint budgets, and reliance on a single detector often results in suboptimal keypoint distributions. Motivated by this observation, we propose \textbf{Mixture of Detectors (MoD)} for dense matching pipelines, a unified framework for complementary keypoint detection through the adaptive composition of heterogeneous detectors. MoD first distills heterogeneous detectors into a unified model, allowing diverse detection maps to be predicted efficiently within a single forward pass. Detector selection is subsequently formulated as a patch-wise, budget-conditioned decision process, in which a lightweight router assigns the most suitable detector to each local region. To avoid heuristic supervision, the router is trained with task-driven rewards derived from downstream matching quality, jointly capturing both keypoint quantity and precision. Extensive experiments on MegaDepth, ScanNet, and HPatches demonstrate that MoD consistently outperforms strong baselines across a wide range of keypoint budgets, demonstrating its effectiveness in improving keypoint distribution and downstream geometric performance.

---


### 483. [Relational Learning as World Modeling](https://arxiv.org/abs/2610.16763)

**<font color=#1a73e8>作者：</font>** Zheyu Zhang, Gjergji Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational learning typically predicts from a database state, but decision making asks a different question: how will that state change under an action? In operational systems, the answer depends on system-specific dynamics that may not be visible in the database itself. We view each such system as a relational "world" and ask whether a model can infer how it behaves from observed executions. We introduce TabWM (Tabular World Model) and WorldRel, a generator of executable relational worlds for pretraining. Given executions from an unseen world, TabWM uses them as context to predict the sparse structured edits caused by a new action without parameter updates. Across 512 held-out worlds, complete-edit F1 rises from 0.016 with no observed executions to 0.685 with 64, where a correct edit must match its operation, relational location, and value. Because these predictions are explicit relational edits, they can be applied recursively to imagine candidate futures and compare actions before they are taken. Broader search over these predicted futures improves the realized return of selected action sequences. Together, these results suggest that relational dynamics can be learned in context, broadening relational learning from modeling system state to modeling how that state changes under action.

---


### 484. [Game-Creation-Agents: Autonomous Game Production](https://arxiv.org/abs/2610.16776)

**<font color=#1a73e8>作者：</font>** Tencent Multimodal RL Team, Xiangxin Zhou, Jiaqi Tang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Game-Creation-Agents (GCA) turns a natural-language request into a runnable Phaser 4 browser game. The pipeline first builds a multimodal game design document that couples mechanics and scene contracts to grounded visual references. It then projects that document into a runtime scaffold, machine-readable contracts, and deterministic tests. Eight specialized agents next carry out production: scenes are implemented serially, assets are produced in parallel, and one reduced manifest joins the two branches into a single build. Build-linked real-UI checks and a code-blind critic then verify that build and decide whether the game may ship. Each blocker returns to the agent that owns the affected artifact for a bounded repair, and the game is released once all the gates pass. We evaluate finished games separately, through their rendered interfaces alone, over prompt-matched tasks run under a common protocol. GCA achieves stronger requirement satisfaction, core mechanics, content depth, and functional visuals than a comparable open pipeline. In a side-by-side human study, raters also score GCA's games higher on every dimension and prefer them overall.

---


### 485. [PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents](https://arxiv.org/abs/2610.16778)

**<font color=#1a73e8>作者：</font>** Zian Yuan, Wei Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud graphical user interface (GUI) agents send instructions and screenshots to remote planners, exposing personally identifiable information (PII). Existing placeholder defenses mask detected spans and reuse exact strings. Fragmented or changed forms can expose PII or break entity continuity across turns. PrivacyGuard addresses this private reference problem with source-linked sanitization (SAN) and a structured reference lifecycle (REF). SAN reconstructs fragmented or overlapping evidence and rewrites the complete source extent. REF links changed appearances to session entities and supports locally resolvable references without returning raw values to the upload path. In five-turn sessions scored against common gold, PrivacyGuard reduces audited source-value leakage by 33.55\%--82.60\% relative to the closest prior full-pipeline system in all four reader--language combinations. REF raises strict cross-form continuity from 0.04 under exact-value reuse to 0.81. In reference-required Android tasks, verified completion rises from 8/30 and 7/30 to 17/30 and 20/30. On AndroidLab, PrivacyGuard achieves the highest or tied-highest task-success point estimate among protection pipelines for all four planners. On PrivScreen, it reduces fixed-reader field exposure by 62.72\%--62.84\% relative to the same baseline. PrivacyGuard lowers upload exposure while preserving a locally resolvable task path.

---


### 486. [InfoVis: Unified Slide Image Generation and Editing](https://arxiv.org/abs/2610.16784)

**<font color=#1a73e8>作者：</font>** Jiahao Wang, Xiyan Jiang, Chenyuan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating and editing presentation slides requires models to combine accurate text rendering, instruction following, visual grounding, aesthetic design, and precise editing within one canvas. Existing work covers only subsets of these capabilities and lacks large-scale slide-native supervision and diagnostic evaluation. We formulate four slide-centric tasks and build a scalable data engine with over 13M continual-pretraining records and 1.9M supervised fine-tuning records. We also introduce VisSlideBench, a benchmark of 1,527 manually screened instances that covers all four tasks with task-specific, multidimensional evaluation. Its automatic rankings agree with blinded, dimension-wise human rankings. Using these resources, we train InfoVis, a unified 9B slide generation and editing model. On VisSlideBench, InfoVis leads every evaluated open-source model on all eleven metrics and scores 7.94 overall against 7.99 for Nano-Banana-2. Starting from FLUX.2-klein-base-9B, slide-specific post-training adds 1.6 points overall, with the largest generation gains in content faithfulness; the remaining gap to proprietary models is smallest in content faithfulness and largest in aesthetic quality. Built on InfoVis, our document-to-slide workflow achieves the second-highest Aesthetics score on the external SlidesGen-Bench. We will release the model, code, data, and benchmark.

---


### 487. [Efficient Preconditioned Optimization Methods with Frequent Directions](https://arxiv.org/abs/2610.16792)

**<font color=#1a73e8>作者：</font>** Sifan Yang, Yuanyu Wan, Yibo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimization methods have received considerable attention in recent years due to their strong empirical performance. However, they generally require maintaining a preconditioning matrix, which incurs prohibitive computational overhead in large-scale applications. To address these limitations, we investigate the acceleration of preconditioned optimization methods through frequent directions (FD), a widely used matrix sketching technique. We first propose FTSL by integrating FD with adaptive subgradient methods under the primal-dual framework and adding back the cumulative information discarded by FD. FTSL obtains a tighter regret bound than existing state-of-the-art results. We then apply a doubling trick that further reduces the time complexity of FTSL, while maintaining the same regret guarantee. We also consider optimization over matrix-valued decision variables and exploit their structural properties to construct sketched preconditioners. We develop FTSL-Shampoo by adapting FD to Shampoo and give a novel analysis under the primal-dual framework. To further mitigate its computational complexity, we design one-sided variants of FTSL-Shampoo under both mirror descent and primal-dual frameworks. Our algorithms not only reduce the computational cost of FTSL-Shampoo, but also achieve tighter regret bounds. We extend our methods to offline stochastic convex optimization and exploit smoothness to achieve faster convergence rates. Finally, we introduce practical variants of our algorithms and empirically demonstrate their efficiency and effectiveness across a broad range of tasks.

---


### 488. [Beyond User-Side Defenses: Image Protection in Open-Weight Diffusion Models](https://arxiv.org/abs/2610.16835)

**<font color=#1a73e8>作者：</font>** Jihye Kang, Jiwon Park, Namhyuk Ahn  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model providers can support image protection, but open-weight deployment introduces practical constraints. We propose four requirements: protection effectiveness, clean fidelity, compatibility, and tamper resistance. We incorporate long-horizon attack simulations to strengthen resistance to protection removal. Experiments with a single protection tool show improved resistance to re-alignment at a cost to clean fidelity, motivating further research toward practical model-side protection.

---


### 489. [Few-for-Many Best-Arm Identification in Multi-Objective Bandits](https://arxiv.org/abs/2610.16840)

**<font color=#1a73e8>作者：</font>** Bo Xue, Yilu Liu, Haodong Jing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world systems often serve many objectives but can deploy only a few options, whose performance must be learned from noisy feedback. Modeling each option as an arm in a multi-objective bandit, we introduce \emph{few-for-many best-arm identification}, which seeks a small set of arms minimizing the worst weighted degradation from the objective-wise optima, rather than the best arm for every objective. We consider both known objective groups and latent groups specified only by a representative budget, and propose \textsc{GFM-Elim} and \textsc{AFM-Elim} with instance-dependent sample-complexity guarantees. For Gaussian rewards, we further derive a lower bound for the latent-group setting and show that it is asymptotically attainable with high probability by an oracle-based Track-and-Stop procedure. Our results show that sharing observations across objectives and ignoring irrelevant objective-wise distinctions can substantially reduce the sampling cost, as confirmed by experiments on synthetic and real-world tasks.

---


### 490. [A Multi-Task Deep Learning Framework for Pose-Invariant Face Recognition and Facial Landmark Localization](https://arxiv.org/abs/2610.16849)

**<font color=#1a73e8>作者：</font>** Ali Ashkeyev, Zukhra Abdiakhmetova  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems often experience performance degradation under large pose variations due to changes in facial appearance and visibility of discriminative features. This study presents a multi-task deep learning framework that jointly addresses pose-invariant face recognition and facial landmark localization within a unified architecture.
To enable simultaneous optimization of identity recognition and facial structure learning, the original Cross-Pose Labeled Faces in the Wild (CPLFW) dataset was adapted into a multi-task learning dataset by associating facial images with identity labels and five-point landmark annotations. The proposed framework consists of two task-specific branches operating on a common facial input: a ResNet50-based branch for identity recognition and an EfficientNetV2B0-based branch with spatial attention for facial landmark localization. The two objectives are jointly optimized using a weighted multi-task loss, allowing the model to learn complementary semantic and spatial facial representations.
The proposed framework was evaluated on the prepared CPLFW-based multi-task dataset. Unlike the original CPLFW benchmark, which focuses primarily on identity recognition, the proposed dataset adaptation incorporates five-point facial landmark annotations to enable joint recognition and localization learning. Experimental results demonstrate that the model achieves a validation recognition accuracy of 81.58% and a facial landmark localization mean squared error of 96.38. The results indicate that combining identity classification and landmark regression within a single optimization framework provides an effective approach for learning robust facial representations under cross-pose conditions
The proposed method demonstrates the potential of multi-task learning and attention-based feature refinement for unconstrained facial analysis.

---


### 491. [Radial Tail Repair: Post-Training Correction for Diffusion and Flow Models](https://arxiv.org/abs/2610.16851)

**<font color=#1a73e8>作者：</font>** Hamza Cherkaoui, Hélène Halconruy, Antonio Ocello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-matching models may struggle to accurately represent distributional tails, especially for heavy-tailed data. Existing approaches often use heavy-tailed noise or modify the generative dynamics, requiring dedicated retraining and more difficult estimation. We take a simpler approach: rather than relearning the full distribution, we correct only the model's behavior in the extreme regime. Our method builds on the radial-angular decomposition of multivariate heavy tails, where radius and direction become asymptotically independent. This allows us to preserve the directional structure learned by the pretrained model and correct only its radial tail. We estimate the tail onset from reference and generated samples, then rescale generated extremes so that their radial survival matches the target distribution. The resulting method is a lightweight post-training correction applied to a frozen diffusion or flow-matching model, requiring neither retraining nor changes to its sampling dynamics. Experiments on challenging synthetic heavy-tailed distributions and real weather and wildfire datasets show that this simple correction substantially improves extreme-tail coverage using only a small number of fitting samples.

---


### 492. [Vision Models Capture Complementary Representations in Children That Converge in Adults](https://arxiv.org/abs/2610.16860)

**<font color=#1a73e8>作者：</font>** Domenic Bersch, Timothy Schaumlöffel, Michela Proietti 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How the relationship between image-text aligned and vision-only models changes across development remains unknown. We applied time-resolved representational similarity analysis to EEG data from 8-year-olds, 12-year-olds, and adults. CLIP showed significant model-brain alignment already in children, whereas vision-only models aligned more strongly later in development. Residual analyses revealed complementary structure, with CLIP retaining alignment beyond an architecture-matched vision-only model from age 8. Much of the model-brain alignment reflected semantic structure, with EEG representations of category and animacy strengthening toward adulthood, while alignment with low-level image properties remained weak across age. Together, these findings suggest that image-text aligned and vision-only models capture complementary aspects of developing visual representations and may provide useful constraints for AI systems that aim to learn and adapt over time.

---


### 493. [GpFlash: Maximizing Speed and Minimizing Memory for Gaussian Process Training and Prediction](https://arxiv.org/abs/2610.16861)

**<font color=#1a73e8>作者：</font>** Andre Marchildon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents GpFlash, a Gaussian process library that is focused on fast training and posterior evaluations, minimal memory usage, and scalability to high-dimensional problems. GpFlash was compared to the popular GP libraries scikit-learn, GPy, GPflow, GPyTorch, and SMT on a MacBook Pro and the supercomputer Trillium. GpFlash was found to use less memory and to be faster for training and posterior evaluations relative to the other GP libraries for all cases considered. For example, when using $\nx = 10^4$ training points in a 10-dimensional space GpFlash required 9.6 to 35 times less memory and was 2.6 to 54 times faster than the other GP libraries for the evaluation of the marginal log likelihood and its gradient. The memory reduction was achieved by only using one matrix of size $\nx \times \nx$ to store different symmetric matrices in its lower and upper triangular entries. The computational speedup was the result of designing algorithms to access memory efficiently, using BLAS and LAPACK methods extensively, and factoring kernel equations so that expensive exponential calculations could be reused. GpFlash was more than 440 times faster than all of the other GP libraries considered when evaluating the posterior mean together with its gradient for the case with $10^4$ training points and 10 dimensions. GpFlash is available at this https URL.

---


### 494. [From Volpiano to Pixels: 30,000 Lines of OMR Ground Truth for Medieval Chant](https://arxiv.org/abs/2610.16862)

**<font color=#1a73e8>作者：</font>** Robert Klugseder  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical music recognition (OMR) for medieval chant lacks training data linking manuscript images to musical symbols across notational families. Using existing Volpiano transcriptions from the Cantus Database, we created 30,567 image-target pairs from ten sources in eleven exports, including 339 verse fragments. Their target sequences contain 1,952,143 tokens. The pipeline locates staff systems, infers clefs and maps known pitches to staff positions. Six detector families handle the different layouts and notations. Where heuristics failed, two small U-Nets learned staff lines and clef letters from manual annotations. Reviews of sampled export lines found zero to four pitch or clef errors, but used different error definitions and do not provide a uniform audit of the corpus. A CRNN trained from scratch achieved a symbol error rate of 9.6 % on 3,086 test lines. The earlier model, trained mainly on Austrian sources of the 15th and 16th centuries, scored 45.3 %. In three separate training runs, each excluding one manuscript, error rates on the excluded manuscript were 21.5-31.0 %. Model-assisted alignment recovered a further 2,686 lines.

---


### 495. [Better together? A performance theory of human-machine skill policies under generalization difficulty](https://arxiv.org/abs/2610.16863)

**<font color=#1a73e8>作者：</font>** Riccardo Zanardelli  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Organizations pairing a human and a machine on a task decide, often by default, which executes each instance and what happens when both do. We account for what this attains under the squared rule, with performance distributed over instances to capture generalization difficulty. A gross stake lies between the skills' mean and best per instance. It splits at the best single skill into a systematic part, known from separate assessments and secured by commitment, and a residual, the expected value of perfect information on which skill each instance favors, known only from paired observation and split further by classes. Skills set the stake; workflows decide the take, via two channels. Routing directs work, weighting or selecting responses; with binary truth it is capped by the best skill per instance. Reading responses as joint evidence is not routing; what they jointly reveal caps it. Synergy lets skills interact before responding; bounded by no skill either way, its lift over independent responses must clear a break-even and can fall below one. As algorithms, arrangements form a ladder stating what each reads, holds and records, and a procedure whose checks keep earlier gains when class means are known and lose little on finite records given a margin. The theory extends to many skills, each worth what it adds where it beats all others held, and to competing skills, where at parity a single failure's allowed cost decides. In a public chest-radiograph study with 227 radiologists, they are near parity with the model and the stake is mostly residual; assisted reading, no better on average originally, returned less than averaging both responses; recalibrating the model alone beats any deployable arrangement of raw responses. Organizations can learn from their records what is at stake, which arrangement collects it and what evidence each step needs; pricing costs and errors is future work.

---


### 496. [Toward Realistic Privacy Risk in FL-Enabled OT Intrusion Detection Systems](https://arxiv.org/abs/2610.16872)

**<font color=#1a73e8>作者：</font>** Assunta Imperatrice, Luigi ROmano  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In Operational Technology (OT) environments, Federated Learning (FL) is increasingly adopted to train Intrusion Detection Systems (IDSs) without sharing raw operational data across facilities. However, model updates may still leak sensitive information about industrial processes, creating privacy risks that remain largely invisible within current OT security architectures. Existing reference models, including the Purdue hierarchy, do not explicitly represent the FL learning lifecycle, making privacy leakage difficult to observe and evaluate. To address this gap, we introduce the ML Plane, a novel architectural abstraction that integrates FL workflows within OT systems, enabling visibility of learning-related information flows that are not explicitly represented in traditional OT architectures. Building on the proposed ML Plane, we outline a privacy auditing framework for FL-enabled OT systems. The framework uses Federated Membership Inference Attacks (FedMIA) as an initial assessment mechanism and is being instantiated within a Smart Grid testbed to support the future evaluation of privacy risks under realistic OT deployment constraints.

---


### 497. [CLIVO: Differentiable Cluster-Based Instruction Mixing with Learned Validation Objectives](https://arxiv.org/abs/2610.16876)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Rui Hu, Batian Di 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Target-aware multimodal instruction selection requires useful examples and an appropriate balance of supervision. Sample-level rankings can overrepresent similar content without optimizing this balance; group-level methods face coarse units, predefined set-level validation signals, and costly or inaccurate mixture search. We propose CLIVO, a target-aware framework connecting fine-grained semantic allocation, automatically learned validation objectives, and differentiable mixture search. Specifically, semantic clusters provide independently adjustable shares at the hundred-cluster scale. Correlations between per-example merged-proxy losses and real probe performance identify target-relevant validation examples; learned nonnegative weights combine their losses into an objective. A single backward pass through the merged proxy supplies gradients for all shares, avoiding an additional mixture-response regression model. Selecting 100K instructions from an 8M pool, CLIVO attains 97.2% of the full-data four-target average score with only 1.25% of the data. It improves on the strongest evaluated selection baseline by 1.16 points using random within-cluster sampling; combining learned quotas with sample ranking increases this advantage to 1.55 points. Analyses show that finer units benefit most targets, short-trained experts preserve mixture responses, sample weighting retains useful validation information, and direct search consistently reduces the learned objective. CLIVO also supports interpretable allocation, modular selection, and reuse across targets and granularities.

---


### 498. [Acceptable Misalignment](https://arxiv.org/abs/2610.16881)

**<font color=#1a73e8>作者：</font>** Maud van Lier, Ludovica Marinucci, Vieri Giuliano Santucci 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is a specific challenge designers face in developing autonomous robots capable of open-ended learning. This challenge is how one can develop such systems in an ethically sound way when there are many unknowns during design time about their manner of deployment, what they can and will learn, and how these systems will act on the basis of what they have learned. One response to this challenge is to align, as far as possible, the activities and goals of autonomous robots with human values, raising the question of how to make this alignment possible, a question known as the value alignment problem. We argue that the value alignment problem faces a number of challenges that show that full alignment is both theoretically and practically impossible, meaning that misalignment incidents will keep occurring. This undermines current alignment approaches, as the attempt to maximize alignment cannot properly deal with the possibility that the risk of misalignment that remains after alignment methods have been implemented might still be unacceptable to society. To overcome this difficulty, we argue that a shift in perspective is required from a focus on the maximization of alignment to the conditions under which misalignment incidents become acceptable. In this paper, we explore what this shift in perspective entails. We introduce the concept of acceptable misalignment, formulate normative requirements for alignment mechanisms aimed at bringing misalignment incidents to an acceptable level, and we conclude by presenting a new methodological framework that consists of alignment mechanisms that can meet these requirements.

---


### 499. [Learning Operators for Symmetry Discovery: From Lie Groups to Local Symmetry Geometry](https://arxiv.org/abs/2610.16884)

**<font color=#1a73e8>作者：</font>** Pavan Karjol, Scindhiya Laxmi, Prathosh AP  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous symmetry discovery is typically formulated as a separate estimation problem for each function or dataset. We instead investigate whether the map from a function to its symmetry structure can be learned across a family of functions from finite observations. Using the infinitesimal differential characterization of continuous symmetries, we formulate this map as an inverse symmetry operator, analogous to an inverse PDE problem. For global Lie-group symmetries, we establish a representation-theoretic population characterization: the symmetry Lie algebra is the nullspace of a positive-semidefinite operator constructed from representation coefficients and the infinitesimal group action. We also show that the inverse symmetry operator is equivariant under coordinate changes through the adjoint action. This characterization separates the geometric symmetry map from finite-sample estimation, motivating a hybrid approach that amortizes statistically difficult components while retaining analytic structure. On SO(5) benchmarks, amortized equivariant estimation of harmonic coefficients improves symmetry recovery from sparse observations, whereas ordinary least squares suffices for SL(2,R). We extend this viewpoint to local symmetries, where symmetry directions form smoothly varying tangent distributions rather than a fixed Lie algebra. Under the Lie-bracket consistency condition, Frobenius' theorem guarantees local integral submanifolds along which observables remain unchanged. We recover this geometry using a hybrid estimator that learns observation weights while preserving analytic differential and geometric recovery. Across global, non-compact, local, and physically motivated synthetic benchmarks, our results support learning the statistically difficult finite-sample components while preserving the known geometric structure of symmetry recovery.

---


### 500. [Transparency as Answerability: Role-Dependent Information Flow Modeling](https://arxiv.org/abs/2610.16887)

**<font color=#1a73e8>作者：</font>** Mattias Brännström, Themis Dimitra Xanthopoulou, Lili Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transparency in AI-supported decision systems is widely required but poorly defined. Existing approaches treat transparency as a property of systems or components, producing characteristic failures: assessments that do not transfer across organizational boundaries, stakeholder questions that cannot be formulated within the available frame of analysis, and component-level findings that say nothing about system-level behavior. We propose treating transparency as a relation: a system is transparent to a stakeholder to the degree that their legitimate questions are answerable from its structure. We formalize this using information flow networks, in which transparency questions are expressed in terms of network structure and answerability is the condition that the system settles them. The framework supports three dimensions of analysis: structural answerability from the network alone, compositional answerability across organizational boundaries for deployed systems, and role-dependent answerability given a stakeholder's accessible sub-network. We demonstrate the framework on a real pre-integration assessment of an AI recruitment tool in a public sector municipality. The assessment uses participatory design and interviews to model the decision system structure. We show how structural and role-dependent transparency questions can be formally stated and analyzed across the Provider and Deployer boundary where the AI system is composed together with the deployer's decision process.

---


> [!TIP]
> 当前位于：**451-500**（第 10/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
