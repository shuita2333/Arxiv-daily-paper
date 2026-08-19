# 📦 其他研究 | 2026年08月20日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-173**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-173**

---

### 151. [AppendiGrade: An XAI-Enhanced Deep Learning Framework for Grading Appendicitis in Ultrasound with Gaussian Blur and Grad-CAM](https://arxiv.org/abs/2608.17923)

**<font color=#1a73e8>作者：</font>** Fahad Ahammed, Omar Faruq Shikdar, Navid Zaman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Appendicitis is one of the most common abdominal emergencies worldwide and requires prompt diagnosis and treatment to prevent life-threatening conditions. However, accurately differentiating complicated cases, such as perforation or abscess formation, from uncomplicated appendicitis remains a significant clinical challenge. Among other methods, ultrasound is a safer and more cost-efficient diagnostic technique because of the lack of radiation exposure. In this research, an advanced system capable of automatically detecting complicated appendicitis from ultrasound images was developed. A dataset consisting of 4679 ultrasound images with 5 classes, namely perforated, abscess, acute, appendicolith, and normal, was used for the proposed model training and testing. Four pretrained deep learning models, DenseNet201, InceptionV3, ConvNextTiny, and VGG19, have been employed for detecting and classifying complicated appendicitis. In the initial configuration, InceptionV3 achieved the second highest accuracy, with a value of 69.21%. Owing to suboptimal performance with raw images, further optimization techniques, including image preprocessing, hyperparameter tuning, model fine-tuning, and image sharpening, were applied. These enhancements significantly improved the model's performance, with an accuracy of 95.58% for InceptionV3. The model performance is then explained with gradient-weighted class activation mapping (Grad-CAM), which creates a heatmap of the regions responsible for the model's prediction of the infected areas. This could make crosschecking with experts much easier.

---


### 152. [A Theoretical Framework for Parallel Lifelong MAPF Using Group Decentralized Planning](https://arxiv.org/abs/2608.17928)

**<font color=#1a73e8>作者：</font>** Alex DeWeese, Jiaoyang Li, Guannan Qu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In the Lifelong Multi-Agent Path Finding (L-MAPF) problem, agents must repeatedly move from one destination to another while avoiding obstacles and inter-agent collisions. Widely regarded as one of the highest-performing solutions to this problem is the Rolling-Horizon Collision Resolution (RHCR) framework. However, commensurate with its quality solutions, it incurs a computational cost that limits its applicability to even modest agent counts. In this paper, leveraging theoretical methods from the Locally Interdependent Multi-Agent MDP literature, we first theoretically prove the near-optimality of RHCR in a discounted MDP formulation of the L-MAPF problem. Then, we leverage these results to naturally motivate an extended framework called Group Decentralized RHCR (GD-RHCR) which incorporates a group decentralized structure that partitions agents based on a transitive communication scheme and plans for each partition of agents in parallel. We show that both RHCR and GD-RHCR achieve similar exponentially close to optimal guarantees, establishing a theoretical duality between the time based restrictions performed by vanilla RHCR and the additional space based partitioning performed by GD-RHCR. Lastly, we show that across varying maps, GD-RHCR is able to attain high throughput that scales into higher agent counts while maintaining a significantly lower per plan cost.

---


### 153. [Adaptive Policy Portfolios for Robust Markov Decision Processes](https://arxiv.org/abs/2608.17929)

**<font color=#1a73e8>作者：</font>** Kasper Engelen, Sebastian Junges, Guillermo A. Pérez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robust Markov decision processes optimize one policy against a set of plausible transition functions. This can be conservative when the unknown dynamics are fixed and become partially identifiable after deployment. We study adaptive policy portfolios: finite sets of memoryless randomized policies synthesized offline and paired with a lightweight online selector. Robust regret is a natural measure of portfolio quality: for each plausible environment, it measures the loss of the best portfolio member relative to the policy that would have been optimal had that environment been known. Related regret objectives were studied by Ghavamzadeh et al. (2016) with an emphasis on approximations and relaxations for safe policy improvement. We give a complexity-theoretic account of portfolio certification and synthesis. Certifying a given portfolio is $\forall\mathbb{R}$-complete already for deterministic portfolios in acyclic (s,a)-rectangular RMDPs. Synthesizing a portfolio of unary-bounded size is $\exists\forall\mathbb{R}$-complete for general rational polytopes, even with fixed discount and acyclic dynamics. The single-policy case is already hard, both combinatorially and algebraically. Finally, we present an offline portfolio construction that is amenable to runtime specialization.

