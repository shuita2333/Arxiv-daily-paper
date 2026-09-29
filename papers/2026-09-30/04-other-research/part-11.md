# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 501. [ENet-GP: Unified Document Image Restoration](https://arxiv.org/abs/2609.33758)

**<font color=#1a73e8>作者：</font>** Sujal Burad, Aakanksha, A. N. Rajagopalan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable document digitization in uncontrolled capture settings is challenging because real images exhibit multiple interacting degradations rather than a single isolated distortion. Documents thus captured are affected simultaneously by geometric distortions, like page warping, as well as photometric degradations such as non-uniform illumination, and blurring. However, most existing approaches address these factors independently and are evaluated on benchmarks containing only one distortion type, limiting their real-world applicability. We introduce GutenDoc, a large-scale dataset of high-resolution dense-text documents with physically grounded compound degradations. Using physics-based rendering, our dataset jointly models geometric warping and diverse photometric effects, enabling systematic evaluation under realistic capture conditions. We further propose a unified restoration framework that jointly corrects geometric and photometric distortions within a single-network and single-training setup, without the need for degradation-specific retraining or sequential inference passes. Extensive experiments show that our method remains competitive on established single-distortion benchmarks while substantially improving robustness under compound degradations, providing a practical solution for real-world document digitization.

---


### 502. [Oracle-Efficient Online Classification with Stochastic Inputs and Adversarial Outputs](https://arxiv.org/abs/2609.33760)

**<font color=#1a73e8>作者：</font>** Gon Buzaglo, Elad Hazan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider contextual binary prediction with i.i.d. contexts from an unknown distribution and adaptively chosen losses. We show that a simple Follow-the-Perturbed-Leader algorithm with Gaussian perturbation for each observed context achieves the optimal $\widetilde O(\sqrt{T\log N})$ expected regret for a class of $N$ experts, while requiring one optimization-oracle call per round and no explicit enumeration of the class. For an infinite hypothesis class $\mathcal H$, the algorithm attains $\widetilde O(\sqrt{T\operatorname{VC}(\mathcal H)})$ regret. This resolves an open problem posed by Lazaric and Munos (2012), showing that hybrid classification is computationally as easy as statistical learning.

---


### 503. [StatD2GAN: When Calibration Masks Generator Quality in Held-Out Evaluation of Synthetic Weather Sequences](https://arxiv.org/abs/2609.33761)

**<font color=#1a73e8>作者：</font>** Mustafa Ozaytac, Ozge Karadag Atas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for multivariate weather series are routinely evaluated with pooled distributional metrics computed after marginal calibration. We show this practice can invalidate architectural conclusions, and rebuild the evaluation of StatD2GAN, a three-discriminator GAN with evolutionary weight adaptation, around a held-out protocol: the final two calendar years of each dataset are held out behind a 168 hour embargo, calibration is fitted on the training block only, and all metrics are computed on the held-out block. Evidence comes from 25 matched (location, seed) pairs across five Koppen-Geiger climates, tested with Wilcoxon signed-rank tests under Holm correction. Four results follow. First, isotonic calibration drives the Kolmogorov-Smirnov distance to within 2% of a per-location noise-and-shift floor for every architecture tested, including a deliberately weak RCGAN baseline, so calibrated marginal metrics cannot discriminate between architectures. Second, the sorted-representation discriminator is the only component whose removal significantly degrades cross-variable dependence (Kendall tau MAE +0.080, Holm p = 0.009), with a regime-dependent effect: near zero in Ankara, above 115% in Dubai and Yakutsk. A rank-transformed variant isolates the mechanism as quantile supervision of the marginals rather than copula matching. Third, physical constraint violations are injected by calibration, not the generator; projection removes them at negligible cost (deltaKS <= 0.003). Fourth, pooled metrics conceal a collapse of between-sequence weekly-mean variability, a proxy for seasonal and regime diversity, in TimeGAN that only sequence-level statistics expose. We recommend floor-referenced marginal evaluation, matched-pair testing, and sequence-level variance decomposition as minimum requirements for calibrated generative pipelines.

---


### 504. [Beyond Fixed Features: Architecture-Dependent Sensitivity to Node Representations under Heterophily](https://arxiv.org/abs/2609.33764)

**<font color=#1a73e8>作者：</font>** Priyanath Maji, Sidharth Gaur, Rajavinoth Paul Durai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) perform well on homophilic graphs but struggle in heterophilic settings, where connected nodes often carry dissimilar labels. Existing evaluations typically compare architectures under a fixed node-feature representation, leaving unclear whether conclusions about heterophily robustness remain stable as the input representation changes. We address this question by constructing parallel feature variants of two large-scale heterophilic benchmarks, Roman-Empire and Amazon-Ratings, pairing each graph with representations ranging from static fastText vectors to contextual Transformer embeddings and evaluating seven GNN architectures across these representations. We find that the effect of representation varies across architectures: on Roman-Empire, the contextual gain ranges from 2.38 percentage points for GCN-sep to 13.67 points for GAT, with H2GCN gaining 8.77 points. On Amazon-Ratings, where node text is limited to short product titles, GAT improves by 6.78 points from fastText to MPNet, while GCN-sep changes by only 0.20 points. These results show that architectural performance is conditional on node representation: the same representation change can produce different magnitudes of performance gain across architectures, so architecture and representation cannot be treated as independent evaluation factors. A rank-correlation analysis on these two benchmarks further shows that the relative ordering of architectures remains highly stable across representations, isolating differential sensitivity, rather than ranking instability, as the primary effect.

---


### 505. [M3-Score: Fidelity, Memorization and Coverage as Separate Axes for Evaluating Generative Radiology Image Models](https://arxiv.org/abs/2609.33769)

**<font color=#1a73e8>作者：</font>** Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative evaluation of generative models for radiology remains challenging. Clinically relevant structures are often small and infrequent, feature spaces learned from natural images may represent them poorly, and a single summary score cannot distinguish limited fidelity from limited diversity. This study proposes the Medical Multi-axis Maximum Mean Discrepancy score (M3-Score), an evaluation framework based on RadioDINO-s16, a frozen vision transformer pretrained on radiology images. M3-Score reports three complementary axes computed at pre-specified encoder depths: \emph{fidelity}, measured by an unbiased multi-bandwidth radial basis function (RBF) MMD$^2$ at the final block; \emph{memorization}, measured by nearest-neighbor distances at 75\% depth; and \emph{coverage}, defined as the fraction of real images with a generated neighbor within their $k$-nearest-neighbor radius at 33\% depth. Reference sets are sampled across subjects to limit the influence of correlated slices. On BraTS brain MRI, the fidelity axis ordered five comparison sets of increasing severity (Spearman $\rho = 1.00$), and a subject-disjoint real set yielded $\mathrm{MMD}^2 = 0$ (permutation $p = 1$). An unconditional denoising diffusion probabilistic model achieved $\mathrm{MMD}^2 = 0.073$ (95\% confidence interval $[0.071, 0.080]$) but covered only 38\% of the real distribution. Under progressive mode dropping, $k$-NN manifold recall increased at all twelve encoder blocks, whereas the proposed coverage estimator decreased monotonically ($\rho = -1.00$). RadioDINO-s16 features separated real brain MRI from generated samples with a ROC-AUC of 0.819, compared with 0.555 for InceptionV3 and 0.582 for CLIP. Across a twentyfold range of sample sizes, the mean M3 value varied by a factor of 1.05, compared with 2.52 for the Fréchet Inception Distance.

---


### 506. [Skill2Env: Capability-Oriented Environment Synthesis from Skills for General Agents](https://arxiv.org/abs/2609.33772)

**<font color=#1a73e8>作者：</font>** Weiyi Xu, Xiaowen Yang, Wen Da 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Executable environments are critical for post-training agents on tasks that require tool use and multi-step interaction, but constructing executable tasks together with their environments remains difficult to scale. Skills provide reusable domain knowledge, operational procedures, and tool-use instructions, but a substantial gap remains between the information contained in a skill and a concrete, challenging task with a complete executable environment. To address this gap, we introduce Skill2Env, a capability-oriented framework that starts from a skill and uses agent capability demands to guide task and environment synthesis. Skill2Env represents these demands through reusable difficulty patterns and instantiates them into task blueprints that specify objectives, challenges, environment facts, information boundaries, and acceptance criteria. These blueprints guide the joint construction of task instructions, execution substrates, workspaces, and rubric-based evaluators around source skills. We further propose Iterative Task Hardening, which uses solver execution evidence to identify insufficiently challenging task designs, strengthen or extend their difficulty-pattern instantiations, and revise the corresponding blueprints and environments. Using 1.5K high-scoring trajectories generated from Skill2Env environments for supervised fine-tuning, we observe consistent improvements across a broad range of agent benchmarks, demonstrating the effectiveness of capability-oriented environment synthesis for agent post-training.

