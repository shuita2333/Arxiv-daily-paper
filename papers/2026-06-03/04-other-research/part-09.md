# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 401. [PaCX-MAE: Physiology-Augmented Chest X-Ray Masked Autoencoder](https://arxiv.org/abs/2606.01537)

**<font color=#1a73e8>作者：</font>** Yancheng Liu, Kenichi Maeda, Manan Pancholy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis often requires combining imaging with physiological measurements, yet deployed models typically operate on unimodal data. We present PaCX-MAE, a cross-modal distillation framework that injects physiological priors into chest X-ray (CXR) encoders while remaining strictly unimodal at inference. PaCX-MAE augments in-domain masked autoencoding with a dual contrastive-predictive objective, aligning CXR representations with paired ECG and laboratory embeddings. Extensive evaluation across nine benchmarks demonstrates consistent improvements over domain-specific MAE, particularly on physiology-dependent tasks (e.g., +2.7 AUROC on MedMod; +6.5 F1 on VinDr). The method proves highly label-efficient in the 1% regime and preserves anatomical fidelity, achieving parity with MAE on segmentation tasks. Zero-shot and attention analyses confirm that PaCX-MAE successfully learns to attend to physiological indicators, such as the cardiac silhouette, absent in standard visual pretraining.

---


### 402. [TN-SHAP-G: Graph-Structured Tensor Network Surrogates for Shapley Values and Interactions](https://arxiv.org/abs/2606.01540)

**<font color=#1a73e8>作者：</font>** Farzaneh Heidari, Guillaume Rabusseau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley values are a widely used tool for attributing importance and interactions among input variables in black-box models, but their computation involves a function defined over an exponentially large space of subsets. We propose TN-SHAP-G, a framework that exploits structure in graph-structured inputs to compute Shapley values and higher-order interaction indices efficiently. Given a predictor and a fixed masking scheme, TN-SHAP-G learns a compact, graph-aligned multilinear surrogate that approximates the masked-input behavior, represented as a tensor network whose topology mirrors the input graph. Once trained from a small number of oracle queries, the surrogate enables deterministic recovery of first- and higher-order Shapley indices via the multilinear extension, without additional model queries or Monte Carlo variance. Experiments on molecular benchmarks show that the learned factorization closely matches exact Shapley values on small graphs and scales efficiently to larger graphs where sampling-based methods become infeasible.

---


### 403. [Flexible Online Representation Learning Based on Similarity Matching](https://arxiv.org/abs/2606.01546)

**<font color=#1a73e8>作者：</font>** Shagesh Sridharan, Yanis Bahroun, Anirvan M. Sengupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse high-dimensional representations are conducive to uncovering nontrivial structures in unsupervised exploration of data. Such a representation can deal with the dense connectivity in graphs relevant to community detection problems. However, sparse high-dimensional representations are capable of doing more, including manifold tiling and feature learning. Conventional algorithms optimize in the space of computationally intractable completely positive matrices or relax the problem to the space of doubly nonnegative matrices that scale with sample size in a way rendering them impractical for large data sets. Some of these methods also impose a row sum constraint, such as double stochasticity. Row sum constraints have the added advantage of being shift-invariant, in the context of manifold tiling. Constraints on the row sum of output similarity matrices require nontrivial online learning rules. Addressing these needs, we propose a versatile online biologically plausible learning algorithm capable of learning sparse shift-invariant representations, useful for clustering, manifold tiling, or sparse coding, depending on the data structure.

---


### 404. [ForestMamba: Sparse Mamba with Geometry-guided Queries for 3D Forest Point Cloud Segmentation](https://arxiv.org/abs/2606.01549)

**<font color=#1a73e8>作者：</font>** Trung Thanh Nguyen, Tuan-Anh Vu, Duc Viet Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-based semantic and instance segmentation of terrestrial and drone LiDAR point clouds is emerging as a transformative approach for converting the complex 3D structure of forests into actionable information for forest monitoring and biodiversity assessment. However, forest LiDAR scenes remain highly challenging due to their large data volumes, irregular sampling density, overlapping and complex canopy structure, and geographic variability. Existing methods based on sparse convolutions or Transformers achieve promising results, but suffer from two key limitations: Quadratic complexity of attention scales poorly to large forest scenes, and Generic context modeling does not exploit forest structural priors, limiting tree separation in complex regions. To address these challenges, we propose ForestMamba, a structure-aware method that incorporates forest-specific priors into feature encoding, query generation, and query refinement, while replacing quadratic attention with linear-time state-space modeling. First, we introduce a sparse encoder with vertical-priority slab serialization that organizes sparse voxels into vertically coherent sequences for efficient long-range context modeling. Second, we propose a geometry-guided query initialization strategy based on an on-the-fly multi-scale Canopy Height Model (CHM), where canopy maxima provide ecologically meaningful query seeds, supplemented by Farthest Point Sampling (FPS) to cover understory trees. Third, we design a Mamba-based query decoder that combines local kNN voxel aggregation with a spatial dual-path Mamba for query refinement with linear computational complexity. Extensive experiments across seven forest regions demonstrate that ForestMamba consistently outperforms existing baselines in both segmentation tasks, while achieving 3 times faster inference and 2.3 times lower GPU memory than Transformer-based methods.

---


### 405. [Everywhere Learning: Artificial Intelligence with Pointwise Constraints](https://arxiv.org/abs/2606.01557)

**<font color=#1a73e8>作者：</font>** Ignacio Boero, Ignacio Hounie, Luiz Chamon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Everywhere learning is a new paradigm whereby Artificial Intelligence (AI) systems are trained to satisfy loss constraints with probability one over the data distribution. This is in contrast to the standard paradigm of training AI systems to minimize average losses. We develop an approximate duality theory to substantiate a generalization analysis that establishes the proximity between solutions of empirical and statistical everywhere learning problems. Our results show that dual variables reweigh the data distribution towards points in which loss constraints are more difficult to satisfy and that generalization is controlled by the mismatch between the concentration of mass of the data distribution and the concentration of mass on points where constraints are more difficult to satisfy. We further show that we can control generalization with a sparse L1 penalty on constraint relaxations. We illustrate the merits of everywhere learning with an experiment in agentic classification for language model tasks.

---


### 406. [GJDNet: Robust Graph Neural Networks via Joint Disentangled Learning Against Adversarial Attacks](https://arxiv.org/abs/2606.01560)

**<font color=#1a73e8>作者：</font>** Canyixing Cui, Tao Wu, Xingping Xian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are vulnerable to adversarial attacks, which inherently invert connectivity patterns by introducing disassortative edges in assortative graphs and assortative edges in disassortative graphs. This structural inversion creates structure-feature mismatches that disrupt neighborhood aggregation across different graph types. However, we find that existing defenses are limited, as they either treat neighborhoods as monolithic under fixed assortativity assumptions or rely on standard softmax classifiers that fail to account for perturbation-induced representation shifts. To further exploit this observation, we adopt a robustness perspective that jointly disentangles node representations and decision spaces, isolating perturbation effects while enforcing well-separated decision regions. Based on this principle, we propose Graph Joint Disentanglement Network (GJDNet), a unified framework for robust node classification across diverse graph assortativity regimes. GJDNet enhances robustness at both representation and decision levels: it employs feature-driven soft structural disentanglement with skewness-aware neighbor filtering to suppress perturbation-induced structure-feature mismatches, and introduces a Spherical Decision Boundary (SDB) to promote intra-class compactness and inter-class separation in the embedding space, thereby stabilizing decision boundaries under perturbations. Theoretical analysis provides insights into the effectiveness of the proposed disentangled representation and decision mechanisms, while extensive experiments demonstrate that GJDNet consistently achieves strong robustness across graphs with different connectivity regimes.

---


### 407. [RobustModelMaker: Coupling Bootstrap Stability Selection with Leakage-Safe Nested Cross-Validation for Scientific Machine Learning](https://arxiv.org/abs/2606.01566)

