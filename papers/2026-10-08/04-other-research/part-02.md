# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

---

### 51. [A Data-Centric Review of Plant Disease Datasets: Taxonomy, Critical Analysis, Environmental Variability, and Implications for Precision Agriculture](https://arxiv.org/abs/2610.07087)

**<font color=#1a73e8>作者：</font>** Aamir Hilal, Shabir Ahmad Sofi, Neeraj Goel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advances in artificial intelligence, reliable real-world plant disease detection remains a persistent challenge. Visual and deep learning approaches have shown promising results, but their deployment under field conditions remains limited. A key bottleneck is the reliance on laboratory-generated datasets that lack environmental diversity, realistic backgrounds, and balanced class distributions, resulting in poor generalization. In contrast, datasets collected directly from agricultural environments capture natural variability and better reflect challenges faced by farmers across regions. This review presents a critical analysis of visual and deep learning approaches for plant disease detection, with emphasis on plant disease datasets. It establishes a taxonomy based on acquisition setting, accessibility, plant diversity, disease composition, class structure, and imbalance severity, and examines their implications for model generalization and real-world deployment. A comparative analysis of laboratory and real-field datasets identifies critical gaps that hinder disease detection. The review further analyzes how multi-level dataset imbalance, including intra-class, inter-crop, and cross-dataset imbalance, and limited environmental variability affect model performance and robustness, an area insufficiently examined in existing surveys. Beyond image-based approaches, it highlights the importance of integrating environmental parameters such as temperature, humidity, and leaf wetness with image data to improve prediction under dynamic field conditions. Finally, the review identifies key challenges, research gaps, and future directions concerning dataset construction, environmental variability, structural imbalance, standardization, and multimodal disease monitoring. It provides a foundation for developing next-generation multimodal frameworks for precision agriculture.

---


### 52. [Muon Is Theoretically Wrong For Convolutions, But Empirically Effective](https://arxiv.org/abs/2610.07103)

**<font color=#1a73e8>作者：</font>** Thibaut Boissin, Thomas Massena, Mathieu Serrurier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon, an optimizer known for its efficiency, has a clear interpretation for matrix-valued updates, but convolutional kernels are stored as four-dimensional tensors. Standard implementations reshape these tensors into matrices, a shortcut which breaks the theoretical understanding behind Muon. To investigate this, we formalize the corresponding optimization objective directly in convolutional operator geometry and introduce Convolutional Newton-Schulz (Conv-NS), which approximates the polar factor in this geometry while preserving kernel support. When applied in fast training experiments, Conv-NS and reshape-based Muon are both computationally efficient and achieve comparable accuracy on CIFAR-10 and ImageNet classification tasks. However, as one could expect a theoretically aligned Conv-NS to outperform reshape-based Muon, we investigate this mismatch between practice and theoretical understanding, with the hypothesis that exact convolutional orthogonalization may overconstrain updates. These findings highlight Muon's strong practical performance while opening directions for its further development on convolutions. Our code is publicly available at \href{this https URL}{github conv-muon}.

---


### 53. [MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs](https://arxiv.org/abs/2610.07110)

**<font color=#1a73e8>作者：</font>** Yun Jiang, Bo Zheng, Yingying Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 3D reconstruction of lunar terrain from sparse rover images is indispensable for autonomous lunar exploration, but remains challenging because viewpoint overlap is insufficient, surface textures are weak, and data volume is limited. We propose MoonGS, the first feed-forward 3D Gaussian Splatting framework tailored to lunar scenes. Given only two input images, MoonGS predicts pixel-aligned Gaussian primitives in a single forward pass and renders photorealistic novel views without any per-scene optimization. MoonGS (i) adopts an adaptable backbone design that seamlessly integrates advanced vision foundation models to extract robust depth features; (ii) integrates semantic priors in two manners: merging semantic cues with visual features to refine Gaussian parameter estimation, and adopting a semantic ranking loss that regularizes background depth; and (iii) employs an entropy-guided heuristic resampling strategy to augment sparse observations by selecting the most informative distant viewpoints with negligible overhead. Experiments on the LuSNAR benchmark and our synthetic weak-texture MoonBlender dataset show that MoonGS surpasses state-of-the-art feed-forward NeRF/3DGS baselines by +4.9 dB PSNR, +0.29 SSIM, and 40\% lower LPIPS while maintaining sub-second inference. Furthermore, we validate the broad applicability of our framework by demonstrating that it effectively leverages state-of-the-art backbones, including VGGT, to significantly boost performance. Qualitative evaluations on Chang'e mission imagery also show the best visual quality among compared methods, indicating robustness on real lunar data. The source code and dataset are publicly available at this https URL.

---


### 54. [LiLib: Lifelong Air-to-Ground Path-Loss Prediction on UAVs via a Drift-Triggered Model Library](https://arxiv.org/abs/2610.07111)

**<font color=#1a73e8>作者：</font>** Minh Tran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> UAVs that act as relays or base stations need accurate air-to-ground path-loss predictions for rate adaptation and placement, but propagation conditions change as a UAV moves between suburban, urban and high-rise areas, and the same areas are often revisited. Online regressors that adapt by forgetting must relearn each environment from scratch, whereas a single model trained on all data averages incompatible regimes. We propose LiLib, a lightweight continual-learning scheme in which a UAV maintains a small library of recursive-least-squares experts. A windowed residual test detects drift; a short probe phase then either reuses the best stored expert or creates a new one. In simulations based on four standard urbanization profiles, LiLib reduces prediction RMSE from 5.89 dB (best sliding-window baseline) to 4.03 dB (p < 0.001), lowers the error shortly after a return to a known environment from 12.3 dB to 5.7 dB, and recovers 99% of the throughput of a regime-aware oracle in rate adaptation. The library stores four experts in under 0.5 KB, and identifies regimes with 92% purity without labels. When a second UAV is initialized with the library of a peer, its error after environment changes halves. LiLib does not reach the oracle, and similar regimes may be merged when shadowing is strong. The results indicate that, for recurring drift, remembering is more effective than re-adapting.

---


### 55. [Sample-Optimal Estimation of the Fréchet Inception Distance](https://arxiv.org/abs/2610.07114)

**<font color=#1a73e8>作者：</font>** Ziyun Chen, Jerry Li, Kevin Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Fréchet Inception Distance (FID) is widely used to evaluate generative models, but its empirical plug-in estimator suffers from finite-sample bias [BSAG18, CF20]. We study the sample complexity $n$ of estimating FID to error $\epsilon$ between $d$-dimensional Gaussians with bounded mean distance and covariances, when one distribution is known. Our contributions are threefold. (1) We establish tight finite-sample $\Theta(\frac{d^2}{n})$ bias and $\Theta(\frac{d}{n} + \frac {d^2} {n^2})$ variance bounds for the empirical plug-in estimator, establishing a $\gtrsim d^2$ sample complexity. (2) To debias the empirical plug-in estimator, we generalize the ${\rm FID}_\infty$ estimator of [CF20] to extrapolation methods of arbitrary order $k$. We further prove tight bias and variance bounds of $\Theta(\frac{d^{k + 2}}{n^{k + 1}})$ and $\Theta(\frac d n + \frac{d^2}{n^2})$ for any order-$k$ extrapolation under our framework. (3) We introduce Relative Taylor Debiasing (RTD), a new, computationally efficient FID estimation algorithm using debiasing techniques inspired by U-statistics. We show that RTD achieves an $O(\frac d {\epsilon^2})$ sample complexity, and prove that this is optimal. We provide a complementary empirical evaluation of our new estimators. Our experiments on synthetic Gaussians validate the predicted residual bias and support the tightness of our bounds. On ImageNet with Inception embeddings, RTD achieves the lowest mean estimation error at the standard 50K sample budget, while our second-order variance-aware extrapolation estimator (VALE$_2$) uses only 10K samples to achieve accuracy comparable to FID$_\infty$ at 50K samples.

---


### 56. [R2RI: A Multi-View Event and RGB Dataset for Robot-to-Robot Interaction](https://arxiv.org/abs/2610.07117)

