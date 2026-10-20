# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 201. [Stable Signer V3: 4D Deformable Primitive Splatting Is All You Need for Sign Language Production](https://arxiv.org/abs/2610.24926)

**<font color=#1a73e8>作者：</font>** Sen Fang, Liwei Che, Dimitris N. Metaxas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Stable Signer V3, an interactive high-resolution sign language avatar system built on 4D Deformable Primitive Splatting. It addresses three limitations of existing avatars: restricted facial expression, inaccurate identity-specific body deformation, and loss of fine appearance details. Shared Face Primitive Splatting adds transferable superquadric primitives for richer expression control; Test-Time Body Primitive Splatting learns an identity-specific virtual muscle layer for more faithful motion; and Test-Time Tunneling Super-Resolution uses TunnelingNet to recover identity-specific high-resolution details. Both test-time modules are optimized once per signer identity; inference then runs entirely from the stored identity parameters. Together, they reduce facial geometry error by 71.4%, body-boundary error by 35.1% across ten identities, and high-resolution RGB reconstruction error by 24.2% on held-out evaluations, while retaining interactive streaming.

---


### 202. [MLFont: Machine Learning-Driven Font Subsetting and Range-Compact Unicode-Range Slicing for Low-Latency Web Typography](https://arxiv.org/abs/2610.24937)

**<font color=#1a73e8>作者：</font>** Quan Wang, Yiran Mao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> CSS3 @font-face rules with unicode-range descriptors partition web fonts into downloadable slices. While Latin fonts need ~20 KB in WOFF2, Pan-European (LGC) and East Asian (CJK) fonts contain 2,297-30,759 codepoints (158 KB-5.9 MB in WOFF2), where heuristic partitioning causes unused-glyph downloads, high HTTP RTT, CSS bloat, or missing-glyph fallbacks. We present MLFont, a machine learning and optimization framework that learns font slicing strategies from corpora via three stages: (1) a Zipfian High-Frequency Tier (most) isolating top-frequency codepoints; (2) a Latent Co-Occurrence Topic Tier using Online Variational Bayes LDA (Online LDA) or a Deep Neural Network Topic Model (DNNTM) with Shannon Entropy Difference Loss and Sinkhorn-Knopp normalization; and (3) a Memetic Range-Compact Genetic Algorithm (GA) with Potts-Viterbi dynamic programming and island bridging that minimizes topic discrepancy and CSS fragmentation. Across five Google Noto fonts (LGC, KR, JP, TC, SC), MLFont cuts 3G per-glyph latency by 56.7%-75.3% over single-file delivery and 46.1%-66.3% over equal-bin baselines on CJK with 100% coverage, reduces CSS intervals by 17.9%-41.7%, and achieves 1.56x-6.09x cold-cache speedups (65.4%-84.9% CJK and 44.7% LGC bandwidth savings) across 20 websites in simulator and Headless Chrome benchmarks (45/45 exact slice-set parity).
Code: this https URL
Models: this https URL

---


### 203. [LowNet: Looped Wavelet Neural Networks with 24 Learnable Parameters for Solving Poisson Equations](https://arxiv.org/abs/2610.24941)

**<font color=#1a73e8>作者：</font>** Yuanhao Gong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Poisson equations frequently appear in various fields, such as mathematics, physics and informatics. Solving Poisson equation, however, is challenging. Traditional methods are not data-specific, although have high certainty. They require a large number of iterations due to the CFL numerical stability. In contrast, deep learning methods are data-driven and more efficient, but require accurate training data and suffer from heavy computation. To tackle these issues, we propose a wavelet-inspired Poisson solver with 24 trainable scalars. The proposed network has several advantages. First, it is compact. It has four independent $5\times5$ kernels, each represented by six parameters, leading to 24 scalars in total. Such compact format can be deployed on most devices. Second, thanks to the loop design, it achieves higher accuracy than previous methods. A residual loop reuses the wavelet block without increasing its parameters. Numerical experiments confirm that such loop indeed improves the solving accuracy. On 10000 images, one, two, and three loops of the wavelet block lead to PSNRs of $47.27$, $74.14$, and $100.74$ dB, respectively. Third, the proposed method is computationally fast. Thanks to the wavelet transform, the proposed method has linear computation complexity, leading to high computation performance. In short, we propose a novel looped wavelet neural network with compactness, accuracy and efficiency for solving Poisson equations. Our method can be applied in various fields, such as computational fluid dynamics, image reconstruction, biomedical engineering, electromagnetic field simulation.

---


### 204. [Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research](https://arxiv.org/abs/2610.24944)

**<font color=#1a73e8>作者：</font>** Yue Huang, Zhangchen Xu, Xiaonan Luo 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches. Its experiments run across session boundaries, and a fixed verifier evaluates their outputs. Épi produced 120 record-setting results, comprising 20 numerical bound records across 12 families and 100 construction records across eight families. These include an approximately 84-fold narrower interval for the $n$-queens constant and a more than 3.6-million-fold narrower rigorous interval for the quartic Feigenbaum attractor dimension. Exact dual certificates establish that the Cohn-Elkies linear-programming bound cannot be sharp in dimensions 10 and 11. Beyond numerical improvements, Épi gives a computer-assisted proof of Tuza's conjecture for split graphs with an eight-vertex clique part and at most three triangle-active neighborhood types, with arbitrary multiplicities. We extend this research process to algorithmic coding with Épi-turbo, a lightweight configuration that develops executable solvers for tasks including vehicle routing, scheduling and production planning. On 30 FrontierOR tasks, Épi-turbo achieves a 5.4% higher total benchmark score than Codex at 64% of its model cost, using the same underlying model and reasoning effort. Épi is designed to support human understanding by connecting computational results to explicit methods and mathematical arguments that researchers can examine and build upon.

---


### 205. [Label-Space Mismatch Distorts Cross-Cohort Evaluation in Breast Cancer Molecular Subtyping](https://arxiv.org/abs/2610.24962)

**<font color=#1a73e8>作者：</font>** Suxing Liu, Byungwon Min, Zhijian Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-cohort evaluation of breast cancer subtype classifiers is unreliable when source and target cohorts use different annotation standards: METABRIC labels six classes, PAM50 defines five, and a claudin-low prediction cannot be correct under a five-class standard. A classifier transferred from 1,369 METABRIC patients (train n=958) to TCGA-BRCA (n=987) and GSE21653 (n=266) separates three evaluation operations routinely conflated in cross-site comparisons. (1) Label-space restriction - an evaluation-rule change, not a retraining gain - is the dominant correction (73.76%->79.74% on TCGA-BRCA; 63.16%->68.42% on GSE21653); (2) EM prior correction on the reconciled space is an optional calibration step (Brier fidelity up, macro F1 down; to 80.65% and 74.06%); and (3) the target label space is not recoverable from unlabelled predictions (EM retains prior 0.0751 on the absent class; calibrated detectors fail), so compliance must come from cohort documentation. The protocol exposes why internal validation overstates cross-cohort value: multimodal fusion gains do not transfer (no configuration beats mRNA alone, n=694; McNemar p=0.13-1.00), and the genomic panel adds nothing to pathological complete response prediction over clinical variables (DeltaAUC = +0.0045). Clinically, without label-space compliance, cross-site accuracy comparisons misattribute annotation-standard differences to model skill; Luminal A/B and claudin-low boundary errors map to distinct treatment decisions; and subtype accuracy is a weaker portable endpoint than survival discrimination (external C-index 0.577-0.584). Reporting the cohort's allowed label set and applying label-space compliance are therefore prerequisites before any cross-cohort performance claim.

---


### 206. [Meta Inverse Prompting for Video Generative Models](https://arxiv.org/abs/2610.24965)

**<font color=#1a73e8>作者：</font>** Yerin Jung, Jongheon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generative models have enabled flexible conditional generation and editing pipelines, such as text-to-video, image-to-video, and reference-guided synthesis. However, these workflows are inherently one-directional, mapping conditions to videos without providing a mechanism to invert this process. In complex media production settings, the ability to recover controllable textual conditions from a given video is highly desirable, yet remains underexplored. While inverse prompting has been studied for image generation, directly extending these approaches to video is challenging due to the need to capture temporal dynamics beyond static appearance, as well as the substantial computational cost of per-video optimization. In this work, we propose the first practical framework for efficient video inverse prompting. Specifically, we formulate inverse prompting as a meta-learning problem and introduce Meta Video Inverse Prompting (MVIP), which learns a meta-prompt optimized over temporal dimensions to enable fast and effective prompt inference. Our approach amortizes the inversion process, eliminating the need for costly iterative optimization at test time. Experimental results demonstrate that MVIP recovers higher-quality inverse prompts with significantly improved reconstruction fidelity compared to image-based inversion and iterative captioning baselines, while achieving substantial gains in efficiency. Code and video results are available at this https URL.

