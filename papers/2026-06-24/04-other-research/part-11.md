# 📦 其他研究 | 2026年06月24日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 501. [CITADEL: CSI-Based Jamming Detection and Open-Set Classification for IIoT Networks](https://arxiv.org/abs/2606.22939)

**<font color=#1a73e8>作者：</font>** Aymen Bouferroum, Ildi Alla, Valeria Loscri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Radio frequency jamming poses a critical threat to the availability of wireless Industrial Internet of Things (IIoT) networks. Existing detection and classification techniques are poorly suited to this setting: coarse signal-strength and cross-layer features lack information richness, while raw I/Q baseband approaches require hardware and throughput that is impractical at the scale of hundred-node IIoT deployments. This paper presents CITADEL, a lightweight two-stage hierarchical pipeline that uses only Channel State Information (CSI) measurements, which are natively available on commodity IIoT devices, to detect and classify jamming attacks including previously unseen ones. While prior work has shown that jamming leaves observable CSI signatures, CITADEL is the first system to translate this insight into an end-to-end pipeline that jointly achieves closed-set classification of known attacks, open-set detection of zero-day attacks, and resistance to adversarial evasion. Evaluated across 6 known attack types and 15 zero-day scenarios, CITADEL achieves 100% known-attack detection and 97.1% zero-day detection at a 0.4% end-to-end false positive rate. Under adversarial evaluation spanning white-box and black-box threat models, gradient-based evasion remains below 2% across all tested perturbation budgets and the strongest published CSI attack generator achieves less than 5% average evasion. A systematic comparison against eight baselines confirms that no existing method achieves comparable performance on CSI data across all three axes: detection, generalization, and robustness. The full pipeline completes inference in 14.2 ms at 95.9 mJ on an edge GPU, establishing CITADEL as a practical solution for large-scale IIoT network security.

---


### 502. [Evaluating self-supervised echocardiographic representations across downstream extraction strategies for left-ventricular segmentation and ejection fraction estimation](https://arxiv.org/abs/2606.22943)

**<font color=#1a73e8>作者：</font>** Sylwia Majchrowska, Philip Teare  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) is increasingly used in medical imaging to reduce annotation requirements, but representation quality is often judged using a single downstream evaluation setting. For dense clinical tasks, this can confound representation quality with the capacity of the downstream model used to recover task-relevant information. We present a systematic evaluation of self-supervised representations for left-ventricular segmentation and ejection fraction (EF) estimation from apical four-chamber echocardiography on EchoNet-Dynamic. Rather than relying on a single downstream probe, we compare a hierarchy of extraction strategies with increasing expressivity: heuristic extraction without mask-supervised training, frozen linear probes, frozen lightweight decoder probes, and partial fine-tuning. We apply this framework to two complementary representation families: generic frozen self-DIstillation with NO labels (DINOv3) features and a task-adapted dense self-supervised representation, Bootstrap Your Own Segmentation (BYOS). In both families, heuristic extraction substantially understated what was recoverable from the frozen representation. For DINOv3, performance improved from Dice 0.684 and EF mean absolute error (MAE) 13.01 under heuristic extraction to Dice 0.906 and EF MAE 9.65 with a frozen lightweight decoder, approaching a supervised U-Net baseline (Dice 0.915, EF MAE 9.72). For BYOS, performance improved from Dice 0.687 and EF MAE 17.83 under heuristic extraction to Dice 0.902 and EF MAE 8.74 with a frozen lightweight decoder. These results show that conclusions about self-supervised representation quality in dense echocardiographic analysis depend strongly on the downstream extraction strategy used for evaluation. We therefore argue that multi-strategy evaluation is an important methodological consideration for SSL in dense medical image analysis.

---


### 503. [Neural Operator Processes for Probabilistic Operator Learning under Partial Observations](https://arxiv.org/abs/2606.22946)

**<font color=#1a73e8>作者：</font>** Jose Miguel Lara-Rangel, Serge Guillas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators learn mappings between function spaces, but are typically developed with dense input-output training fields and fully observed inputs at inference. Many scientific problems require instead predicting solution fields from sparse, irregular, or partial observations under uncertainty. We introduce Neural Operator Processes (NOPs), a framework that unifies neural-process conditioning with neural-operator decoding to predict full output fields from limited context. NOPs condition on sparse joint input-output observations and support deterministic and probabilistic prediction within a shared encoder-decoder architecture. We study two conditioning strategies, convolutional pooled summaries and query-aligned attention, and analyze how their interaction with latent stochastic variables depends on PDE geometry. Across function regression and three PDE benchmarks, we find that sparse conditional operator learning is viable and can match dense-grid behavior in several regimes, that preserving local context-query geometry is essential in non-periodic settings but less so in spectrally smooth periodic regimes, and that uncertainty-aware operator learning succeeds when latent conditioning complements rather than overwrites the local geometric pathway. These results provide a basis for probabilistic operator learning under partial observations and help bridge operator learning and probabilistic meta-learning in function space.

---


### 504. [ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents](https://arxiv.org/abs/2606.22948)

**<font color=#1a73e8>作者：</font>** Yincheng Zhou, Athena Zhuoming Zhong, Shijie Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As multimodal agents move from interface understanding to real software control, successful trajectory discovery in live desktop environments becomes a key challenge. GUI tasks require long-horizon sequences of precise mouse and keyboard actions, while feedback is sparse, delayed, and costly to obtain through VM rollouts. We propose Environment-Native Verified Search (ENVS), a training-time search-and-filter pipeline that uses the environment to construct verified supervision before policy optimization: it branches over behaviorally distinct GUI actions in live OSWorld VMs, verifies successful leaves, and trains from globally balanced step-level supervision. To evaluate robustness under realistic desktop interruptions, we also introduce OSWorld-Noisy, a dynamic benchmark for recoverable desktop interruptions that preserves the original tasks while testing whether agents can refocus, dismiss, wait, or recover under live perturbations. On the 300-task OSWorld pool, ENVS reaches 30.3 pass@8 on original evaluations and 29.0 on OSWorld-Noisy, outperforming matched ARPO-style online RL while reducing compute from 184-192 to 138-153 GPU-hours; even with only 30% of its search data, ENVS reaches 27.0 pass@8, exceeding ARPO from the base model. Training from noisy environments also better preserves visual-reasoning abilities on auxiliary benchmarks, including OSWorld-G Refusal (16.7 vs. 1.9) and BLINK Functional Correspondence (26.2 vs. 23.1).

---


### 505. [DT-GOL: Dual-Track Geometric Online Learning in Nonstationary Environment with Label Delay](https://arxiv.org/abs/2606.22950)

**<font color=#1a73e8>作者：</font>** Yulin Wang, Yi He, Dianlong You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online learning is crucial for handling complex data streams in big data applications. Recent research has begun to focus on dynamic scenarios, i.e., non-stationary environments. However, a crucial yet often overlooked aspect is label latency, where new data may not receive labels in time due to the slow and expensive labeling process, thus hindering rapid adaptation to dynamic environments.
To resolve this impasse, we propose Dual-Track Geometry Online Learning (DT-GOL), a novel framework that shifts from temporal compensation to spatial reasoning to bridge the supervised latency gap. By modeling the delay challenge as a semi-supervised task, we leverage real-time topological evolution of features as a reliable geometric surrogate for unobservable conceptual changes to achieve proactive supervised adaptation within the delay window. Unlike rigid self-training, we introduce a dynamic evidence calibration mechanism that distills geometric information into soft labels that perceive uncertainty, effectively mitigating the confirmation bias inherent in hard pseudo-labels. Furthermore, to resolve the stability-plasticity dilemma, we design a decoupled dual-track architecture in which a master learner serves as a stable anchor, updated strictly from delayed ground truth, while a transient branch leverages soft geometric knowledge for low-risk forward adaptation. Extensive experiments on real and synthetic datasets demonstrate that DT-GOL significantly outperforms existing state-of-the-art baseline methods, especially in scenarios with concept drift.

---


### 506. [The Impact of VAE Design on Latent Pose Representations for Diffusion-based Sign Language Production](https://arxiv.org/abs/2606.22959)