---


### 507. [Is your uncertainty map wrong, or is its target? Exact diagnostics for the Tweedie diagonal, and a gradient-free alternative](https://arxiv.org/abs/2609.33786)

**<font color=#1a73e8>作者：</font>** Vicent Ribas, Anna Oliveras Tous  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A diffusion model can predict a follow-up medical scan from a baseline, but a clinician needs a per-voxel map of where that prediction can be trusted. Many such maps approximate the diagonal of the Tweedie posterior covariance, and are evaluated against another approximation of it, so whether the estimator or the target limits them is unclear. We compute the exact diagonal on six checkpoints across fourteen model-corpus conditions. Hutchinson at M=200 tracks it at rank agreement of at least 0.92 everywhere, yet in four of the fourteen the exact diagonal is anti-correlated with the denoising error, reaching -0.13, so a faithful estimator reproduces that reversal. All four are real-image conditions; on the models' own samples the reversal does not appear, so evaluating on generated samples flatters this family. What limits these maps is the target, not the estimator.
We then introduce Tweedie Probe-Tangent (T-PT), a gradient-free residual probe that corrupts one model-supported prediction repeatedly and measures the voxel-wise variance of the denoiser's response. T-PT reads a different functional of the same Jacobian, and its exact second-order form ranks with the diagonal wherever the diagonal reverses; at thirty probes it returns a map too unstable to reproduce that ranking, while Hutchinson at M=5 already reproduces it, so T-PT there is not evidence against the reversal. We offer it as an instrument, not a better approximation. On brain MRI at full resolution, where every Jacobian-based estimator we test runs out of memory, T-PT leads a twenty-chain Monte-Carlo ensemble on five of eight endpoints inside tissue and trails it on none, at 16x fewer network evaluations; over the whole volume the ensemble leads, and fifty chains close the tissue gap. On lung CT the ensemble is ahead throughout. Both lose most of their discrimination where the change is, which remains open.

---


### 508. [Binding Multiple Modalities via Multimodal Wasserstein Barycenter](https://arxiv.org/abs/2609.33800)

**<font color=#1a73e8>作者：</font>** Xiaole Tang, Jiayi Xu, Xiang Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning beyond two modalities commonly leverages a specific modality (e.g., text) to bind other modalities. However, how to establish a more balanced representation space that approximates shared semantics while respecting the holistic geometry of $n$-modal data remains challenging. In this work, we present BaryBind, which aims to transport the specific modality towards the Wasserstein barycenter (WB) optimized across all modalities and introduces a volumetric alignment objective to establish a unified semantic space around the WB embedding. Specifically, we project specific modalities to the WB, which minimizes the average Wasserstein distances to multimodal distributions and serves as the anchor for subsequent alignment. We then construct a barycenter simplex, whose volume is taken as a similarity metric for global alignment centered at the WB. Experiments show that BaryBind achieves competitive performance in text-video-audio retrieval, classification, videoQA, and cross-modal generation tasks, along with robustness under modality absence and scalability to more than three modalities. Code is released at this https URL.

---


### 509. [MinkowskiPE: Minkowski Positional Encoding for Spatiotemporal Perception](https://arxiv.org/abs/2609.33804)

**<font color=#1a73e8>作者：</font>** Yuhao Li, Louie Hong Yao, Tianyi Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling spatiotemporal coupling is a key challenge in building physical intelligence across scales, from microscopic to macroscopic. Existing models capture such structure broadly through physics-motivated dynamical formulations or learning-motivated architectures. The former provide stronger priors but may constrain flexibility, whereas the latter are more flexible but leave the spatiotemporal coupling largely implicit. We therefore seek an approach that combines flexible learning with an explicit geometric bias for jointly modeling time and space. To this end, we propose Minkowski Positional Encoding (MinkowskiPE), which uses joint temporal and spatial coordinates to parameterize Lorentz transformations applied to query and key features. With MinkowskiPE, the query-key attention score depends on position only through the relative spacetime displacement between the two tokens and is therefore invariant to global translation of the coordinates. This paradigm retains the standard dot-product attention interface and remains compatible with efficient attention implementations. We evaluate MinkowskiPE on microscopic molecular dynamics and macroscopic video prediction tasks, achieving the best results on all nine multi-trajectory molecular evaluations and reducing KTH video-prediction MSE by 9.9% relative to the best baseline while using roughly one-tenth as many parameters.

---


### 510. [Eyes on the Road: A Naturalistic Comparison of MTW Rider Gaze in Urban Indian Traffic](https://arxiv.org/abs/2609.33811)

**<font color=#1a73e8>作者：</font>** Prerak Srivastava, Bhaiya Vaibhaw Kumar, Kavita Vemuri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motorized two-wheelers (MTW) dominate Indian roads but remain underrepresented in driver behavior research. This study presents the first large-scale analysis of MTW driver gaze behavior in naturalistic, heterogeneous urban traffic, using the \textit{myEye2Wheeler} dataset. A semantic segmentation pipeline (YOLOv11 + SAM2) was used to extract object-level gaze metrics under two attention modes: direct gaze (foveal overlap) and central vision (parafoveal monitoring). Results reveal a functional division: central vision supports broad monitoring, while direct gaze enables brief, selective sampling. Novice riders exhibit road-anchored scanning, returning to the road between object fixations, while experienced riders form longer chains of attention across multiple objects. The findings suggest that experience primarily refines temporal rhythm rather than altering allocation strategy and reduces object-class effects in gaze patterns. These findings offer new insight into MTW attention structures and inform future work on behavior modeling and safety systems.

---


### 511. [dOPT: Differentiating Conic Optimization via Geometric Reduction](https://arxiv.org/abs/2609.33828)

**<font color=#1a73e8>作者：</font>** Fengyu Yang, Connor W. Magoon, Tyler Watts 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization layers enable the incorporation of structured constraints and decision problems into learning systems. Training such systems requires differentiating through the embedded optimization problem, which can be challenging for general conic programs. We introduce dOPT, a solver-agnostic framework that, rather than differentiating the full conic formulation, reduces it at a computed primal-dual solution to an equality-constrained quadratic program that preserves the reference solution and its first-order sensitivity. The reduction captures the local first- and second-order conic geometry relevant to differentiation and remains well defined at singular configurations. Computing solution derivatives then requires a single symmetric linear solve, independently of the forward solver. We derive explicit reductions for convex NLPs, QPs, SOCPs, and SDPs. Numerical experiments validate the computed gradients and show favorable backward-pass scalability, with substantial speedups over existing differentiable conic optimization methods as problem size increases.

---


### 512. [The Cost of Stability: Deanonymizing Onion Services Long-Lived Introduction Circuits](https://arxiv.org/abs/2609.33831)

**<font color=#1a73e8>作者：</font>** Nicolas Constantinides, Mahdi Rahimi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tor is a widely used anonymity network that provides network privacy by routing client communications through a sequence of relays to their destinations. An adversary observing a single Tor relay cannot readily link clients to their destinations, as doing so requires identifying the other relays along the client circuit. Identifying these relays from traffic observed at the monitored relay alone is challenging: each relay carries traffic for many circuits simultaneously, and client circuits typically last only about 10 min, limiting observations of a given circuit. In contrast, Tor onion services use introduction circuits that remain fixed for 18 to 24 h. We develop an intersection attack that exploits this design, allowing an adaptive adversary observing one Tor relay at a time to identify the network location of an onion service. We evaluate the attack on the live Tor network against a self-operated onion service carrying genuine third-party traffic. Across nine end-to-end experiments, the attack reconstructs the complete Tor circuit in every run, with an estimated median time of 2.2 h. To mitigate this attack, we propose a mechanism that periodically rebuilds internal introduction circuits to limit evidence accumulation without changing publicly advertised information.

---


### 513. [CLIMB-flow: Coupled Linear Inverse posterior sampling via Multiscale-Based flow](https://arxiv.org/abs/2609.33834)