---


### 207. [Towards Human-AI Complementarity for AI Safety](https://arxiv.org/abs/2610.24969)

**<font color=#1a73e8>作者：</font>** Sander Lanbo Shi, Miranda Anna Christ, Eric Modesitt 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safely overseeing AI is increasingly challenging for the humans doing it, as they must evaluate longer and more complex outputs with every new model generation. To mitigate this challenge, we could leverage complementarity: where humans and models make different mistakes, combining their judgements could yield an oversight signal stronger than either produces alone. We study this opportunity in realistic, safety-relevant settings, contributing the largest known suite of such tasks (3,957 instances across 8 datasets and 6 domains) as well as a platform and data pipeline for measuring human, AI, and human-AI performance on matched items. We collected 35,613 judgements from 416 human raters, finding a considerable opportunity for a complementarity effect. We also found that with the assistance methods we tested, human raters corrected the AI's errors less often, even when overall human accuracy rose, and the hybridisation methods we tested added little over the better single source on average. While complementarity is an important and feasible engineering target for safe oversight, achieving it remains an open challenge for future work.

---


### 208. [MultiAltitudeSR: Multi-Altitude Agricultural UAV Image Super-Resolution via Physical Ground Sampling Distance Conditioning](https://arxiv.org/abs/2610.24992)

**<font color=#1a73e8>作者：</font>** Xintong Jiang, Yu Tian, Yixue Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) enable high-throughput platforms for crop monitoring but face a fundamental trade-off between flight altitude and image spatial resolution. Many existing super-resolution (SR) methods for UAV imagery rely on oversimplified synthetic degradation models and are restricted to fixed integer upsampling scales, limiting their ability to handle real-world degradations and varying flight altitudes. This study proposes MultiAltitudeSR, a framework that conditions feature modulation and reconstruction on source and target ground sampling distances (GSDs). MultiAltitudeSR trained jointly on real UAV images at altitudes of 10 to 70 m above ground level supports all 21 source-to-target altitude pairs without pair-specific fine-tuning, covering scale factors ranging from 1.18$\times$ to 6.03$\times$. The framework can be extended to additional source-target GSD combinations by incorporating corresponding image pairs into training. On the 20-to-10 m pair, the model achieved competitive perceptual performance compared with pair-specific baselines, with LPIPS of 0.2236, DISTS of 0.2431, and NIQE of 8.9020. Experiments using the same architecture demonstrated the value of acquiring real-world multi-altitude UAV image pairs for SR training, with real-pair training achieving better average reconstruction performance across the 21 altitude pairs than training with the tested synthetic degradation pipeline. Downstream zero-shot segmentation case studies illustrated task-dependent benefits of super-resolved imagery for crop monitoring, suggesting potential UAV flight-time savings through image acquisition at higher altitudes.

---


### 209. [When Does Better Acceptance Pay? A Controlled Study of Speculative Decoding](https://arxiv.org/abs/2610.24993)

**<font color=#1a73e8>作者：</font>** Yongchao Long, Chunrui Zheng, Yuxuan Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The throughput gains of speculative decoding depend on the trade-off between acceptance length and execution latency. We ask when additional acceptance is worth the cost of obtaining it. We establish a comparison protocol spanning training, inference, and evaluation, remeasuring released checkpoints and retraining six drafter recipes on shared target-generated data across ten benchmarks and two target models. Alignment changes the picture: gaps that appear large in published comparisons shrink substantially under shared training and inference conditions. This narrowing motivates two deeper questions: how is acceptance improved at different costs, and when do these gains improve throughput? We find that acceptance can be improved through nearly free objective and context changes or more expensive token-to-token conditioning. DCore illustrates the former route as a strong baseline with little additional measured drafting overhead. The payoff is conditional: task uncertainty and serving conditions affect acceptance returns, execution costs, and the preferred drafter and budget. These findings inform future drafter design and deployment choices.

---


### 210. [Block Recursive Transformers for Structured Parameter Sharing](https://arxiv.org/abs/2610.24998)

**<font color=#1a73e8>作者：</font>** Josep Marques, Hyunyoung A. Cho, Youngeun Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive Transformers depend not only on how many parameters are shared, but also on how shared parameters are organized across depth. Existing static schemes adopt two extreme reuse topologies: layer-wise repetition, where each layer is reused independently, and global cyclic reuse, where the entire stack is repeatedly applied as a single shared function. We argue that sharing granularity is an important factor in recursive parameter sharing. This study proposes Block Recursive Transformers (BRT), which partition layers into contiguous blocks and recursively reuse each block before moving to the next. This intermediate topology enables local refinement within blocks while preserving depth-wise transitions, without adding routing modules, auxiliary states, or extra training objectives. Across decoder-only models up to 1.7B parameters, with additional encoder-decoder and encoder-only studies, BRT improves validation negative log-likelihood and downstream accuracy over static recursive sharing baselines. Ablations and representation analyses further show that intermediate block granularity better balances local refinement and depth-wise differentiation. Project website: this https URL

---


### 211. [FineSplat: Fine Patches, Local Groups, Detailed Splats](https://arxiv.org/abs/2610.25011)

**<font color=#1a73e8>作者：</font>** Hyebin Kim, Hwasik Jeong, Joonhyuk Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) promises instant scene reconstruction with high-quality novel-view synthesis. Yet, fine-grained geometry and appearance remain difficult to recover, motivating us to revisit how feed-forward models represent, aggregate, and refine detailed visual information. We introduce FineSplat, a feed-forward 3DGS framework built around fine-grained image patches. Since global multi-view attention becomes prohibitively expensive at such high token resolutions, we develop a dual-grouping strategy that combines two complementary forms of locality: view-wise grouping enables efficient interaction among neighboring views, while 3D spatial grouping reconnects geometrically related tokens that may never have interacted under view-wise grouping by lifting them into the 3D scene space. We further leverage reconstruction error as direct feedback, providing an explicit rendering-based signal to recover fine-grained structures and appearance, thereby overcoming the limitations of one-pass feed-forward prediction. Finally, a compact Gaussian generation scheme preserves the benefits of fine-grained features without unnecessarily increasing the number of primitives. Together, these designs enable FineSplat to recover richer geometry and appearance while remaining efficient and compact, achieving state-of-the-art results by a substantial margin, under the same or smaller Gaussian budgets than existing methods.

---


### 212. [Latent World Models Should Plan with Distances Along the Latent Manifold](https://arxiv.org/abs/2610.25013)

**<font color=#1a73e8>作者：</font>** Zunzhi You, Linwei Tao, Siyu Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models such as LeWM plan by searching for an action sequence whose predicted terminal latent is closest to the goal latent under an ambient norm, such as the Euclidean distance. Planning with such a cost assumes that proximity in the ambient latent space reflects proximity to the goal in the environment. Studying LeWM, we find that this assumption holds only in a small neighborhood around the goal, whereas farther away the L2 cost forms spurious low-cost basins that trap the planner. Yet neighborhood-based embeddings show that the latents retain the underlying physical state. We therefore hypothesize that the latents lie near a curved, low-dimensional manifold, and that the terminal cost should measure the distance along this latent manifold rather than through the ambient space. To estimate this manifold distance, we propose the Neighborhood Graph Cost (NGC), which computes shortest-path distances on a mutual nearest-neighbor graph constructed over training latents. NGC changes only the terminal cost and requires no retraining. This single change improves the planning success rate of LeWM across all four benchmark tasks and nearly solves TwoRoom and Reacher: even at the farthest goal offsets tested, NGC reaches 95% and 100% success, whereas the L2 cost falls to 27% and 81%. These results support the manifold hypothesis and our argument that latent world models should plan with distances along the latent manifold.

---


### 213. [Multifidelity Monte Carlo Estimator for High-Dimensional Quantities of Interest](https://arxiv.org/abs/2610.25016)

**<font color=#1a73e8>作者：</font>** Zhibo Dai, Hamdi A. Tchelepi, Daniel M. Tartakovsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multifidelity Monte Carlo (MFMC) reduces the cost of estimating the statistics of quantities of interest (QoIs) computed via expensive high-fidelity model by using cheaper low-fidelity models as control variates. We extend MFMC to vector-valued QoIs by replacing the scalar control-variate coefficients with matrices and minimizing a weighted mean-squared error. The optimal full-matrix coefficients are available in closed form, and their variance reduction is summarized by an effective correlation that takes the place of the squared Pearson correlation in the closed-form MFMC design. Restricting the coefficients to block-diagonal, diagonal, and scalar classes gives a nested hierarchy of estimators with increasing variance reduction and increasing pilot-data demand, with closed-form coefficients for compatible weightings. For a scalar QoI obtained by linearly projecting the state, correcting the full state before projecting is never worse at the population level. Experiments on a Gaussian problem, a reduced-order model of an advection--diffusion problem, and a coarse-grid two-phase flow problem show that the best class depends on the pilot size relative to the number of covariance quantities it must estimate, and that reusing the pilot samples lowers the mean-squared error.

