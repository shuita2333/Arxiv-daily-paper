# 📦 其他研究 | 2026年06月05日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 1. [Early Detection of Alzheimer's Disease Using Explainable Machine Learning on Clinical Biomarkers: A Multi-Class Classification Study Using the Alzheimer's Disease Neuroimaging Initiative (ADNI) Dataset](https://arxiv.org/abs/2606.03995)

**<font color=#1a73e8>作者：</font>** Afshan Hashmi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Alzheimer's disease (AD) affects over 55 million people worldwide. Accurate, interpretable detection of normal cognition (NC), mild cognitive impairment (MCI), and AD from routine clinical assessments remains a critical unmet need. Methods: An XGBoost classifier was developed for three-class detection using eight clinical features from the Alzheimer's Disease Neuroimaging Initiative (ADNI): MMSE, CDR Global, CDR Sum of Boxes (CDR-SB), MoCA, FAQ, age, sex, and education. Hyperparameters were optimised using Optuna (50 trials); class imbalance was addressed with SMOTE. Performance was evaluated by macro AUC-ROC with 1,000-iteration bootstrap 95% confidence intervals, macro F1, balanced accuracy, and Cohen's kappa. SHAP values provided feature-level explainability. Results: The dataset comprised 1,641 baseline subjects (608 NC, 767 MCI, 266 AD). On five-fold cross-validation, mean macro AUC was 0.983 (SD 0.007), accuracy 0.944 (SD 0.006), and macro F1 0.929 (SD 0.008). On the held-out test set (n = 247), macro AUC was 0.982 (95% CI: 0.965--0.995), accuracy 0.943, balanced accuracy 0.932, macro F1 0.927, and Cohen's kappa 0.909. SHAP analysis identified CDR Global as the dominant predictor for NC and MCI, while CDR-SB and MMSE together drove AD classification. Conclusion: An explainable machine learning model trained on routine clinical assessments achieves near-perfect three-class Alzheimer's detection. SHAP analysis reveals clinically plausible, class-specific feature importance patterns supporting clinical validity. Future work will extend this framework with speech biomarkers for multimodal detection.

---


### 2. [Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning](https://arxiv.org/abs/2606.04028)

**<font color=#1a73e8>作者：</font>** Andrew Fitzgibbon, Christoph M. Wintersteiger, Jeffrey Sarnoff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The IEEE P3109 draft standard defines a parameterized family of binary floating-point formats and associated operations, with a focus on facilitating machine learning. These formats allow efficient and consistent representation of values in a small number of bits. The defined formats are parameterized over width and precision in bits, signedness, and the presence of infinities. Operations are defined by decoding floating-point values to the set of closed extended reals: the reals augmented with positive and negative infinity and NaN (Not a Number). Explicit treatment of NaN and infinite operands ensures that only real arithmetic is invoked in operation definitions. Extensive rounding and saturation modes are defined; stochastic rounding is included. Operations are exception-free, accelerating throughput, with exceptional situations communicated through return values, e.g., NaN. Operations on blocks of values sharing a common scale factor are defined in terms of the underlying operations in a uniform manner. System vendors may describe approximate implementations via a novel scale-invariant measure, akin to units in the last place, called kappa-approximation. Standard function definitions and various other properties are mechanically verified and generated using formal specifications.

---


### 3. [Position: Deployed Reinforcement Learning should be Continual](https://arxiv.org/abs/2606.04029)

**<font color=#1a73e8>作者：</font>** Parnian Behdin, Kevin Roice, Golnaz Mesbahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has received increasing attention and adoption in real-world use cases. Most of these systems follow a train-then-fix paradigm, where trained agents do not learn while interacting with the world until performance degrades and retraining becomes necessary. In this position paper, we argue that deploying an agent that is incapable of optimality, but receives an evaluative reward signal, is inherently a continual RL problem. We identify four sources of non-stationarity after deployment that necessitate never-ending learning, and highlight why the best deployed agents never stop adapting. We analyze successful examples of continual RL in the real world, and present the community with the advantages and measures to move away from the current train-then-fix paradigm.

---


### 4. [Pseudospectral Bounds for Transient Amplification in Coupled Gradient Descent](https://arxiv.org/abs/2606.04031)

**<font color=#1a73e8>作者：</font>** Ahanaf Hasan Ariq  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coupled gradient descent--where the update of one parameter block depends on another--underlies bilevel optimization, two-time-scale stochastic approximation, and adversarial training. When the coupled Jacobian is block-triangular, asymptotic stability is governed by the spectral radii of the diagonal blocks, yet transient amplification before convergence can be arbitrarily large due to non-normality. We develop a sharp pseudospectral theory for such block-triangular Jacobians, proving that the Kreiss constant satisfies $K(J) \leq 2/(1-\gamma) + \|C\|/(4(1-\gamma))$ when the diagonal blocks are symmetric with spectral radii at most $\gamma < 1$, and we establish matching minimax lower bounds. We characterize the critical coupling threshold for spectral instability and extend the analysis to nearly self-referential systems via a Neumann-series perturbation framework. As a consequence, we obtain a finite-horizon iteration-complexity bound of $O(K(J)^2 \log(1/\delta))$ for stochastic coupled descent. Framed as scaling laws for non-stationary two-time-scale optimization, our results expose a non-asymptotic, instance-dependent regime of high-dimensional learning dynamics that is invisible to spectral-radius analysis. Experiments on linear-quadratic problems, IQC-based comparisons, and neural-network training confirm the theory.

---


### 5. [Do Transformers Need Three Projections? Systematic Study of QKV Variants](https://arxiv.org/abs/2606.04032)

**<font color=#1a73e8>作者：</font>** Ali Kayyam, Anusha Madan Gopal, M Anthony Lewis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role. However, the individual contribution of these three projections and the impact of omitting some remain poorly understood. We systematically evaluate three projection sharing constraints: a) Q-K=V (shared key-value), b) Q=K-V (shared query-key), and c) Q=K=V (single projection). The last two variants produce symmetric attention maps; to address this, we also explore asymmetric attention via 2D positional encodings. Through experiments spanning synthetic tasks, vision (MNIST, CIFAR, TinyImageNet, anomaly), and language modeling (300M and 1.2B parameter models on 10B tokens), we discovered that our transformers perform on par or occasionally better than the QKV transformer. In language modeling, Q-K=V projection sharing achieves 50% KV cache reduction with only 3.1% perplexity degradation. Crucially, projection sharing is complementary to head sharing (GQA/MQA): combining Q-K=V with GQA-4 yields 87.5% cache reduction, while Q-K=V + MQA achieves 96.9%, enabling practical on-device inference. We show that Q-K=V preserves quality because keys and values can occupy similar representational spaces and attention operates in a low-rank regime, whereas Q=K-V breaks attention directionality. Our results systematically characterize projection sharing as an underexplored instance of weight tying in attention, with direct, quantifiable inference memory benefits, particularly valuable for edge deployment. The code is publicly available at this https URL

---


### 6. [Inverse Critical Experiment Design via Gradient Optimization and a Multigroup Attention-Based Neural Network Architecture](https://arxiv.org/abs/2606.04033)

**<font color=#1a73e8>作者：</font>** Will Savage, Logan Burnett, Dean Price  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The validation of advanced nuclear reactor designs and fuel concepts requires critical experiments with high neutronic similarity to the target technology. Neutronic similarity is quantified by the correlation coefficient $c_k$, which captures the shared bias in $k_\text{eff}$ induced by uncertainties in nuclear data. Generally, a $c_k\geq0.9$ is needed for an experiment to be sufficiently similar to a target technology. This work presents a methodology for the inverse design of critical experiments. Deep neural network surrogate modeling and nonparametric gradient optimization are used to generate experiment geometries that maximize $c_k$.
A deep neural network is trained on OpenMC-calculated sensitivity vectors for grid-based critical experiment geometries. The model architecture combines a U-Net convolutional encoder-decoder with a novel multigroup attention pooling layer, introduced to capture the differing spatial dependencies of sensitivities. Multigroup attention pooling is shown to achieve better performance than traditional pooling, as well as interpretable internal behavior. The differentiability of the surrogate enables gradient-based optimization of the full combinatorial design space, allowing $c_k$ to be maximized by directly changing the material assignment of each position in the geometry grid.
The method is applied to the validation of the TN-Americas TN-LC transportation cask with HALEU fuel, for which existing critical experiment coverage is limited. The optimization procedure is shown to produce experiment geometries achieving $c_k$ scores of 0.97757, 0.81324, and 0.93276 for three configurations of interest. This approach demonstrates the potential of deep learning and gradient optimization to accelerate the development of advanced nuclear technology.