**<font color=#1a73e8>作者：</font>** Zeqiu Yu, Ruizhi Yuan, Mathews Jacob  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are now widely used in Bayesian inverse problems in imaging as priors, where latent diffusion models are often used for larger scale problems to keep the computational complexity and model-size manageable. Unfortunately, the auto-encoder based compression results in loss of spatial detail. In addition, the optimization is converted to a non-linear problem. In this paper, we introduce a posterior sampling algorithm customized for the pyramidal/cascaded architecture, which relies on a coarse to fine hierarchical strategy to generate images in the pixel domain. We present CLIMB-Flow which alternates between three steps: an end-point estimation from the current coarse and noisy image, data-consistent update of the clean image, and re-noising it back to the level the network expects. Together these steps sample the posterior at that scale using an approximate Gibbs sampling from two conditional distributions. Experiments on ImageNet, CelebA, AFHQ and fastMRI span inpainting, deblurring, super-resolution and accelerated MRI, with PSNR gains of 1.37-7.66 dB over the strongest competing method on CelebA and pixel-domain reconstruction up to 512x512.

---


### 514. [Laya as a Typed Probabilistic Assessor: An Independent Reproduction and a Preregistered Study of Calibration and Selective Escalation](https://arxiv.org/abs/2609.33843)

**<font color=#1a73e8>作者：</font>** Gowthamkumar Nandakishore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The shipped Laya Typed-Decisions checkpoint, a 421M-parameter ModernBERT-large assessor that answers typed choice/noul/score questions over workflow state, is uniformly under-confident. The signed confidence-accuracy gap is $-0.214$, every occupied reliability bin's accuracy exceeds its confidence, and that sign uniformity collapses every binned ECE variant to the same value, $0.214$. The card frames the risk as over-confidence; the measured direction is the opposite, and the direction decides which way a confidence-gated cascade fails. A single disjointly fitted temperature ($T=0.469$, sharpening) removes most of the miscalibration (held-out ECE $0.204$ to $0.037$) and outperforms the shipped per-option-count table. The frozen selection rule instead chose isotonic regression, which overfit and failed its held-out NLL contrast on both tracks, so hypothesis H2 is not supported. Re-running the released checkpoint on its full official test split reproduces the card's headline accuracy ($0.767$ vs. $0.766$). The retrospective E1 reproduction preceded the analysis freeze; E2-E8 were prospectively preregistered, and 20 of 22 executed confirmatory tests reject under Benjamini-Hochberg FDR at $q=0.05$ (two descoped). The frozen gate beats random escalation but misses its 10% accepted-set error target on both tracks, an exploratory out-of-distribution probe finds no zero-shot transfer (accuracy $0.617$), and every score measures agreement with a synthetic teacher whose self-agreement ceiling ($0.735$) the specialist exceeds. Per-decision predictions, run manifests, and the frozen preregistration are in the ancillary files. The author has no affiliation with the model's publisher, the dataset's publisher, or TypeSafe.

---


### 515. [Rethinking Contextualization by Reinterpreting Attention Head Channels](https://arxiv.org/abs/2609.33851)

**<font color=#1a73e8>作者：</font>** Hakaze Cho, Haolin Yang, Zhun Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextualization, the core operation of language modeling, transmits information across words to build sentence-specific word representations. Prior works mainly study contextualization, focusing on individual words and attention heads as a growing discrete dictionary, lacking a global view of their general behavior. Therefore, we propose a general principle: Globally, we find and estimate that different words carry different amounts of information, and less-informative words tend to absorb more contextual information. Specifically, these low-information words do not absorb contextual words uniformly, and finer-grained selectivity enables more precise routing to promote information transmission between matched words. Moreover, to find what mechanism causes such processing, we reinterpret attention heads as channels gated by their singular vectors and find that: (1) these singular vectors point to the hidden states of more informative words, allowing such words to write their information to others more strongly to act as information sources, and vice versa; and (2) these singular vectors can be viewed equally as hidden state features, enabling automated interpretation of attention heads beyond prior heuristic head discovery, also embedding heads into a continuous space rather than treating them as discrete, independent dictionary entries.

---


### 516. [ReDrive: Shaping Representations with World Modeling for End-to-End Driving](https://arxiv.org/abs/2609.33854)

**<font color=#1a73e8>作者：</font>** Yueting Zhu, Shaoyu Chen, Yuehao Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving policies require capabilities of scene understanding and future evolution prediction. To achieve this goal, current end-to-end models typically construct complex perception-planning pipelines or introduce world models that explicitly predict future states, resulting in a complex system architecture. Inspired by the transferability of general-purpose visual representations, we argue that combining sufficiently strong visual representations with representation world modeling can support effective planning without relying on complex inference-time auxiliary modules. Based on this insight, we present ReDrive, an end-to-end driving framework that strengthens planning-oriented visual features via future representation prediction. To achieve this, ReDrive adopts a three-stage training pipeline consisting of driving video pretraining, joint world-modeling and planning training, and planner adaptation. This yields a strong planning-oriented representation and a high-performance planner, while requiring neither auxiliary perception modules nor future prediction at inference time. Experiments on NAVSIM demonstrate strong performance, achieving 91.0 PDMS on NAVSIM v1 and 90.8 EPDMS on NAVSIM v2. These results show that shaping representations with world modeling is sufficient to enable high-performance end-to-end planning while retaining a simple encoder-planner inference pipeline.

---


### 517. [PI-NOMT: Physics-Informed Neural Optimal Mass Transport for Brain Fluid Dynamics](https://arxiv.org/abs/2609.33857)

**<font color=#1a73e8>作者：</font>** Mehmet Emin Acar, Vahit Bugra Yesilkaynak, Helene Benveniste 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering hidden transport mechanisms from sparse spatiotemporal observations is a fundamental inverse problem in scientific machine learning. In brain tracer imaging, dynamic contrast-enhanced MRI (DCE-MRI) provides time-resolved measurements of tracer concentration, while the underlying velocity and source mechanisms governing tracer propagation remain unobserved. We formulate this problem as physics-informed latent-state inference, in which the transport field itself is the primary object of inference rather than an auxiliary variable used only to reconstruct observed densities. We propose Physics-Informed Neural Optimal Mass Transport (PI-NOMT), a framework that represents density, velocity, and source as continuous neural fields and combines a continuous neural density teacher, recursive differentiable advection--diffusion--source rollout, unbalanced optimal-transport regularization, and governing-equation supervision. Physical laws act as structural priors that constrain the space of admissible transport mechanisms, while observed tracer dynamics provide evidence for estimating the latent transport state. We evaluate PI-NOMT on a synthetic benchmark with known ground-truth transport and on DCE-MRI sequences from nine control rats. On the synthetic benchmark, PI-NOMT accurately recovers the prescribed velocity field, including its magnitude, direction, and integrated trajectories, rather than merely reconstructing endpoint densities. Across the nine rat datasets, the framework yields sub-percent local endpoint error, consistent physical speed scales, and low post-training PDE and incompressibility residuals. These results support physics-informed latent-state inference as a general framework for recovering hidden transport mechanisms from observed dynamic scalar fields.

---


### 518. [Vanilla Policy Optimization Is Both Optimal and Differentially Private for Stochastic Contextual Bandits](https://arxiv.org/abs/2609.33888)

**<font color=#1a73e8>作者：</font>** Idan Attias, Orin Levy, Alexander Ryabchenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can vanilla policy optimization explore enough to achieve near-optimal regret in stochastic contextual bandits? We show that standard exponential policy updates driven by offline regression do so under realizability, without exploration bonuses or importance weighting. For $A$ actions, $T$ rounds, and a finite prediction class $F$, vanilla PO achieves $\widetilde O(\sqrt{AT\log(|F|)})$ regret with high probability. Our analysis reveals an implicit exploration mechanism of independent interest: gradual policy updates prevent actions from losing probability too quickly, allowing the regression oracle to learn their expected losses. We further develop a batched version using only $O(\log T)$ regression calls and policy switches, and show how private regression oracles yield differentially private contextual bandit algorithms without composition across batches. For a finite class, this gives pure $\varepsilon_{\rm priv}$-DP and regret $\widetilde O\left( \sqrt{AT \log(|F|/\delta)}(1+\varepsilon_{\rm priv}^{-1/2}) \right)$. Finally, experiments across oracle-based contextual bandit algorithms, with and without privacy, demonstrate the practical effectiveness of policy optimization and the value of explicit exploration under stronger privacy constraints.

---


### 519. [Augmented Feature Boosting for Multicalibration](https://arxiv.org/abs/2609.33891)

