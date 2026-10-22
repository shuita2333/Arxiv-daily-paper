# 📦 其他研究 | 2026年10月23日

> 本类共 **232** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-232](./part-05.md)

---

### 51. [Rethinking Time Series Tokenization from a Frequency Perspective](https://arxiv.org/abs/2610.28997)

**<font color=#1a73e8>作者：</font>** Zelong Tian, Ming Jin, Bo Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tokenization that partitions time series into subsequences has become a foundational paradigm in modern time series modeling. However, we find that current tokenization strategies inherently introduce spectral distortions, forcing the learned representations to diverge from the true underlying patterns such as trend, periodicity, and seasonality, thereby impairing model performance. Through theoretical analysis from a frequency perspective, we derive the boundary conditions under which such distortions occur. To overcome this distortion, we propose TimeFT, a nearly distortion-free frequency-based tokenizer for time series data. TimeFT obtains tokens through frequency-domain partitioning, frequency shifting, and Nyquist sampling. The method is parameter-free, incurs negligible computational complexity, and can serve as a drop-in replacement for existing tokenizers. Our extensive experiments on diverse tasks such as forecasting, classification, and anomaly detection demonstrate that TimeFT consistently and significantly improves performance.

---


### 52. [Enhancing Cross-Grade Generalization in Banana Variety Classification via Hybrid CNN-Transformers and Knowledge Self-Distillation](https://arxiv.org/abs/2610.29008)

**<font color=#1a73e8>作者：</font>** Khush Kataruka, Mohammad Muzammila, Zahid Akhtar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, automated fruit classification systems have become a more critical component in precision agriculture for efficient yield estimation, quality control, and supply chain optimization. However, they still face significant challenges under varying quality, fruit maturity, illumination, texture degradation, morphological attributes, domain shift, and post-harvest handling conditions. In this study, we address the challenging issue of cross-grade banana variety classification. This is a real-world setting where models that have been trained on specific quality grades must generalize to unseen grades to handle significant domain shift. Under a rigorous Leave-One-Grade-Out evaluation protocol, we present a thorough comparative analysis of CNNs, ViTs, and dual-stream hybrid architectures using a large-scale dataset of 31,678 banana images with three varieties and three quality grades. Specifically, to address the drawbacks of single-paradigm frameworks, we present a dual-stream Swin ResNet hybrid framework enhanced with KL-divergence-based self-distillation to align probabilistic feature representations across the CNN and Transformer streams. Comprehensive experimental analyzes show that the presented hybrid framework with KL-divergence based self-distillation achieves better overall performance, i.e., it attains a mean accuracy of 81.25% and significantly surpasses CNN and Transformer baseline models. Qualitative analysis further confirms that the hybrid framework in this study improves discriminative feature transferability, improves attention localization, and stabilizes optimization.

---


### 53. [Local and Sparse Kernel Operator Learning for Incompressible Flows: An Operator Lagrange Formulation](https://arxiv.org/abs/2610.29009)

**<font color=#1a73e8>作者：</font>** Ramansh Sharma, Matthew Lowery, Houman Owhadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a local and sparse kernel method for learning the solution operators of incompressible flows. It builds on our earlier property-preserving kernel method, whose global output reconstruction and dense operator regression scale poorly. Our method replaces the global output reconstruction by local divergence-free interpolants with divergence-free polynomials of any degree, solved in parallel on the GPU. These interpolants are divergence free, periodic on periodic domains, and, with a multiscale kernel, approach Kolmogorov statistics under refinement. A compactly supported kernel, positive semidefinite in any input dimension, makes the operator regression sparse. Its support radius, and hence the sparsity, is fitted to data, and optional affine polynomials in the input capture global trends. Operator Lagrange weights join the two. They cost one sparse solve per new input and act on the training fields before the output reconstruction, so their local coefficients are never formed. We show that, unlike direct evaluation, Lagrange evaluation does not amplify solve errors by the cancellation among spatial coefficients. On ten fluid benchmarks, validation selects sparse matrices nearly everywhere, with densities that mostly decrease as the training set grows, and affine augmentation lowers the error by more than an order of magnitude for forced isotropic turbulence. These sparse models are at least as accurate as our earlier dense method and more accurate than neural operators. Lagrange evaluation is as accurate as direct evaluation with local output reconstructions, and up to nearly three orders of magnitude more accurate with global ones. We also present GPU timings and storage.

---


### 54. [Dissimilarity-Based Markov Decision Processes for Stabilizing State Distributions](https://arxiv.org/abs/2610.29024)

**<font color=#1a73e8>作者：</font>** Xun Shen, Yuepeng Wang, Daniyal Sajedi-Hosseini 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for stochastic systems typically optimizes expected cumulative rewards, while reliable and repeatable behavior also depends on how the state distribution evolves over time. Optimizing expected return alone does not guarantee that this distribution converges to a desired target or remains stable. This paper develops a theoretical framework for learning policies that stabilize state distributions. We formulate the problem as a Dissimilarity-based Markov Decision Process (DMDP), in which the policy acts on the current state distribution and the objective measures its dissimilarity to a target distribution. We establish sufficient conditions under which the optimal policy makes the target distribution asymptotically stable. To support policy learning, we introduce a finite-dimensional representation of distributions and show how stability guarantees for its parameter dynamics extend to the underlying state distributions. We further develop certificates for the learned policies, including their deployment using estimated distribution parameters. These results quantify how learning and estimation errors affect the guarantees and identify conditions under which learned policies retain asymptotic stability. For practical implementation, we combine distribution estimates and target-dependent rewards with PPO and SAC. A computable example on a linear system illustrates the proposed theoretical certificates. Furthermore, experiments on a HalfCheetah task demonstrate the benefits of distribution feedback and explicit target matching for regulating the velocity distribution.

---


### 55. [Better Policies, Worse Verifier Audits](https://arxiv.org/abs/2610.29029)

**<font color=#1a73e8>作者：</font>** Daniel Cieślak, Jacek Łubiński  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verifier stacks increasingly sit inside post-training and test-time compute loops. We study a specific control loop: a component verifier is evaluated on fresh policy outputs against the full success label and refreshed when that aggregate score falls. For a conjunctive target $y = F \wedge M$, its on-policy AUC is $(1-q)A_{\mathrm{own}} + qA_{\mathrm{cross}}$, where $q = \Pr[F=1 \mid y=0]$. As the policy masters $F$, $q$ can rise toward one, removing weight from $F$-failures and rewarding information about $M$. We call this on-policy audit collapse. We derive a sharp identified set, a complete-erasure threshold, and the exact point at which the audit can prefer a worse component verifier; its population optimum is the full-outcome predictor, not the component oracle. An exact oracle exhibits the collapse, a natural multi-label text control shows inversion can select a head with lower canonical $F$-AUC at the observed failure mixture, and a prediction-registered ECG study shows that acting on the audit can reduce off-policy $F$-AUC, transfer the damage to an unseen generator, and increase downstream constraint violations. Preserving own-failure support prevents the damage. Matching label-complexity bounds and a controlled-mixture audit give the corresponding repair: audit the component on its own failures, and keep those failures in the refresh distribution.

---


### 56. [Gate Initialisation versus Recurrent Dropout and Zoneout in Learning Long Dependencies: A Controlled Study of LSTM and GRU Networks on Synthetic Tasks](https://arxiv.org/abs/2610.29034)

**<font color=#1a73e8>作者：</font>** Oleksandr Kholodniak, Oleksandr Prokhorov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dropout and zoneout are routinely added to long short-term memory (LSTM) and gated recurrent unit (GRU) networks, but, to our knowledge, their placements have not been crossed with gate initialisation in a factorial design, and it is not known whether early gradient propagation tells which runs will learn long dependencies. We trained one-layer LSTMs and GRUs on the adding problem and on delayed recall in a factorial grid of 720 runs, crossing conventional and chrono gate initialisation with up to six recurrent regulariser placements at one rate each, with pre-specified follow-ups, and recorded how sensitive the final hidden state was to the input at every lag. Because both tasks supply fresh or exhaustive training data, the study measures the regularisers' effects on optimisation and does not assess generalisation from a finite training set. At lengths chosen to make conventional initialisation difficult, all 360 chrono-initialised runs reached the validation criterion within 5000 updates, as did 119 of 120 unregularised runs with a horizon about four times too short or too long, whereas conventionally initialised networks learned slowly or did not reach the criterion within the budget at the longer lengths. Under conventional initialisation, dropout generally delayed learning and zoneout helped only in some conditions. The early input sensitivity added little to predicting which conditions learn once the early validation loss was modelled per task, architecture and initialisation. Within conditions, a flatter early decay went with the seeds that learned, but in a pre-specified test the association was modest (concordance 0.61), condition-dependent and not robust to resampling seeds. The results support chrono initialisation, even with a rough horizon, on such tasks.

