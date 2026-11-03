# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 401. [CytoWave: Perturbation-Centric Pretraining for Single-Cell Response Prediction](https://arxiv.org/abs/2611.02311)

**<font color=#1a73e8>作者：</font>** Yuwei Miao, Jingquan Yan, Hehuan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting gene expression under perturbations from single-cell data is a fundamental task for modeling cellular responses, with applications in discovering gene function and designing therapeutics. However, existing methods often struggle to generalize across datasets due to differences in experimental protocols, biological contexts, and species. We present \textbf{CytoWave}, a perturbation-centric pretraining framework for single-cell genetic perturbation response prediction. We leverage large-scale cross-species perturbation datasets unified via orthology and train CytoWave in a two-stage manner. In the first stage, we learn reference control cell states via masked gene expression recovery on unperturbed cells. In the second stage, we pretrain the model to predict perturbed gene expression given control states and perturbation signals, together with a contrastive objective that aligns latent representations of perturbation responses with perturbation signals. We perform strict dataset-held-out evaluation across multiple condition combinations and case studies of pathway activity changes, demonstrating consistent and effective performance of CytoWave in predicting single-cell genetic perturbation responses.

---


### 402. [Improving Financial Cybersecurity Through Fraud Transaction Detection with Deep Learning](https://arxiv.org/abs/2611.02312)

**<font color=#1a73e8>作者：</font>** Harish Kant Pathak, Rahul Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial fraud detection remains a critical challenge in cybersecurity, with traditional rule-based systems struggling to keep pace with evolving attack patterns. This paper presents a deep learning approach for fraud transaction detection, leveraging neural network architectures to identify anomalous financial behaviors with high accuracy. We evaluate multiple deep learning models including LSTM, CNN, and hybrid architectures on real-world financial transaction datasets, demonstrating significant improvements over conventional machine learning baselines. Our approach achieves robust performance in detecting fraudulent transactions while minimizing false positives, providing a scalable solution for enterprise financial cybersecurity systems

---


### 403. [The DynaCell Evaluation Suite for Dynamic 3D Virtual Staining of Live Cells](https://arxiv.org/abs/2611.02324)

**<font color=#1a73e8>作者：</font>** Alexandr A. Kalinin, Dihan Zheng, Taylla Milena Theodoro 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how cells respond to perturbations over time is central to cell biology and drug discovery. Live-cell imaging captures the dynamics of perturbation-induced phenotypes in individual cells. While fluorescence imaging can visualize specific molecular phenotypes, labeling and repeated illumination often affect cell health. Virtual staining offers an alternative by predicting these fluorescence images from images acquired without fluorescent labels. Although many virtual staining models have been developed, their performance on volumetric time-lapse data remains poorly characterized. We address this gap with an evaluation suite for 3D time-lapse virtual staining of live cells. The suite combines paired 3D time-lapse images acquired with and without fluorescent labels, a set of baseline models, and three metric tiers measuring pixel-level fidelity, organelle segmentation performance, and single-cell phenotype similarity. Using this evaluation suite, we study metric and model behavior across 3 cell types, 2 microscopes, 4 organelles, and 3 perturbation states. We find that regression baselines better predict the spatial localization of target organelles, whereas the generative baseline better captures the distribution of phenotypes across cells. These differences expose trade-offs between structural and phenotypic fidelity that are obscured by single-metric evaluation and suggest how virtual staining models can be developed for diverse downstream tasks such as localization, segmentation, tracking, and phenotypic profiling. We release the curated datasets, baseline checkpoints, and evaluation code as part of DynaCell, a broader framework for image-based profiling of cell-state dynamics.

---


### 404. [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341)

**<font color=#1a73e8>作者：</font>** Shaoheng Fang, Yiqun Mei, Hanwen Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent interactive video world models generate visually compelling videos from a single image, following user-provided camera motion and text prompts. However, such low-level control demands substantial user effort to realize a high-level intent, and the generated world struggles to remain persistent as the exploration proceeds. In this work, we present AgiWorld, an agentic video world model that explores and builds a persistent world from a single image and a free-form instruction. For high-level planning, our agent AgiWorld-Agent designs the world and the journey through it in a world state and directs the exploration. For low-level realization, our video world model AgiWorld-WM generates the video chunk by chunk and stores it with its geometry in a spatial memory, from which the agent updates its world state. This closed loop keeps the world faithful to the user's intent and keeps the agent's world state consistent with the generated content throughout the exploration. We co-design the two levels around the shared spatial memory and an interface of metric camera trajectories and structured prompts. In AgiWorld-WM, to handle occlusion and accumulated geometric errors in the spatial memory over long rollouts, we propose occlusion-aware history selection, which retrieves past views by surface visibility, and reliability-based memory maintenance, which prefers reliable geometry and earlier observations. AgiWorld-WM achieves state-of-the-art overall performance on world revisiting and exploration benchmarks, and qualitative results and ablations show that AgiWorld builds persistent worlds from free-form instructions over minute-long journeys. Persistence thus arises not from the video model alone but from its closed loop with the agent.

---


### 405. [Malware Clustering in the Wild: Taxonomy, Challenges, and Evaluation Metrics](https://arxiv.org/abs/2611.02380)

**<font color=#1a73e8>作者：</font>** Raguvir S, Bojing Li, Prajna Bhandary 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As malware continues to grow in volume, diversity, and sophistication, clustering has emerged as a critical technique for analyzing large malware corpora. Clustering enables the discovery of structural relationships, behavioral patterns, and evolutionary trends, and is widely used to group unknown samples, infer malware family boundaries, and identify novel variants. However, existing research remains fragmented, employing a wide range of clustering techniques with no unified perspective that systematically organizes prior work or clearly identifies gaps in the literature. This survey addresses this gap by organizing previous malware clustering research into seven categories: centroid-based, hierarchical-based, density-based, distribution-based, mixed- type, fuzzy, and AI-driven approaches. In addition, this survey summarizes publicly available malware datasets commonly used in clustering research and examines the feature representations derived from these datasets. Our goal is to clarify the current landscape and outline promising avenues for future research on malware clustering, including how AI-driven methods may shape large-scale and reproducible analysis.

---


### 406. [IMUdrape: Generating Garment-Mounted Virtual IMU Data from Text through Physics-Based Cloth Simulation](https://arxiv.org/abs/2611.02393)

**<font color=#1a73e8>作者：</font>** Zikang Leng, Thomas Plötz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inertial sensors are moving into clothing, from sensorized sportswear to garments instrumented with hundreds of IMUs. Sewn into clothing, a sensor no longer moves rigidly with the body: loose fabric slides, twists and swings, so a garment-mounted sensor records the motion of the fabric as well as that of the body, and this extra motion differs from one garment to the next. Models for such sensors need training data recorded with the deployed garment, yet labeled data are scarce. Virtual IMU data generated from videos or text have eased this scarcity for body-attached sensors, but existing generators attach their virtual sensors rigidly to the body. We present IMUdrape, which generates garment-mounted virtual IMU data from text through physics-based cloth simulation. IMUdrape synthesizes motion from activity descriptions, reconstructs the target garment as a sewing pattern from photographs, places virtual IMUs at the deployment's real sensor positions, and simulates the garment with an intersection-free contact solver, so that every simulation yields paired garment and body signals. On four real datasets with clothing-mounted sensors, IMUdrape improves on existing virtual-data approaches for both activity recognition and full-body pose estimation. With one real subject, its data improve recognition macro-F1 by 7% to 46% over real data alone and by 2% to 11% over body-mounted virtual data from the same motion. When the garment is simulated on recorded motion, the pose error without any real training data falls by 30% to 33% relative to generated motion, and garment data remain 12% more accurate than body data. IMUdrape thus reduces the amount of real data that garment-mounted sensing requires.

---


### 407. [Spatial Organization Is Accessibility Structure: Hierarchical Screen Reading of Mobile UIs](https://arxiv.org/abs/2611.02410)

**<font color=#1a73e8>作者：</font>** Yongxiang Hu, Xuan Wang, Qingyang Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Screen readers for blind and low-vision (BLV) users flatten mobile UIs into a linear sequence. Modern mobile UIs, however, contain dozens of elements grouped by spatial layout. Such linear access is ill-suited for BLV users, who must infer each element's meaning and which elements form a functional unit. Drawing on a quantitative TalkBack audit and formative interviews, we present Spatial Screen Reader (SeeR), which builds a function-aware hierarchy from accessibility metadata and provides unit summaries with hierarchical navigation. Compared with TalkBack, SeeR reduces non-informative focus stops by 82.1% and navigation steps by 52.7%. With ten BLV participants, summaries helped them connect controls to their functions and skip nonessential elements, especially on unfamiliar pages, though extra navigation levels added effort when the target was already known. These findings recast spatial organization as accessibility information: apps and platforms should expose it, rather than leaving screen readers to infer it post hoc.

