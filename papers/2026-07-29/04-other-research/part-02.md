# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

---

### 51. [Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features](https://arxiv.org/abs/2607.22739)

**<font color=#1a73e8>作者：</font>** Dzmitry Malyshau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how far a deliberately simple behavioral-cloning policy can progress in a visually rich first-person game before adding reinforcement learning or explicit memory. Cortex is a compact Quake policy with 10.98 million trainable parameters in a six-layer transformer over a frozen DINOv3 encoder. It is trained on the Quake subset of the public Pixels2Play corpus: 6,849 recordings (about 474.7 hours), represented as 17.09 million cached decision frames with keyboard and mouse actions. One sampled training epoch uses 517,048 four-frame windows and takes 3.3 minutes of policy-head optimization on one RTX 5080, excluding one-time feature extraction. We evaluate two independent batches of 20 stochastic, 120-second episodes on Quake E1M1. Cortex does not complete the level, but every episode reaches the opening door, button room, and gate descent; 19 of 20 episodes in each batch record at least one kill. Under the same time-controlled harness, released P2P-150M and NitroGen checkpoints remain shallower in five matched-duration episodes each. These comparisons are limited by small reference samples and different native interfaces. Ablations show that denser visual tokens improve combat and survival, while longer optimization and naive action history improve offline metrics without consistently improving play. The remaining failures are consistent with covariate shift and motivate targeted corrective data. We release the policy implementation, checkpoint, and a representative rollout.

---


### 52. [A Diagnostic Gap Framework for Evaluating Reconstruction Fidelity in Weakly Supervised Mammography](https://arxiv.org/abs/2607.22740)

**<font color=#1a73e8>作者：</font>** Vinceline Bertrand, Ionut Cardei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised pipelines for medical imaging have become increasingly popular over the years. These systems often include multiple stages and components, such as reconstruction, generation, and localization, yet standard evaluation metrics provide limited insight into whether clinically relevant information is preserved across each stage. We present the diagnostic gap framework, a practical evaluation tool that measures decision preservation and explanation preservation as a function of measured reconstruction fidelity. To isolate the effect of reconstruction from localization, we evaluate on curated lesion ROI crops using a fidelity ladder of three class-conditional reconstructors---VQ-VAE-GAN, VAE-GAN, and diffusion (SDEdit)---spanning a twenty-fold range in perceptual distance (LPIPS 0.029--0.584). At autoencoder fidelity, both decision and explanation are preserved: AUC changes remain within $\pm$0.005 and attribution similarity (HiResCAM, Grad-CAM++) stays high. At diffusion fidelity, both collapse: pooled AUC drops by 0.253 and mass-pathology AUC falls below chance. The diagnostic gap is thus a measurable function of reconstruction fidelity rather than an intrinsic cost of reconstruction, and the framework provides an architecture-agnostic instrument for identifying when and where multi-stage pipelines lose diagnostic signal.

---


### 53. [QFedPolyp: A Communication- and Inference-Efficient Federated Learning Framework for Polyp Segmentation](https://arxiv.org/abs/2607.22743)

**<font color=#1a73e8>作者：</font>** Madan Baduwal, Priyanka Paudel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Automatic polyp segmentation supports computer-aided diagnosis and early colorectal cancer detec- tion. Centralized deep learning requires hospitals to share sensitive medical data, while federated learning preserves privacy but introduces high communication costs through repeated transmission of full-precision model parameters. We propose QFedPolyp, a communication- and inference-efficient federated learning framework for collaborative polyp segmentation.
Methods: QFedPolyp combines quantization-aware training with low-precision model communication. Each hospital locally trains a lightweight U-Net on private data while simulating quantization during training. Clients transmit quantized model parameters to a central server, where they are reconstructed and aggregated using Federated Averaging. Evaluation is performed on Kvasir-SEG, CVC-ClinicVideoDB, PolypGen, and BKAI-IGH NeoPolyp.
Results: Full-precision federated training achieves Dice scores of 0.910 on Kvasir-SEG and 0.930 on CVC-ClinicVideoDB. Uni- form 8-bit communication reduces transmission cost by approximately 4 times while preserving competitive segmentation accuracy. Quantized models also achieve up to 1.5 times faster inference than full-precision models.
Conclusions: QFedPolyp enables privacy-preserving collaborative polyp segmentation with reduced communication overhead and faster inference. The resulting lightweight models are suitable for real-time clinical deployment.

---


### 54. [Advancing All-Weather Building Damage Mapping to the Instance Level: Outcomes and Insights from the 2026 Bright Challenge](https://arxiv.org/abs/2607.22746)

**<font color=#1a73e8>作者：</font>** Hongruixuan Chen, He Huang, Haifeng Wang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid post-disaster response requires timely, building-level information on whether structures remain intact, are damaged, or are destroyed. Post-event optical imagery, however, may be unavailable because of cloud, smoke, or darkness. The Bright Challenge evaluated all-weather building damage mapping from a submeter-resolution pre-event optical image and a post-event SAR image. Participants were required to detect and delineate each building and assign exactly one of three mutually exclusive damage labels. The challenge extended the globally distributed \textsc{Bright} dataset with instance-level annotations for about 291,000 buildings across 16 disaster events spanning seven disaster types. The final phase was evaluated exclusively on two 2025 events absent from training: a wildfire event in California and a hurricane in Jamaica. A total of 157 participants made 1,289 submissions, and 46 teams entered the final phase. The two winning solutions achieved test mAPs of 0.182 and 0.181, approximately 8.7 times the public baseline of 0.021, but remained far below the best in-domain holdout score of 0.513. Across teams ranked in both phases, performance declined sharply and the rank order changed substantially. The two leading solutions independently favored modality-specific encoding, staged or late optical--SAR fusion, and an optical-dominant separation of building localization from damage recognition. The winning method additionally used scene-aware threshold adjustment and pseudo-label adaptation. These results identify cross-event generalization and stable severity discrimination as the principal remaining challenges. All data, annotations, baseline code, and winning solutions are publicly available at this https URL.

---


### 55. [Learning to Access Computation: Accessibility Plasticity as a Principle of Adaptive Intelligence](https://arxiv.org/abs/2607.22748)

**<font color=#1a73e8>作者：</font>** Zhaowen Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural networks primarily adapt through parameter modification within predefined computational structures. While recent methods introduce modularity, conditional computation, and parameter-efficient adaptation, they generally do not distinguish computational capability from computational accessibility as separate adaptive variables. This work introduces Accessibility Plasticity, a principle of adaptive computation in which systems adapt not only by changing what computation exists, but also by reorganizing which existing computations can interact and participate. We formalize Accessibility Plasticity through a relationship-based operational realization and establish a reuse-first hierarchy of adaptation, where accessibility modification precedes more costly capability and structural changes. A proof-of-concept evaluation on sequential learning tasks shows that accessibility adaptation can reduce capability modification while maintaining comparable task performance. These results suggest accessibility as a distinct adaptive dimension and provide a foundation for future dynamic neural systems whose computational relationships evolve with changing environments.

---


### 56. [Post-Operative Glioma Segmentation via Loss Stabilization, Normalization and Subspace Attention](https://arxiv.org/abs/2607.22749)

**<font color=#1a73e8>作者：</font>** Alexandru Crişan, Diana Borza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking residual tumor after surgery is essential for catching recurrence early, but automating post-operative glioma segmentation remains a difficult task. Although transformer-based architectures, such as SwinUNETR, achieved impressive results, few studies test how well they generalize across clinical protocols. In this paper, we conduct an ablation study on the MU-GLIOMA-POST and UCSF-ALPTDG datasets and show that the standard Generalized Dice Loss (GDL) is unstable under domain shift: the Whole Lesion (WL) Dice drops from 0.88 on the internal validation set to 0.73 on the external UCSF test set. To address this, we pair brain-masked percentile normalization with voxel-level contrastive learning. We also propose a Subspace-Aware Class Attention (SACA) module that re-calibrates the bottleneck features and raises Enhancing Tumor (ET) sensitivity by 8% (9.1% relative improvement) on internal validation. Ensembling these refinements with nnU-Net brings every stable configuration to a WL Dice of 0.94, and the SACA variant ensemble achieves the best boundary error (HD95) of 2.92 mm on MU-GLIOMA-POST.

---


### 57. [Commitment To Cooperation With Self-Negotiated Contracts](https://arxiv.org/abs/2607.22750)