**<font color=#1a73e8>作者：</font>** Guilhem Fauré, Mostafa Sadeghi, Sam Bigeard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent diffusion approaches to sign language production (SLP) rely on an initial stage that learns an encoding of sign pose sequences, enabling generative modeling in the resulting latent space. The autoencoder used in this stage is typically evaluated in terms of reconstruction quality using geometric metrics common in SLP. While informative, these metrics do not fully capture latent space properties that may influence the training and performance of the downstream generative model. In this work, we investigate how architectural and training objective design choices in a variational autoencoder (VAE) for sign pose encoding affect latent space structure, and how these differences translate into the performance of a latent diffusion model for text-to-sign generation. Our experiments on Phoenix14T dataset show that variations in generative performance, measured through back-translation BLEU scores, can sometimes be better explained by differences in latent space properties than by VAE reconstruction accuracy alone.

---


### 507. [Topological Out-of-Domain Generalization in Dynamical Systems Reconstruction](https://arxiv.org/abs/2606.22969)

**<font color=#1a73e8>作者：</font>** Georg Trede, Charlotte Ricarda Doll, Elias Weber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the behavior of dynamical systems (DS) beyond the dynamical and parameter regimes observed in training is a pivotal and essentially unresolved problem in scientific ML. It is central to any good scientific theory, which we expect to be able to make predictions about regimes not covered by currently available data. Recent hierarchical and hyper-network guided approaches for DS reconstruction (DSR) enable training on many DS simultaneously, and revealed that extracted latent features are often related to crucial control parameters of the underlying DS that varied across the training corpus. However, true out-of-domain forecasting abilities of these models, e.g., across tipping points, remain limited, and fine-tuning, or even full model retraining, on time series from the new dynamical regime is usually required. Here, we mathematically analyze the root of these limitations in previous model formulations and identify three core shortcomings rooted in a mismatch between structural assumptions of the reconstruction model and typical properties of physical systems. We propose a combination of remedies for these shortcomings, most importantly feature splitting, and furthermore derive a closed-form bound on the reliable extrapolation range. We demonstrate empirically that our techniques allow for accurate zero-shot prediction into new dynamical regimes, outside the observed training regime, as, e.g., encountered across tipping points.

---


### 508. [Understanding Parallel Samplers in Masked Diffusion via Random Walks on Graphs](https://arxiv.org/abs/2606.22976)

**<font color=#1a73e8>作者：</font>** Vansh Bansal, Cho Cholyeon, Syamantak Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose using random walks on graphs as a verifiable sandbox to study different parallel sampling strategies in masked diffusion models (MDMs). We train an MDM on random walk samples from a fixed graph. The graph or the transition kernel is never shown to the model explicitly and plays the role of latent structure in the sequences, albeit one that is controllable and can be used for quantitative evaluation. Thus, this framework enjoys a Sudoku-like validity check: verifying that an output is a valid walk and estimating the Markov kernel from the walks to measure distribution fidelity.
Using simple graphs, we theoretically prove that parallel unmasking via widely used scores like lowest entropy is not uniformly better than a random parallel sampler; the performance critically depends on the structure of the underlying graph. We develop a new bisection sampler for random walks, which takes logarithmic steps in the sequence length and is provably exact under perfect training. Experiments on various graph walk tasks show that different parallel samplers are better for different graphs even in practice. Our initial experiments on a pretrained OpenWebText MDM show that the bisection-style samplers improve speed-quality tradeoffs even for language generation. Together, these results position graph random walks as a mechanistic benchmark for diagnosing and designing parallel samplers for masked diffusion models.

---


### 509. [Joint Air Traffic Flow and Capacity Management via Answer Set Programming](https://arxiv.org/abs/2606.22978)

**<font color=#1a73e8>作者：</font>** Alexander Beiser, Markus Hecher, Nysret Musliu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operational Air Traffic Flow and Capacity Management (ATFCM) balances flight demand with available sector capacity, to ensure safe and efficient operations. Mathematical models enhance operational ATFCM performance by framing demand-capacity balancing as an optimization problem, maximizing efficiency while adhering to safety constraints. However, SOTA research optimizes the aircraft trajectories (called ATFM) or the sector configuration (called DAC) separately. This leaves a research gap of whether joint optimization of ATFM and DAC can bring benefits. We partially address this limitation by introducing a joint ATFCM model with an encoding in Answer Set Programming (ASP). The ASP implementation is evaluated against two baselines applied to our joint model: a SOTA Mixed Integer Programming (MIP) model and an iterative CASA-based heuristic. Computational experiments utilize an instance generator fitted to historical OpenSky Network flight data. Our results indicate that the ASP model outperforms the MIP model, while ASP remains competitive against heuristics on small instances. Furthermore, while DAC has the largest improvement on solving performance compared to rerouting and delaying, unrestricted variants of DAC or rerouting lead to search space thrashing.

---


### 510. [Subject-Level Unknown-Identity Identification from Leap Motion Controller 2 Hand Landmarks](https://arxiv.org/abs/2606.22986)

**<font color=#1a73e8>作者：</font>** Bahar Moharrer, Susanna Cifani, Marco Raoul Marini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work studies subject recognition from Leap Motion Controller 2 (LMC2) hand landmark data under a subject-level unknown-identity identification protocol on the Multi View Leap2 Hand Pose (ML2HP) dataset. Using only the landmark modality, we retain the original geometric representation and enrich it with fingertip-to-palm distances and palm-normalized inter-finger angular descriptors. Evaluation is performed under a Leave-One-Subject-Out (LOSO) protocol in which, for each outer fold, one subject is excluded from the enrolled set and treated as unknown at test time. To avoid tuning on the true outer unknown subject, the unknown-rejection threshold is selected in an inner validation step by temporarily withholding one enrolled subject from the inner gallery and using it only for threshold estimation. We compare a tree ensemble baseline with two neural alternatives: a learned embedding baseline based on centroid matching and cosine-similarity-based rejection, and an MLP+OpenMax model, which represents a more established open-set recognition approach. Under this evaluation setup, Extra Trees remains the strongest overall method, indicating that the main challenge on this benchmark is not enrolled-subject discrimination alone, but robust score separation between known and unknown probes. The results support the feasibility of compact, interpretable landmark-based descriptors for contactless hand-based unknown-subject rejection and identification on a small-cohort dataset.

---


### 511. [Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?](https://arxiv.org/abs/2606.22987)

**<font color=#1a73e8>作者：</font>** Yu Zhan, Guangcheng Chen, Hanjing Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-view mesh reconstruction predicts object meshes and spatial layouts from a single observation, making it attractive for fast robot spatial reasoning and real-to-sim digital twins. However, robot-mounted cameras naturally rotate during manipulation and navigation, while learned single-view reconstruction models often rely on view-dependent priors and may generalize poorly to out-of-distribution camera rotations. Such rotations can introduce 3D inconsistencies, incorrect layouts, and violations of physical constraints, but this failure mode remains under-evaluated. We introduce an evaluation protocol with controlled axis-wise roll, pitch, and yaw sweeps to trace errors in monocular depth estimation (MDE), canonical object meshes, camera-space layout, and physical plausibility within a representative SAM3D-style pipeline. On the Aria Digital Twin dataset and a real Franka wrist-camera sequence, camera rotations induce MDE distortion, layout drift, and collision penetration, while canonical mesh predictions remain relatively stable. A two-stage SAM3D+FoundationPose pipeline is more robust than one-stage feed-forward layout prediction, and our Gravity-Aware Refinement reduces one-stage pairwise ICP-based layout-orientation error by 47.1$\%$. Our evaluation reveals that current single-view mesh reconstruction methods generalize poorly to robot camera rotation, and suggests that explicit gravity cues are important for reliable robotic single-view mesh reconstruction.

---


### 512. [Public Diffusion Models, Private Images: Key-Controlled Inversion for Conditional Reconstruction](https://arxiv.org/abs/2606.22988)

**<font color=#1a73e8>作者：</font>** Lijunxian Zhang, Weihai Li, Bin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Diffusion models are often deployed in settings where model parameters are publicly accessible (e.g., open-source libraries or released checkpoints). This white-box scenario creates a serious security risk: any user who obtains an intermediate latent representation can invert the process to recover the original input image. Most prior work on access control for generative models assumes a black-box model (i.e., parameters are kept secret), typically under an honest-but-curious adversary. By contrast, we address the more challenging and realistic white-box setting where all parameters are public.
We present a key-controlled inversion framework that turns the inherent error propagation of diffusion models, which exponentially amplifies small perturbations, into a security asset. By injecting key-dependent noise into the inversion formula, we ensure that only a user with the correct key can reconstruct the original image; any other key yields unrecognizable output.
Theoretically, by leveraging existing error-propagation theory for diffusion models, we prove that the resulting ciphertext distribution is IND-CPA secure and derive that the adversary's advantage is exponentially small in a tunable security parameter, hence negligible for any probabilistic polynomial-time (PPT) adversary. Experimentally, we validate these security guarantees across several models and datasets and further demonstrate cross-model robustness, that the injected key noise does not amplify the performance drop caused by model discrepancies.