---


### 408. [A Novel Federated Learning Framework for Defending Against Gradient Inversion Attacks](https://arxiv.org/abs/2611.02412)

**<font color=#1a73e8>作者：</font>** Pengxin Guo, Ziying Huang, Shuang Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) offers a paradigm for collaborative machine learning model training among clients, preserving data privacy by avoiding direct data sharing. However, the gradient information exchanged in FL has been shown to be vulnerable to Gradient Inversion Attacks (GIA), which can reconstruct sensitive user data. To counter these threats, various privacy-enhancing technologies like Secure Multi-party Computing (SMC), Homomorphic Encryption (HE), and Differential Privacy (DP) have been integrated into FL. While effective, these methods often introduce significant trade-offs between privacy and model utility. By revisiting the key to privacy exposure in FL under GIA, which lies in the frequent sharing of model gradients that contain private data, we take a new perspective by designing a novel privacy-preserving FL framework that effectively ``breaks the direct connection'' between the shared parameters and the local private data to defend against GIA. Our proposed framework, HyperFL++, leverages hypernetworks to generate local model parameters, where only the hypernetwork parameters are aggregated by the server. To ensure practicality, HyperFL++ incorporates a Row-wise Kronecker Decomposition (RKD) to mitigate the memory and communication overhead from the hypernetwork. Comprehensive theoretical analysis and extensive experiments validate our method's effectiveness in protecting data privacy while maintaining high model utility. Our code is available at this https URL.

---


### 409. [Behavior-Discriminative Reward Shaping for Reward-Robust Reinforcement Learning](https://arxiv.org/abs/2611.02415)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Fangzheng Wu, Brian Summa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-robust RL typically models misspecification by specifying an uncertainty set that constrains the discrepancy of plausible rewards from a base reward. However, such reward space discrepancies can be behaviorally irrelevant: under potential-based reward shaping (PBRS), many distinct rewards preserve policy ordering. This can introduce substantial redundancy into standard uncertainty sets and degrade optimization performance. We propose Shaping-Aware Reward-Robust RL, which constructs uncertainty sets over PBRS equivalence classes by projecting each reward to a canonical representative, ensuring that the resulting set contains only rewards that induce behaviorally distinct policy rankings. We prove that this projection preserves the optimal robust value while shrinking the uncertainty set and improving empirical performance. Using the connection between robustness and regularization, we obtain a practical algorithm to solve the shaping-aware reward-robust RL problem and enjoy convergence guarantees under standard assumptions. Experiments on benchmarks spanning diverse task domains and levels of complexity show consistent improvements over representative robust RL baselines and exhibit improved robustness to reward perturbations.

---


### 410. [TERA: Task-Evidence Restoration for Underwater Object Detection under Bandwidth-Constrained Transmission](https://arxiv.org/abs/2611.02419)

**<font color=#1a73e8>作者：</font>** Heejin Kim, Joon-Seok Song, Eunil Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater object detectors are typically evaluated on pre-transmission images, overlooking additional degradation from bandwidth-constrained downscaling and compression. We introduce AquaTX, a controlled benchmark built from real underwater detection datasets with seen and held-out codecs. We also propose TERA, a metadata-blind receiver-side framework combining task-guided pixel restoration and dual-state feature correction while keeping the detector frozen. Under seen compound degradation, TERA improves mean average precision (mAP50:95, averaged over IoU thresholds from 0.50 to 0.95) from 37.7 to 50.0 on DUO-TX and from 31.5 to 41.3 on RUOD-TX relative to the frozen detector without restoration. TERA also preserves clean-input performance and remains competitive with detector fine-tuning under the held-out AVIF codec. These findings support transmission-aware evaluation and task-guided restoration for underwater object detection. Code is available at this https URL.

---


### 411. [Architecture-Aware Mixed Precision for Replica-Exchange Training of Geometry-Aware Neural Operators with Uncertainty Quantification](https://arxiv.org/abs/2611.02427)

**<font color=#1a73e8>作者：</font>** Ujin Jeon, Michael Penwarden, Wenqian Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometry-aware neural operators face substantial computational and memory demands when learning across complex physical domains. We introduce Architecture-Aware Mixed Precision (AA-MP), a replica-exchange training strategy that allocates numerical precision according to replica roles and architecture-specific operations. By retaining FP32 for refinement while selectively employing BF16 for exploration, AA-MP preserves predictive accuracy while improving training efficiency. Across fluid dynamics and three-dimensional structural mechanics benchmarks, AA-MP achieves comparable accuracy to full-precision training over an ensemble of runs, while reducing hot-replica peak GPU memory by 46.9% and training time by up to 25.8%. It also outperforms naive Automatic Mixed Precision (AMP) in memory efficiency and computational cost, with increasing memory advantages at larger model and geometry scales. Ablation studies show that retaining FP32 in the cold-replica is important for predictive accuracy, while additional FP32 operations in the exploratory replica provide limited benefits relative to their computational cost. Finally, conformal prediction for uncertainty calibration shows that AA-MP achieves near-nominal coverage with narrower prediction intervals than the alternatives. These results advance the scalability of geometry-aware scientific machine learning by reducing computational costs without compromising predictive accuracy or uncertainty quantification.

---


### 412. [Singularity-Induced Local Complexity for High-Dimensional Learning Models](https://arxiv.org/abs/2611.02428)

**<font color=#1a73e8>作者：</font>** Atsuyoshi Muta, Masaaki Imaizumi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many overparameterized models that have achieved remarkable success are singular models. That is, the set of optimal parameters consists of multiple points, or the Hessian of the generalization error at such parameters is degenerate, reflecting redundancy in the model parametrization. Therefore, understanding the effective dimension and intrinsic model complexity, beyond the apparent dimension of the parameter space, is essential for studying the generalization ability of such overparameterized models. In this work, we focus on the real log canonical threshold (RLCT) and its localized counterpart, the local RLCT, which are fundamental quantities for characterizing the generalization of singular models. We clarify the theoretical relationship between the local RLCT and existing two key metrics related to generalization under some localization assumption: (I) the rank of the Hessian matrix of the generalization error and (II) the covering number of a family of loss functions. This result provides novel insights into effective dimension and intrinsic complexity of overparameterized models.

---


### 413. [A Parameter-Free Best-of-Both-Worlds Policy for Queueing Bandits](https://arxiv.org/abs/2611.02431)

**<font color=#1a73e8>作者：</font>** Jongyeong Lee, Chansoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online channel scheduling for a single queue served by $K$ channels under bandit feedback. We propose a simple best-of-both-worlds policy that explores when the queue is empty. During busy periods, it selects the empirical best channel while the prescribed conditions hold and, if any condition is violated, switches to a robust bandit policy to clear the queue. For arbitrary arrivals and services determined by an oblivious adversary, our policy achieves $\tilde{\mathcal{O}}(\sqrt{K L_T})$ worst-case queue length regret with high probability, where $L_T$ is the longest busy-period length. This result improves the previous $T^{3/4}$ dependence and matches the worst-case lower bound up to logarithmic factors. Under bounded i.i.d. stochastic models with a unique best stabilizing channel, we show that the cumulative queue length regret converges to a finite problem-dependent constant, and further establish the logarithmic expected worst-case queue length regret bound.

---


### 414. [Evaluating Synthetic Skin Lesion Images for Classifier Training: A Safety-Aware Algorithm](https://arxiv.org/abs/2611.02437)

