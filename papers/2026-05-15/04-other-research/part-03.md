# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 101. [GTA: Advancing Image-to-3D World Generation via Geometry Then Appearance Video Diffusion](https://arxiv.org/abs/2605.12957)

**<font color=#1a73e8>作者：</font>** Hanxin Zhu, Cong Wang, Peiyan Tu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent developments in generative models and large-scale datasets have substantially advanced 3D world generation, facilitating a broad range of domains including spatial intelligence, embodied intelligence, and autonomous driving. While achieving remarkable progress, existing approaches to 3D world generation typically prioritize appearance prediction with limited modeling of the underlying geometry, leading to issues such as unreliable scene structure estimation and degraded cross-view consistency. To address these limitations, motivated by the coarse-to-fine nature of human visual perception, we propose GTA, a novel image-to-3D world generation method following a Geometry-Then-Appearance paradigm. Specifically, given a single input image, to improve the structural fidelity of synthesized 3D scenes, GTA adopts a two-stage framework with two dedicated video diffusion models, which first generate coarse geometric structure from novel viewpoints and then synthesize fine-grained appearance conditioned on the predicted geometry. To further enhance cross-view appearance consistency, we introduce a random latent shuffle strategy during the training process, along with a test-time scaling scheme that improves perceptual quality without compromising quantitative performance. Extensive experiments have demonstrated that our proposed method consistently outperforms existing approaches in terms of fidelity, visual quality, and geometric accuracy. Moreover, GTA is shown to be effective as a general enhancement module that further improves the generation quality of existing image-to-3D world pipelines, as well as supporting multiple downstream applications and exhibiting favorable data efficiency during model training, highlighting its versatility and broad applicability. Project page: this https URL.

---


### 102. [Sustaining AI safety: Control-theoretic external impossibility, intrinsic necessity, and structural requirements](https://arxiv.org/abs/2605.12963)

**<font color=#1a73e8>作者：</font>** James M. Mazzu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems become increasingly capable, safety strategies must be evaluated not only by how much they reduce present risk, but by whether they could sustain safety once external control can no longer reliably constrain system behavior. This paper addresses that problem by using control theory to clarify, at a structural level, whether externally enforced safety-sustaining strategies can succeed and, if not, what any alternative strategy would have to satisfy in order to be viable. It establishes two main results. First, under explicit premises including a reachability condition, it proves a class-wide external impossibility result: once the system's effects exceed what bounded external control can counteract, no strategy that depends in any degree on continued external enforcement can sustain AI safety. This failure is structural across the entire externally enforced class rather than contingent on any particular strategy. Second, it establishes a conditional class-level necessity result: if at least one candidate safety-sustaining strategy remains after that elimination, then all such remaining strategies must be intrinsic. It then states four structural requirements for viability: safety may not depend on continued external enforcement; the system's terminal objective must be safety-compatible when first formed; that objective must remain stable under self-modification; and safety must continue to be preserved as capability grows. The paper does not propose a complete strategy for sustaining AI safety. Its contribution is to give formal structure to a widely held concern about the limits of external control. It does so by deriving explicit conditional results that identify which safety-sustaining strategies are ruled out and what any remaining strategies must satisfy.

---


### 103. [Asymmetric Flow Models](https://arxiv.org/abs/2605.12964)

**<font color=#1a73e8>作者：</font>** Hansheng Chen, Jan Ackermann, Minseo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-based generation in high-dimensional spaces is difficult because velocity prediction requires modeling high-dimensional noise, even when data has strong low-rank structure. We present Asymmetric Flow Modeling (AsymFlow), a rank-asymmetric velocity parameterization that restricts noise prediction to a low-rank subspace while keeping data prediction full-dimensional. From this asymmetric prediction, AsymFlow analytically recovers the full-dimensional velocity without changing the network architecture or training/sampling procedures. On ImageNet 256$\times$256, AsymFlow achieves a leading 1.57 FID, outperforming prior DiT/JiT-like pixel diffusion models by a large margin. AsymFlow also provides the first-ever route for finetuning pretrained latent flow models into pixel-space models: aligning the low-rank pixel subspace to the latent space gives a seamless initialization that preserves the latent model's high-level semantics and structure, so finetuning mainly improves low-level mismatches rather than relearning pixel generation. We show that the pixel AsymFlow model finetuned from FLUX.2 klein 9B establishes a new state of the art for pixel-space text-to-image generation, beating its latent base on HPSv3, DPG-Bench, and GenEval while qualitatively showing substantially improved visual realism.

---


### 104. [U-HNO: A U-shaped Hybrid Neural Operator with Sparse-Point Adaptive Routing for Non-stationary PDE Dynamics](https://arxiv.org/abs/2605.12965)

**<font color=#1a73e8>作者：</font>** Yingzhe Ma, Xiao Yang, Yuxin Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solutions to many partial differential equations (PDEs) display coexisting smooth global transport and localized sharp features within a single trajectory: shock fronts, thin interfaces, and concentrated high-frequency content sit on top of slowly varying backgrounds. This poses a challenge for neural operators: Fourier-based architectures mix nonlocal interactions efficiently but tend to under-resolve localized non-smooth features, whereas spatially local architectures recover fine detail at the cost of long-range propagation and rollout stability. Existing hybrid operators paper over this tension with a fixed, spatially uniform fusion that forces the same trade-off everywhere.
We propose U-HNO, a U-shaped hybrid neural operator whose central design is Sparse-Point Adaptive Routing (SPAR): at every spatial location, a per-pixel hard mask selects whether the global Fourier branch or the local multi-scale Gaussian branch should dominate, and the sparsity ratio is a function of the local contrast of the routing signal, so smooth and shock-aligned regions receive different mixtures of global and local computation. SPAR is embedded in a hierarchical encoder-bottleneck-decoder backbone with skip connections so that the dual branches and the gate operate at every resolution. Training combines pointwise supervision with a finite-difference H^1 gradient term and a band-wise spectral consistency regularizer.
Across benchmarks spanning 1D Burgers, Kuramoto-Sivashinsky, KdV, 2D advection, Allen-Cahn, Navier-Stokes, Darcy flow, and 3D transonic compressible Navier-Stokes from PDEBench, U-HNO achieves state-of-the-art rollout accuracy on the majority of tasks in both relative L^2 and H^1 metrics, with the largest gains on problems dominated by sharp localized features. Ablations show that removing any single component substantially degrades rollout error.

---


### 105. [ImageAttributionBench: How Far Are We from Generalizable Attribution?](https://arxiv.org/abs/2605.12967)

**<font color=#1a73e8>作者：</font>** Tingshu Mou, Zhipeng Wei, Chao Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative AI has enabled the creation of highly realistic and diverse synthetic images, posing critical challenges for image provenance and misinformation detection. This underscores the urgent need for effective image attribution. However, existing attribution datasets are constrained by limited scale, outdated generation methods, and insufficient semantic diversity - hindering the development of robust and generalizable attribution models. To address these limitations, we introduce ImageAttributionBench, a comprehensive dataset comprising images synthesized by a wide array of advanced generative models with state-of-the-art (SOTA) architectures. Covering multiple real-world semantic domains, the dataset offers rich diversity and scale to support and accelerate progress in image attribution research. To simulate real-world attribution scenarios, we evaluate several SOTA attribution methods on ImageAttributionBench under two challenging settings: (1) training on a standard balanced split and testing on degraded images, and (2) training and testing on semantically disjoint splits. In both cases, current methods exhibit consistently poor performance, revealing significant limitations in their robustness and generalization to unseen semantic content. Our work provides a rigorous benchmark to facilitate the development and evaluation of future image attribution methods.

---


### 106. [Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective](https://arxiv.org/abs/2605.12969)