**<font color=#1a73e8>作者：</font>** Ira Globus-Harris, Inbal Livni Navon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multicalibration requires a predictor's residuals to be unbiased not only globally, but also after conditioning on the predictor's own level sets and reweighting by a rich class of test functions. Standard boosting approaches in the distributional setting achieve this by repeatedly discretizing the predictor's range then auditing and repairing the resulting level sets. One consequence is that in practice, the algorithm's guarantees are sensitive to this parametrization of the rounding parameter. A natural theoretical question, then, is how to do discretization-free boosting which avoids this rounding within the boosting process itself. Here, we analyze an alternative feature-augmentation boosting paradigm inspired by Tax et al. (2026): at each round, a squared-loss oracle is called on hypotheses that receive the previous predictor's output as an additional feature, and only the final predictor is rounded to have a finite set of level sets to provide the multicalibration guarantee with respect to. We give a theoretical analysis of this procedure through the expressivity of the augmented hypothesis class, and show how the expressivity of this class yields a hierarchy of guarantees, including multiaccuracy, multicalibration, and the stronger notion of level-set multicalibration.

---


### 520. [Residual-Stream Burden Shapes Representation Learning in Diffusion Transformers](https://arxiv.org/abs/2609.33895)

**<font color=#1a73e8>作者：</font>** Tongtong Liang, Siqi Kou, Ziqiao Xi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In diffusion-based generation, a neural network can be trained to predict the clean data, the noise, or the velocity from a noisy input. These prediction targets are interconvertible and describe the same generative process, yet plain Diffusion Transformers operating on large pixel patches succeed with clean prediction and fail with noise or velocity prediction. We argue that this asymmetry arises because noisy targets require the residual stream to preserve noise-dependent input variation through depth for the final readout, forcing subsequent layers to compute on noisy representations. A spectrally concentrated clean target imposes a lighter demand, leaving greater freedom to organize hidden representations for subsequent computation. We call this preservation requirement *residual-stream burden* and show how it shapes representation learning in Diffusion Transformers. Controlled experiments indicate that the exploitable structure is spectral concentration in patch space and that the bandwidth of the persistent residual state is a key resource for noisy prediction. We further show that this account is consistent with recent decoupled pixel-space architectures, whose diverse designs all reduce the residual-stream burden on the main pathway. To examine this understanding from a complementary direction, we expand and reorganize the residual-stream bandwidth directly, introducing Spatially Indexed Hyper-Connections (SiHC) that reach FID 1.71 on ImageNet $256^2$. Together, these results identify residual-stream burden as a mechanism through which prediction targets and architecture jointly shape representation learning in Diffusion Transformers.

---


### 521. [NSV-Shift: A Contrastive Benchmark for Non-Speech Vocalization Understanding and Response Adaptation in Speech-to-Speech Models](https://arxiv.org/abs/2609.33899)

**<font color=#1a73e8>作者：</font>** Ziwei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce NSV-Shift, a contrastive benchmark for evaluating whether speech-to-speech models can understand non-speech vocalizations (NSVs) and adapt their responses accordingly. Each pair contains two conversations with identical lexical content that differ only in the NSV embedded in the final turn. Our pilot contains 22 human-verified pairs (44 audio conditions) and evaluates five models on NSV perception, emotion understanding, and response adaptation. Results show that models generally perform better at detecting NSVs than at interpreting their fine-grained emotional meaning or producing appropriately differentiated responses. The data construction pipeline, dataset, and evaluation pipeline are publicly available at this https URL.

---


### 522. [Finite Probes Suffice: Identifiability and Universality for Weight-Space Learning](https://arxiv.org/abs/2609.33901)

**<font color=#1a73e8>作者：</font>** Soutrik Sarangi, Yonatan Sverdlov, Adir Dayan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning properties of neural networks has recently attracted growing interest, with existing approaches operating either directly on network parameters or through probe-based representations of network behavior. While probing methods have shown strong empirical performance, their theoretical foundations remain limited. In this work, we study when finite probe-based representations are sufficient for learning neural functionals. We establish general identification and universality results for probing, and show that using intermediate hidden representations can provide significantly more informative representations than relying only on final outputs. Motivated by these results, we introduce HIDDENPROBE, a simple architecture for learning from hidden probe responses. Across a range of neural functional benchmarks, including both MLPs and Transformers, HIDDENPROBE consistently improves over existing probing methods and achieves state-of-the-art performance. Our code is publicly available on GitHub.

---


### 523. [On the Two Faces of Adam in Separable Linear Classification](https://arxiv.org/abs/2609.33904)

**<font color=#1a73e8>作者：</font>** Chen Fan, Csaba Szepesvári  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the behavior of deterministic, full-batch, bias-corrected Adam in separable linear classification with softmax parametrization under log-loss. In this setting, under a wide range of conditions Adam is known to approach max-norm-margin optimality when its stability constant $\epsilon$ is zero, while with a positive $\epsilon$, it is known to approach Euclidean-margin optimality. Our main contribution is the quantitative description of Adam's behavior for small fixed positive $\epsilon$. We give sufficient conditions under which an Adam-trained classifier nearly maximizes the max-norm margin before the updates become gradient-like. We also show that the classifier reaches a fixed target Euclidean margin only much later. Specifically, we show that for polynomially decreasing stepsizes with exponent \(a\), where \(1/3<a<1\), the updates become approximately proportional to the negative gradient after $\Theta(\log(1/\epsilon)^{1/(1-a)})$ iterations. At that time, the classifier still nearly maximizes the max-norm margin. Reaching a fixed target Euclidean margin above that of every max-norm-optimal classifier, but below the optimum,
is shown to require $\epsilon^{-\Theta(1)/(1-a)}$ iterations. Under inverse-linear stepsize decay (\(a=1\)), the update
transition takes polynomially many iterations, whereas reaching the target margin takes
exponentially many. Experiments support these predictions. The later change in the classifier
can improve or worsen generalization after training error reaches zero, connecting the
analysis to grokking and its reverse.

---


### 524. [JIVE: Jacobian-Informed Volume Expansion for Diverse Generative Sampling](https://arxiv.org/abs/2609.33906)

**<font color=#1a73e8>作者：</font>** Guangxun Zhang, Brian Cai, Boxuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models often suffer from mode collapse and limited sample diversity. While prior works attempt to mitigate this by jointly generating a batch of samples and repelling their trajectories, these heuristics do not explicitly maximize the diversity of the resulting endpoints. We introduce JIVE, a training-free framework that enhances generative diversity by injecting velocity perturbations aligned with the leading right singular subspace of the generator's endpoint Jacobian. By leveraging this local geometric structure, JIVE provably maximizes endpoint diversity while preserving sample quality. To maintain practical efficiency, we compute these perturbation directions via matrix-free iterations rooted in classical numerical linear algebra, requiring only a small computational overhead. Across different benchmarks, JIVE boosts both pixel and feature-level diversity in few-step and one-step generation.

---


### 525. [Near-Duplicate Families Break Exact-Record Membership Inference](https://arxiv.org/abs/2609.33909)

**<font color=#1a73e8>作者：</font>** Yiyong Liu, Jiayang Liu, Yixin Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Membership inference (MI) asks whether a specific record appeared in a model's training set and is increasingly used as evidence for data provenance and copyright auditing. These applications require determining whether the exact queried record was used for training, rather than merely whether the model was exposed to similar content. Making this distinction is challenging because web-scale datasets naturally contain near-duplicates, including syndicated articles, mirrored pages, and lightly modified images. We show that this creates a fundamental confound for standard MI. A clean-reference audit typically calibrates membership against a null in which neither the queried record nor its near-duplicate family is present. In deployment, however, the queried record may be absent while a non-identical family member was used for training. We introduce a four-world audit that independently varies exact-record inclusion and family presence to separate these cases. Natural near-duplicate families cause severe false attribution. On CC-News, a clean-reference LiRA auditor labels 99.70% of family-present exact non-members as members at 1.00% false-positive rate. This failure persists across alternative scores, model architectures, and executed deduplication and retraining. Controlled interventions further reveal that the effect depends on the learning objective. In classification, faithful families largely substitute for the exact record, reducing exact-given-family inference to near chance. In autoregressive language modeling, the exact sequence retains a detectable residual, while family presence still confounds clean-reference decisions. These results show that positive model-only membership evidence may establish family-level exposure without establishing exact-record provenance.

---


### 526. [ReVision: Supporting Designers' Interpretation and Exploration of Visuals in Concepts and Forms](https://arxiv.org/abs/2609.33911)

**<font color=#1a73e8>作者：</font>** Yaqing Yang, Mei-Xi Chia, Aniket Kittur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual designers get inspiration from references to expand their design space. They decompose what makes a reference evocative into conceptual and visual elements, ranging from explicit attributes such as objects and colors, to less readily articulated concepts and visual motifs. They then create different visual forms to explore how the selected elements could be combined differently. Novices often struggle with these moves, instead focusing on surface features or producing limited visual variation, thus becoming fixated on the reference. Existing tools support editable visual attributes and high-level themes, but provide limited control over how conceptual interpretations relate to expressive visual motifs or how their combinations can be systematically re-expressed. We present ReVision, an AI-based tool that decomposes visual and textual references into editable conceptual interpretations and visual motifs, enables their recombination across conceptual and visual spaces, and renders each direction as divergent visual-form variations, supporting more divergent exploration during the creation process.