**<font color=#1a73e8>作者：</font>** Tim Wyse, Kaitlin Bustos, Yulia Volkova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents operate with increasing autonomy in a multi-agent world, they will need to learn to cooperate with other agents and with humans to generate mutual benefits. However, cooperation is a challenge because the costs of cooperation are often incurred early on, but the benefits are only realized later, creating an incentive to defect. How can AI agents cooperate with commitment? Here, we draw on inspiration from legal institutions and contracting that human societies have used to solve principal-agent problems of this kind. Contracts provide observable representations of agreements that enable credible commitments through the enforcement of terms. We study the role of contract-based cooperation using LLM-based agents in \CT, a spatial-temporal game that combines bargaining with navigation towards a goal. We study a suite of contract representations that range from formal contracts that compile to code to natural contracts that require reinterpretation. We evaluate agents with a range of LLM backbones using different sizes and providers. We find that self-negotiated contracts can improve cooperative outcomes beyond what is possible with regular trading.

---


### 58. [Beyond Error-vs-Discard Characteristic: Toward Stable and Reliable Evaluation for Face Image Quality Assessment](https://arxiv.org/abs/2607.22752)

**<font color=#1a73e8>作者：</font>** Bhavesh Wani, Žiga Babnik, Vitomir Štruc 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Image Quality Assessment (FIQA) aims to estimate the utility of facial images for reliable recognition. The evaluation of FIQA methods is predominantly based on the Error-versus-Discard Characteristic (EDC), which evaluates performance by progressively discarding low-quality samples and measuring recognition error on the retained subset. In this work, we demonstrate that the widely used EDC protocol has fundamental limitations: Test-Set Divergence and Threshold Drift, which together limit the reliability and comparability of FIQA methods. To address this, we propose discard-based EDC variants and a rank-based Rank Consistency Evaluation (RCE) metric that operates on the entire test set without discarding samples, using a fixed decision threshold. Extensive experiments on five datasets, four face recognition models, and 15 state-of-the-art FIQA methods demonstrate both the limitations of EDC and the effectiveness of the proposed approaches in enabling a more reliable and comparable evaluation. Despite evaluated on face images only, the limitations arise from the EDC protocol rather than the biometric modality, suggesting a broader applicability to biometric quality assessment in general.

---


### 59. [Real-time Reconstruction of Human Visual Perception from fMRI](https://arxiv.org/abs/2607.22753)

**<font color=#1a73e8>作者：</font>** Rishab S. Iyer, Jiaxin Cindy Tu, Cesar Kadir Torrico Villanueva 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time closed-loop neurofeedback based on functional magnetic resonance imaging (fMRI) has led to important scientific and clinical advances. However, the sophistication of the analysis methods used in real-time fMRI lags behind the state-of-the-art in fMRI decoding, largely due to computational factors: Most advanced decoding pipelines do not fit within the envelope of real-time processing, where the analysis needs to be conducted in a matter of seconds and without leveraging data acquired later in the session. Here, we present a real-time compatible adaptation of a computationally intensive state-of-the-art pipeline for reconstructing perceived natural images (MindEye2), and we demonstrate that reliable fine-grained decoding is still achievable in this setting. Using RT-Cloud, an open-source, scalable cloud-based platform, we performed a real-time scan where we decoded single-trial visual perception within seconds after an image was shown to the participant. Finally, we use simulated analyses to document the factors driving changes in performance from offline to real-time analysis. This work serves as a proof-of-concept that it is feasible to deploy these powerful fMRI decoding pipelines in real-time analysis, paving the way for their use in brain-computer interfaces for scientific discovery and clinical treatment.

---


### 60. [An Integrated Deep Learning and Statistical Framework for Whole-Network Gene--Environment Association with Leaf Vascular Architecture](https://arxiv.org/abs/2607.22763)

**<font color=#1a73e8>作者：</font>** Geran Zhao, Yangsheng Wang, Xiaotian Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leaf veins exhibit remarkable diversity in architecture and patterning, yet existing gene--environment association studies have primarily quantified leaf venation using a small collection of low-dimensional summary traits, thereby discarding most of the structural information contained in the original images. We propose an integrated deep learning and statistical framework. The proposed framework achieves four methodological advances. First, it represents the complete leaf vascular architecture as a whole-network image phenotype. Second, it fine-tunes the deep learning-based Edge Detection with Transformers (EDTER) model to accurately extract whole-network leaf vascular architecture from RGB images by jointly learning local and global contextual features. Third, it constructs a new annotated leaf image database by integrating edge maps generated by DiffusionEdge with the Berkeley Segmentation Database (BSDS500). Fourth, it applies Semiparametric Sparse Canonical Correlation Analysis (SSCCA) to perform variable selection and model associations between repeatedly measured high-dimensional Bivariate image responses and high-dimensional predictors while simultaneously accommodating sparse, zero-inflated data represented by edge maps through a truncated latent Gaussian copula model. Two simulation studies demonstrate the performance of the proposed framework under increasing levels of complexity. Application to a real \emph{Populus} dataset identifies three significant gene--geography interactions associated with leaf vascular architecture, providing new biological insights and establishing a broadly applicable methodological framework for high-dimensional complex image phenotypes.

---


### 61. [Dementia Etiology Diagnosis via Collaborative Meta Knowledge Enhancement](https://arxiv.org/abs/2607.22770)

**<font color=#1a73e8>作者：</font>** Siyuan Du, Mengxi Chen, Xinyang Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although artificial intelligence (AI) has shown promising performance in several medical tasks, accurate dementia etiology diagnosis with AI remains challenging due to complex overlapping symptoms among diseases. Scaling up the dataset size by combining the cross-center samples may bring a gain in the pursuit of performance, while the inherent data heterogeneity across centers or populations induces the conflict. Conventional multi-task learning paradigms offer a promising framework; however, they fail to consider critical meta information (e.g., site-specific acquisition and modality availability) to combat the heterogeneity. To address this challenge, we propose a Collaborative Meta Knowledge Enhancement (COME) framework for dementia etiology diagnosis, which injects multi-center acquisition semantics, source identifiers, and modality indicators as heterogeneity-aware embeddings into a unified Transformer architecture for scale-up training, enabling explicit modeling of heterogeneity. Besides, a trust-region constrained optimization scheme is designed to regularize the model from spurious correlations during training through a reference model. Across seven independent cohorts, our method achieves state-of-the-art in-domain performance with a mean macro-averaged AUC of 85.62% and a 4.29-point gain over the strongest baseline, while maintaining superior out-of-domain generalization under both cross-center and cross-sequence evaluations. Extensive validation also confirms the alignment between model predictions and established biomarkers (amyloid, tau) and clinical severity, highlighting the potential of COME to enable robust and interpretable dementia diagnostics in real-world settings.

---


### 62. [CC-AOS: Cost- and Horizon-Conditioned Amortized Backward Induction for Finite-Horizon Optimal Stopping](https://arxiv.org/abs/2607.22774)

**<font color=#1a73e8>作者：</font>** Tianwei Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite-horizon optimal stopping is a central problem in early time-series classification, where a system must decide at each sequence prefix whether the expected benefit of another observation justifies its acquisition cost. Existing data-driven backward-induction methods typically solve each cost-horizon operating point separately, so changing operating conditions requires repeated optimization and separate model stacks, making continuous cost adaptation and multi-horizon deployment inefficient. We propose CC-AOS (Cost- and Horizon-Conditioned Amortized Optimal Stopping), a structured amortized solver for a family of finite-horizon stopping problems with continuous costs and multiple horizons. CC-AOS learns a shared continuation-value model conditioned on the current state, absolute time, remaining horizon, and acquisition cost through joint amortized fitted backward induction. We establish that the exact value and continuation functions are nondecreasing, concave, and horizon-dependently Lipschitz in cost, encode these properties in the model architecture, and derive residual-based bounds on value and policy errors. Experiments on controlled Gaussian and time-varying non-Gaussian processes and the FordA engine-noise time-series benchmark compare CC-AOS with representative per-operating-point backward-induction solvers and tuned static stopping rules. At six unseen FordA cost-horizon pairs, one CC-AOS checkpoint achieved a lower terminal-risk-plus-sampling-cost objective than independently fitted Convex Function Learning at all six pairs, with an average reduction of 15.75 percent, while matching the tuned static thresholds on average.

---


### 63. [Predicting the Outcome of rTMS Depression Therapy using EEG Signals and CNN](https://arxiv.org/abs/2607.22776)

**<font color=#1a73e8>作者：</font>** Wael Korani, Md Fahimul Kabir Chowdhury, Sadam AlQadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repetitive transcranial magnetic stimulation (rTMS) is a non invasive therapy for Major Depressive Disorder (MDD). In this study, we generate images using two time frequency methods to represent EEG signals: Fourier-Bessel Series Expansion with Euclidean Distance (FBSE-ED) and Discrete Wavelet Transform (DWT). We propose an efficient deep learning classifier to predict the outcome of rTMS depression therapy. In this study, we use a private rTMS databases to train a lightweight custom Convolutional Neural Network (CNN) using 10-fold cross validation strategy in order to avoid any bias in our results. The results show that the FBSE-ED representation achieves the highest classification accuracy of 93.60\%, outperforming traditional time-frequency technique (DWT). In addition, the proposed architecture with FBSE-ED image representation technique outperforms more complex EEG-Specific deep learning models (EEGNet, DeepConvNet, SleepEEGNet) by 3.62-10.72% and pretrained models (Xception, DenseNet201, and MobileNetV2) by 23.03-27.35%. For more experiments, we utilize another private rTMS database as test database to show the robustness of the proposed model. Our results suggest that integrating advanced signal decomposition with deep learning can facilitate early prediction of rTMS treatment response and support more targeted clinical decision-making. The proposed framework is interpretable, computationally efficient, and well-suited for deployment in real-world local psychiatric clinics.