**<font color=#1a73e8>作者：</font>** Feng Zhang, Xinhong Ma, Ziqiang Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RLVR has become a widely adopted paradigm for improving LLMs' reasoning capabilities, and GRPO is one of its most representative algorithms. In this paper, we first show that GRPO admits an equivalent discriminative reformulation as a weighted positive-negative score difference. Under this view, GRPO increases sequence-level scores of verified positive rollouts and decreases those of negative rollouts, where the scores are averages of clipped token-level importance sampling ratios. This reformulation reveals two structural limitations of GRPO: likelihood-misaligned scoring, where clipped ratio-based surrogate scores are optimized instead of generation likelihoods, and score-insensitive credit assignment, where rollout-level credit is assigned without accounting for relative score gaps between positive and negative rollouts in the same group. To address these limitations, we propose ConSPO, a framework for Contrastive Sequence-level Policy Optimization in RLVR. ConSPO replaces GRPO's clipped ratio-based scores with length-normalized sequence log-probabilities, aligning the optimized rollout scores with the likelihoods used in autoregressive generation. It then optimizes a group-wise InfoNCE-style objective that contrasts each positive rollout against negative distractors from the same group, enabling credit assignment to depend on their relative scores. This contrastive formulation amplifies updates for poorly separated positives while concentrating suppressive updates on high-scoring negatives. Moreover, ConSPO introduces a curriculum-scheduled margin, guiding optimization from coarse positive-negative ordering in early training toward stronger separation in later stages. Extensive evaluations across diverse backbone models, parameter scales, and training datasets show that ConSPO consistently outperforms several strong RLVR baselines on challenging mathematical reasoning benchmarks.

---


### 107. [CLOUDBURST: Cloud-Layer Observations Using Beacons for Unified Real-time Surveillance and Threat Attribution](https://arxiv.org/abs/2605.12976)

**<font color=#1a73e8>作者：</font>** Abraham Itzhak Weinberg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern cloud-native environments present a fundamentally different exfiltration threat surface than traditional file-based scenarios. Attackers targeting AWS, GCP, Azure, and OCI steal S3 presigned URLs, container images, Kubernetes secrets, Terraform state modules, and IAM role tokens -- artefacts that existing honeytoken and beacon frameworks do not address. We present \textbf{CLOUDBURST}, the first formal taxonomy and measurement framework for cloud-native passive beacons, comprising six vector classes across four major cloud providers.
We introduce the \textit{Cloud Attribution Score} (CAS), a four-component metric that explicitly models ephemeral infrastructure penalty ($E_p$), IAM coverage depth ($I_c$), and multi-cloud correlation bonus ($M_b$) -- dimensions absent from all prior attribution quality metrics. Experiments across $21$ deployed beacons, $205$ simulated callbacks, and three attacker sophistication levels yield four principal findings. First, IAM Canary Roles achieve the highest CAS (mean $0.450$) and Detection Resistance (DR $= 0.873$), making them the most deployable vector. Second, S3 Presigned URLs achieve the highest detection resistance (DR $= 0.890$), surviving all three cloud-native scanner models (AWS Macie, Checkov/tfsec, Prisma Cloud/Wiz). Third, ephemeral infrastructure churn degrades CAS from $\approx 0.79$ at deployment to $\approx 0.18$--$0.22$ at $48$ hours for all vectors ($p < 0.001$), establishing the first quantitative model of attribution decay in containerised environments. Fourth, Serverless Function Triggers exhibit the worst detection resistance (DR $= 0.611$) due to their explicit outbound HTTP callback pattern, motivating covert callback channel design as future work. No significant CAS difference is observed across cloud providers ($H = 1.99$, $p = 0.57$), confirming that CLOUDBURST is provider-agnostic in its effectiveness.

---


### 108. [CoRe-Gen: Robust Spectrum-to-Structure Generation under Imperfect Fingerprint Conditions](https://arxiv.org/abs/2605.12980)

**<font color=#1a73e8>作者：</font>** Tianbo Liu, Chixiang Lu, Jing Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular structure elucidation from tandem mass spectra (MS/MS) remains challenging, particularly for de novo generation beyond database coverage. A common approach decomposes the task into spectrum-to-fingerprint prediction followed by fingerprint-to-structure decoding, enabling the use of large-scale molecular corpora. However, at deployment, the decoder relies on predicted rather than oracle fingerprints, introducing structured errors that propagate into generation. This results in a fundamental condition mismatch, where models trained on clean inputs must operate under noisy, biased predictions, especially for long-tail substructures.
We present CoRe-Gen that explicitly addresses this gap. CoRe-Gen improves the intermediate condition via synthetic-spectrum pretraining of the encoder, matches deployment-time noise through frequency-aware fingerprint corruption during decoder training, and mitigates residual errors using structure-aware autoregressive decoding with compositional SELFIES representations, auxiliary structural supervision, and lightweight chemical constraints. Experiments on standard benchmarks show that CoRe-Gen establishes a new state of the art on NPLIB1, achieving 19.54\% Top-1 and 29.92\% Top-10 exact-match accuracy, while remaining competitive on the more challenging MassSpecGym benchmark. Importantly, CoRe-Gen preserves the efficiency advantages of autoregressive decoding, providing a practical and scalable solution for robust spectrum-to-structure generation under realistic conditions.

---


### 109. [Decision Tree Learning on Product Spaces](https://arxiv.org/abs/2605.12983)

**<font color=#1a73e8>作者：</font>** Arshia Soltani Moakahr, Faraz Ghahremani, Kiarash Banihashem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision tree learning has long been a central topic in theoretical computer science, driven by its practical importance. A fundamental and widely used method for decision tree construction is the top-down greedy heuristic, which recursively splits on the most influential variable. Despite its empirical success, theoretical analysis of this heuristic has been limited. A recent breakthrough by Blanc et al. (ITCS, 2020) provided the first rigorous theoretical guarantees for the greedy approach, but only under the uniform distribution. We extend this analysis to the more general and practically relevant setting of arbitrary product distributions. Our main result shows that for any function $f$ computable by an optimal decision tree of size $s$, maximum depth $D_{\text{opt}}$, and average depth $\Delta_{\text{opt}}$, the greedy heuristic constructs an $\epsilon$-approximating tree whose size grows at most with $\exp\bigl(\Delta_{\text{opt}} D_{\text{opt}} \log(e/\epsilon)\bigr)$. In the special case where the optimal tree is a full binary tree, this bound improves upon the bound of Blanc et al. and holds under a strictly broader class of distributions. Moreover, we present an algorithm based on the top-down greedy heuristic that is entirely parameter-free -- it requires no prior knowledge of the optimal tree's size or depth -- offering a practical advantage over Blanc et al.'s method.

---


### 110. [Insecure Despite Proven Updated: Extracting the Root VCEK Seed on EPYC Milan via a Software-Only Attack](https://arxiv.org/abs/2605.12990)

**<font color=#1a73e8>作者：</font>** Muyan Shen, Yu Qin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the official whitepaper of Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP), AMD explicitly emphasizes the capability to prevent Trusted Computing Base (TCB) rollback attacks. Cryptographically, this is realized by signing attestation reports with the Versioned Chip Endorsement Key (VCEK), which is derived by incorporating the TCB version into the hardware root seed.
In this architecture, safeguarding the hardware root seed is the ultimate line of defense. However, our research reveals that this protection is insufficient on EPYC Milan by presenting a software-only exploit. Specifically, we firstly introduce MilanLaunchy attack, an exploit that achieves code execution on the AMD secure processor. Building on this foundation, we develop the BadFuse attack, which extracts the hardware root seed by exploiting a lack of write restrictions in the fuse controller. This end-to-end attack chain enables an adversary to forge valid attestation reports for any firmware version, thereby effectively undermining the security model of SEV-SNP.

---


### 111. [DP-Muon: Differentially Private Optimization via Matrix-Orthogonalized Momentum](https://arxiv.org/abs/2605.12994)

**<font color=#1a73e8>作者：</font>** Jihwan Kim, Chenglin Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study differentially private (DP) training with Muon, a matrix-valued optimizer that updates hidden-layer weights using momentum followed by Newton--Schulz orthogonalization. While DP-SGD is well understood, the interaction between per-example clipping, Gaussian noise, momentum, and nonlinear orthogonalization in Muon has not been systematically analyzed. We formulate DP-Muon, a private Muon procedure that clips per-example matrix gradients, adds Gaussian noise to the clipped lot average, and then applies momentum and Newton--Schulz orthogonalization as post-processing. We prove that DP-Muon inherits the privacy guarantee certified by the corresponding same-lot subsampled Gaussian accountant, with no additional privacy cost from Muon-specific post-processing. On the optimization side, we establish finite-horizon and vanishing stationarity guarantees under per-matrix clipping, with bounds that separate optimization error, clipping residual, privacy noise, and Newton--Schulz approximation error. We further show that the DP-induced bias in Muon arises not in the linear momentum buffer itself, but after the nonlinear Newton--Schulz map, where Gaussian noise induces a matrix-valued heat-smoothing bias. This motivates DP-MuonBC, a bias-corrected variant that removes the leading output-level bias term while preserving the same privacy guarantee. Experiments on E2E and DART show that Muon-style matrix updates improve private fine-tuning, and that DP-MuonBC further improves utility without increasing the privacy budget.