---


### 57. [GRAIL: From Saliency to Semantics in Time-Series Explanation](https://arxiv.org/abs/2610.29036)

**<font color=#1a73e8>作者：</font>** Enver Menadjiev, Yiqiu Shen, Jaesik Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explaining a time-series model requires both locating the evidence and extracting meaningful knowledge from it. Yet a single timestep is not a semantic unit: the meaningful patterns live across many samples, not in any one of them. Per-timestep saliency is therefore noisy, high-dimensional, and unstable. Existing methods address this by introducing fixed-size windows and treating them as independent players in a cooperative game. Evaluating a coalition of such players requires defining a ``baseline'' region, which prior work tackles with fixed counterfactuals (e.g., a flat line, noise, or a spectral surrogate). This choice frequently dominates the resulting explanation, obscuring the model's true decisions.
To address these issues, we propose GRAIL, a region-based time-series explanation framework that uses domain-specific intervals, such as the P-wave and the QRS complex of an electrocardiogram (ECG) beat, as players. We describe each region with human-readable features and generate counterfactual baselines with an on-manifold conditional generator. Such a choice of players also admits non-temporal features: static covariates enter as singleton players attributed with the temporal regions on one scale, so a patient's tabular evidence (e.g., age, sex) is weighed directly against the signal. We attribute the predictions to the features via Owen values with common-random-number variance reduction. Experimental results on both synthetic and real data show that the proposed framework produces faithful and robust explanations, evaluated under matched on- and off-manifold operators, offering meaningful knowledge to domain experts.

---


### 58. [HumanCentric-Scenes-AI: A Human-Curated Multimodal Dataset of AI-Generated Human-Centric Scenes Across Surveillance, Occupational Portraits, AI-Edited Images, and Short-Form Video](https://arxiv.org/abs/2610.29045)

**<font color=#1a73e8>作者：</font>** Nima Kamali, Sana Nasiri, Negar Kamali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HumanCentric-Scenes-AI, a human-curated dataset of 296 AI-generated stimuli that depict people across four contexts in which people encounter AI-generated media. The Surveillance subset contains 85 AI-generated CCTV-style images. The Occupations subset contains 128 AI-generated occupational portraits in a balanced paired design covering 64 occupations with one female and one male version of each. The AI-edited subset contains 27 real photographs in which a region was altered or replaced by a generative model. The Video subset contains 56 AI-generated short videos. We curated the images and videos manually over multiple rounds to make them as photorealistic as possible. For each stimulus we release the file, the generation prompt where recorded, and per-stimulus metadata. We report depicted-gender distributions from an initial set of 134 generations without a specified gender and compare them with U.S. Bureau of Labor Statistics occupational gender shares. We report edit-region size and its association with zero-shot detection difficulty for the AI-edited subset. We report image-quality distributions for the Surveillance subset and subject-category coverage for the Video subset. HumanCentric-Scenes-AI is intended first for human-perception research, and also for calibration of AI-detection classifiers and bias analysis of generative models.

---


### 59. [Weakly Supervised Fish Segmentation through Point-Supervised Tracking and Motion-Informed Language](https://arxiv.org/abs/2610.29047)

**<font color=#1a73e8>作者：</font>** Vedanth Kallakuri, Katherine A. Skinner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the properties of fish populations is increasingly important. Analyzing fish length, width, and mass is integral to maintaining healthy stock in the aquaculture industry, while counting wild fish populations supports marine conservation and coastal reef restoration efforts. Deep learning-based segmentation models offer a promising means of obtaining such information at scale. Most of these models, however, require costly and time-consuming per-pixel segmentation labels for training, which can take up to two minutes per fish to annotate manually. To address this inefficiency, we propose a weakly supervised segmentation pipeline that requires only point-labeled data (one click per fish) to produce accurate segmentation masks. Our pipeline consists of four stages. First, a point-supervised tracker predicts point annotations for each frame. These points are then converted into motion-informed language expressions, which guide a language-conditioned segmentation model (LMPM++) to capture temporal consistency and produce candidate segmentation masks. Finally, optical flow and background subtraction are applied as post-processing filters to suppress noise from incorrect segmentations. Experiments on the DeepFish dataset show improvement in foreground mean intersection over union (mIoU) as compared to baseline models.

---


### 60. [ART-MPG: Autoregressive R/T Manifold Path Guiding](https://arxiv.org/abs/2610.29049)

**<font color=#1a73e8>作者：</font>** Zehao Zhao, Yanyang Yang, Xiaole Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specular chains concentrate important transport in small regions of path space and the structure depends on chain topology. We introduce ART-MPG, a compact neural model that samples chain length, an autoregressive reflection/transmission (R/T) string, and a direction from a topology-conditioned four-component von Mises-Fisher (vMF) mixture. We extend the repeated trial weighting in Manifold Path Guiding (MPG) by conditioning retry sampling on both chain length and the sampled R/T string, accounting for its known mass outside the stochastic re-hit trials. For a fixed proposal and target chain, this preserves the ideal expectation while reducing the expected retry count and reciprocal-estimator variance compared with retries conditioned on chain length alone. We distinguish the formal unbiasedness result from the capped and clamped renderer used in experiments. We evaluate fourteen scenes across a range of samples per pixel (SPP) against existing online and offline rendering algorithms. Our method consistently produces lower mean squared error at equal SPP than the online and offline baselines, with lower standard deviation across runs.

---


### 61. [OccJEPA: Occlusion as Masking for Amodal Video Segmentation](https://arxiv.org/abs/2610.29061)

**<font color=#1a73e8>作者：</font>** Genpei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Amodal video segmentation asks for the complete mask of an object in every frame, including the parts hidden behind other objects. The best current methods generate these masks with fine-tuned video diffusion models, which need many denoising steps and an extra depth network, and give a different answer for every sample. Self-supervised video world models of the JEPA family are trained on a closely related task: predicting the representation of masked space-time regions from the visible ones. We therefore treat occlusion as masking. The tokens that the object's visible mask does not cover are dropped, the pre-trained V-JEPA 2.1 predictor fills them in, and a light head decodes the observed and predicted features into amodal masks. The resulting model, OccJEPA (Occlusion-as-masking JEPA), is deterministic and 33.5x faster than the diffusion-based state of the art, and more accurate on SAIL-VOS, on TAO-Amodal, including a held-out test split (+4.00 AP50) and visible masks tracked by SAM2, and on Kubric. Controlled experiments trace the gain to the predictor's pre-trained weights rather than to its capacity, for world models from 87M to 1.85B parameters. Code is available at this https URL.

---


### 62. [Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection](https://arxiv.org/abs/2610.29063)

**<font color=#1a73e8>作者：</font>** Dongchan Cho, Jiho Han, Juwon Hwang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series anomalies take diverse forms, and individual detectors encode different anomaly scoring principles that rarely cover all anomaly types. Recent unsupervised time-series anomaly detectors provide complementary scoring signals, yet deploying them as an ensemble preserves the inference and maintenance cost of every individual detector. We study whether heterogeneous teacher detectors can be distilled into a single lightweight detector in the unsupervised setting, where no anomaly labels are available to define a shared target. AnoMix addresses this by extracting weak pairwise supervision from the training-set anomaly scores of frozen teachers. It normalizes each teacher score sequence independently and trains the student with CoRank, a multi-teacher ranking-distillation objective that converts teacher score gaps into pairwise supervision through teacher consensus. Across seven benchmark datasets, AnoMix successfully integrates complementary teacher scoring principles into a single deployable model, improving over individual detectors and static score ensembles while using a compact student with under 80k parameters on the benchmark settings. A zero-shot variant further shows that the distilled ranking signal transfers to unseen datasets and can outperform large pretrained time-series foundation models for anomaly detection.

---


### 63. [Value-Rectified Distillation for Flow-based Offline Reinforcement Learning](https://arxiv.org/abs/2610.29075)

**<font color=#1a73e8>作者：</font>** Ke Jiang, Wen Jiang, Yoshinobu Kawahara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We aim to address the problem of Out-of-Distribution (OOD) Mode Averaging, a critical problem that emerges when distilling Flow Matching (FM) based behavior policies in offline Reinforcement Learning (RL): When learning over multi-modal datasets, standard distillation inadvertently forces the policy to interpolate across different behavioral modes, causing the generated actions to collapse into invalid, OOD regions. To resolve this, we propose Value-Rectified Distillation (VRD), a novel framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem. By employing a dynamic coupling mechanism, VRD actively rectifies flow dynamics to explicitly decouple distinct behavioral modes, cleanly isolating high-value actions. Specifically, we instantiate VRD through two complementary algorithms: VRD-Q, which utilizes value-quantile behavior distillation to statistically filter out low-value behaviors, and VRD-R, which reorganizes the latent space to geometrically isolate high-value generative trajectories from the FM-based behavior policy. Extensive empirical evaluations demonstrate that VRD improves existing generative baselines across diverse continuous control and planning tasks on the D4RL, OGBench, and Minari benchmarks, especially over those multi-modal, non-expert datasets.