---


### 64. [LC-SEPLM: long-range contact-supervised adaptation for sequence-only protein representation learning](https://arxiv.org/abs/2607.22777)

**<font color=#1a73e8>作者：</font>** Chen Wang, Boming Kang, Qinghua Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models learn transferable sequence representations. However, because they primarily model contextual dependencies along amino-acid sequences, their training objectives do not explicitly constrain the model to learn three-dimensional residue contacts formed after folding . Here, we introduce LC-SEPLM (Long-range Contact-supervised ESM Protein Language Model), which adapts ESM2 with LoRA and long-range residue-pair contact supervision while retaining sequence-only downstream inference. Pair-specific queries use cross-attention over the complete sequence to extract global sequence context associated with long-range spatial contacts. To expose the model to diverse structural information, we trained LC-SEPLM on 500,000 AlphaFold Swiss-Prot proteins. In downstream evaluation, LC-SEPLM improved all eight protein-level tasks relative to ESM2. The largest gain occurred in remote-homology recognition, where macro-F1 increased from 0.6122 to 0.6769 (+0.0647, or 6.47 percentage points). On the official ESM-S EC benchmark, LC-SEPLM also outperformed ESM-S with a maximum absolute gain of 0.1771. These results support residue-pair contact supervision as a bounded route for introducing structural information into protein sequence representations while preserving sequence-only inference.

---


### 65. [What Softmax Throws Away: Mass-Aware Attention for Evidence Accumulation](https://arxiv.org/abs/2607.22781)

**<font color=#1a73e8>作者：</font>** Minwoo Yu, Young-guk Ha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High task performance does not show whether a model retains prediction-relevant structural information in its internal representation. Temporal graph models, for example, can achieve high future-link AUC while basic graph statistics remain difficult to recover from the same representation. We identify one source of this gap in the weighted averaging used by standard attention: when an evidence pattern is repeated, the numerator and denominator grow at the same rate, so inputs with different amounts of accumulated evidence can produce the same aggregate.
We propose Mass-Aware Attention (MAA), which generalizes standard L1 normalization to an Lp family. Under repetition, MAA makes the numerator and denominator scale at different rates, retaining the effective number of contributing inputs in the representation magnitude. It adds no supervision, parameters, hidden dimensions, or explicit count features, and recovers standard attention at p=1.
Across four continuous-time dynamic graph models and three datasets, MAA improves future-link AUC in 11 of 12 model-dataset cells. Linear recovery from the same hidden representation increases by 4.49% on average, and preferential-attachment recovery improves in all 12 cells after family-wise correction. We also observe consistent evidence in marked temporal point processes, temporal knowledge graphs, retrieval-augmented generation, and spatio-temporal point processes. Information accessibility and task utility remain distinct: NLL improves in MTPP, ranking is largely preserved in TKG, additional information in RAG does not improve the diagnostic head, and downstream LayerNorm can erase the signal in STPP. These results position MAA as a general normalization principle for improving predictor-facing representation informativeness by controlling repetition invariance in standard attention.

---


### 66. [Optimizing Transformer Neural Network for Real-Time Outlier Detection on FPGAs](https://arxiv.org/abs/2607.22786)

**<font color=#1a73e8>作者：</font>** Ilia Sobakinskikh, Paul Alexander Bilokon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we explore how the inference time of a Transformer Neural Network can be efficiently optimized with applications to real-time anomaly detection in financial time series. The financial time series are price series such as asset prices. Unfortunately, the data is often with errors or outliers that make the downstream data processing tasks useless, unstable or even harmful. Moreover, the amount of financial time-series data has been significantly increasing. Hence, there is a need for better data-cleaning methods in terms of accuracy and in terms of processing speed.
Transformers as a neural network architecture have achieved superior performances in many tasks such as Natural Language Processing and Computer Vision. Time series modelling and especially anomaly detection tasks can benefit from the features of transformers architecture in multiple ways, including the capacity to capture long-range dependencies and interactions.
Increasingly powerful hardware, such as field-programmable gate arrays (FPGAs), have seen increasing usage in recent years due to their reconfigurability and high performance. They can be efficiently utilized to speed up the computations of the Transformer architecture.
We explore different Transformer architectures for time series modelling and how they can be efficiently implemented on an FPGA board (PYNQ-Z2). In particular, we examine the application of Transformers to detect anomalies in time series and we show how they can be efficiently implemented on an FPGA board to minimize latency.
The code is available at this https URL

---


### 67. [FMOPF: Latent Flow Matching with Constraint-Aware Interaction Priors for AC Optimal Power Flow](https://arxiv.org/abs/2607.22788)

**<font color=#1a73e8>作者：</font>** Zhilin Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AC optimal power flow determines the minimum-cost generation dispatch under nonlinear power balance constraints and is solved thousands of times daily in electricity market operations. Learning a direct mapping from load conditions to OPF solutions can accelerate this computation, yet with deepening renewable penetration, a single optimal dispatch is no longer sufficient. Operators require a characterization of the distribution of feasible near-optimal solutions for risk quantification, sensitivity analysis, and multi-objective trade-off assessment. Supervised neural networks provide fast point predictions but cannot capture this conditional distribution. Diffusion-based generative models can sample diverse solutions in principle, yet existing methods operating in the raw state space exhibit degraded solution quality and fail to scale beyond medium-sized systems. We identify the root cause as the conflation of two distinct tasks within a single model. Compressing the high-dimensional OPF solution manifold is one task, and learning the conditional mapping from loads to that manifold is another. This paper presents FMOPF, a framework that resolves this conflation by decoupling compression from generation through latent flow matching and by explicitly modeling load-state coupling through a Constraint-Aware Interaction Prior Network. Experiments on four IEEE test systems demonstrate that FMOPF provides the most effective Newton-Raphson warm starts, achieves the lowest tail risk among generative methods, and is the first such method to scale to systems with several hundred buses while preserving full feasibility. Ablation studies confirm that the latent generation pipeline is a necessary condition for physical feasibility and that the interaction prior functions as a late-stage tail-risk controller.

---


### 68. [LithoFormer: A Robust Framework for Stratigraphic Inference via Transformers](https://arxiv.org/abs/2607.22804)

**<font color=#1a73e8>作者：</font>** Shwetha Salimath, Francesca Bugiotti, Sylvain Wlodarczyk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate geological characterization of subsurface reservoirs from well log data is essential to support projects such as carbon capture and storage (CCS), geothermal development, and extraction of natural resources. Existing automated techniques for geological characterization primarily use sliding-window classification, which limits their ability to understand broader geological contexts, often leading to misaligned formation layers. To overcome these limitations, we introduce LithoFormer, a robust framework for stratigraphic inference using a Seq2Seq transformer model that ingests entire multivariate well logs in a single pass. The framework utilizes a channel-independent PatchTST backbone enhanced with rotary positional embeddings (RoPE) to capture long-range geological dependencies across entire multivariate well logs. A decoupled multi-task head is employed to jointly predict geological zonation and precise boundary probabilities, while a geology-informed loss function enforces physical constraints such as the Law of Superposition. Validated and deployed on three real-world datasets, LithoFormer demonstrates a 90% reduction in median boundary error and eliminates stratigraphic order violations compared to traditional sliding-window baselines. It also achieves a 80% reduction in manual expert labor and eliminates stratigraphic inconsistencies, providing a scalable and reliable solution for large-scale subsurface modeling.

---


### 69. [OrchNAS: Orchestrated Neural Architecture Search Service for Personalised Federated Edge Intelligence](https://arxiv.org/abs/2607.22805)

**<font color=#1a73e8>作者：</font>** Keya Patel, Sajib Mistry, Sheik Mohammad Mostakim Fattah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose OrchNAS, an energy-aware, personalised, federated edge intelligence framework that leverages a Neural Architecture Search Service to automatically design service-adaptive models for heterogeneous edge environments. The framework orchestrates the architecture search process on a server-side NAS service, enabling edge services to derive personalised architectures under device-level energy, computation, and memory constraints. We introduce an energy-aware global architecture search mechanism that learns a compact global representation across heterogeneous services. We develop an energy-efficient architecture selection mechanism that enables each service to derive a personalised subnet that satisfies its resource constraints via a progressive, greedy, energy-aware pruning strategy. We propose an energy-efficient personalised model optimisation scheme that updates service-adaptive parameters while preserving global representations, where a primal-dual optimisation mechanism enforces strict energy budgets during architecture adaptation. Experiments on real-world and benchmark datasets demonstrate the effectiveness of the proposed approach.