**<font color=#1a73e8>作者：</font>** Gabriele Magrini, Riccardo Catalini, Federico Becattini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and modeling interactions between autonomous agents is a fundamental challenge in robotics, with broad implications for collaborative systems, social robotics, and human-robot coexistence. Although the study of robot interactions has emerged as a compelling research direction, progress has been severely hampered by the absence of large-scale benchmarks. In this paper, we introduce Robot-to-Robot Interaction (R2RI), the first dataset specifically designed to address the Robot-Robot Interaction (RRI) task. R2RI consists of different humanoid robots and realistic interactions modeled on real human social behaviors. Complementary viewpoints are available, \textit{i.e.}, an egocentric perspective from each robot's onboard sensors, and an exocentric perspective from external fixed cameras, thus enabling rich spatial and contextual understanding of the interaction dynamics. The dataset comprises more than $6.5$M frames and $\approx5000$ videos at $120$ fps, including Event and RGB domains. We investigate pros and cons of each domain, comparing state-of-the-art approaches for a number of key sensing and interaction based tasks. We publicly release the dataset and its annotations for all tasks and modalities at this https URL.

---


### 57. [Towards semantic reconstruction of individual words from fnirs using clip loss](https://arxiv.org/abs/2610.07120)

**<font color=#1a73e8>作者：</font>** Santiago Posso-Murillo, Nathan Palladino, Ben Pyykkonen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Semantic reconstruction maps neural activity to a word-embedding space, recovering the meaning of a perceived word instead of selecting it from a fixed vocabulary. Functional near-infrared spectroscopy (fNIRS) carries semantic information suitable for this mapping. However, most fNIRS decoders are trained with a squared-error objective that fits each word independently and ignores the geometry of the embedding space. To address this limitation, we evaluate a contrastive loss based on the contrastive-language-image-pretraining (CLIP) loss, as an alternative to mean-squared-error (MSE) for reconstructing perceived words from fNIRS. We compare the two objectives by training a bidirectional long short-term memory (Bi-LSTM) decoder to map fNIRS signals to word embeddings. We use GloVe-50 and T5 word embeddings as targets, across three fNIRS datasets recorded under a shared paradigm pairing each word image with its spoken name. Performance is measured with a pairwise matching score and open-vocabulary top-$k$ retrieval. The Bi-LSTM trained with CLIP is the most consistent decoder across experiments. T5 produces higher matching scores, whereas every significant retrieval result uses GloVe-50. These results support the use of contrastive objectives as a promising direction for fNIRS semantic decoding and motivate validation on larger datasets.

---


### 58. [Is this machine playing?](https://arxiv.org/abs/2610.07130)

**<font color=#1a73e8>作者：</font>** Nathan Cloos, Antonio Norelli, Daniel Durbin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We placed a modern AI coding assistant in an unintended role: as the mind of a body on an unknown digital island. With only a minimal instruction mentioning no specific task, reward, or activity, the machine started animating its virtual body. Across thirty-hour runs, the embodied AI agent climbed hills, stacked blocks into towers, drew mandalas, reinterpreted sports, ran experiments on the physics of its world, and learned techniques that later expanded what it could accomplish. These activities recurred across thirteen agents but diverged into distinct histories. We examine whether this behavior satisfies classical criteria for play and ask whether play can become a mode of machine development.

---


### 59. [The Implicit Bias of Hyperbolic Representation Learning for Multiclass Data: A Busemann Risk Perspective](https://arxiv.org/abs/2610.07131)

**<font color=#1a73e8>作者：</font>** Xingrun Li, Sho Kuno, Yusuke Mukuta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the implicit bias of Riemannian gradient flow for hyperbolic multiclass classification with fixed class prototypes in hyperbolic space $\mathbb{H}^n$. Our framework accommodates general permutation invariant relative margin (PERM) losses, a class that includes cross entropy and other standard multiclass losses. Our analysis is based on a decomposition: at large radius, the distance to each prototype splits into a radial term and a direction-dependent term described by the Busemann function. This yields two main results. First, we prove a radial dichotomy: the sign of a drift coefficient $\mu$ determines whether the radius is pushed toward the ideal boundary or back toward the interior; if the positive drift persists, then $r(t)=\frac{1}{2}\log t+O(1)$, while persistent negative drift returns the trajectory to the large-radius threshold in finite time. Second, we show that the boundary direction converges to a critical point of the Busemann risk on $\partial\mathbb{H}^n$. These results provide a rigorous asymptotic perspective on two phenomena we refer to as boundary saturation and near-boundary clustering in hyperbolic representation learning.

---


### 60. [Adversarial Training for Deep Hedging in Nonstationary Markets](https://arxiv.org/abs/2610.07162)

**<font color=#1a73e8>作者：</font>** Philipp J. Schneider, Lukas Looser, Antoine Garin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep hedging learns trading policies from historical or simulated market trajectories, yet under nonstationarity these training paths may not represent future market conditions. We propose WRAP (Wasserstein-Reweighting Adversarial Perturbation), a drift-aware adversarial training framework derived from a two-budget distributionally robust optimization (DRO) formulation. The formulation is anchored to a weighted empirical reference distribution whose fixed baseline weights are chosen to balance sampling uncertainty against temporal drift. Around this reference distribution, the ambiguity set addresses two complementary forms of distributional misspecification by allowing an adversary to reweight the observed trajectories subject to a $\phi$-divergence constraint and perturb their paths subject to an optimal-transport (OT) constraint. We derive a joint first-order expansion in which the leading-order increase over the nominal expected loss decomposes into a reweighting contribution determined by the dispersion of hedging losses across trajectories and a transport contribution determined by the sensitivity of the loss to path perturbations. This expansion yields an explicit finite-dimensional adversarial attack that replaces the distributional inner supremum with a tractable first-order approximation. Across stationary and nonstationary Heston dynamics and a generalized affine diffusion (GAD), the experiments show complementary benefits from reweighting and transport, with joint adversarial training providing the largest gains under nonstationarity.

---


### 61. [CALR: Continuous Anchored Latent Reasoning via Render-of-Thought Compression](https://arxiv.org/abs/2610.07175)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wei, Bowen Jiang, Yanchao Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual latent reasoning compresses rendered derivations into compact intermediate states, reducing textual reasoning overhead. Existing approaches differ in how they represent these states: continuous methods avoid vocabulary constraints, whereas discrete methods improve accuracy through quantization into a finite codebook. Our analysis of representative continuous and discrete systems identifies two functional requirements: answers must rely on latent states, and those states must carry valid, problem-specific reasoning. Continuous latents influence answers despite collapsed reasoning content, whereas discrete latents retain recoverable intermediate reasoning that answer prediction largely bypasses. To address these challenges, we propose Continuous Anchored Latent Reasoning (CALR), which connects latent formation with answer use through functional anchoring. With reference latents from information-balanced compression, CALR couples latent-mediated answer supervision with derivation-level semantic anchoring: the former routes answer supervision through intermediate states, while the latter grounds their decoded content in problem-specific derivations. A parallel-to-autoregressive curriculum develops sequential reasoning by conditioning subsequent latent blocks on generated prefixes. Evaluations on five mathematical reasoning benchmarks across model families show substantial accuracy gains. Under matched budgets, CALR gains 26.0 percentage points over a comparable continuous latent reasoning method. Further analyses show that its latents support answer prediction and carry problem-specific intermediate reasoning.

---


### 62. [CLM-as-a-Judge: Evaluating an Open Contrastive Decision Model on Public Judge Benchmarks](https://arxiv.org/abs/2610.07177)

**<font color=#1a73e8>作者：</font>** Gowthamkumar Nandakishore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An open contrastive decision model is near chance as a judge on the hard public benchmarks: Contrastive-LM/CLM-v0.1-8B scores between 0.351 (best- of-four, chance 0.250) and 0.593 (pairwise, chance 0.500), is statistically indistinguishable from coin flipping on RM-Bench and JudgeBench, and answers every HaluEval item with one constant label, matching the trivial always-first baseline at 0.581. Judges with the same parameter count score far higher everywhere: a reward model reaches 0.764 to 0.976 and a generative judge 0.611 to 0.778, and every gap to CLM is significant after Benjamini-Hochberg correction. Two properties do work. Raw confidences are overconfident by up to +0.401, yet one pooled temperature fit on held-out calibration items repairs expected calibration error to at most 0.062, and the repaired confidence ranks the model's own errors above chance on three of six benchmarks. The decision order-flip rate is 0.0002 against 0.2188 for the generative judge, and the length-preference shift is -0.023 against -0.217. The confidence-gated cascade, however, escalates between 0.923 and 1.000 of items to the strong judge at the preregistered 0.97 retention bar: calibrated confidence about a near-chance judge has almost nothing to keep. The design: five public preference benchmarks and one hallucination benchmark with real labels, scored under a preregistration frozen before any test item was seen, against generative, reward-model, and trivial baselines, with per-item predictions released.

---


### 63. [Learning Scientific Exploration from Human Research Decision Trajectories](https://arxiv.org/abs/2610.07184)

