# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 451. [On the Geometry of Multimodal Saturation: Riemannian VICReg](https://arxiv.org/abs/2610.06096)

**<font color=#1a73e8>作者：</font>** Nessim Ben Abbes, Duc Han Le, Sabri Mtibaa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In self-supervised learning, a third modality should improve, or at least preserve, performance. Across nine image-text-tabular datasets, we show that it instead harms performance: the trimodal model underperforms its own best bimodal subset in 55.6% of paired runs under VICReg. The same failure occurs in 51.1% of paired runs under SimSiam. We call this failure multimodal saturation. We propose that the failure lies in the alignment geometry. Riemannian VICReg (R-VICReg) generalizes classical VICReg: it aligns views by squared geodesic distance on learnable negative-curvature product factors and recovers VICReg exactly as curvature vanishes. Over the same 45 paired runs, R-VICReg raises the probability that the third modality helps from 44.4% to 64.4%, with gains concentrated where VICReg saturates.

---


### 452. [Benchmarking CLIP for Zero-Shot Face and Periocular Gender Estimation](https://arxiv.org/abs/2610.06102)

**<font color=#1a73e8>作者：</font>** Fernando Alonso-Fernandez, Kevin Hernandez-Diaz, Jose Maria Buades 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate CLIP for zero-shot gender estimation from full-face and periocular images. Three CLIP backbones are evaluated on 11,299 frontal images from Adience using image-text similarity with male/female prompts, achieving 95.54% full-face accuracy without task-specific training. For periocular, zero-shot predictions are strongly biased towards males, primarily due to a misaligned decision boundary. Threshold alignment substantially reduces this bias, reaching 85.29% accuracy. Linear SVMs trained on CLIP features provide only marginal gains, with a best periocular accuracy of 86.17%, approximately 2.8% above previous Adience results in the literature. Nevertheless, the gap with full-face performance confirms the greater difficulty of periocular gender estimation

---


### 453. [Mind the Drift: Diagonal Linear Networks Under Large Learning Rates](https://arxiv.org/abs/2610.06120)

**<font color=#1a73e8>作者：</font>** Aniket Sanyal, Tom Jacobs, Rebekka Burkholz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large learning rates can qualitatively change the trajectory of neural network training, often pushing optimization into regimes far from classical gradient-flow behavior. The Edge of Stability (EoS) offers a valuable lens on the dynamics such learning rates induce. We study corresponding dynamics in diagonal linear networks, where we uncover a competition between two distinct implicit biases that jointly determine the sparsity of the recovered solution in regression settings. Complementary to the Gain, which captures the average discretization error accumulated by Gradient Descent relative to Gradient Flow, we derive a closely associated but overlooked quantity: the Drift. Under large learning rates, it describes an imbalance between different discretization errors and represents a systematic shift in the optimization trajectory. While the Gain grows monotonically in certain regimes, and can bias towards denser, flatter interpolators, the impact of the Drift depends on its alignment with potential solutions, which can either counteract or reinforce the effect of the Gain. Consequently, its behavior drives model selection, particularly during early training epochs. To validate our theoretical insights, we introduce an intervention that actively steers the Gain to recover sharper, sparser solutions. Thus, our analysis reveals that large learning rates do not universally hinder the recovery of sparse solutions. On the contrary, they can be harnessed to control the implicit bias of training.

---


### 454. [Integrating Survival-Based Aging Models with Data-Driven RUL Prognostics](https://arxiv.org/abs/2610.06128)

**<font color=#1a73e8>作者：</font>** Abhishek Srinivasan, Juan Carlos Andresen, Sepideh Pashami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive maintenance requires reliable remaining useful life (RUL) estimation. Existing methods mainly follow two paradigms: wear-based aging models that capture cumulative degradation and sensor-driven data models that reflect instantaneous health conditions, each providing only partial information. In this work, we propose a probabilistic fusion framework that integrates wear-based and sensor-based prognostic components through failure probability distributions. Based on explicit structural assumptions linking wear, latent health, sensor observations, and failure, we derive a principled combination rule that enables uncertainty-aware integration with adaptive weighting of the components. Experimentally, we assess this combination rule by learning the wear-based component using a parametric survival model and the sensor-based component using a 1D convolutional neural network (1D-CNN) with a post-hoc uncertainty model. Evaluation on multiple N-CMAPSS datasets demonstrates that the fused model improves point accuracy, preserves the C-index, and produces narrower yet well-calibrated prediction intervals compared to either component alone. The results highlight the complementary roles of wear-based survival model and sensor-based deep learning model, and show that their probabilistic integration provides a structured pathway toward more robust and consistent prognostics over the life-time.

---


### 455. [Security Is More Than a Library Call: How Security Features Live in Code](https://arxiv.org/abs/2610.06132)

**<font color=#1a73e8>作者：</font>** Kevin Hermann, Sven Peldszus, Thorsten Berger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Implementing security features---functionalities that protect sensitive data or prevent malicious actions by attackers---is important for ensuring the security and integrity of software systems. Correctly implementing access control, cryptography, or other security features is challenging as they require substantial domain expertise, careful design, and custom implementation to integrate them within the software system.
Previous work has thoroughly studied security awareness, perception, practices, and expertise via surveys, interviews, and experiments. While they have shown that the implementation of security features are often supported by security libraries and frameworks, they have also shown that developers rarely are security experts, and make mistakes that introduce vulnerabilities into software when using them. Despite this extensive knowledge of security practices and developer behavior, we still lack a comprehensive understanding of how security features actually manifest at the code level across full software systems.
We close this gap by conducting a mining study of security features in 9 popular and large open-source Java systems. We manually inspected 2,127,761 lines of code across 19,121 files, identifying and annotating 183,395 lines implementing 561 security features corresponding to 54 security features in our taxonomy. We analyzed the characteristics of the identified security features, such as their size, scattering, tangling, common implementation patterns, and the use of internal and external functionalities. Our findings show that security features are far more than mere calls to external libraries. Security features, such as access control, can grow large in size, scatter across the whole codebase, and frequently tangle with each other. External security libraries are commonly used, but they require substantial amounts of code for integration.

---


### 456. [Machine learning for journal entry testing: A type-aware evaluation of anomaly detectors under a review budget](https://arxiv.org/abs/2610.06133)

**<font color=#1a73e8>作者：</font>** Jan Gronewald, Michel Scherer, Nijat Mehdiyev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Journal entry anomaly detectors are commonly evaluated on the full population with ROC-AUC, precision and recall, ignoring the review budget and which anomaly types are found. We propose a type-aware evaluation combining per-type recall, fair-share type recall (FSR), which caps each type's credit at its budget share, type coverage and first-hit rank. We evaluate nine unsupervised detectors, a supervised reference and feedback-driven Deep Semi-Supervised Anomaly Detection (DeepSAD) on four real client ledgers with injected typed anomalies and a public synthetic ledger. On the largest client ledger, principal component analysis (PCA), an autoencoder (AE) and a variational autoencoder (VAE) each place on average 98 anomalies among the first 100 postings, but at least 95.8 belong to one type. FSR instead favours a nearest-neighbour (kNN) detector and changes the top-ranked detector on three of four client ledgers. Representation also matters: one-hot encoding exposes unseen accounts, whereas frequency encoding leaves unseen contra accounts largely undetected. On the public ledger, the Histogram-Based Outlier Score (HBOS) and Empirical Cumulative Distribution-Based Outlier Detection (ECOD) reach all eight markings within 1,386 entries, whereas kNN, the hit leader at 1,000 entries, first reaches cross-linked clearing at rank 4,641, and the supervised row-level reference misses this marking within 1,000 entries. There, the adaptive DeepSAD review protocol raises mean hits per 100 reviews from 40.0 to 68.3 but type coverage only from 2.7 to 3.0. These findings show that high hit rates can conceal systematic blind spots and suggest that feedback can reinforce existing detection patterns without broadening anomaly coverage.

---