---


### 513. [Neural Architecture Search of Sample Reweighting Networks for Complex Distribution Shift](https://arxiv.org/abs/2606.22991)

**<font color=#1a73e8>作者：</font>** Keisuke Sugawara, Kento Uchida, Shinichi Shirakawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample reweighting is a major approach to addressing distribution shifts, such as label noise and class imbalance. Meta-Weight-Net (MW-Net) is a promising sample reweighting network that computes weights based on classification loss. Although MW-Net improves prediction performance under a single type of distribution shift using a simple neural network, its performance degrades when facing both label noise and class imbalance, where it is hard to determine appropriate weights solely from classification loss and using a simple network. In this study, we introduce neural architecture search to MW-Net to mitigate such performance degradation. Using the tree-structured Parzen estimator, we explore the optimal number of hidden layers and nodes and select the most suitable intermediate layer in the classification model to serve as the input for MW-Net. Experimental results on the CIFAR-10 and CIFAR-100 datasets that were modified to include both label noise and class imbalance demonstrate the effectiveness of neural architecture search for MW-Net.

---


### 514. [Do Sparse Autoencoders Learn Meaningful Concept Hierarchies?](https://arxiv.org/abs/2606.22994)

**<font color=#1a73e8>作者：</font>** Nils Grandien, David Steinmann, Felix Friedrich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have become an important tool for unsupervised concept discovery in large models. To make the resulting feature spaces more interpretable and manageable, recent approaches have begun imposing hierarchical structure, either explicitly or as an implicit effect of training constraints, yet rigorous comparison remains difficult. There are no agreed-upon requirements for what a meaningful feature hierarchy should satisfy, and evaluation has largely relied on qualitative illustrations with fragmented quantitative protocols. To address this, we derive a set of key requirements for generalization/specialization hierarchies in unsupervised concept discovery, drawing on semantic net and taxonomy research alongside recent SAE work, and use them to derive a concrete evaluation protocol. Applying this protocol to current SAE approaches trained on visual data, we find that while feature spaces generally provide a basis for sensible hierarchies, establishing good hierarchical structure remains challenging. In particular, feature absorption, both in its well-known hard form and in a continuous, soft form, systematically compromises hierarchy quality, pointing to a fundamental tension that future approaches will need to navigate.

---


### 515. [MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations](https://arxiv.org/abs/2606.23000)

**<font color=#1a73e8>作者：</font>** Yuhua Luo, Junsheng Zhang, Mengyin Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion follows a temporal hierarchical structure, transitioning from low-frequency global trajectories to high-frequency details. Inspired by the success of multi-level autoregressive models in computer vision, we propose MotionMAR, a coarse-to-fine framework for motion reconstruction from sparse observations. It first estimates the global trajectory of human motion and then gradually refines the temporal details. This architecture consists of four integrated components. The Temporal Multi-scale Tokenization (TMT) VQ-VAE encodes the data at multiple temporal resolutions, separating semantic motion from minor jitters. The Motion Autoregressive Network (MAN) operates in this latent space, predicting motion across scales. It first establishes the global structure through coarse indices and then generates finer indices to recover specific details. Meanwhile, the Scale-Aware Control (SAC) module integrates sparse tracking data to ensure the generated output aligns with actual observations. The Motion Refinement Network (MRN) subsequently smooths consecutive poses and eliminates quantization artifacts. Experiments show that MotionMAR achieves state-of-the-art accuracy on the AMASS dataset, providing a reliable and structure-aware approach for motion reconstruction. The source code is publicly available at this http URL.

---


### 516. [Machine Translation and Post-Editing: Comparative Evaluation of Different MT Systems and Post-Editor Groups in Specialised Translation](https://arxiv.org/abs/2606.23002)

**<font color=#1a73e8>作者：</font>** Joachim Minder, Alexandra Mestivier, Natalie Kübler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article aims to evaluate the quality of machine translation (MT) and post-editing (PE) in the context of specialised translation from English into French. Three MT systems (DeepL, eTranslation and Systran) were compared, and two groups of post-editors -linguists/translators and NLP experts -were asked to perform post-editing. Translation assessment is based on error annotation using an error typology adapted to MT and PE evaluation. The results reveal significant differences between the three MT systems and the two groups of post-editors, particularly in terms of terminological accuracy and fluency. This study highlights the importance of domain knowledge in specialised translation, as well as the limitations and variable performance of MT systems in language for specific purposes (LSP).

---


### 517. [From Point Estimates to Distributions: GMM Pooling for MIL in Preterm Birth Prediction](https://arxiv.org/abs/2606.23005)

**<font color=#1a73e8>作者：</font>** Hussain Alasmawi, Numan Saeed, Soha Said 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preterm birth (PTB) prediction can enable targeted surveillance and timely intervention, yet most ultrasound-based models use a single selected transvaginal ultrasound (TVUS) frame per patient despite routine exams acquiring multiple cervical images. We formulate PTB prediction as a multiple instance learning (MIL) problem, representing each patient as a variable-sized bag of TVUS images with a single outcome label. To move beyond standard MIL aggregators that collapse a bag into a point estimate, we propose a Gaussian Mixture Model (GMM) pooling, which summarizes all images in a bag into a fixed-length representation by modeling their feature distribution. This design captures intra-patient variability. We evaluate the method on a private clinical cohort and on a public lymph node metastasis benchmark. For PTB prediction, GMM pooling improves over the instance-based model PR-AUC from 0.44 to 0.56. On the lymph node benchmark, it achieves state-of-the-art performance with 0.91 F1-score and 0.89 ROC-AUC for classification and 0.18 MAE for regression. The code is publicly available at this https URL.

---


### 518. [A Novel Approach to Temporal QoS Estimation via Extended Kalman Filter-Incorporated Latent Feature Analysis](https://arxiv.org/abs/2606.23010)

**<font color=#1a73e8>作者：</font>** Ye Yuan, Song Wang, Hongxun Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting temporal Quality of Service (QoS) data is critical for optimizing network services and rationalizing resource allocation in cloud computing and service-oriented systems. Existing mainstream methods have achieved promising predictive performance. However, their purely data-driven manner limits their ability to capture non-stationary temporal patterns, thereby leading to accuracy degradation when temporal QoS data exhibits fluctuations. To tackle this limitation, we propose a novel Extended Kalman Filter-Enhanced Latent Feature Analysis (EKL) model to perform efficient and accurate temporal QoS prediction from the perspective of bidirectional model-data-driven learning. Its main idea is three-fold: a) designing a model-driven feature producer to obtain the temporal latent features to capture the intricate temporal pattern following the principle of an Extended Kalman Filter; b) building a data-driven feature producer based on the alternating least squares algorithm to identify time-invariant latent features describing intrinsic user-service characteristics; c) exploiting a density-oriented parallel strategy that achieves workload balancing by sorting users in accordance with their service invocation density, which effectively elevates computational efficiency. In addition, we provide a rigorous theoretical analysis to formally prove the convergence of the proposed EKL. Experimental evaluations conducted on real-world temporal QoS datasets reveal that our proposed EKL surpasses existing state-of-the-art models with respect to both computational efficiency and prediction accuracy for missing temporal QoS data.

---


### 519. [Counterfactual learning of new adaptive instructional policies using logged data](https://arxiv.org/abs/2606.23015)

**<font color=#1a73e8>作者：</font>** Samuel Girard, Sein Minn, Amel Bouzeghoub 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing instructional policies in Intelligent Tutoring Systems (ITS) typically requires costly online experimentation or student simulators that may fail to capture real-world dynamics. This paper introduces an offline contextual bandit framework that learns new adaptive policies directly from logged interaction data. By mapping student-item interactions onto a continuous latent proficiency-difficulty scale using a Rasch model, we cast the tutoring process as a continuous stochastic bandit problem. We propose a novel reward function designed to optimize ''flow'' by balancing task challenge with student success. Our approach includes a round-specific behavior policy estimation that serves as both a propensity model for off-policy evaluation and a diagnostic tool for ITS adaptivity. We demonstrate the efficacy of this framework across four large-scale real-world datasets, achieving consistent policy improvements over the logged behavior policy. The results show that effective instructional policies can be learned and visualized within seconds of computation, providing a scalable path for improving adaptive learning systems without further data collection.