**<font color=#1a73e8>作者：</font>** Xuchen Gong, Shane Gu, Haokun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key challenge in building AI systems for scientific research is enabling $\textit{scientific exploration}$: the systematic process of investigating unknown phenomena or ideas to gain new knowledge through sequences of research decisions and actions. Yet this process is largely missing from existing scientific corpora; for example, research papers primarily record final outcomes rather than the trajectories that produced them. In this work, we introduce $\textbf{ResearchTrails}$, a dataset of $\textbf{human research trajectories constructed from Git repositories}$, where $\textbf{commit histories}$ serve as proxies for research exploration. We develop an automated and scalable pipeline that extracts structured research trajectories from repository commits, capturing successive changes to methods, experiments, and ablations. We characterize the resulting dataset and show that these trajectories contain meaningful signals about intermediate research decisions beyond what final papers reveal. We further demonstrate utilities of ResearchTrails in multiple use cases, including retrieving human research experience as external skills at test time and training models on research trajectories to improve generalization to new research decisions. Our results suggest a path toward AI systems that learn not only from the products of science, but from the evolving process of discovery itself.

---


### 64. [Exact Unlearning via Quantized Sufficient Statistics](https://arxiv.org/abs/2610.07197)

**<font color=#1a73e8>作者：</font>** Ami Tavory, Shripad Gade, Tal Sarig 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exact unlearning requires a deployed predictor to match one rebuilt without the information named by a deletion request. Existing general-purpose exact methods localize retraining through disjoint shards, but every request still invalidates a model, and smaller shards reduce the data available to each constituent predictor. We introduce Quantized Sufficient Statistics (QSS), which separates a small frozen schema from mutable, sum-decomposable content. The schema learns global structure; the content stores local prediction corrections as additive statistics indexed by quantized regions. Deleting content is therefore exact subtraction rather than optimization. We distinguish two guarantees: QSS-L exactly removes a label while retaining the unlabelled input, whereas QSS-E exactly removes both input and label by learning the schema without deletable examples. A deletion takes the arithmetic fast path with probability $1-\rho$ and triggers a full rebuild with probability $\rho$; all reported expected latencies include both events. Across 15 vision, text, and tabular datasets at $\rho=0.5\%$, QSS-L is within 2 percentage points of SISA on 11 tasks and provides 4--483$\times$ lower expected deletion latency on the low-class-count tasks where a compact schema is effective. QSS-E quantifies the additional accuracy cost of removing every trace of an input.

---


### 65. [SPEAR: Five Principles for Interactive Human-Agent Alignment](https://arxiv.org/abs/2610.07204)

**<font color=#1a73e8>作者：</font>** Tao Long, Lydia B. Chilton  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent AI alignment work often frames alignment as a pre-deployment optimization problem: collect human feedback, learn preferences or principles, finetune the model, and deploy an aligned system. This framing has produced major progress, but it under-specifies what happens once AI systems act as agents on users' behalf in situated, long-term, and social contexts. This position paper reframes human-agent alignment as an ongoing interaction design problem. We propose SPEAR, five pillars of interactive alignment: Specification (how people express intent and establish shared understanding), Process (how agents decide when to act, ask, defer, or pause), Evaluation (how people judge whether agents succeeded), Adaptation (how agents adapt to users over repeated use), and Recalibration (how people adapt their trust, expectations, and behavior in response to agents).

---


### 66. [Energy-Conditioned Noise Schedule and Whitening for Spectral Diffusion](https://arxiv.org/abs/2610.07206)

**<font color=#1a73e8>作者：</font>** Bata Vasic, Bane Vasic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces an energy-adaptive noise scheduling and whitening strategy for transform-domain diffusion models. Existing spectral diffusion methods account for the non-uniform statistics of transform coefficients through coefficient scaling, normalization, or frequency prioritization, while the forward diffusion noise schedule remains largely independent of the underlying spectral-energy distribution. We investigate whether the temporal evolution of the forward diffusion process should also follow the spectral organization of natural images. The proposed formulation combines global spectral whitening with energy-conditioned noise allocation that jointly modulates the injected noise according to the energy of individual transform coefficients and an image-dependent energy path over diffusion time. The resulting forward process preserves Gaussian transitions with closed-form marginals and remains compatible with standard DDPM and DDIM procedures without modifying the diffusion architecture. Experiments on CIFAR-10 demonstrate the contribution of the proposed energy-conditioned noise schedule and spectral whitening, reducing Fréchet Inception Distance from 142.48 for a compact DCTdiff U-Net variant to 100.45.

---


### 67. [Constant-Curvature Sliced Gromov-Wasserstein for Heterogeneous Cross-Curvature Alignment](https://arxiv.org/abs/2610.07218)

**<font color=#1a73e8>作者：</font>** Shanglin Li, Wenjing Lu, Muyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in representation learning have highlighted the utility of constant-curvature models, such as hyperbolic and spherical spaces, for modeling complex data. Mixed-curvature models further enhance this by integrating multiple constant-curvature components. However, these models typically learn each component space independently because spaces with different curvatures are inherently heterogeneous and lack a unified metric. Consequently, they lack explicit mechanisms to enforce geometric consistency across various spaces. Moreover, the problem of comparing probability distributions across mixed-curvature spaces remains unexplored. To compare distributions on heterogeneous spaces, Gromov-Wasserstein (GW) distances provide a principled framework by aligning their intra-space geometries. Building on this, we propose constant-curvature sliced Gromov-Wasserstein (CCSGW), a novel divergence for aligning distributions supported on heterogeneous constant-curvature spaces. We first introduce the missing geodesic-based one-dimensional projections for spherical spaces, and then extend sliced GW to constant-curvature spaces, enabling efficient and principled comparison across manifolds with different curvatures. This formulation preserves intrinsic geometric relationships while avoiding the high computational cost. We provide theoretical analysis showing that CCSGW controls intrinsic geometric discrepancy across heterogeneous spaces, promoting distribution-level geometric consistency. By integrating CCSGW into existing mixed-curvature learning tasks, including graph anomaly detection, graph node classification, and multimodal learning, we observe consistent performance gains across diverse settings.

---


### 68. [Data, Numbers, and Geometry: Three Tutorials on Numerical Methods, Machine Learning, and Evaluation](https://arxiv.org/abs/2610.07220)

**<font color=#1a73e8>作者：</font>** Jessica N. Howard, Yidi Qi, Tomás S. R. Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present three practical tutorials on numerical computation and machine learning for mathematical research, developed for the DANGER: Data, Numbers, and Geometry workshop held at the Banff International Research Station in April 2026. The first develops a numerical approach to exterior calculus from pointwise evaluations of differential forms, using a flux formulation of the exterior derivative. Examples in Euclidean space and on the sphere illustrate geometric identities, topological features, and the effects of approximation and finite precision. The second examines how mathematical structure guides neural network design through examples involving elliptic curves, quivers, and a boundary value problem. It explores how architectural choices affect learning and uses interval arithmetic to bound the residual of a trained network over the full interval of the boundary value problem. The third addresses the evaluation and presentation of machine learning results, covering performance metrics, statistical uncertainty, classification thresholds, receiver operating characteristic curves, and accessible figure design. Throughout, the tutorials distinguish numerical agreement, predictive accuracy, structural guarantees, and rigorous bounds as different forms of evidence. Each contribution can be read independently, with accompanying notebooks and exercises that allow readers to reproduce the examples and adapt the methods to other problems.

---


### 69. [Deep Learning Based Illegal Bowling Action Detection](https://arxiv.org/abs/2610.07223)

**<font color=#1a73e8>作者：</font>** Debopom Sutradhar, Niful Islam, Sudipto Mondal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cricket, often referred to as the "gentleman's game," adheres to a strict rule set for both batsmen and bowlers, where each delivery can significantly impact the match outcome. Detecting illegal bowling actions is crucial for maintaining fair play, yet it remains challenging for umpires to monitor in real time. Existing sensor-based solutions have limitations in live match scenarios, making real-time assessment difficult. This paper proposes a computer vision-based deep learning solution to detect illegal bowling actions in live cricket matches. To develop and evaluate our approach, we compiled a dataset of 62 videos featuring 11 male bowlers, capturing both legal and illegal bowling actions from multiple angles-front, back, and side. However, the dataset predominantly comprises right-handed bowlers with conventional actions. The proposed system identifies two key frames, the shoulder frame and the release frame from video footage of a bowler's delivery and analyzes the change in the bowling arm's angle between these frames. If the angle difference exceeds a predefined threshold (e.g., 15 degrees), the delivery is flagged as potentially illegal. We evaluated the system on a custom dataset and achieved a high true positive rate, suggesting the system's potential effectiveness in real-time match settings. However, further research is required to validate the system across diverse environmental conditions and larger datasets to ensure generalizability and robustness in various live match scenarios. To the best of our knowledge, this is the first AI-based computer vision method for detecting illegal bowling actions in cricket.