**<font color=#1a73e8>作者：</font>** Amanda S Barnard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small-to-medium scientific datasets place machine learning pipelines under two compounding pressures. Single-run feature selection produces feature sets that change substantially under small perturbations of the training data, and any procedure that uses the same data for selection, tuning, and evaluation produces optimistically biased performance estimates. The two failure modes are routinely treated as separable, but in the regimes where scientific data live, they interact: an unstable selection inflates the variance of an already-optimistic score, and standard remedies for one rarely address the other. RobustModelMaker is a Python framework that couples bootstrap stability selection with strict nested cross-validation, performs all preprocessing and selection inside each fold, and produces a stability-tested feature subset together with a leakage-safe performance estimate. The framework supports nine algorithms across binary classification, multiclass classification, and regression. Behaviour is verified by a deterministic test suite spanning unit, performance, and reproducibility checks on three real scientific datasets comparing to three alternative selectors (ANOVA F-test, recursive feature elimination with cross-validation, and Boruta) on both predictive score and a Jaccard measure of selection stability. RobustModelMaker is competitive in score with the best alternative selector on each dataset, and occupies a position on the joint score-stability frontier that none of the alternatives match across all three task types. Two example applications, ovarian cancer biomarker discovery from the PLCO Trial and critical-temperature regression on the UCI Superconductivity Data, illustrate how the framework is used in practice and what trade-offs become visible when stability is treated as a first-class deliverable rather than an emergent property.

---


### 408. [$\text{VG}^2$GT: Voxel-Gaussian Splatting Visual Geometry Grounded Transformer](https://arxiv.org/abs/2606.01573)

**<font color=#1a73e8>作者：</font>** Yibin Zhao, Yihan Pan, Jun Nan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting has shown strong potential for 3D reconstruction and novel view synthesis. However, most existing methods require accurate camera parameters and per-scene optimization, while feed-forward methods with pixel-aligned Gaussian primitives often suffer from artifacts and non-uniform primitives. In this paper, we propose $\text{VG}^2$GT, a Voxel-Gaussian Splatting Visual Geometry-Grounded Transformer. $\text{VG}^2$GT leverages a frozen pretrained visual foundation model (VFM), incorporates a multi-scale differentiable voxel module to enhance geometric understanding, and directly splits and regresses Gaussian primitive parameters from voxel features. During training, depth maps are supervised through stochastic solid volume rendering, enabling geometrically accurate Gaussian scene reconstruction while keeping the visual foundation model fully frozen. This design enables $\text{VG}^2$GT to be seamlessly plugged into any patch-feature-based VFM, while substantially reducing the required training cost. $\text{VG}^2$GT outperforms current state-of-the-art methods on widely used DTU, Replica, TAT, and ScanNet datasets.

---


### 409. [Deformable Wiener Filter for Future Video Coding](https://arxiv.org/abs/2606.01576)

**<font color=#1a73e8>作者：</font>** Xuewei Meng, Chuanmin Jia, Xinfeng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-loop filters have attracted increasing attention due to the remarkable noise-reduction capability in the hybrid video coding framework. However, the existing in-loop filters in Versatile Video Coding (VVC) mainly take advantage of the image local similarity. Although some non-local based in-loop filters can make up for this shortcoming, the widely-used unsupervised parameter estimation method by non-local filters limits the performance. In view of this, we propose a deformable Wiener Filter (DWF). It combines the local and non-local characteristics and supervisedly trains the filter coefficients based on the Wiener Filter theory. In the filtering process, local adjacent samples and non-local similar samples are first derived for each sample of interest. Then the to-be-filtered samples are classified into specific groups based on the patch level noise and sample-level characteristics. Samples in each group share the same filter coefficients. After that, the local and non-local reference samples are adaptively fused based on the classification results. Finally, the filtering operation with outlier data constraints is conducted for each to-be-filtered sample. Moreover, the performance of the proposed DWF is analyzed with different reference sample derivation schemes in detail. Simulation results show that the proposed approach achieves 1.16%, 1.92%, and 2.67% bit-rate savings on average compared to the VTM-11.0 for All Intra, Random Access, and Low-Delay B configurations, respectively.

---


### 410. [FLAME: Physics-Guided Neural Operators for Onboard Satellite Methane Detection in Hyperspectral Imagery](https://arxiv.org/abs/2606.01577)

**<font color=#1a73e8>作者：</font>** Junhyuk Heo, Junhwan Park, Sancheol Sim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methane is a major driver of near-term climate change, and rapidly identifying its emission sources is a critical climate intervention. Spaceborne hyperspectral imagery is the primary tool for this task, but the volume of data produced by each sensor makes ground-based detection impractical and necessitates onboard detection. Classical methods incur prohibitive computational cost on onboard hardware, while deep learning models are fast but fall short on detection quality. We propose FLAME, a physics-guided neural operator that builds the physics of methane absorption directly into its architecture. On the methane detection benchmark, FLAME achieves the highest detection accuracy among all evaluated methods, reduces the pixel-level false positive rate by nearly $3\times$ over the strongest neural baseline, uses the fewest parameters among learned baselines, and runs within the latency budget of onboard satellite hardware.

---


### 411. [Agent System Operations: Categorization, Challenges, and Future Directions](https://arxiv.org/abs/2606.01581)

**<font color=#1a73e8>作者：</font>** Zexin Wang, Changhua Pei, Yuanhao Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As the reasoning capabilities of Large Language Models (LLMs) continue to advance, LLM-based agent systems offer advantages in flexibility and interpretability over traditional systems, garnering increasing attention. However, despite the widespread research interest and industrial application of agent systems, these systems, like their traditional counterparts, frequently encounter anomalies. These anomalies lead to instability and insecurity, hindering their further development. Therefore, a comprehensive and systematic approach to the operation and maintenance of agent systems is urgently needed. Unfortunately, current research on the operations of agent systems is sparse. To address this gap, we have undertaken a survey on agent system operations with the aim of establishing a clear framework for the field, defining the challenges, and facilitating further development. Specifically, this paper begins by systematically defining anomalies within agent systems, categorizing them into intra-agent anomalies and inter-agent anomalies. Next, we introduce a novel and comprehensive operational framework for agent systems, dubbed Agent System Operations (AgentOps). We provide detailed definitions and explanations of its four key stages: monitoring, anomaly detection, root cause localization, and resolution.

---


### 412. [Effective Multi-sensor Conditioning for Street-view Novel-view Synthesis](https://arxiv.org/abs/2606.01590)

**<font color=#1a73e8>作者：</font>** Zhengfei Kuang, Adam Sun, Liyuan Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vehicle platforms are equipped with a rich sensor suite, including LiDAR, calibrated multi-camera rigs, and accurate ego-motion, that in principle offers strong signal for re-rendering a driving scene from novel viewpoints. A growing line of recent work leverages video diffusion models for this task, using their generative priors to synthesize plausible novel views from sparse vehicle observations. In practice, however, existing methods exploit only a fragment of this signal, and their quality tends to degrade as the target trajectory departs from the recorded driving path. We argue that this is fundamentally a multi-sensor fusion problem: sparse LiDAR reprojections supply accurate but incomplete metric geometry, surround-view reference imagery supplies dense appearance but no metric depth, and camera poses tie the two together across views. We introduce StreetNVS, a video diffusion framework that jointly conditions on all three signals through a Reference-Enhanced Camera Attention module based on a relative ray-level positional encoding. We develop a two-stage curriculum training strategy that gradually exposes the model to increasingly sparse LiDAR. On the Waymo Open Dataset, StreetNVS substantially outperforms state-of-the-art baselines under sparse LiDAR conditioning, matches methods that rely on 10-100 times denser point clouds. We further show capabilities of synthesizing coherent videos along extreme out-of-trajectory paths such as elevation, lane-shift, pullback, and rotation.
Our website: this https URL

---


### 413. [TLG: Temporal-Logic Grounding for Video Question Answering via Source-Annotation Reconstruction and Category-Targeted Reasoning](https://arxiv.org/abs/2606.01591)

**<font color=#1a73e8>作者：</font>** Ali Alavi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The TimeLogic Challenge evaluates formal temporal-logic reasoning over video - 16 operators (before, after, until, since, always, co-occur, ordering, ...) in boolean and 4-way multiple-choice form. End-to-end video-language models (VLMs) hover near chance on this task because they treat video as a bag of frames and cannot localize when actions occur. We present TLG (Temporal-Logic Grounding), a three-tier system that (i) reconstructs each video's action timeline from the public source-dataset annotations the benchmark was generated from, parses every question into a temporal-logic program, and executes it deterministically; (ii) falls back to a strong open VLM where no annotation exists; and (iii) routes only the question categories where the VLM is empirically weakest to a frontier reasoning model. TLG raises test accuracy from a 46.9% VLM baseline to 71.37%, a +24.5 absolute gain, reaching within 3 points of the leaderboard top. We report extensive ablations, including three model-based timeline-reconstruction variants that all underperform a holistic VLM, isolating temporal grounding as the irreducible bottleneck and showing that real annotations - not larger models - drive accuracy.