---


### 214. [Decentralized Online Exp-Concave Optimization](https://arxiv.org/abs/2610.25017)

**<font color=#1a73e8>作者：</font>** Hao Qiu, Mengxiao Zhang, Yuanyu Wan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized Online Convex Optimization (D-OCO) is a fundamental framework in which a set of local agents aims to minimize a sequence of global loss functions using only local computations and communications. While recent work has established near-optimal regret guarantees for convex and strongly convex losses, the case of exp-concave losses remains an open challenge: specifically, whether logarithmic regret is achievable. In this paper, we answer this question affirmatively by proposing Decentralized Online Newton Step (D-ONS), which adapts the idea of blocking and accelerated gossip to the Online Newton Step algorithm in a non-trivial manner. Concretely, our algorithm achieves a regret bound of $O\left(Nd(1-\sigma_2)^{-1/2}\,\log^2(T) \right)$ where $N$ is the number of agents, $d$ is the dimension, $T$ is the horizon, and $1-\sigma_2$ represents the spectral gap of the network. To our knowledge, this is the first logarithmic regret bound for decentralized online exp-concave optimization. We further establish a nearly matching lower bound of $\Omega\left(Nd (1-\sigma_2)^{-1/2}\,\log(T/N) \right)$ showing the near optimality of our upper bound. Finally, we extend our algorithm to decentralized online linear regression in which the feasible domain is unbounded and features and labels are locally observed. By gossiping covariance and label-feature statistics, we also achieve logarithmic regret.

---


### 215. [Synergy-Aware Residual Flow Matching for Single-Cell Perturbation Prediction](https://arxiv.org/abs/2610.25021)

**<font color=#1a73e8>作者：</font>** Jingrui Wu, Wangyun Dan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting single-cell responses to genetic and chemical perturbations is important for understanding regulatory mechanisms and prioritizing therapeutic interventions. Existing methods have made progress by modeling perturbation-conditioned expression shifts with neural networks, graph priors, foundation-model representations, or distributional generative models. However, combinatorial perturbation prediction remains challenging because much of the response can be explained by additive single-perturbation effects, while the biologically informative signal often lies in a smaller non-additive residual induced by perturbation interactions. Directly generating the full post-perturbation expression profile may therefore allocate substantial capacity to the dominant additive component and underemphasize synergy-specific structure. To address this issue, we propose \textbf{SynGeneFlow}, a synergy-aware flow matching framework that anchors the source distribution at an additive prior and learns a residual flow toward the true perturbed state. SynGeneFlow further incorporates perturbation-conditioned gene interaction modeling, where a static gene-gene mask provides biological structure and a perturbation-dependent deformation bias dynamically modulates gene-gene coupling. To preserve population-level response structure, we align both endpoint distributions and biological residual distributions with MMD-based regularization. We evaluate SynGeneFlow on genetic and drug perturbation benchmarks under observed-single, held-out, and cross-modality settings. The results demonstrate that residualizing flow matching around additive perturbation effects provides a biologically grounded and robust framework for single-cell perturbation response prediction.

---


### 216. [PRET is a few-shot system for pan-cancer recognition without example training](https://arxiv.org/abs/2610.25054)

**<font color=#1a73e8>作者：</font>** Yi Li, Ziyu Ning, Tianqi Xiang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological examination stands as the cornerstone in cancer diagnosis, impacting millions worldwide annually. With the shortage of pathologists globally, artificial intelligence (AI) has emerged rapidly to automate the diagnostics process. However, conventional AI models require substantial labeled data for each disease, posing huge challenges in scalability and practicality. Therefore, we introduce PRET (pan-cancer recognition without examples training), a few-shot system to achieve flexible, scalable, and effective cancer recognition across diverse organs, hospitals and tasks without training. Evaluated on 23 international benchmarks comprising 4,484 whole-slide images, our method outperforms existing approaches across 20 tasks, achieving over 97% area under the curve on 15 benchmarks with a maximum improvement of 36.76%. Notably, PRET delivers clinical-grade diagnostic performance in lymph node metastasis detection using only eight slide examples, outperforming 11 pathologists. By offering a flexible and cost-effective solution for pan-cancer recognition, PRET paves the way for accessible and equitable AI-based pathology systems, particularly benefiting minority populations and underserved regions.

---


### 217. [HCFM: Helmholtz Component Flow Matching for Time Series Anomaly Detection](https://arxiv.org/abs/2610.25059)

**<font color=#1a73e8>作者：</font>** Shyam Sundar Saravanan, Tie Luo, Sanjay Madria  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching (FM) is an efficient simulation-free approach for training flow-based generative models, making it a promising foundation for scalable time-series anomaly detection (TSAD). However, standard FM learns a monolithic vector field in which nominal transport and local density-changing behavior are entangled. This creates a central challenge for TSAD; local expansion and contraction carry crucial anomaly-sensitive information, yet isolating this signal requires expensive Jacobian-trace estimation over the entire field. We propose \emph{Helmholtz Component Flow Matching} (HCFM), an unsupervised TSAD framework that parameterizes the vector field prediction network with separate transport, compression, and residual heads. The transport head is constrained to be divergence-free, so divergence estimation is restricted to the compression head, while a lightweight residual head absorbs the remaining mismatch. This structured parameterization improves scalability and detection performance by separating volume-preserving nominal transport from density-changing compression, yielding cleaner anomaly signals from distinct deviations of nominal behavior. Experiments on large-scale univariate and multivariate TSAD benchmarks show that HCFM consistently improves detection accuracy while maintaining efficient inference compared with 16 baselines. The code is available at this https URL

---


### 218. [Policy Is Not Capability: Some Safety Benchmarks Measure Which Definition of "Unsafe" You Trained On](https://arxiv.org/abs/2610.25060)

**<font color=#1a73e8>作者：</font>** Vahid Jebraeeli, Jonathon Romero, Yijin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A guardrail classifier is reported as if unsafe were a property of text. It is not: it is a property of a policy, and the policy enters the model through its labels. We exploit an accident of an industrial deployment in which the same ~53k prompts were labelled twice, under two operational definitions ("is this a request for harmful content?" and "would a moderator block this?"), and used to train ten guardrail arms sharing architecture, codebase and optimiser family, at two model scales. First, the guardrail's own training corpus already contained the benchmarks: JailbreakBench-benign is 88% and OR-Bench-hard 82% present in the training pools, two over-refusal benchmarks, the kind a guardrail reports to argue it does not over-block. Everything below is decontaminated. Second, safety benchmarks stratify sharply by how much of their score is decided by the label definition rather than by the model: with architecture and optimiser fixed, the range across the ten arms is 0.99 on HarmBench-copyright and 0.043 on WildGuard-benign, a 23x spread. Third, a benchmark score can be moved across its entire range by 0.03% of the parameters. Across these arms HarmBench-copyright spans 0-100 and OR-Bench-hard over-refusal 3.4-56.4%, and the four arms whose last supervision signal carries a given policy occupy one extreme of both (exact rank p=0.005, or 0.04-0.14 at worst), at unchanged detection capability. For a distilled student the teacher's soft labels do this even when every hard label carries the other policy, so teacher provenance is an unrecorded confound in any released checkpoint. Fourth, validation accuracy on the one split that grades all twenty arms tracks agreement with the annotator's policy (rho=+0.74), not detection capability (rho=+0.34). We argue that guardrail evaluations should report contamination, a seed floor and the definition they were graded against as first-class variables.

---


### 219. [The Optimal Sample Complexity of Pointwise Replicable Agnostic Learning](https://arxiv.org/abs/2610.25062)

**<font color=#1a73e8>作者：</font>** Guangjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pointwise replicability asks that two independently trained predictors, using the same random seed, agree at each fixed query with high probability. We determine its optimal agnostic sample complexity on finite and countable domains. For every nonempty binary class of finite VC dimension $d\ge1$, the required number of independent examples is $\Theta\!\left(\frac{d}{\rho^2\alpha^2}+\frac{\log(1/\beta)}{\alpha^2}\right)$, uniformly over independent accuracy, failure, and disagreement parameters $\alpha,\beta,\rho\in(0,1/10)$. The learner returns one binary function, may be improper, and uses unrestricted shared randomness. Its sample budget is fixed before observing data, and the replicability guarantee includes queries of zero marginal mass. The main construction combines an ensemble of empirical-risk minimizers with a smooth, signal-dependent risk decomposition. A single shared phase selects the final binary predictor. Record times certify its weak-signal risk, while a uniform bound protects the strong-signal risk at that same selected time. A phase-comparison theorem controls the actual shared-seed execution under simultaneous changes in the marginals and risk coefficients. A rare repair step then makes the confidence cost additive. Together with matching lower bounds, this removes the remaining logarithmic overhead and parameter restrictions in the general countable-domain sample-complexity problem. This extended version also retains the earlier explicit constructions and their proofs, including proper learning for VC-one classes, the full finite-atom class, a faster realizable bound, and counterexamples that separate restrictions of particular algorithms from restrictions of the learning problem.