---


### 64. [Causal world models under physical parameter shifts](https://arxiv.org/abs/2610.29088)

**<font color=#1a73e8>作者：</font>** Chu Lin, Yi Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models predict how embodied systems evolve under actions, but their accuracy can degrade when physical conditions move outside the training distribution. We study two components of causal modeling: which inputs a predictor may use, and how its mechanism computes their effects. In a synthetic benchmark with shortcut features, a frozen dependency mask derived from paired interventions reduces mean out-of-distribution (OOD) RMSE from 1.769 for a fully connected predictor to 0.697, close to the generator-oracle mask (0.694). For robot link-mass extrapolation in CausalWorld, with disjoint training and test mass ranges, we develop finger-local world models in which link masses enter inertia and dynamics-bias terms through explicit affine coefficients, actions act through either a learned torque network or the known PD controller, and learned residuals capture contact-related effects. Compared with a separately trained control whose mass inputs are fixed at training means, the known-PD model turns out-of-range masses into a consistent predictive gain: median time-averaged joint R2 over 150-step rollouts rises from 0.609 to 0.727, with improvement in all ten task-seed runs (exact two-sided sign test, p = 0.002). In a shared 100-step forecast, the learned-torque model is competitive with the strongest recurrent robotic world model (RWM) configuration (median joint R2 of 0.755 - 0.768 versus 0.752), whereas supplying out-of-range masses sharply degrades the MLP and recurrent predictors. These results indicate that how a physical parameter enters the dynamics mechanism determines whether its out-of-range value helps or harms prediction.

---


### 65. [ReSeg: Retraining-free segmentation of abdominal organs via generalizable semantic representation learning](https://arxiv.org/abs/2610.29090)

**<font color=#1a73e8>作者：</font>** Derong Yu, Guoyan Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Abdominal organ segmentation is essential in modern medical applications. While existing deep learning approaches demonstrate promising performance, their heavy reliance on large-scale image data raises concerns over generalization capability and privacy risks. This motivates the development of generalizable segmentation training paradigms based on domain-randomized image synthesis, facilitating generalization across unseen real image domains. However, existing paradigms either suffer from limited segmentation performance when applied to abdominal organs, or require dataset-specific finetuning. To address these limitations, we propose ReSeg, a novel two-stage retraining-free framework for domain-agnostic zero-shot abdominal organ segmentation. At the first stage, our organ-agnostic synthetic data-driven pretraining approach exploits semantically and visually diverse synthetic images generated by a dedicated data engine to optimize a Generalizable Semantic Representation Network (GSRNet). The network is thereby capable of learning semantic features robust against variations in anatomical structure, imaging contrast, resolution and spatial context, which provide universal representation capabilities that serve as a foundation for segmentation learning. Subsequently, in the second stage, we continue to train an Organ-specific Encoder-decoder Segmentation Network (OESNet), whose encoder is initialized with the pretrained weights. This training process is facilitated by another dedicated data engine, which generates diversified visual images while strictly retaining the inherent spatial layout of abdominal organs. Comprehensive evaluation on seven abdominal organ segmentation datasets across three different modalities including CT, MRI, and PET demonstrates that ReSeg consistently outperforms existing state-of-the-art (SOTA) methods while eliminating the need for real training images.

---


### 66. [Context-Augmented, Session-Calibrated Blood Pressure Tracking from Photoplethysmography](https://arxiv.org/abs/2610.29091)

**<font color=#1a73e8>作者：</font>** Farouk Ganiyu Adewumi, Timothy Oladunni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> this http URL distinguish the contributions of acquisition context and photoplethysmography (PPG) to session-calibrated blood pressure (BP) this http URL. The original comparison used three repeats of five-fold participant-level cross-validation in 653 AuroraBP participants, excluding calibration-labelled prediction targets. Matched analyses separated context and PPG and removed elapsed-time terms. Later exploratory follow-ups retained PPG, accelerometer signals and three initial cuff readings. Separate studies evaluated pulse-rate fusion and an intraoperative VitalDB model. Main this http URL original wearable-state model achieved participant-level mean absolute errors (MAEs) of 7.697/6.139 mmHg for systolic/diastolic BP (SBP/DBP). Added context reduced MAE by 0.436/0.126 mmHg (97.5% intervals 0.305-0.573/0.053-0.200). In the matched factorial without the external PPG prior, PPG improved on calibration, time and protocol-provided posture/activity by 0.214/0.135 mmHg; removing time left the DBP interval including zero. Standard PPG descriptors contributed, but additional nonlinear/attractor benefit was not established. In a separate follow-up series, a sensor-history ensemble achieved 7.299/5.445 mmHg versus its static-rich reference's 7.363/5.470, small gains of 0.064/0.025 mmHg. Larger DBP errors did not improve uniformly. Quality-weighted fusion reduced pulse-rate MAE from 3.985 to 3.690 beats per minute. VitalDB MAEs remained 15.375/8.833 mmHg despite small PPG gains. Significance. The contribution is a calibrated evaluation framework with explicit controls, reproducible feature-cache-to-results analyses and retained negative findings. The sensor-history gain is exploratory after repeated dataset reuse. Independently estimated wearable states, complete raw-signal reproduction of the supplied richer features, external transfer and clinical adequacy remain unestablished.

---


### 67. [Multi-level Encoder with Global Topic for Task-oriented Dialogue Summarization](https://arxiv.org/abs/2610.29097)

**<font color=#1a73e8>作者：</font>** Zhuoqi He, Peijie Huang, Yuhong Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented dialogue summarization aims to automatically extract key information to generate domain summaries to improve service efficiency and quality. Task-oriented dialogue is inherently logical and surrounds specific topic. How to effectively capture the dialogue topic and the most salient information becomes one of the major challenges of this task. In this paper, we propose a task-oriented dialogue summarization model utilizing a multi-level encoder with global topic (MLEGT). This model discovers temporal and spatial dependencies through a multi-level encoder, while simultaneously obtaining a simple yet effective global topic in the process of graph construction. It not only captures the crucial details but also breaks the long-range limit and discover the intrinsic structure across the dialogue. Then, a global topic guided pointer mechanism is added into the summrizer to capture ignored but important information, which is helpful to improve the accuracy of the summary. A comprehensive study of two public datasets, including a real-world large-scale Chinese police interrogation dataset and a medical reporting service dataset proves the superiority of our method on several strong baselines.

---


### 68. [UNIVERS: Learning UNIversal Voxel-wise Embedding via Randomized Synthesis for generalizable one-shot landmark localization](https://arxiv.org/abs/2610.29098)

**<font color=#1a73e8>作者：</font>** Derong Yu, Qingsong Zhao, Yanbing Yue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-shot landmark localization in volume scans with varying fields of view (FOVs) is challenging. While existing self-supervised learning methods have shown promising performance, they rely on contrastive learning built upon augmented views of the same image, which inherently limits their generalization in cross-modality scenarios. This motivates research on cross-modality embedding learning using paired multi-modality images. However, existing methods suffer from not only limited training data, but also the requirement of multi-stage iterative training. To address these limitations, we propose UNIVERS, an end-to-end trainable framework that learns UNIversal Voxel-wise Embedding via Randomized Synthesis. Our framework leverages diverse pseudo-data synthesized from organ shape templates, with randomization applied to semantic layout, visual appearance, FOV, and spatial pose. Coupled with cross-domain discriminative voxel-wise contrastive learning, this domain randomization strategy forces the network to disregard domain-specific biases and learn features that are robust against variations in imaging contrast, resolution, and spatial context. Consequently, the trained model enables one-shot landmark localization in multi-modality volume scans with arbitrary FOVs. In this study, the efficacy of the proposed method is demonstrated by applying it to the task of localizing the adrenal glands, which are paired, small, and irregular endocrine organs. In particular, comprehensive experiments are conducted on three challenging adrenal gland datasets. The experimental results demonstrate that UNIVERS consistently outperforms the state-of-the-art (SOTA) one-shot landmark localization approaches, with particularly prominent advantages in cross-modality scenarios. The source code is publicly available at this https URL.

---


### 69. [Diffusion Posterior Sampling with Uncertain Forward Models](https://arxiv.org/abs/2610.29102)