---


### 414. [Uncertainty-Calibrated Diffusion for Reliable 3D Molecular Graph Generation](https://arxiv.org/abs/2606.01595)

**<font color=#1a73e8>作者：</font>** Fang Wan, Jingxiang Qu, Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian inference provides a principled framework for modeling epistemic uncertainty in neural networks by treating predictions as distributions rather than deterministic values. Meanwhile, diffusion-based models for 3D molecular graph generation operate on fragile geometric structures governed by strict chemical constraints, making inference highly sensitive to uncertainty miscalibration. A largely overlooked issue is that epistemic uncertainty arising from the learned denoiser interacts with the aleatoric uncertainty intentionally injected during reverse diffusion, leading to systematic variance inflation and a mismatch between the true distribution and the simulated distribution. This effect is particularly detrimental for high-precision molecular generation, where even small deviations can violate chemical validity. In this work, we provide a theoretical and empirical analysis of how epistemic uncertainty propagates through diffusion inference and degrades sampling quality. Building on this investigation, we propose UCD (Uncertainty-Calibrated Diffusion), a simple yet effective method that calibrates the reverse diffusion process to account for epistemic uncertainty. Extensive experiments on standard 3D molecular benchmarks demonstrate that UCD consistently improves sampling quality across diverse baseline methods, establishing new state-of-the-art performance for 3D molecular diffusion. The code is available at this https URL.

---


### 415. [EIVE: End-to-End Instance-Specific Visual Explanations for Detection Transformers](https://arxiv.org/abs/2606.01601)

**<font color=#1a73e8>作者：</font>** Jianlin Xiang, Yanshan Li, Linhui Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual explainability for object detection remains challenging due to the multi-instance nature of detection. Existing approaches predominantly adopt post-hoc paradigms, such as gradient-based or perturbation-based explanation methods, to interpret pretrained detectors. However, these methods require additional gradient computation or repeated model inference, resulting in limited efficiency. To address this issue, we propose an End-to-end Instance-specific Visual Explanation framework (EIVE) that directly generates instance-level saliency maps following the forward pass of Detection Transformer (DETR)-like models. Specifically, we reformulate the cross-attention mechanism in the decoder as an instance-level feature attribution pathway, so that the cross-attention of each object query corresponds to the visual attribution of its predicted instance. Based on this formulation, we design a cross-layer hybrid consensus fusion (CLHCF) module to aggregate cross-attention signals across decoder layers, producing stable and compact explanations. The explanation process of EIVE requires neither gradient computation nor input perturbation, yielding high computational efficiency, and applies to single- and multi-scale DETR-like object detectors. Finally, we present an attention-aware joint training strategy (AAJTS) as a training-oriented application, which imposes spatial constraints on cross-attention patterns to encourage stable and concentrated attribution representations, thereby improving both interpretability and detection performance. Experiments on MS COCO 2017, ExDark, and Cityscapes demonstrate that EIVE produces high-quality instance-level saliency maps and achieves performance comparable to, or better than, state-of-the-art post-hoc methods across standard metrics, while substantially improving explanation efficiency. Code is available at this https URL.

---


### 416. [Estimating Mutual Information between Time Series and Temporal Event Sequences Across Diverse Analysis Tasks](https://arxiv.org/abs/2606.01602)

**<font color=#1a73e8>作者：</font>** Haoji Hu, Huaqing Mao, Yijun Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise dependence measures such as correlation and causality are fundamental to temporal data mining, yet there is still no principled and robust way to quantify dependence between heterogeneous data types, especially between continuous time series and discrete temporal event sequences. Existing approaches rely on ad hoc transformations or mutual-information estimators that are highly sensitive to quantization, repeated values, and event redundancy, leading to biased or unstable results in practice. We propose a nonparametric mutual information estimator that directly measures the dependence between time series and event sequences without data transformation, learning, or ad hoc discretization. Our method models the continuous-discrete duality of real-world time series to handle quantization and repeated-value artifacts and introduces a latent event clustering strategy to mitigate bias from event co-occurrence and redundancy. Together, these yield a robust and unified framework that bridges discrete and continuous mutual information. We evaluate the proposed estimator on four representative tasks: discrete-continuous time-delayed mutual information for causality analysis, global and local temporal repetition discovery, discrete covariate selection for time series forecasting, and continuous feature selection for classification. Experiments on synthetic and real-world datasets show consistent improvements over existing methods in accuracy, robustness, and interpretability, positioning our approach as a general-purpose dependence operator for heterogeneous temporal data, similar to Pearson correlation for homogeneous time series. Code available at: this https URL

---


### 417. [Paving the Way for Point Cloud Video Representation Learning Using A PDE Model](https://arxiv.org/abs/2606.01604)

**<font color=#1a73e8>作者：</font>** Zhuoxu Huang, Zhenkun Fan, Jungong Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Investigating spatial-temporal correlations, specifically how spatial points vary over time, is crucial for understanding point cloud videos. Traditional methods, particularly flow-based techniques, struggle with these correlations due to the unordered spatial arrangement of sequential point cloud data. To address this challenge, we propose a novel approach that regularizes spatial-temporal correlation learning by formulating the problem as a solvable Partial Differential Equation (PDE). While PDEs have long been effective in the physical domain, their application to novel sequential data like point cloud video remains underexplored. Inspired by fluid analysis, we construct a simplified PDE, and the process of solving PDE is guided and refined by a contrastive learning structure between the temporal embeddings and the spatial embeddings. With this extra supervision, our method, named MotionPDE, serves as an effective, plug-and-play enhancement module for existing backbone models, adding minimal computational overhead and parameters. Capitalizing on the contrastive learning process, we delve deeper into the self-supervised capabilities of MotionPDE, yielding promising results that underscore its utility and adaptability in point cloud video data interpretation. The code repo with trained checkpoints will be available at this https URL for facilitating future research.

---


### 418. [FedMTFI: Feature Importance Based Optimized Multi Teacher Knowledge Distillation in Heterogeneous Federated Learning Environment](https://arxiv.org/abs/2606.01607)

**<font color=#1a73e8>作者：</font>** Nazmus Shakib Shadin, Aaron Cummings, Xinyue Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a decentralized approach that enables collaborative model training without exposing raw data. Instead of transferring sensitive data, it allows devices to share only model weights, keeping personal data locally and secure. However, in real world settings, the data held by devices is often not evenly distributed and devices mostly differ in computing power and memory capacity. These differences make FL harder to maintain consistent performance across the system. To address these issues, we propose FedMTFI, a novel architecture that combines multi-teacher knowledge distillation (MTKD) with feature importance to improve the FL process in heterogeneous environments. In FedMTFI, clients are clustered based on similar hardware and model types. Each cluster trains a specific model on not independently and identically distributed (non-IID) data. Within a cluster, every client updates that model using only its own local private data. The server then aggregates the locally trained models in each cluster using FedAvg to form multiple prototype models. Then these prototypes serve as teacher models to train a global generalized student model using MTKD. What makes FedMTFI more unique is the integration of Shapley values (SHAP) to emphasize important features during distillation, which enhances both accuracy and interpretability. Experimental results show that FedMTFI achieves higher accuracy than traditional FL algorithms and performs more effectively under non-IID data conditions.

---


### 419. [Exploiting Semantic and Pixel Representations for Ultra-Low Bitrate Image Compression](https://arxiv.org/abs/2606.01608)