---


### 520. [ScalingAttention: Discovering Intrinsic Sparse Attention Topology for Video Diffusion Transformers](https://arxiv.org/abs/2606.23019)

**<font color=#1a73e8>作者：</font>** Ruiliang Zhou, Xuecheng Wu, Kang He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Diffusion Transformers (DiTs) have revolutionized high-fidelity video generation, their reliance on 3D full attention creates a quadratic computational bottleneck. Existing sparse methods face a dilemma: dynamic pruning suffers from prohibitive runtime overhead and memory fragmentation, while static heuristics fail to capture fine-grained dependencies. In this work, we propose ScalingAttention, a training-free framework grounded in a key inductive bias: while individual activations are input-dependent, the high-mass attention regions for each head rapidly converge to a stable, prompt-agnostic Intrinsic Sparse Topology. This topology is weight-encoded, scale-invariant, and efficient to extract. ScalingAttention decouples topology discovery from sparsity control via: (1) WEST (Weight-Encoded Sparse Topology), which extracts a robust block-sparse prior mask offline to eliminate runtime search; (2) FAST (Fidelity-Aware Sensitivity Tuning), which adaptively tunes head-wise sparsity based on diffusion fidelity requirements. To ensure practical acceleration, we co-design a hardware-aligned bit-wise block-sparse kernel. Experiments on Wan2.1 show up to 1.90X end-to-end speedup with superior fidelity, establishing a new Pareto frontier over state-of-the-art baselines.

---


### 521. [Boosting Neural Video Codec via Scale-Driven Online Flow Refinement](https://arxiv.org/abs/2606.23023)

**<font color=#1a73e8>作者：</font>** Tiange Zhang, Rongqun Lin, Haocheng Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although state-of-the-art neural video codecs (NVCs) have achieved remarkable performance, they suffer from limited generalization when encountering complex motion patterns unseen during training. To bridge this domain gap without the expensive cost of online fine-tuning, we propose a Training-Free Scale-Driven Online Flow Refinement (SOFR) method. Serving as a plug-and-play module, SOFR integrates motion information from coarse and fine scales and dynamically fuses them according to warping accuracy, effectively rectifying motion estimation errors with negligible computational overhead. Furthermore, we design a rate-aware strategy that selects different dynamic fusion strategies according to bitrate modes, and employs a reliability check based on warping error to ensure robustness. Extensive experiments on the USTC-TD dataset verify the effectiveness and generalization of SOFR across various NVC frameworks, including DCVC-SDD, DCVC-FM, and EHVC. Notably, it brings an average of 2.84% and 4.05% bitrate savings in terms of PSNR and MS-SSIM, respectively, to DCVC-FM with negligible coding time increase. Our code is available at this https URL.

---


### 522. [Learning Stable Canonical Worlds for Novel View Synthesis and Beyond](https://arxiv.org/abs/2606.23027)

**<font color=#1a73e8>作者：</font>** Xiaoyu Xu, Jian Zou, Sheyang Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian splatting (FFGS) facilitates real-time novel view synthesis, yet current methods often remain tied to view-dependent predictions. As more input views are added, they may accumulate noisy or redundant evidence instead of converging to a stable scene representation. In this paper, we introduce CanonicalGS, a feed-forward pipeline that maps cluttered multi-view observations into a stable, scene-centric representation. CanonicalGS first extracts view-centric evidence from depth, semantic features, and uncertainty estimates, and then aggregates this evidence in a canonical latent world using uncertainty-aware fusion. By emphasizing reliable observations while suppressing uncertain or redundant ones, CanonicalGS produces representations that scale more effectively for novel view synthesis and transfer to downstream visual perception tasks. Experiments show up to a $2.5$ dB improvement in peak signal-to-noise ratio for synthesizing novel views and an $11\%$ gain in semantic segmentation accuracy.

---


### 523. [Physics-Guided Spatiotemporal State Space Modeling for Lookahead Molten Pool Segmentation in Laser Wire-Feed Welding](https://arxiv.org/abs/2606.23028)

**<font color=#1a73e8>作者：</font>** Sen Li, Haichao Cui, Changhao Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time weld-pool perception is critical for closed-loop control in laser wire-feed welding, where sensing, computation, and actuator response introduce unavoidable delay. This paper presents a physics-guided spatiotemporal state space network for lookahead weld-pool segmentation. The model uses historical coaxial grayscale images, welding process parameters, and aligned wire-state electrical signals to predict the future semantic layout of three physically meaningful regions: keyhole, wire, and molten pool. It combines a visual encoder, process- and sensor-conditioned feature normalization, patch-level temporal state space modeling, horizon-conditioned latent prediction, dense future feature prediction, and a motion-aware mask decoder. Auxiliary signed-distance-function supervision, temporal consistency, feature distillation, and fine-grained keyhole losses further constrain the predicted geometry and local motion. Experiments on a 43-sequence laser welding dataset show that the proposed WeldMamba reaches 74.63\% mIoU at a 500 ms lookahead. Ablation studies further show that temporal history, patch-level state space modeling, and keyhole motion awareness are the main contributors to robust future segmentation.

---


### 524. [From numerical proportions to analogical proportions between probabilities](https://arxiv.org/abs/2606.23029)

**<font color=#1a73e8>作者：</font>** Henri Prade, Gilles Richard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analogical proportions link four items a, b, c, d by a relation stating that ``a is to b as c is to d", a, b, c, d being the formal representation of real world entities, ranging from simple numerical values to more complex structures such as profiles. Accordingly, $a, b, c, d$ could be atomic values like Boolean, nominal or numerical values, more generally vectors of such values, or even families of items represented by logical formulas. In this paper, we consider another representation setting, which is the probabilistic one. Precisely, the article proposes a study of {analogical} proportions between probabilities, whether they are simply between probability values, or between distributions (which requires the preservation of their normalization). More particularly, we study the properties of definitions based on arithmetic proportion, or on a combination of the former with geometric proportion, while other options are also discussed. Previous works have shown that when four profiles a, b, c, d, represented as vectors, form analogical proportions componentwise, it is likely that their classes form an analogical proportion also. This is the basis of an analogical proportion-based classification method that can produce accurate predictions. Similarly, in this paper, each profile is associated with a distribution describing the frequencies of the possible values of a discrete attribute of interest. We then discuss and experimentally investigate if the distributions associated to four profiles forming an analogical proportion themselves also form an analogical proportion.

---


### 525. [DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031)

**<font color=#1a73e8>作者：</font>** Tania Aguirre, Luis Roldão, Moussab Bennehar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic urban scenes remains challenging due to the unbounded nature of driving environments and the presence of multiple dynamic objects. Currently, potentially faster sparse voxel methods are mainly designed for static scenarios. On the other hand, dynamic approaches based on 3D Gaussian Splatting, despite their high-fidelity, are often time-consuming for driving scenarios and exhibit uncontrollable memory growth in large scenes. To address these limitations, we present DrivingVoxels, a compositional sparse voxel rendering framework for dynamic driving scenes. Our method jointly rasterizes sparse voxels from multiple independent octrees within a single rendering pass. Each rigid dynamic object is represented by an octree defined in its local coordinate frame, while a separate static octree models the stationary background. DrivingVoxels adopts a fully explicit, neural-free representation together with a LiDAR-guided structural initialization that efficiently captures scene geometry. We evaluate our framework on the PandaSet benchmark, demonstrating that DrivingVoxels performs on par on perceptual metrics and better on structural metrics for NVS and reconstruction while requiring shorter training times than previous 3DGS-base methods to an efficient optimization workflow anchored by a strong LiDAR prior.

---


### 526. [Prime Fourier Embeddings: A Principled Basis for Modular Arithmetic](https://arxiv.org/abs/2606.23044)