**<font color=#1a73e8>作者：</font>** Wentao Shangguan, Vivek K Goyal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion posterior samplers reconstruct signals by combining a pretrained diffusion prior with a measurement likelihood specified by a forward model and a noise model. Calibration and reference data can characterize uncertainty in the forward model's parameters, such as blur kernels or detector responses. Fixing these parameters at estimated values leaves their uncertainty out of the likelihood, and parameter errors are thus absorbed into the reconstruction. We introduce an uncertainty-aware likelihood (UAL), a Gaussian approximation to the marginal likelihood obtained by integrating over the uncertain parameters. For each candidate signal, UAL propagates parameter uncertainty into a structured measurement covariance, reducing the quadratic penalty along residual directions that parameter variation can explain. Existing samplers can use UAL in their data updates while retaining their pretrained diffusion priors and sampling schedules. Under a fixed Gaussian nuisance model, we bound likelihood error from linearization and average divergence between the exact marginal and UAL posteriors. We compare samplers with and without UAL across six inverse problems spanning Gaussian and motion deblurring, CT, MRI, ultrasound, and fluorescence microscopy, and find improvements in reconstruction and ensemble prediction. UAL reduces geometric mean MSE by 9% to 20% across samplers in the main Gaussian-deblurring setting and by 51% to 92% in motion deblurring when non-blind samplers use the population-mean kernel. In motion deblurring, DAPS and PnP-DM with UAL also give 6.2 to 6.4 dB higher ensemble-mean PSNR than published BlindDPS and Fast Diffusion EM. On the ablation set, UAL outperforms trace-matched isotropic inflation for PnP-DM in both deblurring tasks; in motion deblurring, it also exceeds the best-tested fixed scalar data weighting by 3.3 dB for PnP-DM and 4.2 dB for DAPS in average PSNR.

---


### 70. [From Canon to Nikon: Camera Domain Shift and Potential Equity Implications in Retinal AI](https://arxiv.org/abs/2610.29104)

**<font color=#1a73e8>作者：</font>** Lisa Y.W. Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic retinopathy is a leading cause of preventable blindness, yet access to regular screening remains limited worldwide. AI offers a scalable approach, but its performance can be sensitive to image quality and acquisition conditions. In a Brazilian cohort of 8,524 patients, retinal images acquired with the Nikon NF5050 were more than twice as likely to have inadequate image quality compared with those acquired with the Canon CR-2, despite refurbished Canon systems costing more than twice as much as Nikon systems. This potential cost-quality trade-off highlights an important consideration for the reliability of AI systems deployed across heterogeneous imaging systems. Using a frozen pretrained retinal foundation model, we systematically evaluate whether camera-associated performance differences persist across 12 retinal disease classification tasks, four input resolutions, and five downstream classifiers. We find that camera-associated performance differences vary substantially across tasks, and that neither higher input resolution nor classifier choice consistently mitigates cross-camera variation. These findings identify camera platform as a potentially overlooked source of performance variability, with implications for the safety and reliability of retinal AI when deployed across heterogeneous imaging systems. We release all source code, evaluation scripts, and per-task results on GitHub to support reproducible benchmarking.

---


### 71. [DriftNeRF: Cross-Ray Density Drifting for Sparse-View Neural Radiance Fields](https://arxiv.org/abs/2610.29106)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Yihan Wang, Sheng'en Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural Radiance Fields (NeRF) synthesize photorealistic novel views from dense image collections, but degrade sharply when few views are available. We attribute a specific, measurable defect to the objective itself: the rendering loss is a sum over independent rays and contains no term comparing densities that different rays assign to the same region of space, so nearby 3D points can settle on contradictory densities while every training pixel is reproduced correctly. We make this quantity explicit by measuring cross-ray density disagreement directly during training, and show that it stays high in vanilla NeRF, falls only incidentally under frequency-based regularization, and moves together with held-out quality in the sparse regime. We then close the gap with DriftNeRF, a drop-in regularizer that instantiates the drifting-field template on density samples: a masked exponential kernel aggregates densities from nearby points on other rays into a stop-gradient consensus target, and the resulting drifting field penalizes unsupported disagreement while leaving agreed-upon boundaries intact. The regularizer reads only sampled positions, ray identifiers, and predicted densities, so it requires no pretrained model, external geometry, or additional images, and transfers across field parameterizations. On NeRF-Synthetic it reduces residual disagreement by an order of magnitude, and across NeRF-Synthetic, DTU, and LLFF it improves 3-view PSNR over the strongest MLP-NeRF baseline by 0.42-0.65 dB and remains competitive with sparse-view Gaussian pipelines under a matched protocol without their depth, flow, or covisibility preprocessing.

---


### 72. [PhyMo: Learning Physical Dynamics with Accurate and Continuous Motion from Multi-View Videos](https://arxiv.org/abs/2610.29107)

**<font color=#1a73e8>作者：</font>** Shangjia Liu, Jinxi Li, Siyuan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering dynamic 3D scene geometry, appearance, and the physical motion states that govern scene evolution from multi-view videos is important yet challenging. A key difficulty is that appearance can be deceptive. Under rendering supervision alone, a model may fit the observed images by changing color or opacity to compensate for inaccurate deformation, rather than recovering the true evolving geometry and motion. This issue is especially severe in scenes with fast or locally complex motion, where inaccurate trajectories can still produce plausible images over the observed frames, but lead to unreliable reconstruction and discontinuous future prediction. In this paper, we propose PhyMo, a framework for learning evolving dynamics from multi-view videos. We introduce a Motion-Aware Trajectory Representation that drives the model to recover accurate motion from deformation, rather than relying on appearance shortcuts to explain observed motion. On top of this, we propose a Continuous Motion Evolution module with bidirectional kinematic continuity constraint to promote temporally consistent evolution of displacement, velocity, and acceleration. Together, these designs yield geometrically faithful interpolation and continuous motion extrapolation. Experiments on four dynamic scene benchmarks demonstrate state-of-the-art performance.

---


### 73. [MHeatmap: Two-Walk Laplacian Reordering and Mosaic Layout for Rectangular Matrix Visualization](https://arxiv.org/abs/2610.29114)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Sheng'en Li, Liming Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weighted rectangular matrices record relations between two types of objects, such as occupations and industries, documents and terms, origins and destinations, or annotated classes and computed clusters. Their heatmaps become difficult to read when arbitrary row and column orders scatter related objects, while equal size cells hide large differences in row and column totals. We present MHeatmap (Mosaic Heatmap), which addresses these problems in two stages. Two-Walk spectral seriation first represents the matrix as a weighted bipartite graph. Ordinary bipartite ordering uses only observed row to column links. Two-Walk also uses length-two walks, so rows that share columns and columns that share rows receive explicit similarity links. Sorting a Fiedler vector of the resulting graph Laplacian gives coordinated row and column orders. The Mosaic layout then partitions a unit square so that row height is proportional to the row total and column width is proportional to the column total, while color represents the observed entry. We prove how the Two-Walk energy combines direct alignment with shared-neighbor smoothness, derive an exact matrix vector product that permits sparse computation, and formalize the tiling and area semantics of Mosaic. Across 300 synthetic matrices and seven real data sets, Two-Walk obtains the lowest normalized 2-SUM in all 15 synthetic regimes and the highest Band@10% in 14. The largest gains occur when shared neighborhoods express the latent relational structure.

---


### 74. [Two for One: Privileged Learning for Resource-Constrained Screening](https://arxiv.org/abs/2610.29126)

**<font color=#1a73e8>作者：</font>** Lisa Y.W. Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine learning systems are often developed under data-rich conditions but deployed when only incomplete information is available. A natural example arises in colour fundus photography (CFP), where both eyes are commonly imaged because they can provide complementary information for ocular disease assessment. Prior approaches that exploit bilateral information either fuse both eyes in a single model or use knowledge distillation to compress a dual-eye teacher into a lightweight student that still requires both images at test time. However, bilateral acquisition may not always be feasible. We thus propose a privileged learning framework in which a teacher model has access to bilateral CFP images during training and learns representations informed by information from both eyes, while the student is trained to transfer this knowledge from the bilateral teacher using only a single-eye image as input. At inference, the student operates exclusively on this single-eye input and does not require the contralateral image. Experimental results show consistent improvements in area under the receiver operating characteristic curve over conventional monocular training, with the largest gains observed for left-eye images for the detection of age-related macular degeneration (0.931 vs. 0.966) and diabetic retinopathy (0.789 vs. 0.836).%, while requiring only a single-eye image at inference. By enabling models to benefit from bilateral information during training while requiring only a single-eye image at inference, our approach may support more reliable deployment in resource-constrained clinical and screening environments.

---


### 75. [Mitigating Reward Hacking in Realistic Scenarios Through Representation Engineering](https://arxiv.org/abs/2610.29129)