---


### 7. [Self-Distilled Policy Gradient](https://arxiv.org/abs/2606.04036)

**<font color=#1a73e8>作者：</font>** Yifeng Liu, Shiyuan Zhang, Yifan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation, where a language model conditions on privileged context to supervise its own generations, is a promising source of dense supervision for sparse-reward reinforcement learning. Actually, it can be instantiated as an auxiliary full-vocabulary student-to-teacher reverse Kullback-Leibler divergence loss. We therefore propose SDPG, a self-distilled policy-gradient framework that combines group-relative verifier advantages with normalized standard deviation, exact full-vocabulary on-policy self-distillation, as well as reference-policy KL regularization. Empirically, SDPG improves stability and performance over RLVR and self-distillation baselines. The code is available at this https URL.

---


### 8. [Bayes-Sufficient Representations in Supervised Learning](https://arxiv.org/abs/2606.04045)

**<font color=#1a73e8>作者：</font>** Vasileios Sevetlidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning is often described as preserving the information in an input that is relevant for prediction. This work asks what relevance means for a fixed supervised decision problem. A representation is defined to be Bayes-sufficient for a joint distribution and loss if some prediction head can use it to implement a Bayes-optimal action rule. This makes the target information loss-dependent. In the almost-surely unique Bayes-action case, the relevant object is a Bayes quotient, which identifies inputs that require the same Bayes-optimal action. A representation is sufficient when it refines this quotient, and Bayes-minimal when it is informationally equivalent to it. The framework connects naturally to property elicitation: zero-one loss requires the Bayes class, squared loss the conditional mean, Brier loss the conditional probability in binary prediction, and log loss or strictly proper scoring rules the predictive distribution. Controlled finite experiments, learned neural bottleneck experiments, and a real-data iNaturalist taxonomic refinement experiment illustrate the distinction between sufficiency, minimality, and retained non-required information. For a fixed supervised problem, the distribution and the loss determine the Bayes action, the Bayes action determines the quotient, and the quotient determines the minimal information required for Bayes-optimal prediction.

---


### 9. [Dive into the Scene: Breaking the Perceptual Bottleneck in Vision-Language Decision Making via Focus Plan Generation](https://arxiv.org/abs/2606.04046)

**<font color=#1a73e8>作者：</font>** Boyuan Xiao, Bohong Chen, Yumeng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In embodied vision-language decision making tasks such as robotic manipulation and navigation, Vision-Language and Vision-Language-Action Models (VLMs & VLAs) are powerful tools with different benefits: VLMs are better at long-term planning, while VLAs are better at reactive control. However, their performance is limited by the same perceptual bottleneck: visual hallucinations arise due to the models' inability to distinguish task-relevant objects from distractors. In principle, accurate identification and focus on critical objects while filtering out irrelevant ones is the key to break this limitation. A straightforward solution is one-step focus: directly attending to essential objects. However, this approach proves ineffective because effective focus inherently requires deep scene understanding. To this end, we propose SceneDiver, a coarse-to-fine focus plan generation method for VLMs leveraging their long-term planning abilities, that first constructs a holistic scene graph to establish initial comprehension, then progressively decomposes the task into simpler sub-problems through an iterative cycle of recognition, understanding, and analysis. To enable reactive control, we also design a lightweight adapter for distilling the deliberate focus ability into VLAs. Evaluations on standard embodied AI benchmarks confirm that our method substantially reduces visual hallucinations for both VLMs and VLAs, while preserving computational efficiency in tasks requiring fast execution. Our code and data are released at: this https URL.

---


### 10. [Unlocking Feature Learning in Gated Delta Networks at Scale](https://arxiv.org/abs/2606.04048)

**<font color=#1a73e8>作者：</font>** Yifeng Liu, Quanquan Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training and scaling Large Language Models demand enormous computational resources, motivating both efficient sub-quadratic architectures and principled hyperparameter tuning methods. While the Maximal Update Parametrization ($\mu$P) has enabled zero-shot hyperparameter transfer for standard Transformers, its extension to linear models, particularly those with structured state transitions and complicated architectures, remains largely unexplored. By rigorously propagating coordinate-size estimates through the forward pass, gating mechanisms, and recurrent state dynamics, we derive the scaling rules for Gated Delta Network. Experiments on language-model pre-training confirm that our configurations enable stable learning-rate transfer across model widths under both AdamW and SGD, whereas standard parametrization fails to transfer, validating the correctness and practical utility of our analysis.

---


### 11. [A Goal-Set Characterization of Task Composition in the Boolean Task Algebra](https://arxiv.org/abs/2606.04053)

**<font color=#1a73e8>作者：</font>** Eduardo Terrés-Caballero, Herke van Hoof  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Boolean Task Algebra (BTA) provides a principled framework for zero-shot task composition in reinforcement learning by equipping goal-reaching tasks with Boolean operations. We revisit its structural assumptions and formalize a collapse in the space of optimal extended Q-value functions: in deterministic MDPs, every such function is fully determined by the universal and empty tasks. This makes the logarithmic set of base tasks proposed in the original BTA formulation redundant. Building on this observation, we introduce a goal-set-based composition method that performs logical operations on goal sets and reconstructs composed value functions by selecting slices from the universal and empty value functions. This reduces learning costs for standard BTA and reduces composition time for both BTA and Skill Machines, while preserving policy performance. Experiments across tabular, visual, function-approximation, and continuous-control domains show that learning additional base tasks does not yield better performance. Finally, we study the stochastic setting and provide a counterexample showing that this collapse need not hold, that is, optimal composition may require accounting for exponentially many policies in the number of goals. Code is available at this https URL.

---


### 12. [Spectral Scaling Laws of Muon](https://arxiv.org/abs/2606.04058)

**<font color=#1a73e8>作者：</font>** Gagik Magakyan, Pablo Parrilo, Asuman Ozdaglar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthonormalized update rules have rapidly become a leading choice of optimizer for training large language models, with recent open-source state-of-the-art models adopting Muon. To keep these updates tractable, Muon performs the orthonormalization with the Newton--Schulz (NS) iteration. Since NS is only approximate, directions with small singular values fail to be orthonormalized. In Muon, NS is applied to the momentum matrix at every step, yet little is known about how the singular value spectrum of these momentum matrices behaves during training, or how that behavior changes with model size. We present the first systematic study of this question. Tracking singular value quantiles of the momentum buffer across layers in models ranging from 77M to 2.8B parameters, we observe a consistent picture: after a short burn-in, the quantiles stabilize at a value determined by the layer type and model size. These stabilization values follow remarkably clean power laws in model size, with layer-dependent exponents. Layers up to mid-late depth scale very mildly with model size $M$ (around $M^{-0.25}$), so the standard 5-step NS configuration used at academic scale will continue to orthonormalize them at much larger scales. Some of the late layers, however, scale much more aggressively (up to $M^{-0.96}$) and will fall into the NS failure regime at frontier scale unless one uses more NS iterations or better-tuned coefficients. NS iterations are computationally expensive at scale; our laws give practitioners a principled, layer-aware recipe for choosing the minimum NS configuration that still orthonormalizes the directions that matter -- avoiding unnecessary computation without sacrificing update quality.

---


### 13. [Weakly Supervised Incremental Segmentation via Semantic Anchors and Spatial Arbitration](https://arxiv.org/abs/2606.04060)