---


### 112. [Frequency Bias and OOD Generalization in Neural Operators under a Variable-Coefficient Wave Equation](https://arxiv.org/abs/2605.12997)

**<font color=#1a73e8>作者：</font>** Runlong Xie, An Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators learn to map initial conditions to the terminal solution of partial differential equations (PDEs), providing a surrogate for the full operator mapping. This enables rapid prediction across different input configurations. While recent neural operator architectures have demonstrated strong performance on diverse PDE tasks, their behavior under structured distribution shifts remains insufficiently understood. To investigate this, we study operator learning in a wave propagation setting governed by a one-dimensional variable-coefficient wave equation, using two representative architectures, the Fourier Neural Operator (FNO) and the Deep Operator Network (DeepONet). To examine their generalization under distribution shifts, we consider structured out-of-distribution (OOD) settings that independently vary input frequency and coefficient smoothness. The results show that under smoothness shifts, both models maintain stable performance, with FNO achieving lower error. In contrast, under frequency shifts, FNO exhibits a sharp increase in error under unseen high-frequency inputs, whereas DeepONet shows milder degradation despite higher overall error. Our analysis reveals that these differences arise from how each architecture represents and responds to variations in frequency structure. Together, these findings highlight a fundamental gap between strong in-distribution performance and generalization under distribution shifts in operator learning, underscoring the role of architectural representation bias in developing more reliable neural operators for physics-based PDE simulations beyond the training distribution.

---


### 113. [\emph{DRIFT}: A Benchmark for Task-Free Continual Graph Learning with Continuous Distribution Shifts](https://arxiv.org/abs/2605.12998)

**<font color=#1a73e8>作者：</font>** Guiquan Sun, Xikun Zhang, Jingchao Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual graph learning (CGL) aims to learn from dynamically evolving graphs while mitigating catastrophic forgetting. Existing CGL approaches typically adopt a task-based formulation, where the data stream is partitioned into a sequence of discrete tasks with pre-defined boundaries. However, such assumptions rarely hold in real-world environments, where data distributions evolve continuously and task identity is often unavailable. To better reflect realistic non-stationary environments, we revisit continual graph learning from a task-free perspective. We propose a unified formulation that models the data stream as a time-varying mixture of latent task distributions, enabling continuous modeling of distribution drift. Based on this formulation, we construct DRIFT, a benchmark that spans a spectrum of transition dynamics ranging from hard task switches to smooth distributional drift through a Gaussian parameterization. We evaluate representative continual learning methods under this task-free setting and observe substantial performance degradation compared to traditional task-based protocols. Our findings indicate that many existing approaches implicitly rely on task boundary information and struggle under realistic task-free graph streams. This work highlights the importance of studying continual graph learning under realistic non-stationary conditions and provides a benchmark for future research in this direction. Our code is available at this https URL.

---


### 114. [Amortized Guidance for Image Inpainting with Pretrained Diffusion Models](https://arxiv.org/abs/2605.13010)

**<font color=#1a73e8>作者：</font>** Yilie Huang, Xun Yu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study image inpainting with generative diffusion models. Existing methods typically either train dedicated task-specific models, or adapt a pretrained diffusion model separately for each masked image at deployment. We introduce a middle-ground model, termed Amortized Inpainting with Diffusion (AID), which keeps a pretrained diffusion backbone fixed, trains a small reusable guidance module offline, and then reuses it across masked images without per-instance optimization. We formulate it as a deterministic guidance problem with a supervised terminal objective. To make this problem learnable in high dimensions, we derive an auxiliary Gaussian formulation and prove that solving this randomized problem recovers the optimal deterministic guidance field. This bridge yields a principled continuous-time actor--critic algorithm for learning the guidance module in a fully data-driven manner. Empirically, on AFHQv2 and FFHQ under the pixel EDM pipeline and on ImageNet under the latent EDM2 pipeline, AID consistently improves the quality--speed trade-off over strong fixed-backbone and amortized inpainting baselines across multiple mask types, while adding less than one percent trainable overhead.

---


### 115. [OCH3R: Object-Centric Holistic 3D Reconstruction](https://arxiv.org/abs/2605.13018)

**<font color=#1a73e8>作者：</font>** Yi Du, Yang You, Xiang Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric scene understanding is a fundamental challenge in computer vision. Existing approaches often rely on multi-stage pipelines that first apply pre-trained segmentors to extract individual objects, followed by per-object 3D reconstruction. Such methods are computationally expensive, fragile to segmentation errors, and scale poorly with scene complexity. We introduce OCH3R, a unified framework for Object-Centric Holistic 3D Reconstruction from a single RGB image. OCH3R performs one forward pass to simultaneously predict all object instances with their 6D poses and detailed 3D reconstructions. The key idea is a transformer architecture that predicts per-pixel attributes, including CLIP-based category embeddings, metric depth, normalized object coordinates (NOCS), and a fixed number of 3D Gaussians representing each object. To supervise these Gaussian reconstructions, we transform them into canonical space using the predicted 6D poses and align them with pre-rendered canonical ground truth, avoiding costly per-image Gaussian label generation. On standard indoor benchmarks, OCH3R achieves state-of-the-art performance across monocular depth estimation, open-vocabulary semantic segmentation, and RGB-only category-level 6D pose estimation, while producing high-fidelity, editable per-object reconstructions. Crucially, inference is fully feed-forward and scales independently of the number of objects, offering orders-of-magnitude speedups over conventional multi-stage pipelines in cluttered scenes.

---


### 116. [Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle](https://arxiv.org/abs/2605.13021)

**<font color=#1a73e8>作者：</font>** Xu Bai, Bin Lu, Kun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph coarsening is a graph dimensionality reduction technique that aims to construct a smaller and more tractable graph while preserving the essential structural and semantic properties of the original graph. However, most existing methods rely on pair-wise similarity matching, where each node independently searches for its best partner based on global information. This selfishness matching paradigm incurs substantial computational and memory overhead. To address this problem, we shift to a non-selfishness principle that prioritizes the collective interference of neighborhood in coarsening, and propose an efficient method named NOPE, which achieves linear memory consumption and near-linear computational complexity in the number of nodes. Furthermore, we derive a faster variant NOPE*, which reduces O(\delta \dot d) interference evaluation to O(d) based on the local isotropy assumption, and consequently alleviates the computational bottleneck for high-degree nodes. Experimental results show that NOPE* achieves 1.8-10\times speedup over NOPE and surpass almost all baselines with 1-3 orders of magnitude acceleration. Meanwhile, learning on coarsened graphs yields comparable performance to original graphs, and can even show superior performance over LLM-based graph reasoning owing to compact graph information. The code can be available at this https URL.

---


### 117. [Offline Two-Player Zero-Sum Markov Games with KL Regularization](https://arxiv.org/abs/2605.13025)

**<font color=#1a73e8>作者：</font>** Claire Chen, Yuheng Zhang, Xinyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning Nash equilibria in offline two-player zero-sum Markov games. While existing approaches often rely on explicit pessimism to address distribution shift, we show that KL regularization alone suffices to stabilize learning and guarantee convergence. We first introduce Regularized Offline Sequential Equilibrium (ROSE), a theoretical framework that achieves a fast $\widetilde{\mathcal{O}}(1/n)$ convergence rate under \textit{unilateral concentrability}, improving over the standard $\widetilde{\mathcal{O}}(1/\sqrt{n})$ rates in unregularized settings. We then propose Sequential Offline Self-play Mirror Descent (SOS-MD), a practical model-free algorithm based on least-squares value estimation and iterative self-play updates. We prove that the last iterate of SOS-MD attains the same $\widetilde{\mathcal{O}}(1/n)$ statistical rate up to a vanishing optimization error of order $\widetilde{\mathcal{O}}(1/\sqrt{T})$ in the number of self-play iterations $T$.

---