**<font color=#1a73e8>作者：</font>** Hao Wei, Yanhui Zhou, Chenyang Ge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing extreme compression methods fail to achieve an optimal rate-distortion-perception trade-off, as they typically prioritize perceptual fidelity and visual realism over pixel-level accuracy. Consequently, the resulting reconstructions often deviate noticeably from the originals. Ultra-low bitrate image compression is therefore crucial-not only for producing extremely compact representations but also for ensuring that reconstructed images remain semantically coherent and faithful to the source at the pixel level. To this end, we propose SPRDiff, a diffusion-based compression method that fully leverages both semantic and pixel representations, thereby enhancing reconstruction fidelity under ultra-low bitrate constraints. Specifically, we develop a triple-encoder architecture that utilizes high-fidelity features from the pretrained distortion-oriented and semantic-oriented encoders to compensate for the limited representations extracted by the frozen VAE encoder, thereby improving latent compression and entropy modeling. To further enhance the reconstruction fidelity of diffusion models, we introduce a distortion-aware reconstruction module with dual feature extraction. This module not only generates a coarse reconstruction that preserves the main structures, but also provides practical and accurate semantic- and pixel-level conditional signals to guide the diffusion model. Extensive experiments on benchmark datasets demonstrate that our method outperforms state-of-the-art approaches in the rate-distortion-perception tradeoff at extremely low bitrates (below 0.03 bpp), effectively preserving both perceptual quality and pixel-wise fidelity in the reconstructed images. We will release the source code and trained models at this https URL.

---


### 420. [Revisiting Ripple Effects in Knowledge Editing through Pressure-Aware Joint Neighborhood Optimization](https://arxiv.org/abs/2606.01610)

**<font color=#1a73e8>作者：</font>** Haoben Huang, Shuxin Liu, Ou Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-edit updates in large language models can trigger ripple effects across local knowledge neighborhoods: desirable propagation to related facts and unintended perturbation of preserved ones. Existing methods address these two effects separately, without explicitly modeling their coupling. We challenge this separation through an analysis of ripple responses across typical baselines, identifying two coupled design pressures: editable-side coordination and preserved-side leakage. We propose Joint Neighborhood Optimization (JNO), a new knowledge-editing framework to formalize and jointly address both pressures at the target-planning stage. JNO instantiates this principle through Pressure-Aware Coordination (PAC), which jointly optimizes neighborhood target representations under coupled constraints, and a semantic pre-execution gate that rejects high-risk target plans before parameter execution. Experiments on RippleEdits show JNO improves propagation and preservation metrics by at least 7.0% while preserving cross-backbone editing stability.

---


### 421. [Real-Time Generation of Streamable Talking Portrait Video with Reference-Guided Deep Compression VAEs](https://arxiv.org/abs/2606.01620)

**<font color=#1a73e8>作者：</font>** Sicheng Xu, Yu Deng, Shoukang Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models have significantly advanced portrait video generation, yet their high computational demands limit their use in interactive applications. This work presents a framework for streamable talking portrait video generation conditioned on speech audio and reference images. Designed meticulously for streaming scenarios, it features a causal video VAE for deep latent compression and an autoregressive latent denoising model. Our causal VAE integrates a variable number of reference images as guidance, allowing the network to focus on dynamic information rather than static appearance, thereby enhancing compression efficacy and reconstruction quality. Additionally, we extend the residual auto-encoding paradigm to improve spatial-temporal causality handling in our VAE. The generator is based on a Rectified Flow Transformer architecture and produces video latents in a blockwise auto-regressive manner. Our method enables the real-time generation of high-quality talking portrait videos, achieving speeds significantly faster than baseline models. Furthermore, comprehensive experiments demonstrate that it is on par with or even outperforms these large models in realism, vividness, and video quality.

---


### 422. [Goal2Pixel: Grounding Goals to Pixels for Vision-Language Navigation](https://arxiv.org/abs/2606.01621)

**<font color=#1a73e8>作者：</font>** Muyi Bao, Yuxin Cai, Hang Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have become a common foundation for vision-and-language navigation in continuous environments (VLN-CE). Yet most VLM-based methods cast navigation as low-level action prediction, an interface that is ambiguous, tied to short-horizon motion primitives, and inefficient due to repeated VLM querying. We propose Goal2Pixel, a pure pixel-based paradigm that reformulates VLN-CE as navigable pixel grounding. Rather than predicting actions, Goal2Pixel uses the image plane as a unified spatial interface between VLM reasoning and robot motion: the model predicts a visible navigable pixel to the agent, which is back-projected into a 3D waypoint for forward navigation. For non-forward actions, we append auxiliary directive regions to the image plane, where the left/right/bottom regions are interpreted as turning left, turning right, and stopping, respectively. To enable long-horizon navigation, we propose a visibility-aware keyframe memory for compact and informative history representation. To adapt pretrained VLMs to navigable pixel grounding, we introduce semantic embeddings and coordinate-aware auxiliary losses. Goal2Pixel achieves competitive state-of-the-art performance while requiring fewer VLM inference calls than prior methods. On R2R-CE Val-Unseen it achieves 54.1% SR and 52.5% SPL with just 7.75 VLM calls per episode, 6x fewer than the 46.62 required by direct action prediction at 32.9% SR. The same trend holds on this http URL Page: this https URL.

---


### 423. [E4GEN: Event-level Explainable Extreme-Enhanced Time-series Generation](https://arxiv.org/abs/2606.01634)

**<font color=#1a73e8>作者：</font>** Lin Jiang, Dahai Yu, Ximiao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating realistic time series is essential for scientific research and real-world applications. However, existing methods often emphasize overall distributional fidelity while failing to faithfully capture extreme events. To advance existing research, we propose E4GEN, an explainable diffusion framework for extreme event-aware time-series generation. E4GEN provides systematic insights into when, what, and how to control extreme-event generation through three key components. First, E-Activator learns the dataset-adaptive extreme-control signal activation step during the denoising process without interfering with regular temporal components, including trend and seasonality. Second, E-Predictor determines what control signal to enforce through Self-Driven Semantic Prediction, where each sample derives its own control signal by inferring latent extreme-event information during generation. It also includes a novel Data-Conditioned Training, Noise-Initiated Sampling mechanism to address the issue of unavailable training labels. Third, E-Control specifies how to control extreme-event generation through a trainable Extreme Control Network, which transforms the semantic control signal into layer-wise signals and injects it into the denoising process. We evaluate E4GEN on six datasets with 17 metrics, and extensive experiments show that E4GEN outperforms state-of-the-art models across multiple dimensions, including overall fidelity, extreme-event fidelity, and downstream utility.

---


### 424. [CanonCGT: Reference-Based Color Grading via Canonical Pivot Representation](https://arxiv.org/abs/2606.01638)

**<font color=#1a73e8>作者：</font>** Jinwon Ko, Keunsoo Ko, Chang-Su Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based color grading aims to reproduce the tonal mood and lighting of a reference while preserving color harmony and scene structure. Existing photorealistic and filter-based methods often produce unstable tone mappings -- over-shifting or inconsistently retaining colors -- leading to unnatural results. We propose CanonCGT, a two-stage framework built on a canonical pivot -- a style-neutral intermediate representation for stable color mapping. The first stage canonicalizes the input by removing intrinsic tonal bias, and the second color-grades it to match the reference style. A dual-phase training scheme, DP-CGT, combines supervised preset learning with self-supervised refinement on unpaired photographs. CanonCGT delivers photorealistic and tonally consistent results across diverse datasets, surpassing state-of-the-art methods in stability and visual fidelity. Our codes are available at \href{this https URL}{this https URL}

---


### 425. [Edge-directed geometric partitioning for versatile video coding](https://arxiv.org/abs/2606.01641)

**<font color=#1a73e8>作者：</font>** Xuewei Meng, Xinfeng Zhang, Chuanmin Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To improve the coding performance, geometric partition (GEO) was proposed for the upcoming VVC standard. GEO provides 140 partition candidates. The index of optimal GEO mode needs to be signaled explicitly. Considering different structural characteristics of different CUs and the correlation between spatial adjacent blocks and temporal collocated blocks, we propose a GEO mode prediction strategy by constructing a Most Probable Mode (MPM) list to reduce the overhead of GEO index and improve coding efficiency. Based on the observation of the high correlation between the partition mode and object boundaries, an edge-directed geometric partition scheme is proposed to construct the MPM list according to spatio-temporal edge information. The proposed method provides an objective BD-rate gain of 0.58% and 1.00% on average for RA and LDB configurations compared to VTM-6.0. Besides, it also promotes the visual quality of object boundaries.

---


### 426. [Conditional Collapse in Sign Language Production: A Diagnostic and a Scaling Argument](https://arxiv.org/abs/2606.01643)