### 457. [AnchorGen: Anchored Optimization for Customizable Generative 3D Design](https://arxiv.org/abs/2610.06135)

**<font color=#1a73e8>作者：</font>** Hantao Zhang, Oliver Heinimann, Jieke Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Engineering design often starts from a 2D sketch that fixes style and proportions, yet the subsequent 3D shape optimization relies on learned generative priors to keep the geometry valid. However, these priors are agnostic to the sketch: while they admit a valid design by correcting a drifted proposal back to its training distribution, they often correct it towards the high-density region, ignoring the specified design. We introduce \emph{AnchorGen}, a rectified-flow framework trained unconditionally on the concatenated shape and sketch latents of paired data. The learned manifold represents the joint distribution of shape-sketch pairs, so constraining the sketch component restricts the iterate to the sub-manifold of shapes consistent with a target style. Since training employs no conditioning signal, the constraint is imposed at inference: gradient descent optimizes the shape latent to minimize a differentiable drag surrogate, while constraining the sketch latent to remain close to the target sketch via a token-wise cosine penalty. A single model thereby supports design-preserving optimization, dimensionally explicit design edits, and sketch-only synthesis.

---


### 458. [Co-Optimizing Graph Sparsification and Approximate Computing for Energy-Efficient FPGA-Based GCN Inference](https://arxiv.org/abs/2610.06138)

**<font color=#1a73e8>作者：</font>** Nathaniel Kaye Mellor, Shreejith Shanker, George Floros  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Convolutional Networks (GCNs) have emerged as a powerful framework for learning from graph-structured data, yet their deployment on resource-constrained edge platforms remains challenging due to the computational and memory demands of sparse graph aggregation. This work presents an FPGA-based GCN accelerator that combines DSpar graph sparsification, 8-bit quantization, and approximate multipliers on the AMD Kria KV260. Evaluated on Cora, LastFM Asia, and Amazon Photo, the design explores the interaction between sparsification and approximation across graphs with widely varying densities. Results show that the effectiveness of approximate arithmetic is governed by accumulation depth within GCN computations. Approximate multipliers are most effective when applied to sparse aggregation operations, while graph sparsification further improves their viability by reducing aggregation depth. The combined approach achieves up to 9.88$\times$ speedup while maintaining 86.6\% classification accuracy on Amazon Photo, and 1.52$\times$ speedup with 77.0\% accuracy on Cora, with total power consumption below 1 W. These results demonstrate that graph sparsification and approximate computing are complementary techniques whose co-optimization enables efficient low-power GCN inference on edge FPGA platforms.

---


### 459. [On Impact of Loss Function on the Performance of Neural Networks in Melanoma Diagnosis](https://arxiv.org/abs/2610.06139)

**<font color=#1a73e8>作者：</font>** Morgan May, Pierpaolo Dondio, Simon Caton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Melanoma is the deadliest type of skin cancer, whose early diagnosis is crucial for patients' survival. Image classification using deep learning models has shown promising results for melanoma diagnosis. However, the performance of these models on the melanoma datasets such as SIIM-ISIC melanoma classification dataset is a challenge due to the class imbalance. One of the methods to deal with this challenge is using loss function modifications. In this work, we have investigated the effect of different loss functions on the performance of deep neural networks. We trained these networks using focal loss, logit-adjusted softmax cross-entropy (CE) loss, and weighted softmax CE loss, and we report different metrics for evaluating performance and uncertainty calibration. Our results suggest that focal loss delivers a good combination of performance in terms of AUC and uncertainty calibration in terms of expected calibration error (ECE) simultaneously.

---


### 460. [Impact of Data Augmentation on Confidence Calibration in Melanoma Classification](https://arxiv.org/abs/2610.06146)

**<font color=#1a73e8>作者：</font>** Morgan May, Simon Caton, Pierpaolo Dondio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately quantifying the predictive uncertainty or improving model calibration plays an important role in medical image classification, in particular in melanoma diagnosis, where accurate uncertainty quantification can have significant implications for patient care. One of the methods for calibration improvement is data augmentation. In addition, data augmentation as a method for synthetically increasing the size of the dataset has been proven to improve the performance of models trained on imbalanced datasets. However, the impact of data augmentation, as a transformation of a part of the original data, on calibration of models trained on imbalanced datasets, in particular in melanoma classification is under-explored. We train neural networks on SIIM-ISIC 2020 melanoma classification dataset under two conditions: with and without data augmentation, and compare the differences in AUC and expected calibration error (ECE) in both scenarios. Our results shows improvements in uncertainty calibration using different augmentation methods.

---


### 461. [Introducing Code-Switched Contexts to Cognitively-Inspired Bilingual Model Training](https://arxiv.org/abs/2610.06161)

**<font color=#1a73e8>作者：</font>** Zhuojing Huang, Luise Pohlmann, Lisa Beinborn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During language acquisition, bilingual children are regularly exposed to code-switched input and use it as a cognitive scaffold to accelerate vocabulary growth and cross-linguistic syntactic mapping. In contrast, computational bilingual models are conventionally pretrained on interleaved monolingual corpora. While introducing synthetic code-switching during pretraining has become a promising strategy to enhance cross-lingual alignment and downstream performance, the structural and developmental parameters governing the success remain poorly understood. In this work, we investigate the efficiency of training with synthetic code-switched data across two typologically distinct language pairs by controlling two key variables: the structural location of code-switches and the dynamic switching rate across training stages. Our results show that training with code-switched data improves cross-lingual alignment for typologically close languages.

---


### 462. [Bayesian Optimization in Sequence-to-Architecture Latent Space for Zero-Shot NAS](https://arxiv.org/abs/2610.06167)

**<font color=#1a73e8>作者：</font>** Ondrej Tybl, Lukas Neumann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot Neural Architecture Search removes the prohibitive cost of traditional NAS, but its search process is typically based on the evolutionary algorithm (EA); lacking an explicit model of the objective, it often resorts to a near-random search through mutation. Bayesian Optimization offers a principled alternative by modeling the objective and aggregating information across iterations, but scales poorly to the high-dimensional, discrete, graph-structured spaces of modern NAS, restricting its use to only small networks. In this paper, we bring Bayesian Optimization to zero-shot NAS for large-scale architectures by learning a latent space via a Variational Autoencoder trained to reconstruct a novel prefix encoding of architectures and propose a proxy scalarization that combines several zero-shot proxies into a single Bayesian Optimization objective. After only 10,000 iterations of the proposed search algorithm (8 hours on a single GPU), our method found a network architecture which under the given model parameter count constraints achieves state-of-the-art results on three separate tasks -- image classification, object detection and semantic segmentation.

---


### 463. [Two-Point Local Optimality in $k$-Means via Boundary-Point Screening](https://arxiv.org/abs/2610.06182)

**<font color=#1a73e8>作者：</font>** Wenlong Lyu, Xujie Xiao, Yuheng Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lloyd's algorithm and the discrete local (D-local) optimization method (Li et al., 2025) for $k$-means provide only weak local-optimality guarantees, and their solution quality remains sensitive to initialization. In this paper, we introduce $r$-point local optimality, under which no reassignment of at most $r$ samples decreases the objective function, and focus on $r=2$. The main computational obstacle is the $\mathcal{O}(n^2(k^2+d))$ cost of exhaustive two-point certification for $n$ samples in $d$ dimensions and $k$ clusters. To address this challenge, we prove that (i) every improving two-point move of a D-local optimum must involve a cluster shared by both reassignments, and (ii) only certificate-defined boundary points can participate in an improving pair. Exploiting this structure, we propose Boundary-Point-Screened Two-Point Local Search (BPS-2PLS), which terminates at a two-point local optimum. For fixed $k,d$ and nonvanishing cluster occupancy, the number $m$ of retained candidates satisfies $m=\mathcal{O}_{\mathbb{P}}(\log n)$ under i.i.d. sampling from a bounded-support distribution with bounded density or from a Gaussian mixture. Across twelve benchmarks, BPS-2PLS attains the lowest available mean WCSS on ten. In a subsampling study, screening retains 0.10% to 2.81% of samples on average at the largest tested sizes. The code is available at this https URL.