---


### 70. [SLA-Constrained Carbon-Aware Routing in Geo-Distributed Serverless Clouds](https://arxiv.org/abs/2607.22806)

**<font color=#1a73e8>作者：</font>** Anmol Chaudhary, Rahul Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern cloud deployments distribute applications across multiple geographic regions, yet standard routing mechanisms prioritize latency while ignoring the fluctuating carbon intensity of local power grids. Latency-driven routing incurs avoidable carbon emissions, particularly when cleaner regions are within acceptable latency bounds. The proposed model formulates the carbon-aware serverless routing problem as a constrained optimization over geo-distributed cloud regions and introduces an SLA-constrained carbon-aware routing policy that achieves optimal carbon reduction within the SLA-feasible region, evaluated using real carbon intensity measurements across 5 primary AWS deployments. Experimental results show that the proposed policy achieves up to 46.8% carbon reduction while maintaining zero SLA violations across all evaluated thresholds. The system reduces carbon by an average of 27.4% under mixed workloads, and the routing overhead is very low (less than 0.02% of total request latency). A scalability study across 12 AWS regions spanning 6 continents demonstrates that average carbon savings increase from 27.4% to 47.5% as routing flexibility expands under mixed workloads. The proposed work contributes to SDG 13 (Climate Action) and SDG 7 (Affordable and Clean Energy) by enabling low-carbon routing decisions. These results indicate that cloud systems can achieve significant carbon savings without compromising user experience.

---


### 71. [Hybrid Semantic and Spectral Ensemble for Robust Synthetic Image Source Attribution](https://arxiv.org/abs/2607.22808)

**<font color=#1a73e8>作者：</font>** Md. Ajwad Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of text-to-image (T2I) models has necessitated robust Synthetic Image Source Attribution (SIA) methodologies. A critical challenge in SIA is the distribution shift between pristine training images and real-world deployed images, which undergo unknown post-processing operations such as JPEG compression and blurring. In this work, proposed for the DLMMDD Challenge at ICANN 2026, we introduce a dual-branch ensemble framework fusing Semantic Deep Learning with Mathematical Forensic Feature Extraction. The semantic branch employs EfficientNet-B0 regularized with Exponential Moving Averaging (EMA) and Label Smoothing. The forensic branch extracts 126 mathematical features -- including SVD spectral profiles and Local Binary Patterns -- from high-pass noise residuals, compressed via Truncated SVD and classified with XGBoost. Evaluated on a dataset of 10 generators where 55% of the test set is degraded, our approach achieves a private leaderboard accuracy of 95.60%. Furthermore, the entire pipeline is highly computationally efficient, requiring no GPU acceleration and executing end-to-end on a standard CPU in under 6.5 hours, highlighting the practicality and scalability of mathematical forensics for real-world deployment.

---


### 72. [From Hybrid Mechanistic--Data-Driven Modeling Toward Neuro-Symbolic AI: What, Why, and How](https://arxiv.org/abs/2607.22811)

**<font color=#1a73e8>作者：</font>** Moein E. Samadi, Andreas Schuppert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid mechanistic/data-driven models, which combine first-principles with learned components, are increasingly used in process engineering and scientific machine learning. Common hybrid modeling designs are specified primarily through their architectures and training losses, which offers a limited basis for a shared semantic interface to compare or verify them across domains, with comparatively little attention paid to epistemic uncertainty in the mechanistic part.
We bridge hybrid modeling and neuro-symbolic (NeSy) AI by reconstructing these designs as instances of NeSy interface. The resulting translation, Hybrid-to-NeSy (H2N), places mechanistic knowledge on the language side, learned modules on the belief side, and validity domains together with constraints on the logic side. For each design, H2N then yields an explicit NeSy inference functional and a logic-belief decomposition.
From this decomposition we derive two metrics: structural violation rate (SVR), measuring whether the learned belief respects the mechanistic structure; and belief dispersion (BD), measuring how concentrated the learned plausibility is, serving as a hybrid model's epistemic uncertainty in its mechanistic part. We instantiate H2N on a case study of a structured hybrid model for binary classification under label noise and show that models with higher SVR and BD exhibit greater variability in held-out accuracy. Under structural distribution shift, H2N further quantifies a model's uncertainty during extrapolations, whereas test accuracy reveals the same shift only post hoc.

---


### 73. [GeoTEAM: A Geospatial Tangible User Interface for Exploration and Visual Analysis of Migration Data](https://arxiv.org/abs/2607.22825)

**<font color=#1a73e8>作者：</font>** Karen Penaranda Valdivia, Nujaimah Ahmed, Aswah Butt 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Migration studies is an interdisciplinary field, requiring collaboration between researchers with varying levels of geospatial and quantitative data literacy. Geospatial tangible user interfaces (GTUIs) offer promising opportunities for embodied and collaborative spatial exploration of migration data. Few GTUIs, however, provide real-time visual feedback of data values to help users collaboratively identify trends. To address this gap, we present GeoTEAM, a novel tangible system for real-time, dynamic regional exploration, co-designed with migration and HCI researchers. GeoTEAM features active tangible dials with built-in touchscreens designed to control time and navigate map layers for net migration and various environmental sub-drivers in a multi-surface environment with tabletop and wall displays. We evaluated this system with nine pairs of researchers possessing multi-expertise in geospatial data literacy. Qualitative findings show that our system promotes collaboration, intuitive sense-making, and increased user confidence, enabled by physical interaction and real-time feedback from the active tangibles.

---


### 74. [Disentangling Multi-View Scanning in Mamba for Network Traffic Anomaly Detection](https://arxiv.org/abs/2607.22829)

**<font color=#1a73e8>作者：</font>** Xinglin Lian, Chengtai Cao, Ting Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Network Traffic Anomaly Detection (NTAD) is a critical task in cybersecurity, yet timely and accurate anomaly detection remains challenging. Mamba has emerged as a particularly promising backbone for NTAD due to its linear-time complexity for long-sequence modeling. It further incorporates a dedicated multi-view scanning mechanism to enhance detection precision through complementary contextual cues. However, we identify a previously overlooked structural deficiency in multi-view Mamba scanning for NTAD: redundancy accumulation. Specifically, distinct scanning branches capture substantial view-invariant information, which is repeatedly amplified during multi-view fusion; conversely, view-specific information is diluted or even suppressed, leading to representation homogenization and multi-view degradation. To address this problem, we propose DisenMamba, a novel disentangled multi-view Mamba framework. DisenMamba reformulates multi-view scanning as a two-stage disentangle-then-fuse process that explicitly separates view-invariant and view-specific components prior to fusion. This design prevents the invariant information accumulation while preserving complementary multi-view cues, yielding more discriminative representations for subtle traffic anomalies. Extensive experiments demonstrate the effectiveness of DisenMamba, establishing a new disentangled multi-view Mamba paradigm. Code is available at this https URL.

---


### 75. [ID-V2V: Identity-Preserving Video Restylization](https://arxiv.org/abs/2607.22830)

**<font color=#1a73e8>作者：</font>** Yuancheng Xu, Mingming He, Pablo Salamanca 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In visual storytelling, human performances are central to creative intent and narrative meaning. However, preserving human identity and performance while enabling flexible visual edits remains challenging for generative video models. We formalize this challenge as identity-preserving video restylization, which propagates scene, lighting, and style changes specified by an edited keyframe across a source video, while preserving facial likeness and performance, including expressions, eye gaze, and lip synchronization. A key obstacle is the absence of paired training data, as identity-preserving restylized video pairs are rare in real-world settings. To address this, we propose a decoupling of source-grounded identity preservation and edit-driven video synthesis. Our key insight is that facial appearance and expression should remain invariant, with illumination being the primary permissible variation. We therefore cast identity preservation as a video relighting problem, while modeling visual edit propagation as controlled video synthesis guided by the edited keyframe. Building on this formulation, we introduce ID-V2V, a video-to-video generative framework integrating complementary control signals: relit facial regions and facial normal maps tightly constrain facial likeness and performance, while edited keyframes and depth sequences enable flexible and temporally coherent generation. This design enables constructing training pairs from a single video, eliminating the need for scarce paired data. Extensive experiments demonstrate that ID-V2V significantly outperforms existing methods in preserving facial likeness and fine-grained facial performance, supports both single- and multi-subject scenarios, and delivers high visual quality, highlighting its potential as a human-centric tool for real-world content production. The code is available at: this https URL.

---


### 76. [MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution](https://arxiv.org/abs/2607.22832)