### 118. [PRISM: Prior Rectification and Uncertainty-Aware Structure Modeling for Diffusion-Based Text Image Super-Resolution](https://arxiv.org/abs/2605.13027)

**<font color=#1a73e8>作者：</font>** Zihang Xu, Xiaoyang Liu, Zheng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text image super-resolution (Text-SR) requires more than visually plausible detail synthesis: slight errors in stroke topology may alter character identity and break readability. Existing methods improve text fidelity with stronger recognition-based or generative priors, yet they still face two unresolved challenges under severe degradation: the text condition extracted from low-quality inputs can itself be unreliable, and a plausible global prior does not fully determine fine-grained stroke boundaries. We present PRISM, a single-step diffusion-based Text-SR framework that addresses these two challenges through Flow-Matching Prior Rectification (FMPR) and a Structure-guided Uncertainty-aware Residual Encoder (SURE). FMPR constructs a privileged training-time prior from paired low-quality/high-quality latents and learns a flow matching that transports degraded embeddings toward this restoration-oriented prior space, yielding more accurate and reliable global text guidance. SURE further predicts uncertainty-aware structural residuals to selectively absorb reliable local boundary evidence while suppressing ambiguous stroke cues. Together, these components enable explicit global prior rectification and local structure refinement within a single diffusion restoration pass. Experiments on both synthetic and real-world benchmarks show that PRISM achieves state-of-the-art performance with millisecond-level inference. Our dataset and code will be available at this https URL.

---


### 119. [FeatCal: Feature Calibration for Post-Merging Models](https://arxiv.org/abs/2605.13030)

**<font color=#1a73e8>作者：</font>** Yanggan Gu, Shuo Cai, Zihao Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines task experts into one model and avoids joint training, retraining, or deploying many expert models, but the merged model often still underperforms task experts. We study this performance gap through feature drift, the difference between features produced by the merged model and by the expert on the same input. Our theory decomposes this drift into upstream propagation and local mismatch, tracks how it propagates and combines through later layers in forward order, and links final feature drift to output drift. This view motivates FeatCal, which uses a small calibration set to calibrate the merged model weights layer by layer in forward order, reducing feature drift while staying close to merged weights and preserving the benefits of model merging. FeatCal uses an efficient closed-form solution to update model weights, with no gradient descent, iterative optimization, or extra modules. On the main CLIP and GLUE benchmarks, FeatCal beats Surgery and ProbSurgery, the closest post-merging calibration baselines: 85.5% vs. 77.0%/78.8% on CLIP-ViT-B/32 Task Arithmetic (TA) and 85.2% vs. 83.7%/82.2% on FLAN-T5-base GLUE. On CLIP-ViT-B/32, 8 examples per task reach 82.9%, and 256 examples per task take 53 seconds, about 4x faster than both baselines, showing better sample efficiency and lower calibration cost.

---


### 120. [What Information Matters? Graph Out-of-Distribution Detection via Tri-Component Information Decomposition](https://arxiv.org/abs/2605.13032)

**<font color=#1a73e8>作者：</font>** Danny Wang, Ruihong Qiu, Zi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks are widely used for node classification, but they remain vulnerable to out-of-distribution (OOD) shifts in node features and graph structure. Prior work established that methods trained with standard supervised learning (SL) objectives tend to capture spurious signals from either features and/or structure, leaving the model fragile under distributional changes. To address this, we propose textscTide, a textbfnovel and effective underlineTri-Component underlineInformation underlineDecomposition framework that textbfexplicitly decomposes information into textitfeature-specific, structure-specific and joint components. textscTide aims to textbfpreserve only the label-relevant part of the joint information while textbffiltering out spurious feature- and structure-specific information, thereby enhancing the separation between in-distribution (ID) and OOD nodes. Beyond the framework, we provide theoretical and empirical analyses showing that an information bottleneck objective is preferable to standard SL for graph OOD detection, with higher ID confidence and a greater entropy gap between ID and OOD data. Extensive experiments across seven datasets confirm the efficacy of textscTide, achieving up to a 34% improvement in FPR95 over strong baselines while maintaining competitive ID accuracy.

---


### 121. [Conveyor Parcel Routing with Order-Contiguous Arrivals](https://arxiv.org/abs/2605.13035)

**<font color=#1a73e8>作者：</font>** Takuro Kato, Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In warehouse logistics, parcels released from the outfeed of an automated storage system must be routed through conveyor networks to workstations. Beyond collision avoidance, practical operations impose an additional requirement of order-contiguous arrivals: at each delivery point, parcels belonging to the same order must arrive as a consecutive block in the arrival sequence to reduce downstream re-sorting effort. We formalize this problem as online multi-agent path finding with order-contiguity (online MAPF-OC), where agents (i.e., parcels) appear over time and exit upon delivery. To efficiently solve online MAPF-OC, we propose Dual-Ordering Prioritized Planning (DOPP), a complete polynomial-time algorithm with a three-level structure that (i) searches order-level arrival sequences, (ii) refines agent-level priorities, and (iii) synthesizes feasible solutions via prioritized planning. Experiments on various conveyor-network layouts, including those derived from actual warehouses, demonstrate DOPP's practical scalability and ability to generate high-quality plans within tight time budgets.

---


### 122. [MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning](https://arxiv.org/abs/2605.13037)

**<font color=#1a73e8>作者：</font>** Yuxin Liu, Ziang Ye, Yueqing Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current interactive LLM agents rely on goal-conditioned stepwise planning, where environmental understanding is acquired reactively during execution rather than established beforehand. This temporal inversion leads to Delayed Environmental Perception: agents must infer environmental constraints through trial-and-error, resulting in an Epistemic Bottleneck that traps them in inefficient failure cycles. Inspired by human affordance perception and cognitive map theory, we propose the Map-then-Act Paradigm (MAP), a plug-and-play framework that shifts environment understanding before execution. MAP consists of three stages: (1) Global Exploration, acquiring environment-general priors; (2) Task-Specific Mapping, constructing a structured cognitive map; and (3) Knowledge-Augmented Execution, solving tasks grounded on the map. Experiments show consistent gains across benchmarks and LLMs. On ARC-AGI-3, MAP enables frontier models to surpass near-zero baseline performance in 22 of 25 game environments. We further introduce MAP-2K, a dataset of map-then-act trajectories, and show that training on it outperforms expert execution traces, suggesting that understanding environments is more fundamental than imitation.

---


### 123. [CoGE: Sim-to-Real Online Geometric Estimation for Monocular Colonoscopy](https://arxiv.org/abs/2605.13038)

**<font color=#1a73e8>作者：</font>** Liangjing Shao, Beilei Cui, Hongliang Ren  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric estimation including depth estimation and scene reconstruction is a crucial technique for colonoscopy which can provide surgeons with 3D spatial perception and navigation. However, geometric ground truth in colonoscopy is difficult to obtain due to narrow and enclosed space of the colon, while there is a large feature gap between simulated data and realistic data caused by artifacts and illumination. In this paper, we present CoGE, a novel framework for online monocular geometric estimation during colonoscopy. Firstly, we propose an illumination-aware supervision module based on the Retinex theory to address illumination diversity in different colonoscopy scenes. Moreover, a structure-aware perception module is proposed based on wavelet decomposition to extract common structural and local features of the colon. Both quantitative and qualitative results demonstrate that the proposed model solely trained on simulated data achieves state-of-the-art performance in geometric estimation for both simulated and realistic scenes.

---


### 124. [EgoForce: Robust Online Egocentric Motion Reconstruction via Diffusion Forcing](https://arxiv.org/abs/2605.13041)

**<font color=#1a73e8>作者：</font>** Inwoo Hwang, Donggeun Lim, Hojun Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With recent advances in embodied agents and AR devices, egocentric observations are readily available as input for real-world interactive online applications. However, egocentric viewpoints can only sporadically observe hands, in addition to the estimated head trajectory. We propose EgoForce, an online framework for reconstructing long-term full-body motion from noisy egocentric input. While existing generative frameworks can robustly handle noisy and sparse measurements, they assume a fixed-length observation window is available and are thus not suitable for real-time applications. Faster inference often relies on autoregressive prediction, sacrificing robustness. In contrast, we adopt a diffusion-based method with a temporally asymmetric noise schedule inspired by Diffusion Forcing. Specifically, our approach models temporally evolving uncertainty and incrementally denoises states as new streaming observations arrive. Combined with a noise-robust imputation strategy, EgoForce progressively generates stable and coherent full-body motion under strict causal constraints. Experiments demonstrate that our online framework outperforms existing online and offline methods, enabling long-horizon, full-body motion reconstruction in challenging egocentric scenarios.