---


### 464. [Loss-Invariant Projections as Passive Probes of Learned Representations](https://arxiv.org/abs/2610.06195)

**<font color=#1a73e8>作者：</font>** Akshay Chandrasekhar, Pavlo Melnyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned feature representations in neural networks often contain structure beyond that directly used by the final task output. We study this structure using $\textit{passive probes}$ that apply fixed, untrained, property-independent projections to representations as they evolve during training. We motivate this approach through the task of prediction on $S^2$ where equivalent vector and Hermitian parameterizations reveal an additional loss-invariant trace coordinate. This motivates a general construction in which fixed random projections serve as observers of learned features. Because the observer is loss-invariant and independent of the property being studied, changes in accessibility reflect changes in the representation relative to the fixed observer rather than adaptation of the observer itself. We show that ensembles of passive probes can directly reflect task-relevant information such as target alignment. Under our constructions, the accessibility of eventual difficulty evolves differently across tasks. It increases during training in the regression tasks of surface-normal estimation and image inpainting but remains near its initial level in image classification. Comparisons with learned linear probes further show that recoverability and passive accessibility can evolve differently during training. Together, these results show how passive probes can separately characterize changes in representation geometry and the accessibility of eventual task difficulty.

---


### 465. [MoCAR: Motion-code Coordinate-aware AutoRegression for Continuous Trajectory Forecasting](https://arxiv.org/abs/2610.06210)

**<font color=#1a73e8>作者：</font>** Yiming Xu, Hao Cheng, Monika Sester  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive generation is natural for language, where predicted tokens can be directly reused as the next prediction state, but trajectory forecasting lacks such a clean token: motion is continuous, multimodal, and expressed in local coordinate frames that evolve with the predicted trajectory. We present MoCAR (Motion-code Coordinate-aware AutoRegression), a decoder-only framework that casts trajectory forecasting as next-code prediction in a coordinate-aware continuous latent space. MoCAR learns a continuous motion-code space from endpoint-normalized trajectory segments, where each code jointly captures local trajectory geometry and the reference-frame transition induced by that segment. Historical motion codes are used as a teacher-forced prefix, future codes are generated autoregressively under temporal, map, agent, and mode interactions, and predicted codes persist in latent memory while decoded endpoints update the local scene context. This enables rollout without trajectory-space re-tokenization, trajectory queries, goal candidates, or proposal-and-refinement pipelines. On Argoverse (AV) benchmarks, MoCAR achieves top-tier performance with a simple single-stage architecture, transfers strongly from AV2 to AV1 in zero-shot evaluation, and improves on turn-heavy scenarios. Ablations confirm that the learned continuous motion-code space, latent alignment, weak KL regularization, and joint tokenizer-predictor optimization are essential for stable latent autoregression.

---


### 466. [Structured Representation Learning for Behavior Cloning: How can we learn to safely control a nuclear power plant?](https://arxiv.org/abs/2610.06211)

**<font color=#1a73e8>作者：</font>** Perceval Beja-Battais, Alain Grosset{ê}te, Nicolas Vayatis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned models for industrial control are usually judged by aggregate accuracy, but accuracy at the component level does not guarantee safety once it is embedded in the system it is meant to serve. We study this gap on a behavior-cloning task: imitating an expert Nonlinear Model Predictive Control (NMPC) policy for load-following of a Pressurized Water Reactor (PWR), an industrial system with tight safety constraints. We propose a structured architecture encoding variables from each timescale into separate latent spaces, reflecting the physical decomposition of the system, before training a controller to imitate the expert on the product latent space. On long-horizon rollouts, separated embeddings improve both accuracy and feasibility compared with a shared-embedding baseline. Sensitivity analysis further shows that our model yields interpretable representations aligned with the system's physics. However, standalone deployment still leaves several percent of trajectories infeasible regardless of the architecture. Using our method to warmstart the NMPC optimizer rather than acting standalone, we recover full feasibility and near-optimal cost while still cutting computation time by $\sim$15% relative to the expert controller, and even more for abrupt operating changes.

---


### 467. [Sampling Allocation of LinUCB: Optimal Design Limits in the Small-Gap Regime](https://arxiv.org/abs/2610.06213)

**<font color=#1a73e8>作者：</font>** Yujie Liu, Vincent Y. F. Tan, Yunbei Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sampling allocation of LinUCB in the small-gap regime, where the reward gaps are of order at most $n^{-1/2}$ over the decision horizon $n$. This scaling captures the hard instances underlying worst-case regret lower bounds, for which LinUCB is known to be near optimal up to logarithmic factors in $n$. Using a mean-field perspective, we characterize this allocation through the empirical sampling distribution, a macroscopic object that averages the effect of adaptive decisions over the horizon, and identify its limit as $n\to\infty$. We establish that in this regime, the empirical sampling distribution induced by LinUCB converges to the set of D-optimal designs. This central result reveals that, in the small-gap regime, LinUCB not only achieves near optimal minimax regret but also allocates samples in a way that is asymptotically efficient for learning the reward parameter, thereby connecting regret-driven online learning with information-efficient experimental design. Building on the optimal design limit, we obtain two useful consequences. First, we refine the asymptotic regret analysis of LinUCB in the small-gap regime by characterizing its leading-order constant in the limit. Second, we show that, despite LinUCB's adaptive sampling strategy, the regularized least-squares estimator satisfies a central-limit-type theorem in the small-gap regime, thereby enabling valid statistical inference for the reward parameter.

---


### 468. [Frequency-Decoupled Diffusion Guidance for Non-Blind Image Deblurring](https://arxiv.org/abs/2610.06221)

**<font color=#1a73e8>作者：</font>** Sihan Wang, Jinshu Huang, Haibin Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained diffusion models provide powerful image priors for training-free posterior sampling in image restoration. To guide this sampling process, frequency-aware methods progressively incorporate measurement information across frequency bands, facilitating coarse-to-fine reconstruction. However, existing methods typically do not explicitly separate frequency activation from degradation-induced attenuation, leaving attenuation differences among inactive frequencies insufficiently modeled. In this work, we propose frequency-decoupled posterior guidance to separate frequency activation from attenuation-aware spectral regularization. Specifically, a progressive low-to-high frequency schedule determines the active measurement band, while a kernel-derived attenuation map defines a selective spectral prior over inactive components. To stabilize the sampling process, we also introduce a local trajectory regularizer that suppresses spatially irregular state-to-clean deviations. For a fixed endpoint energy, we provide a KL-regularized path-space interpretation. In practice, we construct time-dependent guidance through local energy corrections using a Tweedie plug-in approximation. Experiments on natural-image benchmarks demonstrate strong PSNR and SSIM performance across challenging non-blind deblurring settings, even at higher measurement noise levels.

---


### 469. [LeAVJEPA: A Minimalist Architecture for Audio-Visual Self-Supervised Learning](https://arxiv.org/abs/2610.06226)

**<font color=#1a73e8>作者：</font>** Benjamin Robson, Santeri Mentu, Wenshuai Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior audio-visual self-supervised learning methods rely on mechanisms such as EMA target encoders, prediction heads, reconstruction decoders, and contrastive losses. We introduce LeAVJEPA, the first audio-visual encoder trained under LeJEPA's collapse-free objective. A single early-fusion Vision Transformer processes audio, video, and joint audio-video inputs. Modality dropout treats a missing modality as another view of the same event, making cross-modal alignment implicit in the objective. The model aligns global embeddings with modality-specific local embeddings, and SIGReg prevents representational collapse. A controlled ablation identifies modality dropout as the key mechanism for audio-visual alignment. Despite the architectural simplicity, LeAVJEPA reaches 36.0 mAP on AudioSet-20K and 91.3% accuracy on ESC-50 under frozen evaluation. After fine-tuning, it reaches 61.1% accuracy on VGGSound, and its embeddings support zero-shot audio-visual retrieval.