**<font color=#1a73e8>作者：</font>** Alkis Sygkounas, Victor Aregbede, Amy Loutfi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon embodied tasks require policies that execute many dependent actions before task success can be observed. Representing policies as executable control pro- grams (code-as-policy) enables their decision logic to be inspected and revised after rollout evaluation. Revised programs can then be executed and compared by rollout performance, framing policy improvement as execution-guided program search. Evo- lutionary methods driven by large language models (LLMs) provide a natural mecha- nism for this search by generating variants and selecting high-performing candidates. However, existing approaches primarily select among independently generated vari- ants and lack a sequential local improvement phase. We introduce MEMENTO, a memory-guided single-elite memetic framework for code-as-policy evolution. ME- MENTO first evolves a rollout evaluator that maps policy rollouts to scalar fitness and structured feedback metrics. Fitness selects accepted candidates and the next elite, while feedback metrics condition policy proposals generated by memory-guided hill-climbing, macro-mutation, and crossover. We evaluate MEMENTO on two long- horizon embodied domains: Robosuite Franka Tower-of-Hanoi manipulation and AI2- THOR household interaction. MEMENTO outperforms Eureka and REvolve, adapted as code-as-policy evolutionary baselines, in task success and generalization to held- out Robosuite object configurations and unseen AI2-THOR scenes. Ablations show that zero-shot generation and unevolved evaluators fail to solve either domain, and that removing policy-search branches reduces performance. Finally, we deploy the best-evolved Robosuite policy on a physical Franka robot, demonstrating the feasibil- ity of sim-to-real transfer of the evolved code-as-policy. Code, prompts, and videos are available at: this https URL.

---


### 77. [Gaze-Anchored Social Net: Decoding Implicit Relations via Joint Modeling](https://arxiv.org/abs/2607.22847)

**<font color=#1a73e8>作者：</font>** Yuqi Hou, Zhuo Chen, Han Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human gaze does more than point to visual targets; it serves as a subtle indicator of social intent within static images, whereas standard models typically process individuals independently, treating gaze as an i.i.d. quantity or predicting social semantics in isolation. Recent multi-person methods attempt to address this but often treat social relations as rigid, post-hoc classifications decoupled from the gaze estimation process. This oversimplification fails to capture the nuanced nature of social intent, which acts as an underlying driver of gaze behavior rather than a secondary categorical output. We address these limitations by proposing ANCHOR, a target-centric paradigm designed to decode gaze-anchored social intent by modeling the joint distribution of visual attention and latent implicit relations. Our approach surfaces these dependencies as the latent structural scaffolding of gaze behavior. The architecture utilizes a relational attention mechanism to capture fine-grained interpersonal links, leveraging feature-wise modulation for efficient multi-person parsing from a single vision backbone. To stabilize the training of this coupled formulation, we implement an optimization synergy to resolve the inherent conflicts between spatial gaze accuracy and latent social reasoning. This approach ensures robust generalization by seeking stable, flat minima while simultaneously harmonizing competing task gradients. We validate our framework on an extended benchmark featuring dense multi-person annotations and novel social influence rankings. Our results demonstrate state-of-the-art performance and provide the first quantitative evidence that implicit social hierarchies can be robustly disentangled and learned directly from static gaze patterns.

---


### 78. [Validation of a Real-Time Manual Wheelchair Simulator through Biomechanical and Perceptual Measures: A Comparison with Overground Propulsion](https://arxiv.org/abs/2607.22851)

**<font color=#1a73e8>作者：</font>** Ateayeh Bayat, Félix Chénier  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Purpose: Manual wheelchair simulators can provide a safe and controlled environment for propulsion training, biofeedback, and biomechanical assessment. However, their ecological validity must be established to ensure that simulator-based outcomes reflect overground propulsion. This study aimed to evaluate the ecological validity of a real-time manual wheelchair simulator by comparing biomechanical and perceptual outcomes during matched overground and simulator tasks. Materials and Methods: Thirteen participants (10 able-bodied individuals, 3 experienced manual wheelchair users), performed propulsion tasks overground and on the simulator. Task segments included straight-line propulsion, acceleration, turning, ascending, and descending. Biomechanical outcomes were collected using instrumented wheels and compared between environments using temporal, kinetic, and waveform-based measures. Perceived realism and user experience were assessed using task-specific realism ratings, a post-test questionnaire, and semi-structured interviews. Results: Temporal variables showed relatively small differences between overground and simulator propulsion, whereas kinetic variables showed larger discrepancies, consistent with previous simulator comparisons. Waveform patterns for force, moment, and power demonstrated high similarity between environments. Participants generally reported positive perceptions of realism, safety, and satisfaction, and highlighted the value of practicing wheelchair skills in a controlled environment. Conclusion: The simulator demonstrated partial ecological validity, particularly for temporal and waveform-based propulsion outcomes. Its ability to accommodate the user's own wheelchair configuration may help preserve ergonomics and enhance realism, supporting its potential use as an assistive technology tool for manual wheelchair propulsion training.

---


### 79. [Coordinated Networking for On-Device Agent-Augmented Real-Time Communication](https://arxiv.org/abs/2607.22854)

**<font color=#1a73e8>作者：</font>** Goodsol Lee, Juheon Yi, Jinglu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are enabling a new paradigm of agent-augmented real-time communication (RTC), where humans focus on high-level collaboration, while agents autonomously retrieve, analyze, and generate information in real time to support their interactions. These apps enable new experiences across various domains: for example, when corporate employees co-author a legal document, their agents can discuss and draft on their behalf, sparing them the burden of manually reviewing each other's work. As existing cloud-based agents suffer from privacy risks and unscalable server costs, on-device agent-augmented RTC offers a promising alternative. However, this on-device paradigm introduces a new networking challenge: contention between concurrent traffic flows generated by humans (for live video streaming) and agents (for sending context files for analysis). We design HFS, a framework to ensure both high live video quality and low agent response latency in agent-augmented RTC apps. We achieve the goal through an app-guided multi-flow transport approach, where a unified app-layer orchestrator jointly controls the sending rates of live video and agent context flows based on their heterogeneous app requirements. Our prototype built atop WebRTC and this http URL demonstrates that HAFS outperforms baselines, achieving 1.5x higher video quality while reducing agent response time by 31%.

---


### 80. [PatiGonit22K: A Comprehensive Dataset for Solving Complex Bengali MWPs](https://arxiv.org/abs/2607.22859)

**<font color=#1a73e8>作者：</font>** Swastika Kundu, Azizul Hakim Fayaz, Tashreef Muhammad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical Word Problems (MWPs) are an important benchmark for evaluating natural language understanding and quantitative reasoning. Despite recent progress in high resource languages, Bengali remains underexplored due to the limited availability of large scale annotated datasets. In this work, we introduce PatiGonit22K, an expanded Bengali MWP dataset containing 22,441 problems, developed by extending the original PatiGonit dataset with a substantially larger collection of complex mathematical problems. The dataset includes both simple and multi operation equations, providing a balanced benchmark for evaluating mathematical reasoning across different difficulty levels. Each problem is carefully translated, annotated, culturally adapted, and verified to ensure linguistic consistency and mathematical correctness. By increasing both the scale and complexity of Bengali MWPs, PatiGonit22K provides a more comprehensive resource for future research on mathematical reasoning and educational NLP applications in low resource languages.

---


### 81. [What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents](https://arxiv.org/abs/2607.22868)

**<font color=#1a73e8>作者：</font>** Shawn Ray  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime guardrails act before irreversible tool calls, but their guarantees depend on what policy state is representable, what a judge observes, and whether intervention changes future behavior. We separate three questions. First, relative to fixed oracle predicates, a deterministic gate enforces exactly the nonempty safety policies whose good prefixes its register model recognizes; policy nontriviality is undecidable with two decrementable counters but in PSPACE for a separable monotone fragment. Second, under a fixed exogenous law, Neyman-Pearson gives the exact false-block/miss frontier and conformal calibration gives a finite-sample marginal certificate, possibly via block-all. Third, once blocking changes future proposals, static scores and ungated trajectories need not identify the closed-loop frontier; a specified finite controlled model instead yields an occupancy program. Bounded representation attacks add a robustness margin, so benign calibration alone does not transfer. Experiments target these distinctions through static diagnostics, controlled-model enumeration, representation rewrites, and paired closed-loop reruns.

---


### 82. [Same Predictions, Different Reasons: The Effect of Quantization on Model Explanations](https://arxiv.org/abs/2607.22872)