---


### 154. [Collective Counterfactual Planning: Coordination, Consent, and Verification under Representational Constraints](https://arxiv.org/abs/2608.17932)

**<font color=#1a73e8>作者：</font>** Chainarong Amornbunchornvej  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Groups routinely complete projects that no single member can plan, execute, or verify alone. We propose a formal model of this phenomenon, Collective Counterfactual Planning (CCP), in which the binding limitation on each agent is neither capability, knowledge, nor observability, but representational geometry: each agent perceives the state, conceives moves, consents to actions, and certifies goal requirements only through a projection onto an agent-specific subspace of a common task space. Four gates jointly determine whether a team can reach a conjunctive goal and legitimately recognize that it has done so: the exogenous implementation coalitions required to perform each action, together with three representational gates -- conception, consent, and task-relative verification qualification. We define the Collective Counterfactual Solvability (CCS) problem, separating geometric feasibility, executable attainment, and validated completion. The results expose a positive-negative duality. Iterated cross-agent relay can unlock a solution that no one-shot pooling of individual plans contains, but any goal requirement depending essentially on the subspace dark to the entire team is unverifiable and therefore not validly completable, even when the trajectory accidentally attains it. Memoryless and audited consent further constrain different objects -- action directions versus cumulative trajectory states -- and neither dominates the other. A four-step exhaustive horizon-bounded solvability scheme is sound and complete under exact representation of the relay closure; restricted implementations remain sound on returned plans but need not be complete. The model gives one geometry for sequential mutual enabling, competent execution of steps whose purpose is invisible to the executor, forced sub-teaming at expertise boundaries, and completion that cannot be validly declared.

---


### 155. [Beyond Instrument Motion: Recognizing Tissue Tension Toward Surgical Skill Assessment](https://arxiv.org/abs/2608.17935)

**<font color=#1a73e8>作者：</font>** Marko Haralovi, Zhiqi Miao, Alexander Machiel Bont 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical performance assessment in minimally invasive surgery largely relies on manual expert review, making it time-consuming, subjective, and difficult to scale. While existing surgical video understanding methods address tasks such as instrument segmentation, surgical phase recognition, and action recognition, they do not explicitly capture fine-grained tissue handling, a key indicator of surgical quality. To address this gap, we introduce tissue tension recognition, a new clinically motivated video understanding task for laparoscopic and robot-assisted rectal cancer surgery. To support this task, we construct SurgTension, the first expert-annotated tissue tension dataset, providing a benchmark for objective tissue tension recognition. We further propose TensionTRAC, a lightweight trajectory-based framework that models tissue tension from sparse point trajectories. Using a compact trajectory encoder, TensionTRAC achieves competitive performance against strong pretrained video backbones.

---


### 156. [Cross-Domain Generalization in Machine Unlearning via Label-Conditioned Energy Magnitude Regularization](https://arxiv.org/abs/2608.17942)