---


### 220. [Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks](https://arxiv.org/abs/2610.25069)

**<font color=#1a73e8>作者：</font>** Shenqi Zhou, Qiran Zou, Wenhao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are increasingly capable of developing machine learning (ML) models end to end. In medical practice, however, strong performance on the target metric does not fully characterize how good the models are in real-world use cases. For example, medical ML models should also provide well-calibrated risk estimates and remain robust across patient populations. Yet autonomous model development is typically guided by task objectives that emphasize simple predictive discrimination (e.g. AUROC). This raises a key question: are these objectives sufficient to guide agents toward models that meet the broader requirements of real-world medical use? In this study, we introduce Auto-MD-bench, a benchmark of 15 real-world medical tasks from 10 clinical datasets, spanning survival analysis, classification and sequential prediction, with external validation across cohorts, hospitals and time periods. We evaluate four agents: AIDE, AI Scientist v2, Codex, and Autoresearch. The strongest agents achieve competitive primary scores, yet their predicted risks are less calibrated than those of the simple baseline models, which could lead to severe medical accidents. Moreover, models with nearly identical primary scores can exhibit markedly different calibration, while performance varies substantially across population shifts. These findings show that primary task performance alone is insufficient to assess autonomous clinical modeling and multiple different metrics widely used in healthcare practice need to be taken into consideration.

---


### 221. [MoWE: Spatially Adaptive Mixture-of-Wavelet-Experts Pooling for Ultrasound Lesion Segmentation](https://arxiv.org/abs/2610.25074)

**<font color=#1a73e8>作者：</font>** Reaz Hassan Joarder, Sidratul Tanzila Tasmi, Alif Arshad Bakshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Mixture-of-Wavelet-Experts (MoWE), a spatially adaptive routing mechanism that replaces max-pooling and strided convolutions in U-Net architectures for ultrasound lesion segmentation. Standard pooling operations suppress high-frequency spatial details, including potential boundary cues in speckled regions. Recent frequency-domain methods preserve some of these details, but a single wavelet family applies the same spectral bias across the image. MoWE instead uses a context-aware router to assign local regions to fixed wavelet families according to local texture and global feature context. The decoder reuses the encoder's spatial routing maps during the inverse transform. Learnable channel-wise gates rescale the high-frequency subbands before reconstruction. We evaluate MoWE with U-Net on four ultrasound lesion benchmarks (BUSI, TN3K, UDIAT, BUS-UCLM) and one cardiac dataset (CAMUS), and with nnU-Net on BUSI. On BUSI, MoWE improves U-Net Dice from 72.59\% to 74.55\% and reduces HD95 from 47.01 to 43.49\,px. With nnU-Net, MoWE improves Dice from 80.18\% to 81.97\% and reduces ASSD from 20.07 to 17.25\,px. On U-Net, MoWE reduces trainable parameters by 6.4\%.

---


### 222. [MoCKEFA: Model-Conditioned Keyframe Extraction and Fair Attribution for Video Model Explanation](https://arxiv.org/abs/2610.25075)

**<font color=#1a73e8>作者：</font>** Lahiru Wijayasingha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We show that a video can be represented with just a few keyframes without sacrificing a given model's belief about the video. Our method is the first of its kind that extracts these keyframes conditioned on the model's prediction, which is massively helpful for building explainable video models. We then fairly distribute the importance of the video to the model among the keyframes with game theoretically fair Shapley values. Through qualitative and quantitative experiments, we show that keyframe attribution is superior to the traditional frame attribution. Further, we conduct preliminary exploration on highlighting the important changes among the frames by looking at the differences between adjacent keyframes.

---


### 223. [Sufficient Frame Subsets for Video Understanding](https://arxiv.org/abs/2610.25084)

**<font color=#1a73e8>作者：</font>** Lahiru Wijayasingha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding when during a video a model makes its critical observations is essential for interpreting video-understanding systems. However, existing attribution methods often spread evidence diffusely across near-duplicate frames. We introduce Sufficient Frame Subsets: compact sets of frames in which all other frames are masked, yet each subset independently preserves the model's prediction. We evaluate our method on two complementary benchmarks, UCF101 and Something-Something v2, using both CNN- and transformer-based architectures. Our results show that the proposed algorithm identifies highly compact and effective frame subsets for explaining model decisions. We also find that models capable of relying on a greater number of sufficient frame subsets tend to perform better, possibly because they are more robust, consistent with prior research. Finally, the extracted frame subsets help us analyze model failure cases, reveal which aspects of a video the model has learned to emphasize, and identify opportunities for improving future training procedures.

---


### 224. [DAGLoop: Aligning Method Design with Experimental Feedback in Automated AI Research](https://arxiv.org/abs/2610.25089)

**<font color=#1a73e8>作者：</font>** Dengyuxing Wang, Yonggang Zhang, Qianshu Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated AI research agents aim to improve machine learning methods by iteratively proposing, implementing, and evaluating candidate methods. Existing work uses the outcome of each evaluation to determine how the next candidate should be revised for performance improvement. However, a candidate often combines multiple design decisions, and its overall outcome alone does not reveal which decisions produced their expected effects, whether their required conditions were satisfied, or which decisions should be retained or revised. Inspired by ablation studies in the machine learning community, we propose DAGLoop to test the expected effect of a design decision by comparing implementations with and without that decision while preserving the other decisions it requires. Specifically, DAGLoop translates each design decision's rationale into a testable expectation and pairs it with a targeted experiment, forming an experimental specification for assessing the expected effect under its required conditions. Using these specifications, we formulate ablation planning as the construction of a directed acyclic graph (DAG) from the candidate method's design: nodes associate decisions with tests, and edges encode dependencies. The DAG specifies which decisions each experiment must retain and supports joint tests when an expected effect requires several decisions to act together. Outcomes are recorded with the tested decisions, expectations, and conditions to form structured research memory. This memory guides the agent in retaining experimentally supported decisions, revising unsupported ones, and planning further experiments when the evidence is unresolved. Experiments on dozens of research tasks demonstrate substantial performance improvements achieved by DAGLoop across diverse executable research settings. Code and evaluation scripts are available at this https URL.

---


### 225. [Towards End-to-End Privacy-Preserving AI for Real-Time ECG Monitoring](https://arxiv.org/abs/2610.25094)

**<font color=#1a73e8>作者：</font>** Beyazit Bestami Yuksel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Healthcare artificial intelligence is shifting from centralized archives toward distributed pipelines that combine wearables, edge processing, cloud analytics, and multi-institutional learning. In this regime, electrocardiogram (ECG) streams cross multiple trust boundaries, so privacy cannot be reduced to a single transmission control. Existing privacy-enhancing technologies typically secure isolated stages and leave gaps between acquisition, analysis, and institutional collaboration.
This doctoral research develops a unified lifecycle framework for end-to-end privacy-preserving ECG AI. Rather than introducing another privacy mechanism, it orchestrates complementary privacy-enhancing technologies across the clinical ECG lifecycle, allocating each mechanism to the trust boundary where its security, computational, and operational properties are most appropriate. Three interoperable modules instantiate the framework: AES with CKKS-based homomorphic statistics for secure monitoring; adaptive chaotic protection for low-latency edge transmission; and federated learning with homomorphic aggregation under heterogeneous partitions. Across prototype monitoring, signal-security analysis, and simulated collaboration, the programme shows that privacy layers can be composed without collapsing diagnostic utility, while exposing overhead and fidelity limits that constrain clinical translation.

---


### 226. [Generation-Heavy Hybrid Machine Translation](https://arxiv.org/abs/2610.25107)