---


### 527. [Preserving DEG Rankings for Gene Discovery in Histology-Based Spatial Gene Expression Prediction](https://arxiv.org/abs/2609.33928)

**<font color=#1a73e8>作者：</font>** Kaito Shiku, Kazuya Nishimura, Yasuhiro Kojima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from histology images could scale spatial transcriptomics (ST) to image-only cohorts, but conventional histology-based ST prediction is trained and evaluated mainly by per-gene spatial-profile reconstruction. This objective is misaligned with a key downstream use of ST: differentially expressed gene (DEG) discovery, where genes are ranked for a biological or morphology-defined contrast by evidence of between-group expression differences. We formulate image-based differential expression ranking (IDER), which asks whether predicted expression profiles preserve the contrast-specific ranked gene list obtained from measured profiles. IDER compares gene rankings induced by differential-expression statistics, rather than raw expression magnitudes or per-gene spatial correlations. We further introduce a differentiable IDER objective that aligns these statistics across genes and can be trained with morphology-derived proxy contrasts without predefined biological group labels. Experiments on public ST datasets show improved DEG-ranking agreement and pathway-enrichment overlap over conventional reconstruction objectives, including morphology-derived and pathologist-annotated tissue-region evaluations.

---


### 528. [Diffusion-Based Rollouts as a Stabilization Mechanism for Long-Horizon Environmental Forecasting](https://arxiv.org/abs/2609.33930)

**<font color=#1a73e8>作者：</font>** Marina Vicens-Miquel, Amy McGovern, Aaron J. Hill 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extending forecast lead times while maintaining predictive skill remains a major challenge in environmental forecasting. We investigate diffusion-based rollouts as a stabilization mechanism for recursive forecasting using low-dimensional water-level time series and high-dimensional precipitation fields. Across both modalities, diffusion suppresses recursive error growth, with the largest stabilization occurring where deterministic rollouts are most unstable. However, stabilization does not guarantee forecast fidelity. In the water-level experiments, forecasts progressively lose event-level fidelity as the rollout loses access to external predictive information, and trajectory-level comparisons show that diffusion can remain numerically stable while contracting toward central values and exhibiting reduced variability. In the precipitation experiments, which retain conditioning from numerical weather prediction throughout the rollout, diffusion better preserves spatial organization and event-detection skill. Together, these contrasting experiments indicate that diffusion can control recursive error amplification, while its practical benefit also depends on the predictive information available to constrain future evolution.

---


### 529. [Behavioral Monitoring of JEPA World Models with Jacobian Centroids](https://arxiv.org/abs/2609.33940)

**<font color=#1a73e8>作者：</font>** Thomas Walker, Randall Balestriero, Richard Baraniuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting failures in World Model (WM)-based planning requires monitoring whether the model is behaviorally aligned with the current task, which in turn requires studying its internal representations. Here, we show that centroids---sub-component Jacobian row-sums---effectively identify the behavioral properties of WMs, complementing traditional activation-based knowledge signals. The centroids of a model are easily computed through Jacobian vector products and characterize how the model organizes the geometry of its input space, yielding an efficient perspective on internal representations, including the generation of task-relevant saliency maps. Evaluated on continuous control tasks using JEPA WMs, this behavioral view reveals a structural dissociation, where the encoder correctly represents the goal while the predictor remains behaviorally unresponsive. This failure mode directly predicts planning failure before any action is taken, allowing for goal resampling to recapture out-of-distribution success. Moreover, centroid-based methods outperform baseline methods as distribution-shift detectors. Together, these tools yield a behavioral monitoring stack that is operational and consequential under distribution shifts.

---


### 530. [TrackFlood: Relocating Latency Attacks from NMS-Free Detectors to Real-Time Trackers](https://arxiv.org/abs/2609.33948)

**<font color=#1a73e8>作者：</font>** Zonghua Gu, Julian Singh-Smith, Junlin Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We consider latency attacks on object detectors, where the attacker's goal is not to corrupt a prediction but to make the system fail to respond in time, targeting real-time applications such as autonomous driving. Modern object detectors eliminate Non-Maximum Suppression (NMS) through one-to-one assignment or set prediction, removing the classical detector-side latency bottleneck exploited by prior latency (``sponge'') attacks. We show that NMS-free does not mean latency-robust: this architectural change does not eliminate the attack surface but relocates it downstream to multi-object tracking, whose data-association cost remains content dependent. We present \emph{TrackFlood}, a unified white-box overload attack against NMS-free detect-then-track pipelines spanning both one-to-one detectors (YOLOv10 and YOLO26) and query-based detectors (RT-DETR). TrackFlood recovers differentiable confidence tensors and optimizes perturbations that flood the tracker with spatially distributed phantom detections while leaving detector inference unchanged. Evaluated entirely on an NVIDIA Jetson AGX Orin (TensorRT FP16), detector latency remains essentially constant, whereas tracker latency increases substantially. At a standard imperceptible budget ($L_\infty{=}8/255$), a universal perturbation produces clearly measurable tracker overload but only modest end-to-end slowdown, without deadline misses for the association-dominated trackers; a separate higher-budget stress test drives severe end-to-end slowdowns and sustained deadline misses. We further evaluate a lightweight, architecture-agnostic bounded-admission layer that caps the tracker workload and largely restores end-to-end latency, at a non-trivial cost in admitted clean detections. Our results demonstrate that evaluating NMS-free perception systems requires considering downstream tracking and end-to-end timing, not detector inference alone.

---


### 531. [EEG-Fusion: Failure-Informed Source-Free Expert Routing for Robust Motor Imagery EEG Decoding](https://arxiv.org/abs/2609.33962)

**<font color=#1a73e8>作者：</font>** Abdul Basit, Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Subject-independent motor-imagery (MI) EEG decoding can exhibit subject-level failures even when average performance appears acceptable: under subject shift, a decoder can become an overconfident near-one-class predictor. This is especially problematic in source-free deployment, where target-user labels are unavailable during adaptation and expert selection. We present \textit{EEG-Fusion}, a failure-informed decision-level fusion framework that treats source-free MI decoding as label-free reliability estimation over heterogeneous experts. EEG-Fusion applies subject-wise Euclidean alignment and normalization-only test-time adaptation, then routes each target subject to a neural, covariance-based, or physiological-feature expert using a reliability gate trained on source-held-out folds to predict expert performance and collapse risk from label-free stream diagnostics. The gate uses confidence, entropy, prediction diversity, expert agreement, and predicted class balance; collapse is measured as the maximum predicted class fraction. In 9-fold leave-one-subject-out (LOSO) evaluation with three seeds, relative to a no-alignment raw EEGNet source-free anchor, EEG-Fusion improves subject macro-F1 from 0.417 to 0.529 on BCI IV-2a local protocol, from 0.314 to 0.482 on BNCI2014-001, and from 0.607 to 0.708 on BNCI2014-004; corresponding collapse-index reductions are 0.199, 0.227, and 0.169. In a 9-subject Cho2017 external subset, EEG-Fusion improves macro-F1 from 0.516 to 0.630. These results suggest that label-free reliability estimation can reduce subject-level failure modes in source-free MI-EEG deployment.

---


### 532. [ThinkNet: Compact Architecture Selection and Validation-Gated Ensembles for Subject-Independent MI-EEG Decoding](https://arxiv.org/abs/2609.33967)

**<font color=#1a73e8>作者：</font>** Abdul Basit, Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Practical assistive and rehabilitative brain--computer interfaces require subject-independent motor-imagery EEG (MI-EEG) decoders that generalize to new users under limited target-user data and constrained compute. However, held-out-subject performance can be overstated when test-subject information influences preprocessing, model selection, or ensemble selection. We present \textit{ThinkNet}, a validation-controlled framework that combines train-only normalization, validation-guided evolutionary search, and validation-gated inference to identify compact decoders and inference policies for held-out subjects. We evaluate four-class BCI Competition IV-2a (session T) decoding with nine Leave-One-Subject-Out (LOSO) folds, three seeds, seven fixed decoder entries, and a broader search over ten representative decoder families; the held-out subject is never used for normalization, hyperparameter, architecture, or ensemble-policy selection. In the fixed benchmark, the validation-selected compact decoder achieved 44.35$\pm$15.41\% accuracy with 4.9K parameters, 19 KB FP32 weights, and 0.99 ms batch-1 Orin CUDA inference. Across the broader search, compact models ($\leq$25K parameters) achieved higher mean held-out accuracy than mid-size and large alternatives after selected retraining (40.10\% vs. 35.09\% and 34.78\%). Validation-gated ensembling improved over validation-selected single-model inference, reaching 43.98$\pm$16.25\% in the fixed benchmark and 43.31$\pm$15.88\% for the compact six-family ensemble. A non-deployable oracle analysis revealed a 6.1-point family-selection gap and near-zero validation--test correlation, showing that validation reliability remains a key bottleneck under subject shift. Thus, ThinkNet is a validation-controlled framework for compact MI-EEG model and inference-policy selection, rather than a single-architecture benchmark.