**<font color=#1a73e8>作者：</font>** Rui Hong, Jana Košecká  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign Language Production (SLP) is the task of generating avatar sign language motion from natural language text. The quality of the generated motion is typically evaluated by a motion-space Fréchet distance (FID) and back-translation (BT) BLEU score on benchmarks such as How2Sign. Both metrics can improve substantially while the underlying generator fails to faithfully represent the sign language gestures. In this work we propose to evaluate the generated motion at three independent levels: ($\tau1$) initial-pose conditioning, ($\tau2$) output diversity, and ($\tau3$) target faithfulness. We compute these as pairwise-distance ratios using latent representations of a frozen motion autoencoder (MoAE). We evaluate 14 SLP model checkpoints on the How2Sign dataset, including a re-implemented Neural Sign Actors (NSA), and show that $\tau3$ faithfulness is never attained, while FID varies by nearly two orders of magnitude and is uncorrelated with faithfulness. We show that on the isolated gloss dataset ASL3DWord favorable $\tau3$ can be attained, hence isolating the size of the sentence-level paired-dataset as the bottleneck.

---


### 427. [PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](https://arxiv.org/abs/2606.01649)

**<font color=#1a73e8>作者：</font>** Weixing Chen, Zhuoqian Feng, Yang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating physically consistent 3D tabletop scenes is a fundamental yet underexplored problem for interactive and generalist robotic learning. The challenge stems from dense object hierarchies and irregular affordances. Here, an interactive scene denotes a physically valid, collision-free environment directly loadable into physics simulators. Existing methods, ranging from decoupled symbolic solvers to end-to-end regression models, often suffer from error propagation or overfitting to noisy supervision containing widespread physical violations. To address these limitations, we introduce PhyScene3D, a framework that reformulates generation as a Human-Mimetic Constructive Process. The proposed Cognitive Topological Reasoning Chain (CTRC) factorizes scene synthesis into a sequential, anchor-conditioned process. It employs a 3D AABB-based placement scheme that imposes a strong structural inductive bias. To address imperfect supervision and physical infeasibility, we introduce Physics-Aware Denoising Alignment (PADA). It integrates a differentiable Signed Distance Field (SDF) with Test-Time Optimization (TTO) to project generated scenes onto a physics-feasible manifold while preserving semantic intent. Experiments demonstrate that PhyScene3D outperforms state-of-the-art approaches in both semantic accuracy and physical validity, achieving a 40% reduction in scene-wise collision rate relative to the human-annotated training data.

---


### 428. [CoreUnlearn: Rethinking Concept Unlearning through Disentangled Component-Level Erasure in Text-guided Diffusion Models](https://arxiv.org/abs/2606.01658)

**<font color=#1a73e8>作者：</font>** Mengnan Zhao, Lihe Zhang, Baocai Yin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text guided diffusion models have revolutionized image synthesis but also raise ethical concerns, such as privacy violation and harmful content generation. To mitigate these issues, prevailing methods typically leverage an alignment mechanism, with predefined erasure references, to fine-tune pretrained model weights. However, these techniques are intrinsically limited by the representational capacity of textual space and display high sensitivity to the choice of predefined erasure references, e.g., suboptimal references may significantly affect the model utility preservation during erasure. To overcome these limitations, we introduce CoreUnlearn, aiming to disentangle and remove the erasure-critical component of the undesirable concept. Specifically, CoreUnlearn comprises a Component Extraction Module (CEM) and a Swap Disentangling Strategy (SDS). Guided by SDS, CEM is pre-trained to decompose concept embeddings into distinct component types. Leveraging this decomposition, CoreUnlearn then removes the erasure-critical component while retaining non-critical ones by fine-tuning model weights. Extensive experiments demonstrate that CoreUnlearn achieves effective concept erasure with minimal impact on overall model performance.

---


### 429. [Gate the Filter, Not the Message: Node-Channel Mixtures for Pre-Propagation GNNs](https://arxiv.org/abs/2606.01660)

**<font color=#1a73e8>作者：</font>** Zichao Yue, Zhiru Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-propagation graph neural networks (PPGNNs) push all graph-dependent computation into a preprocessing step and train only on the resulting dense hop features, which makes them highly scalable. A puzzle in this regime is that more complex hop aggregators do not reliably outperform simpler ones: on many benchmarks, a plain MLP-based aggregator matches or beats hop-attention variants. We revisit this behavior from a graph-filter perspective. Over a precomputed diffusion basis, existing PPGNNs differ mainly in how filter coefficients are shared across nodes and feature channels, rather than simply in raw aggregator capacity. MLP-based architectures learn channel-dependent filters that are largely shared across nodes, while hop-attention-based architectures learn node-dependent mixtures that are largely shared across channels. This reveals a missing regime in standard PPGNN designs: joint node- and channel-adaptive filtering under the pre-propagation computational contract. We propose FilterMoE, a mixture-of-experts PPGNN in which a small bank of learnable Chebyshev filter experts is routed jointly over nodes and channels by a 3D gating tensor. Across eleven homophilic and heterophilic benchmarks, FilterMoE outperforms strong PPGNN baselines on nine datasets and ranks first on all three large-scale benchmarks, improving the average test score by 1.53 points. These results establish joint node-channel filter routing as a robust alternative to dataset-specific hop-aggregator selection.

---


### 430. [Quantifying the Energy Floor: Direct Measurement and Replay Buffer Bias in SAC-Based HVAC Control on sbsim](https://arxiv.org/abs/2606.01665)

**<font color=#1a73e8>作者：</font>** Bo Li, Chen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We quantify the energy floor -- the minimum achievable cost given action space constraints -- for Soft Actor-Critic (SAC) HVAC control on the sbsim calibrated building simulator. Through minimum-action experiments, we directly measure this floor at USD 35.51/day, dominated by continuous electrical loads (USD 35.44, 99.8%) with negligible gas consumption. The standard SAC baseline, initialized with schedule-policy replay buffer transitions, converges to USD 37.18/day, 4.7% above the floor. We identify buffer initialization as the dominant source of sub-optimality in this scenario: training from an empty buffer reduces cost to USD 35.57/day, eliminating 96% of the gap. Expanding the supply water temperature range by 10 K yields negligible additional savings (USD 0.03/day), and further expansion triggers physical constraint violations. We additionally uncover a discount factor coupling (gamma_eff = 0.891) shrinking the effective planning horizon from 8.3 h to 46 min -- a benchmark-wide issue warranting audit. Systematic ablation across planning horizon, reward weights, and observation enrichment confirms all pre-filled-buffer configurations cluster within 0.7% (USD 37.18--USD 37.42), demonstrating that equipment minimum power -- not algorithmic design -- imposes the binding constraint.

---


### 431. [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672)

**<font color=#1a73e8>作者：</font>** Hojoon Lee, Ajay Subramanian, Ben Abbatematteo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has enabled the acquisition of impressive robotic skills, but typically requires hand-crafted reward functions that are slow to design and difficult to align with human intentions. Recent work, such as Eureka, automates reward design by using an LLM to iteratively generate and refine reward code from task descriptions. However, they rely on coarse feedback signals such as success rate, which provide little semantic insight into the learned behavior. As a result, their trained policies achieve the final goal but are frequently poorly aligned with task instructions. We introduce the Reward Design Agent (RDA), a VLM-based agentic framework that injects semantic understanding into reward design. RDA decomposes tasks, visually evaluates trajectories, summarizes failure modes, and iteratively revises reward code to better align with task instructions. Across 12 tabletop manipulation tasks from ManiSkill and 4 whole-body manipulation tasks from HumanoidBench, RDA produces policies substantially more instruction-aligned than those of other baselines, while achieving comparable task success rates. Videos and the generated reward code are available on this https URL.

---


### 432. [Why Do Self-Harm Prediction Models Struggle to Generalise? Lexical and Semantic Variations in Emergency Department Triage Notes](https://arxiv.org/abs/2606.01678)

**<font color=#1a73e8>作者：</font>** Liuliu Chen, Mike Conway, Jo Robinson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-harm presentations to emergency departments (EDs) are strongly associated with higher suicide risk. NLP models have shown robust performance in detecting self-harm from triage notes within single hospitals, yet performance often declines across institutions. To examine potential causes, we compare ED triage notes from two hospitals by analyzing lexical characteristics, highly associated predictive features, and salient topics. Our results reveal variation in lexical expression and feature importance related to self-harm across hospitals, despite consistent core themes such as self-poisoning and self-injury. These documentation differences are associated with reduced cross-site performance. Our findings provide insight into how institutional variation affects the identification of self-harm in clinical text and highlight potential methods to improve model generalisability.