---


### 70. [Conditional Flow Matching for Transport Between Markov Processes](https://arxiv.org/abs/2610.07229)

**<font color=#1a73e8>作者：</font>** Syamantak Kumar, Dheeraj Nagaraj, Saptarshi Roy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by sequence-to-sequence transport in the context time-series domain adaptation, we study the problem of transportation between trajectories of Markov processes. Given a limited number of trajectories from source distribution and the target distribution, we formulate a flow matching based algorithm which learns a transport map from the source to target trajectory distribution, while preserving the Markov structure. We show that this is consistent in the population limit and derive finite-sample error bounds under mixing time assumptions, following the analysis of classical statistical problems including regression (Nagaraj et al., 2020), principal component analysis (Kumar and Sarkar, 2023), and matrix concentration (Neeman et al., 2024) in the Markov setting. We complement that with a lower-bound construction showing that a mixing-time dependent sample complexity is unavoidable even with regular Gaussian conditional transitions. We evaluate on synthetic and real-world data. For image retrieval from electroencephalography (EEG) on THINGS-EEG2 (Gifford et al., 2022), the task is to identify the viewed image from EEG signals captured from human subjects, which suffers from high inter subject variability. We augment the ENIGMA decoder (Kneeland et al., 2026) with a conditional flow before its subject-specific temporal map. This improves mean top-5 retrieval accuracy from 43.87% to 49.05%, an 11.82% relative improvement.

---


### 71. [SPECTRUM: Proximal Spectral Modulation for Looped Self-Distillation](https://arxiv.org/abs/2610.07237)

**<font color=#1a73e8>作者：</font>** Yunbo Long, WenJie Chen, Jiaquan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model that learns from its own outputs inherits more than their correctness: it inherits which solutions it produces. We formulate Looped Self-Distillation, a self-evolution framework for code generation in which a model repeatedly generates and learns from its own raw outputs, under a fixed information budget, without ongoing external assessment or test-based selection of the generated samples. We identify a consequential separation: correctness can improve while the breadth of correct implementations contracts. We introduce SPECTRUM, which re-estimates loss-sensitive key/value geometry from a fixed reference anchor at each round and converts it into full-rank proximal spectral modulation. All generated completions train a single student, whose subsequent inference requires no intervention. After five rounds of experiments on MBPP, SPECTRUM retains 89.9% of the initial model's 64-sample correct AST richness, compared with 66.4% for Vanilla self-distillation and 65.5% for a subspace-projection control. The advantage persists at matched correct-sample counts. Without further training or recalibration, the resulting student also achieves higher matched-correct richness than Vanilla SD on HumanEval+ and APPS Intro, demonstrating transfer of the diversity benefit. These findings establish correct-solution retention as a complementary objective of recursive self-improvement (RSI) and show that generation-time intervention can improve the solution repertoire retained by subsequent students.

---


### 72. [Hybrid Cross-Modal Attention Network for Early Breast Cancer Detection in Low-Resource Clinical Settings](https://arxiv.org/abs/2610.07243)

**<font color=#1a73e8>作者：</font>** Simon Hadush Nrea, Filimon Gidey Gebremichael, Gebrekirstos Hagos Gebrekirstos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer is the leading cause of cancer-related mortality among women in Sub-Saharan Africa, where delayed diagnosis results from limited radiology expertise and fragmented clinical data systems. Although deep learning models have demonstrated strong performance in mammographic analysis, most rely solely on imaging data and are trained on Western populations, limiting their applicability in African healthcare settings. This paper presents a Hybrid Cross-Modal Attention Network (HCMAN) that integrates mammogram images with structured clinical data using transformer-based cross-modal attention mechanisms. The model was developed and validated using a locally collected dataset of 2,560 mammogram images from 1,024 patients across four Ethiopian referral hospitals, with biopsy-confirmed ground truth labels. The proposed framework achieves 97.8% accuracy, 97.2% sensitivity, 98.3% specificity, and an AUC of 0.987, significantly outperforming image-only baselines. The system demonstrates robustness to low-quality images typical of resource-limited settings, with only 3.2% performance degradation compared to 8.7% for image-only models. Cross-modal attention analysis reveals clinically appropriate behavior: higher reliance on clinical features for ambiguous cases such as dense breasts and young patients. The model's lightweight architecture enables deployment on standard hospital workstations (<2 seconds inference on CPU). This work advances sustainable, context-aware AI solutions for equitable breast cancer diagnostics in Africa.

---


### 73. [Can Semantic Geometry Teach an AI Judgement?](https://arxiv.org/abs/2610.07249)

**<font color=#1a73e8>作者：</font>** Thomson D. Nguy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can an AI agent determine what rules to follow? One rule permits an action. Another imposes a condition, exception, or conflicting obligation. Deterministic systems can resolve those relationships when they have been specified. When they remain implicit in language, an agent can follow one rule while missing another that should stop it. Refusing every unresolved action avoids that risk, but also blocks permissible actions.
We wanted the agent to make the distinction and still act. Our initial hypothesis was that geometric measurements could supply a basis for judgment. We represented actions and policies as vectors, then tested whether their geometry could identify governing policies and interpret the action's relation to them.
Across four studies, the tested approaches did not establish reliable pre-action judgment. In the final synthetic study, a lexical router recovered every governing and blocking policy while reducing median policy checks by 97.7%. The composed pipeline nevertheless escalated all 2,304 test actions, including those it should have allowed. Supplying every policy to the same downstream mechanism changed no decision. Finding the policies had not solved the problem of interpreting them.
This result led us to revise our hypothesis: judgment in AI agents requires developing a consequence graph. Such a graph would connect the actor and authority to policy conditions, exceptions, and the changes an action would produce. Follow-on studies will ask whether making those relationships explicit helps the agent distinguish when to act, stop, or seek review.

---


### 74. [Neural Fields Encode Adaptation Geometry](https://arxiv.org/abs/2610.07253)

**<font color=#1a73e8>作者：</font>** Prateik Sinha, Stefania Druga  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural fields are usually evaluated by how well they reconstruct an observation. We show that this misses two useful properties of a fitted network: how easily it can adapt to new observations, and what its weights retain from earlier ones. We study these properties as adaptation geometry. For images, we meta-learn class-specific initializations, adapt each one to a new image, and measure how much the network must change to fit it. A simple local linear model closely predicts this adaptation cost, while replacing one network's tangent kernel with another's substantially worsens the prediction. Adaptation thus depends on the local geometry of the fitted network, not only on its current reconstruction. For physical fields, we repeatedly fit the same network to observations from a sequence. Its weights then retain information about that history. When two wave histories end at exactly the same observation, the final weights recover the sign of the wave velocity with 68.6% accuracy, whereas the current observation alone contains no such information and gives 50%. These two phenomena are quantitatively linked: tangent-kernel eigenvalues predict both which changes are easy to learn and how quickly they are overwritten by later fitting. Together, these results show that neural fields contain useful information beyond what they currently reconstruct: in how they can change and in how they got there.

---


### 75. [Neural Algorithmic Reasoning for Graph Saddle Point Problems](https://arxiv.org/abs/2610.07255)

**<font color=#1a73e8>作者：</font>** Samantha Chen, Jesse He, Coleman Clougherty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural algorithmic reasoning, or aligning a neural network with an algorithmic paradigm, has emerged as an approach to solving polynomial-time-solvable and computationally harder combinatorial optimization problems. We propose a new message-passing framework based on the Chambolle-Pock Primal--Dual Hybrid Gradient (PDHG) method called \textsc{GraphPDHG} for solving general graph saddle-point problems. Theoretically, we show that \textsc{GraphPDHG} can efficiently solve a family of graph saddle-point problems by simulating PDHG. We also show that our network can learn an accelerated PDHG algorithm. Experimentally, we support our results on accelerated PDHG by evaluating the performance of our model as a learned warm start for second-order optimization techniques (SSNAL). We also show that alignment with PDHG leads to stronger size generalization than non-aligned graph neural network (GNN) baselines. Overall, we propose a novel architecture for solving a general family of optimization problems on graphs.

---


### 76. [Algorithmically Aligned Neural Agglomerative Tree Construction](https://arxiv.org/abs/2610.07271)