**<font color=#1a73e8>作者：</font>** Zhonggai Wang, Kai Fang, Guangyu Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly Incremental Learning for Semantic Segmentation (WILSS) suffers from the continuous introduction of noisy supervision, which progressively corrupts class-level representations, leading to severe feature drift and semantic corruption, thereby causing newly learned classes to overwrite old ones. To address these issues, we propose a drift-resilient WILSS approach, named SASA, designed to stabilize semantic learning via Semantic Anchors and Spatial Arbitration. Specifically, at the representation level, we introduce semantic anchors of learnable tokens as rigid class-level references to preserve long-term semantic identity. Complementary to this, an elastic residual adaptation facilitates controlled, instance-specific refinement, ensuring a stable yet flexible learning trajectory. At the supervision level, we develop a Spatial Label Arbitration mechanism that performs geometry-aware decisions to directly filter unreliable signals and enforce a strict "one object, one class" constraint. By synergistically stabilizing representations and improving supervision reliability, SASA effectively mitigates feature drift under weak supervision. Extensive experiments on standard benchmarks demonstrate that our approach consistently outperforms existing state-of-the-art methods, particularly in challenging multi-step incremental settings. The code is available at this https URL.

---


### 14. [Intra-Modal Neighbors Never Lie: Rectifying Inter-Modal Noisy Correspondence via Graph-Based Intra-Modal Reasoning](https://arxiv.org/abs/2606.04061)

**<font color=#1a73e8>作者：</font>** Yang Liu, Wentao Feng, Shu-Dong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale web-harvested datasets have fueled the progress of cross-modal retrieval but inevitably suffer from noisy correspondence, which severely degrades model generalization. Existing methods primarily address this by filtering out noise or seeking a substitute label, yet they predominantly remain bound by a "Discrete Selection" paradigm. We argue that relying on a single discrete proxy induces Single-Point Fragility and Discretization Error. To overcome these limitations, we propose a novel framework, Intra-modal Neighbor-aware Noise Rectification (IN2R), which shifts the paradigm from searching for a substitute to synthesizing a reliable supervision target. Leveraging the intrinsic geometric stability of intra-modal data, IN2R employs a Graph Refiner to perform relational reasoning over neighbors retrieved from a dynamic Cross-Model Memory. Instead of propagating discrete labels, our method synthesizes a continuous, soft prototype that reflects the consensus of the local semantic neighborhood, effectively rectifying inter-modal misalignment. Extensive experiments on Flickr30K, MS-COCO, and CC152K demonstrate that IN2R significantly outperforms state-of-the-art methods. Our code and pre-trained models are publicly available at this https URL.

---


### 15. [Bayesian Membership Privacy for Graph Neural Networks](https://arxiv.org/abs/2606.04069)

**<font color=#1a73e8>作者：</font>** Sinan Yıldırım, Megha Khosla  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing privacy analyses for Graph Neural Networks (GNNs) largely inherit assumptions from non-graph settings, overlooking structural correlations and stochastic training-graph sampling. In particular, node-dependent priors make type-I and type-II errors alone insufficient to characterize the best membership inference test. To address this, we introduce Bayesian Membership Privacy (BMP), a sampling-aware formulation of node-level membership privacy that incorporates node-dependent priors and treats graph sampling probabilities as part of the adversary's knowledge. BMP casts membership inference as a Bayesian hypothesis test and accordingly quantifies membership privacy in terms of posterior membership probability. We explore theoretical properties of BMP in relation to the existing definitions in the literature. We further propose a practical, sampling-aware auditing mechanism to estimate the parameters of BMP as a measure of node-level privacy leakage in GNNs. We conduct experiments on benchmark graph datasets and show that BMP yields fine-grained privacy insights that are not visible through global attack accuracy alone.

---


### 16. [TPA-AD: A Two-Stage Pseudo Anomaly-Guided Method for Bearing Time-Series Anomaly Detection](https://arxiv.org/abs/2606.04073)

**<font color=#1a73e8>作者：</font>** Xiancheng Wang, Zhibo Zhang, Ran Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a two-stage pseudo anomaly-guided anomaly detection method (\textbf{T}wo-stage \textbf{P}seudo \textbf{A}nomaly-guided \textbf{A}nomaly \textbf{D}etection, \textbf{TPA-AD}) for axle-box bearing time-series anomaly detection (time series anomaly detection, TSAD) under the setting where only normal samples are available for training. The method first generates pseudo-anomalous windows near the normal boundary using a reconstruction model and per-feature target-error control. It then learns anomaly-sensitive representations through contrastive learning between normal and pseudo-anomalous windows, and finally produces window-level and point-level anomaly scores using k-nearest neighbors (KNN). Compared with existing methods that rely on known fault categories, real anomaly priors, or random anomaly injection, TPA-AD improves the separability of the normal boundary by constructing pseudo-anomalies in boundary neighborhoods and can jointly handle continuous and discrete features in mixed-variable scenarios. The main experiments are conducted on bearing fault detection datasets and degradation-process datasets, with an additional exploratory extension on $13$ public TSAD datasets. The results show that the proposed method yields relatively stable anomaly responses, is sensitive to degradation evolution, and demonstrates a certain degree of broader applicability on public TSAD benchmarks and real high-speed-train-related bearing data.

---


### 17. [Adaptive Patching Is Harder Than It Looks For Time-Series Forecasting](https://arxiv.org/abs/2606.04074)

**<font color=#1a73e8>作者：</font>** Federico Zucchi, Yi Xie, Chao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive patching is a recent and compelling proposal for time-series Transformers: allocate finer patches where the sequence looks locally informative. This paper asks under what conditions a content-adaptive patching operator should outperform a tuned uniform one. Local heterogeneity alone is not enough: under pointwise forecasting losses, a complex-looking region is not automatically one where finer patching reduces the loss. We model patching as a budgeted bitrate allocation and derive an explicit threshold that a dynamic patching rule must satisfy to beat a well-tuned uniform baseline, then bound the achievable improvement both locally (a quadratic surrogate) and globally (a strong-convexity bound under the model's assumptions). Two structural results follow: without a coupling constraint, scalar local complexity cannot produce a non-uniform optimum under a common loss landscape; and once the backbone is trained to its representation-aware optimum, the alignment gain collapses around a well-tuned uniform patch size. To test these predictions, we run a controlled isolation study on three representative architectures, replacing each adaptive mechanism with a uniform patch-size sweep while keeping the backbone, data, and training protocol fixed. On standard long-horizon forecasting benchmarks, the validation-selected uniform baseline is competitive with the dynamic counterpart, with per-setting effects concentrated near zero and no consistent directional advantage once results are aggregated by dataset. The larger gains we do observe are method- and dataset-specific. Adaptive patching should therefore be evaluated against a tuned uniform baseline; its value depends on whether a cheap and reliable routing signal can identify where finer patches actually reduce forecasting loss.

---


### 18. [Optimal Transport Flow Matching by Design](https://arxiv.org/abs/2606.04092)

**<font color=#1a73e8>作者：</font>** Shimon Malnick, Matan Rusanovsky, Ohad Fried 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching models learn to transport samples from a simple prior distribution to a complex data distribution. When prior-data pairs are coupled via optimal transport (OT), the learned trajectories are straight and non-crossing, enabling fast, even single-step, generation. However, computing the OT coupling in high dimensions is intractable, and existing methods attempt to solve the OT problem, at the cost of persistent bias or significant overhead. Rather than solving for the OT coupling, we reformulate the problem. Once the prior is treated as a design choice rather than a fixed input, the OT coupling between prior and data is no longer unique. Many priors admit an OT-optimal identity coupling to the data, leaving us free to choose one that is also tractable to sample. We identify low-frequency projection of natural images as such a choice. The identity coupling between data and its low-frequency representation is empirically OT-optimal, the prior is structured enough to be sampled by a lightweight model at inference, and the remaining flow-matching task reduces to synthesizing high-frequency detail. Interpolating the prior with Gaussian noise further improves generation quality while preserving the OT coupling. The approach requires no modifications to the flow model itself, and integrates naturally with latent-space models, classifier-free guidance, and one-step generation frameworks. Across all benchmarks, our method reduces trajectory curvature by more than $2\times$ compared to existing flow matching methods, yielding better generation quality in the few-step regime.

---


### 19. [POLARIS: Guiding Small Models to Write Long Stories](https://arxiv.org/abs/2606.04095)