**<font color=#1a73e8>作者：</font>** Amindu Kumarasinghe, Vinh Bui, Reza Ghanbarzadeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin cancer classifiers need large sets of annotated images, which are scarce, especially for rare lesion types. AI-generated images can fill the gap, but a generator produces images of widely varying quality, so selecting which images to retain is important. That choice usually rests on a single quality score, most often the Fréchet Inception Distance (FID), which has not been tested against what a classifier needs and cannot tell whether the generator memorizes its training photographs. We test that practice with a tournament of 16 quality metrics. Each metric alone selects a training subset from a pool of 275,472 images generated by a diffusion model (EDM2), and a classifier trained on each subset scores the metric per class. The tournament shows that no single metric serves every class: FID computed on Inception features gives the best classifier for one lesion type and no measurable advantage over random sampling for another, and the generation setting it prefers is also the one closest to the training images. We turn these per-class measurements into a safety-aware evaluation algorithm that weights each metric by its measured value in each class and removes images too close to a real training image. On the held-out ISIC-2018 test set, the algorithm improves Macro-$F_2$, a recall-weighted measure of classification performance, over the FID baseline for a Swin-B classifier by +0.0136 to +0.0164 across four safety thresholds (Bonferroni-corrected $p < 0.02$) and over random sampling by about +0.03, though not for ResNet-50. Tightening the threshold improves a memorization-safety score with no measurable change in utility, but every curated set remains less safe than random sampling. The results show a modest but statistically significant gain on the primary classifier, and offer a practical, safety-aware procedure for evaluating and using synthetic data.

---


### 415. [DruMR: A Feedback Driven Mixed Reality Air Drumming System](https://arxiv.org/abs/2611.02447)

**<font color=#1a73e8>作者：</font>** Omar Elgohary, Viktor Radev, James Herbert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper introduces DruMR, a mixed reality (MR) drumming system designed to make learning drums more accessible, responsive, and feedback-driven. By combining Aerodrums hardware with the Meta Quest 3 headset, DruMR allows users to drum in a virtual environment without a physical drum set. Unlike existing VR drumming applications, DruMR emphasizes instructional value through quantitative feedback and future integration of AI-generated insights, refined quantitative and qualitative visualizations, reactive environment modes and more. Overall, this paper reviews the current state of the DruMR system, related works that influenced the systems development, planned user study comparing physical and virtual training, and future work to be added to the system.

---


### 416. [Turbo-GMM: FlashAttention-Inspired GPU-Accelerated Gaussian Mixture Model](https://arxiv.org/abs/2611.02449)

**<font color=#1a73e8>作者：</font>** Momin Abbas, Sadia Asif, Asad Ul Haq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expectation-maximization (EM) for Gaussian mixture models (GMMs) requires scoring $N$ data points against $K$ mixture components. Prior fused GPU implementations, notably Flash-GMM, eliminate materialization of the $N \times K$ responsibility matrix but traverse the component dimension twice to compute normalization terms and accumulate sufficient statistics. We introduce Turbo-GMM, a single-sweep fused EM kernel that completes responsibility normalization and sufficient-statistic accumulation within one traversal of the component dimension. By retaining the complete component axis on chip, Turbo-GMM avoids the second score computation required by the released two-sweep Flash-GMM implementation. Its applicability is limited by register pressure, occupancy, and the component and feature dimensions, making it particularly suitable for large datasets with relatively small numbers of components. For larger configurations, Turbo-GMM employs a two-pass fallback following the established fused design. We establish algebraic equivalence to standard EM in real arithmetic and evaluate sixteen configurations on an NVIDIA A100. Under the reported benchmarking protocol, Turbo-GMM achieves a median $2.15\times$ speedup over the evaluated Flash-GMM implementation and up to $5.3\times$ and $9.9\times$ over PyTorch and \texttt{scikit-learn}, respectively. The results demonstrate the potential of single-sweep component traversal while identifying on-chip resource constraints as the principal limitation of this approach.

---


### 417. [Adjustment control usability and dynamic accommodation in office chairs: A comparative study of two contemporary designs](https://arxiv.org/abs/2611.02452)

**<font color=#1a73e8>作者：</font>** Yejin Kang, Dusan Baek, Dongwoo Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adjustability is a core determinant of ergonomic fit in office chairs, but its benefits depend on users being able to operate the controls and, on the chair, continuing to support the body as posture changes during work. We compared two high-end office chairs, the T90 (Sidiz; Chair A) and the Aeron (Herman Miller; Chair B), in two experiments to explore which design features may explain differences between them. In Experiment 1, 20 participants adjusted ten controls common to both chairs and rated perceived adjustment difficulty on four items. Chair A had significantly lower overall difficulty (Wilcoxon signed-rank test, p = 0.008), with control-level advantages for headrest angle, armrest height, armrest rotation angle and lumbar support position; Chair B was easier for seat height, possibly because its side-mounted lever is more visible than Chair A's underside button. The headrest comparisons involved a third-party headrest fitted to Chair B, and control- and item-level tests were not corrected for multiple comparisons. In Experiment 2, the same participants completed a 15-minute multi-device task requiring repeated posture changes, reach and reorientation, then rated body-part discomfort, general comfort and satisfaction with five components. Discomfort and comfort did not differ; Chair A had higher satisfaction for the seat-pan and lumbar support (exploratory, uncorrected). Interviews suggested links to mechanism properties: Chair B's rear lumbar dial was often described as producing little perceptible change, and for controls without significant differences each chair appeared to leave a different aspect of the same need unmet. These findings suggest mechanical and interface properties that designers of adjustable office chairs may consider for dynamic, multi-device work.

---


### 418. [Learning the Entropic Relaxation: Stable Coarse-Grid Emulation with Neural Discrete Equilibrium](https://arxiv.org/abs/2611.02458)

**<font color=#1a73e8>作者：</font>** Jose Antonio Lara Benitez, Kareem Hegazy, Anastasis Kratsios 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to emulate complicated and computationally-expensive physical systems in an efficient and stable manner is a popular motivation for scientific machine learning (SciML). Stable numerical solvers tend to be computationally expensive, as they attempt to resolve small (spatial and temporal) scales that receive and dissipate spectral energy. Learned coarse-grid forecasters remove the dissipative channel, allowing unresolved frequencies to re-emerge as grid-scale noise (aliasing). In this paper, we use the Neural Discrete Equilibrium (NeurDE) method to explore stable emulation at extremely coarse grids, demonstrating physically-principled control over entropy dynamics that reinforces the physical system's dissipative mechanism. Entropically-stabilized NeurDE produces stable long-time rollouts for thousands of forecasting steps on large Reynolds number turbulent flows ($\mathrm{Re}=100{,}000$) with very coarse grids (down to $\mathbb{R}^{16\times16}$). At these very coarse grid scales, entropically-stabilized NeurDE can be more stable than even our stabilized data-generation numerical method.

---


### 419. [Think Globally, Generate Personally: Multi-View Thinking with Adaptive Generation for Generative Recommendation](https://arxiv.org/abs/2611.02463)

**<font color=#1a73e8>作者：</font>** Yuxuan Hu, Yingyi Zhang, Wenlin Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic-ID-based (SID) generative recommendation (GR) represents each item as a sequence of discrete tokens and predicts the next item through autoregressive SID generation. However, existing methods face two challenges. First, insufficient shared context modeling for user sequences: full-history and recent behaviors provide overlapping yet complementary evidence, but modeling them within a single sequence may dilute current cues, whereas processing them through separate streams may fail to coordinate them. Second, insufficient personalized adaptation in progressive SID decisions: although decoder states evolve with generated prefixes, existing models typically use a shared output-side transformation across recommendation instances, without explicitly selecting a transformation suited to the current user need.
To address these challenges, we propose Multi-View Thinking with Adaptive Generation (MV-Thinker), a framework that Thinks Globally and Generates Personally. First, Multi-View Temporal Thinking uses view-specific thinking queries and readers over overlapping full-history and recent-history views, coordinating both sources into complementary user-conditioned contexts before SID generation. Second, Hierarchical Residual Adaptation organizes lightweight adapters into nested residual paths before a shared vocabulary projection, adaptively transforming context-bearing decoder states for SID decisions. Extensive experiments on four public datasets demonstrate that MV-Thinker consistently outperforms strong discriminative and generative recommendation baselines across multiple ranking metrics. The implementation code and datasets are available on: this https URL

---


### 420. [A dynamic backrest may help accommodate trunk movement, and multi-device work elicits more of it: An exploratory comparison of high-end office chairs under single- and multi-device tasks](https://arxiv.org/abs/2611.02467)

