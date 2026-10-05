# 📦 其他研究 | 2026年10月06日

> 本类共 **260** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-260**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-260**

---

### 251. [Forecasting from Counterfactual Simulator Rollouts: A Sim2Real Evaluation](https://arxiv.org/abs/2610.03662)

**<font color=#1a73e8>作者：</font>** Angel Wang, Dominique Perrault-Joncas, Alvaro Maggiar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying a new decision policy creates a cold-start problem for prediction models whose targets depend on the policy's actions: historical observations reflect earlier policies, while real observations under the new policy are not yet available. Simulation offers a way to address this gap by rolling out the target policy across counterfactual scenarios and using the resulting trajectories to learn how the system responds to those controls. The simulation-to-reality (Sim2Real) transfer of this simulator-trained model can then be backtested by evaluating it against real observations from past deployments. Using two real-world inventory-control deployments, we evaluate this process from three angles: simulator fidelity, zero-shot transfer to real behavior, and adaptation as real target-policy observations accumulate. The simulator-trained forecaster achieves lower point-estimate mean absolute percentage error (MAPE) than the same architecture trained on historical real data, reducing MAPE by 1.2-3.1 percentage points in Study 1 and 12.5-18.7 points in Study 2. After deployment, lightweight calibration using early real observations further reduces error by up to 2.5 percentage points. These results provide empirical evidence that simulator-generated counterfactual data can support cold-start forecasting under a new policy, and the resulting model can be further refined as real deployment data become available.

---


### 252. [ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664)

**<font color=#1a73e8>作者：</font>** Linghui Shen, Tinghui Zhu, Sheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video models excel at causal generation, but their reliance on next-chunk prediction confines them to a short-sighted, reactive paradigm. This limitation is particularly consequential for reasoning-oriented generation, where achieving a target outcome through valid intermediate states matters more than local visual plausibility. To address this challenge, we propose Learning Prospective Reasoning with Autoregressive Video Models (ProAR), a novel framework that transforms autoregressive video generation into a goal-oriented reasoning process. ProAR introduces two key components: (1) To anchor generation to the long-range outcome, we integrate goal-frame prediction into the autoregressive loop via an asymmetric attention mask, enabling the predicted goal frame to guide the generation of intermediate states without being disrupted by them. (2) To guide short-range transitions, we introduce future representation self-alignment to encourage current hidden states to anticipate upcoming temporal dynamics. By leveraging teacher-forcing in AR training, we extract clean future representations in a single forward pass and align current representations with them using a lightweight, training-only predictor. Together, these two mechanisms seamlessly combine explicit, sparse target supervision with implicit, dense step-wise guidance, promoting coherent, goal-directed reasoning progress with modest computational cost. Experiments show that ProAR's complementary components consistently improve performance across diverse visual reasoning benchmarks. The framework proves highly training-efficient, surpassing fully trained standard AR baselines using only 25% of the training steps. This paradigm also demonstrates promising applicability to embodied reasoning tasks.

---


### 253. [Simulation-Free Learning of Population Dynamics with Wasserstein Lagrangian Residuals](https://arxiv.org/abs/2610.03679)

**<font color=#1a73e8>作者：</font>** Fedor Sergeev, Markus Heinonen, Daniel Waxman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The dynamics of cells, organisms, and fluids are often modeled as probability distributions evolving over time. Reconstructing and extrapolating this evolution from unpaired snapshots requires assumptions about the underlying process. Wasserstein gradient flows are a common choice, but they cannot describe conservative or periodic dynamics. Lagrangian mechanics in Wasserstein space covers both, but existing methods for learning it are simulation-based: they run a numerical solver at every training step, which makes training expensive. We propose Double-Stitch, a simulation-free method that learns these mechanics by penalizing the residual of the equation of motion along a learned population path. We derive this equation from a Clebsch variational principle that does not require gradient velocities, and show that the residual vanishes exactly when the equation holds. We test Double-Stitch on synthetic, single-cell and ocean vortex datasets and find that it matches or outperforms gradient-flow methods and simulation-based WLM on most tasks, while training $4$-$14$ times faster than WLM. We provide a JAX implementation of Double-Stitch at this https URL.

---


### 254. [SigLIP2 for aerial fire risk classification](https://arxiv.org/abs/2610.03689)