**<font color=#1a73e8>作者：</font>** Syed Ali Ahmed, Syed Bilal Ahsan, Muhammad Zaigham Zaheer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning removes the influence of specific data from a trained model. However, most methods treat the forgotten concept as isolated. In this paper, we study what happens to the rest of the model when a class is forgotten, using a label-conditioned energy-based model (EBM) that assigns per-class energies, making the effect directly observable. We forget a class by raising the energy of its image-label pairs, training with a forget term, a retain anchor to the pretrained model, a global margin, and an energy regularizer that stops the energy magnitudes from growing without limit. A propagation term applies the same forget signal to retain samples, weighted by each sample's DINOv2 similarity to the forget class, so forgetting reaches images that resemble it and leaves the rest untouched. We evaluate on two benchmark datasets: 1) On a subset of DomainNet across four visual domains, we forget tiger, lion, and scissors one at a time. Forgetting a class in the sketch domain also erases it from real, clipart, and painting, with forgetting error reaching 98% and 99% for lion and scissors, and the effect carrying over to the most similar class. 2) On CIFAR-10, we turn off the propagation term and forget each of the ten classes on its own. Forgetting is complete (100%), while the other nine classes retain 98.5% of their pre-unlearning accuracy on average.

---


### 157. [Towards Zero-Shot Task Transfer with Neurosymbolic World Models](https://arxiv.org/abs/2608.17959)

**<font color=#1a73e8>作者：</font>** Isidoro Tamassia, Lennert De Smet, Giuseppe Marra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, without assumptions on the structure of the underlying environment. While expressive, these models are generally task-dependent: they learn uninterpretable latent representations that are tied to the training task and thus hard to generalize to new tasks. In this work, we present a novel world model formulation where the reward prediction only depends on a subset of structured, symbolic components of the whole latent state. Decoupling observation reconstruction and reward prediction allows us to learn world models that can adapt zero-shot, i.e. without further environment interactions, to new reward functions defined over the same symbolic state space. We discuss the main advantages and challenges of learning these neurosymbolic world models and demonstrate the strong generalisation properties of our approach over purely neural methods.

---


### 158. [SFMformer: A Spatial-Frequency Modulation Transformer for Lightweight Image Super-Resolution](https://arxiv.org/abs/2608.17966)

**<font color=#1a73e8>作者：</font>** Chih-Hsiang Yang, Chia-Min Lin, Ching-Yu Tsai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse attention mechanisms, which score all token pairs but propagate only the strongest, now underpin the most efficient Transformers for lightweight image super-resolution. This paper observes that sparsification changes what it means to improve such a network. A dense attention layer has one place where representation quality matters: the aggregation of attended features. A sparse layer has two, because the top-k operator first decides which tokens survive and only then decides what to do with them, and a token discarded at the selection stage cannot be recovered downstream. Selection quality and aggregation quality are therefore separable targets, addressed by modules placed before and after the attention respectively. We test this by pairing a dual-branch spatial enhancement on the input of a progressive focused attention with a wavelet-domain modulation on its output, forming SFMformer. Measuring each module alone and jointly over all fifteen benchmark-scale pairs, we find their gains are not additive: the joint gain exceeds the sum of the individual gains on nine pairs, and the sign of the discrepancy is predicted by how much the weaker module contributes on its own (r = -0.72), so the two compound when they relieve different constraints and overlap when they relieve the same one. Enabling spectral modulation once per block rather than once per layer retains the effect at roughly one-sixth of its cost, keeping the model below one million parameters at every scale. SFMformer ranks first on 28 of 30 PSNR/SSIM entries across five benchmarks and three upscaling factors. We report the cases where the pairing does not help, and deploy the model on a Raspberry Pi 5 to confirm the design is practical under tight resource budgets.

---


### 159. [Evaluating and improving crop-yield forecasting methods during extreme drought](https://arxiv.org/abs/2608.17971)