**<font color=#1a73e8>作者：</font>** Kazi Kamruzzaman Rabbi, Md. Zami Al Zunaed Farabe, M. Sohel Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) has become a practical solution for deploying deep learning models on resource-constrained edge devices by compressing high-precision floating-point weights into low-precision representations without requiring retraining. Past research has demonstrated that quantization largely preserves classification accuracy; however, whether it also preserves the model's internal reasoning remains an open question. This study presents a systematic evaluation on how static PTQ affects the interpretability / explainability of five widely used CNN architectures: VGG19, ResNet18, EfficientNet-B0, DenseNet161, and MobileNetV2 at INT8 and INT4 precision. We employ a dual interpretability framework that combines Grad-CAM for spatial attention analysis with LIME for input-level feature attribution, and systematically compare full-precision and quantized models on two binary classification datasets. Interpretability is evaluated using three complementary metrics: the Pearson correlation coefficient, structural similarity index, and top-20% IoU to capture distributional and structural variations in model explanations, supplemented by deletion/insertion faithfulness analysis. The results show that classification accuracy is not a reliable indicator of interpretability stability under reduced precision. DenseNet161 maintains strong feature consistency across both precision levels, whereas EfficientNet-B0, despite achieving competitive spatial attention and classification accuracy at INT8 precision, exhibits a substantial degradation in input-level feature attribution. These findings have direct implications for the trustworthy deployment of quantized models in applications with high interpretability requirements, demonstrating that architecture selection is as important as the quantization strategy.

---


### 83. [Spatial Prediction of Soil Microplastics and Organic Matter Using Graph Attention Networks](https://arxiv.org/abs/2607.22875)

**<font color=#1a73e8>作者：</font>** Anik Dev Nath, Md Al Amin, Bikash Kumar Paul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of soil microplastics and organic matter is essential to assess ecosystem health and support sustainable land use. This study presents a graph-based deep learning approach using Graph Attention Networks (GATs) to model spatial dependencies among 91 georeferenced soil samples. By incorporating spatial coordinates, soil properties, and land use data, a two-layer GAT architecture was developed to capture local interactions. The final model showed strong performance, achieving RMSEs of 625.06 ($R^2 = 0.87$) for microplastics and 0.43 ($R^2 = 0.91$) for organic matter. However, cross-validation results revealed limited generalization, probably due to the small sample size and sparse graph structure. These findings demonstrate the potential of GATs for spatial soil prediction and underscore the need for dense datasets and improved graph connectivity.

---


### 84. [Physical AI Governance: From Theory to Practice Across Life Cycle](https://arxiv.org/abs/2607.22877)

**<font color=#1a73e8>作者：</font>** Wang Yang, Shaobo Wang, Hongxuan Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the emergence of Physical AI, artificial intelligence is extending beyond screen-based applications to embodied systems that perceive, interact with, and act in the physical world. Unlike traditional AI, Physical AI operates under real-time safety constraints, continuously interacts with dynamic environments, and coexists with humans, introducing governance challenges that existing AI governance frameworks do not explicitly address. This paper presents a comprehensive survey of Physical AI governance from both scientific and operational perspectives. We synthesize existing governance principles and organize them into a unified governance framework tailored to physical AI systems. Building on this foundation, we propose a five-stage Physical AI lifecycle comprising research, design, data, model development, and deployment, and demonstrate how governance can be operationalized across each stage through concrete implementation practices. By connecting governance principles with engineering workflows, this survey provides a structured reference for researchers, developers, and policymakers to build Physical AI systems that are safe, trustworthy, and aligned with societal values.

---


### 85. [CHiPS: Character Histograms and Positional Signals for Lightweight Authorship Attribution in Romanian Texts](https://arxiv.org/abs/2607.22884)

**<font color=#1a73e8>作者：</font>** Sanda-Maria Avram, George C. Ţurcaş  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose CHiPS, a lightweight character-level authorship attribution method for Romanian texts. All reported experiments are closed-set: the true author is one of the candidate authors in the training data. CHiPS studies two complementary fingerprints of writing style: CH-SVM, a character-histogram classifier based on one-character marginal distributions, and FFT12-LR, a positional-signal classifier that represents selected characters and punctuation classes as impulse trains (binary indicator sequences over character positions) and extracts Fourier/Welch spectral descriptors. We also report CHiPS-F, a leakage-safe decision-level fusion variant, and an optional top-5 listwise reranker trained only on out-of-fold predictions. The method requires no tokenization, syntactic analysis, pretrained language model, or transformer fine-tuning, and it avoids character $n$-gram features with $n \geq 2$ in the histogram component. On a locked grouped ROST split comprising 400 files from 392 source-text groups, written by 10 authors, with source-text-level evaluation and grouped five-fold model selection, CHiPS-F reaches 0.9310 accuracy and 0.9341 macro-F1. A matched but unrestricted character 2--5-gram TF--IDF SVM comparator reaches 1.0000 accuracy and macro-F1 on the same held-out groups, so the contribution is not a claim of best possible classification accuracy. Instead, the experiments ask how far restricted, transparent character evidence can go under strict leakage control. On ROSTories-cleaned, a secondary ROST-overlapping corpus comprising 1,248 files from 1,240 source-text groups, written by 19 authors, the same protocol gives 0.8919 accuracy and 0.8708 macro-F1 for CHiPS-R.

---


### 86. [Reflections and Recommendations on AI Adoption Practice from a Mixed-Ability Research Group](https://arxiv.org/abs/2607.22886)

**<font color=#1a73e8>作者：</font>** Shalini Madan, Sreelakshmi Surabiyil Bindu, Veronica Pimenova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI tools have recently been rapidly adopted by academics in mixed-ability research teams for both personal and professional tasks. While previous work on adoption of AI-based workflows has focused on collaboration and productivity, the perceptions of AI use within research teams remains divided. Through qualitative analysis of interviews of the five members of our mixed-ability research team, we discuss the motivations, challenges, and practices surrounding the use of generative AI in our lab. We reflect on experiences that shaped recommendations for balanced AI use that enable mixed-ability team workflows: (1) managing disability tax & crip time, (2) homogenizing identity, (3) risk disclosure of private information, (4) self-experimentation and miscellaneous tasks, and (5) information seeking. We build upon these themes to present AI practice recommendations we established for our lab to promote AI workflow adoption while preserving agency and disability identity.

---


### 87. [Efficient Learning of Truncated Boolean Product Distributions: Influence to the Rescue](https://arxiv.org/abs/2607.22889)

**<font color=#1a73e8>作者：</font>** Rohan Chauhan, Ioannis Panageas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning the natural parameters $z \in \mathbb{R}^n$ of discrete distributions $\mu_z$ from independent samples constrained to a subset $S \subseteq \{0,1\}^n$ is a foundational challenge in high-dimensional statistics. Existing methods for efficiently estimating truncated Boolean product distributions, notably the work of [Fotakis et al' COLT'20, Algorithmica '22], require either strong local connectivity assumptions on $S$ -- a property denoted fatness -- or stringent anti-concentration assumptions and necessitate the total mass of the truncation set to be a constant with respect to $n$. Moreover, the results in [Fotakis et al' COLT'20, Algorithmica '22] suffer from sample complexities that scale as $\Omega(2^n)$ if the mass of $S$ is exponentially small in $n$.
In this work, we circumvent these limitations by analyzing the geometry of $S$ under the measure $\mu_z$. We refine the existing parameter estimation guarantees under the fatness assumption, improving the prior sample complexity to $O( \log n / \epsilon^2)$ for $\ell_\infty$-recovery, matching the untruncated minimax rate. We further generalize fatness using the notion of influence utilized in the analysis of Boolean functions and provide sufficient conditions for efficient inference. Notably, unlike previous work, our method does not require sampling at arbitrary parameterizations of the model. Lastly, we establish a theoretical lower bound demonstrating the sample complexity exhibits an intrinsic exponential dependence on the width of the model and the minimum distance between elements in the set.

---


### 88. [AdaKAN: A dual-branch adaptive Kolmogorov-Arnold network for medical image segmentation](https://arxiv.org/abs/2607.22891)

**<font color=#1a73e8>作者：</font>** Dalia Alzu'bi, Deep Bhattacharyya, Ali Ayub 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is a fundamental task in computer-aided diagnosis, yet it remains challenging due to the complexity of anatomical structures and the variability across imaging modalities. In this paper, we propose AdaKAN, an Adaptive Kolmogorov-Arnold Network (KAN) that synergistically integrates convolutional operations with a novel efficient KAN (EffiKAN) block, comprised of an efficient attention mechanism and an adaptive KAN (AdaptKAN) module. This module features a dual-branch design: one branch employs a KAN layer with Bernstein polynomial activations for globally smooth and stable function approximation, while the other branch performs channel-wise refinement through projection operations and adaptive scaling. AdaKAN adopts a U-shaped architecture that effectively captures both long-range dependencies and fine-grained local features, overcoming the limitations of conventional convolutional and Transformer-based segmentation models. Skip connections are employed to preserve spatial details during encoding and facilitate accurate reconstruction during decoding. Extensive experiments conducted on diverse medical imaging datasets demonstrate that AdaKAN achieves state-of-the-art performance in segmentation accuracy.

---