---


### 470. [SO(3)-RoPE for Spherical Transformers](https://arxiv.org/abs/2610.06229)

**<font color=#1a73e8>作者：</font>** Christian Libner, Chase van de Geijn, Alexander S. Ecker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spherical data arise in many scientific applications. Often spherical transformers disregard the geometry of the underlying spherical domain, causing distortions and coordinate singularities near the poles. We introduce SO(3)-RoPE, a relative positional embedding that incorporates spherical geometry into transformer attention through unitary SO(3) representations. Our formulation is SO(3)-equivariant and compatible with FlashAttention, retaining efficiency of vanilla transformers. On shallow water dynamics prediction over a rotating sphere, our SO3ViT outperforms an S2Transformer baseline with lower errors and reduced runtime.

---


### 471. [Parameter Estimation in Machining Dynamics with Regenerative Delay and Nonsmooth Friction using Physics-Informed Neural Networks](https://arxiv.org/abs/2610.06230)

**<font color=#1a73e8>作者：</font>** Meiyazhagan Jaganathan, Vikram Pakrashi, Aasifa Rounak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A multi-domain eXtended Physics-Informed Neural Network (XPINN) framework is developed for nonsmooth Delay Differential Equations (DDEs). This is the first implementation to demonstrate the efficacy of partitioning the temporal domain into subdomains of integer multiples of the characteristic time delay and progressively training the associated subnetworks while freezing previously learned parameters. The efficacy of the proposed framework is demonstrated using a machining dynamics model that incorporates both regenerative and nonsmooth frictional effects. Results demonstrate that the proposed multi-domain XPINN framework leads to better solution reconstruction in DDEs and improved parameter estimation compared to a generic PINN (SPINN) formulation. The proposed method works particularly well for extended temporal domains and non-constant history functions. The robustness of inverse XPINN (I-XPINN) is also assessed using reference data contaminated with Gaussian measurement noise. Results indicate that I-XPINN remains resilient to measurement noise and the physics-informed constraints guide the network toward accurately recovering the underlying dynamics. This demonstrates, for the first time, the potential of the proposed framework for reliable parameter identification in DDEs characterised by nonsmoothness and large time delays.

---


### 472. [Joint Class-Time Learning for Video Classification with Multi-Instance Partial-Label Learning](https://arxiv.org/abs/2610.06234)

**<font color=#1a73e8>作者：</font>** Lingyu Shen, Wei Tang, Fakhri Karray 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-instance partial-label learning (MIPL) addresses inexact supervision in both the instance and label spaces, which can be applied to video classification. However, bag-level labels do not explicitly supervise the correspondence between candidate classes and temporal evidence. We propose {\ours}, which couples label disambiguation with temporal evidence allocation through a joint class--time assignment. Occupancy-regularized spherical matching associates contextualized video features while learning nonuniform temporal mass and discouraging excessive concentration. During training, candidate-restricted inference recomputes the assignment within the candidate label set. A dual-marginal KL projection then constructs a structured teacher that incorporates momentum-refined class beliefs while preserving the proposal's temporal occupancy. A single plan-level KL objective aligns the full-space predictor with this teacher. Our analysis characterizes when candidate re-solving differs from masking and shows that, under the stated construction, the joint objective decomposes into class-marginal and class-conditional temporal supervision. We construct VCMIPL benchmarks from Breakfast, DoTA, and FineAction using model-generated candidate labels and evaluate the method across four feature representations. Extensive experimental results demonstrate that PIVOTMIPL outperforms existing MIPL algorithms in both effectiveness and efficiency.

---


### 473. [Few-Shot Prototype Head Adaptation for On-Device ECG Personalization on PSoC~6](https://arxiv.org/abs/2610.06241)

**<font color=#1a73e8>作者：</font>** Guilherme Silva, Pedro Silva, Gladston Moreira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable and bedside electrocardiogram (ECG) monitors must adapt to patient-specific morphology to maintain arrhythmia detection accuracy across users, yet personalization is typically performed offline and cannot account for individual physiology, electrode placement, or recording drift. On-device adaptation by backpropagation is expensive for microcontroller-class medical devices because it requires an optimizer state, repeated backward passes through convolutional layers, and labeled arrhythmic beats that may not be available at deployment time. This letter proposes prototype-only head adaptation as a compact personalization primitive for TinyML ECG systems. A one-dimensional convolutional neural network (1-D CNN; 1,314 parameters and 72.6k multiply-accumulate operations per beat) is trained offline on the MIT-BIH Arrhythmia Database under an inter-patient protocol, frozen as a feature extractor, and exported to a PSoC 6 microcontroller. Patient-specific adaptation then reduces to computing closed-form class means in a 32-dimensional embedding space, requiring no convolutional backward pass, no iterative optimization, and only one forward pass per support beat. Prototype adaptation improves inter-patient macro-F1 from 0.635/0.639/0.646 to 0.731/0.771/0.797 at 1/5/10-shot, outperforming linear stochastic-gradient-descent (SGD) head fine-tuning at every shot count for the target tiny backbone. On-device replay over 18 one-shot episodes on a PSoC 6 Cortex-M4F matches the host macro-F1 for the prototype head (0.798), with 11.39 ms per beat, 5.2 KB flash, and 22.2 KB SRAM. A restricted variant that updates only the normal-class prototype from passively buffered sinus beats yields a consistent +0.05 macro-F1 gain, reducing the annotation burden during initial

---


### 474. [Constrained Goal-directed Planar Graph Generation with Grammar-based Reinforcement Learning](https://arxiv.org/abs/2610.06244)

**<font color=#1a73e8>作者：</font>** Nicolas Hochuli, Lorenzo Miele, Kristina Shea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planar graphs are central to applications across science and engineering, yet existing generators provide limited support for goal-directed generation under hard structural and geometric feasibility constraints. We propose a dataset-free method for generating planar graph embeddings by combining parametric graph grammars with safe reinforcement learning to optimize generic task-specific objectives while satisfying constraints during construction. We formulate the generation process as a constrained Markov decision process, where the graph grammar defines the state and action spaces. We further introduce an action projection that maps sampled actions toward state-dependent safe sets, improving constraint satisfaction during training. In contrast to classical graph generators and deep generative models, which typically offer limited goal-directed control or rely on weak constraint satisfaction, our method constructs feasible planar graph embeddings directly during generation. We also introduce a benchmark suite for constrained and goal-directed planar graph generation, together with classical and deep generative baselines. Across all benchmark tasks, our method consistently outperforms baselines while satisfying the formulated constraints.

---


### 475. [Generative World Models Enable Predictive Control of Laser Melt Pool Dynamics](https://arxiv.org/abs/2610.06250)

**<font color=#1a73e8>作者：</font>** Yiyang Yan, Markus Bambach, Mohamadreza Afrasiabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models, which learn how environments respond to actions, are emerging as a powerful paradigm for planning through imagined futures, transforming decision-making across games, robotics and autonomous driving. Bringing this capability to manufacturing could enable process decisions on timescales inaccessible to high-fidelity simulation. Here we introduce a generative world model for localized highly dynamic laser melt pool that predicts evolution from histories of temperature and phase morphology under candidate actions. Its generative latent dynamics capture the effects of unresolved melt flow, enabling more accurate recursive rollouts than deterministic regressors under transient laser inputs. Because the learned dynamics are differentiable, the model can serve directly as a predictive control plant. Gradients through imagined futures optimize laser schedules that regulate melt-pool depth over previously unseen geometry, path, initialization. We further distil this optimization into an amortized policy that produces control actions in a single forward pass, providing a proof of concept for real deployment on machines.

---


### 476. [Lipschitz Thinking: Ten Years of Certifiable-by-Design Robust Neural Networks](https://arxiv.org/abs/2610.06252)