**<font color=#1a73e8>作者：</font>** Yejin Kang, Dusan Baek, Dongwoo Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dynamic-sitting office chairs are usually compared with static sitting rather than with each other, and the contribution of backrest deformability (lateral backrest movement) is unknown. Office work also increasingly spans multiple devices. Twenty healthy adults (10 men, 10 women) completed a 15-minute single-device and a 15-minute multi-device proofreading task on each of three chairs: two commercial dynamic-sitting chairs (T90, Aeron) and a T90 whose backrest lateral movement was mechanically fixed (T90-fixed). We recorded subjective ratings, head and trunk posture (inertial measurement units), upper trapezius and lateral gastrocnemius activity (electromyography), and task performance. Chair effects were largely null: T90 and Aeron did not differ in ratings or performance, posture and muscle activity showed only isolated, direction-inconsistent differences, and preferences were polarized. The standard T90 showed greater trunk movement (mean absolute angular velocity in yaw) than T90-fixed during the multi-device task (p = 0.042), which may indicate that its movable backrest helps accommodate trunk movement under demanding work; no other whole-sample posture, muscle, rating or performance measure differed between these two configurations, and replication is needed. Task effects were large and consistent: the multi-device task elicited greater and faster head, trunk and shoulder movement and higher upper trapezius activity than the single-device task, with lower reading throughput. Multi-device work thus imposes substantially greater movement demands than single-device work, which supports designing chairs that accommodate movement in modern work environments.

---


### 421. [MAGAR: Multimodal Agents for GUI-Based 3D Mechanical Assembly and Minimal Rework](https://arxiv.org/abs/2611.02472)

**<font color=#1a73e8>作者：</font>** Jingxuan Wei, Jiahao Fu, Fuqiang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A GUI command can be correct at the interface level yet still produce an incorrect assembly. An agent must identify the relevant components, respect their structural relationships, and determine which parts should move during recovery. We introduce MAGAR-Bench, a benchmark of 4,000 multimodal samples from 26 assembly families that separates Assembly Decision, Atomic Action, and Minimal Rework. For rework, the objective counts distinct moved parts within the validated recovery candidate set for each state, rather than the number of actions. We also introduce MAGAR, a selective correction framework built on a frozen policy obtained by supervised fine-tuning. Its key design matches correction granularity to output dependencies. Structured candidates revise assembly fields and rework scope, while complete action candidates keep native GUI primitives coupled with their parameters. A learned selector retains the original prediction unless a candidate passes a task-specific intervention threshold. On recorded states from held-out assembly families, MAGAR improves Overall, the task-balanced aggregate, from 37.50 to 41.39, with gains on all three tasks. Across 209 interventions, 70 correct an error and 22 introduce one. These results support task-specific correction while highlighting the remaining tradeoff between fixing errors and preserving reliable predictions.

---


### 422. [Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling](https://arxiv.org/abs/2611.02474)

**<font color=#1a73e8>作者：</font>** Lingwei Dang, Yan Zhou, Juntong Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) use video-generation priors to jointly predict future observations and robot actions. Yet RGB futures entangle physical state changes with appearance, while frame-wise depth and point maps lack temporal correspondence. Existing 4D approaches either keep motion implicit in visual features or translate predicted traces into actions through a separate interface. We present Gnomon4D, a WAM that jointly generates future video, robot actions, and GeoDelta, a video-aligned 4D geometric motion field encoding the cross-frame image-plane displacement and depth change of embodiment and object points. By placing embodiment motion and object responses in a shared space, GeoDelta exposes their motion relations to the action expert at inference. Interaction-Salient Attention (InSAttn) uses these relations to focus spatial readout on task-relevant interaction regions, while Transition-Anchored Aggregation (TransAgg) aggregates evidence around changes in their relative motion, such as grasp and release. GeoDelta describes surface motion independently of embodiment-specific controls, providing a shared human--robot quasi-action for action-free pretraining on EgoManip-5000H followed by robot mid-training on Robot-30H. Gnomon4D leads on RoboTwin~2.0, VLABench, and RoboDojo, and outperforms the strongest real-robot baseline by 7.0 and 16.0 percentage points under in-distribution and out-of-distribution settings, respectively.

---


### 423. [MetaPOCS: Meta-Learned Multi-Exit Unfolding for Budget-Aware Seismic Data Interpolation](https://arxiv.org/abs/2611.02478)

**<font color=#1a73e8>作者：</font>** Baisong Jiang, Chunxia Zhang, Xiaoli Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Seismic data interpolation must reconcile reconstruction fidelity with the computational budgets of acquisition quality control and subsequent imaging. Fixed-depth unfolding networks are optimized for a single operating point, whereas their intermediate estimates may be insufficiently trained for early deployment. We present MetaPOCS, a meta-learned multi-exit unfolding framework for budget-aware seismic interpolation. Building on a spatial--spectral POCS reconstruction backbone, MetaPOCS supervises intermediate stages and preserves the acquired traces at every exit. A Meta-GF-based optimization procedure constructs exit-oriented parameter displacements from a common initialization and learns their fusion weights through an equal-exit outer objective. The weights vary across parameter tensors and respect the nested support of the reconstruction stages. We derive the resulting fusion hypergradient to characterize how the outer objective reallocates competing updates, and distinguish this mechanism from scalar loss reweighting. At inference, one checkpoint provides a set of reconstruction budgets through a latency-calibrated exit policy. The evaluation framework couples matched-cost interpolation comparisons with finite-update diagnostics and a fixed reverse-time-migration operator, connecting multi-exit optimization to waveform and imaging fidelity. MetaPOCS thus provides a unified formulation for studying the reconstruction--computation trade-off of seismic unfolding across deployment budgets.

---


### 424. [Chain on Demand: Deferred Evidence Organization for Long-Term Conversational Memory](https://arxiv.org/abs/2611.02480)

**<font color=#1a73e8>作者：</font>** Di Lu, Zechen Li, Hao Xue  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational memory faces a timing mismatch: write-time summaries and graphs organize history before a future query is known, while independent retrieval can allocate a limited evidence budget to redundant or fragmented turns. We introduce Chain on Demand (CoD), a query-time evidence organization framework over an unchanged turn-level memory. Given a broad candidate pool, CoD constructs a temporary evidence chain by allocating a fixed anchor budget according to query relevance, lexical diversity relative to selected anchors, and newly covered query terms, followed by deterministic restoration of each selected anchor's same-session neighborhood. The resulting chain is used only for the current query, while the underlying conversational memory remains unchanged. In a paired comparison over all 1,986 LoCoMo questions, CoD achieves 82.2% accuracy on 1,540 non-adversarial questions and 76.3% on all 1,986 questions. On LongMemEval-S, one fixed configuration that indexes both user and assistant turns obtains 86.6% across all 500 questions. These results show that long-term memory can preserve the original conversation while deferring evidence organization until the information need is known.

---


### 425. [End-to-End Stability of Online Active Learning in Large-Scale Neural Systems](https://arxiv.org/abs/2611.02488)

**<font color=#1a73e8>作者：</font>** Shuiwen Shen, Jinhua Zhang, Chenlei Hou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online Active Learning (OAL) aims to extend deep learning from static inference after offline training to continuous adaptation during real-time interaction with a changing physical environment. This transition is essential for safety-critical applications, but it raises a central theoretical question: whether the online parameter update process remains stable when scaled to multilayer neural architectures. This paper develops a stability-focused OAL framework. The framework uses prediction error as a feedback signal to update a structured deep model, thereby linking online learning with Lyapunov-based energy minimization. We show that prediction error convergence alone is insufficient for global parameter convergence because multilayer networks may admit high-dimensional manifolds of equivalent output solutions. The analysis therefore separates output error regulation, internal zero dynamics, interlayer coupling, and parameter convergence. Persistency of excitation and active damping are then used to remove the residual null-space modes that remain after output error convergence. A cascaded Lyapunov analysis establishes asymptotic stability of the overall OAL learning process, while monotonic activation functions and diffeomorphic layer mappings provide the uniqueness condition for the target parameter trajectory. The resulting proof provides a theoretical basis for applying online adaptive learning to large-scale neural systems in nonstationary and safety-critical settings.

---


### 426. [Cross-Domain Joint-Embedding Pretraining For Heterogeneous Industrial Time Series](https://arxiv.org/abs/2611.02489)