**<font color=#1a73e8>作者：</font>** Rishanth Rajendhran, Jenna Russell, Mohit Iyyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small open-weight models struggle at long-form creative writing: their generated stories either fall far short of the requested length, or their quality significantly degrades as length increases, especially when compared to frontier models. We present POLARIS (Policy Optimization with LLM-as-a-judge rewards and Anchored-Reference Injection for Storywriting), a lower-compute GRPO recipe with two key ingredients: a frontier LLM judge with a structured Story Quality rubric as the online reward, and human-reference injection (HRI), where a teacher-forced human-written story serves as a high-reward anchor within each GRPO group. By applying our training recipe to Qwen3.5-9B, using a dataset of approximately 1.4K prompt-story pairs derived from 100 short-story anthologies and 4 A100 GPUs, we obtain POLARIS-9B. Across five benchmarks spanning in-distribution and out-of-distribution prompts and rubrics, POLARIS-9B is competitive with much larger open-weight models while following length instructions more closely. A blinded human evaluation confirms that POLARIS-9B is preferred to the base Qwen3.5-9B and on par with Qwen3.5-27B. Despite training only on stories up to 4k words, POLARIS-9B preserves quality on prompts requesting stories up to 3 times the training length, a regime where most open-weight models degrade substantially in quality, length adherence, or both. More broadly, our results suggest that length generalization is a meaningful stress test for creative-writing models and a useful lens for distinguishing otherwise close models.

---


### 20. [When Seeing Is Not Believing -- A Benchmark for Search-Grounded Video Misinformation Detection](https://arxiv.org/abs/2606.04098)

**<font color=#1a73e8>作者：</font>** Tao Yu, Yujia Yang, Shenghua Chai 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video misinformation increasingly operates at the semantic and evidential level: authentic footage may be selectively edited, temporally reordered, spliced across sources, or augmented with AI-generated content to construct false narratives. Such evidence-dependent manipulations cannot be reliably verified from the input video alone, because the missing, reordered, replaced, or recontextualized evidence lies outside the video itself. We introduce \textbf{EVID-Bench}, a benchmark for search-grounded video misinformation detection, where a system must search the open web for related videos and identify what information is false through cross-video comparison. EVID-Bench comprises 222 videos spanning 9 manipulation types across 3 categories: AI generation, single-source editing, and multi-source editing. All samples are verified to be undetectable by frontier models through visual inspection alone. We evaluate nine frontier multimodal models using a retrieval-augmented verification baseline. The best system achieves only 61.43\% point-level accuracy and 43.24\% video-level accuracy, while AI-generated manipulations remain especially challenging. Error analysis reveals recurring challenges: models fixate on irrelevant anchors, misattribute synthetic content to editorial splicing, and terminate search prematurely before fully explaining the manipulation.

---


### 21. [Stein Kernelized Molecular Dynamics for Active Learning of Interatomic Potentials](https://arxiv.org/abs/2606.04100)

**<font color=#1a73e8>作者：</font>** Joanna Zou, Fraser Birks, Dallas Foster 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning interatomic potentials (MLIPs) enable efficient and accurate atomistic simulations but depend critically on the quality and diversity of the training data. We introduce Stein kernelized molecular dynamics (SKMD), an enhanced sampling method that uses interacting particle dynamics to acquire informative training configurations for the active learning and fine-tuning of MLIPs. SKMD corresponds to a stochastic variant of Stein variational gradient descent that is adapted for molecular dynamics by incorporating asynchronous particle updates and a kernel of global atomic descriptors, which provides a symmetry-aware measure of configurational similarity. Unlike other enhanced samplers used in molecular dynamics, SKMD preserves the Boltzmann distribution as the asymptotic distribution of the dynamics. This property enforces a balance between the exploration of diverse configurations and attraction toward high-probability regions of the energy landscape. We further propose an approach to efficient online data acquisition using an adaptive stopping criterion that selects non-redundant training data over the course of simulation. We demonstrate SKMD for the active learning of a neural network model of the Müller-Brown potential and the fine-tuning of a MACE interatomic potential for alanine dipeptide. Compared to active learning baselines, our method achieves higher model accuracy in fewer training iterations with the same number of acquired training samples.

---


### 22. [Building The Ph(ysical)AI Layer Of Machine Intelligence](https://arxiv.org/abs/2606.04106)

**<font color=#1a73e8>作者：</font>** Ulbert Jose Botero, Liam Smith, Brooks Olney 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models achieve generalization through massive-scale training on diverse data, but have limitations with transfer to truly unseen domains without paired training data. We propose principle-driven foundation models that encode signal-theoretic principles (Fourier decomposition, energy conservation, symmetry) rather than learn untethered statistical correlations. We hypothesize that domains differ not in fundamental physics, but in learnable transformations in time, frequency, magnitude, or phase. Training exclusively on radio-frequency (RF) data with co-designed architecture and losses incorporating these principles, we achieve cross-modal transfer to audio, images, text, and video using only frozen representations learned from RF data, requiring no fine-tuning of the encoder on target domains. Our 1.99M parameter frozen encoder achieves 77.7% average accuracy (91.9% top-3) across 15 diverse tasks via linear probing, with systematic variation: 84.5 on physically-grounded tasks (speaker recognition, seismology, RF fingerprinting) versus 70.0% on semantic tasks (music genre, language recognition). This reveals that principle-driven and scale-driven approaches offer complementary paths: physical principles enable efficient cross-modal transfer while naturally establishing the boundary between physical and semantic understanding.

---


### 23. [Reflection Separation from a Single Image via Joint Latent Diffusion](https://arxiv.org/abs/2606.04107)

**<font color=#1a73e8>作者：</font>** Zheng-Hui Huang, Zhixiang Wang, Yu-Lun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image reflection separation is highly challenging under extreme conditions like glare or weak reflections. Existing methods often struggle to recover both layers in glare or weak-reflection scenarios because of insufficient information. This paper presents a diffusion model explicitly fine-tuned for this task, leveraging generative diffusion priors for robust separation. Our method simultaneously generates transmission and reflection layers through a unified diffusion model, incorporating a novel cross-layer self-attention mechanism for better feature disentanglement. We further introduce a disjoint sampling strategy to iteratively reduce interference between the layers during diffusion and a latent optimization step with a learned composition function for improved results in complex real-world scenarios. Extensive experiments demonstrate that our approach surpasses state-of-the-art methods on multiple real-world benchmarks. Project page: this https URL

---


### 24. [Variance Reduction for Heavy-Tailed Monetization Metrics in Ranking Experiments via Post-Stratification](https://arxiv.org/abs/2606.04110)

**<font color=#1a73e8>作者：</font>** Neeti Pokharna, Olivier Jeunen, Yatharth Saraf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online evaluation of ranking and retrieval systems often relies on downstream monetization metrics such as app revenue or creator earnings. These metrics are typically heavy-tailed, with a small fraction of users dominating both mean and variance, leading to low statistical power and unreliable conclusions in A/B experiments -- especially under limited traffic.
We present a practical framework for variance reduction in online experiments by combining post-stratification with CUPED. Our approach leverages pre-experiment covariates to improve the sensitivity of monetization experiments without requiring additional traffic. Deployed at ShareChat across ranking-driven monetization experiments, the method substantially reduces variance and improves decision stability, achieving equivalent statistical confidence with ~45\% less traffic than standard metrics. We further discuss practical design choices, guardrails, and limitations, providing guidance on when post-stratification is appropriate for real-world information retrieval and Recommendation systems.

---


### 25. [SaliMory: Orchestrating Cognitive Memory for Conversational Agents](https://arxiv.org/abs/2606.04120)

**<font color=#1a73e8>作者：</font>** Kai Zhang, Xinyuan Zhang, Hongda Jiang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational agents that serve as lifelong companions must maintain persistent memory across all interactions. However, simply expanding context windows with raw retrieval degrades reasoning quality, while training memory agents via standard reinforcement learning creates a severe credit assignment bottleneck in a multi-stage pipeline. To solve this, we introduce SALIMORY, a framework that trains a single language model to manage a cognitively-structured memory-spanning user facts, preferences, and working memory. By introducing a hierarchical stage-wise process reward and reward-decomposed contrastive refinement, SALIMORY provides isolated supervision for distinct memory operations (selective filtering, consolidation, and cue-driven recall) end-to-end. SALIMORY cuts memory-attributed failures by one-third, outperforms the state-of-the-art by over 10% in end-to-end accuracy, and more than doubles the Good Personalization rate.

---


### 26. [Pinpoint: Grounded Worldwide Image Geolocation via Cross-Source Retrieval and Reranking](https://arxiv.org/abs/2606.04133)