**<font color=#1a73e8>作者：</font>** Austin Meek, Kyle Cox, Matthew Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward hacking is a major problem in current production machine learning systems, resulting in costly and dangerous failures. Here we study how to monitor for and mitigate reward hacking in realistic settings, including tool calls and long contexts. We apply a dynamic intervention to steering directions obtained by three different methods: difference-in-means vectors from labeled rollouts, gradient optimization-based vectors, and vectors extracted when models reference an anti-reward-hacking model spec. This dynamic intervention perturbs model representations less than uniform steering vector addition to the residual stream, allowing for more precise edits. We find that we are able to cheaply and significantly reduce reward hacking without correspondingly significant costs to model coherence or capability, and that steering vectors originally extracted from coding environments also generalize to reducing reward hacking in other domains. Our results pave the way towards latent space monitoring and control over realistic production systems.

---


### 76. [NormTune: Norm-Guided Parameter-Efficient Fine-Tuning for Reasoning-Intensive Tasks](https://arxiv.org/abs/2610.29134)

**<font color=#1a73e8>作者：</font>** Zhangming Li, Qinghao Hu, Weifan Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full fine-tuning has achieved remarkable success on reasoning-intensive tasks, but it often requires substantial GPU resource consumption. Parameter-efficient fine-tuning (PEFT) provides a promising alternative for reducing this cost, yet we observe a substantial performance gap on reasoning-intensive tasks. In this paper, we present three key observations showing that this gap is closely associated with norm-related under-adaptation, where PEFT produces markedly smaller weight-update norms than full fine-tuning. Based on these observations, we propose Norm-Guided Parameter-Efficient Fine-Tuning (NormTune), a simple yet effective strategy that adaptively strengthens insufficiently updated layers according to their weight-update norms. Extensive experiments show that NormTune consistently enhances multiple PEFT methods across challenging reasoning benchmarks. Specifically, when trained on S1K-1.1, integrating NormTune into rank-8 LoRA, Bone, and MoRA yields substantial average accuracy improvements of 24.24\%, 11.33\%, and 16.21\% , respectively, across AIME 2024, MATH 500, GPQA, and AIME 2025. Moreover, NormTune-enhanced rank-256 LoRA, Bone, and MoRA achieve performance comparable to S1 full fine-tuning, with respective average gains of 2.17\%, 0.93\%, and 3.00\% over this baseline.

---


### 77. [LaVGuard: Selective Decoding for Contextual Value Drift](https://arxiv.org/abs/2610.29135)

**<font color=#1a73e8>作者：</font>** Jiale Dai, Liuxian Ma, Hongcan Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A content-safe response can still promote priorities that conflict with its task: an assistant may demand compliance when asked to preserve autonomy. We study contextual value drift as a task-relative decoding problem with an explicit allowance for change. LaVGuard separates an authorized ten-dimensional profile from a frozen estimate of the values expressed in the visible prefix. A profile-relative density gate selects when to evaluate candidate continuations; their signed progress determines a logit tilt constrained by both changed-position and cumulative-KL budgets. We establish local surrogate improvement, pathwise budget feasibility, and a bound on response-distribution change. Profile conditioning raises boundary TPR at 5% FPR from .58 to .72. At the same .12 mean intervention ratio, the selection study reports risk-safety scores of .88 for LaVGuard and .72 for position-matched edits. The resulting interface makes task priorities actionable while keeping the extent of intervention explicit and bounded.

---


### 78. [DGCM-SSFA: Dual-Granularity Cross-Modulation and Sparse Strip Frequency Attention for Efficient 3T-to-7T MRI Synthesis](https://arxiv.org/abs/2610.29141)

**<font color=#1a73e8>作者：</font>** Zhichun Fan, Zhiqiang Chen, Lanling Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing high-fidelity 7T MRI from routinely acquired 3T scans offers a practical pathway to enhanced neuroimaging without the prohibitive cost of ultra-high-field scanners. While existing deep learning approaches have achieved promising results, state-of-the-art methods typically rely on either large-scale architectures exceeding 45 million parameters or computationally intensive ensemble strategies, limiting their practicality in resource-constrained clinical environments. In this work, we propose a compact multi-domain attention framework, termed DGCM-SSFA, that achieves competitive synthesis quality with only 11M parameters. The proposed architecture integrates two complementary modules into a U-Net Transformer backbone. First, a Dual-Granularity Cross-Modulated Feature Modulator (DGCM) is embedded at multiple hierarchical levels to enhance local edge and texture details through Sobel-guided spatial attention and depthwise frequency-aware channel attention with cross-branch gating. Second, a Sparse Strip Frequency Attention (SSFA) module at the bottleneck captures global spatial context via strip-pooled attention with near-linear complexity, while simultaneously performing FFT-based spectral modulation in the frequency domain. These two modules operate synergistically with the backbone's native channel attention, forming a triple-granularity feature refinement pipeline. Extensive experiments on the UNC and BNU 3T-to-7T MRI datasets across T1w and T2w modalities demonstrate that DGCM-SSFA achieves strong structural fidelity, attaining an SSIM of 0.8431 on BNU T2w---approaching the best benchmark value of 0.8624---and 0.8100 on BNU T1w, while using substantially fewer parameters than Transformer-based alternatives such as ResViT (123.4M) and FS-RWKV (45.4M).

---


### 79. [SICAF: Time-Varying Focus Bottleneck for Self-Supervised Event-Based Optical Flow with Spiking Neural Network](https://arxiv.org/abs/2610.29158)

**<font color=#1a73e8>作者：</font>** Shuangming Yang, Qing He, Shangqi Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based optical flow estimation achieves high temporal resolution and dynamic range by exploiting asynchronous events, while self-supervised learning provides an effective solution to the absence of ground-truth labels. Spiking neural networks (SNNs), as brain-inspired models, process information through asynchronous spikes, naturally aligning with optical flow events. However, the temporal irregularity across event streams hinders the compact extraction of spatiotemporal features, while the absence of explicit labels leads to spurious correlations, thereby increasing redundancy within latent representations. In this paper, we propose a novel 'Compactly Compress, Time-varying Focus' training strategy. We present SICAF (Spikes Information Compression And Focus) framework that formulates the learning process as a constrained optimization with temporal modulation. It encourages self-supervised SNNs to extract compact latent representations while preventing over-compression that would discard temporal saliency. To better enable feature selectivity across time steps, we design an estimator with learnable temporal attention, achieving context awareness with cross-time dependencies. Experimental results on several datasets demonstrate that SICAF achieves state-of-the-art performance in self-supervised SNNs, with a 8.14% improvement in AEE on the MVSEC dataset and a 13.49% increase in robustness under white-box adversarial attacks.

---


### 80. [RiO-DETRv2: Geometry-Aware Uncertainty Modeling Meets Real-Time Oriented Object Detection Transformer](https://arxiv.org/abs/2610.29159)

**<font color=#1a73e8>作者：</font>** Zhangchi Hu, Zilong He, Yifan Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RiO-DETR is the first real-time end-to-end transformer for oriented object detection, yet further localization gains require a more expressive box representation. Although distributional regression has succeeded in horizontal DETRs, extending it to oriented detection introduces geometry-misaligned boundary modeling and topology-inconsistent orientation refinement. We present RiO-DETRv2, a geometry-aware uncertainty modeling framework for real-time oriented object detection. To resolve the geometry mismatch, Object-Aligned Boundary Distribution Refinement represents box boundaries as probability distributions in an object-aligned coordinate system and progressively refines them across decoder layers. For better orientation topology consistency, we introduce Circular-to-Local Angular Residual Refinement that transitions from global periodic search to local fine-grained estimation. Unified OBB Quality-Aligned Learning further aligns classification, boundary and angular refinement with complete-OBB localization quality. Together, these designs improve localization without compromising efficiency, achieving a better balance between speed and accuracy. Specifically, RiO-DETRv2-l/x achieves 53.7/54.1 mAP50-95 on DOTA, outperforming RiO-DETR-l/x by 1.2/1.5 points with nearly unchanged computational cost. Code is available at this https URL.

---


### 81. [Carving Radiology Reports at Their Evidential Joints: Anatomical Region Sets as Generation Units](https://arxiv.org/abs/2610.29165)

**<font color=#1a73e8>作者：</font>** Jinwei Yang, Junhao Chen, Jianwei Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizing radiology reports into independently generated units offers a way to generate fine-grained clinical content and bind it to visual evidence. However, existing methods typically adopt generation-unit structures not directly specified in natural reports or their annotations, introducing additional modeling compromises. We propose RadCarve, which instead defines generation units directly from the anatomical region sets in existing statement-region correspondences, unifying unit formation with visual evidence selection. RadCarve's planner uses composition-specialized query banks to jointly predict unit existence and region composition from the image, iteratively refining both with regional evidence aggregated according to current membership predictions. The generator independently produces each unit's text conditioned on the joint visual evidence of its predicted region set. Compared with strong baselines, RadCarve improves CXRFEScore by 9.4% in unit generation given region sets and achieves 2.4 times the end-to-end binding F1. It also achieves leading report-generation results on Chest ImaGenome and PadChest-GR, using fewer than one-sixth as many parameters as large-scale baselines.