**<font color=#1a73e8>作者：</font>** Shrey Gupta, Yi Ming, George Mohler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The impact of climate variability on food production has led to the creation of various forecasting models that uses machine learning (ML), numerical weather predictors (NWP) or a hybrid of ML-NWP models to identify structural and physical relationships between meteorological drivers and crop growth, in order to predict crop yield. Droughts, for example the 2012 Midwestern US (Corn Belt) drought, are extreme events that affect crop production and test the limits of these forecasting models. Using 16 meteorological drivers as predictors, we compare ML (non-deep learning) and deep learning forecasting models to predict the county-level corn yield for the extreme drought year, 2012. This forecasting problem is characterized by a dissimilarity between the feature distributions of the training and test data, where the meteorological conditions of the extreme drought year fall outside the range of historically observed values. Additionally, the dataset consists of spatial and temporal irregularities where counties with missing yields introduce spatial sparsity and the use of only a subset of daily values per year introduce temporal sparsity. To overcome this, we use sample weighting and feature selection as modifications to improve our forecasting models. These modifications lead to an improvement for ML models; however, the deep learning model VITA shows little to no improvement. While VITA outperforms the ML models with or without modifications, our current study sheds light on the effect of dissimilarity between train and test feature distributions on forecasting models, compares deep learning versus non-deep learning models, and introduces modifications that are effective for non-deep learning models.

---


### 160. [Colour Blinded by the Noise](https://arxiv.org/abs/2608.17976)

**<font color=#1a73e8>作者：</font>** Harriet Mason, Rachel Rogers, Alison Kleffner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Uncertainty visualisation is important for data transparency, especially for map visualisations where data is often aggregated. Despite the importance of this area, studies evaluating uncertainty visualisation lack consensus and produce conflicting results. This work introduces a new evaluation approach for uncertainty visualisation that attempts to assess uncertainty as noise, rather than signal. We evaluate five methods of visualising uncertainty: standard choropleth maps, value/variance bivariate maps, value-suppressing uncertainty palettes, overlaid sampling, and pixelated sampling maps. Built on principles of implicit testing, we put an 'uncertainty visualisation' spin on the classic Ishihara colourblind test to create a novel test that is able to evaluate uncertainty as noise. We compare signal visibility to conventional hypothesis tests at various levels of group separation. By building our experimental design on top of established graphics theory, we isolate the plot components that facilitate successful signal suppression and establish foundational theory for the perception of uncertainty visualisation.

---


### 161. [Dual Co-Train: Cross-Dataset Ultrasound Tongue Segmentation Under Extreme Data Scarcity](https://arxiv.org/abs/2608.17983)

**<font color=#1a73e8>作者：</font>** Alisher Myrgyyassov, Zhen Song, Bruce Xiao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound tongue contour segmentation remains challenging under cross-dataset domain shift, where limited annotations, probe variability, and acquisition noise often degrade model generalization. We present a source-free domain adaptation framework for robust ultrasound tongue segmentation built on a lightweight UltraUNet backbone. Starting from a checkpoint pretrained on only five labeled source images, simulating an underfitted constrained source model, the proposed method adapts to a fully-unlabeled target domain by iteratively refining pseudo-labels, filtering unreliable masks with a contour-based quality-control module, and generating target-style synthetic image-mask pairs through a segmentation-guided conditional GAN. The student model is then trained on a mixture of clean pseudo-labeled target images, noisy pseudo-labels with consistency regularization, and synthetic samples, enabling closed-loop adaptation without access to source data. We evaluate the method on 12 source-target transfer pairs across eight ultrasound tongue imaging datasets, and conduct source-size scaling experiments and ablation studies. Across all comparisons, the proposed framework improves segmentation overlap and contour accuracy over the baselines, including supervised ones. These results suggest that task-specific pseudo-label refinement and synthetic target-style augmentation can substantially improve source-free adaptation for ultrasound tongue imaging.

---


### 162. [GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation](https://arxiv.org/abs/2608.17988)