**<font color=#1a73e8>作者：</font>** Nika Chuzhoy, Brian Hu, Amit A. Arora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image geolocation aims to estimate where a photograph was taken from its visual content. At worldwide scale, this remains challenging because visual evidence is often ambiguous, diverse, and unevenly distributed. Prior work has typically treated geolocation of ordinary internet photos and street-view imagery as separate tasks, despite their complementary strengths: internet photos better match the appearance distribution of user-captured queries, while street-view imagery provides denser, geographically grounded coverage. We present Pinpoint, a retrieve-and-rerank architecture that combines both sources in a coarse-to-fine pipeline. A contrastive image-GPS embedder is trained on both user-uploaded Flickr photos and street-view imagery, learning a shared image-GPS embedding space that is used to retrieve candidate locations. An attention-based reranker then rescores retrieved candidates by combining candidate-level visual and GPS features with cross-source evidence from nearby locations to ground the prediction. Unlike recent prior work, Pinpoint does not rely on multimodal large-language models, making inference faster and more reproducible. Pinpoint achieves state-of-the-art results across all metrics on standard benchmarks for internet photos (IM2GPS3k and YFCC4k) and street-view imagery (OSV-5M).

---


### 27. [Stationarity-Aware Retrieval-Augmented Time Series Forecasting](https://arxiv.org/abs/2606.04135)

**<font color=#1a73e8>作者：</font>** Shiqiao Zhou, Holger Schöner, Zipeng Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting relies on historical patterns, but real-world series often exhibit non-stationarity and regime shifts that challenge fully parametric forecasters. Inspired by Retrieval-Augmented Generation (RAG), recent work augments forecasters by retrieving relevant historical segments and using them as external evidence at inference time. However, due to the intrinsic non-stationarity of real-world time series, a highly similar past segment does not necessarily imply a similar future, rendering similarity-only retrieval brittle and prone to redundancy. We propose Stationarity-Aware Retrieval-Augmented Time Series Forecasting (SARAF), a framework that adaptively balances relevance and diversity in retrieval. SARAF first forms a candidate pool via temporal similarity with time-aligned enhancement, then applies a diversity-aware selection strategy to cover heterogeneous historical regimes, with the diversification strength automatically modulated by dataset-level stationarity. Moreover, SARAF uses stationarity-aware aggregation to fuse the retrieved futures. Extensive experiments on eight real-world datasets show that SARAF achieves competitive forecasting performance and improves average accuracy and robustness over strong baselines, with particularly clear benefits under challenging non-stationary settings. Code: this https URL.

---


### 28. [Physics-Informed Machine Learning for Short-Term Flood Prediction](https://arxiv.org/abs/2606.04143)

**<font color=#1a73e8>作者：</font>** Tewodros Syum Gebre, Jagrati Talreja, Leila Hashemi-Beni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate flood forecasting is essential for mitigating disaster risks and protecting communities. However, purely data-driven machine learning models often struggle in data-scarce environments and may violate fundamental hydrological principles. Standard Long Short-Term Memory (LSTM) networks can generate physically inconsistent predictions, particularly when extrapolating to extreme weather conditions. To address these limitations, we propose a Physics-Informed Machine Learning (PIML) framework that incorporates hydrological knowledge directly into the loss function of an LSTM model. Specifically, a Trend Alignment constraint penalizes directional inconsistencies between precipitation and discharge trends, improving model robustness without requiring complex hydrodynamic equations. This regularization encourages the model to learn physically plausible hydrograph behavior, even with limited training data, while enhancing reliability during peak flood events. Experimental results show that the proposed physics-informed model outperforms a standard LSTM baseline in data-scarce settings, increasing the Nash-Sutcliffe Efficiency (NSE) from 0.20 to 0.23 when trained on only 5% of the available data. Additional stress tests under simulated extreme climate scenarios demonstrate that the baseline model exhibits unstable behavior, whereas the physics-informed model maintains directional consistency and physical plausibility. Although accurately predicting extreme peak magnitudes remains challenging with limited data, the proposed approach substantially reduces unphysical fluctuations common in purely data-driven models. These findings demonstrate that simple physical constraints can significantly improve the reliability of deep learning models for real-time flood forecasting, offering a practical solution for ungauged basins and evolving climate conditions.

---


### 29. [Stumbling Into AI Emotional Dependence: How Routine AI Interactions Reshape Human Connection](https://arxiv.org/abs/2606.04150)

**<font color=#1a73e8>作者：</font>** Yaoxi Shi, Cathy Mengying Fang, Pattie Maez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public discourse and emerging policy typically assume that AI emotional support is a deliberate act: a lonely user consciously seeking comfort from a dedicated companion chatbot. In this paper, we draw on emerging empirical evidence and argue that this picture is inaccurate on two accounts, both in how AI emotional support arises and how it shapes future behavior. First, AI emotional support commonly emerges incidentally within task-oriented interactions on general-purpose platforms, much as workplace friendships deepen through collaboration. Second, these incidental encounters are path-dependent: positive experiences of AI emotional support update people's beliefs about AI's emotional capabilities and redirect their choices for future emotional support, increasing preference for AI and decreasing preference for humans. We review recent evidence, including a large-scale longitudinal study conducted in collaboration with OpenAI, showing that daily five-minute conversations with an AI about personal issues over 28 days led to a 10.3% decrease in the preference for seeking support from humans and an 11.6% increase in the preference for AI. These findings suggest that current policy, focused on companion apps and isolated interactions, cannot adequately protect human connection. Instead, effective regulations should extend to general-purpose AI systems and address cumulative, trajectory-level changes in how people seek support. Recognizing how people stumble into AI emotional support and how those encounters redirect human connections over time is essential to safeguarding human well-being.

---


### 30. [When Offline Selectors Cannot Beat the Best Single Model: A Diagnostic Study on edX Dropout Prediction](https://arxiv.org/abs/2606.04161)

**<font color=#1a73e8>作者：</font>** Tyler Crosse, Alan Nadelsticher Ruvalcaba, Dustin Khang LeDuc 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Different predictors often excel on different inputs, so picking the best one per instance promises higher accuracy than committing to a single model. In practice, selectors trained from logged data routinely fail to beat the strongest single predictor. Three causes typically go unseparated before more tuning is applied: a mismatched learner, a state that does not predict which model wins, or buffer-to-deployment label shift.
A three-stage diagnostic rules them out on a shared buffer. Stage~1 estimates a local ceiling on oracle recovery from $k$-NN label consistency. Stage~2 asks whether paired BC and offline-RL learners (BC, DQN, and CQL across penalty weights) reach that ceiling. Stage~3 ablates the selector state to test whether richer features would raise it. The combined verdict points to the most promising next step: tuning the learner, redesigning the state, or collecting new data.
We apply it to selecting among five dropout-prediction models on edX clickstream data. Across 16 windows, the oracle beats the strongest single base model by 9.7 accuracy points on average, yet BC, DQN, and CQL land in the same test-accuracy band below it (robust to a tenfold buffer sweep and $N{=}2{,}000$ held-out examples). The bottleneck is local representational ambiguity: CQL closes the imitation gap without a deployment gain (not conservatism), regret clusters tightly across learners (not tie-breaking), and the three learners converge on test accuracy (not shift). The next iteration should change the state or collect new data, not tune the offline learner further.

---


### 31. [End-to-End Text Line Detection and Ordering](https://arxiv.org/abs/2606.04166)

**<font color=#1a73e8>作者：</font>** Benjamin Kiessling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Practical text-recognition pipelines for historical documents typically decompose layout analysis into line detection followed by a separate reading-order step, with the latter most often handled by a hand-coded geometric heuristic that struggles with marginalia, multiple columns, tables, and source-specific editorial conventions. This article introduces Orli (Ordered Regression of Lines), an end-to-end model that casts both sub-tasks as a single image-to-sequence problem: from a page image, Orli autoregressively generates text-line baselines directly in reading order. Baselines are represented in a chord-frame parameterization that anchors a line's position, orientation, and extent while encoding local geometry through perpendicular offsets; an iterative refinement head and a local visual refiner produce the final curve. Trained on a heterogeneous corpus of 196,691 pages spanning ten writing systems, Orli marginally exceeds the previously reported state of the art for cBAD line detection without dataset-specific training, reaches near perfect coverage and ordering on multiple reading-order benchmarks zero-shot, and adapts to more specialized out-of-domain layouts with limited fine-tuning. The method's source code and model weights are available under an open license at this https URL.