---


### 82. [Conditional Flow Models Convert Epistemic Uncertainty into Apparent Aleatoric Variance](https://arxiv.org/abs/2610.29172)

**<font color=#1a73e8>作者：</font>** Navodita Sharma, Abhishek Shetty, Max Simchowitz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional Flow Models (CFMs) are increasingly being used in place of deterministic predictors across machine learning, including for tasks that were classically formulated as regression. Given their success in such tasks, we ask the question: what useful information do the conditional distributions produced by CFMs carry beyond what a point predictor would provide?
We identify a systematic phenomenon: in many natural regimes, CFM samples routinely have larger variance than the true conditional distribution, even in nearly deterministic regression problems. This effect is most pronounced where the model has not resolved the dependence on the conditioning variable, and thus the additional variance can be viewed as converting epistemic uncertainty in fitting the ground truth conditional distribution into apparent aleatoric variance in the generated samples. Through controlled synthetic and real-data experiments, and comparisons with explicit smoothing estimators, we show that the induced variance tracks model underfitting of complex or hard-to-fit targets, and decreases with additional training or data. We provide a theoretical account of the phenomenon in a simplified setting and demonstrate a consequent practical use-case of conditional flow-matching: designing high-coverage predictive sets that cover the ground-truth regression target.

---


### 83. [Regular Syndrome Decoding Is Easier Than Previously Estimated](https://arxiv.org/abs/2610.29175)

**<font color=#1a73e8>作者：</font>** Jiseung Kim, Minkyu Kim, Changmin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Regular Syndrome Decoding (RSD) problem is a structured variant of classical Syndrome Decoding and underlies a growing number of efficient cryptographic constructions, including zero knowledge protocols, pseudorandom correlation generators, and MPC in the Head signatures. Although RSD is generally believed to be computationally hard, recent works have shown that algebraic attacks can outperform information set decoding on important RSD parameter regimes.
Building on this line of work, we revisit the concrete hardness of RSD and show that many widely used parameter sets are substantially easier to solve than previously estimated. This improvement stems from a refined hybrid algebraic attack that exposes and removes a previously overlooked source of concrete complexity: the joint blockwise placement of zero coordinate guesses and syndrome based variable eliminations. Rather than treating the two guessing stages and linear elimination as largely separate choices, our method coordinates them across all regular blocks so that the guessing penalty is balanced while sufficient equations are retained for linearization. This gives a systematic block balancing principle for the entire guess reduce solve pipeline.
We reassess several RSD based applications, including Ferret, Wolverine, and committed VOLE. Our estimates place at least one parameter set per application below its 128 bit target, with losses approaching 67 bits. On PCG benchmarks, we improve previous best attack costs by up to 29.77 and 25.91 bits over non binary and binary fields, respectively. Moreover, for the revised 128 bit PCG parameter sets of Liu et al. evaluated here, estimated attack costs are all below $2^{111}$ field operations. These results substantially revise the concrete security landscape of RSD and indicate that several existing parameter choices overestimate the hardness of their underlying RSD instances.

---


### 84. [Multi-Scale Latent Temporal Compression Attention and Video-Text Cross Attention Fusion for Video Action Detection](https://arxiv.org/abs/2610.29176)

**<font color=#1a73e8>作者：</font>** Yicheng Qiu, Keiji Yanai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In video action detection, modeling the temporal dependencies in continuous video streams is crucial. Previous methods based on deep neural networks can perform frame-level video recognition tasks. However, these methods struggle to model dynamic temporal patterns, facing challenges such as redundant frame information, difficulty balancing global and local features, and insufficient fusion of visual and textual features. To address these issues, we propose a video temporal attention module based on the Multi-Scale Latent Temporal Compression Attention, which aggregates continuous temporal sequences into feature representations across diverse temporal scales while efficiently reducing redundancy. We also introduce a Video-Text Cross Attention Fusion module that leverages cross-attention at both latent and standard feature levels, achieving fine-grained fusion between video and textual features to enhance semantic alignment and feature interaction. Experimental results across multiple video recognition benchmarks demonstrate that our proposed methods achieve superior performance compared to existing methods, validating the effectiveness and generalization capability.

---


### 85. [ROCOCO: Robust Outline Completion of Occluded Curvilinear Objects](https://arxiv.org/abs/2610.29177)

**<font color=#1a73e8>作者：</font>** Ken Zheng, Jaimyn Drake  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a learning-based generative model for completing curvilinear features under occlusion by environmental obstacles. To this end, we adopt a flow matching-based approach that supports the inpainting of occluded regions with the appropriate curvilinear features. To eliminate the reliance on privileged information about the occlusion a priori, we also train a UNet-based mask prediction model, which can identify regions for inpainting given only the occluded observation. The components of our approach are validated via experiments using procedurally-generated test cases, and the complete pipeline is validated using large public datasets for curvilinear objects. Against off-the-shelf inpainting baselines, ROCOCO is the strongest method by a wide margin when no occlusion mask is given, and is competitive with mask-supervised inpainting when one is, achieving best on full-image error and second only to LaMa on the occluded region, while using a completer of $7.7$M parameters against LaMa's $51$M and Stable Diffusion's $860$M.

---


### 86. [Truncated Out-of-Bag Probability Gain: A Noise-Robust Criterion for Random-Forest Wrapper Feature Selection](https://arxiv.org/abs/2610.29195)

**<font color=#1a73e8>作者：</font>** Sejong Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random-Forest wrapper feature selection can use out-of-bag (OOB) predictions as a built-in validation signal, but the criteria that decide each forward step accumulate OOB estimation noise. We propose TOP-Gain (Truncated Out-of-bag Probability Gain), which scores a candidate feature by the mean sample-level increase in the OOB probability of the true class, with decreases truncated at zero. Under a simple noise model, truncation removes about two-thirds of the noise variance contributed by unaffected samples while preserving the signal, and it makes the ranking of candidate features markedly more reproducible. In a pre-registered benchmark on 26 OpenML-CC18 datasets, TOP-Gain achieved the best mean rank in area under the ROC curve (ROC-AUC), accuracy and Macro-F1 among 15 methods; it was significantly better than 13 of 14 baselines and matched the accuracy of VSURF with 21 times less single-core computation. Within an identical wrapper, it selected significantly more stable feature sets than net-gain, Brier, log-loss and accuracy criteria without loss of accuracy. A confirmatory study on 24 further datasets replicated the advantage over all baselines. The accuracy gains were broad rather than tied to specific dataset characteristics, and, as pre-registered, the stability gain grew as relevant features became sparser

---


### 87. [NeuralSRender: G-Buffer Guided Video Diffusion for Sim-to-Real Rendering](https://arxiv.org/abs/2610.29200)

**<font color=#1a73e8>作者：</font>** Yipeng Lu, Youqi Liao, Zhenyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scarcity of high-quality annotated visual data remains a critical bottleneck for autonomous-driving perception. Simulators provide training data at scale, but the limited realism of synthetic videos compromises perception performance in real-world applications. To address this limitation, we propose NeuralSRender, a sim-to-real video translation framework that enhances the photorealism of synthetic videos while maintaining geometric consistency with the source scenes. Built on a pretrained video diffusion transformer (DiT), NeuralSRender uses a lightweight projector to inject geometric and material priors from G-buffers, and LoRA enables parameter-efficient adaptation. The model is trained in two stages: it first learns G-buffer conditioning from synthetic videos with accurate G-buffers, then adapts to real-world appearance using real videos with estimated G-buffers. During the second stage, an additional LoRA module is trained while the projector and first-stage LoRA remain frozen to reduce interference from estimation noise. NeuralSRender introduces only 1.45\% parameter overhead and can be trained on consumer-grade GPUs with 24 GB of memory. To support training and evaluation, we introduce GenReal, a large-scale driving video dataset comprising synthetic and real-world videos with corresponding G-buffers. Experiments demonstrate improved photorealism with competitive geometric consistency. Training perception models on our translated videos instead of raw simulator renders improves detection $\mathrm{AP}_{50}$ on nuImages from 35.1 to 40.6 and segmentation mIoU on Cityscapes from 32.4 to 40.8. Our code, data, and model weights are available at: this https URL.

---