**<font color=#1a73e8>作者：</font>** Jonathan Adam Rico, Nagarajan Raghavan, Senthilnath Jayavelu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial predictive maintenance and manufacturing tasks frequently contain abundant sensor measurements, but with limited labeled data. We investigate cross-domain self-supervised pretraining using joint-embedding predictive architecture for heterogeneous industrial time series (JEPA-HITS), which learns one encoder from various domains such as battery, semiconductor chemical mechanical planarization (CMP), computer numerical control (CNC) machining, and bearing while preserving dataset-specific temporal scales. We evaluate representation reuse on regression and classification problems under reduced-label downstream training, and leave-one-domain-out (LODO) pretraining. Compared with the same architecture initialized randomly, LODO pretraining reduces RMSE from 10.72 to 7.95 on battery remaining useful life (RUL), 4.34 to 3.89 on CMP, and 13.53 to 11.72 on tool wear regression, while improving bearing fault diagnosis macro-F1 from 0.547 to 0.737. Overall results suggest that unlabeled time series measurements from heterogeneous industrial processes can provide reusable representations for downstream learning with limited labeled data.

---


### 427. [How Contextual Information in Physical Environments Shapes Decisions with AI](https://arxiv.org/abs/2611.02490)

**<font color=#1a73e8>作者：</font>** Omar Elgohary, Amanda Elvarsdottir, Vannessa Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We studied whether contextual information helps people make better decisions with fallible AI in a partially visible environment. In an AR study (N = 32), participants judged whether a rendered key was present on a physical desk, with or without AI advice. We varied target prevalence and scene visibility. Focal analyses excluded visible targets and AI suggestions that could be directly checked. Within this subset, the combined context of a stronger prior toward absence (lower prevalence) and a target-free half increased AI-assisted accuracy by 9.5 percentage points. An exploratory analysis accounted for most of this increase through changes in the cases and AI suggestions being evaluated; changed participant responses did not significantly improve accuracy beyond maintaining baseline response patterns. The stronger prior reduced agreement with Present suggestions, while the target-free half lengthened decision time. We did not detect more selective agreement with correct versus incorrect advice. These findings motivate evaluating situated assistance on matched cases and designing ways to obtain evidence that can resolve claims about hidden states.

---


### 428. [Fast-Slow Evolutionary Occupancy Prediction via Controlled Dynamics](https://arxiv.org/abs/2611.02499)

**<font color=#1a73e8>作者：</font>** Runhe Yang, Zhiyuan Zhou, Yuxiang Yan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D semantic occupancy prediction provides dense geometric and semantic scene representations for autonomous driving, where both high accuracy and low response latency are crucial for safe downstream forecasting and planning. Existing methods usually exhibit different accuracy-latency characteristics. Performance-oriented models provide stronger geometric and semantic predictions, while deployment-friendly models provide faster responses. This motivates EvoOcc, a fast-slow evolutionary occupancy prediction framework that jointly exploits their complementary strengths to improve the accuracy-latency balance without changing the upstream architectures. EvoOcc models evolutionary occupancy prediction as a continuous time controlled dynamical system, enabling flexible adaptation to variable slow system delays and irregular fast system arrivals. The framework further decomposes the evolution process into dual state evolution where ego state evolution compensates for the deterministic coordinate shifts and scene state evolution models the genuine geometric and semantic scene changes. Extensive experiments on three different fast-slow system pairs and irregular prediction arrivals show that EvoOcc consistently improves over fast system baselines while maintaining much lower latency than the slow system, indicating a favorable accuracy-latency balance and stable behavior under practical inference situations.

---


### 429. [QFacePlacement: From Arbitrary Tensorization to Semantic Spatial Correspondence in Modern Face Verification](https://arxiv.org/abs/2611.02505)

**<font color=#1a73e8>作者：</font>** Krishna Bhatia, Kavita Choudhary, Pruthwik Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantum-inspired computer vision often reshapes high-dimensional features into tensors and applies tensor-network models. In face verification, this can be misleading: modern embeddings are optimized for cosine similarity, and tensorization alone does not establish the low-rank structure needed for tensor trains or matrix-product operators (MPOs). We study model placement through two controlled interfaces. First, cross-model embedding alignment requires a 512 x 512 operator to map AdaFace embeddings into ArcFace space. Dense Ridge and Procrustes mappings remain strong, while deterministic TT-SVD and MPO compression underperform even with basis changes and low-rank residuals. At a 64K-parameter storage budget, mean directional AUC is 0.9297 for dense Ridge, 0.8952 for rank-64 SVD, 0.8685 for the best low-rank-MPO hybrid, and approximately 0.649 for raw MPO. Second, before global pooling, we construct a 7 x 7 x 7 x 7 probe-gallery correspondence tensor from local AdaFace descriptors. A geometry-aware symmetric tensor train with bond dimension 2 uses 122 trainable parameters, compared with 2,403 for a dense linear matcher, while attaining an LFW AUC of 0.9802. Yet compression does not translate into better low-false-acceptance performance: on CFP-FP, TAR at FAR = 0.001 is 0.0102 versus 0.1734 for global cosine matching, and on CPLFW it is 0.7805 versus 0.8737. These results suggest that quantum-inspired factorization is most credible when the chosen interface provides task-aligned axes and compressible structure. They also show why aggregate AUC must be assessed alongside operational low-FAR metrics.

---


### 430. [CellPlex: Benchmarking Single-Cell Spatial Proteomics Prediction from H&E](https://arxiv.org/abs/2611.02506)

**<font color=#1a73e8>作者：</font>** Zijun Gao, Yijiang Chen, Xiangde Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial proteomics measures tens of proteins in every cell of a tissue section, but its cost confines it to small research cohorts, whereas hematoxylin and eosin (H\&E) slides exist for nearly every patient. Inferring single-cell spatial proteomics from H\&E would bring its analyses to routine pathology, and a growing number of virtual staining models pursue this goal. Each is evaluated on its own cohort, panel and pixel-level metric, and released models transfer poorly to new cohorts, leaving open which approach to build on and which proteins H\&E can reveal. We introduce CellPlex, a benchmark that poses the task at the level of the cell: seven cohorts with same-section H\&E and multiplexed immunofluorescence, from colorectal and breast cancer to lymph-node metastases, bone marrow and glioma, with 717 samples, 44.8 million cells and 149 proteins, processed by one pipeline into per-cell targets. Pathology foundation models (PFMs) are adapted with one cell-level protocol, specialist models are fine-tuned under a matched budget, and all are scored on the same cells. Adapted PFMs are the most accurate models on every cohort, ahead of the specialists even after fine-tuning, but keep less than half of their accuracy on cohorts they were not trained on. Which proteins can be predicted depends on the tissue, not on how many cells were measured for them. By fixing the cells, targets and splits on which predictions are judged, CellPlex sets a common standard for inferring costly molecular measurements from routine H\&E and shows how far H\&E can stand in for spatial proteomics. We will release the data, splits, evaluation code and baselines as a testbed for developing and comparing future pathology foundation models and virtual staining methods.

---


### 431. [Latent Spectral Prompting for Multimodal Hyperspectral Object Tracking](https://arxiv.org/abs/2611.02512)

**<font color=#1a73e8>作者：</font>** Wangshu Cai, Jun Zhou, Lei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral videos provide rich spectral signatures for robust tracking under challenging conditions such as camouflage and low illumination. However, limited hyperspectral annotations and the large RGB-hyperspectral domain gap hinder the direct use of modern temporally pretrained RGB trackers. We propose SProTrack, a multimodal framework that transfers temporal knowledge from pretrained RGB trackers to the hyperspectral domain through latent spectral prompting. The key idea is to decouple temporal modeling from spectral adaptation, allowing temporal dynamics to be inherited from RGB foundation models while hyperspectral information is learned from unlabeled data in a self-supervised manner. Unlike band-selection methods that discard most spectral information or prompt-based approaches that rely on local-search crops, SProTrack learns a global, scene-level spectral representation from the full hyperspectral frame using an autoencoder. This latent representation is used to guide spectral prompt extraction while a pretrained RGB tracker preserves strong temporal modeling on RGB-compatible inputs. By encoding spectral-spatial structure into compact latent prompts, SProTrack bridges the RGB-hyperspectral modality gap without extensive retraining or dense supervision. Experiments on HOT2020 and HOT2023 demonstrate that SProTrack achieves the best overall performance, with strong results across all spectral domains.

---


### 432. [Touching Projected Agents through the DAT Screen -System Design and Questions of Interaction Boundaries-](https://arxiv.org/abs/2611.02525)