---


### 32. [Smart Transportation Without Neurons -- Fair Metro Network Expansion with Tabular Reinforcement Learning](https://arxiv.org/abs/2606.04167)

**<font color=#1a73e8>作者：</font>** Dimitris Michailidis, Sennay Ghebreab, Fernando P. Santos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We tackle the Metro Network Expansion Problem (MNEP), a subset of the Transport Network Design Problem (TNDP), which focuses on expanding metro systems to satisfy travel demand. Traditional methods rely on exact and heuristic approaches that require expert-defined constraints to reduce the search space. Recently, deep reinforcement learning (Deep RL) has emerged due to its effectiveness in complex sequential decision-making processes-it remains, however, computationally expensive, environmentally costly, and requires additional engineering to interpret. We show that MNEP problems are small enough to not require Deep RL methods. Reformulating the MNEP as a Non-Markovian Rewards Decision Process (NMRDP), we use tabular RL to achieve similar performance with significantly fewer training episodes, additionally offering greater interpretability. Additionally, we incorporate social equity criteria into the reward functions, focusing on efficiency and fairness, highlighting the versatility of our method. Evaluated in real-world settings-Xi'an and Amsterdam-our method reduces total episodes by a factor of 18 and total carbon emissions by a factor of 12 on average, while remaining competitive with Deep RL. This approach offers a replicable, modular, interpretable, and resource-efficient solution with potential applications to other combinatorial optimization problems.

---


### 33. [Low-rank Distributional Matrix Completion](https://arxiv.org/abs/2606.04176)

**<font color=#1a73e8>作者：</font>** Jiayi Wang, Raymond K. W. Wong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a distributional generalization of the matrix completion problem in which each entry of the target matrix is a probability distribution rather than a scalar. In this setting, only a subset of matrix entries is observed, and even for observed entries, the underlying distributions are not directly accessible; instead, we observe finitely many samples drawn from them. To represent distributional entries, we employ kernel mean embeddings and introduce a notion of Tucker rank for distribution-valued matrices to capture their low-rank structure. The infinite-dimensional nature of kernel embeddings poses significant methodological challenges. To address this, we introduce functional unfolding operators that link the proposed distributional low-rank structure to the classical Tucker rank for finite-dimensional tensors. Based on this framework, we propose a novel estimator for distributional matrix completion. We establish non-asymptotic error bounds that characterize the statistical performance of the estimator. Extensive experiments on synthetic data and a real-world application demonstrate the effectiveness of the proposed method.

---


### 34. [A Systematic Analysis of Linguistic Features in AI-Generated Text Detection Across Domains and Models](https://arxiv.org/abs/2606.04177)

**<font color=#1a73e8>作者：</font>** Yassir El Attar, Esra Dönmez, Maximilian Maurer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretable linguistic features offer a promising approach for explaining why a given text appears machine-generated, particularly for non-expert users. However, existing findings on which features reliably indicate LLM-generated text remain fragmented across feature sets, models, and text domains. To address this gap, we conduct a large-scale empirical study assessing the robustness of linguistic signals for characterizing AI-generated text. Our analysis covers 284 interpretable linguistic features across outputs from 27 LLMs and ten text domains under cross-model and cross-domain generalization settings. We show that classifiers based solely on linguistic features can reliably distinguish AI-generated from human-written text. However, many previously proposed indicators prove strongly context-dependent, with the exception of measures of lexical richness, which remain robust signals across model families and text domains. These results demonstrate which linguistic signals generalize across contexts and provide a foundation for more reliable, interpretable analyses of AI-generated language.

---


### 35. [Exact Unlearning in Reinforcement Learning](https://arxiv.org/abs/2606.04182)

**<font color=#1a73e8>作者：</font>** Thanh Nguyen-Tang, Raman Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate the problem of \emph{exact unlearning} in reinforcement learning, where the goal is to design an efficient framework that enables the removal of any user's data upon deletion request, i.e., the online learner's output after unlearning is \emph{indistinguishable} from what would have been produced had the deleted user never interacted with the learner. For any $\rho >0$, we show that there exists a reinforcement learning (RL) algorithm that is $\rho$-TV-stable and supports an exact unlearning procedure whose expected computational cost is only a $\rho \sqrt{\ln T}$ fraction of the computational cost of retraining from scratch. We construct such a $\rho$-TV-stable RL algorithm for tabular Markov decision processes (MDPs), which achieves a regret bound of $\mathcal{O}(H^2 \sqrt{SAT} + H^3 S^2 A + {H^{2.5} S^2 A}/{\rho})$, where $S, A, H$, and $T$ denote the number of states, the number of actions, the episode horizon, and the number of episodes, respectively. We also establish a lower bound of $\Omega(H\sqrt{\!SAT}\! +\! {SAH}/{\rho})$ for $\rho$-TV-stable RL algorithms, showing that our algorithm is nearly minimax optimal.

---


### 36. [Dual Advantage Fields](https://arxiv.org/abs/2606.04188)

**<font color=#1a73e8>作者：</font>** Alexey Zemtsov, Maxim Bobrin, Alexander Nikulin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned reinforcement learning requires both long-horizon reachability estimates and local action comparisons. Dual goal representations provide value fields that capture global goal reachability, but they do not directly specify which action should be preferred at a given state. We propose Dual Advantage Fields, a policy-extraction method that turns a bilinear dual value model into a local advantage signal. Under bilinear dual parameterization, the goal embedding is the gradient of the value field with respect to the state representation. DAF learns an action-effect model that predicts the discounted feature displacement induced by an action and scores actions by the alignment between this displacement and the goal direction. In the realizable case, this score equals the goal-conditioned Bellman advantage, yielding a standard local policy-improvement guarantee. On OGBench locomotion, manipulation, and puzzle tasks, DAF improves aggregate RLiable metrics and performs strongly in settings where locally correct actions differ from direct movement toward the final goal.

---


### 37. [ACAT: A Collaborative Platform for Efficient Aspect-Based Sentiment Dataset Annotation](https://arxiv.org/abs/2606.04189)

**<font color=#1a73e8>作者：</font>** Ana-Maria Luisa Mocanu, Ciprian-Octavian Truica, Elena-Simona Apostol  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-Based Sentiment Analysis (ABSA) requires high-quality datasets to train reliable models. However, existing annotation tools treat output as flat files, leaving researchers to manually consolidate multi-annotator data, reconstruct relational structures, and compute reliability metrics through custom scripts. This paper introduces ACAT (Aspect-based sentiment analysis Collaborative Annotation Tool), a web-based platform natively supporting four ABSA workflows: (1) Aspect-Category Sentiment Analysis, (2) Clause-Level Segmentation, (3) Aspect-Term Sentiment Analysis with character-level position tracking, and (4) Aspect Sentiment Triplet Extraction with dual span offset preservation. Its core contribution is an automated Extract, Transform, Load (ETL) pipeline that aligns collaborative annotations and computes Inter-Annotator Agreement (IAA) metrics directly at export, yielding training-ready datasets. In a preliminary validation on 1,002 restaurant reviews with two annotators of differing expertise, ACAT achieves a median annotation time of 31.58 seconds and a raw IAA ranging from 0.78 to 0.86 across all tasks.

---


### 38. [Metric-Aware Hybrid Forecasting for the CTF4Science Lorenz Challenge](https://arxiv.org/abs/2606.04191)

**<font color=#1a73e8>作者：</font>** Cen Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We describe our approach to the CTF4Science Lorenz challenge, a benchmark that mixes short-horizon forecasting, long-time distribution matching, and trajectory reconstruction across nine task pairs. The key discovery is that no single model family dominated all metrics. Instead, we built a metric-aware hybrid system that assigned a different predictor to each metric family: (1) synthetic-pretrained denoisers for full-trajectory reconstruction, (2) Lorenz ODE fitting and trajectory shooting for the first 20 forecast steps, and (3) histogram-tail substitution using synthetic Lorenz libraries for long-time evaluation. A representative mature submission from this system family scored 83.83551 on the public leaderboard, and a small follow-up stack of the same ideas reached 83.85529. We focus on the cleaner intermediate system because it captures the full method while remaining simple enough to reproduce and analyze, while the final submission can be understood as a conservative extension of the same backbone.