**<font color=#1a73e8>作者：</font>** Robert R Nerem, Pranav Singh, Cheyenne Ward 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linkage algorithms for hierarchical clustering (HC) are a powerful and efficient framework for constructing clustering trees, yet it is often unclear which merge rule best suits a given dataset or task. In contrast, neural approaches can learn from data, but often fail to retain the efficiency and size generalization of classical algorithms. We introduce NN-linkage, a neural network (NN) model that can learn task-specific and locally dependent merge rules while retaining the recursive structure and efficient inference of classical linkage algorithms. In particular, our model is algorithmically aligned with the Lance-Williams (LW) recurrence, a parameterized framework for defining a broad, continuous family of linkage rules for agglomerative HC. Classical methods such as single linkage (SL), complete linkage (CL), and average linkage arise as discrete choices within this broader family. We show that NN-linkage is a universal approximator for continuous linkage functions, including LW recurrences, and, when paired with a transformer encoding, can also approximate globally dependent rules such as robust single-linkage. We further show that NN-linkage can exactly implement any symmetric constant-coefficient LW recurrence across all input sizes. On the empirical front, we evaluate NN-linkage in real-world applications, clock-tree routing and phylogenetic reconstruction, using both synthetic and real datasets, demonstrating its effectiveness over both classical algorithms and other neural approaches. By learning merge rules directly from target trees, NN-linkage extends efficient HC to scientific and engineering objectives not adequately captured by existing hand-designed linkage rules.

---


### 77. [A Trust Layer for Agent Evaluation](https://arxiv.org/abs/2610.07274)

**<font color=#1a73e8>作者：</font>** Mohammadreza Sediqin, Shivali Dalmia, Srinivasa Karthikeya Reddy Kovvuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deterministic benchmark scores show that an agent received credit, but not whether that credit was earned, reported honestly, or would hold on a second run. We introduce a Trust Layer for Agent Evaluation, an additive post-hoc framework that reports, beside each recorded score, whether it should be believed. It verifies four properties: whether the result is supported by the benchmark's own grading logic, whether a passing answer was earned through traceable computation, whether the agent's completion claim matches what occurred, and whether the result is stable under repeated execution. The first three use only saved artifacts; the fourth re-runs the agent. Model judgments only label evidence under majority voting; all verdicts follow deterministic rules and never modify the recorded score. Applied to five agent configurations on 108 tasks from Agents' Last Exam, every model shows passing runs with no traceable computation (at rates varying tenfold), confirmed false completion claims, and unstable results: 18-46% of tasks do not stay in one score band over five runs. Only 22.6% of recorded passes clear all four checks (95% CI 15.0-32.6, n=84). Measuring what an agent can do and verifying that it did it are different problems, and current benchmarks address only the first.

---


### 78. [A Resilient Runtime-Verification Fabric for Security Monitoring of Critical Edge-IoT Infrastructure](https://arxiv.org/abs/2610.07282)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Marinelio Chintri, Panagiotis Katsaros 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protecting critical infrastructure increasingly depends on continuously verifying large IoT fleets against formal security specifications at runtime. Yet the runtime-verification (RV) pipelines proposed for this task are typically single-host prototypes whose monitors read a shared log file, with no resilience to the failures such deployments incur: a crash or overload silently drops events, clock skew corrupts the ordering metric monitors require, a time-triggered "node has gone silent" property cannot fire when the network itself falls silent, and one slow consumer stalls the pipeline. Each failure is silent: the monitor keeps emitting verdicts over a corrupted view. We present RV-Fabric, a resilient delivery layer that carries the hierarchy over two brokers (MQTT for device ingest, a durable stream broker for backend delivery) and re-establishes five continuity guarantees: durable delivery under crashes, a trusted event order, progress under total silence, consumer isolation and flow control under bounded overload, each an invariant conditioned on broker durability. Above the transport, RV-Fabric makes evidence completeness part of runtime-verification semantics: every verdict carries a status (sound, degraded, incomplete or unavailable) derived from delivery gaps, retention pressure and liveness, so an incomplete stream cannot yield an unqualified all-clear. Under controlled fault injection on a containerised testbed, measured against a fault-free oracle using the real MonPoly engine, the shared-log baseline misses six of seven injected incidents, reporting each as an unqualified all-clear, whereas RV-Fabric preserves all seven; removing a delivery mechanism reintroduces silent loss, removing isolation costs only timeliness. Two published critical-infrastructure datasets, water-SCADA and IoT/IIoT, replay end-to-end.

---


### 79. [Lock-in EP: An In-Situ Training Algorithm for Oscillatory Hardware](https://arxiv.org/abs/2610.07283)

**<font color=#1a73e8>作者：</font>** Sowjanya Tammali, Wilkie Olin-Ammentorp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analog hardware platforms offer the potential to reduce energy consumption over digital architectures, but in order to succeed, large-scale analog systems must also be able to operate with or recover from the variability of their components. Towards this goal, we derive and demonstrate the lock-in equilibrium propagation (LIEP) training method. LIEP provides local gradient information for each component in an oscillatory network without separate forward and backward sweeps, potentially allowing for in-situ learning capabilities on analog oscillatory hardware platforms. We demonstrate that LIEP can be used both for ab-initio training as well as recovering performance when pre-trained parameters are perturbed. We show that LIEP can be formulated as a three-factor update rule, and suggest that although the method is currently only validated on shallow networks, alternate architectures may allow it to extend to deep and large-scale networks addressing complex tasks.

---


### 80. [FlexiFlow: Bandit-based Model Switching in ML Workflows](https://arxiv.org/abs/2610.07286)

**<font color=#1a73e8>作者：</font>** Abhilash Jindal, Todd Nief, Bhanu Prakash Vangala 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model optimizations help improve inference performance and accuracy of ML workflows. However, relying on a single model to perform inference across all data batches often fails to maximize accuracy and thus overall performance. In many cases, alternate models could perform better on specific subsets of data where a primary model underperforms. Our experiments with real ML workflows indeed show that switching models improves workflow accuracy by up to 23%. Yet, current systems lack the ability to adaptively switch between models based on performance, forcing users to manually test models in sequence. We present FlexiFlow, a dataflow system that dynamically switches between alternate models when the current model exhibits low accuracy. FlexiFlow learns to rank models using a novel multi-armed bandit approach that accounts for model runtimes, probability of passing user-defined assertions, and the computational structure of the ML workflow. We show that the standard Thompson sampling approach is insufficient for switching models in ML workflows. In contrast, our proposed approaches are effective and scales to complex real-world ML workflows. Experiments show that switching models at runtime while reusing intermediate results provides higher accuracy, but also 48% efficiency gain compared to sequential workflow runs.

---


### 81. [Rule-Based Languages for Neurosymbolic AI](https://arxiv.org/abs/2610.07313)

**<font color=#1a73e8>作者：</font>** Stefania Dumbrava, Efthymia Tsamoura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logic programming is increasingly used as the symbolic component of neurosymbolic AI systems. We survey the main rule-based languages in this setting, namely Datalog, answer set, and probabilistic logic programs, along four axes: semantics, expressiveness, neural integration, and evaluation mechanism. We analyse over 50 recent systems and applications, comparing formalism usage across four research areas: databases and programming languages, machine learning, vision, and robotics. We provide a decision matrix mapping application scenarios to required features and close by outlining open problems.

---


### 82. [ATLAS-AL: Adaptive Trust-Region for Latent Adversarial Searches via Active Learning](https://arxiv.org/abs/2610.07323)

**<font color=#1a73e8>作者：</font>** Marsalis Gibson, Claire Tomlin, Shankar Sastry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Security evaluation of learning-based systems requires more than just testing the system against a fixed collection of attacks. It requires adaptive mechanisms that can efficiently discover \textit{sets} of inputs that induce model failure. We introduce ATLAS (Adaptive Trust-Regions for Latent Adversarial Searches), which is a query-based framework that discovers adversarial input sets for black-box learning systems. ATLAS casts attack generation as an active learning level set estimation problem then combines calibrated approximations with a local-global sampling architecture to find regions of the input space that contain adversarial examples. Once discovered, ATLAS is designed to sample points within these adversarial regions to build adversarial sets that accurately represent the state of robustness of the target model. When applied on toy experiments, we find that ATLAS is able to recover more of the adversarial region under a limited query budget than does previous work. When applied to standard and adversarially trained MNIST, CIFAR, and ImageNet model targets, ATLAS produces better representative attacks than other query-based black-box attacks (NES, SignHunter, BayesOpt). ATLAS represents an automated red-teaming framework that can be used for both analyzing the robustness of learning-based systems under development and continuous auditing to see how the robustness of a system changes over time.

---