### 88. [Understanding Target Probability Reuse in Speculative Decoding](https://arxiv.org/abs/2610.29210)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Giyoon Jang, Chailin Nam 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding uses a target model to verify a tree of draft tokens in parallel. We study whether the resulting next-token distributions can help select the next tree. For unrestricted target models, we show that guaranteed exact reuse requires a distribution computed at the next round's complete context. We characterize when retaining this distribution requires sacrificing accepted tokens and establish conditions under which this loss persists across decoding rounds. Across six targets, we find that reranking first-token branches with a separately computed distribution at the current context improves expected acceptance over draft ranking, especially with small tree budgets. Drawing the first token from this distribution before allocating the tree further improves expected acceptance over pruning a preselected tree, even at equal mean tree size. In our experiments, both selection rules also decode faster than draft ranking when the separate target pass overlaps standalone drafting. Our findings show that making target probabilities available before tree allocation can improve the efficiency of speculative decoding. Our code is available at this https URL.

---


### 89. [DetM-Tracker: Deterministic and Memory-Efficient VIS for Autonomous Industrial Inspection](https://arxiv.org/abs/2610.29212)

**<font color=#1a73e8>作者：</font>** You-Rui Lin, Jen-Chieh Wu, Tzu-Ti Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous industrial inspection requires strictly deterministic real-time inference under tight memory and computational constraints. However, existing Video Instance Segmentation (VIS) models suffer from prohibitive scaling: dense temporal memory grows with spatial resolution and sequence length, while fixed-capacity decoders fail to exploit the inherent sparsity of industrial scenes, creating a practical memory wall on resource-constrained edge platforms. We present DetM-Tracker, a streamlined VIS framework for autonomous industrial inspection, where target objects often exhibit highly similar appearance under constrained "micro" fields of view. DetM-Tracker eliminates architectural redundancy through three synergistic components: (1) Compact Scalar Memory, which condenses high-dimensional instance features into four-scalar descriptors, reducing temporal memory complexity from $O(T \cdot N \cdot R)$ to $O(T \cdot \hat{N})$. This mechanism effectively compresses frame-level representations into a bank of active instances, where $R$ denotes resolution, $N$ and $\hat{N}$ represent global and window-specific instance counts, respectively and $T$ the temporal window size; and (2) Dynamic Instance Channels, which adaptively allocate query capacity according to the actual number of visible objects; and (3) Entropy-Gated Skip Connection, which concentrates computational budget on high-uncertainty spatial regions to refine object boundaries in a single forward pass without auxiliary refinement heads. Our approach effectively bridges the gap between modern VIS models and the practical demands of industrial edge deployment, reducing inference latency by approximately 20$\times$ and VRAM consumption by 6$\times$ compared to state-of-the-art dense-feature baselines.

---


### 90. [PerSPL: Personalized Semi-supervised Preference Learning](https://arxiv.org/abs/2610.29219)

**<font color=#1a73e8>作者：</font>** Xiaoan Xu, Tingzhou Wei, Juncheng Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized reward models require user-specific preference comparisons, but collecting such feedback is costly and provides only limited supervision for each user. At the same time, large pools of responses can be generated without user identities or preference labels, yet existing personalized reward models leave this data unused. Directly learning from these responses is difficult because pairwise objectives constrain relative scores within a prompt, whereas pseudo-labeling individual responses requires scores that are comparable across prompts for the same user. We propose \textbf{PerSPL} (Personalized Semi-supervised Preference Learning), a backbone-agnostic framework that uses pair-mean score centering to stabilize this cross-prompt score coordinate and iteratively turns unlabeled responses into user-specific training signals. Against seven representative baselines across four benchmarks---PersonalLLM, HelpSteer2, Reddit TLDR, and Chatbot Arena---PerSPL achieves the highest reported mean accuracy among the evaluated methods for both seen and unseen users. The two latter benchmarks provide real-user preference comparisons in summarization and open-domain chatbot interaction, respectively. These results indicate that unlabeled responses can provide additional supervision for personalized reward modeling when per-user preference labels are scarce.

---


### 91. [Delay-Guided Attention for Quality Prediction in Multistage Manufacturing](https://arxiv.org/abs/2610.29220)

**<font color=#1a73e8>作者：</font>** Jiarui Zhang, Zhaoyang Guan, Zhixuan Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quality prediction in multistage manufacturing is challenging when inter-stage lags vary over time, as measurements taken at the same timestamp may reflect different process states. Existing approaches often preserve production order but fuse timestamp-aligned features or model delayed dependencies implicitly, without identifying the upstream history relevant to each downstream observation. We propose Delay-Guided Attention for Multi-stage Forecasting (DAMF), which explicitly estimates inter-stage lag distributions and uses them to guide cross-stage information transfer for final quality prediction. For each adjacent stage pair, a lag predictor compares the current downstream representation with candidate lagged upstream representations. An occurrence-magnitude factorization separately estimates the probability of a positive lag and its conditional magnitude, yielding a sample- and stage-pair-specific distribution over discrete lag states without requiring plant-specified delays at inference. DelayAlignment incorporates this soft distribution as a temporal prior into differentiable cross-stage attention, while gated residual fusion regulates information propagation across production stages. For interpretation, segment-wise Viterbi decoding converts pointwise lag distributions into temporally coherent lag paths, whereas forecasting retains the soft distributions for alignment. On the real-world LiquidSugar dataset, DAMF improves final quality prediction over the compared baselines. Evaluations on two controlled-delay benchmarks show more accurate and stable lag recovery, and ablation studies support the contributions of lag prediction, delay-guided attention, and structured temporal decoding.

---


### 92. [Cryptanalysis and Repair of "Decentralized Multi-authority ABE for NC$^1$ from BDH"](https://arxiv.org/abs/2610.29224)

**<font color=#1a73e8>作者：</font>** Xingwang Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a plaintext-recovery attack on the decentralized multi-authority attribute-based encryption construction of Datta, Komargodski, and Waters (Journal of Cryptology, 2023). The attack succeeds in the claimed static model with one corrupt authority and two users whose individual attribute sets remain unauthorized even when combined with the corrupt authority's attribute. The flaw is an incorrect extension of LSSS matrix-normalization invariance from complete secret shares to coordinate-wise ciphertext masks. A corrupt authority can expose these masks and remove identity binding from other users' decryption shares. We replace the coordinate-wise masks with independent full linear sharings of zero and prove static security under decisional bilinear Diffie-Hellman (DBDH) in the random oracle model. The repair retains the original matrix-width and row-labeling restrictions and leaves authority keys, user keys, decryption, and ciphertext size unchanged, while increasing encryption randomness and field arithmetic. We also give analogous attacks on both multi-authority attribute-based inner-product functional encryption constructions of Datta and Pal (PKC, 2023). The same modification restores correctness and matrix-substitution invariance for both variants. We prove static security of the repaired small-universe variant under asymmetric DBDH. For the large-universe variant, we identify a separate missing source-group encoding in the original reduction, formulate an augmented $L$-DBDH assumption, prove its hardness in the asymmetric generic bilinear group model, and give a static security reduction for the repaired scheme.

---


### 93. [From Scores to Safe Sets: Exact Safety--Constrained Decoding for Medication Recommendation](https://arxiv.org/abs/2610.29228)

**<font color=#1a73e8>作者：</font>** Animesh Agarwal, Meysam Ghaffari, Nina Fatehi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent generative medication recommendation systems ultimately produce sets of drugs, but drug--drug interaction (DDI) constraints depend on the set as a whole. A natural post-hoc approach is to first predict medications and then locally repair interacting pairs by removing one drug at a time. We ask whether this local repair step itself introduces avoidable error. Using fixed medication scores from FLAME's frozen classifier on MIMIC-III, we compare increasingly strong local repair strategies with an exact global decoder while holding the scores, output size, and DDI constraint fixed. The global decoder jointly selects the highest-scoring feasible medication set using mixed-integer linear programming. Across validation and test splits, global decoding consistently achieves higher Jaccard similarity than greedy repair, degree-aware repair, and degree-aware repair strengthened with exhaustive 1-swap local search. Its advantage is small under loose DDI constraints and becomes larger as the constraint tightens; on the test split it reaches +0.0064 Jaccard over the strongest local baseline at the strict DDI operating point. The finding also holds across a fine accuracy--DDI sweep at matched realized DDI exposure and under three score representations. At the strict setting, global decoding retains more true-positive medications while removing more false positives. These results show that medication recommendation is not only a representation-learning problem: even with a frozen clinical model, how its scores are converted into a constrained medication set can materially affect the final prediction.

---


### 94. [MA-UITD: Offline Multi-Agent Reward Inference for Characterizing Continuous Social Behavior](https://arxiv.org/abs/2610.29237)