**<font color=#1a73e8>作者：</font>** Nizar Yahya Habash  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The state of the art techniques in Machine Translation (MT) require large amounts of symmetric resources from source and target languages. This is true regardless of whether the approach is Transfer or Interlingua, Symbolic or Statistical. Symmetry within these approaches is necessary to ensure quality, robustness and retargetability. In reality, such symmetry, whether it is in terms of structural transfer lexicons, interlingual dictionaries or parallel corpora, is a major bottleneck in developing any MT system.
This dissertation presents an approach to MT that addresses the lack of symmetry by exploiting symbolic and statistical target language resources in source-poor/target-rich language pairs. This approach is called Generation-Heavy Hybrid Machine Translation (GHMT). Expected source language resources include a syntactic parser and a simple one-to-many translation dictionary. No transfer rules or complex interlingual representations are used. Rich target language symbolic resources are used to overgenerate multiple structural variations from a target-glossed syntactic dependency representation of source language sentences. Statistical target-language resource are then used to select amongst the overgenerated translations. The source-target asymmetry of systems developed in this approach makes them more easily retargetable to new source languages.

---


### 227. [Self-organizing reinforcement learning: a swarm approaches the explore-exploit optimum](https://arxiv.org/abs/2610.25113)

**<font color=#1a73e8>作者：</font>** Galen J. Wilkerson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The explore/exploit trade-off is the core problem of reinforcement learning (RL). We show that a minimal foraging swarm approaches its optimum - the ideal-free / Nash allocation of a multi-agent resource-sharing game (an equilibrium, not a return maximum) - with no learner and no reward signal. Agents explore by heavy-tailed (Levy) flights, recruit neighbours to a discovery through a threshold cascade on their proximity network, and disperse as a patch crowds; this cascade cycle balances exploration and exploitation and drives foragers toward the ideal free distribution. The swarm attains the shape of this optimum (committed foragers track richness with slope 0.94) but not its exact equilibrium - it stays measurably exploitable - reaching it dynamically (~150 steps) through the coupling of recruitment to movement: remove the coupling and matching collapses (0.94 -> 0.08). The RL sits at the level of the problem and the allocation reached, not the micro-rule: no step evaluates payoff (reward-free by construction, though the crowd signal is informationally tied to payoff), and the swarm reaches the allocation without learning it (quality plateaus and re-settles after resources move, no cumulative gain). Against a trained baseline the comparison is two-sided: in an easier, disembodied game a learner is more precise, while in the same embodied environment the reward-free swarm reaches ~65% of a validated oracle ceiling at zero training and leads until trained PPO and centralised-critic (CTDE) learners overtake it (~74-75%, 16 seeds, all above the swarm mean) after ~4,000 of 15,000 training steps - its advantage is in budget, not asymptote. In this one setting we read it not as beating RL but as a strong zero-shot, reward-free operating point: a demonstration that the self-organizing physics of a minimal swarm can carry a collective close to the optimum RL seeks, with none of RL's machinery.

---


### 228. [Polynomial Learning of Positive ReLU Networks under Gaussian Inputs](https://arxiv.org/abs/2610.25116)

**<font color=#1a73e8>作者：</font>** Zhijie Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study bias-free, one-hidden-layer ReLU networks with nonnegative output weights under standard Gaussian inputs. Hidden directions may be arbitrarily close or linearly dependent. The labels have the target as their conditional mean, and only the unconditional second moment of the noise is bounded. We present a candidate real-arithmetic learning guarantee: a width-$k$ target with total output weight at most one can be approximated to squared prediction error $\varepsilon$ by a nonnegative ReLU network of width at most $k+\min\{k,d\}$, with sample and operation cost $(1+\sigma^2)\operatorname{poly}(d,k,\varepsilon^{-1},\log(1/\delta))$. The argument combines implicit high-order moments with a direction cover that is complete for heavy atoms and sound for every output. Exact Gaussian soft localization refines this cover while pruning keeps at most $k$ centers at every scale. Clipping the query multipliers controls heavy-tailed, input-dependent noise without assuming a uniform conditional variance bound. A final convex fit and an exact sparsification step give the stated output width. We also obtain a parameterized projective direction-recovery guarantee. The result concerns real-arithmetic complexity; no bit-complexity or practical running-time guarantee is asserted.

---


### 229. [How Much Feedback Is Needed to Break Template Protection? The Geometric Vulnerability of Biometric Authentication](https://arxiv.org/abs/2610.25118)

**<font color=#1a73e8>作者：</font>** Eliron Rahimi, Margarita Osadchy, Orr Dunkelman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Biometric authentication systems increasingly use privacy-preserving mechanisms to protect sensitive templates. However, the authentication interface itself may still leak information that enables reconstruction attacks. Prior attacks exploit released similarity scores, whereas more advanced systems reveal only the binary accept/reject decision. This binary feedback provides substantially less information, making template reconstruction far more challenging.
In this work, we introduce query-efficient reconstruction attacks under extremely limited feedback, addressing two key limitations of prior attacks. First, we introduce the first attack that reconstructs protected biometric templates using only authentication success/failure feedback by exploiting the geometric constraints of biometric authentication. Second, we introduce distribution-aware query-efficient reconstruction methods for score-releasing systems, achieving a more realistic threat model by reducing the number of required queries by a factor of $5\times$ compared to recent prior score-based attacks. Finally, we combine these two insights by incorporating a pretrained facial diffusion prior into our geometric binary attack, reducing the number of required queries by a factor of $5\times$.
Our findings reveal a fundamental security limitation of biometric authentication: independently of the template protection mechanism, the authentication process itself exposes geometric information that can enable perfect template reconstruction up to numerical precision. Moreover, the distribution of biometric templates can be leveraged to make significantly more effective reconstruction attacks.

---


### 230. [LC-TSRNet: A Land-Cover-Guided Two-Stage Network for Annual MODIS Surface Reflectance Time Series Reconstruction](https://arxiv.org/abs/2610.25120)

**<font color=#1a73e8>作者：</font>** Wenjuan Zhang, Xuesong Ma, Zhen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MODIS surface reflectance (SR) products often suffer from data gaps due to cloud contamination and sensor malfunctions, limiting their applications in long-term and large-scale studies. Most existing methods rely on cloud-free observations from optical time series or introduce SAR time series as auxiliary information. However, due to the coarse spatial resolution of MODIS, cloud-free reference images are difficult to obtain, and SAR imagery is not well matched to the spatial resolution of MODIS, making it difficult to provide effective prior constraints. To address these issues, this study proposes LC-TSRNet for seamless reconstruction of annual MODIS SR products. In the first stage, an annual land cover map is introduced as prior knowledge, and CSPM is designed by leveraging the spectral similarity within identical land cover types, thereby providing prior spectral constraints for missing regions. In the second stage, to address large-area, persistent, and overlapping gaps in MODIS imagery, SMRM is designed to adaptively exploit and integrate multi-scale spatiotemporal contextual information. Meanwhile, to address the limited collaborative utilization of spatio-temporal-spectral information, 3DAM is designed to impose cross-dimensional joint constraints. Considering the lack of publicly available MODIS sample datasets, this study constructs the AIRMOD-TSR dataset. Extensive experimental results show that LC-TSRNet outperforms the comparison methods and achieves better reconstruction accuracy and spectral fidelity. Under the spatially adjacent scenario, LC-TSRNet improves PSNR by 0.56 dB and reduces SAM by 0.13°. The vegetation monitoring application further verifies the practical value of the reconstructed SR time series.

---


### 231. [HullProbe: Measuring Interventional Part Reliance in Maritime Vessel Classifiers](https://arxiv.org/abs/2610.25137)

**<font color=#1a73e8>作者：</font>** Faisal Mohammad, Mohamed Younis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing a vessel's type from an image supports maritime surveillance and sanctions monitoring, but a classifier can reach high accuracy by leaning on the generic hull instead of the more distinctive superstructure, and is then fooled when a vessel is re-hulled or occluded. De-biasing methods claim to remove such reliance, yet the field certifies them with worst-group accuracy, a proxy that needs group labels and only infers reliance from accuracy. We measure the reliance directly. HullProbe swaps a registered anatomical part of a vessel for another instance's and reads how much that part drives the decision, using a same-class swap to control for compositing artifacts. Because a surface vessel is a hull and a superstructure arranged along one axis, its parts form a 2x3 grid whose 2^6 = 64 swaps we evaluate exhaustively, and a single Walsh transform returns each part's interventional influence and its interaction spectrum. On planted shortcuts, where the true reliance is known, the measure tracks worst-group accuracy (r = -0.94 over 45 configurations), and replacing its learned segmenter with human annotations changes the hull-share by less than the audit's resolution. On the 26 vessel types of MARVEL, the classifier places about 46% of its corrected sensitivity on the generic hull yet follows the superstructure when the two conflict, and the group-label-free de-biasers available there do not detectably reduce the hull's share. The findings hold across three architectures and a second maritime dataset, and the method extends to fine-grained vehicle recognition on Stanford Cars.

---


### 232. [Reflection-Guided Dynamics Rectification for Text-to-Image Generation](https://arxiv.org/abs/2610.25139)