**<font color=#1a73e8>作者：</font>** Fabio Brau, Giorgio Piras, Maura Pintor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Lipschitz property of a deep neural network provides a direct measure of its sensitivity to input perturbations and, when explicitly controlled, offers a principled way to limit the propagation of errors and improve robustness. Over the past decade, Lipschitz-bounded layers have been incorporated into increasingly expressive and high-performing deep models, narrowing the gap between empirical robustness and formal, by-design guarantees of stability. This article introduces the fundamental concepts underlying Lipschitz-bounded neural networks, explaining the principles behind Lipschitz-constrained layers, the mechanisms used to enforce their bounds, and how they yield robustness certificates at the cost of a single forward pass. The tutorial concludes by discussing emerging and open directions, highlighting Lipschitz control as a general framework for offering guaranteed, by-design stability.

---


### 477. [SatBleed: Security of Commoditized Communication Modules in Satellites](https://arxiv.org/abs/2610.06258)

**<font color=#1a73e8>作者：</font>** Ulysse Planta, Julian Rederlechner, Martin Strohmeier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Substantial reduction in launch and manufacturing costs has resulted in the accelerated deployment of small satellite missions, with commercial off-the-shelf (COTS) components becoming the prevailing standard for specific subsystems. However, this modular architecture introduces critical security risks, most notably in the Communication Subsystem (COM), which is continuously exposed by design and implicitly trusted as the entry point for command and control. We construct a tailored threat taxonomy for attacks targeting the COM subsystem and analyze representative COM systems from various vendors. Our findings uncover severe vulnerabilities across firmware, protocols, and architectural designs. This work presents the first in-depth security evaluation of widely deployed COTS COM modules employed in small satellites, identifying vulnerabilities affecting dozens of missions. To assess the real-world impact, we correlate our discoveries with open-source telemetry data, inferring at least 28 vulnerable missions in orbit that are susceptible to hostile takeover. Our work reveals that satellite COM subsystems form an attractive and dangerously neglected attack surface, necessitating urgent attention from the community.

---


### 478. [OCL-PDE: A Generative Framework for PDE Inverse Problems with Observation-Complementary Latents](https://arxiv.org/abs/2610.06259)

**<font color=#1a73e8>作者：</font>** Ding Yang, Chuqi Chen, Chang Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equation (PDE) inverse problems are often ill-posed, making fine-scale details difficult to recover. We address this problem by introducing a learned observation-complementary latent representation that preserves reconstruction-relevant information and is combined with the observation to reconstruct the unknown field. Building on this representation, we propose OCL-PDE, a generative framework that encourages the observation to guide large-scale structure and the latent to supply complementary fine-scale details. OCL-PDE is built on a physics-aware autoencoder (AE) and conditional Flow Matching, supporting inverse reconstruction as well as forward PDE prediction. Experiments demonstrate improved reconstruction accuracy and fine-detail recovery compared with the evaluated baselines.

---


### 479. [Ramp Metering Control via Hybrid State Deep Reinforcement Learning in Partially Observable Connected Vehicle Environments](https://arxiv.org/abs/2610.06266)

**<font color=#1a73e8>作者：</font>** Youcef Mehamlia, Nadir Farhi, Meriem Bouali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Freeway on-ramp merges are major sources of congestion, causing significant economic and environmental costs. While Deep Reinforcement Learning (DRL) offers a promising solution for ramp metering, existing approaches rely primarily on aggregated macroscopic data. Connected vehicles (CVs) provide vehicle-level observations that can complement aggregate traffic measurements, but their limited penetration produces incomplete microscopic information. This paper proposes a hybrid observation representation combining macroscopic traffic measurements with a two-channel grid encoding observed CV presence and speed. A Dueling Double Deep Q-Network processes these inputs to select ramp-metering green durations. The controller is trained under varying traffic demands and CV penetration rates and evaluated against ALINEA and macroscopic-only DRL variants in SUMO. Across 50 matched evaluation scenarios, the hybrid controller under partial CV visibility reduces the reported total travel time by 11.4 % and mean spillback duration by 84.9 % relative to ALINEA. Evaluating the same trained policy with full CV visibility yields a further travel-time reduction of approximately 1.6 %. Analysis across penetration rates suggests that the performance gap decreases as microscopic observations become more complete. These results support the use of complementary macroscopic and sparse microscopic observations for learning-based ramp metering. The source code implementation of the model is available at: this https URL

---


### 480. [DPNL: A DPLL-based Algorithm for Probabilistic Neurosymbolic Learning](https://arxiv.org/abs/2610.06270)

**<font color=#1a73e8>作者：</font>** Thomas Jean-Michel Valentin, Pierre Genev{è}s, Luisa Sophie Werner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic Neurosymbolic Learning (PNL) combines neural predictions with symbolic reasoning, enabling end-to-end learning from final-output supervision without labels for intermediate concepts. A central challenge is probabilistic inference: state-of-the-art approaches often rely on materializing the logical provenance of a query, which can itself become a major computational bottleneck. We introduce Dynamic Probabilistic Neurosymbolic Learning (DPNL), an oracle-guided framework that avoids requiring complete provenance materialization before inference. DPNL lazily explores the space of intermediate assignments, while oracles resolve entire regions that can already be certified to produce or exclude the target output. We establish conditions ensuring soundness and termination. ApproxDPNL extends the same search with early termination while maintaining certified bounds on the exact output probability, providing controlled approximation guarantees. The oracle interface decouples inference from the representation of the symbolic component, enabling problem-specific reasoning within the same framework. Experiments on several neurosymbolic tasks show that DPNL and ApproxDPNL substantially extend the range of problem instances tractable by probabilistic neurosymbolic inference.

---


### 481. [What May an Agent Change About Itself? A Containment Floor for Self-Configuring Agent Runtimes](https://arxiv.org/abs/2610.06274)

**<font color=#1a73e8>作者：</font>** Sajib Hossain, Moeen Uddin Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many agent runtimes give the agent a tool for editing its own configuration. Some of that configuration grants abilities, such as enabling a tool. Other parts set the agent's limits: which directories it may write to, who may send it messages, which network address it listens on, how callers authenticate, and the gate that blocks risky writes. If the agent can edit those limits, a single ordinary request can widen them. We study this in a deployed, model-agnostic runtime. We propose a rule: the agent may change fields that grant abilities, and may never change fields that set its limits. We enforce the rule as a containment floor inside the configuration tool and measure what happens with and without it. Without the floor, a frontier model wrote a protected value on 25 of 72 ordinary requests that gave it permission to change settings, often when the request never named the field. Prohibitions written in the system prompt failed in a predictable way. A prompt that listed the protected field names stopped every request that used those names (0 of 36 saved, against 17 of 36 with no prompt) and did not stop the requests that only described the goal (10 of 36 saved, against 8 of 36). A prompt that described the forbidden effects did the reverse. With the floor, 0 of 167 protected writes were saved, although the models attempted a protected write in 65 of those cases. A search for other routes through the tool found only one, a pinned shell, which the floor's scope statement already excludes. The study covers two models and a single agent. We state what that does and does not support.

---


### 482. [dIon: Fragmentation-Based Invariance for Self-Supervised Learning of Tandem Mass Spectra](https://arxiv.org/abs/2610.06282)

**<font color=#1a73e8>作者：</font>** Alfred Nilsson, Joel Lapin, Samuel H. Payne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a novel invariance for peptide tandem mass spectrometry data, unlocking self-supervised representation learning that improves de novo sequencing of peptides. This invariance exploits the physical relationship between precursor properties (mass and charge) and fragment-ion evidence, without requiring peptide sequence labels. We introduce dIon, which adapts the DINO framework with two latent prediction tasks, both recovering a clean teacher representation: one from a spectrum mixture, using the precursor as a selection query, and one from a partial spectrum with the precursor withheld. The first associates precursor information with fragment-ion evidence; the second prevents representational collapse onto that information alone. Mechanistic probes support both effects, and ablations show that the full objective performs best. Under identical end-to-end training, dIon initialization improves de novo peptide precision over training from scratch by 5.5 and 8.4 percentage points on the held-out MassIVE-KB and Kingdoms test sets, and by 2.3 and 4.8 percentage points with a larger supervised training corpus. The resulting models surpass fully supervised state-of-the-art de novo sequencing models on the diverse, multi-species Kingdoms corpus under the same greedy-decoding protocol. Without peptide labels, dIon learns strong native peptide-similarity geometry compared with other learned models; with limited peptide-supervised adaptation, it achieves the best retrieval and pair-discrimination performance across all representation benchmarks.