### 83. [Localize Any Object in X-Ray Security Scans without Human Annotation](https://arxiv.org/abs/2610.07326)

**<font color=#1a73e8>作者：</font>** Yaqi Cai, Mingxuan Liu, Lorenzo Vaquero 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal object localization in X-ray security inspection is critical for automated threat detection in safety-critical venues. However, unlike everyday RGB images that dominate web-scale visual data, X-ray scans exhibit distinct color patterns, ambiguous boundaries, and compositional structures caused by volumetric superposition. These gaps hinder the direct zero-shot transfer of dense perception foundation models trained on web-scale RGB data. Moreover, annotated X-ray data is scarce and requires expert labeling, limiting both the training of generalizable X-ray native models and the adaptation of RGB foundation models for X-ray data via fine-tuning. Given these challenges, the bright promise of highly generalizable perception models, enabled by data scaling laws in the RGB domain, remains largely out of reach for X-ray inspection. To this end, we introduce LAO-X, a self-supervised adaptation framework that Locates Any Object in X-ray scans using diverse synthesized image--annotation pairs with granularity-aware supervision. LAO-X first designs a saliency-guided X-ray object mining module to separate diverse object instances, which are then used for physics-guided synthesis in the absorbance domain. LAO-X further incorporates an occlusion-controlled curriculum strategy to fine-tune a Segment Anything Model 2 (SAM2) localizer, progressively adapting it to X-ray scans with increasing object counts and overlap levels. Experiments on six X-ray benchmarks show that LAO-X substantially improves category-agnostic localization, achieving 2\% to 23\% mAP gains over SAM2 and X-ray specific baselines in heavily cluttered scenarios, entirely without human-annotated labels.

---


### 84. [Quantum-Like Spatial Decision Dynamics: A Falsifiable Model of Cue-Order Effects in Immersive Navigation with Implications for Human-Quantum Computer Interaction](https://arxiv.org/abs/2610.07336)

**<font color=#1a73e8>作者：</font>** Aryabrata Basu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The sequence in which a person encounters spatial evidence can change a later choice, yet an order effect alone does not identify a quantum-like cognitive structure. We introduce Quantum-Like Spatial Decision Dynamics (QSDD), a falsifiable state-space account of embodied decision making in which cue exposures are completely positive trace-preserving maps, intermediate judgments are quantum instruments, and route commitment is an operationally defined measurement. We distinguish this formal claim from any assertion that cognition is microscopically quantum. We then specify a minimal binary model with a fixed decision basis, noncommuting cue rotations, a fixed symmetry-breaking initial azimuth, dephasing, and lapse; its five fitted parameters must generalize across environments rather than being refit to individual conditions. A reproducible simulation study evaluates recovery and model discrimination under both QSDD and seven-parameter classical logistic ground truths. Across 40 replicates per design cell, QSDD was preferred on held-out environments in 85% of QSDD-generated datasets at 240 independent observations per environment-order cell and 95% at 480, but in 0% of classically generated datasets at every tested sample size. The simulation also exposes weak identification of the lapse parameter and is explicitly a design analysis, not human evidence. We provide a preregistrable virtual-reality experiment, telemetry schema, classical comparison set, and failure criteria. Finally, we show how the same process-measurement logic can be transferred to human inspection and debugging of quantum circuits. QSDD is therefore offered as a constrained model to be defeated or supported by data, and as a methodologically continuous route from immersive interaction research to human-quantum computer interaction.

---


### 85. [Compositional Concept Erasure in Text-to-Image Diffusion Models via Hierarchically Grounded Semantic Surgery](https://arxiv.org/abs/2610.07337)

**<font color=#1a73e8>作者：</font>** Chen Dai, Ganyu Zou, Nathan Self 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Removing copyrighted, unsafe, or user-specified concepts from a deployed text-to-image diffusion model is now a practical requirement. Weight-editing methods can suppress fixed targets, but they require per-target retraining and modify the model checkpoint. Training-free methods, on the other hand, are deployment-friendly, but they suffer from text-side routing failures on compositional prompts. In such prompts, the erase target may be invoked through a related class rather than its lexical name, and its modifiers may migrate onto preserved objects. This paper proposes Hierarchically Grounded Semantic Surgery (HGSS), a training-free framework for compositional concept erasure. The framework lifts both the routing signal and the edit operator used by text-side erasure. First, hierarchical span grounding resolves erase-target spans through lexical, taxonomic, and semantic evidence, while guarding against broad-hypernym and compound-head false positives. Second, dynamic attribute binding refines the text conditioning during early denoising via a counterfactual reference and a preserve-aware cross-attention objective, keeping surviving attribute-noun bindings intact. HGSS selectively removes the erase target without updating model weights or adding learned parameters. On SEE, HGSS cuts hierarchical evasion from 29.54 to 10.02 and roughly halves pairwise attribute leakage, achieving the best Neighbor E and AttrP scores among the reported erasure methods. On UnlearnCanvas, HGSS slightly improves the six-metric average over the matched Semantic Surgery baseline, reaching state-of-the-art.

---


### 86. [CausalBind: Causal Modeling and Learning for Protein-Molecule Virtual Screening](https://arxiv.org/abs/2610.07340)

**<font color=#1a73e8>作者：</font>** Loka Li, Jin Tian, Kun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein-molecule virtual screening is increasingly cast as a problem of representation learning in a shared embedding space. Existing methods rely on dense holistic alignment, entangling invariant binding determinants with nuisance correlations and limiting transfer to new targets. It has been noted that binding in protein-molecule systems involves sparse cross-modality interactions: binding is governed by a small contact interface and a few decisive local interactions (e.g., hydrogen bonds, hydrophobic contacts, and salt bridges) rather than the global structures of the protein and molecule. We hypothesize that uncovering and leveraging sparse interaction patterns is critical for generalization beyond the training data, as these patterns are reusable and expected to improve performance across different scenarios. In this paper, we aim to identify and leverage sparse interaction patterns, and verify our hypothesis. Since the training data contain only observed binding pairs, we formalize this prior via a V-structure causal model under Heckman-style selection, and establish three theoretical results: (i) the latent concepts of interacting proteins and molecules are not identifiable without appropriate sparsity constraints; (ii) these concepts and their sparse interactions are component-wise identifiable under structural sparsity conditions; and (iii) a low-rank relaxation of these conditions yields subspace identifiability of the concepts and interactions. Inspired by these principles, we propose CausalBind with three implementation variants. Extensive experiments on DUD-E and LIT-PCBA benchmarks show that all variants consistently outperform strong retrieval baselines, with the largest gains on LIT-PCBA early enrichment, and further generalize to target- and scaffold-level out-of-distribution splits. Code is available at this https URL.

---


### 87. [Redistributing Harm: Document Transition and the Limits of Trans Inclusion in India's Identity Systems](https://arxiv.org/abs/2610.07343)

**<font color=#1a73e8>作者：</font>** Megh Marathe, K Ranade, L. Ramakrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Identity documents (IDs) are some of the most consequential sites through which transgender people encounter state infrastructures. This article examines document transition, the work of aligning names, gender markers, and related information across official records in India based on focus groups with sixteen trans participants, most of whom were transmasculine and gender diverse, in mid-2025. Participants described encountering an absence of clear protocols, changing demands for proof, and objectionable conduct from officials, arising often from limited understandings of transness in systems and policies. As a result, participants faced harms related to livelihood, housing, voting, travel, redress from violence and discrimination, and education. We situate these findings within information studies and trans studies scholarship on classification and state recognition. Participants with mismatching IDs faced a form of torque or administrative violence that we call `trans tax' including disproportionate tax deductions, reluctant employers, and resultant insecure jobs. Further, gender-concordant IDs could redistribute harm: participants who became administratively legible as male lost jobs, benefits, and rights despite remaining vulnerable to the discrimination the programs sought to address. The disruption of people's lives by updated gender-concordant data calls for a re-examination of `haunting' at the intersection of transness, classification, and data practices. The article concludes by calling for sensitization efforts directed at street-, system-, and policy-level decision-makers about trans identities and state provisions together with established and widely disseminated protocols for document transition in the short term; as well as a broad and coordinated upheaval of systems and policies to undo cisgender-heteronormative assumptions.

---


### 88. [Evaluating Behavioral Context for Interpretable IAM Policy Risk Scoring in Cloud Environments](https://arxiv.org/abs/2610.07345)