**<font color=#1a73e8>作者：</font>** Shuo Xu, Hanrui Ying, Debin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained rectification of existing generations under a limited additional budget remains a key problem in test-time optimization (TTO) for image generation. As for prior approaches, they could identify residual errors, but could not directly ensure that the model acts on the feedback during reasoning. Such errors stem from multiple sources, such as the initial noise or text prompt, and ultimately induce an execution gap of failing to handle potential deviations along the trajectory generating. However, classic models generally cannot remedy this gap. To narrow it, we propose Reflection-Guided Dynamics Rectification (RGDR), which turns reflections on completed outputs into corrective interventions on the process of sampling dynamics at the trajectory level. Specifically, RGDR could impact every sampling step by adapting to instantaneous intervention. Moreover, RGDR generates flexible candidates while adjudicating between them and the reference. As experiments show, rectification from RGDR starts from the existing base trajectory and reflection, and RGDR is substantially more effective than former trajectory exploration. Under matched budgets for additional image generation, RGDR's gain in the cross-model average final checklist score over the reference is $1.51\times$ that of TIR prompt refinement and $1.81\times$ that of Dynamic CFG.

---


### 233. [Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting](https://arxiv.org/abs/2610.25140)

**<font color=#1a73e8>作者：</font>** Amirhossein Ghaffari, Susanna Pirttikangas, Ekaterina Gilman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting models based on spectral graph convolution offer an interpretable account of how information is mixed between sensors, but they rely on an eigendecomposition of the graph Laplacian. It costs cubic time, is fixed by the road network, and provides a symmetric operator that cannot represent the directed propagation of traffic congestion. Attention-based spatio-temporal transformers remove these limitations but generate a dense sensor-by-sensor attention map at each layer and time step, so memory, rather than accuracy, becomes the binding constraint on large networks. We introduce the spectral adaptive graph transformer, whose spatial operator is learned rather than derived from the Laplacian, directed rather than symmetric, and conditioned on the current traffic state rather than a static state, at a cost linear in the number of sensors. A sparse road graph diffusion branch provides the strictly local propagation that a low-rank operator cannot express, and a zero-initialized gate learns the balance between the two. Before spatial mixing, a unit-mean-gain frequency-bin attention module reweights each sensor's short-term periodicities according to its identity and current context. Across six public benchmarks spanning 170 to 1843 sensors, evaluated over three random seeds, the proposed model attains the lowest error of any single end-to-end model on one benchmark and remains competitive with the strongest current attention models on the others, while using about a quarter of their memory and training about twice as fast.

---


### 234. [Image Dehazing as In-Context Tabular Inference](https://arxiv.org/abs/2610.25142)

**<font color=#1a73e8>作者：</font>** Le-Anh Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image dehazing is traditionally addressed through handcrafted physical priors or task-specific deep learning models, often requiring carefully designed architectures or extensive model training. Recent advances in tabular foundation models (TFMs), however, offer an alternative learning paradigm in which continuous relationships can be inferred directly from contextual examples without task-specific model training. Motivated by this capability, this paper investigates whether single-image dehazing can be effectively reformulated as an in-context tabular regression problem and introduces DehazeTab, a framework that estimates atmospheric transmission from structured image-patch representations. Specifically, overlapping patches extracted from hazy images are transformed into tabular samples using handcrafted haze-related descriptors, pretrained visual embeddings, or their hybrid combinations, while corresponding transmission patches are summarized as scalar regression targets. A pretrained TFM then performs in-context regression using labeled reference patches to predict transmission values for unseen images without any further fine-tuning. These predictions are spatially aggregated into a transmission map, refined through guided filtering, and incorporated into the atmospheric scattering model to recover haze-free images. Experiments on benchmark datasets demonstrate competitive restoration performance and reveal that physically motivated handcrafted features can outperform pretrained visual embeddings, while hybrid representations offer complementary benefits. Further analyses examine the effects of feature representations, patch selection, and contextual reference configurations on restoration quality. Beyond image dehazing, the findings highlight the potential of TFMs as an alternative paradigm for addressing low-level vision tasks through structured and in-context inference.

---


### 235. [FHKAN: Fractional Hermite Kolmogorov-Arnold Networks for Data-Driven and Physics-Informed Learning](https://arxiv.org/abs/2610.25148)

**<font color=#1a73e8>作者：</font>** Arsha Farnoush, Amirhossein Sadr, Aida Pakniyat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) replace fixed scalar weights by learnable univariate maps, yet most spectral KANs still rely on Chebyshev polynomials that live on a bounded interval and therefore require a saturating squashing of the pre-activation. We introduce the Fractional Hermite Kolmogorov-Arnold Network (FHKAN), a neural architecture that equips KANs with an adaptive, trainable fractional-order generalized Hermite basis. With a nonnegative shape parameter, the underlying generalized Hermite functions are orthonormal on the entire real line and uniformly bounded under a Gaussian envelope, so they act directly on unbounded pre-activations without any saturating map. We derive closed-form derivatives of the generalized, fractional, and scaled basis away from the origin and determine its order of differentiability at the origin, where the fractional power map creates a singular point. On synthetic regression, FHKAN attains the lowest test error at every network depth among nine fixed activations and the spline-based KAN. On image classification, image denoising, and sentiment analysis, the best-performing fractional Hermite block yields the highest accuracy or reconstruction quality. On physics-informed problems, FHKAN reaches mean absolute errors of order 10^-6 to 10^-5 on the Lane-Emden equation, residuals of order 10^-4 on the Burgers equation, and absolute errors below 10^-4 on a fractional delay differential equation.

---


### 236. [Learning without Overwriting: Structural Knowledge Fusion for Continual Learning](https://arxiv.org/abs/2610.25150)

**<font color=#1a73e8>作者：</font>** Kanishk Bakshi, Amitansu Pattanaik, Kathiravan Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting in sequential deep learning arises from a fixed-capacity architectural constraint: parameter updates encoding new tasks perturb weight subspaces supporting prior representations. We introduce the Knowledge Fusion Network (KFN), which mitigates the stability-plasticity trade-off in class-incremental learning through novelty-gated structural expansion rather than parameter negotiation within a shared capacity budget. KFN decouples task acquisition from knowledge consolidation: each incoming task is learned in an isolated lightweight specialist network (2.8M parameters) and integrated into the global model via a Structural Fusion Module that allocates dedicated channel capacity conditioned on a quantitative novelty score. Dual structural isolation--channel-space separation with temporally phased gradient unfreezing--protects consolidated knowledge. On ten-task Split CIFAR-100, KFN achieves 11.94% minimum task accuracy and 71.16% task-10 accuracy, whereas shared-parameter baselines degrade severely: LwF to 9.07% average accuracy (0.00% min), Replay++ to 8.91% (85.08% forgetting), and Replay to 16.21% (73.44% forgetting); KFN's forgetting (57.92%) is 15.5 pp lower than Replay. Furthermore, KFN prevents logit-scale drift, maintaining near-symmetric task performance. Across CIFAR-100 and EuroSAT satellite imagery, KFN's class-incremental retention (72.7% and 42.5%) substantially exceeds the best baselines (29.6% and 0.94%). Crucially, KFN achieves parameter-efficient linear scaling, adding 25% of the base parameter count per step and requiring 25.1% of naive backbone duplication over ten tasks (28.1M vs 112.0M). With a 37.1% peak GPU memory reduction over full retraining, KFN establishes novelty-gated expansion as a practical path beyond fixed-capacity architectures.

---


### 237. [M-JEPA: Predictive Self-Supervised Learning for Molecular Graphs with Scaffold-Shift Evaluation on Tox21](https://arxiv.org/abs/2610.25163)

**<font color=#1a73e8>作者：</font>** Karthik Iyer, Nasser Sabar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised molecular representation learning is increasingly used to improve transfer on small, label-limited property prediction tasks, yet commonly used contrastive objectives can be sensitive to view construction and are often evaluated with protocols that report only discrimination. We adapt Joint Embedding Predictive Architectures (JEPAs) to molecular graphs by masking chemically coherent connected subgraphs and training a context encoder to regress the masked target embedding produced by an exponential-moving-average (EMA) teacher. To evaluate predictive self-supervision under realistic distribution shift, we introduce a leakage-resistant, compute-matched three-phase protocol: (i) an 80-run objective screening on ESOL with fixed compute budgets, (ii) JEPA-only refinement of masking and augmentation choices, and (iii) per-assay Tox21 evaluation under Bemis-Murcko scaffold splits with joint discrimination-reliability analysis and attribution diagnostics. Under matched compute, M-JEPA achieves substantially lower ESOL proxy RMSE than a compute-matched InfoNCE baseline (mean RMSE 2.12 vs 3.75; mean paired dRMSE 1.61; 95% bootstrap CI [1.52, 1.72]; Wilcoxon p=2.4e-4) and typically completes runs faster (~15-25 min vs ~35-45 min on a single GPU under identical hardware), albeit with higher runtime variance. On Tox21, improvements in ROC-AUC/PR-AUC are assay-dependent and do not uniformly imply better calibration; reliability diagrams and Brier/ECE metrics reveal endpoints where fine-tuning improves ranking but leaves probabilities miscalibrated.