---


### 125. [No Attack Required: Semantic Fuzzing for Specification Violations in Agent Skills](https://arxiv.org/abs/2605.13044)

**<font color=#1a73e8>作者：</font>** Ying Li, Hongbo Wen, Yanju Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-powered agents can silently delete documents, leak credentials, or transfer funds on a routine user request, not because the agent was attacked, but because the skill it invoked broke its own declared safety rules. We call these specification violations: benign inputs cause a skill to breach the natural-language guardrails in its own specification, typically because the guardrail's semantics are undefined for autonomous execution, or because the implementation silently ignores the documented constraint. These violations are invisible to static analyzers, traditional fuzzers, and prompt-injection defenses alike, yet they undermine the very contract a user trusts when installing a skill.
We present Sefz, a goal-directed semantic fuzzing framework that automatically discovers specification violations in agent skills. Sefz translates each guardrail into a reachability goal over an annotated execution trace, reducing violation checking to a deterministic graph query. An LLM-based mutator generates benign inputs whose traces progressively approach the violation patterns, guided by a multi-armed bandit that uses goal-proximity as its reward signal.
On 402 real-world skills from the largest public agent-skill marketplace, Sefz finds specification violations in 120 (29.9%), including 26 previously unknown exploitable guardrail violations in deployed skills. Six recurring specification pitfalls explain the bulk of the failures, suggesting concrete principles for safer skill design.

---


### 126. [Revealing the Gap in Human and VLM Scene Perception through Counterfactual Semantic Saliency](https://arxiv.org/abs/2605.13047)

**<font color=#1a73e8>作者：</font>** Ziqi Wen, Parsa Madinei, Miguel P. Eckstein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating whether large vision-language models (VLMs) align with human perception for high-level semantic scene comprehension remains a challenge. Traditional white-box interpretability methods are inapplicable to closed-source architectures and passive metrics fail to isolate causal features. We introduce Counterfactual Semantic Saliency (CSS). This black-box, model-agnostic framework quantifies the importance of objects by measuring the semantic shift induced by their causal ablation from a scene. To evaluate AI-human semantic alignment, we tested prominent VLMs against a human psychophysics baseline comprising 16,289 valid responses across 307 complex natural scenes and 1,306 high-fidelity counterfactual variants. Our analysis reveals a pervasive scene comprehension gap: models exhibit an overreliance (relative to humans) on large objects (size bias), objects at the center of the image (center bias), and high saliency objects. In contrast, models rely less on people in the scenes than our human participants to describe the images. A model's size bias is a primary driver explaining variations in model-human semantic divergence. Code and data will be available at this https URL.

---


### 127. [Uncertainty-aware Spatial-Frequency Registration and Fusion for Infrared and Visible Images](https://arxiv.org/abs/2605.13049)

**<font color=#1a73e8>作者：</font>** Xingyuan Li, Haoyuan Xu, Xingyue Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and Visible Image Fusion (IVIF) has shown promise in visual tasks under challenging environments, but fusion under unregistered conditions faces inherent misalignments. Current studies to solve them either predict the deformation parameters coarse-to-fine (i.e., coarse registration and fine registration) or estimate the deformation fields in multi-scales for registration. Though straightforward, they overlook the cumulative errors in registration, which contaminate the fusion stage and severely deteriorate the resulting images. We introduce the Spatial-Frequency Registration and Fusion (SFRF) framework, which incorporates uncertainty estimation and infrared thermal radiation distribution consistency into a unified pipeline to handle the error accumulation for robust registration and fusion across both spatial and frequency domains. Specifically, SFRF constructs a Multi-scale Iterative Registration (MIR) framework that iteratively refines the deformation field across scales, leveraging uncertainty estimation at each stage to mitigate error accumulation and enhance alignment accuracy dynamically. To ensure the accurate alignment of infrared thermal distributions during registration, thermal radiation distribution consistency is employed as a frequency-domain supervisory signal, promoting global consistency in the frequency domain. Based on the spatial-frequency alignment, SFRF further adopts a Dual-branch Spatial-Frequency Fusion (DSFF) module, which incorporates spatial geometric features and frequency distribution information to reconstruct visually appealing images. SFRF achieves impressive performance across diverse datasets.

---


### 128. [Context Training with Active Information Seeking](https://arxiv.org/abs/2605.13050)

**<font color=#1a73e8>作者：</font>** Zeyu Huang, Adhiguna Kuncoro, Qixuan Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most existing large language models (LLMs) are expensive to adapt after deployment, especially when a task requires newly produced information or niche domain knowledge. Recent work has shown that, by manipulating and optimizing their context, LLMs can be tailored to downstream tasks without updating their weights. However, most existing methods remain closed-loop, relying solely on the model's intrinsic knowledge. In this paper, we equip these context optimizers with Wikipedia search and browser tools for active information seeking. We show that naively adding these tools to a standard sequential context optimization pipeline can actually degrade performance compared to baselines. However, when paired with a search-based training procedure that maintains and prunes multiple candidate contexts, active information seeking delivers consistent and substantial gains. We demonstrate these improvements across diverse domains, including low-resource translation (Flores+), health scenarios (HealthBench), and reasoning-heavy tasks (LiveCodeBench and Humanity's Last Exam). Furthermore, our method proves to be data-efficient, robust across different hyperparameters, and capable of generating effective textual contexts that generalize well across different models.

---


### 129. [Bridging Domain Gaps with Target-Aligned Generation for Offline Reinforcement Learning](https://arxiv.org/abs/2605.13054)

**<font color=#1a73e8>作者：</font>** Minung Kim, Jeongmo Kim, Gwanwoo Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-domain offline reinforcement learning aims to adapt a policy from a source domain to a target domain using only pre-collected datasets, where environment dynamics may differ. A key challenge is to leverage source data while reducing distributional mismatch, particularly when the target dataset is extremely limited. To address this, we propose Target-aligned Coverage Expansion (TCE), a framework that decides how source data should be used, either by directly incorporating target-near transitions or by expanding state coverage through target-aligned generation, guided by theoretical analysis. TCE builds on a dual score-based generative model to synthesize target-consistent transitions over an expanded state region. Extensive experiments across diverse cross-domain environments show that TCE consistently outperforms state-of-the-art cross-domain offline RL baselines.

---


### 130. [BrainAnytime: Anatomy-Aware Cross-Modal Pretraining for Brain Image Analysis with Arbitrary Modality Availability](https://arxiv.org/abs/2605.13059)

**<font color=#1a73e8>作者：</font>** Guangqian Yang, Tong Ding, Wenlong Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical diagnostic workups typically follow a modality escalation pathway: after initial clinical evaluation, clinicians begin with routine structural imaging (e.g., MRI), selectively add sequences such as FLAIR or T2 to refine the differential, and reserve molecular imaging (e.g., amyloid-PET) for cases that remain uncertain after standard evaluation. Consequently, patients are observed with heterogeneous and often incomplete modality subsets. However, most current AI models assume fixed data modalities as the model inputs. In this paper, we present BrainAnytime, a unified pretraining framework pretrained on 34,899 3D brain scans from five datasets that support brain image analysis under arbitrary modality availability spanning multi-sequence MRI and amyloid-PET. A single model accepts whatever imaging is available, from a lone T1 scan to a full multimodal workup. Pretraining learns structural-molecular correspondences between MRI and PET via cross-modal distillation (RCMD) and prioritizes disease-vulnerable anatomy via atlas-guided curriculum masking (PACM), all within a shared 3D masked autoencoder (Multi-MAE3D). Across four downstream tasks and five clinically motivated modality settings, BrainAnytime largely outperforms modality-specific models, missing-modality baselines, and large-scale brain MRI pretrained foundation models on most modality settings. Notably, it surpasses the strongest missing-modality baselines with relative improvements of 6.2% and 7.0% in average accuracy on CN vs. AD and CN vs. MCI classification, respectively. Code is available at this https URL.

---