---


### 39. [Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions](https://arxiv.org/abs/2606.04193)

**<font color=#1a73e8>作者：</font>** Juan Figuera  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current AI agent observability is structurally compromised: the entity producing the activity log is the same entity whose activity is being logged. A compromised or buggy agent can omit, alter, or fabricate its own traces, and the operator running the agent has no independent way to detect tampering. We propose a class of protocols that resolves this by inverting the trust boundary: the service that receives an agent's call signs a receipt of what it observed using its own key, encrypts the receipt to the agent's owner, and publishes it to a public transparency log. The owner reconstructs a tamper-evident trail without trusting the agent or its operator. We instantiate the class as Sello, a protocol combining four properties absent in any current system: (P1) receiver-side signing, (P2) HPKE encryption to an owner public key bound to the authorization token via JWS, (P3) publication to a witness-cosigned Merkle log, and (P4) owner-side discovery by token reference. We describe the protocol, analyze its security under an adversary that controls the agent and its operator, present microbenchmarks of the cryptographic operations, and situate Sello among adjacent receipt-protocol work (Signet, AgentROA, Agent Passport System, draft-farley-acta, SCITT). We discuss known limitations including the suppression attack, service collusion, and the adoption-incentive problem.

---


### 40. [Training-Free Lexical-Dense Fusion for Conversational-Memory Retrieval](https://arxiv.org/abs/2606.04194)

**<font color=#1a73e8>作者：</font>** Christian Lysenstøen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieving the few past turns that answer a new query across long multi-session histories is the retrieval bottleneck behind long-term conversational memory (LoCoMo, LongMemEval). Recent concurrent work, Nano-Memory, shows that scoring a session by the maximum query-turn similarity (late interaction, "Turn Isolation Retrieval") beats mean-pooled session embeddings. We do not claim that effect; we replicate it and ask what a training-free, CPU-only retrieval stage should add around it. We report four findings. (1) Fuse: score-level fusion of the late-interaction dense score with BM25, under a single leave-one-conversation-out weight, adds +8.8 to +17.2 points of LoCoMo Hit@1 over late interaction alone across six encoders (all p<1e-4), reaching Hit@1 0.752 / NDCG@5 0.829 (e5-large-v2), +11.2 pp over BM25. (2) An off-the-shelf web-search cross-encoder reranker over the fused top-10 hurts here, degrading Hit@1 by 6.9 pp (one reranker, one configuration). (3) A pooling-operator ablation shows top-k late interaction matches max-similarity, but a naive smooth-max (log-sum-exp) collapses for half the encoders. (4) The late-minus-early gap is large for all six encoders and tends to be larger for larger ones, while the marginal fusion gain shrinks; on LongMemEval-S, a lexical regime where BM25 saturates, the net fusion gain over BM25 is small and not significant. A per-category analysis frames the gain as a division of labor: dense late interaction helps most on multi-hop and temporal questions but trails BM25 on adversarial ones. The contribution is a controlled, reproducible account of a strong training-free retrieval recipe, not the late-interaction retriever itself (Nano-Memory's). We make no claim to a complete memory architecture; this is a retrieval-stage study.

---


### 41. [Spatial Artifact Coherence Determines Codec Robustness in Patch-Based rPPG](https://arxiv.org/abs/2606.04198)

**<font color=#1a73e8>作者：</font>** Achraf Ben Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) achieves low heart-rate error on uncompressed benchmarks yet is deployed over compressed video channels in telehealth, neonatal ICU, and driver fatigue applications. No prior work identifies the physical quantity determining when spatial decomposition outperforms global-projection methods under codec compression.
We propose Spatial Artifact Coherence (SAC), defined as the ratio of off-diagonal to diagonal energy in the 4x4 inter-patch Green-channel covariance matrix (bandpass 0.75-2.5 Hz), and the PatchPCA algorithm family (four codec-aware rPPG algorithms). We evaluate 280 subjects across three public datasets, 11 codec degradation variants (MPEG-4, H.265, H.264, JPEG, chroma subsampling), and 13 algorithms via Wilcoxon tests (BH-FDR, q < 0.05, 904 tests).
SAC explains 93.8% of between-variant variance in PCA advantage (r = +0.969), with zero overlap between codec families: non-MPEG-4 variants cluster at SAC 0.10-0.18 with 84-90% PCA win rates, while MPEG-4 variants cluster at SAC 0.48-0.59 with 61% win rate and a 5.8x reduction in mean improvement. Within subjects, 78% confirm the expected pattern (p < 10^-22, dz = 0.73). Within-variant subject-level SAC correlation is r = +0.099, confirming SAC classifies codec families rather than predicting individual outcomes. MPEG-4's effect is structural (macroblock DCT geometry, not noise amplitude), governed by source codec state, not resolution.
P-Hybrid is identified as the most deployment-robust algorithm. Two necessary operating conditions for PatchPCA advantage are established: SAC < 0.30 and low-to-moderate motion, directly ruling out raw-to-MPEG-4 transcoding pipelines. SAC provides a physically grounded metric for codec-aware rPPG algorithm selection in clinical remote monitoring systems.

---


### 42. [Cross-Prompt Generalization in Detecting AI-Generated Fake News Using Interpretable Linguistic Features](https://arxiv.org/abs/2606.04199)

**<font color=#1a73e8>作者：</font>** Aya Vera-Jimenez, Samuel Jaeger, Calvin Ibenye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The increasing use of large language models has raised concerns about the spread of AI-generated fake news, particularly under varying prompting strategies. Most existing detection models are trained and evaluated under a single generation setting, leaving their ability to generalize across unseen prompts unclear. In this study, we investigate cross-prompt generalization in fake news detection using three datasets of AI-generated articles produced under distinct prompts, combined with real news articles. We extract interpretable linguistic features capturing lexical diversity, readability, and emotion-based characteristics and evaluate a random forest classifier under a cross-prompt framework, where models trained on one prompt are tested on another. Across all six train-test combinations, performance remains consistently high, with AUC values ranging from 0.988 to 1.000. Analysis of feature distributions shows that AI-generated text exhibits increased lexical diversity, reduced readability, and substantially lower emotional intensity compared to the overall dataset, with variations across prompts. Despite these distributional shifts, the classifier maintains strong performance, indicating that these features capture stable properties of AI-generated text that generalize across prompting strategies. These findings suggest that feature-based approaches can provide robust detection of AI-generated fake news under prompt variability.

---


### 43. [A Geometric View of Counterfactual Behavior: Interaction of Boundary Proximity and Local Support](https://arxiv.org/abs/2606.04209)

**<font color=#1a73e8>作者：</font>** Ioanna Gemou, Matteo Gamba, Randall Balestriero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations seek small, semantically meaningful changes to an input that alter a model's prediction, and are widely used to interpret and audit machine learning systems. In modern vision, language, and multimodal systems, pretrained encoders map inputs to representation spaces, and downstream classifier heads impose decision boundaries within those spaces. As a result, the feasibility and distance of nearby counterfactuals depend on boundary placement relative to the data. Yet models with similar predictive performance can differ substantially in whether such changes are achievable and how far representations must move. This work examines this variation using a standardized local search probe across several pretrained encoders and linear classifier heads. Results show that despite similar predictive performance, models differ substantially in their counterfactual behavior. Under fixed representations, varying only the classifier head alters counterfactual outcomes while leaving predictive performance largely unchanged. This variation is explained by the interaction of decision-boundary proximity and local data support, which jointly determine whether prediction changes are both feasible and lie in regions supported by the data, and can also improve counterfactual search within fixed models. Together, these findings identify counterfactual behavior as a distinct dimension beyond predictive performance and show that it can be altered without changing accuracy, with implications for model selection, robustness, and the reliability of counterfactual methods.

---


### 44. [Edge of Stability Selectively Shapes Learning Across the Data Distribution](https://arxiv.org/abs/2606.04212)