**<font color=#1a73e8>作者：</font>** Hyunsang Hwang, Suhyun Bae, Donghun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numbers have algebraic structure that standard neural embeddings often fail to expose. We introduce Prime Fourier Embeddings (PFE), which encode integers as prime-indexed (cos, sin) pairs derived from the harmonic analysis of Q, providing a pre-structured representation in which modular arithmetic reduces to selecting the relevant prime channel rather than discovering algebraic structure from scratch. We prove that any linear map equivariant with respect to the product group action on PFE must be block-diagonal with one independent block per prime -- a consequence of Schur's lemma applied to the resulting character decomposition. For square-free composite moduli, the Chinese Remainder Theorem predicts which prime channels are task-relevant. Both predictions are confirmed empirically: ablation studies show specialization ratios exceeding 500x between task-relevant and task-irrelevant channels, with perfect in-distribution test accuracy across all square-free composite moduli tested.

---


### 527. [UECP: Uncertainty-Enhanced Collaborative Perception](https://arxiv.org/abs/2606.23046)

**<font color=#1a73e8>作者：</font>** Kang Yang, Tianci Bu, Peng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception serves as a pivotal solution to enhance the perception capability of individual agents in autonomous driving, where a core challenge lies in seeking reliable evidence to quantify and weight the contribution of each participating agent. Existing methods typically rely on a confidence map, which is co-trained with the detection head, but it is inherently correlated with the detection results and thus fails to provide unbiased physical evidence. Furthermore, how to deeply integrate evidence into the cooperative fusion process remains an open question. To address these issues, this paper first proposes an uncertainty map, a physically grounded and unambiguous metric for evaluating perception quality. This map is directly supervised by real-time sensor signals, i.e., LiDAR point density, ensuring decoupling from detection noise and thereby providing physical scenario-aware evidence for weighting agent contribution. Based on this map, we develop the Uncertainty-Enhanced Collaborative Perception (UECP) framework, centered on the Uncertainty-Aware Pyramid Fusion (UAPF) module. UAPF uses a coarse-to-fine strategy, with two key components: Uncertainty-Weighted Downsampling (UWD) for high-fidelity feature preservation, and Uncertainty-Guided Residual Fusion (UGRF) to reinforce ego features, suppressing noise and ensuring robust fusion. Extensive experiments on real-world datasets show UECP outperforms state-of-the-art methods in effectiveness and robustness by embedding the uncertainty map into fusion. Code will be publicly available.

---


### 528. [Some Results about the Expressivity of Preference-Incomplete Structured Argumentation Frameworks](https://arxiv.org/abs/2606.23055)

**<font color=#1a73e8>作者：</font>** Antonio Yuste-Ginel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies the expressive power of ASPIC$^+$ argumentation frameworks with uncertain preference profiles by comparing them with several abstract formalisms with uncertain defeats. Most of our results are negative (and some of them are theoretically unexpected). We also conjecture a positive, non-trivial threshold for the expressivity of uncertain preferences, and prove some essential preliminary steps toward the confirmation of this conjecture.

---


### 529. [Three-Step Hierarchical Transformer for Multi-Pedestrian Trajectory Prediction](https://arxiv.org/abs/2606.23058)

**<font color=#1a73e8>作者：</font>** Raphaël Delécluse, Hazem Wannous, Laurent Grisoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian trajectory prediction requires modeling temporal dynamics, multimodal cues, and social interactions in crowded environments. Existing methods often address these factors separately or entangle them in costly attention blocks, limiting scalability, flexibility, and interpretability. We propose a three-step hierarchical Transformer that explicitly separates temporal encoding, multimodal fusion, and scene-level interaction reasoning. Lightweight GRU summaries enable efficient cross-modal attention, while social attention over time--agent tokens captures inter-pedestrian influences at manageable cost. Experiments on JTA, JRDB, and the Pedestrians and Cyclists in Road Traffic dataset show state-of-the-art performance on real-world datasets (JRDB, Urban) and competitive results on JTA. Ablation and qualitative analyses confirm the contribution of each stage and the model's ability to anticipate complex behaviors such as early turning.

---


### 530. [MotionHalluc: Diagnosing Kinematic Hallucinations in Fine-Grained Motion Reasoning](https://arxiv.org/abs/2606.23061)

**<font color=#1a73e8>作者：</font>** Weile Guo, Shenghong He, Danying Mo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion instruction generation in cross-video comparison aims to produce corrective feedback that describes the differences between a query and a reference motion. However, existing models often generate instructions that exhibit motion hallucinations, failing to reflect actual kinematic differences between paired videos. To systematically investigate these hallucinations, we introduce MotionHalluc, a dedicated benchmark for evaluating motion hallucinations in paired-video comparison. MotionHalluc comprises 1540 fine-grained questions over 553 video pairs, evaluating hallucinations along three core dimensions: (1)directional hallucination, (2)attributional hallucination, and (3)temporal hallucination. Extensive evaluations of state-of-the-art large multimodal models demonstrate high susceptibility to these hallucinations. Furthermore, we provide Perceive-Parse-Verify (PPV) as a training-free measurements extraction and verification baseline that converts candidate instructions into executable measurement queries and supplies kinematic measurements at inference time. Our results show that this simple measurements injection yields an average 10.6% performance gain across models, suggesting that motion reasoning with explicit quantitative measurements is a key factor in reducing hallucinations in cross-video comparison. Our code and dataset will be made publicly available upon acceptance.

---


### 531. [Rethinking Prototype-based Similarity Learning for Few-Shot Object Detection](https://arxiv.org/abs/2606.23069)

**<font color=#1a73e8>作者：</font>** KunHo Heo, Seungjae kim, Wongyu Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot object detection aims to detect novel object categories from only a few labeled examples, avoiding costly large-scale annotation. Recent prototype-based similarity learning approaches enable training-free adaptation by matching query features with class prototypes. However, they suffer from two fundamental limitations: (i) class confusion arising from inter-class similarity margin collapse, and (ii) insufficient visual cues for precise localization, as similarity scores capture only class-level semantic affinity while providing limited spatial information. To address these issues, we introduce two complementary components. Text-Anchored Semantic Mask (TSMa) leverages class-level text features as semantic anchors to identify semantically aligned channels through channel-wise interaction between visual and text features. By suppressing style-induced spurious responses and emphasizing class-intrinsic signals, TSMa enlarges inter-class similarity margins and mitigates class confusion. We further propose Stage-Aligned Hierarchical Autoregressive Regression (SHARe), which reformulates localization as a hierarchical autoregressive process that progressively refines bounding boxes across multiple stages. SHARe leverages the layer-wise characteristics of ViT representations by aligning feature abstraction levels with regression stages: deeper layers guide early coarse localization, while shallower layers rich in edge and texture cues refine spatial details in later stages. Experiments on COCO demonstrate a new state of the art, outperforming the previous best by +10.1 nAP, with extensive analysis validating each component. The code is available at this https URL.

---


### 532. [Understanding the Stealthy BGP Hijacking Risk in the ROV Era](https://arxiv.org/abs/2606.23071)

**<font color=#1a73e8>作者：</font>** Yihao Chen, Qi Li, Ke Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The partial deployment of Route Origin Validation (ROV) poses an unexpected security threat known as stealthy BGP hijacking, i.e., a particularly elusive form of BGP hijacking where malicious routes divert traffic without reaching (and thus alerting) the victims. This risk remains largely unexplored, with neither documented real-world incidents nor systematic characterization available. To bridge this gap, we formalize stealthy BGP hijacking and propose heuristics to discover potential instances through routing table discrepancies. We conduct the first empirical study to track and profile stealthy BGP hijacking in the wild, contributing a curated real-world incident dataset and a long-term monitoring service. Inspired by the empirical insights, we further conduct an analytical study to exhaustively assess the risk. This requires accurate ROV deployment data, complete Internet-wide routes, and tailored analytical models. To address these challenges, we develop SHAMAN, a BGP route inference framework dedicated to assessing stealthy BGP hijacking risk. SHAMAN consolidates multiple sources to construct an accurate view of ROV deployment, infers complete Internet-wide routes through a highly efficient matrix-based approach, and facilitates statistical risk analysis via a "victim-target-hijacker" 3-tuple model. By reducing the time for generating Internet-scale routes from over three months to just 5.22 hours, SHAMAN enables systematic risk assessment across 8.3 billion generated routes under real-world ROV deployment. Our findings reveal a 14.1% overall success probability for stealthy BGP hijacking, with targeted attacks reaching 99.5% success in specific cases. Validation against our real-world dataset shows up to 95.9% incident-level accuracy, demonstrating the fidelity of our analytical results.