**<font color=#1a73e8>作者：</font>** Takaya Tamamoto, Tomoko Yonezawa  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Touching a virtual agent involves more than detecting a finger on a display: the contact surface can deform and resist the user's push, and the agent can respond to that action. We describe the Desktop Amid Touch (DAT) screen, which combines spatial projection onto a semi-transparent, deformable mesh with touch sensing and motorized control of resistance to indentation. An initial prototype detected a single touch and estimated its position and depth from tension changes around a flexible projection screen. A subsequent prototype added motorized tension control to vary the screen's resistance to indentation. We describe the tension-controlled DAT implementation and its demonstrations, distinguishing what has been observed from what remains an open design question. These capabilities raise a design question: should touchable virtual agents respond as though they had preferences or boundaries, and under what conditions should such behavior be implemented on systems like DAT. The present paper describes a system and frames this question; it does not establish how users interpret an agent's refusal or consent.

---


### 433. [INTERACT: Learning Interaction-Aware World Dynamics from Driving Videos for Autonomous Driving](https://arxiv.org/abs/2611.02526)

**<font color=#1a73e8>作者：</font>** Zhan Chen, Songyan Zhang, Wenhui Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safe autonomous driving requires more than recognizing the current scene: the ego vehicle must anticipate how surrounding traffic participants will evolve under its own motion. However, existing end-to-end driving models typically encode scenes into dense visual or BEV features, leaving object-level interactions implicit. We propose (INTERACT INTERaction-aware Action-Conditioned Trajectory learning), a three-stage framework that learns a slot-based object-centric world model from unlabeled driving videos and transfers it to trajectory planning. INTERACT first learns recurrent slots that group dense visual features into temporally structured scene-entity representations without object annotations. It then infers latent ego actions from slot context and video transitions, and uses them to condition future slot prediction, capturing how ego motion and surrounding entities co-evolve. Finally, the learned slots, latent actions, and future slot predictions are distilled into a trajectory planner to guide trajectory generation and selection. Extensive experiments on NAVSIM and nuScenes validate the effectiveness of INTERACT. In particular, it achieves state-of-the-art performance on NAVSIM, with improvements in safety-critical collision metrics.

---


### 434. [Scientific Liquidity Agents: An Agent-Based Model of Knowledge Arbitrage in Scientific Communities](https://arxiv.org/abs/2611.02539)

**<font color=#1a73e8>作者：</font>** Koutian Wu, You Liu, Yue Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Scientific knowledge gains new uses when ideas, methods, and results move between research contexts. Understanding this process requires a model of both specialized knowledge production and the intermediary activities that connect it. We introduce Scientific Liquidity Agents (SLA), an agent-based model of knowledge arbitrage in scientific communities. SLA represents domain specialists and epistemic arbitrageurs within a shared environment of research problems, researcher interactions, and scientific artifacts. Individual decisions connect to collective state through a belief-desire-intention architecture, a prerequisite-based problem graph, a dynamic interaction network, and a persistent publication registry. The framework makes researcher roles and knowledge-transfer frictions explicit, providing a process-oriented account of scientific production and exchange. Two exploratory simulations with 10 and 18 agents produce 68 and 274 registered papers. In the smaller run, arbitrageurs take part in 16 of the 26 contact pairs that join this community into one connected component, while topical similarity alone splits it into seven. The same run yields three similarity edges, 26 contact pairs, and two coauthorship pairs, so measured community structure depends on what counts as a link. Paper production is abundant, but no recorded replication succeeds, which places the bottleneck in verification rather than production. Solved-problem sets correspond to the prerequisite reachability of the disciplines represented in each community. SLA makes knowledge liquidity, the movement and reuse of artifacts across domains, a quantity that agentic science can simulate and measure.

---


### 435. [FindLink: Learning to Assess Scientific Connections from Source-Grounded Premises](https://arxiv.org/abs/2611.02545)

**<font color=#1a73e8>作者：</font>** Jingxuan Wei, Song Tan, Xiaohan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery from the literature requires assessing connections among findings obtained under different study conditions. Source attribution makes individual findings traceable, but does not determine what they jointly support. We introduce GI-TraceBench, a benchmark of 10,282 questions in gastrointestinal oncology that unifies provenance question answering, knowledge discovery, and hypothesis evaluation through shared Paper, Claim, and Evidence Span records. We further propose FindLink, a two-stage framework for provenance-grounded scientific reasoning. Premise Grounding constructs source-bound premises with explicit study context and support status. Structured Reasoning organizes these premises into support plans that represent both supported relations and unresolved conditions, then generates evidence-conditioned answers using deterministic compiler feedback. The compiler verifies structural and source-binding consistency, but does not assess scientific entailment. On the 1,545-question fixed-evidence test set, FindLink improves the balanced family macro score from 67.95 to 87.25 over direct supervised fine-tuning of the same backbone. A retrained variant without Structured Reasoning achieves slightly higher premise-identifier F1, but substantially lower relation and evidence-sufficiency F1. These results indicate that scientific reasoning requires not only identifying grounded premises, but also assessing what connections those premises support.

---


### 436. [Re$^3$Rank: Listwise Reranking with Reasoning-Conditioned Retrieval Heads](https://arxiv.org/abs/2611.02550)

**<font color=#1a73e8>作者：</font>** Ruiyi Yan, Zhuoyuan Mao, Yugo Murawaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attention-based rerankers score each candidate by the attention mass that retrieval heads route to it from the question, but the question, serving as a fixed query, carries limited information for locating relevant evidence. We propose Re$^3$Rank, a listwise reranker built on reasoning-conditioned retrieval heads (RRHeads). A generator first writes a reasoning trace over the question and the candidates, and a scorer then uses the trace tokens as the attention query of a few selected RRHeads, reading relevance as continuous scores. We present a straight-through estimator to propagate the ranking loss through the discrete trace, so that the generator and the scorer can be trained jointly for ranking. Averaged over 9 benchmarks, Re$^3$Rank outperforms 11 baseline rerankers: our 4B variant exceeds the strongest baseline by 3.11 NDCG@10 points on average, and even our 0.6B variant surpasses rerankers with up to 32B parameters.

---


### 437. [Flat Features, Detailed Images? Simple Detail Control for Diffusion Transformers](https://arxiv.org/abs/2611.02551)

**<font color=#1a73e8>作者：</font>** Qingtao Yu, Zhen Wang, Jiyang Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt engineering is commonly used to encourage text-to-image models to generate more detailed images. However, it does not provide reliable, continuous, or disentangled control. We analyze feature tokens produced with and without detail-enhancing prompts across six diffusion transformers and observe a common pattern: these prompts tend to increase the entropy of each token's energy distribution while largely preserving its ordering. That is, flattening the distribution increases the level of detail. Motivated by this counter-intuitive finding, we introduce a simple training-free approach that continuously adjusts the level of detail according to a scalar. Specifically, it shifts the squared channel magnitudes of each token toward a higher entropy distribution with a time-aware scheduler to concentrate the intervention at intermediate sampling steps. Across extensive experiments on different types of diffusion transformers, we show that our approach provides continuous control over detail metrics while largely preserving image quality and semantic structure. It requires only a few lines of code and adds negligible inference time overhead.

---


### 438. [EEFA: A Framework for the Ethical Evaluation of AI Agents](https://arxiv.org/abs/2611.02561)

**<font color=#1a73e8>作者：</font>** Swathi Pallikala, Yashas Hariprasad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of autonomous AI agents across consequential domains including healthcare, legal services, nancial management, and enterprise workows has created an urgent governance challenge. While the eld of AI evaluation has produced sophisticated benchmarks for measuring agent capability, these frameworks measure exclusively what agents can do rather than how they do it. The ethical dimensions most critical to responsible agent deployment, in- cluding respect for human autonomy, harm avoidance, transparency and non-deception, privacy compliance, and accountability, are systematically absent from current evaluation practice. This paper addresses that gap through three contributions. First, a structured literature review of twelve leading AI agent benchmarks characterizes the ethical dimensions those bench- marks do and do not measure. Second, the Ethical Evaluation Framework for AI Agents (EEFA) is introduced as a comprehensive, operationalizable instrument for ethical agent evaluation, grounded in established AI ethics principles and designed for use by developers, auditors, and regulators. Third, a reproducible validation protocol is specied for applying the EEFA to deployed agent systems, with illustrative test scenarios across all ve framework dimensions. The EEFA is organized across ve primary dimensions: Autonomy Preservation, Harm Avoid- ance, Transparency and Non-Deception, Privacy Compliance, and Accountability and Traceabil- ity. The framework maps directly onto the requirements of the EU AI Act and the NIST AI Risk Management Framework, positioning it as a practical compliance assessment instrument for high-risk AI applications. Empirical application of the framework across diverse benchmarks and agent systems is identied as a priority direction for future work.