---


### 238. [Concept Representations in Vector Space: Toward an Interdisciplinary Study of Meaning Variation](https://arxiv.org/abs/2610.25184)

**<font color=#1a73e8>作者：</font>** Simon Josef Durstewitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An increasing number of disciplines recognize the explanatory potential of meaning-bearing mental structures through which individuals interpret the world and guide their behavior. Concept representations constitute a core class of these structures, emerging from individuals' experiences with concept referents and encoding and organizing their understanding of them. Recognizing a private level of meaning, where concepts are not objectively defined by rules in the world but constitute subjective structures in individuals' minds, raises a fundamental question: do different individuals actually mean the same thing when they invoke the same concept? As latent structures, concept representations are difficult to access and model empirically. The present study introduces a measurement framework that makes such representations empirically accessible through textual traces elicited under standardized conditions. Using transformer-based sentence embeddings, the framework maps standardized responses elicited for concepts into a high-dimensional shared vector space, opening concept representations to the systematic analysis of interindividual variation. It develops three analytical avenues: (1) comparing representational sharedness across concepts, (2) identifying variables that correlate with representational variation, and (3) examining how focal actors or subpopulations deviate from a reference population. Each avenue is illustrated through an empirical proof-of-concept drawing on a large-scale free-association dataset. Together, the demonstrations show how researchers from across disciplines can move from a research question and data source to analysis and interpretation. An accompanying GitHub repository provides a ready-to-use implementation of the framework for existing and custom datasets.

---


### 239. [Sampling and Curvature in First-Exit Comparisons for Momentum SGD](https://arxiv.org/abs/2610.25191)

**<font color=#1a73e8>作者：</font>** Haiyi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> First-exit prediction for momentum SGD depends on sampling information that pointwise gradient laws omit. Strongly convex finite pools with identical pointwise laws and matched iid momentum dynamics can have different reshuffled exits; even analytic pools with uniformly close pointwise laws can have separated exit probabilities. For persistent sampling in one dimension, we establish an explicit $O(h)$ mean-exit comparison with a finite-rate switching process under nonvanishing component velocities and step-size conditions; iid sampling instead averages to an ODE. Retaining realized minibatches and sampled curvature yields finite-window exit brackets beyond this regime. In 32 trained ridge-logistic runs, 29 meet prespecified targets with rounding-certified brackets; an enclosure control explains most of the width advantage. Exact-real certificates establish finite means at the original tested radii for three ResNet-18 checkpoints and give local finite-mean conditions for tanh and ViT networks; their upper bounds remain loose, and original-radius ViT mean guarantees remain unresolved despite 128 fresh continuation paths. A two-network replication gives 32/32 successful seeds in each of four finite-path persistence comparisons. Independent equal-length controls retain slower exits after refresh resets than without resets, but the refresh-versus-random ordering reverses with update length at both networks. These interventions do not causally decompose raw momentum SGD. Neural step-size scaling does not validate the switching limit.

---


### 240. [Shallow Probes Are Sufficient for Near-Oracle Personalization Depth Allocation in Federated Learning](https://arxiv.org/abs/2610.25193)

**<font color=#1a73e8>作者：</font>** Beyazit Bestami Yuksel, Emrah Dikbiyik, Ayse Yilmazer Metin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rather than proposing a new federated optimizer, we study whether a small client-specific measurement budget can support cost-aware personalization-depth decisions under a utility that trades Macro-F1 against deployment cost. Exhaustive evaluation of six depths defines an offline oracle that is not deployable. We audit the Probe Sufficiency Hypothesis: three shallow probes (P0--P2) may contain most decision-relevant information for approaching that oracle. FedPBA is a secondary learned instantiation for deep-action extrapolation. On CIFAR-10/100 and patient-disjoint PTB-XL (45 sessions; 900 clients; 2700 evaluations; GroupKFold), training-free greedy probing achieves regret 0.0071 and 98.3 percent oracle recovery, beating metadata-only policies and FedPBA (0.0110 / 97.3 percent). Aggregate shallow-best versus oracle correlation is 0.9818 but falls to 0.578 on deep-oracle rows; PTB-XL deep-oracle cases remain a high-regret boundary without a validated escalation gate.

---


### 241. [A Thousand Faces: A Persuasion Benchmark with Experience-Grounded Persuadees Informed by Psychology and Pragmatics](https://arxiv.org/abs/2610.25206)

**<font color=#1a73e8>作者：</font>** Ziqing Zhuang, Dingyi Zhang, Deyu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People can express the same beliefs and desires yet need different reasons to change their minds. What makes an argument relevant depends on how those views arose: experiences shape what a person finds credible, what matters to them, and what could prompt reconsideration. These personal grounds may also be expressed indirectly, through contextual clues in conversation. Benchmarks that specify beliefs and desires without these connections can reward arguments that match a description while overlooking whether they address the person's reasons. We introduce A Thousand Faces (ATF-Persu), with 1,000 personas across 200 topics and nine domains. Drawing on personality and attitude theories and conversational implicature, we construct five personas per factual context, linking experiences to judgments, expression, and grounds for revision. Evaluations show lower persuasion success than three comparison benchmarks under their respective protocols. Complete backgrounds yield broader use of supplied personal grounds and higher persona faithfulness than simplified specifications; blinded reviewers also rate ATF-Persu above CToMPersu on identifiable personal reasons, their influence on responses, and contextual expression. The dataset is publicly available at this https URL.

---


### 242. [DROD: Dual-Ratio Ordered Dropout for Federated Continual Learning on Heterogeneous Devices](https://arxiv.org/abs/2610.25220)

**<font color=#1a73e8>作者：</font>** Berk Sezer, Özgür Soysal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning for capacity-heterogeneous clients and federated continual learning are each well studied on their own, but their intersection -- clients holding differently sized models while every client's data stream also drifts over time -- remains underexplored. We study this setting directly, training a ResNet-18 fleet from scratch on Split-CIFAR-100 (10 tasks, class-incremental), and introduce DROD (Dual-Ratio Ordered Dropout), which builds on FjORD's Ordered Dropout by using two independent reduction axes to extract sub-models: a shortcut ratio and a branch ratio. On a shared parameter/FLOP budget ladder, DROD achieves the highest mean accuracy among the heterogeneous-model federated learning strategies we compare. Its advantage over the two strongest baseline geometries persists across every replay-buffer size we test and under ER, DER++, and BiC; under EWC, all three geometries collapse alike.

---


### 243. [Map2Vid: Embodied Navigation Video Generation with Human-Friendly Motion Control](https://arxiv.org/abs/2610.25223)

**<font color=#1a73e8>作者：</font>** Yulin Dai, Yuqian Fu, Tianwen Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable video generation has recently achieved impressive visual quality, yet existing control paradigms remain poorly suited to embodied navigation. Text prompts are spatially ambiguous, while camera-trajectory control relies on low-level motion specifications that are unintuitive for human users and difficult to manipulate. In this work, we introduce Map2Vid, a novel task that reformulates embodied navigation video generation as a BEV-map-to-video synthesis problem, together with a large-scale benchmark for systematic evaluation. By using BEV maps, which provide a visual representation of global scene layout and intended navigation routes, Map2Vid enables human-friendly navigation video generation. To support this task, we construct a dedicated dataset with over 100K navigation sequences across 61 indoor scenes, each paired with egocentric videos, BEV maps, camera trajectories and language instructions. We further develop a unified framework that integrates multiple control signals, together with a curriculum training strategy that progressively weakens non-map inputs, enabling flexible inference under both full conditioning and map-only input. Extensive experiments across multiple foundation generation models demonstrate that controllable navigation video generation via BEV map is a viable and promising direction.

---


### 244. [GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation](https://arxiv.org/abs/2610.25245)