### 89. [How Well Can AI Generate Backlogs from App Mockups?](https://arxiv.org/abs/2607.22902)

**<font color=#1a73e8>作者：</font>** Andrea Lezcano Airaldi, Lourdes Romera, Walid Maalej  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Creating sprint backlogs requires considerable effort, as items such as epics, user stories, and tasks can be missed or inconsistently specified. We propose a multimodal approach to support backlog generation from visual app mockups, an artifact available at early project stages. We evaluate three prompting strategies on GPT-4o: a zero-shot baseline, Compositional Chain-of-Thought (CCoT) for vision-language reasoning, and a persona-driven prompt. We study seven app development projects across two countries and interview developers about the results. Overall, we observed that the baseline prompt favours recall over precision, whereas CCoT is more balanced, achieving average F1 scores of 52-66% for epics and user stories. Tasks were more challenging to generate accurately. Precision gains were most consistent when adding architectural context, particularly for backend tasks (precision gains up to 35%). Interviews with developers revealed that up to 26% of false positives were still considered useful, reflecting the creative and open-ended nature of backlog creation. To capture this, we propose a new measure called Revised Recall, which complements ground-truth evaluation with developer assessments. Our findings suggest that hybrid prompting with architectural context can assist backlog generation from early mockups, though results vary by item type and developer oversight remains necessary.

---


### 90. [Learning from the Descent Direction: Adaptive Gradient Descent under One-Sided Hölder Regularity](https://arxiv.org/abs/2607.22906)

**<font color=#1a73e8>作者：</font>** Arzu Ahmadova, Ismail Huseynov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adaptive gradient descent for continuously differentiable, possibly nonconvex objectives under one-sided Hölder regularity. Unlike classical Hölder- or Lipschitz-gradient assumptions, which control the full gradient variation, our condition bounds only the directional term appearing in the descent inequality. This can allow less conservative step sizes when large gradient changes are orthogonal to, or favorable along, the update direction. We propose an adaptive scalar-step method based on an estimate of positive one-sided Hölder curvature, combined with a simple sufficient-decrease safeguard. For nonconvex objectives on a convex region containing the accepted update segments, we prove an explicit best-iterate stationarity bound with a rate determined by the Hölder exponent. Unlike predetermined diminishing step-size schemes, the method adapts to the local descent geometry. We evaluate the approach on two full-batch benchmarks designed to separate directional curvature from full gradient variation. On a binary classification problem, the method achieves the lowest final cross-entropy, objective value, and gradient norm, together with the largest classification margin among the compared scalar gradient methods. On a nonconvex Hölder regression problem, it attains the lowest final objective gap and gradient norm. These results indicate that one-sided Hölder curvature is an effective adaptive step-size signal when full-gradient variation is inflated by directions that do not hinder descent.

---


### 91. [Beyond Directed Acyclic Graphs: Causal Zeros and Causal Differential Equations](https://arxiv.org/abs/2607.22910)

**<font color=#1a73e8>作者：</font>** Sergei V. Kalinin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pearl's structural causal model (SCM) framework, built on directed acyclic graphs (DAGs) and the do-calculus, is the dominant formal language for causal reasoning. Yet it carries two structural restrictions: every relationship must be pre-specified as a directed causal edge, and feedback cycles are forbidden. This paper examines two classes of phenomena that strain these restrictions. First, symmetric physical and economic constraints, the ideal gas law being the canonical case, carry no intrinsic causal direction. Direction emerges only under intervention, and which variable is solved for must be specified as part of the intervention. We formalize such constraints as causal zeros within an Extended Causal Model by adding an activation operator, subject to local solvability and graph-admissibility conditions. Second, for the class of finite-propagation state-space systems considered here, we treat apparent instantaneous cycles as artifacts of suppressed time and ground both causal zeros and feedback in Causal Differential Equations (CDEs). In these, the transient regime is a time-unrolled acyclic causal process, and causal zeros arise as the defining functions of attracting equilibrium manifolds; periodic and chaotic attractors define further regimes of the same dynamics, treated through attractor-relative intervention. We give the extended do-calculus, identifiability conditions, counterfactual semantics, and open problems.

---


### 92. [Small-Pollinator Detection in Cluttered Field Video](https://arxiv.org/abs/2607.22913)

**<font color=#1a73e8>作者：</font>** Onur Onal, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting pollinators in field video is challenging: targets are small, visually similar, and observed against cluttered vegetation under blur and occlusion. We present a systematic empirical study of small-pollinator detection under a practical single-GPU compute budget. Using the BuzzSpot challenge dataset, we compare YOLO and RF-DETR models across input resolutions and evaluate sliced inference, class-gated fusion, size-routed ensembling, and post-hoc temporal processing. RF-DETR Large at 1344-pixel resolution achieved our best hidden-test result, reaching 0.405 mAP50:95 and outperforming the 1120-pixel model (0.379) and the best single-model YOLO26m baseline (0.366). The strongest gains came from adopting RF-DETR and increasing its input resolution, indicating that detector choice and input resolution were more effective levers than added inference-time complexity; the resolution gain was strongest for small objects and the rarer bumblebee and moth classes. Sliced-inference fusion, size-routed ensembling, and warm-started 1536-pixel continuation did not surpass this result, while post-hoc temporal processing did not improve the leaked diagnostic evaluation. Error analysis identified bee-hoverfly discrimination as the clearest remaining bottleneck: neighboring frames rarely supplied correctly classified hoverfly evidence for post-hoc correction. These findings motivate learned feature-level temporal aggregation before the final classification decision.

---


### 93. [Controlling Embedding Spaces with Text-Conditioned Transformations](https://arxiv.org/abs/2607.22919)

**<font color=#1a73e8>作者：</font>** Joseph Fioresi, Fabian Caba Heilbron, Pankaj Nathani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal embedding spaces in models like CLIP enable powerful capabilities such as semantic similarity retrieval and cross-modal zero-shot classification. These embeddings compress high-level semantics into a single vector, which comes at the cost of primarily expressing a dominant semantics like main object while suppressing other important attributes such as camera angle or color tone. We propose a text-conditioned transformation of visual embeddings that makes such attributes explicitly accessible. Given a natural language description of an attribute category (e.g., "color" or "art style"), a network generates an affine transformation that emphasizes the specified attribute. Conditioning on text enables it to learn many attributes simultaneously, accessing them at inference time through an intuitive interface. The network is trained to align transformed embeddings with the frozen latent space, enabling retrieval using existing large-scale embeddings without any re-encoding. When applied to a full set, the same mechanism transforms the latent space for attribute disentanglement tasks such as multi-clustering. By operating directly in latent space, our method provides a unified and efficient framework for controlling embedding spaces, demonstrating state-of-the-art performance across both attribute-based retrieval and multi-attribute organization tasks with near-zero inference cost. Project page: this https URL

---


### 94. [Simple Language Normalization Wins: Cross-Lingual Speaker Verification for the TidyVoice 2026 Challenge](https://arxiv.org/abs/2607.22923)

**<font color=#1a73e8>作者：</font>** Nina Hosseini-Kivanani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual mismatch remains a key source of overall degradation in modern speaker verification. The TidyVoice2026 Challenge targets this setting with text-independent verification, comprising 3,666 training and 808 development speakers in 40 languages and 2,200 evaluation speakers in 38 unseen languages, without language labels at test time. Starting from the official SimAM-ResNet34 baseline pretrained on VoxBlink2 and VoxCeleb2 and fine-tuned on TidyVoice, we revisit Nuisance Attribute Projection (NAP) as a simple language-normalization step in the embedding space. We estimate a compact language subspace from cross-language same-speaker differences and project embeddings onto its orthogonal complement before cosine scoring with Adaptive Symmetric score normalization. This reduces development EER from 2.97\% with cosine and 2.70\% with AS-Norm to 2.18\% and yields a Codabench evaluation score of 8.40, showing that simple back-end language normalization can rival more complex systems.

---


### 95. [Layering Virtual Try-On](https://arxiv.org/abs/2607.22924)

**<font color=#1a73e8>作者：</font>** Chun Feng, Bowei Chen, Mengyi Shan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the real world, fashion is about layering: adding a jacket over a shirt, or a sequence of adding and removing layers, rather than just a single-layer swap. This fundamental real-world task remains a challenge in existing Virtual Try-On (VTON) methods, which excel at single-layer replacement but are not designed to layer or de-layer an existing outfit. This paper proposes Layering Virtual Try-On (LVTON), a layering benchmark and method that preserves an existing outfit while enabling sequential layering. We find that current VTON paradigms are fundamentally ill-equipped for LVTON, as their reliance on cloth-agnostic representations and single-item datasets discards essential layering context. Our key insight is that the LVTON challenge must be disentangled into two distinct competencies: (1) General VTON Priors (e.g., deformation, identity preservation) and (2) Specific Layering Knowledge (e.g., layering order and occlusion reasoning). First, our model obtains general VTON priors by being trained on data produced by an automatic data generation pipeline that synthesizes samples from fashion videos via segmentation and inpainting. Second, the model is fine-tuned on a small, dedicated LVTON dataset to learn the layering logic. Our method achieves state-of-the-art results on our LVTON benchmark and demonstrates superior generalizability on traditional VTON benchmarks, setting new state-of-the-art results when fine-tuned and exhibiting zero-shot capabilities.