---


### 433. [Encoded but Not Routed: Explaining the Table-Chart Gap in Scientific Claim Verification](https://arxiv.org/abs/2606.01679)

**<font color=#1a73e8>作者：</font>** Sunisth Kumar, Xanh Ho, Tim Schopf 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs are increasingly used to assist scientific peer review, where a core requirement is verifying whether claims in a paper are supported by its evidence. Prior work has shown that models perform substantially better at this task when the evidence is a table than when it is a chart of the same underlying data. This raises the question of whether models fail to extract information from charts, or do they extract it but fail to use it when forming their prediction? We study this question through layer-wise linear probing and attention analysis on three open-weight VLMs over table and chart evidence, representing the same underlying data. We find consistent evidence for the latter. Chart information is encoded in the models' intermediate representations but does not reach the prediction position, a gap that is absent for tables and holds across all conditions tested. Attention analysis further reveals that this disconnect takes two architecturally distinct forms across model families. These findings reframe the table-chart gap as a failure of how encoded visual information is routed at prediction time, rather than a failure of encoding itself.

---


### 434. [RPCASSM: Robust PCA State Space Model For Infrared Small Target Detection](https://arxiv.org/abs/2606.01689)

**<font color=#1a73e8>作者：</font>** Pingping Liu, Aohua Li, Yubing Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The detection and segmentation of infrared small targets have important application significance in the fields of surveillance and security, maritime rescue and so on. Due to the low occupancy of these targets in long-distance imaging, the mainstream visual state space model is inefficient and difficult to accurately model the target edge. The existing infrared state space models do not deviate from the mainstream visual state space structure framework from the structural properties of infrared small targets. In order to solve this problem, this paper proposes the RPCASSM network based on the model paradigm of robust principal component analysis(RPCA), which aims to design the background state space module(BSSM) and the target state space module(TSSM) by the nature of the infrared small target in the spatial domain. The BSSM aims to use the saliency of spatial heterogeneous signals to design a spatial probe scanning mechanism(SPCM) to model background information. The TSSM designs a deformable prompt scanning mechanism(DPCM) by using the sparsity and local highlight of the target to focus on the deformable space of the target for state space modeling. According to the above design, we effectively solve the problem that the existing mainstream vision state space model is difficult to accurately model the edge structure of infrared small target. Experimental results on the existing benchmark data sets prove the effectiveness of the RPCASSM design. Our code will be made public at \href{this https URL}{RPCASSM}.

---


### 435. [Understanding Identity Continuity in Thermal Video through Scene-Level Consistency](https://arxiv.org/abs/2606.01694)

**<font color=#1a73e8>作者：</font>** Wei-Chieh Sun, Gyungmin Ko, Heejae Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal pedestrian MOT remains challenging because weak appearance cues and frequent detection interruptions cause severe trajectory fragmentation. We study whether lightweight post-processing can recover identity continuity without relying on heavy re-identification models or complex online association. Starting from a YOLOv8 and SORT baseline, we add a modular identity-repair backend consisting of online short-gap remapping and offline tracklet relinking based on temporal, spatial, motion, and border cues. Controlled ablations on a fixed validation split and evaluation on the official PBVS Thermal Pedestrian MOT benchmark show that the main identity gains arise from conservative relinking, improving IDF1 from 82.25 to 84.93 while preserving MOTA, whereas many heuristic thresholds remain stable across broad operating ranges. These results suggest that, in low-information thermal imagery, robust identity recovery can be achieved more effectively through high-precision trajectory relinking than through increasing tracker complexity. These results provide a controlled analysis of identity recovery in thermal video, showing that scene-level spatial-temporal consistency plays a dominant role in identity continuity compared to local frame-to-frame association.

---


### 436. [RCEM: Embedder Equipped with Query Rewriting Skill for Robust Conversational Search in Distributional Shift](https://arxiv.org/abs/2606.01697)

**<font color=#1a73e8>作者：</font>** Kilho Son, Paul Hsu, Cha Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational search has become increasingly important in retrieval-augmented generation (RAG) systems, where users interact with AI assistants through multi-turn conversations containing context-dependent queries. We propose RCEM, a conversational dense retrieval model that distills the query reformulation capability of LLMs into the embedding model, enabling context-aware retrieval without explicit query rewriting during inference. Unlike prior conversational dense retrieval approaches that learn direct conversation-to-document matching, RCEM aligns conversational-query embeddings with rewritten-query embeddings, improving robustness under distributional shift. RCEM does not require conversational query-to-document relevance mappings for training, which are often expensive and difficult to obtain with high quality. Extensive experiments on QReCC, TopiOCQA, and TREC CAsT demonstrate that RCEM consistently outperforms strong conversational retrieval baselines, achieving particularly large gains under distributional shift, including up to 20% improvement in Recall@10. RCEM further extends the base embedding model with conversational query rewriting capability while preserving its original retrieval functionality, allowing both standalone and conversational queries to be encoded by a single model and searched against existing document indexes without rebuilding the retrieval database.

---


### 437. [Learning Label-Efficient Interpretable Medical Image Diagnosis via Semi-supervised Hypergraph Concept Bottleneck Model](https://arxiv.org/abs/2606.01698)

**<font color=#1a73e8>作者：</font>** Yijun Yang, Ruiqiang Xiao, Lijie Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has revolutionized medical image analysis, delivering exceptional diagnostic accuracy across diverse applications. Yet, the lack of interpretability in its decision-making hinders clinical adoption, particularly in high-stakes medical contexts where transparency is paramount for trustworthiness. For example, in Placenta Accreta Spectrum (PAS), subtle cues in ultrasound imaging challenge reliable diagnosis, rendering black-box models untrustworthy for accurate scoring. To address this, Concept Bottleneck Models (CBMs) offer a promising avenue by embedding clinically meaningful intermediate concepts into the diagnosis pipeline, enabling clinicians to scrutinize and refine model outputs. However, conventional CBMs falter in capturing complex inter-concept dependencies and demand costly, expert-driven concept annotations, limiting their scalability. This study introduces a novel semi-supervised CBM framework designed for medical imaging, which leverages dual-level hypergraph learning to model high-order concept dependencies and generate domain-adaptive pseudo-labels. Our approach achieves superior interpretability and performance by integrating a concept-level hypergraph for enhanced reasoning and an image-level hypergraph for robust pseudo-label generation. Experiments on a newly annotated PAS ultrasound dataset and a breast ultrasound public dataset demonstrate the effectiveness of the proposed concept label-efficient interpretable framework. Its universality is further validated on the dermoscopic image dataset SkinCon. The code is available at this https URL.

---


### 438. [MixerSENet: A Lightweight Framework for Efficient Hyperspectral Image Classification](https://arxiv.org/abs/2606.01700)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Alkhatib, Swalpa Kumar Roy, Ali Jamali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, a novel framework, MixerSENet, is introduced for hyperspectral image (HSI) classification, designed to address the challenges of computational efficiency and limited labeled data. The proposed model processes hyperspectral image patches while maintaining consistent size and resolution throughout the network, effectively decoupling the mixing of spatial and channel dimensions. Notably, MixerSENet is lightweight and computationally efficient, requiring fewer parameters compared to traditional models, making it suitable for resource-constrained environments. A squeeze and excitation block is incorporated into the model to refine feature extraction, enhancing the network's ability to capture more informative features. Experimental results on two benchmark datasets demonstrate that MixerSENet achieves superior performance, reaching an overall accuracy (OA) of 82.47% on Houston13 dataset and 96.70% on the Qingyun dataset, outperforming state-of-the-art methods including 3D-CNN, HybridKAN, HSIFormer, SimPoolFormer, and MorphMamba. Furthermore, a detailed analysis of computational efficiency shows that MixerSENet achieves a favorable balance between accuracy and efficiency, with only 53,146 parameters and an low inference time, confirming its practicality for real-world applications. At publication, source code will be publicly available at this https URL.

---


### 439. [Spatio-Temporal Correlation Guided Geometric Partitioning for Versatile Video Coding](https://arxiv.org/abs/2606.01701)