**<font color=#1a73e8>作者：</font>** Zeyuan Zhang, Yiyun Yang, Yuan Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent inverse reinforcement learning offers a powerful framework not only for imitation learning but also for understanding the neural computations supporting social interactions and decision-making. Inferring rewards from interacting agents is challenging because observed choices reflect both personal preferences and expectations about others. Existing methods often require additional environment interaction, repeated policy optimization as an inner loop, or restrictive assumptions about environment dynamics and action spaces, limiting their applicability to fixed behavioral datasets. We introduce Multi-Agent Unilateral Inverse Temporal Difference Learning (MA-UITD), an offline method for inferring explicit agent-specific rewards from joint demonstrations in continuous-state environments with either discrete or bounded continuous actions. Its core idea is to represent the long-term consequences of each agent's own actions through belief-conditioned successor features that average over other agents' behavior. Shared reward features and agent-specific preference vectors connect these unilateral values to the target reward function, while inverse temporal-difference consistency and noise-contrastive behavioral learning enable inference without known dynamics or an inner policy-optimization loop. Across simulated cooperative, competitive, and general-sum tasks, MA-UITD outperforms baselines in discrete-action settings and infers behaviorally compatible reward profiles in continuous-action settings. When applied to experimentally collected social-foraging trajectories, MA-UITD inferred distinct spatial and interaction-dependent reward structures for leaders and followers, providing a quantitative characterization of latent behavioral objectives that may be relevant for understanding the neural computations underlying social behavior.

---


### 95. [ER-Chord: Spatially Consistent One-Step Image Editing via Equal-Energy Reliability Redistribution](https://arxiv.org/abs/2610.29248)

**<font color=#1a73e8>作者：</font>** Peize Li, Hanzhen Zhao, Xingguo Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step generative models enable fast text-guided image editing, yet they often introduce unintended changes to regions that should remain unchanged. Temporal aggregation stabilizes editing fields across noise levels, but leaves their spatial allocation insensitive to local variations in reliability. Consequently, temporal stability alone does not ensure spatially consistent editing. To address this lim- itation, we propose ER-Chord, a training-free and inversion-free framework for reliability-guided spatial redistribution. Our key insight is that agreement between editing fields at neighboring noise levels provides a local reliability signal for allocating editing strength. We formulate this allocation as an equal-energy op- timization that redistributes control energy according to local reliability while preserving the original editing directions and total control energy. This formu- lation admits a unique global solution that can be efficiently computed using existing field evaluations, requiring no additional denoiser calls. Experiments on two benchmarks, PIE-Bench and TEdBench, demonstrate improvements over state-of-the-art one-step editing baselines, achieving superior source preservation alongside consistent gains across multiple generative this http URL project page is at this https URL.

---


### 96. [MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents](https://arxiv.org/abs/2610.29249)

**<font color=#1a73e8>作者：</font>** Hong Ting Tsang, Boyi Zhang, Haoyu Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal assistants must remember not only what users say, but also what they show and convey. Existing long-term memory benchmarks are mostly text-and-image or report a single end-to-end score, so they cannot locate whether evidence is lost when it is represented, retrieved, delivered, or read. We introduce MOSAIC, a benchmark of 923 questions over persona-grounded histories of 11-24 sessions spanning text, image, video, and audio. MOSAIC constructs targeted spatial, temporal, and prosodic signals rather than decorative media, with the strongest causal validation for spatial information and selector-level validation for annotated prosody, and pairs them with a matched diagnostic protocol that freezes the question, reader, prompt, and budget while intervening on representation, retrieval, and delivery. Matched decomposition shows that representation loss is modality-dependent, residual reading dominates even under gold evidence, and abstention remains weak on these controls: strong answerable scores coexist with failures to refuse. MOSAIC thus turns omni-modal memory evaluation from a leaderboard into a diagnosis of write, retrieve, deliver, and read failures.

---


### 97. [Extending FAIR Principles with Observability for Trustworthy Federated Learning](https://arxiv.org/abs/2610.29252)

**<font color=#1a73e8>作者：</font>** Hangli Ge, Noboru Koshizuka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) keeps data at its source, but locality alone does not make a federation trustworthy. Without sufficient observability, an aggregator cannot determine whether the client service was healthy, the local data pipeline was trustworthy, or contractual constraints were properly monitored during training. We take the position that trustworthy FL needs an evidence plane in addition to its model-update process. Each participant continuously summarizes local infrastructure, data into minimal, signed trust evidence associated with each FL round, while raw data, logs remain local. A local TinyLLM may assist in interpreting observability signals, deriving contextual evidence, and providing natural-language explanations to operators. We instantiate this vision through FAIR-O, an observability extension of FAIR principle. Rather than benchmarking FL accuracy, a three-level trust model has been proposed and a two-participant Python prototype demonstrates evidence generation and trust assessment. We further discuss future integration of FAIR-O Trust Evidence into participant selection, evidence weighting, and federated aggregation.

---


### 98. [CRAB: Cuboid-based Representation for As-built BIM from Point Clouds](https://arxiv.org/abs/2610.29257)

**<font color=#1a73e8>作者：</font>** Haoran Xiong, Jing Wang, Shanshan Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As-built BIM reconstruction from point clouds demands semantic, volumetric, parametric, and editable building components, beyond 2D layouts or planar abstractions. Yet existing scan-to-BIM pipelines often rely on handcrafted rules, heuristic optimization, or manual correction, while learning-based methods fall short of recovering wall thickness, opening geometry, and component-level BIM structure. We introduce CRAB, a BIM-ready cuboid reconstruction framework that encodes walls, doors, windows, beams, and columns as compact architectural cuboids with IFC-compatible semantics and parameters. CRAB bridges point clouds and editable BIM by combining ProposalNet, which predicts coarse component cuboids, with AssemblyNet, a relation-aware Flow Matching model that refines geometry, predicts structural relationships, and enables automatic structural correction and human-guided editing. To address limited cuboid-level supervision, we extend Structured3D with component-wise cuboid annotations and construct cuboid-based procedural scenes. Experiments show CRAB surpasses floor plan and plane-based alternatives in component completeness, geometric accuracy, and generalization. For interior wall thickness estimation, CRAB achieves a mean error of 2.80 cm, with 79.50% of matched walls within 3 cm. The project page is available at this https URL.

---


### 99. [Estimating Performance for Safe Deployment of Machine Learning Models](https://arxiv.org/abs/2610.29262)

**<font color=#1a73e8>作者：</font>** Zeju Li, Konstantinos Kamnitsas, Mobarakol Islam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The main challenge in applying deep neural networks to real-world scenarios lies in distributional discrepancies between training and test datasets, often caused by variations in data acquisition conditions. Assessing the performance of pre-trained models without labels is crucial for safety, but this is complicated by deep models' overly optimistic probabilistic outputs, often exacerbated by class imbalances, leading to unreliable predictions. To address these issues, we introduce MOVAL, a novel MOdel eVALuation tool that estimates performance using unlabeled test data. MOVAL incorporates class-wise confidence calibration to adjust model outputs, allowing for the estimation of metrics beyond accuracy and mitigating the detrimental effects of class imbalance on confidence calibration. Additionally, we propose an ensemble approach that combines multiple calibrated confidence scores for a more robust solution. We validate MOVAL on natural and medical image datasets with various acquisition shifts, covering tasks from classification to segmentation. It achieves state-of-the-art results across evaluation metrics such as accuracy, F1-Score, AUC, and more. Furthermore, we demonstrate that MOVAL provides accurate performance estimations at the class, instance, and pixel levels, ensuring the transparent and safe deployment of machine learning models. We provide MOVAL as a deployment tool for monitoring and estimating performance under a range of domain shifts.

---


### 100. [Clinical radar heart sounds with echocardiographic phenotypes of ventricular dysfunction and valvular disease](https://arxiv.org/abs/2610.29267)

**<font color=#1a73e8>作者：</font>** Jinye Li, Qingchao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar heart sounds capture cardiac mechanical activity without contact, while echocardiography characterizes ventricular and valvular function. Paired measurements connect these signals to structural heart disease, yet such data remain sparsely represented in public resources. Here we present 537 radar heart-sound recordings paired with one echocardiographic report for each of 162 patients. The cohort covers three overlapping phenotypes: left ventricular ejection fraction (LVEF) below 50%, regional wall-motion abnormality and at least moderate valvular regurgitation, present in 38, 43 and 39 patients, respectively. Original complex signals, processed radar heart sounds and temporal quality segmentation support signal-to-phenotype analysis. Technical validation retains 95.93% of signal duration and confirms reproducible waveform reconstruction. Patient-level five-fold evaluation achieves a mean outer-test AUROC of $0.770\pm0.138$ for reduced LVEF, identifying mechanical information associated with ventricular systolic dysfunction. This resource supports research linking non-contact cardiac mechanical signals to echocardiographic structural and functional phenotypes.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-232](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