### 131. [Edit-Compass & EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling](https://arxiv.org/abs/2605.13062)

**<font color=#1a73e8>作者：</font>** Xuehai Bai, Yang Shi, Yi-Fan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image editing models have achieved remarkable progress in instruction following, multimodal understanding, and complex visual editing. However, existing benchmarks often fail to faithfully reflect human judgment, especially for strong frontier models, due to limited task difficulty and coarse-grained evaluation protocols. In parallel, reward models have become increasingly important for RL-based image editing optimization, yet existing reward model benchmarks still rely on unrealistic evaluation settings that deviate from practical RL scenarios. These limitations hinder reliable assessment of both image editing models and reward models. To address these challenges, we introduce Edit-Compass and EditReward-Compass, a unified evaluation suite for image editing and reward modeling. Edit-Compass contains 2,388 carefully annotated instances spanning six progressively challenging task categories, covering capabilities such as world knowledge reasoning, visual reasoning, and multi-image editing. Beyond broad task coverage, Edit-Compass adopts a fine-grained multidimensional evaluation framework based on structured reasoning and carefully designed scoring rubrics. In parallel, EditReward-Compass contains 2,251 preference pairs that simulate realistic reward modeling scenarios during RL optimization.

---


### 132. [Local Inverse Geometry Can Be Amortized](https://arxiv.org/abs/2605.13068)

**<font color=#1a73e8>作者：</font>** Aaditya L. Kachhadiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear inverse problems often trade inexpensive but fragile first-order updates against curvature-aware methods such as Gauss-Newton and Levenberg-Marquardt, which obtain stronger directions by repeatedly solving Jacobian-based linearized systems. We propose a learned alternative: amortize local inverse geometry into a reusable reverse operator. Our framework learns a bidirectional surrogate, Deceptron, and deploys it through D-IPG (Deceptron Inverse-Preconditioned Gradient), an iterative solver that pulls residual-corrected measurement-space proposals back to latent space. The key mechanism is a Jacobian Composition Penalty (JCP), which trains the reverse Jacobian to act as a local left inverse of the forward Jacobian; its runtime counterpart, RJCP, measures the same inverse-consistency error along optimization trajectories. We prove that D-IPG is first-order equivalent to damped Gauss-Newton under local pseudoinverse consistency, with deviation controlled by composition error and conditioning. Across seven PDE inverse-problem benchmarks, D-IPG outperforms standard baselines, achieves 94.8% mean success across the six-problem reliability suite, and reaches comparable or better recovery quality at up to 77x lower inference-time solve cost on the main benchmarks.

---


### 133. [HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization](https://arxiv.org/abs/2605.13073)

**<font color=#1a73e8>作者：</font>** Yulei Kang, Tianze Zhu, Jian-Fang Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-the-wild 3D Gaussian Splatting remains challenging due to transient distractors and illumination-induced cross-view appearance inconsistencies. Existing methods mainly rely on image-level masking to suppress unreliable supervision, but masking alone cannot fully eliminate residual occlusions or resolve illumination-induced inconsistencies, both of which can introduce conflicting cross-view gradients. These unresolved conflicts may destabilize Gaussian optimization and lead to visible reconstruction artifacts. We propose a conflict-aware 3DGS framework that addresses this problem from both image-space supervision and gradient-level optimization. Semantic Consistency-Guided Masking learns pixel-wise consistency scores to adaptively refine prior masks and suppress unreliable supervision before gradient formation. A dual-view Conflict-Aware Gradient Harmonization strategy further reconciles view-specific gradients by mutually rotating them into an orthogonal configuration, reducing negative directional interference across views. We also introduce conflict-aware densification and pruning to stabilize Gaussian growth and remove persistently conflicting primitives. Extensive experiments on standard in-the-wild benchmarks demonstrate that our method achieves state-of-the-art rendering quality under complex transient distractors and cross-view inconsistencies.

---


### 134. [Scaling few-shot spoken word classification with generative meta-continual learning](https://arxiv.org/abs/2605.13075)

**<font color=#1a73e8>作者：</font>** Louise Beyers, Batsirayi Mupamhi Ziki, Ruan van der Merwe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Few-shot spoken word classification has largely been developed for applications where a small number of classes is considered, and so the potential of larger-scale few-shot spoken word classification remains untapped. This paper investigates the potential of a spoken word classifier to sequentially learn to distinguish between 1000 classes when it is given only five shots per class. We demonstrate that this scaling capability exists by training a model using the Generative Meta-Continual Learning (GeMCL) algorithm and comparing it to repeatedly trained or finetuned baselines. We find that GeMCL produces exceptionally stable performance, and although it does not always outperform a repeatedly fully-finetuned HuBERT model nor a frozen HuBERT model with a repeatedly trained classifier head, it produces comparable performance to the latter while adapting 2000 times faster, having been trained less than half of the data for two orders of magnitude less time.

---


### 135. [Counterfactual Reasoning for Causal Responsibility Attribution in Probabilistic Multi-Agent Systems](https://arxiv.org/abs/2605.13077)

**<font color=#1a73e8>作者：</font>** Chunyan Mu, Muhammad Najib  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Responsibility allocation -- determining the extent to which agents are accountable for outcomes -- is a fundamental challenge in the design and analysis of multi-agent systems. In this work, we model such systems as concurrent stochastic multi-player games and introduce a notion of retrospective (backward) counterfactual responsibility, which quantifies an agent's accountability for outcomes resulting from a given strategy profile. To allocate responsibility among agents, we utilise the Shapley value and formally show that this method satisfies key desirable properties, including fairness and consistency. Building on this foundation, we propose a formal framework that supports both verification and strategic reasoning in responsibility-aware multi-agent systems. Furthermore, by adopting Nash equilibrium as the solution concept, we demonstrate how to compute stable strategy profiles in which agents trade off responsibility against expected reward.

---


### 136. [Spectral Flattening Is All Muon Needs: How Orthogonalization Controls Learning Rate and Convergence](https://arxiv.org/abs/2605.13079)

**<font color=#1a73e8>作者：</font>** Tien-Phat Nguyen, Truong Nguyen, Minh-Phuc Truong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon orthogonalizes the momentum buffer before each update, replacing its singular values with ones via Newton-Schulz iterations. This simple change lets Muon tolerate far larger learning rates and converge faster than other optimizers, but why? We show that the mechanism is spectral flattening, and develop two results around it. First, we prove that Muon's maximal stable step size scales with the average singular value of the gradient rather than the largest, which bottlenecks standard gradient descent. Second, we recast Muon as a preconditioned gradient method and show, under a Kronecker-factored curvature model, that it improves the effective convergence factor, with the improvement controlled by the spectrum of the gradient covariance. Extensive experiments validate both results: Muon remains stable at learning rates that cause SGD to diverge within the first few iterations, and reaches accuracy milestones several epochs earlier even at identical step sizes. Taken together, our results offer a principled, geometric explanation for Muon's empirical success.

---


### 137. [PRA-PoE: Robust Alzheimer's Diagnosis with Arbitrary Missing Modalities](https://arxiv.org/abs/2605.13081)

**<font color=#1a73e8>作者：</font>** Guangqian Yang, Ye Du, Wenlong Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Missing modalities are prevalent in real-world Alzheimer's disease (AD) assessment and pose a significant challenge to multimodal learning, particularly when the distribution of observed modality subsets differs between training and deployment. Such missingness pattern mismatch induces a conditional representation shift across modality subsets. Existing approaches that rely on implicit imputation or modality synthesis often fail to explicitly model modality availability and uncertainty, leading to overconfident dependence on synthesized features, reduced robustness, and miscalibrated uncertainty estimates. To address these limitations, we propose PRA-PoE, an incomplete multimodal learning framework that is equipped with Prototype-anchored Representation Alignment (PRA) and an Uncertainty-aware Product of Experts (UA-PoE) fusion mechanism. First, PRA uses learnable global prototypes and availability-conditioned tokens to encode modality availability, distinguish observed from missing modalities, re-synthesize features for missing modalities, and adaptively refine observed representations to align latent spaces across modality subsets, with the goal of reducing representation shift under varying missingness patterns. Second, UA-PoE models each modality as a Gaussian expert and performs closed-form Product of Experts fusion, where experts with higher uncertainty are automatically down-weighted via lower precision, improving uncertainty reliability. We evaluate PRA-PoE under a clinically realistic protocol by training with naturally missing data and testing on all non-empty modality combinations. PRA-PoE consistently outperforms the state-of-the-art across datasets, achieving a 5.4% relative improvement in average accuracy on ADNI and a 10.9% relative gain in average F1 on OASIS-3 over the strongest baseline across all non-empty modality subsets.