**<font color=#1a73e8>作者：</font>** Xuewei Meng, Chuanmin Jia, Xinfeng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric partitioning has attracted increasing attention by its remarkable motion field description capability in the hybrid video coding framework. However, the existing geometric partitioning (GEO) scheme in Versatile Video Coding (VVC) causes a non-negligible burden for signaling the side information. Consequently, the coding efficiency is limited. In view of this, we propose a spatio-temporal correlation guided geometric partitioning (STGEO) scheme to efficiently describe the object information in the motion field of video coding. The proposed method can economize the bits consumed for side information signaling, including the partitioning mode and motion information. We firstly analyze the characteristics of partitioning mode decision and motion vector selection in a statistically-sound way. Based on the observed spatio-temporal correlation, we design a mode prediction and coding method to reduce the overhead for representing the above mentioned side information. The main idea is to predict the STGEO modes and motion candidates that have higher selection possibilities, which can guide the entropy coding, i.e., representing the predicted high-probability modes and motion candidates with fewer bits. In particular, the high-probability STGEO modes are predicted based on the edge information and history modes of adjacent STGEO-coded blocks. The corresponding motion information is represented by the index in a merge candidate list, which is adaptively inferred based on the off-line trained merge candidate selection probability. Simulation results show that the proposed approach achieves 0.95% and 1.98% bit-rate savings on average compared to VTM-8.0 without GEO for Random Access and Low-Delay B configurations, respectively.

---


### 440. [Two-Fidelity Best-Action Identification for Stochastic Minimax Tree](https://arxiv.org/abs/2606.01708)

**<font color=#1a73e8>作者：</font>** Peter Chen, Xi Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study fixed-confidence best-action identification (BAI) in stochastic minimax trees. This problem is increasingly relevant in modern AI planning, where deep minimax search and Monte Carlo Tree Search (MCTS) with language model long rollouts face a fundamental tradeoff: heuristic evaluations are cheap but biased, while accurate rollouts are reliable but prohibitively expensive. We propose 2FFS, a two-fidelity tree-search algorithm that brings multi-fidelity flat bandit ideas into trees. The algorithm combines minimax-style fast expansion with MCTS-style stochastic sampling, adaptively deciding when to exploit cheap biased evaluations and when to invoke expensive accurate evaluations for local certification. We prove fixed-confidence correctness, establish finite stopping for exact identification, and give a polynomial-depth cost upper bound for general-depth trees. Across numerical stochastic-tree experiments, 2FFS uses substantially fewer samples and computational operations comparing to existing BAI-MCTS baseline.

---


### 441. [Fair Finetuning Mitigates Distribution Inference Attacks](https://arxiv.org/abs/2606.01719)

**<font color=#1a73e8>作者：</font>** Rakshit Naidu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models trained on sensitive data can inadvertently leak population-level information about their training distributions -- a threat known as distribution inference attack (DIA). An adversary with black-box access can infer sensitive demographic properties, such as subgroup proportions, without observing any training data directly. While defenses such as differential privacy and property unlearning have been proposed, the link between fairness constraints and distributional leakage remains unexplored. We propose Fair Fine-tuning (FFt): a trained model is fine-tuned on samples from the complementary distribution under an Equalized Odds (EO) constraint. We provide a complete theoretical characterization, proving the tight bound $\text{Adv}(\mathcal{A},M_f) \le \Delta_{\text{EO}} \cdot W$, where $W$ quantifies how distinguishable the two training distributions are by their sensitive-attribute composition. We also establish a necessary condition for FFt to reduce adversarial advantage and prove tightness of the bound. We evaluate across six datasets spanning tabular (ACS Income, COMPAS, German Credit), image (UTKFaces), and NLP (Bias in Bios) modalities. Rehearsal-based FFt consistently reduces the adversarial accuracy gap below the detection threshold $\tau!=!0.1$ across all settings; on ACS Income, the gap falls from $\sim!15%$ to under $4%$. Our work provides the first formal bound connecting a model's measured EO disparity directly to its adversarial advantage in the DIA game, opening a new avenue for unified fairness-and-privacy defenses.

---


### 442. [A Note on Stability for Orthogonalized Matrix Momentum with Client Sampling](https://arxiv.org/abs/2606.01720)

**<font color=#1a73e8>作者：</font>** Da Chang, Qiankun Shi, Lvgang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study finite-sample generalization for a client-sampled distributed optimization scheme with matrix-valued parameters and orthogonalized momentum updates. The central quantity is the gap between the population and empirical objectives at the returned model when only a subset of clients participates in each round. Under independent heterogeneous client data, unequal local sample counts, and fixed aggregation weights, we derive a finite-round upper-tail guarantee from a coupled-neighbor stability recursion and a weighted concentration step. The bound keeps the client-selection counts through the amplification factor \(Y_i(\mathcal C)\); in the uniform full-participation full-batch regime, it yields \(\widetilde{\mathcal O}(n^{-1}+n^{-1/2})\) scaling whenever the horizon-dependent amplification terms are controlled. The matrix-orthogonalization rule is required to be Lipschitz along paired trajectories, a condition satisfied by regularized polar-type maps and normalized finite-step Newton--Schulz orthogonalizers. For the unregularized matrix sign, the same argument requires coupled spectral separation, whereas Gaussian smoothing gives a finite-round smoothed variant. A one-dimensional counterexample shows why a gap, smoothing, or regularity condition is necessary.

---


### 443. [Post-Deterministic Distributed Systems: A New Foundation for Trustworthy Autonomous Infrastructure](https://arxiv.org/abs/2606.01722)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For decades, distributed systems have typically assumed that correct participants execute protocol-specified behavior with stable, externally defined, and deterministic semantics. Classical theory has extensively parameterized network timing, communication topologies, and failure domains, but this participant model has remained comparatively fixed. The integration of autonomous reasoning engines, stochastic model-driven agents, and policy-driven actors into cloud control planes, incident response systems, and financial infrastructure challenges the universality of this assumption. These agents often produce divergent reasoning paths, distinct operational traces, and heterogeneous internal representations while achieving semantically equivalent and correct outcomes. In this paper, we introduce Post-Deterministic Distributed Systems (PDDS) as a research and engineering model for coordinating heterogeneous environments where deterministic code, stochastic models, and autonomous agents coexist. We show that classical distributed computing models form a zero-ambiguity special case of this participant-general model. We do not argue that deterministic systems disappear; rather, deterministic execution can no longer serve as the universal participant assumption for autonomous infrastructure. Finally, we outline five architectural pillars of post-deterministic infrastructure: Protocol-Driven Development, Verifiable Agentic Infrastructure, Autonomous State Control Planes, Semantic Quorum Assurance, and Epistemic State Replication. Epistemic State Replication extends persistence and consistency models from data visibility to knowledge visibility, enabling agentic memory, Verifiable Semantic Rollback, and coherence across reasoning participants. We also define a taxonomy of failure classes that arise in this setting.

---


### 444. [Shortcut to Nowhere: Demystifying Deep Spurious Regression](https://arxiv.org/abs/2606.01723)

**<font color=#1a73e8>作者：</font>** Guanrong Xu, Jessica Li, Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world regression often exhibits shortcuts: attributes that are spuriously correlated with continuous targets in training, yet unreliable under deployment shifts; regressing targets using such shortcuts may fail catastrophically at test time. Existing studies on spurious correlations focus primarily on classification, where labels are categorical and groups are naturally defined. However, many real-world tasks require continuous prediction, where hard label boundaries or discrete group-label pairs do not exist. We define Deep Spurious Regression (DSR) as learning from regression data with attribute-label confounding, addressing continuous spurious correlations, and generalizing to all attribute-label combinations at test time. Motivated by the intrinsic difference between classification and regression shortcuts, we propose to exploit the similarity among spurious attributes in both label and feature spaces, thereby accounting for nearby targets and related groups while calibrating both label and learned feature distributions across attributes. Extensive experiments on common real-world DSR datasets that span computer vision, environmental sensing, and large language model (LLM) regression verify the superior performance of our strategies. Our work fills the gap in benchmarks and techniques for studying spurious correlations in continuous prediction.

---


### 445. [SECUREVENT: Hybrid AI/ML Security Monitoring for Distributed Event-Based Systems](https://arxiv.org/abs/2606.01741)