**<font color=#1a73e8>作者：</font>** Ming Qian, Zijian Wang, Minchao Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many scalable latent 3D generators operate on structured tensors, whereas pre-optimized 3D Gaussian Splatting (3DGS) reconstructions are unordered, spatially irregular, and vary widely in primitive count. We present GS-Voxel, a fitting-free structured latent framework, and evaluate it for large-scale aerial 3D Gaussian scene generation. GS-Voxel deterministically converts a compatible pre-optimized 3DGS reconstruction into sparse active voxels without additional per-scene optimization, retaining the sub-voxel positions and rendering attributes of the selected primitives. A GS-specific factorized VAE then separately encodes voxel geometry and local Gaussian attributes into sparse 3D latents whose size grows with the number of occupied voxels rather than being limited by a fixed scene-wide primitive count. We train image-conditioned flow models in the GS-Voxel latent space to generate aerial 3DGS scenes. A key application enabled by GS-Voxel is large-area scene generation: overlap-aware tiled inference extends synthesis beyond a single training crop conditioned on satellite-view images. Our results show that GS-Voxel provides structured latents for pre-optimized aerial 3DGS reconstructions, with latent capacity that grows with the number of occupied voxels.

---


### 163. [Composing Flow-Matching Energies with Known Physics: Generation, OOD Detection, and Inversion on PDE Fields](https://arxiv.org/abs/2608.18004)

**<font color=#1a73e8>作者：</font>** Yixuan Sun, Anirban Samaddar, Sandeep Madireddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic modeling of physical fields benefits from both a data-driven prior and known physical structure such as the governing equations. Energy-based models (EBMs) are a natural fit since energies compose additively, which enables augmenting physics information during inference. However, EBMs have been difficult to train and sample from due to the intractable partition function. We show in this work that flow matching models with a potential-induced velocity yield an explicit scalar energy at all transport times, whose gradient is exactly the converted learned score and which recovers the marginal negative log-density at the population optimum. The time-dependent energy functions are obtained purely from the matching regression objective on an independent linear Gaussian interpolation, without a variational form or additional MCMC steps, and the sampling retains the flow ODE. Access to the energy function from a trained model serves three roles: energy-corrected data generation, energy as a scoring function for out-of-distribution (OOD) detection, and energy compositional posterior sampling for inverse problems. In particular, we show the explicit energy permits general MCMC samplers in the predictor-corrector sampling framework, reducing PDE residual and spectral distance compared to the flow ODE baseline. Furthermore, we demonstrate utilizing the data energy and physics-based energy (e.g., PDE residuals) as complementary mechanisms to improve detection accuracy for OOD tasks. In addition, we explore the connection to MCMC-based inference for inverse problems by composing the energy with a quadratic observational likelihood that yields a posterior energy, used as an explicitly chosen family of inference-time targets.

---


### 164. [Automated ACL Footprint Identification Using 3D Deep Learning](https://arxiv.org/abs/2608.18012)

**<font color=#1a73e8>作者：</font>** Ruida Cheng, Ali Uneri, Gabriel Gibson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One of the most common reasons for anterior cruciate ligament (ACL) reconstruction failure is femoral tunnel malpositioning (ACL footprint center and tunnel orientation). Such failures may lead to the development of meniscal pathology and osteoarthritis. Accurate ACL femoral footprint identification is therefore essential for precise tunnel placement, restoration of the native knee joint mechanics, post-surgical knee joint health and prevention of graft failure. Recent advances in artificial intelligence (AI) bring new opportunities to improve image-guided orthopedic surgery. However, at present, existing AI research focuses primarily on ACL segmentation and rupture classification based on pre- and post-operative magnetic resonance (MR) images. Identification of the ACL footprint center using deep learning methods has not been thoroughly researched. Thus, the purpose of this study is to explore 3D deep learning models for ACL femoral footprint identification directly from 3D MR images. Two comprehensive 3D deep learning architectures were developed: a 3D graph convolutional neural network-based geometric model applied to 3D femoral meshes; and a 3D landmark-enhanced identification model based on 3D MR images. A total of 4883 right and 3087 left knee image sets were used from a publicly available database. Eighty percent (80%) were applied to model generation, and twenty percent (20%) were preserved for model testing. Both models achieved excellent performance; however, the image-based method outperformed the model-based method (average error of 2.1mm vs 2.8 mm). Thus, 3D deep learning provides a feasible clinical approach for ACL footprint localization and has the potential to improve ACL reconstruction footprint accuracy.

---