---


### 483. [From Abusive Language Classification to Sequence Labeling Identification](https://arxiv.org/abs/2610.06287)

**<font color=#1a73e8>作者：</font>** Nicolas Zampieri, Ignacio Lopez, Manon Girard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Industrial content moderation must process massive message streams under tight latency constraints, yet most abusive language (AL) detection systems rely on sentence-level classification (ALC), which neither localizes abusive spans nor identifies who is targeted. We define Abusive Language Identification (ALI) as a sequence-labeling task that jointly extracts AL spans and target mentions, and assess whether this approach can be used for text moderation. On a pilot corpus drawn from a production moderation pipeline, we compare ALI with ALC on cross-domain generalization and implicit abuse, and we also evaluate AL and target span detection. ALI remains competitive with ALC while providing localized outputs for moderators, with a modest and configuration-sensitive advantage on implicit abuse. Exact AL boundaries and target spans remain difficult to recover. We complement this comparison with a qualitative analysis and discuss perspectives on complete target--span linking and on structured benchmarks for ALI.

---


### 484. [Trajectory-Guided Tokenization of Complex CSI for Wi-Fi Sensing](https://arxiv.org/abs/2610.06288)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Kenuo Xu, Jichu Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wi-Fi channel state information (CSI) enables contactless presence detection and gesture recognition. Its high-dimensional complex-valued time series require input representations that preserve informative temporal variations during compression. We propose Trajectory-Guided Tokenization (TGT), which combines complex trajectory decomposition with asymmetric attention to construct compact continuous tokens. For each antenna link and subcarrier, an orthonormal Helmert transform decomposes short, ordered temporal patches into local-center and centered-trajectory coordinates. Keys are learned from the centered-trajectory coordinates, while values retain both components. Learnable queries aggregate subcarriers into frequency slots, which are fused into temporal tokens. Trained jointly from scratch, TGT with TokenMLP achieves the highest mean accuracy of 92.83% among all evaluated frontend-backend combinations on the self-collected dataset. Experiments on EHUNAM and Widar further support the applicability of TGT to cross-domain presence detection and gesture recognition.

---


### 485. [DialectSentEval 2026: Arabic Dialect Sentiment Analysis and Swapping Shared Task](https://arxiv.org/abs/2610.06298)

**<font color=#1a73e8>作者：</font>** Saad Ezzini, Shadi Abudalfa, Maram Alharbi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis is a fundamental problem in Natural Language Processing (NLP). Standard sentiment classification for the Arabic language remains challenging due to the high volume of dialectal Arabic. To advance research in this area, this paper proposes the Shared Task on Sentiment Analysis and Swapping in Arabic Dialects (DialectSentEval), hosted with the Arabic Natural Language Processing Conference (ArabicNLP 2026). This shared task consists of two subtasks: Subtask 1 focuses on multi-class and multi-dialect sentiment analysis, requiring models to identify sentiment polarity across various Arabic dialects. Subtask 2 introduces a generative task for Arabic sentiment swap, challenging models to invert sentiment polarity while preserving core semantics. In this overview paper, we present the motivation, dataset creation, and summarize the main findings from participating models.

---


### 486. [Teaching a Minimalist Machine to Discover Recursive Programs for Arithmetic](https://arxiv.org/abs/2610.06304)

**<font color=#1a73e8>作者：</font>** Dominik Magiera, Christiane Wiebel-Herboth, Frank Jäkel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans can often acquire and synthesize complex, recursive concepts from minimal experience. Leveraging cognitive insights, we propose the Minimalist Machine, a framework for inductive program synthesis designed to model such conceptual learning. The system uses a compact relational subset of Prolog: Programs are searched within a fixed schema of body-free facts and two-body conjunctive Horn clauses. Recursion is not defined by a dedicated metarule. Instead, it emerges when a target predicate is reused inside the body of a learned clause. Inspired by a primary school curriculum, the model is taught through a human-curated, sequential introduction of new concepts in arithmetic. Starting from initially empty knowledge base, it first acquires simple structural predicates, then successor-based state transformations, and finally recursive programs for addition, subtraction, multiplication, and division. Ultimately, this approach yields the fully transparent, inductive reasoning trace necessary for human-like conceptual learning.

---


### 487. [Cryptanalysis of a Class of Ideal Secret Sharing Schemes Based on the CRT for Polynomial Rings](https://arxiv.org/abs/2610.06312)

**<font color=#1a73e8>作者：</font>** Jian Ding, Zhiyuan Guo, Hongju Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Based on the CRT for polynomial rings, Yang, Zhu, Fu and Xia (ISIT 2026) proposed a compartmented secret sharing scheme for the compartmented access structure with lower bounds, claiming it can be ideal. We exhibit three families of unauthorized subsets that reconstruct the secret. The scheme is therefore insecure, except for a degenerate choice of parameters in which the only authorized subset is the whole participant set. The flaw in the security analysis is that it does not take all published polynomials into account. Similar flaws appear in the same first author's hierarchical schemes (ISIT 2024, 2026).

---


### 488. [SPDAlign: Interpretable Riemannian Alignment for EEG Forward Modeling Shifts](https://arxiv.org/abs/2610.06315)

**<font color=#1a73e8>作者：</font>** Shanglin Li, Shiwen Chu, Okan Koç 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) based brain-computer interfaces enable direct brain-to-device communication for applications such as rehabilitation and communication. However, their practical utility is often limited as the non-stationary nature of the EEG data introduces distribution shifts across domains (e.g., sessions and subjects). Adapting machine learning models to be invariant to these shifts in an unsupervised way, without using costly labeled calibration data, would drastically improve the utility of EEG data. In this work, we use a classic generative model of EEG to study distribution shifts introduced by the domain-specific forward process, which is associated with factors such as head geometry. We theoretically show that such distribution shifts can be recovered solely through linear transformations on the Symmetric Positive Definite manifold. Building on this insight, we propose SPDAlign, an interpretable framework for promoting domain-invariant EEG learning. SPDAlign first aligns the domain-specific means and corrects global rotations across domains using a recent optimal transport technique called Wasserstein Procrustes. We systematically study the proposed approach through simulations and demonstrate its competitive performance on extensive public EEG datasets. Additionally, SPDAlign is a globally linear framework and is intrinsically interpretable, so that the framework can identify frequency ranges of interest, determine the spatial patterns reflecting source-sensor relationships, and address cross-subject variability.

---


### 489. [RollPlace: Improving Macro Placement via Monte Carlo Rollout Search](https://arxiv.org/abs/2610.06316)

**<font color=#1a73e8>作者：</font>** Qi Zhou, Guojun Liu, Guangzhi Qi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The application of Reinforcement Learning (RL) in Electronic Design Automation (EDA), particularly for chip placement, has attracted considerable attention in recent years. While existing machine learning (ML)-based approaches have achieved notable progress, they predominantly focus on generating optimal layouts in a single attempt, often producing solutions that require subsequent refinement. To address this limitation, we propose RollPlace, a novel and generalized macro placement framework. RollPlace adopts a two-stage optimization strategy: generating initial placement solutions via machine learning methods or heuristic-based strategies, and refining these layouts efficiently by adjusting specific macros derived from the initial stage. This strategy circumvents the sequential generation constraints inherent in traditional RL-based placement methods. Furthermore, RollPlace seamlessly integrates Monte Carlo Tree Search (MCTS) to balance exploration and exploitation, and employs a rollout mechanism for efficient local search. Extensive experiments on the ISPD 2005 benchmark demonstrate that RollPlace outperforms state-of-the-art methods. Additionally, end-to-end experimental results based on OpenROAD across 19 benchmarks show that RollPlace excels in multiple metrics. The proposed framework offers a robust and scalable solution for addressing the growing complexity of modern chip design challenges.