**<font color=#1a73e8>作者：</font>** Eric Liang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed event-based systems have become a common substrate for Internet-scale publish/subscribe services, IoT telemetry, cloud-native microservices, and security operations pipelines. Their loose coupling and asynchronous delivery improve scalability, but they also expand the attack surface: publishers, brokers, subscribers, topics, schemas, and temporal ordering can each be abused without a single component observing the whole behavior. This paper proposes SECUREVENT, a hybrid AI/ML security-monitoring architecture for distributed event-based systems. The architecture combines traditional protections such as authenticated transport, topic-level authorization, and signed events with online anomaly detection, graph-aware behavioral features, complex-event policy rules, federated learning, and adversarial-ML governance. A deterministic prototype study over synthetic event-stream attacks illustrates how a hybrid AI/CEP monitor can improve recall over static rules while retaining a low false-positive rate. The central claim is not that machine learning replaces cryptographic and access-control mechanisms, but that model-based security monitoring is necessary when event flows, identities, schemas, and timing relationships are too dynamic for static controls alone.

---


### 446. [Sensitivity as a Double-Edged Sword: A Trade-off Between Discriminability and Adversarial Robustness](https://arxiv.org/abs/2606.01746)

**<font color=#1a73e8>作者：</font>** Kai Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern neural networks are highly susceptible to adversarial perturbations. In this work, we identify that part of this vulnerability stems from the sensitivity of the widely used fully connected (FC) classifiers to such perturbations. In contrast, simple $\ell_2$ distance-based classifiers exhibit significantly greater robustness. We provide thorough theoretical and empirical analysis showing that while FC classifiers' high sensitivity makes them discriminative, it also makes them vulnerable. Conversely, $\ell_2$-classifiers' insensitivity grants robustness but limits performance. Motivated by this trade-off, we propose a novel $\ell_2$-reclassifier based on a Hybrid Prototype Mixing (HPM) framework. This method retains the discriminative power of FC classifiers while leveraging the robustness of $\ell_2$ distance. It yields $\ell_2$-distance-based predictions by fusing two prototype types: (1) stable, dataset-level prototypes updated via EMA, and (2) dynamic, batch-level prototypes generated from the FC classifier's predictions using a Straight-Through Estimator (STE). However, this dynamic, STE-based architecture introduces significant challenges for evaluation, such as gradient obfuscation and forward discontinuity. To address this, we propose a new, rigorous evaluation protocol, the Mixed Surrogate Attack (MSA), which uses multiple surrogates along with powerful AutoAttack to ensure a fair and robust assessment. Extensive experiments demonstrate that our lightweight, plug-and-play module, with minimal fine-tuning, effectively enhances the adversarial robustness of various existing SOTA adversarially trained models.

---


### 447. [Construction of Historical Knowledge Graphs Based on BERT and Graph Neural Networks](https://arxiv.org/abs/2606.01747)

**<font color=#1a73e8>作者：</font>** Ping Li, Bartlomiej Brzozka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Through digital humanities research and scale-up historical data analysis, a significant amount of traditional historical text is converted into structured knowledge graphs. This paper provides a high-level architecture that combines bidirectional encoder representations of transformers (BERT) and graph neural networks (GNN) to extract the entities and relationships from various types of historical texts. The texts of traditional history resolve linguistic ambiguities, references limited by context, and a lack of established grammatical norms in a systematic way. This study develops a new image retrieval system based on FastRQNet and pre-trained vision-language model Vilt-qaformer+RoBInet in accordance with the aforementioned recommendations. The experiments make full use of a comprehensive collection of municipal records, parliamentary documents, and historical correspondence. When compared to conventional rule-based techniques and other popular deep-learning baselines, the joint BERT-GNN system obtains greater Precision, Recall, and F1-score (Table 2). Complex nested structures and implicit reference issues can be handled by this structure with sufficient accuracy and thoroughness when creating knowledge graphs. The aforementioned experiments show that combining relational graph learning algorithms with context-sensitive semantic representation techniques can automatically extract historical data to add accumulated wisdom to the knowledge repository.

---


### 448. [Quality-Guided Semi-Supervised Learning for Medical Image Segmentation](https://arxiv.org/abs/2606.01753)

**<font color=#1a73e8>作者：</font>** Kumar Abhishek, Ghassan Hamarneh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training accurate medical image segmentation models requires large amounts of densely annotated data, which is costly and time-consuming to obtain. Semi-supervised learning (SSL) alleviates this by learning from both abundant unlabeled data and limited labeled data. However, most modern SSL methods rely on pseudolabels for unlabeled data, and typically assess their reliability through model confidence or uncertainty, measures that are self-referential and lack explicit grounding in segmentation quality. Instead, we propose a quality-guided SSL framework that trains a dedicated network to estimate segmentation quality from image-mask pairs. The predictor is trained on variable-quality masks generated through synthetic corruptions augmented with imperfect outputs from partially trained segmentation models, capturing realistic error patterns encountered during training. We integrate the quality predictor into SSL through two complementary mechanisms: a quality-aware regularization loss and a quality-based pseudolabel sample reweighting scheme. We show that our method serves as a drop-in enhancement to existing SSL frameworks. Extensive experiments across five datasets and multiple architectures demonstrate consistent improvements over competing SSL methods, advancing the state-of-the-art in semi-supervised medical image segmentation.

---


### 449. [PillarDETR: YOLO-Backbone and RT-DETR Head for Real-Time 3D Object Detection](https://arxiv.org/abs/2606.01757)

**<font color=#1a73e8>作者：</font>** Smit Kadvani, Shriya Gumber, Kriti Faujdar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time 3D object detection is a critical component for the safe operation of autonomous driving systems and robotics. While LiDAR point clouds provide accurate spatial information, processing them efficiently remains a significant challenge. Traditional methods rely on complex 3D convolutions or anchor-based paradigms that struggle to balance detection accuracy with inference speed. In this paper, we propose PillarDETR, a novel end-to-end 3D object detection architecture that combines the efficiency of pillar-based LiDAR encoding with the representational power of modern 2D vision models. Specifically, PillarDETR replaces standard convolutional backbones with a Cross Stage Partial (CSP) network derived from YOLOv8, enabling richer feature extraction from pseudoimages. Furthermore, we discard conventional anchor-based or center-based detection heads in favor of a Real-Time Detection Transformer (RT-DETR) decoder. This hybrid design allows the network to capture global context and directly predict 3D bounding boxes without relying on non-maximum suppression (NMS). Extensive experiments on the KITTI and nuScenes benchmarks demonstrate that PillarDETR achieves a compelling trade-off between mean Average Precision (mAP) and inference latency. Our ablation studies confirm that integrating the YOLOv8 backbone and RT-DETR head yields substantial improvements over the PointPillars baseline, establishing PillarDETR as a highly effective solution for real-time 3D perception.

---


### 450. [Structure-Guided Adaptive Propagation for Protein-Protein Interaction Site Prediction](https://arxiv.org/abs/2606.01781)

**<font color=#1a73e8>作者：</font>** Enqiang Zhu, Yizi Liu, Yilong Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of protein-protein interaction sites (PPIS) is essential for understanding cellular processes, disease mechanisms, and therapeutic target discovery. Graph-based deep learning has advanced PPIS prediction by incorporating residue-level structural context. However, most graph-based models still rely on fixed propagation schemes that treat all residues similarly, despite the structural and functional heterogeneity of protein interfaces. Such propagation may limit the ability to adapt information diffusion to local geometric environments, making it difficult to distinguish true interaction sites from structurally similar non-interacting neighbors. We present SGAP-PPIS, a structure-guided adaptive propagation model for PPIS prediction. Rather than using a fixed propagation mechanism, SGAP-PPIS leverages multi-scale geometric states from an equivariant graph neural network to generate residue-wise propagation coefficients. This design allows each residue to adaptively balance local feature preservation and neighborhood diffusion according to its geometric microenvironment. Experimental results show that SGAP-PPIS achieves competitive performance among the state-of-the-art methods on Test\_60. Ablation studies show that geometry-conditioned adaptive propagation, scale-aligned geometric guidance, and multi-step propagation-state representation jointly drive these improvements.

---


> [!TIP]
> 当前位于：**401-450**（第 9/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