**<font color=#1a73e8>作者：</font>** Yunus Serhat Bıçakçı  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We examine the transfer of a pretrained SigLIP2 image encoder to seven class fire risk classification from aerial imagery. We introduce a reproducible partition of the public FireRisk training mirror and an implementation that records data provenance, preprocessing and model selection. Two initial runs compare a frozen encoder probe with full model adaptation. On the validation partition, full adaptation reaches 63.05% accuracy and 58.94% macro F1, compared with 55.95% and 50.19% for the probe. Both runs use one training seed and select their checkpoint on the same validation partition. These development results support further evaluation of SigLIP2 but do not establish performance on an independent test set or unseen regions. The accompanying code provides a common framework for repeated experiments and comparisons with additional visual encoders.

---


### 255. [Transcriptome-informed multi-modal AI for predicting neoadjuvant therapy response from breast cancer biopsies](https://arxiv.org/abs/2610.03693)

**<font color=#1a73e8>作者：</font>** Jungkyu Park, Dhruva Biswas, Joseph Cappadona 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scarcity of labeled data limits development of deep learning biomarkers in oncology. We develop a two-stage AI model predicting pathological complete response (pCR) to neoadjuvant therapy in breast cancer. The first stage learns the transcriptome from histopathology using 8,742 patients across 32 cancer types, corroborated by pathologist review and spatial agreement with measured expression. This simplifies the second stage to predicting pCR from inferred expression and clinical variables. Developed using 1,080 patients (five cohorts) and evaluated in 1,412 patients (nine cohorts), the model achieves a pooled AUROC of 0.79 (95% CI, 0.73-0.85), discriminating responders within molecular subtypes. It outperforms histopathological biomarkers, remaining stable across intratumoral sampling and with minimal biopsy tissue. Ablations show transcriptome-wide inference improves discrimination over clinical variables alone or one-stage pathology models, and robustness by avoiding genomic assays' gene selection constraints. These results indicate that biologically informed compression may generalize to data-sparse applications in precision oncology.

---


### 256. [Decoding the Functional Roles of Register and High-Norm Patch Tokens in Vision Transformers](https://arxiv.org/abs/2610.03698)

**<font color=#1a73e8>作者：</font>** Neel Varma, Andrew Rufail, Dipika Khullar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised Vision Transformers (ViTs), such as DINOv2, learn rich visual representations, but the functions of their internal tokens remain poorly understood. Recent architectures introduce dedicated register tokens to reduce high-norm out- lier patch tokens that emerge in background re- gions, yet the semantic and functional roles of both token types have not been fully established. In this paper, we analyze these roles by training sparse autoencoders (SAEs) on register-token and outlier-token activations in DINOv2. Using an automated interpretability pipeline, UMAP clus- tering, and CLIP-space cross-checks, we find that register-token features are more strongly associ- ated with high-level semantic concepts. Outlier- token features, by contrast, are more often associ- ated with lower-level structural, background, and texture-dominant patterns. Causal ablations fur- ther reveal a substantial functional asymmetry: disrupting top-activating register-derived features produces a 48.17% drop in representation cosine similarity, whereas disrupting outlier-derived fea- tures produces only a 0.31% drop. Together, our results provide evidence for token specialization in self-supervised ViTs.

---


### 257. [RNADyn: A Benchmark for Generating and Understanding RNA Dynamics](https://arxiv.org/abs/2610.03712)

**<font color=#1a73e8>作者：</font>** Yiming Huang, Lennart Bastian, Hanqun Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ribonucleic acid (RNA) functions through conformational changes that are not fully captured by static structures. However, large-scale standardized RNA dynamics data remain limited, and existing approaches typically treat trajectory generation and dynamics understanding as separate objectives. Here, we introduce RNADynBench, a standardized RNA molecular dynamics (MD) benchmark with 2585 quality-controlled 100-ns all-atom trajectories and leakage-controlled splits. Building on RNADynBench, we develop RNADynNet, a unified model for RNA dynamics learning that uses a shared backbone for both trajectory generation and dynamics fingerprint extraction from a single conformer. It combines coordinate denoising, single-frame-to-trajectory alignment, and physical grounding to connect all-atom trajectory generation with dynamics representation learning. Physical grounding improves both generated dynamics and the physical information recoverable from these fingerprints. Across both test sets, including the high-flexibility challenge set, the generated trajectories achieve RMSF correlations of 0.875 and 0.766, while single-conformer predictions show comparable agreement with MD-derived dynamics. RNADynBench and RNADynNet together establish a benchmark and unified modeling framework for generating and understanding RNA dynamics.