---


### 533. [Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors](https://arxiv.org/abs/2609.33969)

**<font color=#1a73e8>作者：</font>** Ge Gao, Siyue Teng, Chanqgi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Immersive video communication requires photorealistic, render-efficient, and compact dynamic scene representations. 3D Gaussian Splatting (3DGS) offers a promising representation, but dynamic 3DGS remains difficult to compress due to dense primitives and spatiotemporal redundancy. Anchor-based formulations improve compactness with sparse scaffolds that share geometry and appearance across primitives. However, existing designs often rely on deforming a single canonical scaffold and condition each primitive on its associated anchor in isolation, limiting their ability to handle non-local dynamics and disocclusion while under-exploiting inter-anchor correlations, particularly in motion- or texture-dense regions. To address these limitations, we propose SAGA, a volumetric video codec built upon Sparse Anchor-assisted GAussian splatting representations. SAGA represents dynamic 3D scenes using hierarchically organized sparse 4D anchors, where coordinate-based INR decoders generate fine anchors and Gaussian primitives from inter-anchor interpolations, enabling compact parameter sharing across spatiotemporal structures. For long-range dependencies among unstructured anchors, we further introduce fixed-size memory slots with orthogonality-informed updates for accurate entropy-context modeling. Experiments show that SAGA achieves strong rate-distortion performance against GIFStream, with PSNR BD-rate reductions of 80.39% and 83.94% on Neu3D and MPEG MIV, respectively.

---


### 534. [Do System One Decisions Add Up? A Study of Probabilistic Coherence](https://arxiv.org/abs/2609.33971)

**<font color=#1a73e8>作者：</font>** Saman Sarker Joy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A decision model can give probabilities that sum to one for every question yet disagree with itself when the same decision is broken into smaller steps. We study this form of probabilistic coherence in Jev and the English Laya checkpoint, using 2,500 matched examples per system across TREC, CLINC150, and MASSIVE. Across 72,000 classification questions, we compare direct fine-label predictions with broad-category probabilities and predictions reconstructed through those categories. Both systems show substantial disagreement: mean category-level total variation ranges from 0.219 to 0.349 for Jev and from 0.424 to 0.689 for Laya, on a scale where zero means exact agreement. The consequences differ sharply. On CLINC150, reconstruction reduces Jev's accuracy by 22.9 percentage points (paired 95% bootstrap interval: [-24.9, -20.9]) and improves Laya's by 21.3 points ([18.0, 24.5]). The same directions hold across all three datasets, with all six unadjusted accuracy-change intervals excluding zero. Improved accuracy can also accompany less reliable confidence: on MASSIVE, Laya gains 9.2 accuracy points while its expected calibration error rises from 0.046 to 0.124. Error analysis identifies both broad-category mistakes and within-category confusions. These findings show why decision systems need joint evaluation of accuracy, confidence calibration, and probability coherence in the workflow used by an application.

---


### 535. [DynGraphAgentBench: A Benchmark for Agentic Lifecycle Control in Dynamic Graph Anomaly Detection](https://arxiv.org/abs/2609.33980)

**<font color=#1a73e8>作者：</font>** Yuwei Han, Lingwei Wei, Wooseong Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graph anomaly detection requires repeated decisions as graph structure and class prevalence drift, yet detector benchmarks usually score a fixed pipeline after current labels are known. We introduce DynGraphAgentBench, an executable benchmark for agentic lifecycle control under delayed feedback. It comprises seven temporal graph datasets with node- and edge-level anomaly tasks, eleven selectable detectors, and eight chronological deployment windows per dataset. In each window, a controller sees only time-causal aggregate context, registered model cards, and its own matured history. It must choose a detector before current-window training or candidate scores exist. A sandboxed executor trains the chosen architecture on mature data, scores a hidden deployment window, and releases the outcome after a one-window delay. A deterministic verifier checks decision timing, leakage guards, legal actions, training scope, and persisted artifacts. We measure detection utility with average precision and capture at fixed review depth, and characterize adaptation through model switches and compute. Complete eight-window trajectories from two primary controllers and a no-memory reference on four datasets, together with three additional controllers on three datasets, expose useful, costly, and ineffective reactions to delayed evidence without granting an exhaustive current-window oracle.

---


### 536. [Future Information-Directed Sampling for Bayesian Nonstationary Bandits](https://arxiv.org/abs/2609.33981)

**<font color=#1a73e8>作者：</font>** Yichen Song, Alessio Russo, Aldo Pacchiano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration--exploitation is a central trade-off in bandit learning. While classical algorithms such as upper confidence bound methods and Thompson Sampling effectively balance this trade-off in stationary environments, their exploration strategies mainly reduce uncertainty about the current optimal arm, which can be insufficient in nonstationary settings where future optimal arms may differ substantially from current ones. In this paper, we propose Future Information-Directed Sampling (FIDS), a new algorithm for Bayesian nonstationary bandits that explicitly explores to gather information about future optimal arms. We show that FIDS achieves regret comparable to Thompson Sampling up to a small constant factor, while being able to exploit predictive information structures that conventional exploration objectives fail to capture. To address the practical difficulty of posterior inference, we further propose a supervised-learning-based approximation framework that learns the FIDS policy from offline data, and demonstrate its effectiveness on synthetic benchmarks.

---


### 537. [High-Level Text Preprocessing for Semantic Similarity Analysis of Discursive Texts: A Framework and Empirical Demonstration](https://arxiv.org/abs/2609.33983)

**<font color=#1a73e8>作者：</font>** Mehmet Murat Albayrakoglu, Mehmet Nafiz Aydin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic Textual Similarity (STS) methods assume that a document's lexical content faithfully represents what it asserts. This assumption fails for discursive documents that discuss, compare, critique, and contextualize other positions in the process of articulating their own. The result is semantic diffusion: similarity scores between documents are inflated by vocabulary acquired through discursive engagement rather than substantive alignment. Standard Natural Language Processing (NLP) preprocessing (tokenization, stopword removal, stemming, lemmatization) cannot address this problem because it operates at the lexical level, treating all content identically regardless of its discursive function. This paper introduces high-level text preprocessing: a systematic, rule-based intervention applied before the standard preprocessing pipeline to isolate each document's actual claim from its discursive structure. We propose 12 rules, each with an explicit rationale, and demonstrate their effect on an encyclopedic philosophical corpus: three entries from the Stanford Encyclopedia of Philosophy (virtue ethics, deontological ethics, and consequentialism). A three-phase experiment using eight Transformer-based STS models shows that preprocessing reduces centroid cosine similarity scores across all three theory pairs, with 23 of 24 model-pair comparisons showing the expected decrease and cross-model agreement ranging from 7-1 to 8-0. We introduce the semantic diffusion index (SDI), a per-document metric for assessing the semantic reorientation between a document's raw and high-level preprocessed representations. Although the framework is demonstrated using philosophical texts, it potentially addresses a domain-agnostic problem applicable to legal texts, policy documents, academic articles, and any genre in which a discursive approach introduces vocabulary from positions the document does not endorse.

---


### 538. [From HL to H+L-1 Parameters: A Hankel-Toeplitz Forecaster for Long-Term Time Series Forecasting](https://arxiv.org/abs/2609.33984)

**<font color=#1a73e8>作者：</font>** Chaoqi Zhang, Yu Wang, Haixu Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear forecasters have shown competitive accuracy against Transformer-based models in long-term time series forecasting. We study how classical stationary prediction theory can guide parameter sharing for more compact linear forecasters. For centered second-order stationary processes with nonsingular history covariance, the minimum-MSE finite-window linear predictor factors into a Hankel cross-covariance matrix and an inverse Toeplitz covariance matrix. Shared lags and scale cancellation specify this predictor using $H+L-1$ autocorrelations for lookback $L$ and horizon $H$. Building on the innovations representation, our Hankel-Toeplitz Forecaster (HTF) learns one impulse response that defines both an inverse filter and a forecast map. We characterize the finite-history correction and, under summability assumptions, bound the excess risk of truncating the true filters. HTF uses $H+L-1$ trainable coefficients while allowing a full-rank forecasting matrix. Across seven benchmarks at $L=336$, its horizon-averaged MSE is within 1.2% of Dense Linear on each dataset with 75-229 times fewer trainable parameters.