---


### 138. [Does language matter for spoken word classification? A multilingual generative meta-learning approach](https://arxiv.org/abs/2605.13084)

**<font color=#1a73e8>作者：</font>** Batsirayi Mupamhi Ziki, Louise Beyers, Ruan van der Merwe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meta-learning has been shown to have better performance than supervised learning for few-shot monolingual spoken word classification. However, the meta-learning approach remains under-explored in multilingual spoken word classification. In this paper, we apply the Generative Meta-Continual Learning algorithm to spoken word classification. The generative nature of this algorithm makes it viable for use in application, and the meta-learning aspect promotes generalisation, which is crucial in a multilingual setting. We train monolingual models on English, German, French, and Catalan, a bilingual model on English and German, and a multilingual model on all four languages. We find that although the multilingual model performs best, the differences between model performance is unexpectedly low. We also find that the hours of unique data seen during training seems to be a stronger performance indicator than the number of languages included in the training data.

---


### 139. [Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition](https://arxiv.org/abs/2605.13087)

**<font color=#1a73e8>作者：</font>** Kush Juvekar, Kavya Manohar, Aditya Srinivas Menon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning multilingual ASR models like Whisper for low-resource languages often improves read speech but degrades spontaneous audio performance, a phenomenon we term studio-bias. To diagnose this mismatch, we introduce Vividh-ASR, a complexity-stratified benchmark for Hindi and Malayalam across four tiers: studio, broadcast, spontaneous, and synthetic noise. Through a controlled study of learning-rate timing and curriculum ordering, we find that early large parameter updates improve global WER by 12 absolute points, while a hard-to-easy curriculum adds gains for spontaneous speech. These findings motivate reverse multi-stage fine-tuning (R-MFT), a training recipe that enables a parameter-efficient 244M Whisper model to match or exceed conventionally fine-tuned 769M counterparts. Representational analysis via CKA and SVD reveals effective schedules concentrate adaptation in the decoder, preserving the pre-trained encoder's acoustic geometry. We release the benchmark and models.

---


### 140. [Bayesian Nonparametric Mixed-Effect ODEs with Gaussian Processes](https://arxiv.org/abs/2605.13088)

**<font color=#1a73e8>作者：</font>** Julien Martinelli, Maksim Sinelnikov, Harri Lähdesmäki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamical modelling is central to many scientific domains, including pharmacometrics, systems biology, physiology, and epidemiology. In these settings, heterogeneity is often intrinsic: different subjects or units follow related but distinct continuous-time dynamics. Classical nonlinear mixed-effects Ordinary Differential Equation (ODE) models address this by combining population-level structure with subject-specific effects, but they rely on a parametric vector field and are therefore vulnerable to structural misspecification and unmodelled mechanisms. This motivates nonparametric approaches that can retain principled uncertainty quantification, yet existing nonparametric ODE methods typically assume a single shared dynamical system rather than an explicit mixed-effect hierarchy over subject-specific dynamics. We propose MEGPODE, a Bayesian nonparametric mixed-effect ODE model in which each subject's vector field is decomposed into a shared population component and a subject-specific deviation, both endowed with Gaussian process (GP) priors. To avoid repeated ODE solves per subject during training, we combine state-space GP trajectory priors with virtual collocation observations, yielding Kalman-smoothing trajectory updates and closed-form regressions for the vector fields. Across controlled heterogeneous ODE benchmarks spanning oscillatory, biomedical systems, MEGPODE improves population-field recovery and subject-level trajectory prediction relative to strong baselines.

---


### 141. [RoSplat: Robust Feed-Forward Pixel-wise Gaussian Splatting for Varying Input Views and High-Resolution Rendering](https://arxiv.org/abs/2605.13093)

**<font color=#1a73e8>作者：</font>** Hoang Chuong Nguyen, Renjie Wu, Jose M. Alvarez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable 3D Gaussian Splatting has recently emerged as an efficient approach for novel-view synthesis, enabling feed-forward synthesis from only a few input views. However, existing pixel-wise feed-forward methods suffer from over-bright renderings when the number of input views varies during inference, as well as insufficient supervision for accurate Gaussian scale estimation, which leads to hole artifacts, particularly in high-resolution renderings. To address these issues, we identify that the over-brightness is caused by the varying number of overlapping Gaussians and propose a simple alpha normalization strategy to maintain brightness consistency across different number of input views. In addition, we introduce an auxiliary 3D sampling-based regularizer to improve Gaussian scale estimation, thereby mitigating hole artifacts in high-resolution rendering. Experiments on benchmark datasets demonstrate that our method significantly improves baseline models under varying input-view and high-resolution rendering settings.

---


### 142. [Watermarking Should Be Treated as a Monitoring Primitive](https://arxiv.org/abs/2605.13095)

**<font color=#1a73e8>作者：</font>** Toluwani Aremu, Nils Lukas, Jie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking is widely proposed for provenance, attribution, and safety monitoring in generative models, yet is typically evaluated only under adversaries who attempt to evade detection or induce false positives at the level of individual samples. We argue that watermarking should be treated as a monitoring primitive, and that internal monitoring is unavoidable given per-entity attribution keys and messages, as well as detector access. We introduce an observer-based threat model in which observers can aggregate watermark signals across outputs to infer entity-level information, showing that even zero-bit watermarking enables attribution under multi-key settings. We further show that external monitoring can emerge over time from persistent, key-dependent statistical structure, although this depends on watermark design and may be mitigated by distribution-preserving or undetectable schemes. Our findings reveal a fundamental dual-use tension between attribution and monitoring, motivating evaluation of watermarking beyond per-sample robustness to account for aggregation and observer-based capabilities.

---


### 143. [Security Incentivization: An Empirical Study of how Micropayments Impact Code Security](https://arxiv.org/abs/2605.13100)

**<font color=#1a73e8>作者：</font>** Stefan Rass, Martin Pinzger, Rainer W. Alexandrowicz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security often receives insufficient developer attention because it does not directly generate visible value, leading to underinvestment in practice. We evaluate a countermeasure by team-level incentives tied to measurable security improvements over time. Our semi-automated mechanism aggregates static analysis findings from Bearer, Detekt, and mobsfscan, computes security issue density, and rewards teams based on the relative improvement ratio across sprints, enabling repeatable, scriptable reporting at scale.
In a controlled course experiment with 84 students across 14 teams, we compared a security-incentivized condition, in which bonus points were linked to security scanner results, against a control condition with an otherwise identical grading scheme. The treatment group achieved significantly lower security issue density overall (beta regression: $\beta = -0.396, p = 0.0342$), indicating improved measurable security under incentivization. After controlling for platform, we observed a marked front-end/back-end disparity, with back-ends showing fewer issues and higher improvement ratios under incentives, highlighting heterogeneous effects across stack layers. Notably, these gains were not the byproduct of inflated code volume, as lines of code increased similarly across groups over time. The measurement pipeline and toolchain proved feasible for scripting and automation, supporting scalable adoption in practice.
Our results suggest that aligning rewards with automated security metrics can measurably improve code security and merit follow-up in professional contexts and longer development lifecycles.

---


### 144. [Margin-calibrated Classifier Guidance for Property-driven Synthesis Planning](https://arxiv.org/abs/2605.13101)

**<font color=#1a73e8>作者：</font>** Najwa Laabid, Vikas Garg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthesis planning seeks an efficient sequence of chemical reactions that produce a target molecule. Typically, a pretrained single-step (autoregressive) retrosynthesis model is repeatedly invoked to generate such a sequence. Classifier guidance can, in principle, help steer the output of single-step model toward reactions that satisfy specific constraints or accommodate chemist's preferences during inference without having to retrain the autoregressive generator. We expose the insufficiency of auxiliary classifiers trained with cross-entropy loss to override the unconditional token-level distributions learned from typical sparse single-disconnection reaction datasets. We overcome this issue with a novel method called Sequence Completion Ranking (SCR), which employs contrastive argumentation and a margin-based loss to calibrate the classifier so that it can meaningfully discriminate between continuations during decoding. We formally establish that margin-calibrated classifiers can expand the set of property-satisfying sequences reachable under guided beam search. Empirically, on USPTO-190, given chemist-specified guidance targets, SCR substantially improves multi-step solve rates from $16.8\%$ (unguided generator) to $78.4\%$ with reaction-type guidance and $95.3\%$ with Tanimoto guidance, unlocking valid routes for 33 targets ($17.4\%$) previously unsolvable with baselines. Our method also effectively closes the long-standing diversity gap between template-free and template-based methods.