---


### 533. [PeLAP-A: Adaptive Latent Pruning for Lightweight Latent Diffusion Models](https://arxiv.org/abs/2606.23086)

**<font color=#1a73e8>作者：</font>** Kissa Zahra, Zaib Un Nisa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models achieve strong generative performance by operating in a compressed latent space produced by a variational autoencoder (VAE). However, it remains unclear whether all latent channels contribute equally to the diffusion process, or whether significant redundancy exists. We introduce PeLAP-A (Adaptive Latent Pruning for Diffusion), a lightweight framework that augments a standard latent diffusion pipeline with a learnable channel-wise importance predictor. A two-layer MLP operating on globally pooled latent features produces a soft mask that suppresses unimportant latent channels before they enter the denoising UNet. The entire system is trained jointly on CIFAR-10 under a combined diffusion, reconstruction, and sparsity loss. Experiments reveal a striking result: under aggressive sparsity regularization (lambda = 0.01), the importance predictor drives all latent channels to near-zero yet the denoising UNet achieves lower diffusion loss (0.0236 vs. 0.0240) and lower VAE reconstruction MSE (22.59 vs. 24.67) compared to the unpruned baseline. We term this the sparsity collapse phenomenon and provide an analysis of why it occurs and what it reveals about the information requirements of latent diffusion models. These findings constitute an exploratory study of sparsity dynamics in latent diffusion training, and demonstrate that denoising UNets can remain remarkably robust to latent channel suppression even under aggressive regularization. Code is available at: this https URL.

---


### 534. [FLFL: Federated Latent Factor Learning for Private Recovery of Spatio-Temporal Signals](https://arxiv.org/abs/2606.23091)

**<font color=#1a73e8>作者：</font>** Chengjun Yu, Di Wu, Yi He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless sensor network (WSNs) stands out as a burgeoning and promising domain in intelligent sensing. Owing to various factors such as sudden sensor malfunctions or deliberate shutdown of partial nodes to save energy, the collected sensing signals from WSNs commonly have massive missing data, leading to adverse effects on subsequent analysis or decision-making. Latent factor learning (LFL) has proven to be highly effective in recovering the missing data for WSNs. However, the existing LFL models require the collected sensing signals to be maintained in one central place like a central server, which is becoming unacceptable for data owners who are getting increasingly privacy-sensitive. To address this issue, this paper innovatively proposes a federated latent factor learning (FLFL) model for privacy-preserving spatio-temporal signal recovery. Its main idea is two-fold: 1) it designs a sensor-level federated learning framework based on LFL, where each sensor only needs to upload gradient information rather than raw data for training a privacy-preserving recovery model, and 2) it incorporates the spatio-temporal correlation into the designed federated learning framework as the regularization constraint to improve its recovery accuracy. With such designs, FLFL can not only accurately recover the missing data of WSNs but also ensure data owners' privacy-preserving of raw data. To evaluate the proposed FLFL model, extensive experiments have been conducted on four real-world WSN datasets. The results demonstrate that FLFL significantly outperforms eight state-of-the-art federated and non-federated signal recovery models in terms of recovery accuracy with privacy-preserving.

---


### 535. [Cognitive Digital Twins: Ethical Risks and Governance for AI Systems That Model the Mind](https://arxiv.org/abs/2606.23094)

**<font color=#1a73e8>作者：</font>** Vamshi Krishna Bonagiri, Juan Nicolas Sepulveda-Arias, Abdoul Jalil Djiberou Mahamadou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems become increasingly persistent and personalized, they make possible a class of technologies that we call cognitive digital twins (CDTs): dynamic computational representations of a specific person's cognition, updated from behavioral, contextual, or physiological data in order to model, predict, or simulate that person's cognition, or to act as that person's communicative or decision-making proxy. CDTs combine cognitive inference with longitudinal representation, simulation, and proxy action in ways that existing governance strategies for personal assistants, autonomous agents, recommender systems, and automated decision systems only partially address. This paper makes four contributions. First, we define CDTs and distinguish them from adjacent systems. Second, we introduce a 5A governance framework organized around authority, autonomy, access and control, accountability, and availability. Third, we identify CDT-specific risks, from misrepresentation and epistemic authority shifts to shadow twins, simulated participation, proxy action, and proxy-power asymmetries. Fourth, we analyze governance gaps and propose requirements for high-risk CDTs that strengthen consent, purpose limitation, validity, traceability, contestation, independent review, and model retirement. Existing frameworks primarily regulate data processing, automated decisions, or autonomous actions; CDTs also require governance at the level of cognitive representation itself, before any final decision or external action occurs. We argue that CDTs require governance not only because they can act for people, but because they can become infrastructures through which cognition is represented, simulated, classified, and operationalized.

---


### 536. [Minimax Quantile Lower Bounds for Interactive Statistical Decision Making with Privacy](https://arxiv.org/abs/2606.23096)

**<font color=#1a73e8>作者：</font>** Raghav Bongole, Amirreza Zamani, Tobias J. Oechtering 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimax risk and regret are expectation-based criteria and do not capture rare but consequential failures. To address this concern, we develop a $\delta$-explicit minimax-quantile theory for interactive statistical decision making (ISDM). We first provide structural relations between minimax quantiles, lower minimax quantiles, and minimax risk. This includes a quantile-to-expectation conversion and an equivalence between strict and lower minimax quantiles outside a countable set of confidence levels. We then derive two converse tools for ISDM: a high-probability interactive Fano's method and a high-probability interactive Le Cam's method. Then, we show that mutual-information (MI) privacy can be handled in the same framework by restricting the admissible decision class. For coordinatewise Gaussian privatization, we derive a two-point template that isolates the privacy-induced variance inflation. We instantiate this template for Gaussian mean estimation, and use the same two-point strategy directly for two-armed Gaussian bandits. We then derive a minimax quantile lower bound for the $K$-armed Gaussian bandit problem, showing that the interactive Fano method captures the exploration cost over multiple possible best arms. The resulting lower bounds are explicit in the confidence level $\delta$ and in the privacy budget for the private problems. They yield $\log(1/\delta)/n$ scaling for squared-error Gaussian mean estimation, $\sqrt{T\log(1/\delta)}$ scaling for two-armed bounded-mean Gaussian bandits, and $\sqrt{KT\log(1/\delta)}$-type scaling for the $K$-armed bandits, with privacy appearing through a Gaussian variance-inflation factor for the private problems.

---


### 537. [Poisson2Gaussian: Noise Gaussianization to Enhance Image Denoising](https://arxiv.org/abs/2606.23098)

**<font color=#1a73e8>作者：</font>** Xirou Zhou, Zijing Xu, Yibo Qu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quantum nature of light determines the inherent Poisson stochasticity of photon detection, which is ubiquitous in photography, microscopy, and astronomy. However, our controlled numerical studies reveal that the signal-dependency, heteroscedasticity, and statistical asymmetry of Poisson-mixed noise make it challenging for existing denoisers to learn. In contrast, i.i.d. Gaussian noise, with its statistical independence and symmetric distribution, is easier to model for networks. To address this gap, we propose Poisson2Gaussian (P2G), a noise Gaussianization method that explicitly converts complex real-world noise to i.i.d. Gaussian noise via probability density matching beyond low-order moments. We also design an unbiased denoising framework that synergizes P2G with downstream denoisers, ensuring convergence to the underlying signal without requiring paired clean data or explicit noise parameters. Extensive experiments demonstrate that P2G consistently achieves state-of-the-art performance across diverse datasets. In challenging scenarios where noise strongly deviates from Gaussian statistics, our method improves the PSNR by up to 0.75 dB. Notably, P2G is architecture-agnostic and can provide universal improvements for various denoisers. The source code will be publicly available.

---


### 538. [Scene-agnostic ALS boresight self-calibration](https://arxiv.org/abs/2606.23101)