---


### 539. [ICMAPE: In-Context Multiagent Pure Exploration](https://arxiv.org/abs/2609.33986)

**<font color=#1a73e8>作者：</font>** Xinyi Hu, Alessio Russo, Aldo Pacchiano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In some multi-agent systems, the quantity to be optimized is not an externally specified reward but the information acquired about unknown properties of the environment as done in active sequential hypothesis testing (ASHT) problems. However, the ASHT literature tends to focus on finite single-agent problems with well-specified models, while there is currently a gap for practical multi-agent methods that can perform active sequential testing. We fill this gap with ICMAPE, a Bayesian learning-based framework for decentralized multi-agent pure-exploration driven by inference objectives. ICMAPE converts the fixed-confidence identification objective into a reward derived from inference confidence, so that standard reinforcement learning machinery can be applied to decentralized pure exploration. It jointly learns a centralized neural inference network that estimates a posterior distribution over hypotheses from global trajectory data, and decentralized policies that select actions from local observation histories and learn when to stop collecting data once the target confidence is reached. On two synthetic benchmarks and a Maryland nitrate concentration monitoring task based on real-world data, ICMAPE-TD3 achieves target accuracy with fewer exploration steps.

---


### 540. [A Multi-Dataset Benchmark of YOLO-Based Weed Detection in Precision Agriculture](https://arxiv.org/abs/2609.33991)

**<font color=#1a73e8>作者：</font>** Hristina Zdraveska, Vlatko Spasev, Ivica Dimitrovski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weed detection is an important component of precision agriculture, enabling site-specific weed management and reducing unnecessary herbicide use. Although deep learning methods have achieved strong results for crop and weed detection, many studies rely on single-dataset evaluation, making it difficult to assess robustness across different agricultural domains. This paper presents a multi-dataset benchmark of deep object detectors for weed detection in precision agriculture, with a focused evaluation of YOLO26 models. We evaluate nano, small, and medium variants on seven public weed-detection datasets covering different crops, weed species, field conditions, acquisition setups, and annotation protocols. The models are compared in terms of detection accuracy, model complexity, inference latency, FPS, and model size. In addition to in-dataset evaluation, we investigate cross-domain generalization using a unified one-class weed setup and evaluate multi-source training using the combined training subsets from all datasets. The results show that YOLO26 achieves strong in-dataset performance, with YOLO26m obtaining the highest average accuracy and YOLO26s providing the best practical accuracy-efficiency trade-off. However, cross-domain performance decreases substantially, with YOLO26s dropping from an average in-domain mAP$_{50:95}$ of 0.603 to 0.148 in the off-domain setting. Multi-source training improves performance on several datasets, but does not fully eliminate domain shift. Overall, the benchmark highlights the importance of dataset diversity, domain similarity, and target-domain adaptation for robust weed detection in real-world precision agriculture applications.

---


### 541. [GateDrain: Availability Attacks and Admission-Side Defense for Confidence-Gated Edge-Cloud Inference](https://arxiv.org/abs/2609.33992)

**<font color=#1a73e8>作者：</font>** Zonghua Gu, Julian Singh-Smith, Junlin Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidence-gated edge--cloud inference accepts confident local predictions and offloads uncertain inputs to a stronger cloud model. We show that this routing decision creates an availability attack surface. We call this attack \emph{GateDrain}: bounded input perturbations lower calibrated confidence and redirect requests that would otherwise be answered locally into a shared cloud queue, without increasing the application request rate. Because escalated requests share a cloud service, an increase in per-request cloud demand can move a near-capacity deployment across a queueing knee, causing disproportionate tail-latency degradation for benign users. We evaluate white-box, transfer, decision-only, universal, and multi-gate attacks on the public EdgeBoost artifact. A fixed-application-volume comparison isolates the effect of confidence manipulation from added client traffic, while perturbation-budget and arrival-process sweeps show that the queueing transition persists across several workload models but its amplification depends on the operating point. Adaptive attacks also defeat the evaluated training-free preprocessing defenses. To contain the resulting cloud demand, we evaluate Bounded Escalation, which combines per-source admission budgets, protected capacity, and non-preemptive trusted-class priority; an optional global bucket adds an identity-independent bound on untrusted admissions. The evaluation makes the resulting policy trade-off explicit: authenticated clients receive latency isolation, whereas tighter aggregate containment can reject legitimate unauthenticated offloads and reduce overall expected accuracy through edge fallback.

---


### 542. [ASTRA: ADMM-Accelerated Topology Reconfiguration for Dynamic Satellite Constellations](https://arxiv.org/abs/2609.33993)

**<font color=#1a73e8>作者：</font>** João Norberto, Ricardo Ferreira, Cláudia Soares  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic topology reconfiguration is central to the reliability and efficiency of large satellite constellations, yet many existing approaches rely on idealized assumptions such as full constellation deployment or uniform orbital spacing. We present Adaptive Satellite Topology via Regret-Aware learning (ASTRA), a theoretically-grounded framework for dynamic satellite topology reconfiguration that builds on an online learning formulation and makes it computationally practical. ASTRA combines an ADMM-based offline solver with efficient online updates for both online gradient descent and online conditional gradient, yielding markedly cheaper constrained updates than generic optimization pipelines. On the theory side, we show that for a relevant class of entry-wise nonzero utility matrices, the objective is strongly convex, which yields logarithmic static regret for online gradient descent, and we further instantiate known dynamic-regret guarantees under inexact ADMM inner loops. Empirically, ASTRA matches or improves topology quality, presenting a good trade-off with computational time on synthetic constellations, and it remains effective on real Starlink data under partial deployment and non-uniform spacing, where idealized structural assumptions break down. These results position ASTRA as an efficient and theoretically grounded approach to topology reconfiguration in realistic Low Earth Orbit networks.

---


### 543. [UnfoldCRF: Structured Mask Refinement with Image-Conditioned Latent Regions](https://arxiv.org/abs/2609.33996)

**<font color=#1a73e8>作者：</font>** Chunming He, Rihan Zhang, Lei Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned mask refiners improve segmentation accuracy, but it is hard to tell how much of the improvement comes from explicit structure rather than from extra capacity, and whether it holds up when the mask generator or its error distribution changes. UnfoldCRF treats refinement as inference in a conditional random field over pixel labels and latent region variables. Its energy has a corrected unary term, learned local pairwise interactions, and image-conditioned latent-region consistency, with a null state that lets a region with weak label agreement withdraw from the consistency term; inference unrolls damped mean-field updates on this one energy. To isolate the effect of structure, we compare against recurrent black-box refiners that read the same inputs and receive the same parameter budget, stage count, and supervision. On COD10K, UnfoldCRF beats the strongest matched control by 1.0 $F^\omega_\beta$ point, improves all four COD metrics, and lowers the fraction of images made worse from 11.7\% to 8.5\%. Under a train-once protocol over five datasets and several mask sources, the 2.6M-parameter variant gains 4.2 mean $\Delta$IoU against 2.0 for its control, and a variant built on frozen DINOv2 features matches the strongest foundation-model refiner with about a seventh of its resident parameters while staying ahead of its own control. On mask generators never seen in training, the gain is 2.0 $F^\omega_\beta$ points against 0.6 for the control. Zeroing individual messages shows where the corrections come from: the pairwise messages mostly fix boundaries, the region messages mostly fix non-boundary errors. Code and supporting materials will be publicly released.

---


### 544. [T-SNN: Temporal Simplicial Neural Network for EEG Decoding](https://arxiv.org/abs/2609.34002)

**<font color=#1a73e8>作者：</font>** Nikita Malik, Shubhajit Roy, Mohit Kataria 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding brain states requires models that capture both the evolution of neural activity and interactions among groups of brain regions. Existing EEG methods often treat recordings as multivariate time series or represent functional connectivity with pairwise graphs, leaving dynamic higher-order interactions largely unmodeled. We introduce the Temporal Simplicial Neural Network (T-SNN), which represents EEG recordings as sequences of evolving simplicial complexes. By combining simplicial convolutions with recurrent updates, T-SNN jointly learns higher-order interactions and their temporal evolution. On the seven-class SEED-VII emotion recognition task, T-SNN outperforms convolutional, recurrent, graph-based, and Transformer methods in both trial-wise and cross-subject evaluations. Incorporating eye-movement features further improves performance, demonstrating the framework's potential for multimodal brain-state decoding.