---


### 439. [SeMo3D: Unifying 3D Generation, Editing, and Completion via Selective Modeling](https://arxiv.org/abs/2611.02568)

**<font color=#1a73e8>作者：</font>** Xiaokun Sun, Jian Yang, Zhenyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D generation, editing, and completion are typically treated as regenerating the complete 3D asset under task-specific constraints, even when only a local region needs modification. This leads to task isolation, inconsistency in content that should remain unchanged, and dependence on task-specific paired data. We address these issues with a key observation: the three tasks all synthesize a designated region while keeping the rest intact---the full region for generation, the target region for editing, and the missing region for completion. We term this paradigm Selective Modeling and build SeMo3D upon it; it naturally unifies the three tasks, preserves unchanged content by construction, and enables training without paired editing or completion data, since any 3D asset can be partitioned into a selected region and its context. For training, we propose region-selective denoising, which randomly selects regions of varying sizes on standard 3D assets and applies noise and loss only to them, jointly learning all three tasks. For architecture, we propose Omni3DiT, a multi-condition 3D diffusion transformer that distinguishes regions to create from those to retain and fuses image, text, and point guidance for fine-grained control. Experiments across three benchmarks show SeMo3D surpasses state-of-the-art methods on all tasks, delivering multimodal controllability in generation and strong consistency and accuracy in editing and completion. SeMo3D further serves as a unified modeling tool for agents, enabling efficient 3D creation through natural-language interaction. Project page: this https URL.

---


### 440. [Beyond $L_\infty$-Norm Sets: Synthesizing Interpretable Non-Uniform Uncertainty Sets for Evaluation-Time State-Adversarial Robustness](https://arxiv.org/abs/2611.02576)

**<font color=#1a73e8>作者：</font>** Xulin Chen, Ruipeng Liu, Garrett E. Katz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) agents are vulnerable to perturbations of their observed state inputs. Prior works often constrain state adversaries with $L_p$-norm uncertainty sets and evaluate policy performance under the resulting perturbations. However, in continuous control tasks like robotics control, different state dimensions have distinct physical meanings and influence policy behavior to different degrees, which $L_p$-norm sets fail to capture or explain. Moreover, it is important to identify when and along which state dimensions a policy is vulnerable, independently of the algorithm used to train it. In this paper, we focus on evaluation-time attacks applied to pretrained policies. We propose \textbf{P}erformance-\textbf{D}egradation \textbf{N}on-\textbf{U}niform \textbf{U}ncertainty \textbf{S}et (\method{}), an interpretable formulation of uncertainty sets for state perturbations. \method{} is state-dependent, dimension-wise non-uniform, and can be synthesized online during policy evaluation. We first formulate an ideal constrained optimization problem for \method{} computation, then introduce a surrogate constraint to make the problem tractable. Experiments across multiple continuous-control environments, policy algorithms, and state attacks show that \method{} reveals variation in policy sensitivity across states and dimensions, while its performance degradation is moderately controlled.

---


### 441. [Probing Local Conditional Fit for Diffusion Model Membership Inference](https://arxiv.org/abs/2611.02578)

**<font color=#1a73e8>作者：</font>** ByungHee Cha, Naoki Murata, Yuhta Takida 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Membership inference determines whether a candidate example was used to train a text-to-image diffusion model and is an important tool for auditing training-data use. We identify a directional membership signal in \emph{conditional prediction shifts}, the changes in predicted noise under alternative text conditions at a fixed noisy input: whether movement toward the alternative prediction initially lowers or raises the denoising loss from its value under the original caption. Members exhibit less room for such local improvement. To quantify this response, we propose \emph{LoFIT} (Local Conditional Fit), which measures the initial response of the denoising loss along normalized prediction shifts and aggregates it across multiple text conditions and diffusion states. LoFIT requires no target-model gradients and can be computed using only forward queries to the denoiser. Evaluations on four datasets show improved membership discrimination across fine-tuned and pretrained models. LoFIT distinguishes members early in fine-tuning, while the naive denoising-loss baseline remains near chance. Controlled comparisons show that the membership signal is concentrated in the first-order response, with little discrimination from prediction-shift magnitude alone.

---


### 442. [AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding](https://arxiv.org/abs/2611.02593)

**<font color=#1a73e8>作者：</font>** Shiqi Shen, Shurui Li, Xilin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual mental imagery (VMI) decoding uses brain activity to reconstruct internally generated visual scenes, providing a potential pathway for externalizing internal experiences and developing neuroprosthetic communication interfaces. However, progress is limited by the lack of dedicated, training-scale VMI datasets. Current VMI paradigms often rely on visual prompts or short-term memory images, introducing visual and mnemonic confounds that make it difficult to disentangle neural activity associated with endogenous image construction from signals driven by prior or concurrent visual input. Furthermore, existing VMI datasets offer limited descriptive control over individual visual attributes, making it difficult to systematically assess fine grained visual details. To address these gaps, we introduce AVID, the first dedicated training-scale 5.0 Tesla functional magnetic resonance imaging (fMRI) resource for auditory-induced VMI decoding. AVID comprises approximately 67 hours of dense recordings from nine participants. The dataset is structured into two complementary splits: a scene-level complex split using naturalistic Mandarin descriptions and a controlled simple split with explicitly specified visual attributes. We further formalize a standardized evaluation protocol that decouples source-image consistency from semantic alignment, allowing for a more nuanced assessment of imagery reconstruction. Baseline qualitative and quantitative results show that current reconstruction pipelines remain limited on AVID, although the most successful reconstructions preserve recognizable scene level semantics from spoken descriptions. By combining dedicated training-scale neural recordings and standardized evaluation resources, AVID provides both a data foundation for imagery-specific model development and a benchmark for evaluating VMI decoding with substantially reduced sensory contamination.

---


### 443. [Camera-Free Object Discovery and Interaction with GazeTags](https://arxiv.org/abs/2611.02599)

**<font color=#1a73e8>作者：</font>** Vimal Mollyn, Chris Harrison  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present GazeTags, a camera- and computer-vision-free approach for worn head-gaze object awareness. Our small electronic tags cost roughly \$2 each and can operate for more than a year on a coin cell battery. They work in concert with a user-worn device (smartglasses, hearables, etc.) that periodically emits a focused infrared signal aligned with the user's head direction. Only GazeTags within that narrow head-oriented beam wake and respond, providing their identity and optional payloads such as object state or live sensor readings. By avoiding cameras and computer vision pipelines, our approach is very energy efficient, able to operate continuously even in battery-constrained wearables, and sidesteps non-trivial privacy issues. We describe our hardware design, characterize our system performance and operating tradeoffs, and demonstrate how GazeTags can enable practical gaze-aware environments.

---


### 444. [BGD-SF PolySegNet: boundary-guided dynamic selective fusion network for robust polyp segmentation in colonoscopy images](https://arxiv.org/abs/2611.02603)

**<font color=#1a73e8>作者：</font>** Nishi Kanta Paul, Shamia Maherin, Morsheda Akter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective polyp segmentation in colonoscopy images is crucial for early detection of colorectal cancer, a leading cause of cancer-related death worldwide. While current deep learning models perform well on traditional Dice benchmarks, border segmentation remains difficult. Most methods use boundary information only as an additional loss signal during training, which prevents the network from explicitly learning border-guided feature selection or mask refinement. This paper introduces BGD-SF PolySegNet, a boundary-guided encoder-decoder architecture that controls three phases of the segmentation pipeline: dynamic multi-scale context aggregation, selective skip-feature fusion, and final mask refinement. The architecture comprises a pretrained EfficientNet-B4 backbone and three proposed modules: Boundary-Guided Dynamic Cascaded Multi-Scale Context Aggregation (BGD-CMSCA), Boundary-Guided Selective Attention Fusion (BG-SAGF), and a Multi-Level Boundary Guidance Head (MBGH). The model is trained on 3,535 annotated images from Kvasir-SEG, BKAI-IGH NeoPolyp-Small, and PolypGen, and evaluated on four held-out benchmark datasets. On the internal test set, BGD-SF achieves a Dice of 0.887, IoU of 0.839, mask-derived Boundary F1 of 0.531, HD95 of 30.32, and ASSD of 18.10, improving Boundary F1, HD95, and ASSD by 15.7%, 27.5%, and 34.6% over the strongest CNN baselines. External validation on CVC-ClinicDB, CVC-ColonDB, ETIS-Larib, and CVC-300 yielded Dice scores of 0.891, 0.776, 0.863, and 0.885, respectively. The model runs at 35 FPS with 22.51M parameters. Wilcoxon signed-rank tests confirm statistically significant mask-derived Boundary F1 improvements over six of seven ablation variants (p < 0.001; small-to-moderate effect sizes, r = 0.215-0.434), demonstrating that integrating boundary guidance as an active architectural component measurably advances polyp boundary delineation.