**<font color=#1a73e8>作者：</font>** Aurélien Brun, Jan Skaloud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ALS boresight calibration has relied for two decades on dedicated flight patterns over structured scenes containing planar surfaces of varied aspect and slope. While reliable, this approach imposes constraints on the scene content and operations, which limits its applicability to boresight recovery within routine mapping missions. We present a practical approach that substantially relaxes these requirements by replacing plane-based constraints with scene-agnostic point-to-point correspondences extracted automatically from overlapping ALS strips. Two complementary formulations are proposed to estimate boresight with laser vector observations: (i) a simpler parametric adjustment utilizing INS/GNSS trajectory; (ii) a rigorous formulation treating GNSS and raw inertial data within an existing factor-graph, i.e. a dynamic network, where boresight is added as an additional parameter. Both formulations are evaluated across four operational ALS flights equipped with five inertial systems, covering a wide range of flight altitudes, overlap geometries, terrain types and inertial sensor classes. The analysis draws a clear boundary between the legacy plane-based conditioning that falls short outside the calibration scenario and the proposed formulations, which either recover or absorb boresight effects under conventional mapping geometry. Among them, the lightweight formulation is sufficient for boresight recovery using tactical and navigation grade inertial sensors, while the general factor-graph approach is clearly superior when the inertial sensor errors are less observable within an optimal smoother. This supports the hypothesis that, for INS/GNSS trajectory of sufficient quality, the boresight calibration can be performed without particular scene prerequisites during routine mapping operations using a minimum of 3-4 overlapping strips, with either proposed formulation...

---


### 539. [A Dual-Track Framework for Template-Constrained LaTeX Conversion](https://arxiv.org/abs/2606.23107)

**<font color=#1a73e8>作者：</font>** Chung Cheuk Hei, Liu Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the increasing demands for advanced document conversion, mapping structured Markdown drafts into template-compliant formats like LaTeX remains a challenge. Existing approaches largely depend on either deterministic rule-based converters or pure end-to-end Large Language Model (LLM) generation. The former fails to correctly handle asset insertions and template-specific constraints, while the latter tends to induce semantic drift, leading to hallucinations that are difficult to debug. To address these limitations, we introduce a robust Dual-Track Framework that systematically decouples template formatting from document processing: an offline track extracts template constraints into a reusable manifest, while an online track implements a hybrid execution pipeline. This pipeline confines LLM usage exclusively to reasoning-intensive components (e.g., semantic metadata, bibliographic references, and complex visual/tabular layouts) while delegating rule-based engines for deterministic processing. Empirical evaluation across 7 LaTeX templates and 56 published research papers demonstrates that our method preserves better structural fidelity, satisfies diverse layout constraints, and achieves a higher compilation success rate compared to the previous baselines.

---


### 540. [TTFT-Aware Graph Chain-of-Thought:Distance-Indexed Neural A* for Low-Hallucination Multi-Hop Medical Reasoning](https://arxiv.org/abs/2606.23108)

**<font color=#1a73e8>作者：</font>** Bechir Dardouri, Kaïs Zhioua, Yassine Msaddak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucinations and opaque reasoning remain unacceptable failure modes for clinical LLMs. We present a production-grade GraphRAG stack that constrains answers to verifiable graph chain-of-thought paths in a heterogeneous, ~700K-node medical knowledge graph powering a fertility assistant. The core idea is targeted navigation: a directed Pruned Landmark Labeling (PLL) oracle provides exact distances for sub-millisecond feasibility checks and simple-path enumeration, while a lightweight AStarNet heuristic operates strictly within the PLL corridor to prioritize clinically plausible expansions. We score and pack a small, diverse set of paths (CUI/semantic-type overlap, length prior, provenance priors) to condition generation, yielding compact prompts and improved Time to First Token (TTFT). On fertility-focused queries, the hybrid (PLL+AStarNet) establishes a better latency/recall Pareto frontier than text-only RAG and single-component baselines, lowers TTFT, and reduces clinician-audited hallucinations while preserving explanation clarity. The result is a practical recipe for explainable, low-hallucination multi-hop medical reasoning ready for real-world deployment.

---


### 541. [Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning](https://arxiv.org/abs/2606.23112)

**<font color=#1a73e8>作者：</font>** Jiaqiang Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn tool-using agents must coordinate long-horizon tool sequences while tracking dialogue state and policy constraints. Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. We then construct 161 preference pairs by locating divergence points via state-based matching and prefix-based alignment, filtered through action-correctness annotations, and train DPO under the same ToolGraph context used at inference. Across 375 tau2-bench tasks, ToolGraph raises the weighted average reward from 0.304 to 0.338 (+11.2% relative), while ToolGraph+DPO reaches 0.355 (+16.8% over the baseline), with the DPO gain concentrated in airline and retail. Fine-grained diagnostics further show that roughly half of telecom trajectories exhaust the step budget before action execution and that chosen reward positivity is the most useful checkpoint signal across our 16 evaluated DPO configurations.

---


### 542. [Technical Report for the ICRA 2026 GOOSE 2D Fine-Grained Semantic Segmentation Challenge: Pretraining-Diverse Ensemble of Foundation Vision Encoders for Robust Outdoor Scene Understanding](https://arxiv.org/abs/2606.23113)

**<font color=#1a73e8>作者：</font>** Boyan Wang, Yongxi Huang, Wenjing Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents our solution for the ICRA 2026 GOOSE 2D Fine-Grained Semantic Segmentation Challenge, which requires parsing unstructured outdoor scenes from four camera platforms into 56 fine-grained categories. Our approach pairs foundation vision encoders (including DINOv3, SigLIP2, and InternImage) with a Mask2Former decoder, and trains them with a strong recipe including long training schedules, exponential moving average, a larger crop size, and multi-scale plus flip test-time augmentation. The three encoders, chosen for their complementary pretraining objectives, are combined into a pretraining-diverse ensemble through per-class validation-IoU weighting. Evaluated on the official GOOSE test set, our submission achieves 75.40% composite mIoU and wins the second place of the challenge. Our study further shows that the encoder's pretraining recipe, rather than its parameter count or the decoder design, is the dominant factor for accuracy on this benchmark.

---


### 543. [LUMINA-26: Low-Light Understanding for Modeling and Interpreting Night-time Actions](https://arxiv.org/abs/2606.23118)

**<font color=#1a73e8>作者：</font>** Aman Kumar Pandey, Anil Singh Parihar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light human action recognition remains a challenging problem due to poor illumination, amplified noise, motion ambiguity, and diverse real-world scenes. Existing low-light datasets often lack sufficient action diversity, capture realism, or balanced class distribution, limiting the development of robust models. To address this, we introduce LUMINA-26: Low-Light Understanding for Modeling and Interpreting Night-time Actions, comprising 6,784 clips across 26 action classes, recorded from 22 subjects across 20 indoor and outdoor locations under naturally occurring low-light conditions. We also propose Illumi-Net: An Illumination-Adaptive Mixture-of-Experts Network, which leverages video-level illumination cues to guide adaptive enhancement and transformer-based spatio-temporal feature extraction, with expert-conditioned decision fusion. Our method surpasses previous state-of-the-art performance on ELLAR (Top-1: 55.13%, Top-5: 78.87%) and establishes a strong baseline on LUMINA-26 (Top-1: 75.95%, Top-5: 93.58%), offering a practical benchmark for future low-light action recognition research.

---


### 544. [A Matter of Time: Towards a General Theory of Agency](https://arxiv.org/abs/2606.23122)

**<font color=#1a73e8>作者：</font>** Amahury J. López-Díaz, Carlos Gershenson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agency is often invoked in research on philosophy, biology, and cognitive science without a clear account of how it originates from material organization. Building on temporally parametrized (F, A)-systems, this paper develops a graded organizational theory of agency grounded in relational biology, physical biosemiotics, and process ontology. We argue that self-referential closure cannot be adequately conceived outside time: once the constitutive processes of a semantically closed organization are associated with distinct characteristic timescales, the organization unfolds into an out-of-sync dependency structure that can be formally redescribed as a history-dependent, revisable Asynchronous Dynamic Bayesian Network. This move allows for a principled distinction between autonomy, goal-directedness, agency, and open-endedness. Autonomy arises from precarious closure to efficient causation under material openness; goal-directedness from the maintenance of viability-supporting organization; agency appears when such organization acquires an endogenous anticipatory structure that selectively modulates organism-environment coupling in light of possible futures; open-endedness begins when this anticipatory organization can reconstruct its own future space of possibilities. Our framework reconciles Rosennean anticipation with organizational closure, restricts Markov blankets and active inference to derived formal redescriptions rather than first principles, and reinterprets computational enactivism in non-Fristonian terms. By deriving weaker temporalized organizations, our contribution outlines a hierarchy from proto-agential chemical systems to fully semantically closed agents, with implications for multicellular organisms, synthetic lifeforms, and neuroscience.