### 165. [Revisiting WEASEL 2.0: Reproduction, Sensitivity, and an Adaptive Ensemble-Size Rule](https://arxiv.org/abs/2608.18021)

**<font color=#1a73e8>作者：</font>** Cian Higgins, Gerard Carrigan, Pinar Sungu Isiacik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> WEASEL 2.0 is a dictionary-based time series classifier that combines dilated sliding windows with a randomised hyperparameter ensemble and a fixed-size dense feature representation. Two of its hyperparameter choices, the maximum ensemble size and the maximum window size, are specified by simple thresholding rules whose chosen thresholds are not empirically justified in the original paper. In this work we reproduce WEASEL 2.0 on 114 UCR datasets, achieving a mean accuracy of 0.865 and median of 0.928, closely matching the published values (Wilcoxon signed-rank, p = 0.655). We then test the sensitivity of four design choices: the downstream classifier, the absence of feature weighting, the maximum window-size rule, and the maximum ensemble-size rule. The first three are robust to perturbation. The fourth is over-provisioned for long-series datasets, motivating an adaptive rule that sets the maximum ensemble size from series length and number of classes. Evaluated on fixed-length datasets, the adaptive rule reduces peak fit memory by a median of 37 MB (mean 395 MB) and fit time by a median of 0.4 s (mean 4 s), with a median accuracy change of 0% (mean -0.11%). Memory and time savings concentrate on long-series datasets where the original rule allocates the largest ensemble size.

---


### 166. [TabNSM: Neural Sparse Mixer for Tabular Regression](https://arxiv.org/abs/2608.18026)

**<font color=#1a73e8>作者：</font>** Ali Eslamian, Qiang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale, high-dimensional tabular regression remains challenging: tree-based models are robust but lack end-to-end representation learning, while deep models enable flexible feature learning but often incur costly interaction modeling and sensitivity to noisy or redundant features. We propose TabNSM, a scalable regression framework that extends our earlier sparse-attention and mixer architectures. At its core, the Adaptive Sparse Interaction Module (ASIM) integrates foreground feature discovery, sparse local interaction encoding, and Feature-Token Mixing, providing near-linear complexity under fixed sparse configurations. For regression, TabNSM introduces three complementary components: a Multi-Stage Regression Head for progressive prediction refinement; GridLoss, an ordinal-aware soft-binning objective that incorporates target structure into representation learning; and RISE (Reweighted Instance Sampling by Error), a difficulty-aware sampling strategy based on loss-quantile bins. Across nine real-world regression benchmarks, TabNSM delivers strong predictive performance and practical scalability, with particularly consistent gains on high-dimensional and heterogeneous datasets. These results demonstrate that selective interaction modeling, structured regression supervision, and difficulty-aware sampling provide an effective and scalable approach to deep tabular regression.

---


### 167. [Initialization-Free Bundle Adjustment Revisited: A Controlled Experimental Study](https://arxiv.org/abs/2608.18028)

**<font color=#1a73e8>作者：</font>** Simon Weber, Mateo de Mayo, Je Hyeong Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Initialization-free bundle adjustment (InitFree BA) aims to recover camera poses and scene structure directly from image observations, avoiding the geometric initialization stages of conventional structure-from-motion pipelines. Recent methods based on Object-Space Error (OSE) formulations and Variable Projection (VarPro) show encouraging optimization behavior from random camera configurations. However, existing evaluations primarily measure optimization success, leaving unclear whether a low OSE objective yields a valid metric 3D reconstruction. We revisit InitFree BA experimentally through a unified evaluation framework combining a C++ implementation of existing OSE formulations with a Blender-based dataset generator providing exact ground truth and controlled camera configurations and observation densities. Our experiments reveal a previously overlooked optimization--reconstruction gap: projective solutions with similarly low OSE values can lead to substantially different Euclidean reconstructions after metric upgrade. We identify initialization priors, landmark observation density, and metric-upgrade stability as key factors governing reconstruction success. Overall, our results suggest that the main challenge of InitFree BA is not merely minimizing OSE objectives, but obtaining projective reconstructions that admit reliable metric upgrade. We believe that the proposed benchmark, implementation, and analysis establish stronger experimental foundations for future research on initialization-free bundle adjustment, a problem largely unexplored within the computer vision community. Project page is available at this https URL.