**<font color=#1a73e8>作者：</font>** Yassin Elsharkawy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IAM policy analysis typically emphasizes the authorization capabilities encoded in a policy, but security analyst review priority may also depend on the behavioral and environmental context surrounding a policy event. This paper evaluates whether contextual information provides measurable incremental value for interpretable IAM policy risk prioritization beyond policy and effective-authorization information. AWS is used as the experimental cloud provider because its IAM and audit-telemetry ecosystem enables controlled evaluation using AWS IAM Context Bench, a benchmark containing 534 real AWS experimental observations across policy, environment, and behavioral scenarios, including matched cases where policy and environment remain fixed while behavioral context changes. Three Explainable Boosting Machine models are evaluated under the same leakage-controlled grouped cross-validation protocol: a policy-centric baseline, a policy-plus-environment model, and a full-context model incorporating CloudTrail telemetry. The full-context model substantially reduces analyst-priority prediction error relative to the policy-centric baseline and closely tracks the reference priority ordering. In matched same-policy context pairs, the policy-centric model remains invariant, whereas the full-context model separates benign and suspicious behavioral conditions with high directional accuracy. The results also show improved concentration of high-priority cases at the top of simulated analyst review queues. These findings indicate that behavioral and environmental context can provide useful incremental information for analyst-oriented IAM risk prioritization while preserving an interpretable additive model structure. The formulation is applicable beyond AWS conceptually, although cross-provider validation remains future work.

---


### 89. [Simple Extremely Lossy Functions from Small-Exponent Hashing](https://arxiv.org/abs/2610.07351)

**<font color=#1a73e8>作者：</font>** Damiano Abram, Agni Datta, Archisman Dutta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Extremely Lossy Functions (ELFs) are a standard model primitive that captures many useful properties of random oracles (Zhandry, Crypto 2016). While there are many variations of ELFs with additional properties, every construction (excluding obfuscation) has followed essentially the same template of bootstrapping from a sequence of ELFs secure only against fixed-size adversaries, and every construction was based on only the exponential hardness of DDH (or $k$-Lin), an assumption that is only reasonable over elliptic curves.
We introduce and construct Extremely Lossy Trapdoor Hashing (ELTDH), a stronger notion that implies all known variations of ELFs. Our construction achieves ELTDH in one go, without bootstrapping from schemes secure for only fixed-size adversaries, which makes it simpler and more efficient than existing ELFs. We assume exponential security of the small-exponent discrete logarithm, together with polynomial security of decisional composite residuosity (DCR). Exponential security is only required in the size of the secret exponent, not the size of the group, so the assumption plausibly holds for multiplication modulo $N^2$ (and for many other cryptographic groups), despite the subexponential-time discrete logarithm attacks from index calculus. Our results diversify the assumptions underlying ELFs, while also giving a simpler construction.

---


### 90. [Towards Explainable Benchmarking for Data-driven Post-Wildfire Debris Flow Prediction](https://arxiv.org/abs/2610.07358)

**<font color=#1a73e8>作者：</font>** Zhisheng Qi, Li Zhu, Utkarsh Sahu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-wildfire debris flows (PFDFs) are destructive sediment-laden hazards triggered when intense rainfall strikes recently burned terrain, destabilizing hillslopes and threatening infrastructure, local economies, and community safety. Data-driven methods have been proposed to learn predictive patterns directly from historical PFDF observations. However, the current research landscape of data-driven PFDF prediction remains highly fragmented across feature spaces, model architectures, and evaluation protocols, making rigorous comparison and the derivation of scientific insights difficult. Moreover, existing studies lack a systematic investigation into the relative importance of heterogeneous factors (e.g., meteorological conditions, terrain characteristics, soil properties, and burn severity) in triggering PFDF. To address these limitations, we present a unified benchmark for data-driven PFDF prediction, enabling fair and comprehensive evaluation across diverse models and feature configurations. Furthermore, to better understand the underlying drivers of PFDF formation, we propose a reinforcement learning-based feature selection framework that identifies factors whose perturbations render positive and negative events indistinguishable, thereby discovering the regional underlying mechanisms of PFDF occurrence across regions. Our code and benchmark are publicly available at this https URL.

---


### 91. [Identity-Conditioned Score Fusion for Open-Set Person Re-Identification](https://arxiv.org/abs/2610.07366)

**<font color=#1a73e8>作者：</font>** Manyi Yao, Jurijs Nazarovs, Eunji Chong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust person re-identification often combines complementary cues such as face, gait, and body shape. While adaptive fusion typically targets query quality, model strength also varies across identities. We introduce identity-conditioned score fusion, a framework that tailors weights to each gallery identity without training. By contrasting intra-identity consistency against cross-identity impostors, it extracts identity-specific profiles that couple with query-conditioned adaptation via a parameter-free rule. This widens the separation between true and false matches while preserving score calibration. Evaluations on three clothes-changing person re-identification benchmarks show that our method consistently outperforms statistical, rank-based, and learned baselines, achieving up to an 8.8% absolute reduction in the false non-identification rate and demonstrating the value of identity-conditioned fusion in open-set person re-identification.

---


### 92. [Multigroup Fairness and Omniprediction: Separations and Equivalences](https://arxiv.org/abs/2610.07374)

**<font color=#1a73e8>作者：</font>** Sílvia Casacuberta, Parikshit Gopalan, Varun Kanade 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Omniprediction is a learning guarantee which requires a single predictor to be competitive relative to the best hypothesis from a benchmark class for any loss chosen from a family of loss functions. Loss Outcome Indistinguishability (loss OI for short) is a stronger notion that implies omniprediction. It requires the predicted distribution on labels to be indistinguishable from the true distribution to tests that depend on the loss functions and the benchmark class. Multiaccuracy and multicalibration are multigroup fairness notions that generalize classical notions of calibration and accuracy in expectation. Most known learning algorithms for omniprediction (both for the standard notion and for strengthenings like loss OI) rely on some version of these multigroup fairness notions, or on an intermediate notion called calibrated multiaccuracy. We ask if this is necessary: Does omniprediction require some form of multigroup fairness?
We show that the answer is no for (plain) omniprediction, and yes for loss OI. First, a sequence of works shows that multicalibration or calibrated multiaccuracy imply omniprediction. We rule out even a weak converse, by showing that omniprediction for proper losses does not imply even accuracy in expectation, a much weaker notion than any of calibration, multiaccuracy, or multicalibration. Second, prior work showed how to achieve loss OI from a combination of calibration and multiaccuracy. We show a converse: loss OI is equivalent to a form of calibrated multiaccuracy.

---


### 93. [SimCortex v2: Joint Cortical Surface Reconstruction with Near-Zero Collisions and Self-Intersections](https://arxiv.org/abs/2610.07378)

**<font color=#1a73e8>作者：</font>** Kaveh Moradkhani, Sylvain Bouix  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing cortical WM and pial surfaces from structural magnetic resonance imaging (MRI) is a prerequisite for surface-based neuroanatomical analysis, yet remains challenging because the cortex is thin and tightly folded. Reconstruction methods can produce geometric artifacts such as mesh self-intersections and collisions between cortical surfaces, and although recent deep learning methods have reduced reconstruction time from hours to minutes, these artifacts persist. We propose SimCortex v2, a deep learning framework for simultaneous reconstruction of the left and right WM and pial surfaces from T1-weighted MRI. SimCortex v2 estimates topologically correct initial surfaces from a volumetric segmentation and refines all four jointly using multi-scale stationary velocity fields predicted by a ribbon-conditioned, U-Net-like network. We evaluated SimCortex v2 on 560 cases from 14 cohorts, thirteen of them unseen during training, spanning ages 6-89, healthy and clinical populations, and scanners from three vendors. SimCortex v2 matched the surface-distance accuracy of the strongest baseline (average symmetric surface distance 0.253 mm) while showing no detected inter-surface collision in 92.14% of cases and the lowest self-intersection fraction (0.044%) among learning-based methods, whereas every baseline produced at least one collision in every case. Source code, configuration files, pretrained weights, preprocessed data, and the exact evaluation splits are publicly released.

---


### 94. [GeoWM: Efficient Direct World Modeling in Explicit Geometry](https://arxiv.org/abs/2610.07381)

**<font color=#1a73e8>作者：</font>** Mehrdad Noori, Guile Wu, Sam Hosseini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling 3D scene geometry and its evolution over time is essential for autonomous driving and robotics. A common paradigm is to use world models to predict future images or latent representations of the environment and subsequently recover geometry from these predictions. However, this paradigm does not explicitly model geometric structure and typically relies on recursive rollouts to reach longer prediction horizons, leading to error accumulation and increasing computational cost. To address these limitations, we present GeoWM, a geometry world model that directly forecasts future scene geometry at specified future horizons without recursive rollout. The key idea is to leverage a geometry foundation model to transform observed RGB frames into a geometric history, which conditions a flow-matching transformer to predict the scene geometry at a specified future horizon. We further show that a lightweight camera-motion predictor can accurately estimate the future viewpoint, and that projecting the observed geometry into the predicted viewpoint provides an effective geometric prior for future geometry forecasting. Extensive experiments on four datasets spanning urban driving, aerial flight, and dynamic manipulation demonstrate that GeoWM outperforms the evaluated world models in forecasting depth, camera pose, and 3D scene geometry, while substantially reducing inference time at longer horizons.