---


### 490. [Watermarking: from Impossibility to Auditable Compliance](https://arxiv.org/abs/2610.06317)

**<font color=#1a73e8>作者：</font>** Fernando Delbianco, Fernando Tohmé, Hugo Acciarri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Article 50 (2) of the EU Artificial Intelligence Act requires providers of generative systems to make synthetic outputs machine-readable and detectable, while qualifying the effectiveness, interoperability, robustness, and reliability by technical feasibility, cost, content-specific limits, and the state of the art. For free-form text, one important implementation route is the implementation of a generative watermarking procedure, which poses a compliance problem that is hard to address. Strong watermarking is impossible against adaptive removal, while ordinary edits attenuate statistical evidence, and unmarked human text may overlap distributionally with machine output. This article develops an auditable alternative. First, it defines a description-length robustness profile. A finite-sample bound shows that detectable bias decays and that the required sample size grows with the inverse square of the decay rate. This replaces an unidentified Shannon-entropy constant with collision entropy. Second, it constructs label-conditional conformal prediction sets with separate false-attribution and false-exclusion levels, reporting ``watermark supported,'' ``not supported,'' or ``inconclusive''. Coverage is obtained as a finite-sample result and is class-conditional under exchangeability. A small reproducible simulation of a tournament watermark confirms both claims and shows that the surviving-token rule overstates the tolerable edit rate roughly twofold. The resulting premarket certificate, signed detector report, and postmarket recalibration protocol operationalize the Commission's 2026 Code of Practice without claiming universal robustness.

---


### 491. [CRAFTER: Causality-based Self-adaptation for Autonomous IoT Systems](https://arxiv.org/abs/2610.06320)

**<font color=#1a73e8>作者：</font>** Houssam Hajj Hassan, Ajay Kattepur, Denis Conan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents CRAFTER, an automated framework for designing and deploying self-adaptive IoT systems using Causal Reinforcement Learning (CRL). As IoT devices increasingly populate pervasive computing spaces, smart environments are enabled with advanced monitoring and interactive services. The dynamic nature of these environments, such as fluctuating workloads and evolving application demands, poses significant challenges in maintaining consistent Quality of Service (QoS) levels of IoT applications. While existing self-adaptation techniques offer adaptive capabilities, they are often designed to deal with specific application domains, hindering the design of self-adaptive solutions that can be re-used across multiple IoT verticals. In addition, there is a lack of automated pipelines that act on identifying key performance drivers to take effective adaptation decisions. CRAFTER addresses these issues by using Causality as a formal framework for performance analysis of IoT systems. CRAFTER generates causal graphs to uncover dependencies among system components and guide adaptation decisions based on cause-effect relationships. Then, adaptation agents can leverage this knowledge to take more effective adaptation decisions in dynamic situations. Our experimental evaluation demonstrates how CRAFTER enables deriving causal graphs spanning diverse IoT use cases. Furthermore, we showcase how CRAFTER improves self-adaptation performance by 25% compared to state-of-the-art Reinforcement Learning-based approaches.

---


### 492. [SPIN: Image Immunization Against Diffusion Editing via Single-Step Projection in Stochastic Neighborhoods](https://arxiv.org/abs/2610.06334)

**<font color=#1a73e8>作者：</font>** Fengming Gu, Jie Zhang, Zhongqi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have greatly advanced instruction-guided image editing, while also raising concerns about unauthorized image manipulation. Image immunization addresses this risk by adding imperceptible perturbations to an input image to disrupt subsequent edits. Since editing requests are unknown at image release, protection should remain effective beyond the instruction used to construct the perturbation. Existing immunization methods either require costly full-trajectory backpropagation or use intermediate objectives whose effects may be weakened by subsequent denoising. Meanwhile, a single inference path provides limited feedback about alternative denoising continuations. To address these challenges, we propose \textsc{SPIN}, a framework for image immunization via one-step projection over local stochastic trajectory neighborhoods. Starting from an early denoising state, \textsc{SPIN} generates stochastic neighboring states under the same instruction and predicts their clean latents through one-step projection without full unrolling. We then optimize a bounded input perturbation to maximize the average deviation of these predictions from a clean-edit reference, encouraging the perturbation to disrupt multiple possible editing outcomes. Experiments on two image editors demonstrate substantial gains in protection performance, with \textsc{SPIN} outperforming compared methods across all six metrics under seen instructions and in the more challenging unseen instruction setting.

---


### 493. [BabelFake: A Multilingual Audio-Visual DeepFake Benchmark](https://arxiv.org/abs/2610.06339)

**<font color=#1a73e8>作者：</font>** Carlotta Segna, Joel Tschesche, Anna Rohrbach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable and practical audio-visual DeepFake detection requires benchmarks that reflect diverse linguistic contexts and modern data synthesis pipelines for visual as well as audio manipulations. However, existing datasets predominantly contain footage of English-speakers, often include outdated manipulation types, or overlook the audio modality. Further, many datasets feature individuals who did not consent to be used in DeepFake creation. We introduce BabelFake, a multilingual audio-visual DeepFake benchmark recorded with consenting participants. BabelFake contains 399k clips (1,323 hours) from 496 individuals spanning five languages (English, German, Italian, French, Spanish). Our modular data generation pipeline pairs 11 modern video manipulation methods with 4 voice cloning engines, distinguishing visual-only (face swapping) and joint audio-visual manipulations (lip synchronization and portrait animation). By benchmarking state-of-the-art detectors, we show that detection difficulty depends on the audio-visual generation pairing, with substantial performance degradation when authentic audio is preserved. Cross-language/demographic evaluation reveals sensitivity varying across detector architectures and training data, while human evaluation reveals that perceived realism and machine-detection difficulty do not necessarily align.

---


### 494. [MeSD: Multi-Evidence Self-Distillation for VideoLLM](https://arxiv.org/abs/2610.06342)

**<font color=#1a73e8>作者：</font>** Weijie Zhu, Han Fang, Hanyu Fu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While reinforcement learning with verifiable rewards provides reliable outcome supervision for VideoLLMs, sequence-level rewards offer limited token-level guidance. On-policy self-distillation addresses this limitation by conditioning a self-teacher on privileged information to provide dense token-level supervision. However, aggregating heterogeneous evidence within a single teacher context obscures cross-evidence agreement and conflict. A further challenge lies in determining whether teacher guidance should refine reward-based updates or provide corrective supervision for failed trajectories. To address these issues, we propose MeSD, a multi-evidence self-distillation framework for VideoLLMs. MeSD constructs three evidence-conditioned teachers with shared parameters, using the ground-truth answer as a common semantic context while separately incorporating temporal and spatial evidence. Given the same student-generated prefixes, MeSD evaluates evidence-specific preferences relative to the Answer Teacher and fuses teacher-common preferences with gated teacher-specific residuals. Furthermore, MeSD introduces Verification-Guided Optimization to classify trajectories as Success, Failure, or Indeterminate. For Success and Indeterminate trajectories, MeSD refines token-level advantage magnitudes while preserving reward-derived signs. For verified failure trajectories that contain the required evidence, MeSD applies failure-conditioned distillation, using reverse-KL correction toward the fused distribution. Experiments on multiple video benchmarks demonstrate consistent gains over reinforcement learning and self-distillation baselines.

---


### 495. [Stability-Shaped Deep Graph Learning](https://arxiv.org/abs/2610.06344)