---


### 168. [Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization](https://arxiv.org/abs/2608.18040)

**<font color=#1a73e8>作者：</font>** Travis Zhang, Christian Belardi, Justin Lovelace 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from a diffusion model typically requires many forward passes through a large neural network, making generation computationally expensive. While much work has focused on efficient solvers and samplers, comparatively little attention has been paid to selecting the sampling timesteps themselves. A recent line of work optimizes theoretically derived surrogates for sample quality rather than the quality metric itself. We propose Optimizing Your Sampling (OYS), which instead treats timestep selection as a black-box optimization problem, optimizing the target metric directly with Bayesian optimization. OYS outperforms both the default schedules and those of Align Your Steps on text-to-image generation, and improves over the default schedules on inpainting and other image tasks, in both quantitative and human evaluations. OYS requires no additional training, is applicable even to distilled models, and improves both simple and sophisticated samplers such as Euler and DPM-Solver++. A 5-step OYS schedule retains 89%-94% of the quality of a 50-step schedule while reducing inference cost by 10x.

---


### 169. [HLSR: Hybrid Live Forecast Selective Dynamic Vehicle Rerouting for Real-Time Congestion Avoidance](https://arxiv.org/abs/2608.18056)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Shun Ren Yang, Hui Nien Hung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban traffic congestion reduces productivity and increases travel cost and emissions. Network-wide live travel-time shortest-path rerouting can be highly effective in simulation, but assumes that essentially every on-road vehicle is replanned every decision period. We propose HLSR, a selective hybrid live--forecast vehicle rerouting framework that fuses live edge speeds with short-horizon forecasts under limited intervention scope. Building on dual-threshold congestion detection, calibrated upstream selection, and driver-tailored travel-time prediction, HLSR further introduces approaching-vehicle expansion, travel-time-weighted k-shortest-path generation, and a horizon-dependent hybrid live--forecast segment speed used in multi-cost route allocation.

---


### 170. [The concentration game: Bayesian updating, regret, and information](https://arxiv.org/abs/2608.18061)

**<font color=#1a73e8>作者：</font>** Akshay Balsubramani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a two-player zero-sum repeated game between a learner and nature whose value identity generates Bayesian updating and an exact accounting of exponential-weights regret at once, and supplies the comparator-class variational form that a wide class of concentration phenomena share. The terminal payoff is the most a comparator can gain at fixed relative entropy from the prior, and the one-step constraint is an information budget on nature's move under the learner's mixed action. With the learner's move otherwise unrestricted, Gibbs/Bayes weights emerge as its unique Bellman equalizer -- the mixed action that makes the per-round loss independent of which direction nature moves -- with log-partition functions playing the role of value functions. The regret decomposes exactly into three parts: a per-round information loss reflecting the variation in observed outcomes, an additive retempering drift that accounts exactly for any change of measurement scale between rounds, and the information the comparator carries relative to the prior. The variance and bounded-range proxies that drive standard regret bounds are looser relaxations of this decomposition, which holds generally and governs them all. Both players' strategies are read off from the decomposition term by term, and repeated play yields an information-theoretic ledger of self-play in place of the usual quadratic-variation surrogate. The same comparator-class geometry accounts for the classical large-deviation bounds, and methods across bandits, posterior sampling, aggregation, and boosting are specializations of the one regret decomposition.

---


### 171. [EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing](https://arxiv.org/abs/2608.18063)