**<font color=#1a73e8>作者：</font>** Shauna Kwag, Anakha Ganesh, Tomaso Poggio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing analyses of the edge of stability (EoS) treat it as a global property of optimization. We show that it is also selective: the stability constraint redistributes learning across subsets of the training distribution, amplifying progress on some groups while suppressing progress on others. Using a branching intervention that enters or exits the EoS regime from the same training state, we causally demonstrate this trade-off and identify two necessary conditions for a group to benefit. First, its aggregate gradient must align with the top Hessian eigenvector. We isolate this mechanism with a controlled perturbation that preserves distance but randomizes direction, destroying alignment and eliminating the advantage. Second, the group must sustain non-vanishing gradient magnitude over time. Under cross-entropy loss, gradient saturation decouples confidently classified groups, shifting the advantage to output-outliers, whose gradients persist. Together, these results show that EoS functions not only as a stability boundary, but as a mechanism governing the allocation of learning across the data distribution.

---


### 45. [Consensus is Strategically Insufficient: Reasoning-Trace Disagreement as a Knowledge-Representation Signal](https://arxiv.org/abs/2606.04223)

**<font color=#1a73e8>作者：</font>** Michał Wawer, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are commonly designed to reduce disagreement through voting, consensus protocols, debate, or fault-tolerant aggregation. We argue that this objective is insufficient for value-laden tasks, where disagreement may reflect genuine normative uncertainty rather than agent error. Building on prior work on reasoning-trace disagreement in human-AI collaborative moderation, we propose a knowledge-representation layer in which reasoning traces and agent decisions are abstracted into symbolic disagreement states. Given agents producing explicit reasoning traces and binary decisions, we distinguish four states according to reasoning similarity and conclusion agreement: convergent agreement, divergent agreement, convergent disagreement and divergent disagreement. These states support defeasible strategic routing rules. We instantiate the framework in content moderation and argue that disagreement-aware routing provides a bridge between sub-symbolic LLM deliberation and symbolic knowledge representation for multi-agent strategic reasoning.

---


### 46. [Prospective Dynamic 3D MRI Reconstruction via Latent-Space Motion Tracking from Single Measurement](https://arxiv.org/abs/2606.04249)

**<font color=#1a73e8>作者：</font>** Lixuan Chen, Zhongnan Liu, Jesse Hamilton 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prospective reconstruction is crucial in many clinical applications such as MRI-guided radiotherapy, which demands accurate image reconstruction and fast motion estimation from currently acquired measurements. However, prospective reconstruction remains challenging due to ultra-sparse sampling and stringent latency requirements. In this work, we propose PDMR, a Prospective Dynamic 3D MRI Reconstruction framework with latent-space motion tracking. Our core idea is to learn an efficient and generalizable latent manifold of motion fields offline, enabling rapid online adaptation for prospective reconstruction. Specifically, we parameterize the deformation vector fields (DVFs) on a low-dimensional manifold, effectively reducing the search space for fast online adaptation, and employ a tri-plane representation to achieve geometry-aware and memory-efficient encoding of 3D motion. Experiments on both XCAT digital phantoms and in-house abdominal MRI datasets demonstrate that PDMR achieves high-fidelity and temporally consistent reconstruction across multiple prospective scenarios (Immediate and After-2min), outperforming state-of-the-art retrospective and online methods. Our results suggest a promising pathway toward ultra-fast, motion-aware prospective MRI reconstruction in clinical practice.

---


### 47. [SBP-Net: Learning Thin Structure Reconstruction with Sliding-Box Projections](https://arxiv.org/abs/2606.04251)

**<font color=#1a73e8>作者：</font>** Ofir Gilad, Andrei Sharf  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing thin 3D structures is challenging due to their sparsity, scale variation, and complex geometry. Such structures arise in a wide range of domains, including medical imaging of vascular systems and industrial pipe systems. While recent neural methods perform well on dense surfaces, they often fail to recover fine thin geometries. We propose a reconstruction approach based on local depth projections, which provide an efficient and informative 2D representation of thin structures. Specifically, we traverse the 3D model with a sliding box to generate local orthographic depth projections, which are processed by a neural network to reconstruct missing thin structures in 2D. The local reconstructions are subsequently fused back into the 3D model to produce a coherent and detailed shape. Experiments on pulmonary artery reconstruction from CT volumes and industrial pipeline recovery from synthetic and real scans demonstrate improved preservation of fine structural details over existing methods.

---


### 48. [Behavioral and Performance Indicators of Depression and Anxiety in Electronic Learning Systems](https://arxiv.org/abs/2606.04254)

**<font color=#1a73e8>作者：</font>** Arya VarastehNezhad, Fattaneh Taghiyareh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study investigates whether behavioral and performance indicators derived from a Moodle-based learning management system are associated with university students' depression and anxiety in two undergraduate Computer Engineering courses. Using a quantitative observational design, LMS event logs, academic records, and self-reported Beck Depression Inventory-II and Beck Anxiety Inventory scores from 97 students were integrated. A broad set of behavioral and performance indicators spanning temporal engagement, session structure, deadline-related behavior, page-refresh patterns, and LMS navigation was extracted from raw event logs and analyzed using descriptive statistics, independent-samples t-tests with Benjamini-Hochberg FDR correction, effect sizes, and Spearman correlations; inventory scores were confirmed invariant by sex and academic year. Several indicators were significantly associated with depression and anxiety. Higher depression was associated with shifted temporal activity patterns, longer session durations, and shorter homework submission lead times, while higher anxiety was associated with concentrated temporal engagement and session-based differences. These findings suggest that routine LMS data can provide meaningful behavioral signals related to student well-being and may support earlier educational awareness of students who experience mental-health-related strain. At the same time, such indicators should be interpreted as contextual and non-diagnostic markers rather than as substitutes for clinical assessment.

---


### 49. [Can Generalist Agents Automate Data Curation?](https://arxiv.org/abs/2606.04261)

**<font color=#1a73e8>作者：</font>** Feiyang Kang, Hanze Li, Adam Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Curating training data is among the most consequential yet labor-intensive parts of modern AI development: practitioners iteratively propose, implement, evaluate, and revise data policies against noisy benchmark feedback. We ask whether generalist coding agents can automate this data-curation loop. We introduce *Curation-Bench*, an agent-centric benchmark that fixes the model, training recipe, and evaluation suite while giving agents command-line access to inspect data, implement policies, submit them to a fixed training/evaluation pipeline, and revise. In a vision-language instruction-tuning instantiation, out-of-the-box agents reach strong published data-selection baselines within ten iterations. However, trajectory analysis reveals a persistent *execution-research gap*: agents mainly tune local policy variants rather than explore new policy families, even when given strategy guides and paper references. Scaffolds requiring each iteration to cite, instantiate, and adapt a prior method shift agents toward method-guided exploration. The scaffolded agent autonomously composes -- without human design input -- a data-selection policy that outperforms strong published baselines at one-tenth their data budget. Overall, current agents can run the curation loop, but reliable data research requires scaffolded method adaptation, not open-ended prompting alone. Code and benchmark are open-sourced.

---


### 50. [Long-Term and Short-Term Transistor Aging in Deep Neural Networks: Impact and Mitigation](https://arxiv.org/abs/2606.04266)

**<font color=#1a73e8>作者：</font>** Alireza Sarmadi, Virinchi Roy Surabhi, Prashanth Krishnamurthy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) are used in a variety of real-world applications including, for example, image classification and speech recognition. The inference accuracy of DNN implemented on hardware in integrated circuits (ICs) degrades under phenomena such as transistor aging. Aging slows down the switching speed of transistors, resulting in system-level timing violations due to unsustainable clocks. To maintain reliability for the entire projected lifetime, designers add guardbands to prevent timing violations; however, adding large timing guardbands causes losses in performance (speed or throughput). This chapter provides a detailed discussion of the effects of long-term and short-term transistor aging on DNN inference accuracy. Furthermore, to mitigate aging effects on DNN's accuracy and keep them at bay, a methodology for aging-aware retraining is presented in order to generate a resilient DNN even when aggressive (i.e., smaller than required) guardbands are used. This improves the inference accuracy of the DNNs even in the presence of aging-induced degradation. These effects are discussed in this chapter along with mitigation strategies on a hardware implementation of a DNN for image classification on an off-the-shelf image dataset. The application of short-term aging as an excitation mechanism for the detection of hardware Trojans in integrated circuits is also briefly discussed.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