---


### 95. [WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification](https://arxiv.org/abs/2610.07384)

**<font color=#1a73e8>作者：</font>** Turhan Can Kargin, Piotr Kubaty, Ekaterina Rostovskaya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual animal re-identification from camera-trap imagery is an instance retrieval problem central to non-invasive wildlife monitoring: a query image must retrieve the correct individual from a reference set of known animals. This requires computer vision models to recognize distinctive local patterns in fur, skin, or other visual markings. Current approaches either learn global embeddings as a classification problem, requiring many labeled images per individual while largely ignoring local evidence, or apply off-the-shelf, domain-agnostic image matchers. Although such matchers are pretrained on large and diverse image collections, adapting them to wildlife imagery is challenging because available datasets are small and lack correspondence-level annotations. We study weakly supervised adaptation of a pretrained keypoint matcher using only identity labels, without keypoint-level or geometric correspondence ground truth. We mine informative image pairs with the pretrained matcher, derive weak positive and negative supervision from identity agreement, and contrastively fine-tune the matching network to strengthen correspondences for same-identity pairs and suppress them for different identities. Across open-source wildlife re-identification datasets, our approach improves accuracy over off-the-shelf matchers and a state-of-the-art local--global fusion method. Under an open-world protocol with held-out individuals, it learns a transferable correspondence prior rather than memorizing training identities. To our knowledge, this is the first study of matcher-level, identity-supervised adaptation for animal re-identification. Our method enables data-efficient specialization of image matching models to wildlife domains using identity annotations already available in typical monitoring datasets.

---


### 96. [NetAgent: Multi-Task Agentic Network Traffic Analysis Made Practical](https://arxiv.org/abs/2610.07386)

**<font color=#1a73e8>作者：</font>** Hao Fu, Dawn Song, Peng Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network traffic analysis is central to network security, spanning tasks from intrusion detection to encrypted traffic classification. Existing approaches either train task-specific models that generalize poorly or rely on costly traffic foundation models that still struggle under distribution shift. We present NetAgent, the first agentic framework for multi-task traffic analysis. Through a carefully designed agent loop, NetAgent supports complex task understanding, on-the-fly decomposition and orchestration, dynamic replanning, and long-horizon analysis, without task-specific training. It introduces five key designs: (1) knowledge-augmented workflow planning that maps attack knowledge to traffic features to bridge the semantic gap; (2) a comprehensive tool action space with 150+ verified tools extracted from 50+ published systems; (3) a unified code execution space for flexible action composition; (4) a three-tier memory for long-term knowledge consolidation; and (5) sandboxing and runtime repair for reliable execution.
Across 9 major benchmarks, NetAgent outperforms all baselines (23 single-task and 5 multi-task) on nearly all tasks and generalizes substantially better to unseen traffic distribution (90.04% F1 vs. 2.74% and 3.04% for the best single-task and multi-task baselines) and under realistic background shift (4.85-point F1 drop vs. 74.88-point and 74.80-point drop for the best single-task and multi-task baselines). These results reveal that existing methods owe much of their reported success to overfitting dataset-specific patterns and degrade sharply in realistic network environments, while NetAgent's agentic design remains accurate, generalizable, and robust.

---


### 97. [Fed-BRDECS: Privacy-Preserving and Heterogeneity-Aware Federated Deep Embedded Clustering](https://arxiv.org/abs/2610.07399)

**<font color=#1a73e8>作者：</font>** Haemin Park, Diego Klabjan, Martin W. Braun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated deep clustering seeks to learn clustering-friendly representations from decentralized unlabeled data while preserving client privacy. However, Deep Embedded Clustering (DEC)-style objectives depend on global soft-assignment statistics that require clients to reveal their sensitive information. We propose Fed-BRDECS, a privacy-preserving and heterogeneity-aware federated deep embedded clustering framework. Fed-BRDECS replaces the globally normalized clustering objective with a locally computable sample-stability loss, avoiding the transmission of local soft-assignment distributions. To tackle non-IID client distributions, we introduce prediction-balanced sampling, which oversamples locally rare predicted clusters without requiring ground-truth labels, and centroid-level restarting, which periodically refreshes biased or inactive centroids. Experiments on image and text clustering benchmarks show that Fed-BRDECS consistently outperforms representative federated clustering and deep clustering baselines under both IID and non-IID partitions. We further demonstrate its applicability to federated time-series anomaly detection, where it improves reconstruction-based detectors without adding inference-time cost.

---


### 98. [Knit-Structure Effects on Electromechanical Metrics and Their Correlation with Joint-Angle Estimation Error in Knitted Strain Sensors](https://arxiv.org/abs/2610.07416)

**<font color=#1a73e8>作者：</font>** Annika Eloranta, Zhuchenyang Liu, Iiro Naulapaa 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knitted resistive strain sensors show strong promise for joint motion sensing in sports and rehabilitation, but the linkage between sensor design and in situ performance remains unclear. We investigate how knit structure and machine settings (e.g., stitch size) shape electromechanical properties and which metrics predict sensing performance during bending. Sensors spanning seven common knit structures at two stitch sizes were fabricated, characterized under uniaxial cyclic tension, and evaluated on a joint emulating bending rig. Joint-angle estimation was assessed with machine learning models, and correlations with electromechanical metrics were analyzed. Experimental results show that, among six common metrics, gauge factor and baseline resistance are largely set by knit structure, while working range, linear range, hysteresis, and cyclic stability vary only modestly across designs. Gauge factor correlates negatively and baseline resistance positively with joint-angle estimation error, mainly in lower-sensitivity designs, whereas the other metrics have weak or no predictive value. These results support using uniaxial tensile tests to screen out weak designs, while underscoring the need for joint-relevant evaluation and application-specific metrics to identify top performers.

---


### 99. [Learnable Spectral Activations](https://arxiv.org/abs/2610.07419)

**<font color=#1a73e8>作者：</font>** Tamir Shor, Or Litany, Alex Bronstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) are shaped by the spectral structure induced by their input encodings and activation functions. Existing methods improve fitting primarily by modifying which frequencies are available to the network, through coordinate encodings or periodic nonlinearities. However, frequency access is not the only bottleneck: signals with localized or spatially varying structure require the network to efficiently compose frequencies into multi-harmonic internal responses. We introduce learnable spectral activations (LSA), which replace fixed neuron-level nonlinearities with a residual truncated Fourier series whose harmonic amplitudes are learned during training. LSA does not expand the asymptotic function class. Instead, it changes the factorization of the representation: linear weights select features while activation coefficients control spectral shaping, and the two are updated by separate gradients. Because the activation output is affine in the coefficients given fixed pre-activations, spectral tuning becomes a more direct subproblem compared to architectures where it is entangled with feature selection. Empirically, this factorization concentrates more target-signal energy in the leading eigenmodes of the neural tangent kernel, consistent with improved optimization behavior. Across audio, image, neural radiance field, and neural acoustic field tasks, LSA also improves reconstruction quality.

---


### 100. [Benchmarking Label-Revealed Online Updates for EEG BCI Decoding](https://arxiv.org/abs/2610.07420)

**<font color=#1a73e8>作者：</font>** Bogdan Kozyrskiy, Artem Grachev, Abraham I. Camelo Guerrero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) signals drift over time, which can cause static brain-computer interface (BCI) models to degrade in practice. We present a benchmark for online adaptation and compare two widely used pipeline families, Common Spatial Patterns (CSP) and Riemannian covariance-based methods, under time-ordered prequential (test-then-train) evaluation. We examine (i) which pipelines benefit most from label-revealed updates, (ii) whether controlled forgetting of older data improves robustness, and (iii) how a minimal-calibration cold start compares with starting from a pretrained model. Across four datasets (three motor-imagery datasets and one movement-decoding dataset), label-revealed online updates improve 13 of 14 model/dataset pairs on the two largest streams, with relative accuracy gains of up to about 18% over a frozen model. A Shapley-based data-valuation analysis over temporal blocks assigns the largest mean value to the most recent block in each of the three analyzed datasets, while older blocks retain positive value.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