---


### 96. [Hidden Boundary Motion in Transformer Optimization: Function-Space Orthogonalization of Affine Weight and Bias Updates](https://arxiv.org/abs/2607.22927)

**<font color=#1a73e8>作者：</font>** Zhang Gongyue, Sheng Yixuan, Liu donghan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weights and biases are normally optimized as separate parameter tensors, yet they do not represent separate functions when the input to an affine layer has nonzero mean. For an affine map $z=Wx+b$ with input mean $\mu$, a weight update contains a sample-independent displacement $\Delta W\mu$ that is functionally indistinguishable from a bias update. We call this hidden contribution \emph{boundary motion} and decompose each update into a centered, sample-varying \emph{shape} component and a shared \emph{boundary} component. On a four-layer Transformer trained from scratch on IMDb, the bias-like term $g_b\mu^\top$ has a median norm equal to 0.664 of the raw weight-gradient norm across affine layers and training checkpoints. More strikingly, the median ratio $\norm{\Delta W\mu}/\norm{\Delta b}$ is 134.7, while $\norm{\Delta W\mu}/\norm{\Delta b+\Delta W\mu}$ is 0.994. Thus, under AdamW, the observed boundary motion is almost entirely realized through the weight matrix rather than the explicit bias.
We implement a diagnostic optimizer, Shape--Boundary Orthogonal AdamW (SBO-AdamW), that optimizes $g_W-g_b\mu^\top$ and $g_b$ with independent Adam states and compensates the weight-induced boundary displacement. In a single-seed experiment, SBO-AdamW raises validation accuracy from 81.68\% to 85.81\% and validation-selected test accuracy from 78.73\% to 82.73\%, with the best validation checkpoint occurring at step 800 instead of step 3000. However, the moving-batch-center compensation produces severe bias-coordinate drift and strongly reduces boundary energy. The present evidence therefore supports hidden boundary motion as an important optimization mechanism, but it does not yet establish a final general-purpose optimizer. A stable centered-affine parameterization is identified as the required next step.

---


### 97. [Design Theater: A Benchmark for Generative UI](https://arxiv.org/abs/2607.22928)

**<font color=#1a73e8>作者：</font>** Kashif Imteyaz, Kaif Imteyaz, Nakul Rajpal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative UI tools promise to democratize UI design by turning natural language descriptions into complete interfaces. Alongside the interface, these tools generate user-facing design rationales that explain their layout, accessibility, and design choices. However, it remains unclear whether these stated rationales are actually reflected in the interfaces they produce. We call this disconnect ``Design Theater'': plausible and confident design rationales that have little relationship to the actual implementation. To study this phenomenon, we introduce a benchmark and three metrics for measuring Design Theater. The benchmark includes 24 UI generation tasks spanning structural, styling, and functional design requirements. Using this benchmark, we evaluate 120 interfaces created by five generative UI tools. On average, over 25\% of user-facing design rationales are not implemented in the generated interface, and the implementation failure increases to 34\% for functional requirements. Tools recognize roughly half of the UX principles embedded in prompts (mean = 0.54), with four of five tools implementing 6\% or fewer functional principles. We also measure interface similarity across tools and find convergence in visual appearance and layout organization, with greater variation in color choices. Overall, we contribute: 1) the concept of Design Theater; 2) a benchmark with metrics for assessing whether the stated reasoning of generative UI tools is reflected in their implementations; 3) and findings from a systematic evaluation of these tools. We discuss what these findings mean for the design and evaluation of generative UI tools.

---


### 98. [Distribution-Specific Curvature Control with Finite-Sample Guarantees for Open-Weight Safety](https://arxiv.org/abs/2607.22929)

**<font color=#1a73e8>作者：</font>** Domenic Rosati, Ali Dadsetan, Hong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A short fine-tuning run can undo the safety guards of an open-weight model---retraining a refusal-trained assistant to aid weapons development or produce hate speech. Preventing such harmful fine-tuning while retaining benign adaptability remains difficult: the only prior method with an explicit curvature certificate, spectral deformation, inflates curvature globally and thereby obstructs benign adaptation along with harmful adaptation. We propose HarmAlign, which applies function-preserving spectral deformation along a estimated contrastive activation subspace. We derive finite-sample bounds for the estimated subspace energy and the resulting local harmful-distribution curvature lower bound. A stability--progress dichotomy for constant-step gradient descent turns the certified curvature into conditional convergence-rate control. Empirically, within a fixed-architecture, finite-budget first-order threat model, HarmAlign blocks direct fine-tuning and three data- or objective-adaptive attacks across a hazardous-knowledge relearning setting and a harmful-assistance fine-tuning setting, while the protected benign tasks remain trainable. The block persists across the tested first-order optimizer variants over every attack checkpoint, and under out-of-distribution harmful fine-tuning, and it extends to important cases in our threat model: accidental safety degradation and emergent misalignment.

---


### 99. [Spectral-Aware Analytic Class-Incremental Learning for Long-Tailed Distributions](https://arxiv.org/abs/2607.22931)

**<font color=#1a73e8>作者：</font>** Quyen Tran, Hai Nguyen, Quan Dao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analytic Continual Learning (ACL) offers a computationally efficient alternative to gradient-based approaches. Recent ACL methods are based on Recursive Least Squares (RLS) and have achieved the state-of-the-art results compared to other alternatives. However, they falter significantly in Class-Incremental Learning scenarios characterized by Long-Tailed distributions. While the ill-conditioning of the autocorrelation (Gram) matrix is a known limitation of RLS, we demonstrate that class imbalance exacerbates this issue into a distinct spectral pathology: "tail" classes suffer from severe spectral collapse, rendering their subspaces numerically indistinguishable from noise. Standard Ridge Regression ($L_2$) fails to address this effectively as it applies isotropic regularization - a uniform penalty that is insufficient to stabilize the tail without over-shrinking the head. To address this, we propose Geometry-Spectral Rectification (GSR), a theoretically grounded framework that treats long-tailed learning as a spectral regularization problem. Unlike standard isotropic regularization (Ridge) which uniformly penalizes all eigenvalues, GSR acts as an anisotropic spectral filter, selectively inflating the collapsed eigenvalues of tail classes. We construct a structured, data-dependent spectral perturbation matrix $\Delta$ that selectively inflates collapsed tail eigen-directions of the Gram matrix. Theoretical analysis proves that GSR guarantees an improved stable rank for the Gram matrix, ensuring numerical stability. Extensive experiments show that GSR establishes a new state-of-the-art for analytic CIL, offering a superior trade-off between computational efficiency and robust generalization in long-tailed settings.

---


### 100. [Discrepancy-Rounded Fair Bandits with Static and Time-Varying Exposure Floors](https://arxiv.org/abs/2607.22935)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Joyanta Jyoti Mondal, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimum-exposure constraints arise in recommendation, content curation, and regulated allocation when each provider, arm, or group must receive guaranteed exposure inside a period rather than only in aggregate. We study stochastic bandits with exact exposure floors and show that the right object is a rounding problem: a fractional fair schedule is realized as integral pulls, and the exposure error is exactly a discrepancy vector. The main contribution is a blockwise model with time-varying floors. BDQ-UCB satisfies every block floor deterministically and has fair regret governed by the nonmandatory budget $R$, not the horizon $T$, with high-probability regret $O(\sqrt{KR\log(KT)})$. A MOSS residual variant attains $O(\sqrt{KR})$, and a matching lower bound gives the minimax rate $\Theta(\sqrt{KR})$, even with positive mandatory exposure; a kl-UCB$^{++}$ residual rule adds instance-dependent optimality. The formulation becomes essential for overlapping group floors: per-arm rounding can violate a group constraint by $\Omega(s)$ in the group size, whereas Beck--Fiala null-space rounding meets every group floor within the block budget with violation below the arm degree $t$, and composes with UCB at the same $R$-parametrized regret. For learned group plans, we close disjoint systems at $\widetilde\Theta(\sqrt{KT})$, give a dual-ledger decomposition explaining why naive index rules fail under overlap, and prove a plan-sampling rule that is pathwise feasible under an initial cover-slack condition and attains a conditional $\widetilde O(\sqrt{KT})$ guarantee, leaving the condition-free overlap rate open. Experiments on synthetic floors, MovieLens-100k genre exposure, and deployment stress tests show exact feasibility without penalty tuning and regret competitive with tuned Lagrangian baselines.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