---


### 545. [DeMark: A Query-Free Black-Box Attack for Quality-Preserving Audio Watermark Removal](https://arxiv.org/abs/2609.34003)

**<font color=#1a73e8>作者：</font>** Weikang Ding, Binhao Ma, Hanqing Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Audio watermarking protects digital speech by embedding imperceptible signals for ownership verification and misuse tracing. However, the security of learning-based watermarking remains insufficiently understood under realistic adversarial removal, where attackers cannot access or query the watermark encoder, decoder, or detector. Existing attacks either rely on model feedback, require clean-watermarked pairs, or reconstruct the waveform with generative models, often leading to high query costs, limited generalization, or degraded perceptual quality. In this paper, we propose DeMark, a query-free black-box attack for quality-preserving audio watermark removal. Our key insight is that watermark embedding, while perceptually hidden, can introduce subtle non-speech artifacts in the time-frequency domain that are not fully aligned with natural speech. DeMark removes watermarks by suppressing these artifacts through two stages: Diverse Artifact Learning, which extracts complementary non-stationary and stationary artifact patterns, and Adaptive Artifact Scaling, which adaptively combines and amplifies them under quality-preserving constraints. Across two speech datasets and four state-of-the-art watermarking methods, DeMark achieves average attack success rates of 0.92 and 0.96 while consistently preserving higher perceptual quality than existing adaptive attacks. These results reveal a practical vulnerability of current audio watermarking systems and call for more robust watermark designs against query-free adversarial removal.

---


### 546. [When Known Physics Helps Neural PDE Models: Residual Constraints Out-Regularize Generic Priors for Nonlinear Dynamics](https://arxiv.org/abs/2609.34012)

**<font color=#1a73e8>作者：</font>** Zahra Farazpay, Aniruddha Bora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE surrogates increasingly incorporate structural priors, yet it is often unclear whether their gains arise from physics-specific information or simply from regularization and training choices. We evaluate several such priors under a common protocol against a matched from-scratch neural operator baseline. Our central result is that a known-equation residual consistently outperforms the best generic regularizer at equal tuning budget. At fixed capacity this benefit appears across linear and nonlinear PDEs, but a capacity sweep reveals a sharp distinction: the advantage persists and grows for Burgers, KdV, and Allen-Cahn, while collapsing toward or below parity for linear heat and advection-diffusion. Thus, the durable value of the residual is specific to nonlinear operators. We further falsify a pre-registered hypothesis that the benefit is activated only by data sparsity: the residual remains advantageous even under full supervision. Its usefulness does, however, have a clear boundary. Under grid under-resolution, nonlinear coarse fields no longer satisfy the naive governing-equation residual, and enforcing it becomes actively harmful. In contrast, cross-family pretraining and in-context conditioning fail to outperform the strong from-scratch baseline in the regime studied. Together, these results identify when known physics provides non-redundant information to neural PDE models, when it does not, and when enforcing it introduces bias.

---


### 547. [LTV-CTDNet: Compositional Turning Decomposition for Short-Term Turning-Movement Forecasting](https://arxiv.org/abs/2609.34014)

**<font color=#1a73e8>作者：</font>** Md Atiqur Rahman Mallick, Kamrul Hasan, Robert T. White  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-term turning-movement forecasts can support signal control and corridor operations, but unconstrained neural networks may produce physically impossible negative counts or outputs that are not explicitly tied to an approach-demand total. This study introduces the Linear Temporal-Variable Compositional Turning Decomposition Network (LTV-CTDNet), a forecasting framework designed to combine competitive accuracy with structurally admissible outputs. LTV-CTDNet was evaluated using seven months of 15-minute LiDAR observations from eight monitored corridor locations in Nashville, Tennessee. Its lightweight encoder combines recent turning-movement history, weekly time-slot embeddings, and location embeddings. The Compositional Turning Decomposition framework separately predicts nonnegative approach totals and within-approach turning proportions, then reconstructs movement forecasts from these components. Among the evaluated predefined configurations, LTV-CTDNet achieved a movement-level MAE of 1.8189 and RMSE of 3.8072. Its accuracy gains over the strongest sequence models were modest, but it produced no negative forecasts, while unconstrained learned models generated negative values in approximately 10.6% to 29.2% of raw forecast cells. The framework enforces nonnegative outputs and exact agreement between each model-predicted approach total and the sum of its component movements by construction, providing directly interpretable forecasts without clipping or coherence correction.

---


### 548. [A Computer Vision Approach to Visual Fraud Detection in Phishing Websites Using YOLOv8](https://arxiv.org/abs/2609.34015)

**<font color=#1a73e8>作者：</font>** Basil Sajid Shaikh, Hajar Homayouni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Phishing remains one of the most common vectors for financial and identity fraud, and most detection systems still rely on inspecting a page's URL, HTML markup, or domain registration history. These signals are easy for an attacker to rotate or obfuscate, and they say very little about what actually convinces a victim to hand over a password or a card number: the way the page looks. This paper describes a visual, image-based approach to phishing detection that treats a rendered webpage the same way a human eye would, as a picture that either matches a trusted brand or doesn't. A YOLOv8 convolutional neural network was trained to classify full-page website screenshots as phishing or legitimate based on layout, logo placement, color scheme, and login-form structure, rather than on text extracted from the page. The system reached 92% classification accuracy on a held-out test set, processed a single screenshot in roughly 100 milliseconds, and, after a round of data augmentation aimed specifically at lighting, compression, and scaling variation, cut the false-positive rate by 11% relative to the pre-augmentation baseline. The paper walks through the dataset construction, the augmentation strategy, the model architecture and training setup, and the resulting performance, and closes with a discussion of where this kind of visual detector fits alongside, rather than instead of, existing URL- and content-based defenses.

---


### 549. [SR4-Fit: A Unified Interpretable Rule-Based Machine Learning Framework for Informative and Trustworthy Decision-Making](https://arxiv.org/abs/2609.34019)

**<font color=#1a73e8>作者：</font>** Shyam Sundar Murali Krishnan, Dean Frederick Hougen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many high-stakes applications, machine learning is dominated by black-box models that require post hoc explanations to justify their predictions. These explanations are often unreliable because they do not reflect the model's actual computations, limiting accountability and trust. A natural alternative is to use models that are interpretable by design. However, existing rule-based approaches, such as RuleFit and decision trees, while transparent, often lack stability and predictive strength, reinforcing a perceived trade-off between traditional performance measures and model understandability. To address this, we propose Sparse Relaxed Regularized Regression Rule-Fit (SR4-Fit), an intrinsically interpretable algorithm for both classification and regression that produces compact and stable rule sets without sacrificing performance. Using demographic data from the U.S. Census Bureau's American Community Survey, SR4-Fit predicts U.S. House election outcomes with high accuracy and interpretability while uncovering demographic interactions missed by black-box models. We further validate SR4-Fit across fourteen benchmark datasets (six classification and eight regression), where it outperforms existing rule-based methods, including RuleFit and decision trees in terms of accuracy, stability, and compactness while remaining competitive with black-box models in predictivity. These results demonstrate that interpretability and predictive reliability need not be mutually exclusive, offering a practical and transparent alternative for high-stakes decision-making.

---


### 550. [Structure-Adaptive Tree Field Integrators](https://arxiv.org/abs/2609.34025)

**<font color=#1a73e8>作者：</font>** Millend Roy, Soham Samal, Ivan Zelich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a new class of near-linear algorithms for efficiently integrating general tensor fields defined on trees with distance dependent kernels, the Structure-Adaptive Tree Field Integrators (STAD-TFIs). STAD-TFIs exploit the tree's underlying structure through decompositions built around path backbones and single vertex separators, and use two-dimensional fast Fourier transforms to compute interactions jointly. By exploiting this structural information, STAD-TFIs achieve more computationally efficient integration than their regular efficient tree field integrators (TFI) counterparts. We provide a detailed theoretical analysis of our proposed approach and complement it with an exhaustive empirical evaluation, ranging from speed tests on synthetic trees, through accelerated Sinkhorn-based relaxations of the Optimal Transport algorithms on real meshes, to Topological Attention Transformers for vision tasks. To the best of our knowledge, we provide some of the first results showing that efficient to compute and accurate relaxations of the geodesic Sinkhorn-based solutions of the Optimal Transport problem can be derived by applying fast TFI methods.

---


> [!TIP]
> 当前位于：**501-550**（第 11/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