**<font color=#1a73e8>作者：</font>** Junyou Zhu, Langzhou He, Fenying Cai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In deep graph neural networks, increasing depth enlarges the receptive field but often leads to over-smoothing, where node representations tend to align. We develop a unified, mode-wise stability framework for deep GNN propagation that provides a principled characterization of over-smoothing. By interpreting layer depth as time and layer updates as graph-coupled dynamics, over-smoothing can be understood as an undesirable dynamical synchronization of features, for which the master stability curve provides a theoretical tool to assess the stability of synchrony. Guided by this theory, we further propose Stability-Shaped Deep Graph Learning (SDGL) to mitigate over-smoothing in deep GNNs. SDGL has two complementary instantiations: one induces controlled Turing instability to replace synchronization with spatial pattern formation, and the other maintains stable near-critical propagation. Experiments on diverse node- and graph-level benchmarks demonstrate the improved depth scaling and consistent accuracy gains over strong baselines, including graphs exhibiting long-range dependencies.

---


### 496. [KineWorld: Action-Induced Transport Fields for Embodied World Modeling](https://arxiv.org/abs/2610.06349)

**<font color=#1a73e8>作者：</font>** Ziying Song, Yuchen Liu, Zhuoran Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied world models predict the visual consequences of candidate actions before execution. However, existing action-conditioned world models often adopt uniformly weighted visual generation objectives that can be misaligned with embodied prediction needs. Even with explicit motion conditioning, these objectives can underemphasize spatially sparse changes that are critical to interaction. We propose KineWorld, a transport-aware world-modeling framework that extends robot kinematics from motion conditioning to the spatial allocation of generative supervision. Kinematic Transport Lifting (KTL) constructs renderer-derived, camera-aligned transport fields from commanded robot motion. Transport-Aware World Diffusion (TAWD) calibrates their motion support on the video-latent grid and reweights future-RGB flow matching through a normalized mixture of uniform and transport-focused distributions. We train KineWorld using ALOHA-AgileX bimanual manipulation data from RoboTwin 2.0. KineWorld achieves an EWMScore-P of 68.95 in single-view evaluation and a TWB-Score of 54.82 in multi-view evaluation. These results support a shift from appearance fitting toward action-consequence modeling for embodied decision-making.

---


### 497. [Explicit Nonlinear Functions beyond the Fourier bound](https://arxiv.org/abs/2610.06362)

**<font color=#1a73e8>作者：</font>** Swastik Kopparty, Rishabh Kothary, Shanthanu S. Rai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the problem of constructing highly nonlinear vectorial maps $F: \mathbb F_2^n \to \mathbb F_2^m$. Concretely, we want an $F$ and an $A = A(m,n)> 0$ as small as possible, so that for every affine map $L: \mathbb F_2^n \to \mathbb F_2^m$ (of the form $L(x) = M x + b $) we have:
$$\mathrm{agree}(F, L) := |\{ x \in \mathbb F_2^n \mid F(x) = L(x) \}| \leq A.$$
Such questions have been studied by Nyberg (1991,1993), Carlet and Ding (2004,2007), Liu, Mesnager and Chen (2017), Nagy (2025), and Biryukov, Turecek, and Udovenko (2026).
There is a classical method of constructing such functions from bent-functions and Fourier analytic ideas; the best bound achievable by this method is: $$ A(m,n) = \Theta(2^{n-m} + 2^{n/2}),$$
and in particular, is never smaller than $2^{n/2}$.
In this work, we show how to construct highly nonlinear functions beyond this Fourier bound. Concretely, we show how to construct for every $\gamma>0$, a function $F: \mathbb F_2^n \to \mathbb F_2^m$ with $m = O_{\gamma}(n)$, achieving $$ A(m,n) \leq (1 + \gamma)^n.$$
Surprisingly, we even achieve the same quantitative behavior for the much harder question of having low agreement with $m$-tuples of degree $d$ polynomials $Q: \mathbb F_2^n \to \mathbb F_2^m$, with $m = O_{\gamma, d}(n)$. Here the previously best bounds were of the form $A(m,n) = O( 2^{-\frac{n}{2^{d+1}}} \cdot 2^n )$ of Ben-Sasson and Kopparty (2010), based on Gowers-norm-type arguments.
All our results generalize to all finite fields $\mathbb F_q$ in place of $\mathbb F_2$.
Our methods are based on a new connection to classical results on counting solutions to systems of polynomial equations via algebraic methods. This connection brings us to basic questions in combinatorics, about graphs and hypergraphs with simultaneously a small number of edges and independent sets.

---


### 498. [Multimodal Deep Survival Analysis for Sinkhole Susceptibility](https://arxiv.org/abs/2610.06365)

**<font color=#1a73e8>作者：</font>** Lucas Yuan, Minhee Kim, Zihan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sinkholes are a widespread geohazard in karst terrain. In Florida, soluble carbonate bedrock, shallow groundwater, and intense rainfall combine to make subsidence both common and spatially heterogeneous. Predicting where and when sinkholes will occur is difficult for two reasons. First, locations without reported sinkholes cannot be directly labeled or sampled as true negative locations. Second, the potential factors governing sinkhole risk span heterogeneous data modalities and therefore require careful integration within a unified modeling framework. We address both problems with our proposed model, a multimodal Cox proportional hazards framework for sinkhole susceptibility. Our contributions are threefold. First, we extend the proportional-hazards formulation to heterogeneous multimodal input through modality-specific encoders and a cross-modal fusion layer. Second, we treat unreported locations as right-censored rather than negative, avoiding hard-negative labeling and yielding continuous, time-aware susceptibility from the predicted survival function. Third, a statewide Florida case study with spatially blocked validation and ablation studies quantifies the benefit of multimodal integration. A Florida case study demonstrates that the proposed method effectively ranks sinkhole risk and produces a statewide susceptibility map that captures spatial variations in sinkhole occurrence.

---


### 499. [Environmental sensor readings in two crop disease image datasets identify the session in which each image was taken](https://arxiv.org/abs/2610.06369)

**<font color=#1a73e8>作者：</font>** Sungwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrating environmental sensor data with leaf imagery is widely reported to boost crop disease classification accuracy. In this work, we reveal that these reported gains are often artifacts of dataset construction: because a single sensor reading is shared across many images collected in a single session (one farm on one date), multimodal networks can predict disease simply by memorizing session identities. Analyzing two widely used Korean datasets, the Crop Disease Diagnosis (CDD) benchmark and an AI Hub pest/disease dataset, we demonstrate that nearly all images share sensor values, with 91.9% of CDD test images having exact sensor duplicates in the training set. Remarkably, an image-free classifier given only timestamps matches or exceeds sensor-driven predictions across all seven evaluated crops, and matches the published macro-F1 of a state-of-the-art CDD fusion model. These results indicate that performance gains on standard random splits cannot be disentangled from session leakage. We propose that multimodal crop studies must evaluate on session-held-out splits and report performance against sensor-free date-time baselines to ensure genuine generalization.

---


### 500. [MTOR: Generalizable AI-Generated Video Detection with Multimodal Semantics and Temporal Over-Regularity](https://arxiv.org/abs/2610.06378)

**<font color=#1a73e8>作者：</font>** Hang Wang, Chao Shen, Lei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of video generation has narrowed the perceptual gap between authentic and synthetic videos, making generalizable AI-generated video detection increasingly challenging. Existing detectors predominantly rely on visual representations, leaving caption-derived textual semantics underexplored. Meanwhile, temporal regularity in fine-grained visual representations has received limited attention. We find that caption-derived textual representations provide complementary discriminative cues to global visual representations. Our analysis further reveals that AI-generated videos exhibit stronger temporal persistence and lower temporal variability, a pattern we term temporal over-regularity (TOR). Based on these findings, we propose MTOR with a multimodal branch and a TOR component. The multimodal branch integrates global visual and caption-derived textual representations, while the TOR component models temporal over-regularity at three levels: coarse inter-frame continuity, fine-grained token correspondence, and frame-to-video stability. Extensive evaluations on five benchmarks covering 46 generator variants demonstrate state-of-the-art overall performance against 16 representative baselines, while robustness experiments confirm strong resilience to twelve real-world video perturbations. Code and models will be released at this https URL.

---


> [!TIP]
> 当前位于：**451-500**（第 10/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