---


### 545. [The Fractal Neural Operator: Overcoming Spectral Bias in Chaotic Attractors via Prime-Harmonic Weierstrass Encodings](https://arxiv.org/abs/2606.23123)

**<font color=#1a73e8>作者：</font>** Kanishk Awadhiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models, particularly Transformers and Neural Operators, exhibit a well-documented "spectral bias," effectively acting as low-pass filters that smooth out high-frequency information. While benign in fluid dynamics, this bias is catastrophic for Chaotic Dynamical Systems, where the underlying strange attractor is characterized by fractal geometry and infinite spectral density. We introduce the Fractal Neural Operator (FNO), a novel architecture that utilizes a non-resonant prime number basis to approximate continuous dynamical systems. Unlike geometric encodings ($2^k$), which suffer from spectral gaps and resonance, our Harmonic Weierstrass Encoder injects infinite spectral resolution into the latent space. We demonstrate that FNO extends the valid prediction horizon of the Lorenz-63 system to 347 Lyapunov times, exceeding state-of-the-art Reservoir Computing baselines by a factor of 2.3x. These results suggest that "chaos" is not inherently unpredictable to neural networks, but rather requires non-differentiable, fractal embedding manifolds.

---


### 546. [MambaADv2: Evolving Duality-enhanced State Space Model for Unsupervised Anomaly Detection](https://arxiv.org/abs/2606.23126)

**<font color=#1a73e8>作者：</font>** Xiaobin Hu, Haoyang He, Bo Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent advancements in anomaly detection have demonstrated the efficacy of CNN- and Transformer-based approaches, these architectures face inherent limitations: CNNs struggle to capture long-range dependencies, whereas Transformers suffer from quadratic computational complexity. Consequently, Mamba-based architectures have attracted considerable attention, as they successfully combine superior long-range dependency modeling with linear computational complexity. By critically rethinking the structural evolution across the Mamba lineage 1-3 series, this paper proposes MambaADv2, a framework tailored for multi-class unsupervised anomaly detection. MambaADv2 comprises a pre-trained encoder and a Mamba-inspired decoder, equipped with Duality-enhanced State Space (DSS) modules across multiple scales. The proposed DSS module effectively models both global dependencies and local representations by integrating parallel-cascaded Hybrid State Space (HSS) blocks and frequency-enhanced convolution operations. The structure of the Hybrid State Space (HSS) block is tailored by following the SSD-based Mamba lineage and incorporating Mamba3-style position-aware state-space modeling, leveraging the dual computational paths of linear recurrence and parallel matrix formulation to model local continuity and global contextual comparison, thereby better serving the core anomaly detection objective of precisely reconstructing normal representations while magnifying anomalous deviations. Additionally, we propose a semantics-adaptive progressive scanning strategy that decays scanning complexity along the feature pyramid.

---


### 547. [Spectral Gating via Damped Oscillations for Adaptive Implicit Neural Representations](https://arxiv.org/abs/2606.23129)

**<font color=#1a73e8>作者：</font>** Alex Costanzino, Pierluigi Zama Ramirez, Giuseppe Lisanti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INRs) have been proven successful in encoding continuous signals through coordinate-based networks, yet facing a spectral dilemma: periodic activations capture fine details but act as all-pass filters that memorise noise, while spatially compact activations regularise effectively but suffer from low-frequency bias. Existing attempts to resolve this trade-off introduce computational overhead or tuning frailty. We propose to model each neuron's activation as the steady-state response of a sinusoidally-forced damped harmonic oscillator, whose amplitude naturally governs the network's spectral selectivity during training. By jointly optimising the oscillator parameters alongside the network weights, our method adapts to the target signal's spectral content without explicit regularisation. Initialised in the stopband, the network exhibits a coarse-to-fine learning curriculum that progressively expands its spectral gate, capturing low-frequency structures first and high-frequency details only when justified by the reconstruction objective. Comprehensive experiments show that our approach consistently achieves state-of-the-art or competitive results against established INRs, while requiring no task-specific tuning of any hyperparameters.

---


### 548. [Understanding the (In)Security of Vibe-Coded Applications](https://arxiv.org/abs/2606.23130)

**<font color=#1a73e8>作者：</font>** Junquan Deng, Zhiyu Fan, Ruijie Meng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled vibe coding, an emerging software development paradigm in which users create applications primarily through natural-language interactions with AI agents. Due to its low barrier to entry, vibe coding is rapidly gaining adoption in practice. Unlike conventional AI-assisted programming, where developers remain responsible for implementation and code review, vibe coding delegates a substantial portion of development to AI systems. This shift raises a fundamental question: how (in)secure are applications developed through vibe coding? In this paper, we conduct a systematic study of the security of vibe-coded applications. We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. Using this framework, we examine the prevalence, severity, and root causes of vulnerabilities in the deployed vibe-coded applications. Our study reveals several key findings: (1) vibe-coded applications exhibit recurring vulnerability patterns that differ from those commonly observed in conventional software development workflows, including placeholder logic, unfiltered input, and secret exposure; (2) these vulnerabilities arise from systematic limitations of AI agents throughout the vibe-coding lifecycle, such as memory loss, locally optimized objectives and insufficient security knowledge; and (3) while advances in LLM capabilities and improved prompting strategies can reduce the incidence of vulnerabilities, they do not eliminate the underlying security risks. Overall, our study provides an empirical understanding of the security landscape of vibe-coded applications and lays the groundwork for addressing the security challenges introduced by the growing delegation of software development to AI systems.

---


### 549. [Expert Consensus on Criteria for the Automated Assessment of Laparoscopic Camera Navigation](https://arxiv.org/abs/2606.23131)

**<font color=#1a73e8>作者：</font>** Amir Ebrahimzadeh, Nazila Esmaeili, Michael Ghadimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Laparoscopic camera navigation (LCN) is a critical skill, yet its current assessment typically relies on manual rating systems which are time-consuming and difficult to scale. Automated feedback could significantly enhance surgical training by providing immediate, standardized metrics. This study aims to define, clinically evaluate the relevance, and establish the technical readiness of a set of approaches for LCN assessment.
Methods: We developed a detailed taxonomy of 14 key aspects of camera navigation, categorized into Framing & Composition, Visibility & Clarity, Orientation & Stability, Motion & Dynamics, and Safety & Awareness. For each aspect, we assessed the technological readiness of automated measurement based on the current state of the art (SoTA) in computer vision (CV). To establish clinical relevance, we designed a survey for practicing laparoscopic surgeons to rate the importance of each aspect on a 5-point Likert scale and to select the five most critical skills.
Results: 23 surgeons participated in the survey. Foundational aspects like Field of View, Focus and Centering were rated as most important by surgeons. We present a "Clinical Importance vs. CV Technological Readiness" matrix, identifying high-priority targets for development--aspects that are both clinically crucial and technologically ready to measure.
Conclusion: This work establishes a foundational framework for quantifying LCN skills. By aligning surgeon priorities with CV capabilities, we provide a clear roadmap for automatic skill assessment. This foundation enables the development of AI-driven assistance tools that can accelerate the learning curve for surgical assistants and potentially improve surgical safety and efficiency.

---


### 550. [Koshur Pixel: a large-scale synthetic ocr dataset for kashmiri](https://arxiv.org/abs/2606.23144)

**<font color=#1a73e8>作者：</font>** Haq Nawaz Malik, Faizan Iqbal, Nahfid Nissar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) for low-resource languages is often constrained by the lack of annotated training data and the complexity of script-specific rendering. Kashmiri, written primarily in the Perso-Arabic Nastaliq script, presents additional challenges due to contextual glyph shaping, dense ligatures, and orthographic variability. We introduce Koshur Pixel, the first large-scale synthetic OCR dataset for Kashmiri, comprising 613,078 image-text pairs generated from the KS-PRET-5M corpus using the SynthOCR-Gen framework. The dataset spans multiple fonts and textual granularities, ranging from individual words to full-page documents, and incorporates more than 25 augmentation strategies that emulate real-world document degradations. Koshur Pixel provides a scalable and cost-effective alternative to manual annotation, establishing a foundational resource for training OCR systems, digitizing Kashmiri textual heritage, and advancing language technologies for a severely under-resourced language.

---


> [!TIP]
> 当前位于：**501-550**（第 11/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