**<font color=#1a73e8>作者：</font>** Jiayi Song, Shijie Huang, Fangtai Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution image editing is increasingly demanded in professional workflows, yet existing diffusion-based models remain constrained to resolutions below 1K due to quadratic attention complexity and prohibitive memory requirements. A prevalent workaround employs a two-stage pipeline: editing at low resolution followed by independent super-resolution. However, this approach suffers from two critical issues: information divergence, where hallucinated details contradict the original high-resolution (HR) source, and texture degradation, manifesting as over-smoothed or over-sharpened artifacts. We propose EditBridge, a diffusion bridge framework for efficient ultra high-resolution editing. Unlike conventional diffusion that regenerates from noise, we formulate refinement as structured data-to-data translation from the low-resolution (LR) edited result to its HR counterpart, explicitly conditioned on the original HR source to preserve authentic details. To efficiently incorporate HR source guidance, we introduce a prior-guided block-wise sparse attention mechanism that exploits semantic correspondence from first-stage editing to constrain cross-image interactions to spatially aligned regions, significantly reducing computational overhead. Extensive experiments demonstrate that EditBridge achieves high-fidelity editing with superior perceptual quality at resolutions up to 4K, delivering 3.6--8.4$\times$ speedup at 2K and enabling practical 4K editing in 61 seconds.

---


### 172. [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](https://arxiv.org/abs/2608.18066)

**<font color=#1a73e8>作者：</font>** Qinyuan Ye, Yu Li, Yada Pruksachatkun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-based self-improving agents--those that learn from an online stream of tasks and improve over time by maintaining a textual memory bank--have shown great promise in recent literature. However, the reliability aspects of these methods have been critically overlooked. In this work, we conduct a comprehensive re-evaluation of two memory-based methods, broadening the scope of evaluation along two axes: (1) including multiple runs to quantify variance, and (2) randomly shuffling the tasks to investigate the effect of task order. Through these experiments, we make two observations that expose the fragility of current methods: First, agent evaluation is inherently noisy in complex environments and on multi-step tasks, and stacking a self-improving loop on top can further amplify this noise. Second, the agent's improvement is highly dependent on task order. Prior works often adopt default orderings that impose an implicit curriculum, acting as a hidden prerequisite for success.
To better understand this fragility, we manually examine the agents' memory and hypothesize that task and environment underspecification contribute to this fragility. We validate this hypothesis by incorporating information that enables better specification, such as detailed rubrics and environment feedback, into the memory construction process. While this added information partially closes the performance degradation in previous experiments, significant gaps still remain, suggesting that other uncharacterized factors contribute to this fragility. Looking ahead, our work advocates for more rigorous evaluation protocols for self-improving agents by reporting results across multiple runs and stress-testing them under challenging conditions. Moreover, our findings on underspecification call for systems and interfaces that enable effective human oversight, preventing agents from failing in unforeseeable ways.

---


### 173. [From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation](https://arxiv.org/abs/2608.18076)

**<font color=#1a73e8>作者：</font>** Xingjian Wang, Zhao Wang, Taihang Hu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A central challenge is not only how to curate each task-specific corpus, but also how to organize heterogeneous supervision according to the dependencies among generative capabilities. We present a \textbf{capability-driven data infrastructure} that couples capability-specific supervision construction with capability-aligned curriculum scheduling. Its three specialized yet interoperable data engines build complementary relational supervision for text-image grounding, inter-image transformation, and image-knowledge association, while caption experts align T2I and editing supervision across tasks and granularities. A multi-stage curriculum jointly evolves task composition, visual-concept distribution, data quality, and image resolution along the dependency order of capability acquisition, with capability-aware evaluation closing the loop through targeted retrieval, expert construction, and gap-aware resampling. At scale, the framework curates a 440M-image T2I corpus, 120M editing pairs, and over 27M image-entity pairs. With this infrastructure, we train multimodal diffusion models at two scales from scratch, with 3B and 6B sizes respectively. We conduct quantitative evaluation on CPI-Bench, along with qualitative evaluations across diverse text-to-image and editing scenarios. Experimental results present broad visual coverage, versatile rendering, and effective transfer across generative capabilities.

---


> [!TIP]
> 当前位于：**151-173**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-173**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