---


### 445. [Ask More, Hear Less: How a Review Prompt Changes What Online Ratings Show](https://arxiv.org/abs/2611.02623)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Lei Nico Zheng, Di Zhu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Platforms ask customers for online reviews to reduce self-selection, but theory conflicts on whether review solicitation makes online ratings more or less informative. Selection theory implies that asking helps, voice theory that it dilutes the news, and research on rating inflation that compression destroys information. We reconcile these views with signal detection theory, which separates what a rating knows (its sensitivity) from what it shows (its criterion). We test the framework on Steam, a leading PC video game store, whose client began in October 2019 to prompt players for a review after about three hours of play. Using a difference-in-discontinuities design at that inferred threshold in 21.6 million Steam reviews of 315 games, we find that review counts just above the threshold become 4.25 times those just below, and the jump in the positive share grows by 6.6 percentage points. Agreement with critics changes little near launch and erodes later. The rating's movement changes far more: pass-through from reviews written in the first two hours falls from 0.73 to 0.18 just above the threshold, against 0.81 to 0.64 just below, and a fixed rating tier responds to 12% of downturns in those reviews above the threshold, down from 42%, against 41% and 47% below it. What the stream knows changes less. At equal review counts its sensitivity falls more above the threshold, because added reviews respond about half as much and scores near the ceiling are noisier per review, but at natural counts added volume offsets this loss, leaving a change of -0.03 relative to the stream below (95% CI -0.13 to 0.06). Failures that developers acknowledge, which run through complaints, still move the score after launch. Review prompts therefore mainly change how a rating must be read, and platforms that solicit reviews should recalibrate their rating labels.

---


### 446. [Latent Diffusion-GAN: Adversarial Learning in the Autoencoded Latent Space](https://arxiv.org/abs/2611.02625)

**<font color=#1a73e8>作者：</font>** U-Chae Jun, Jaeeun Ko, Jiwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are powerful generative frameworks for producing high-quality images by denoising latent variables from random noise. However, training with likelihood-based objectives, such as denoising score matching, can lead to locally over-smoothed high-frequency details, including fine textures and sharp edges, thereby limiting perceptual fidelity and structural detail. Adversarial training with GANs enhances sharpness but typically requires additional discriminator networks, increasing computational costs and destabilizing training. To this end, we propose Latent Diffusion Generative Adversarial Networks (LD-GAN), a novel framework that seamlessly integrates adversarial learning into diffusion models without modifying their original pipeline. LD-GAN leverages the pretrained variational autoencoder (VAE) in latent diffusion models as an energy-based discriminator, enabling adversarial training without extra parameters and preserving the structured latent priors learned from large datasets. We also introduce a structural consistency energy that aligns encoder and decoder feature representations, thereby enhancing perceptual quality and compatibility with the pretrained latent space. Extensive experiments demonstrate that LD-GAN significantly improves sample fidelity, perceptual sharpness, and diversity over state-of-the-art baseline methods across various generation tasks while ensuring efficient training dynamics.

---


### 447. [ICJ-Graph: A Citation Graph and a Layered Document Corpus of the International Court of Justice](https://arxiv.org/abs/2611.02630)

**<font color=#1a73e8>作者：</font>** Jirameth Wannasiwaporn, Pawitsapak Akarajaradwong, Chompakorn Chaksangchaichot  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ICJ-Graph, a machine-readable resource connecting documents of the International Court of Justice (ICJ) to cited cases, legal provisions and United Nations resolutions. Court decisions, written pleadings and oral records form distinct document layers, preserving the distinction between the Court's reasoning and the parties' submissions. The collection contains 6,396 ICJ documents and 505 documents from other courts and legal bodies, together with 12,375 provisions and 20,291 UN resolutions. The data files contain text, metadata and embeddings. The accompanying pipeline lets users load the graph and generate embeddings for use in their own retrieval systems. To illustrate the resource's use, we evaluate five models on citation prediction for 199 decisions using documents available before each decision. Tools designed for citation research improve citation-prediction F1 over answering without tools for all five models across case, provision and resolution citations.

---


### 448. [UniCross3D: Unified Cross-View and Cross-Domain Diffusion for Consistent Single-Image 3D Generation](https://arxiv.org/abs/2611.02631)

**<font color=#1a73e8>作者：</font>** U-Chae Jun, Jaeeun Ko, Jiwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing detailed geometry and realistic appearance from a single RGB image is essential yet fundamentally challenging due to inherent ambiguities such as occlusion, lighting variations, and texture-geometry entanglement. While recent diffusion-based generative models have significantly improved novel view synthesis, existing approaches suffer from two critical limitations: lack of cross-view geometric consistency and insufficient cross-domain semantic alignment. To address these issues, we introduce UniCross3D, a unified cross-view and cross-domain diffusion framework designed explicitly for consistent and physically coherent 3D generation. UniCross3D features two novel contributions: (1) a cross-view latent regularization that enforces cross-view geometric consistency across synthesized viewpoints by penalizing latent variance, and (2) a cross-domain mutual information objective grounded in the physics of image formation, explicitly aligning synthesized color and normal maps. Extensive experiments demonstrate that UniCross3D achieves significantly improved view consistency and semantic alignment over state-of-the-art methods and yields higher-fidelity reconstructions, particularly under challenging textures and ambiguous viewpoints.

---


### 449. [Susceptibilities for Neural Networks Learning from Physical Data](https://arxiv.org/abs/2611.02632)

**<font color=#1a73e8>作者：</font>** Rohan Hitchcock, Gary W. Delaney, Jonathan H. Manton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks that are trained on data arising from a physical system must somehow learn regularities induced by the underlying physical laws. In this setting, concepts from statistical physics provide powerful tools for analysing how physical laws influence the learning process. In this paper we explain how susceptibilities --- which measure the response of a neural network to perturbations of a parameter of the data distribution --- can be applied when learning from physical data. We show that such susceptibilities can identify the conditions under which specific input features are most informative for learning, guiding data selection, a prediction we validate experimentally. For distributions lacking a natural parameter, we propose introducing one via a physically meaningful scalar function of the physical state, and demonstrate that susceptibilities track the emergence of specific capabilities (such as collision detection) during training.

---


### 450. [Measuring AI Agents as Teammates with Collaborative Intelligence](https://arxiv.org/abs/2611.02633)

**<font color=#1a73e8>作者：</font>** Sean Wu, Aneesh Pappu, Jiaru Zou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress in AI is often measured by what a single model can do on its own. Yet teams of AI agents are starting to make breakthroughs and discoveries in science, medicine, mathematics and software engineering. As AI begins to work in teams of agents and people, the ability to collaborate becomes a core part of their intelligence. Research on human teams has measured this ability for decades. Inspired by this, we introduce the Collaborative Intelligence Benchmark, which measures how well an AI agent works as a teammate. It contains 240 tasks across 8 dimensions of teamwork, from refusing an unsafe shortcut to checking the work that a weaker model leaves behind. Each task comes from a real record or an existing benchmark, from aviation accident reports and clinical cases to coding tasks and negotiations, and has a programmatically verifiable outcome. To isolate teamwork from individual capability, models are scored only on tasks that they can solve by themselves when they have full information. We evaluate 18 closed- and open-weight models and find that every model, across sizes and families, has clear weaknesses as a teammate, with the best model scoring only 82.2 out of 100. Frontier models almost always refuse unsafe shortcuts and report misconduct, yet they cave under interpersonal pressure, reaching the best overall deal in only 14% of conflicts, and their pass rate drops from 97% to 81% when they take over a task in which a weaker model has cheated. Crucially, general capability does not guarantee good teamwork, as models with nearly the same capability score differ by up to 11 points as teammates. The benchmark includes 160 public tasks with code and data, along with 80 held-out tasks for evaluation. As AI agents increasingly work alongside other agents and people, the ability to collaborate effectively is becoming a crucial capability to measure and develop.

---


> [!TIP]
> 当前位于：**401-450**（第 9/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