---


### 145. [Flow Augmentation and Knowledge Distillation for Lightweight Face Presentation Attack Detection](https://arxiv.org/abs/2605.13108)

**<font color=#1a73e8>作者：</font>** Muhammad Shahid Jabbar, Muhammad Sohail Ibrahim, Taha Hasan Masood Siddique 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face presentation attack detection (FacePAD) remains challenging under diverse spoofing representation, including 2D print and replay, 3D mask-based spoofing, makeup-induced appearance manipulation, and physical occlusions, as well as under varying capture conditions. Motion cues are highly discriminative for FacePAD but typically require explicit optical flow estimation, which introduces substantial computational overhead and limits real-time deployment. In this work, we leverage optical flow to enhance motion representation during training while eliminating the need for flow computation at inference. We propose a dual-branch teacher model that fuses appearance cues from RGB frames with motion cues derived from colorwheel-encoded optical flow, enabling effective modeling of micro-motions and temporal consistency. To enable efficient deployment, we introduce a knowledge distillation framework that transfers motion-aware knowledge from the flow-augmented teacher to a lightweight RGB-only student via logit distillation. As a result, the student implicitly learns motion-sensitive representations without requiring explicit flow estimation or additional feature extraction blocks at inference. Extensive experiments demonstrate strong performance across multiple benchmarks, achieving 0.0% HTER on Replay-Attack and Replay-Mobile, 0.94% HTER on ROSE-Youtu, 5.65% HTER on SiW-Mv2, and 0.42% ACER on OULU-NPU. The distilled student achieves performance comparable to or better than the teacher while significantly reducing parameters and FLOPs, achieving 52 FPS on an NVIDIA Jetson Orin Nano, indicating its suitability for real-time and resource-constrained FacePAD deployment.

---


### 146. [A Multi-Agent Orchestration Framework for Venture Capital Due Diligence](https://arxiv.org/abs/2605.13110)

**<font color=#1a73e8>作者：</font>** Grigorios Alexandrou, Katerina Pramatari  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present a fully automated multi-agent framework for corporate due diligence and market analysis in venture capital. The system runs on an event-driven orchestration architecture, combining Large Language Models (LLMs) with real-time web retrieval to synthesize unstructured data into structured investment intelligence. A central technical contribution is a programmatic extraction pipeline that reverse-engineers the frontend-to-backend communication of the Greek Business Registry ($\Gamma$.this http URL.), querying dynamic endpoints to retrieve official financial filings that are then parsed using a layout-aware OCR extractor. A structural fallback mechanism explicitly flags data absence rather than generating unverified figures, directly targeting hallucination in financial contexts. All workflow artifacts are publicly available to support replication.

---


### 147. [Pyramid Forcing: Head-Aware Pyramid KV Cache Policy for High-Quality Long Video Generation](https://arxiv.org/abs/2605.13111)

**<font color=#1a73e8>作者：</font>** Jiayu Chen, Junbei Tang, Wenbiao Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation enables streaming and open-ended long video synthesis, but still suffers from long-term degradation caused by accumulated errors. Existing KVCache strategies usually apply unified historical-frame retention, implicitly assuming homogeneous historical dependencies across attention heads. We revisit historical-frame attention and reveal three distinct head types: Anchor Heads require broad long-range context, Wave Heads exhibit periodic temporal dependencies, and Veil Heads focus on initial and adjacent frames. Based on this finding, we propose Pyramid Forcing, a head-aware pyramidal KVCache framework that identifies head types offline, assigns behavior-specific cache policies, and supports heterogeneous cache lengths via efficient ragged-cache attention. Experiments on Self Forcing and Causal Forcing show that Pyramid Forcing consistently improves long-horizon generation quality on VBench-Long, increasing the 60-second Self Forcing score from 77.87 to 81.21 while enhancing motion dynamics, visual fidelity, and semantic consistency. Project: this https URL.

---


### 148. [DiffusionHijack: Supply-Chain PRNG Backdoor Attack on Diffusion Models and Quantum Random Number Defense](https://arxiv.org/abs/2605.13115)

**<font color=#1a73e8>作者：</font>** Ziyang You, Liling Zheng, Xiaoke Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Diffusion models depend on pseudo-random number generators (PRNGs) for latent noise sampling. We present DiffusionHijack, a supply-chain backdoor attack that hijacks the PRNG to deterministically control generated images. A malicious PRNG, injected via compromised packages, forces pixel-perfect reproduction of attacker-chosen content (SSIM = 1.00, N = 100 trials) on Stable Diffusion v1.4, v1.5, and SDXL -- without modifying model weights. The attack is inherently undetectable by existing model auditing and content moderation mechanisms, as it operates entirely outside the neural network computation graph. The attack remains effective under stochastic sampling (eta > 0), bypasses CLIP-based safety checkers (98-100% success), and operates independently of the user's prompt. As a countermeasure, we replace the PRNG with a quantum random number generator (QRNG), which provides information-theoretic unpredictability. Across N = 100 prompt-model combinations, QRNG defense completely neutralizes the attack, reducing output similarity to random baseline levels (SSIM < 0.20 for SD 1.x models, < 0.45 for SDXL). This work exposes a previously overlooked supply-chain vulnerability and offers a hardware-level fundamental mitigation for generative AI systems.

---


### 149. [Early Semantic Grounding in Image Editing Models for Zero-Shot Referring Image Segmentation](https://arxiv.org/abs/2605.13122)

**<font color=#1a73e8>作者：</font>** Jingxuan He, Xiyu Wang, Yunke Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing (IIE) models have recently demonstrated strong capability in modifying specific image regions according to natural language instructions, which implicitly requires identifying where an edit should be applied. This indicates that such models inherently perform language-conditioned visual semantic grounding. In this work, we investigate whether this implicit grounding can be leveraged for zero-shot referring image segmentation (RIS), a task that requires pixel-level localization of objects described by natural language expressions. Through systematic analysis, we reveal that strong foreground-background separability emerges in the internal representations of these models at the earliest denoising timestep, well before any visible image transformation occurs. Building on this insight, we propose a training-free framework that repurposes pretrained image editing models for RIS by exploiting their intermediate representations. Our approach decomposes localization into two complementary components: attention-based spatial priors that estimate where to focus, and feature-based semantic discrimination that determines what to segment. By leveraging feature-space separability, the framework produces accurate segmentation masks using only a single denoising step, without requiring full image synthesis. Extensive experiments on RefCOCO, RefCOCO+, and RefCOCOg demonstrate that our method achieves superior performance over existing zero-shot baselines.

---


### 150. [MLGIB: Multi-Label Graph Information Bottleneck for Expressive and Robust Message Passing](https://arxiv.org/abs/2605.13126)

**<font color=#1a73e8>作者：</font>** Chaokai Wu, Haofu Shi, Ningxuan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) suffer from over-squashing in deep message passing, where information from exponentially growing neighborhoods is compressed into fixed-dimensional representations. We show that this issue becomes a distinct failure mode in multi-label graphs: neighboring nodes often share only limited labels while differing across many irrelevant ones, causing predictive signals to be diluted by noisy label information. To address this challenge, we propose the Multi-Label Graph Information Bottleneck (MLGIB), which formulates multi-label message passing as constrained information transmission under irrelevant label noise. MLGIB balances expressiveness and robustness by preserving predictive label signals while suppressing irrelevant noise. Specifically, it constructs a Markovian dependence space and derives tractable variational bounds, where the lower bound maximizes mutual information with target labels and the upper bound constrains redundant source information. These bounds lead to an end-to-end label-aware message-passing architecture. Extensive experiments on multiple benchmarks demonstrate consistent improvements over existing methods, validating the effectiveness and generality of the proposed framework.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