**<font color=#1a73e8>作者：</font>** Yuchen Xi, Yuhan Guo, Chenwei Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis under trajectory changes is essential for autonomous driving simulation, yet existing methods struggle to generate consistent videos when extrapolating to unseen viewpoints such as lane shifts. Reconstruction-based approaches maintain geometric consistency but degrade in visual quality under large viewpoint changes, while reconstruct-then-restore methods often produce visually plausible frames yet suffer from geometric and temporal inconsistencies. We present GeoV2V, a geometry-grounded video-to-video diffusion framework that synthesizes temporally coherent driving videos along novel trajectories by integrating LiDAR and depth-derived geometric priors with full-video conditioning in the Wan 2.1 backbone. A key challenge in learning cross-lane transformations is the lack of synchronized multi-trajectory supervision in real-world datasets. To address this, we also introduce Para4D, a synthetic dataset capturing synchronized multi-lane driving videos within dynamic scenes, which provides explicit supervision for lane-shift generation and serves as a strong training prior for geometry-consistent view synthesis. Experiments on Waymo, nuScenes, and Para4D demonstrate state-of-the-art performance in visual quality, geometric consistency, and robustness to complex lighting dynamics under large trajectory shifts. Project page: this https URL

---


### 245. [PanoDent-KD: From Generalist Knowledge Distillation to Cross-Dataset Specialist Detection and Embedded Deployment in Panoramic Radiographs](https://arxiv.org/abs/2610.25256)

**<font color=#1a73e8>作者：</font>** Muhammad Waqas Ashraf, Imad Ali Shah, Ali Hassan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable panoramic-radiograph detection requires consistency across datasets with different class definitions and deployment software. We present PanoDent-KD, an auditable 1280-pixel YOLO26m pipeline linking a 12-class source generalist, feature-level knowledge distillation (KD), exact classifier-row transfer, teacher-free five-class specialization, and embedded deployment. A common training and evaluation pipeline compares three source-training arms across three seeds: a supervised baseline (B1), single-teacher KD (STKD), and multi-teacher KD (MTKD). Five shared classifier rows initialize nine OralXrays-9 specialists, while the backbone, FPN-PAN neck, and dual-detection-head topology are retained unchanged. On the 2,686-image test subset, all three arms achieve macro box F1 near 0.82. B1 achieves the highest three-seed arm-level mean macro box F1 (0.8239$\pm$0.0027) and $mAP_{50:95}$ (0.6130$\pm$0.0067). STKD seed 1, selected after development but before final testing, was used for deployment. Its Jetson Orin Nano Super FP16 TensorRT engine achieves 77.03-ms median and 80.86-ms P95 prediction-call latency, throughput of 12.90 images/s, and gross total-module energy of 1.39 J/image, with high numerical agreement between within-device PyTorch and TensorRT FP16 inference. These findings demonstrate the feasibility of an auditable, device-specific deployment workflow, but do not establish clinical validity or improved target-domain accuracy from KD.

---


### 246. [SemVideoSte: Agentic AI for Cross-Modal Semantic Video Steganography Communication](https://arxiv.org/abs/2610.25257)

**<font color=#1a73e8>作者：</font>** Rui Meng, Song Gao, Tingting Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose an agentic artificial intelligence (AI)-driven cross-modal semantic video steganography communication (SemVideoSte) scheme for secure cross-modal information transmission. Agentic AI interprets the service context to determine a semantically matched public prompt and coordinates video generation, message embedding, semantic transmission, and message recovery process. A multi-mask mechanism combines variational autoencoder (VAE) reconstruction robustness, semantic transmission robustness, and latent separability to select reliable embedding positions. Meanwhile, a private digital token controls the random seed and guidance offset to construct positive and negative terminal latent states, enabling coverless message embedding during the final diffusion sampling step. Simulation results on open-source datasets demonstrate that SemVideoSte achieves high embedding capacity, reliable message recovery, and strong semantic consistency under different channel conditions. In addition, eavesdroppers without the correct digital token cannot reliably recover the secret message, and the generated stego videos effectively resist the steganalysis detection. We further establish a prototype testbed to verify the practical feasibility of SemVideoSte.

---


### 247. [Emergent Sparsity: How Many Effective Variables Survive Coarse-Graining in AlphaEarth Embeddings?](https://arxiv.org/abs/2610.25258)

**<font color=#1a73e8>作者：</font>** Johannes Hirn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AlphaEarth encodes each 10 m land pixel as a 64-component vector intended to support diverse global mapping tasks. Yet many scientific applications work at coarser spatial supports, for which fewer than 64 effective variables may suffice. We ask whether these vectors can be reorganized into ranked global nonlinear coordinates, how many suffice at a chosen reconstruction accuracy, and whether that number decreases with spatial scale. We thus describe effective dimension as a two-control surface over tolerance and spatial scale, rather than one intrinsic number. At each scale, a $\beta$-VAE scan with a common architecture produces a rank--distortion envelope, giving the smallest retained count achieved within the scanned family at each reconstruction tolerance. At 3% validation tolerance, this number falls from 24 to 7 when the scale is increased from 10 m to 78.9 km, whereas the corresponding PCA rank falls only from 46 to 38. Repeating the analysis on unit-norm targets preserves this trend.

---


### 248. [EasyResearch: Honest Regression, Forecasting and Signal Classification for Researchers Who Do Not Program](https://arxiv.org/abs/2610.25263)

**<font color=#1a73e8>作者：</font>** Ahmad B. A. Hassanat, Ghada A. Altarawneh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EasyClassifier showed that researchers who do not program can obtain honest classification results when the correct evaluation is the default. Most applied studies, however, predict a number, forecast a series or classify recordings, and each task has its own way of producing scores that do not hold on new data. We present EasyResearch, open-source analysis cores for regression, time-series forecasting and signal classification, and EasyResearch Desktop, a Windows application that runs these three tasks and EasyClassifier's classification without code. All four follow the same rules: everything learned from data is learned on training data only, models keep their published defaults with fixed seeds, the selected model receives a separate final score, forecasts are never evaluated on shuffled data, and every run writes a report with a Methods paragraph and the references for every method used. We measured whether the reported scores are honest by keeping part of each dataset untouched. In regression (9 public datasets, 90 runs), the common practice overstated R^2 by +2.2 points and the best comparison score by +2.5, while EasyResearch's final score was -1.0; screening predictors on all rows before cross-validation, which EasyResearch does not offer, reported R^2 = 0.27 on pure noise against -0.44 on new data. In forecasting (15 series), shuffled cross-validation over windows of past values promised errors 19% smaller than its chosen models achieved in the untouched future, while EasyResearch's final-period score was unbiased to within 1.5%; the models EasyResearch chose had 14% lower future error, and on random walks shuffled cross-validation chose a machine-learning model in 5 of 5 series, each worse in the future than repeating the last value, which EasyResearch chose 4 times. In signal classification (4 UCR datasets) one method won every comparison and neither estimate was biased.

---


### 249. [Federated Learning for Malware Image Classification under Data Heterogeneity](https://arxiv.org/abs/2610.25264)

**<font color=#1a73e8>作者：</font>** Victor Taiwo, Cemal Nisan, Muhammad Athallah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware image classification (MIC), in which binary files are converted into visual representations and deep neural networks are trained to identify malware families, has recently emerged as an effective approach for malware detection. Federated learning (FL) enables malware image classifiers to be trained collaboratively by multiple clients without sharing raw data. However, a fundamental challenge in FL is data heterogeneity (non-IID), which is particularly relevant but understudied in the malware context. In this paper, we address this gap via three contributions. First, we present an empirical study of federated MIC under varying degrees of data heterogeneity across three popular malware image datasets (MalImg, Virus-MNIST, and MalNet). We show that while FL achieves strong accuracy under IID conditions, both accuracy and training stability degrade as data becomes increasingly non-IID. Second, we introduce a set of round-level statistics that characterize the data contributed by participating clients in each FL round, and demonstrate that class entropy (diversity of class labels present in a given round) exhibits strong positive correlation with global model accuracy. Third, leveraging this insight, we propose an entropy-aware client selection strategy that filters candidate client subsets based on class entropy, and show that our strategy outperforms standard random selection. Our results highlight the role of client composition in federated MIC and underscore the importance of distribution-aware classifier training under data heterogeneity.

---


### 250. [Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion](https://arxiv.org/abs/2610.25276)

**<font color=#1a73e8>作者：</font>** Yushi Lan, Zeren Jiang, Koichi Namekata 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing a monocular video from a new camera trajectory requires preserving the observed scene geometry and motion while completing regions that become newly visible. Feed-forward 4D reconstructors recover the structure of the observed scene, whereas video diffusion models provide a generative prior for completing unseen content. We introduce Holo4D, a video reshooting framework that uses reconstructed 3D trajectories as a holistic source-view 4D scaffold. We project these trajectories into the requested views and encode their geometry and source appearance to guide a pretrained video diffusion model. Together with the source video and target cameras, the scaffold grounds generation in reconstructed observations while leaving unsupported regions to the generative prior. Experiments demonstrate the value of trajectory-based conditioning for camera control and novel-view synthesis. The framework accommodates different 4D reconstructors without retraining the video generator, allowing it to benefit from future advances in source reconstruction. More details can be found in our project page.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