---


### 258. [4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes](https://arxiv.org/abs/2610.03715)

**<font color=#1a73e8>作者：</font>** Ruihong Shen, Žiga Kovačič, Peter Kulits 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce 4DCodeBench, a benchmark for 4D inverse graphics through code generation, in which agents reconstruct dynamic scenes from video as executable graphics programs. To accomplish this, agents must translate visual observations into compact representations of scene structure and dynamics, by implementing abstractions such as physical simulations to reproduce complex behavior. To evaluate this capability, we curate a set of real-world videos and construct synthetic scenes spanning diverse physical phenomena, including deformation, fluid flow, and fracture. We perform extensive benchmarking of frontier models, finding that strong static reconstruction capabilities do not yet translate into reliable reconstruction of complex dynamics. 4DCodeBench provides a testbed for tracking progress toward agents that can interpret the dynamics of the world through code. Our benchmark is available at this https URL

---


### 259. [MoSE3: Learning World-Space SE(3) at Every Pixel](https://arxiv.org/abs/2610.03716)

**<font color=#1a73e8>作者：</font>** Jiahuan Cheng, Zhiyi Li, Tian Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense 3D point tracking has been a prominent paradigm for modeling motion in dynamic scenes, but a point track is just a 3-DoF translation curve per pixel: it captures where pixels go, not the rotation of the underlying part, nor which pixels move together as one body. We propose MoSE3, the first feed-forward model that predicts dense SE(3) motion from monocular RGB video, producing full 6-DoF rigid transforms at every pixel in world space. Per-pixel SE(3) motion offers a richer view of how a scene moves: rotation, translation, and grouping all at once. Directly predicting SE(3) is challenging: rotations lie on a curved manifold that is ill-suited to Euclidean regression, and annotations for SE(3) are particularly difficult to acquire. To address these challenges, MoSE3 predicts per-pixel SE(3) through two jointly learned intermediates, 3D point tracks and rigidity embeddings, and recovers SE(3) by differentiably fitting transforms within each soft rigid cluster, enabling end-to-end prediction and supervision. To close the data gap, we introduce Art-Kubric, a large-scale synthetic dataset with dense SE(3) and rigidity labels for articulated objects with rich physical interactions. MoSE3 achieves state-of-the-art SE(3) estimation at pixel, part, and object levels on both rigid and articulated benchmarks, and state-of-the-art average 3D point tracking accuracy across three datasets, while showing strong generalization to real-world videos despite being trained solely on synthetic motion data.

---


### 260. [Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis](https://arxiv.org/abs/2610.03717)

**<font color=#1a73e8>作者：</font>** Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper examines the role of Novel View Synthesis (NVS) in geometric representation learning. In principle, NVS should reason about 3D scene structure, thereby enabling transferable multi-view geometric representations. Yet, existing encoder-based NVS methods yield poor representations. This is not because of a lack of supervisory signal, but rather due to inconspicuous architectural choices: \textit{spatially expressive decoders} that dilute representational capabilities of the scene encoder, and \textit{low-level pixel-space targets} that hinder feature learning. We present SNAP, a self-supervised encoder-decoder transformer that addresses both through a pose-conditioned local decoder and a latent-space reconstruction objective. SNAP is task agnostic, and we show that it is competitive with special-purpose geometry-supervised methods. SNAP also performs competitively against self-supervised representations across five tasks: visual localization, pose estimation, point correspondence, depth estimation, and robot manipulation. Remarkably, SNAP's patch features exhibit emergent viewpoint invariance that approaches heavily supervised models despite lower compute and data budgets. Under camera shifts where standard 2D representations collapse, SNAP degrades more gracefully, revealing that restricting decoder expressivity actively prevents the suppression of transferable geometric structure. this https URL

---


> [!TIP]
> 当前位于：**251-260**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-260**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
