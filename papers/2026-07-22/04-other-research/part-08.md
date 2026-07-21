# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-386**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-386**

---

### 351. [fSRD: Fuzzy Spectral Region Decomposition -- Automated Multi Operator Koopman Representations via an Adaptive Spectral Learning Architecture](https://arxiv.org/abs/2607.17990)

**<font color=#1a73e8>作者：</font>** Charles Bokor, Mark Cary, Denise Morrey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Highly nonlinear chaotic dynamical systems remain difficult to model due to fundamental trade-offs between complexity, expressivity, and data efficiency. Modern machine learning methods achieve strong predictive performance but often rely on a-priori system knowledge or curated data with limited interpretability. Koopman operator theory offers a promising direction via linear representation in an infinite-dimensional observable space. However, many data-driven Koopman methods seek globally valid operators for which useful finite-dimensional spectral embeddings remain difficult to identify under these constraints. To overcome associated limitations, we introduce Fuzzy Spectral Region Decomposition (fSRD), a fully automated learning framework for estimating finite Koopman representation via multiple operators. The proposed method realizes a data-adaptive framework for assembling locally invariant embeddings, termed Invariant Decomposition. fSRD achieves highly accurate linear reconstructions of nonlinear systems while learning finite-dimensional representations of their induced evolution operators, bridging interpretable operator-theoretic models with expressive data-driven sequence learning. These embeddings are adaptively constructed via a global fuzzy tree model, drawing inspiration from fuzzy neural architectures to learn the induced dynamics while prioritizing parsimonious solutions. Empirical results across canonical chaotic systems (e.g., Lorenz and Duffing) and high-dimensional real-world data demonstrate strong predictive accuracy, interpretability, and robust expressivity across data-rich and data-limited regimes, highlighting the method's generality.

---


### 352. [PAMD: Structured Adaptive Distances for Bisimulation Representations in Visual Reinforcement Learning](https://arxiv.org/abs/2607.18004)

**<font color=#1a73e8>作者：</font>** Daegyeong Roh, Juho Bae, Han-Lim Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many visual reinforcement learning (RL) algorithms learn representations by matching latent distances to a behavioral distance induced by reward and transition similarity. In practice, the choice of the latent distance can strongly affect performance: using a fixed, pre-specified global norms (e.g., $\ell_p$ norms or other hand-designed metrics) may be overly restrictive to capture the behavioral distance. In contrast, unconstrained pairwise distances may admit degenerate solutions that drive the metric loss down without improving the representation. To address this gap, we introduce **PAMD: Pairwise Adaptive Mahalanobis Distance**, which parameterizes a positive-definite, pair-conditioned metric for measuring latent state similarity.
PAMD is a simple plug-in for existing bisimulation-based methods, offering a more expressive yet structured alternative to fixed, pre-specified latent distances. We empirically validate our method on visual MuJoCo continuous-control tasks, where final performance of several recent bisimulation-based RL algorithms is substantially improved when equipped with the distance we propose.

---


### 353. [SAMRI-3D: Adapting SAM2 for 3D MRI Segmentation with Global Volume Tokens](https://arxiv.org/abs/2607.18014)

**<font color=#1a73e8>作者：</font>** Zhao Wang, Wei Dai, Hongfu Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models such as Segment Anything Model 2 (SAM2) have transformed natural-image and video segmentation, and recent work has begun adapting them to medical imaging. These adaptations, however, are largely general-purpose models that treat MRI as one modality among many; large-scale, MRI-specific modelling and benchmarking remain limited, even though MRI's low soft-tissue contrast leaves many boundaries effectively invisible on individual slices. We present SAMRI-3D, a benchmark and method for 3D MRI segmentation with SAM2. The SAMRI-3D benchmark is the largest MRI-only evaluation to date - 10,392 volumes from 34 datasets (27 public, 7 in-house) spanning 12 anatomical domains and 10+ sequences, with explicit seen/unseen splits. Freezing the image encoder and fine-tuning only the lightweight decoder and memory modules raises mean Dice from 0.58 (zero-shot SAM2) to 0.76, surpassing recent SAM-based medical models (SAMed-2 0.69, Medical-SAM2 0.49, SAM-Med3D 0.37) with strong statistical significance. To target invisible boundaries, we introduce Global Volume Tokens (GVT): persistent memory tokens trained with a Truncated Signed Distance Field (TSDF) reconstruction objective that is discarded at inference (zero added cost). This full model, SAMRI-3D, attains the best accuracy (0.78) and lowest variance across all 34 datasets and, uniquely, shows no drop on 8 held-out datasets (0.79 unseen vs. 0.78 seen); per-sequence analysis confirms the TSDF objective helps most where per-slice contrast is weakest. We will release the benchmark, code, and models in this paper.

---


### 354. [FlashPDE: A Drop-in Fused Triton Operator Library for Neural PDE Solvers](https://arxiv.org/abs/2607.18020)

**<font color=#1a73e8>作者：</font>** Peiyu Zang, Bosen Xie, Ruoxiang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) solve PDEs by incorporating physical constraints into neural-network training, but large-scale problems are limited by automatic-differentiation memory overhead and inefficient execution of grid-based PDE operators. We present FlashPDE, a drop-in fused operator library for grid-based scientific machine learning. FlashPDE replaces fragmented PyTorch finite-difference execution with differentiable Triton kernels. Each operator integrates fused stencil evaluation, an analytic discrete-adjoint backward pass, and boundary-gradient correction within a unified this http URL interface. The library provides 14 differentiable PDE operators covering 17 configurations across 1D--3D elliptic, parabolic, and Navier--Stokes systems, while remaining independent of neural architectures and training strategies. Experiments on an NVIDIA A100 GPU show that FlashPDE reduces peak memory usage by up to 37.0x compared with coordinate-based automatic differentiation and reduces CUDA kernel launches by up to 3.5x compared with eager PyTorch finite-difference implementations. Across six representative PDE benchmarks, FlashPDE achieves up to 2.30x end-to-end time-to-solution speedup and up to 19.2x kernel-level acceleration while maintaining numerical agreement with PyTorch finite-difference references. FlashPDE provides a hardware-efficient execution layer that bridges differentiable PDE solvers and GPU-optimized numerical computation within the PyTorch ecosystem.

---


### 355. [L1 Augmented Attention as an Improved Vector Similarity Metric](https://arxiv.org/abs/2607.18027)

**<font color=#1a73e8>作者：</font>** Kurt Godden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaled dot product attention conflates directional alignment and vector magnitude, limiting its effectiveness as a similarity metric in Transformer models. We introduce L1 augmented attention, a simple and computationally parallelizable modification that subtracts a learned, head specific L1 distance between queries and keys from the dot product score. This hybrid similarity captures complementary geometric information. Dot product rewards directional alignment, while L1 penalizes coordinate deviations. To reduce the cost of L1 computation, we project queries and keys into low dimensional subspaces whose parameters specialize to preserve informative L1 structure. Evaluated on WikiText 2 using a compact transformer, L1 augmented attention achieves up to a 14.5% reduction in perplexity over the original transformer baseline and outperforms an RBF L2 kernel. Analysis of norm variance and learned L1 weights reveals distinct geometric roles across layers and strong head level specialization. These results demonstrate that enriching attention with L1 geometry provides a principled and effective improvement to similarity computation in modern language models, with practical benefits for both accuracy and parallel efficiency.

---


### 356. [Benchmarking NACTI Species Recognition in Long-Tailed Regimes](https://arxiv.org/abs/2607.18033)

**<font color=#1a73e8>作者：</font>** Zehua Liu, Tilo Burghardt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As with most ``in the wild'' collections of the natural world, the North America Camera Trap Images (NACTI) dataset exhibits long-tailed class imbalance, with the largest class covering over 50% of its 3.7M images. Building on the PyTorch Wildlife model, we systematically evaluate Long-Tail Recognition (LTR) methodologies to benchmark species recognition performance, including specialised loss functions and LTR-sensitive regularisation. Our optimised configuration achieves state-of-the-art 99.40% Top-1 accuracy on the NACTI test split, significantly outperforming standard baselines and previously reported top performances. To assess robustness under domain shifts (e.g., night-time captures, occlusion, motion-blur), we extend our evaluation across three independent reduced-bias test sets (including ENA-Detection, Caltech Camera Traps and Missouri Camera Traps). Across these out-of-distribution (OOD) evaluations, our LTR-enhanced model consistently demonstrates substantially stronger generalisation capabilities compared to standard cross-entropy approaches. However, qualitative and quantitative analyses underline that current LTR optimisations cannot fully overcome representational bottlenecks, resulting in catastrophic predictive breakdown for rare `Tail' classes under severe domain shift. For maximum reproducibility, all dataset splits, key code, and network weights are published with this paper at this https URL.

---


### 357. [When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry](https://arxiv.org/abs/2607.18040)

**<font color=#1a73e8>作者：</font>** Guofeng Yu, Zhiqing Guo, Dan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing image manipulation localization (IML) methods rely heavily on 2D forensic cues, such as low-level artifacts, noise traces, and semantic inconsistencies in the manipulated image. While effective in many cases, these cues become much less discriminative when manipulated regions are well blended with their surrounding context in appearance. In such cases, a manipulated region may remain locally appearance-consistent, but still violate the geometric structure of the surrounding scene. This limitation motivates us to go beyond purely 2D evidence and introduce geometric reasoning into IML. To this end, we leverage monocular reconstruction to obtain auxiliary geometric cues, including depth and surface normals. However, a key challenge lies in the fact that reconstructed geometry on manipulated images is inherently noisy and cannot be used naively. Rather than treating depth and normals as direct evidence, we estimate their reliability and exploit them selectively for localization. Based on this principle, we design a geometry-aware framework (GFrame) that fuses reliable geometric cues with RGB features and propagates them across scales to improve fine-grained localization. Extensive experiments show that the proposed method achieves excellent performance under limited budget constraints. These results indicate that reliable 3D geometry provides complementary forensic evidence beyond traditional 2D cues for IML. Related code will be released.

---


### 358. [Anticipate Before Acting: Future-State-Conditioned Vision-Language Navigation](https://arxiv.org/abs/2607.18042)

**<font color=#1a73e8>作者：</font>** Lingfeng Zhang, Zhanguang Zhang, Liheng Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end vision-language navigation (VLN) with causal vision-language models can map instructions and egocentric observations directly to actions, but standard behavior cloning supervises only the next action and does not explicitly train the policy state to be predictive of future visual outcomes. We first ask a diagnostic question: if the policy is given an expert-trajectory future image as privileged input at training and testing time, is that additional visual evidence useful for choosing the current action? (These expert-trajectory future images are unavailable at test time in real deployment, so we use this setting only as a privileged-input diagnostic.) The answer is yes; this sanity check shows that future observations can provide rich, actionable cues.
We then ask a deployable question: without accessing future images at inference, can we still benefit from future information by using a compressed future visual latent only as training supervision? We propose Future-State-Conditioned VLN (FSC-VLN), which adds a future-query token and aligns its hidden state to a frozen visual embedding $\Delta$ steps ahead via a training-only target branch that is removed after training. On R2R val-unseen, FSC-VLN improves SR/OSR/SPL over a StreamVLN-style baseline under two training-data regimes, with larger gains on long-horizon episodes; ablations further support the dual-query design (separating future and action queries).

---


### 359. [Adaptive Mamba Neural Operators](https://arxiv.org/abs/2607.18043)

**<font color=#1a73e8>作者：</font>** Zeyuan Song, Zheyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately solving partial differential equations (PDEs) on arbitrary geometries and a variety of meshes is an important task in science and engineering applications. In this paper, we propose Adaptive Mamba Neural Operators (AMO), which integrates reproducing kernels for state-space models (SSMs) rather than the kernel integral formulation of SSMs. This is achieved by constructing Takenaka-Malmquist systems for the PDEs. AMO offers new representations that align well with the adaptive Fourier decomposition (AFD) theory and can approximate the solution manifold of PDEs on a wide range of geometries and meshes. In several challenging benchmark PDE problems in the fields of fluid physics, solid physics, and finance on point clouds, structured meshes, regular grids, and irregular domains, AMO consistently outperforms state-of-the-art solvers in terms of relative $L^2$ error. Overall, this work presents a new paradigm for designing explainable neural operator frameworks.

---


### 360. [The Shared Discovery Paradox: How a One-Answer Rule Turns Better Information into Worse Search](https://arxiv.org/abs/2607.18045)

**<font color=#1a73e8>作者：</font>** Yohei Nakajima  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations often pool dispersed information into one ranking and then allow many agents to act on that shared view. In a discovery problem, this can improve beliefs while reducing coverage. We develop an exactly solvable benchmark with sixteen boxes, one target, eight searchers, and noisy private clues. Pooling raises the accuracy of the best single recommendation from 0.20 to 0.3835, but repeating that recommendation lowers group discovery from 0.8322 under decentralized clue-following to 0.3835. A coordinated eight-action portfolio using the same pooled reports reaches 0.8594, and seven coordinated actions recover the decentralized benchmark. The paradox is a protocol failure, not an information failure: a one-answer rule compresses a portfolio of available actions into one repeated choice. We then replace the planner with self-interested searchers who split a prize. The equal-split game is a potential game. Its anonymous symmetric equilibrium obeys a water-filling rule. In the canonical instance it achieves 0.5991: strictly above consensus, but below both private search and the planner. The exact mixed price of anarchy is 2 - 1/N. A sole-rescue reward, which pays only an agent who covers the target alone, makes every pure Nash equilibrium first-best. Finally, a latent common-cue model shows how correlated reports collapse effective discovery channels. The centralized planner gain rises strictly with copying, and in the canonical environment the symmetric market overtakes decentralized report-following at copying probability c = 0.788462. In a proportional large-market limit the five-protocol ordering survives exactly: consensus discovery vanishes while blind, market, private, and portfolio search converge to 0.500, 0.547, 0.847, and 0.874. The contribution is a compact benchmark that separates information, allocation, incentives, and dependence into exact, reusable quantities.

---


### 361. [SEE: Structure-aware Exploring \& Exploiting for Long-horizon GUI Agent Trajectory Synthesis](https://arxiv.org/abs/2607.18046)

**<font color=#1a73e8>作者：</font>** Zhuohang Fan, Beichen Zhang, Yuanfa Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents powered by vision-language models hold promise for automating real-world mobile tasks. However, progress is limited by the lack of high-coverage, long-horizon interaction trajectories collected from element-rich and rapidly evolving apps. Existing pipelines often rely on costly human demonstrations or on-policy framework, which tends to over-sample common flows while missing rare transitions and complex multi-step procedures. To address this problem, we propose SEE, a two-stage data synthesis framework consisting of (i) an efficient exploration stage that builds an explicit UI transition graph over screens and elements, and (ii) a graph-based synthesis stage that composes diverse multi-step trajectories via planning and controlled sampling. This design yields reproducible and explainable data generation, while explicitly preventing spurious cycles and enabling long-horizon composition. Across multiple real-world apps, SEE produces trajectories with an average length of 14.8 steps while avoiding spurious loops, and agents fine-tuned on SEE achieve improved task success and generalization to unseen screens. We will publicly release our synthesis code and dataset.

---


### 362. [SAR Vessel Detection and Gross Tonnage Estimation from Heterogeneous Datasets for Dark Vessel Identification](https://arxiv.org/abs/2607.18051)

**<font color=#1a73e8>作者：</font>** Davide Paltrinieri, Andrea Diecidue, Roberto Basla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting vessels engaging in illegal activities is of paramount importance for maritime security. One of the major goals is to detect dark vessels, ships that disable their transponders to evade surveillance. Deep Learning (DL) models can detect vessels in Synthetic Aperture Radar (SAR) images, enabling maritime traffic analysis regardless of weather or visibility conditions. However, to detect potential dark vessels, a DL model must select only those that are required to carry a transponder based on their Gross Tonnage (GT). Unfortunately, no public SAR dataset is available for training an end-to-end DL model for vessel detection and GT regression. In this work, we present a framework that leverages heterogeneous image and tabular datasets to solve this task. Our solution combines a multi-task DL framework for predicting the location, vessel type, and physical dimensions of ships, cascaded with a non-parametric model for predicting GT from vessel size and category. We perform GT regression by a KNN that measures sample similarity using a hybrid Euclidean and categorical distance. Experiments show that our solution can predict multiple outputs while remaining competitive with state-of-the-art models on individual subtasks, thus enabling the identification of dark vessels. We publish our code on GitHub this https URL.

---


### 363. [QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2607.18067)

**<font color=#1a73e8>作者：</font>** Shizeng Jiang, Hao Zhang, Xuerui Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) achieves high-quality real-time rendering by representing a scene with a large collection of anisotropic Gaussian primitives. However, complex scenes often require millions of Gaussians, resulting in substantial storage and rendering costs. Existing compression methods mainly reduce redundancy through primitive-wise pruning, attribute quantization, clustering, or neural coding, while redundancy caused by strongly overlapping and non-orthogonal Gaussian basis functions remains largely unexplored. We present QIRF, a quantum-inspired non-orthogonal function-space compression method for 3D Gaussian Splatting. QIRF models neighboring Gaussian primitives as a local non-orthogonal basis and formulates primitive reduction as a subspace-aware selection problem. Specifically, an analytic Gaussian overlap matrix and a radiance-response density matrix are constructed to characterize functional redundancy and rendering relevance. Generalized eigendecomposition is then used to identify the dominant local subspace and select representative Gaussian primitives. An RRDM-based response model and detail-aware safeguarding further preserve visually important high-frequency structures under aggressive pruning. Experiments on 13 scenes from Mip-NeRF 360, Tanks and Temples, and Deep Blending show that QIRF reduces the Gaussian count and raw PLY storage by 71.7 percent on average, corresponding to approximately 3.54 times compression, while maintaining reconstruction quality comparable to 3DGS and achieving a marginal average PSNR improvement of 0.10 dB. QIRF also improves the average rendering speed over 3DGS by 34.3 percent. These results suggest that non-orthogonal function-space redundancy is an important yet underexplored source of representational redundancy in explicit Gaussian radiance fields.

---


### 364. [SGN: A Similarity-based Generative Network for Data Generation under Distribution Shift](https://arxiv.org/abs/2607.18072)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhu, Xincheng Chen, Yuncheng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models trained on a source domain often produce samples that are poorly aligned with shifted target domains, limiting their effectiveness for target-domain data augmentation. Although target-specific adaptation can reduce this mismatch, it typically requires additional optimization and domain-specific parameters. We propose a Similarity-based Generative Network (SGN), a reusable framework that is trained once on labeled source data and applied to new target domains without parameter updates. SGN learns a latent space structured by label-induced pairwise similarities while preserving reconstructive information through an encoder-decoder architecture. At generation time, a small labeled representative set from the target domain is encoded and combined in the learned latent space, allowing the generated samples to inherit target-specific characteristics while maintaining class consistency. We further analyze the realizability and dimensionality requirements of the proposed similarity structure. Experiments on image and tabular datasets demonstrate the effectiveness of SGN for target-guided data augmentation under source-to-target distribution shifts.

---


### 365. [Sobek: Streaming Equivariant Tensor Product Convolutions](https://arxiv.org/abs/2607.18074)

**<font color=#1a73e8>作者：</font>** Vladimir Chorošajev, Cédric Bény  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant graph neural networks repeatedly apply edge-conditioned tensor-product convolutions over graph edges. Conventional implementations materialize edge-specific weights, messages, and adjoints, causing tensor-product workspace and memory traffic to grow rapidly with graph size and operator width. This limits feasible workloads and can prevent larger problems from fully utilizing the GPU.
We show that these edge-sized intermediates are artifacts of the execution schedule, not requirements of the equivariant operator. By reassociating radial projection, spherical-harmonic coupling, and graph aggregation, edge-local products can be consumed directly into bounded receiver-side state. The resulting streaming formulation preserves fully connected multiplicity mixing and extends through forward, backward, and double backward.
We implement this formulation in Sobek, a generated-CUDA backend, and evaluate it across edge-scaling regimes and varied feature structures. Across two operator families and all three differentiation orders, Sobek is faster in all 75 capacity-matched comparisons, with speedups ranging from $1.2\times$ to $49.7\times$, and reduces peak allocated memory by up to 99\%. It also executes workloads up to two orders of magnitude beyond OpenEquivariance's capacity while retaining near-peak throughput. These results show that edge-scaled tensor-product workspace is a property of the conventional schedule, not of equivariant convolution itself.

---


### 366. [Modeling turn-taking with distant viewing: investigating silence thresholds in human and AI-generated discourse](https://arxiv.org/abs/2607.18076)

**<font color=#1a73e8>作者：</font>** Taylor Arnold, Nicolas Ballier, Artem Saloev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates silence gaps in two kinds of audiovisual material. We analysed thirty US situational comedies and fifty-one synthetic podcasts generated with Google NotebookLM. Gaps were compared across speaker gender, assigned from a fundamental-frequency threshold estimated in Praat, and across production settings.

---


### 367. [VGOcc: Learning Visual-Geometric Gaussians for Vision-Centric 3D Driving Occupancy Prediction](https://arxiv.org/abs/2607.18078)

**<font color=#1a73e8>作者：</font>** Junhong Lin, Xianda Guo, Kangli Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-only occupancy prediction requires recovering a semantic 3D occupancy field from calibrated surround-view images, where each view provides observations with ambiguous depth along camera rays. Existing methods have progressed from dense structured representations to sparse Gaussian primitives, improving the efficiency of 3D scene representation. However, Gaussian learning still relies primarily on image domain features, which provide limited explicit geometric information for volumetric reasoning. Our key observation is that effective Gaussian occupancy modeling requires not only sparse primitives, but also richer geometric and semantic learning cues. In this paper, we propose VGOcc, which learns visual and geometric cues from foundation models for Gaussian modeling. VGOcc incorporates these cues into primitive initialization and refinement, yielding a representation termed Visual-Geometric Gaussians tailored to semantic occupancy prediction. Specifically, we propose Visual-Geometric Gaussian Birth to form spatially balanced Gaussian centers from ray depth hypotheses, while visual semantic features initialize primitive attributes. Next, we design Pose-Aware Feature Learning to combine foundation tokens with camera embeddings and calibrated ray information. Features from neighboring views are then aggregated at projected 3D locations for each Gaussian refinement stage. Finally, Gaussian decoder refines birth Gaussians with pose-aware features and renders them into semantic occupancy. Experiments on nuScenes demonstrate that VGOcc achieves state-of-the-art performance in vision-only 3D occupancy prediction. Codes will be available at this https URL.

---


### 368. [Enhancing Rubric-based RL via Self-Distillation](https://arxiv.org/abs/2607.18082)

**<font color=#1a73e8>作者：</font>** Mingxuan Xia, Yuhang Yang, Chao Ye 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based RL has recently shown promise in improving LLMs on open-ended tasks. A widely recognized limitation of rubric-based RL is limited exploration: criteria that no rollout manages to satisfy (Unexplored Criteria, UC) receive no optimization signal. Recent methods address this by incorporating rubric information as external guidance during rollout, yet they introduce a train-inference mismatch: the policy is optimized on rollouts produced under external guidance while this guidance is absent at inference time, causing error accumulation through autoregressive decoding. Moreover, these exploration-focused approaches overlook a fundamentally different failure mode that we term Suppressed Criteria (SC) -- criteria that are satisfied by some rollouts yet whose learning signals are lost during optimization because scalar reward aggregation assigns them non-positive aggregate advantages. Our analysis reveals that SC are remarkably prevalent: over 57% of samples exhibit this failure mode throughout training, with an average of 1.8 SC per sample. To simultaneously address both UC and SC without introducing training-inference mismatch, we propose Criterion-Distilled Policy Optimization (CriPO), which enhances rubric-based RL via on-policy self-distillation. For UC, CriPO constructs a criterion-injection self-teacher and computes a localized forward-KL loss to inject missing behaviors into the policy. For SC, CriPO employs a counterfactual self-teacher to locate criterion-relevant tokens in negative-advantage rollouts and flips their token-level advantages to positive values, preserving useful patterns that would otherwise be suppressed. Experiments on medicine and science benchmarks demonstrate that CriPO consistently outperforms rubric-based RL, achieving stronger final performance with approximately $2\times$ fewer optimization steps.

---


### 369. [Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator](https://arxiv.org/abs/2607.18101)

**<font color=#1a73e8>作者：</font>** Mateusz Piechocki, Alessandro Capotondi, Marek Kraft  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device model adaptation is essential to enable lifelong personalization on resource-constrained hardware, but compute, power, and memory limitations of such devices make end-to-end backpropagation impractical for modern deep neural networks. This work proposes a heterogeneous adaptation pipeline that repurposes a commercial edge AI inference accelerator, Hailo-8L, for frozen-backbone feature extraction during on-device training. The computational graph is partitioned so that the pre-trained backbone is quantized to INT8 and run on the accelerator, while only a lightweight FP32 classification head is fine-tuned on the host CPU, enabling frequent, energy-efficient in-field updates with most weights remaining fixed. Across multiple architectures and datasets, this pipeline achieves up to 15.4x faster wall-clock training time compared to a Raspberry Pi 5 CPU baseline, offers competitive throughput in favorable settings, and consistently reduces energy per sample. Post-training quantization restoration is shown to be crucial for preserving the quality of accelerator-generated features and mitigating accuracy loss in quantization-sensitive architectures. Overall, the results demonstrate a practical approach to efficient on-device adaptation using inference-oriented edge accelerators. The implementation is available at this https URL.

---


### 370. [Occlusion-Aware Panoptic Segmentation with Joint Position Embedding and Occlusion-Level Attention](https://arxiv.org/abs/2607.18112)

**<font color=#1a73e8>作者：</font>** Wenbo Wei, Jun Wang, Shan Raza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoptic segmentation in complex scenes remains challenging because of occlusions, yet modern approaches often neglect occlusion modelling. In this paper, we propose \textbf{P}osition \textbf{E}mbedding \textbf{M}odulation with \textbf{O}cclusion-\textbf{L}evel \textbf{A}ttention (PEMOLA), a novel occlusion-aware module that can be seamlessly integrated into transformer-based panoptic segmentation. To obtain occlusion cues, we train an occlusion classifier on the COCO-OLAC dataset. The classifier derives the occlusion-level attention, which serves as spatial guidance, while the occlusion labels are encoded into a learnable embedding to produce channel-wise weights. Through joint modulation, PEMOLA elegantly introduces the occlusion priors into the position embedding, thereby improving the occlusion modelling. We further annotate the Cityscapes dataset with occlusion levels, termed Cityscapes Occlusion Labels for All Computer Vision Tasks (Cityscapes-OLAC), following the same labelling protocol as COCO-OLAC, to evaluate the cross-dataset generalisation ability of PEMOLA. Extensive experiments on COCO-OLAC and Cityscapes-OLAC demonstrate that PEMOLA consistently improves panoptic segmentation quality while introducing minimal computational overhead. These results highlight the importance of occlusion modelling, where incorporating occlusion-level attention helps deliver robust panoptic segmentation under occlusion. Code and dataset are available at this https URL.

---


### 371. [Manifold-Constrained Hyper-Connections for Parameter-Efficient Finetuning](https://arxiv.org/abs/2607.18130)

**<font color=#1a73e8>作者：</font>** Valentijn Oldenburg, Floris de Kam, Bente Zuijdam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most parameter-efficient finetuning (PEFT) methods adapt weights or activations, thus leaving one of the key Transformer components unchanged: residual connections. This paper investigates Manifold-Constrained Hyper-Connections (mHC), a generalisation of residual connections, as a novel PEFT approach, wrapping frozen OLMo-2 backbones with learned residual routing modules. We find that mHC can finetune frozen Transformers, but that its role differs fundamentally from the original pre-training setting: in finetuning, fixing the residual mixing matrix to identity often improves performance. As a standalone PEFT method, mHC does not consistently outperform LoRA. However, at matched trainable parameter budgets, mHC+LoRA combinations improve language-modelling loss and show task-dependent benchmark gains at both 1B and 7B scale. Overall, our results identify residual routing as a distinct and promising novel PEFT axis.

---


### 372. [O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning](https://arxiv.org/abs/2607.18142)

**<font color=#1a73e8>作者：</font>** Mei Yuan, Qi Long, Qifeng Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial Video Anomaly Detection (IVAD) aims to identify anomalous objects and events in an industrial process, which is crucial for modern manufacturing and quality control systems. Existing VLM-based anomaly reasoning methods are capable of detecting open-ended anomalies in general domains. However, their performance declines in industrial settings characterized by intricate object transformations, strict physics, and procedural constraints. To tackle the complexity of such interaction-intensive detection, we introduce a training-free agentic framework for anomaly detection free of domain-specific knowledge, emphasizing object state evolution like humans inspectors. It is designed to track spatial-temporal dynamics and underlying transformations of detected objects over time, and then reason over the object-wise temporal state trajectories to identify abnormal objects in grounded frames. Our method overcomes limitations of prior approaches that rely on retraining on normal clips or injecting domain knowledge as context for test-time inference. Extensive experiments on three IVAD datasets demonstrate that our method outperforms frontier VLMs, agentic frameworks, and traditional VAD methods fine-tuned on the respective datasets, while providing interpretable reports over anomaly processes and types.

---


### 373. [Totally Positive Matrices and the Highest-Order Coefficients of the Characteristic Polynomial](https://arxiv.org/abs/2607.18148)

**<font color=#1a73e8>作者：</font>** Tiago Closs, Leandro Farina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the extent to which totally positive matrices can be distinguished through the highest-order coefficients of their characteristic polynomials. To identify the most informative coefficients, we also employed neural-network classifiers together with feature-attribution methods. Using datasets built from several structured totally positive families, including products of positive bidiagonal matrices, Vandermonde matrices, and Cauchy matrices, we find that the coefficients (a_{n-1}, a_{n-2}, a_{n-3}) already contain strong discriminatory information for separating totally positive from non-totally positive matrices in dimensions 5, 10, and 30. The resulting separation is markedly nonlinear and admits a natural geometric description in the corresponding three-dimensional coefficient space by means of Mahalanobis ellipsoids. These ellipsoids enclose the totally positive samples while excluding most non-totally positive ones. Moreover, different structured totally positive families exhibit distinct ellipsoidal signatures, and the separation between these signatures increases with the dimension. These observations lead us to formulate a conjecture on the geometric separation of structured totally positive families in the space determined by the three highest-order characteristic coefficients.

---


### 374. [Differentiable Logic Gate Networks for Low-Latency EEG Classification on Edge Devices](https://arxiv.org/abs/2607.18149)

**<font color=#1a73e8>作者：</font>** Shyamal Y. Dharia, Stephen D. Smith, Camilo E. Valderrama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time EEG classification on edge devices is bottlenecked by the floating-point arithmetic of conventional neural networks. We investigated Differentiable Logic Gate Networks (Diff-Logic) as a hardware-native alternative that compiles models into pure Boolean circuits executable via bitwise CPU operations. Through rigorous iso-parameter experiments across four EEG datasets spanning two classification tasks, binary dementia detection and 3-class emotion recognition, we compared Diff-Logic against matched-capacity Multi-Layer Perceptron (MLP) and Binarized Neural Network (BNN) baselines at four complexity tiers (50k-500k parameters). On dementia screening, Diff-Logic achieved 80.2% Macro F1, outperforming the MLP baseline by 6.8%. On emotion recognition, the MLP retained a moderate performance advantage but incurred a 2.3$\times$ higher latency and 14$\times$ larger model size when deployed on a power-constrained (7W) Nvidia Jetson Orin Nano CPU (Single-core). Critically, Diff-Logic inference time remained nearly constant across a 10$\times$ increase in model scale, achieving a peak speedup of 2.9$\times$ over MLPs at the largest complexity tier. Our results establish logic-based neural architectures as a practical paradigm for resource-constrained brain-computer interfaces, achieving competitive or superior performance while natively satisfying the latency and memory constraints of portable edge deployment. Code is available on GitHub: this https URL

---


### 375. [Lossless-INR: Lossless Volumetric Implicit Neural Representations](https://arxiv.org/abs/2607.18150)

**<font color=#1a73e8>作者：</font>** Kaiyuan Tang, Daniel Burke, Chaoli Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representation (INR) methods provide continuous coordinate-to-value mappings and integrate naturally with direct volume rendering, making them attractive for representing volumetric data. However, existing INR-based approaches for volumetric data are inherently lossy, and even small reconstruction errors can propagate through rendering and downstream analysis. In this work, we explore Lossless-INR, a lossless INR framework for 3D scientific volumetric data based on bit-plane decomposition. By decomposing each voxel value into binary bit-planes, we reformulate reconstruction as per-bit binary classification, so that exact recovery reduces to predicting every bit correctly. To make this optimization tractable while keeping the representation compact, we combine an octree block-partitioning strategy that adaptively subdivides complex regions with a ternary feature-grid network whose grid entries are parameterized by a ternary set of values. Experiments on diverse volumetric datasets show that this design can achieve zero bit-error rate and bit-exact reconstruction, enabling faithful rendering and downstream analysis with a compact representation. The code is available at this https URL.

---


### 376. [Plenoptic Condensation: A Novel Approach to Generalized Scene Reconstruction](https://arxiv.org/abs/2607.18151)

**<font color=#1a73e8>作者：</font>** Brevin Tilmon, Alex DeJournett, John Leffingwell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel Generalized Scene Reconstruction (GSR) approach called Plenoptic Condensation (PCon). PCon uses a multi-stage reconstruction pipeline, initially converting images into "soupy" scene elements with low (representational) power, then adaptively condensing the "soup" into "structured" elements of higher power capable of efficiently representing, for example, sharp edges and smooth reflective surfaces. PCon scene models called Reality Models (Relms) enable spatially varying representational power, which is essential for high-fidelity rendering, measurement, and scene understanding. We showcase several in-the-wild PCon reconstructions captured with consumer phone cameras and drones. In one case called "Damaged Fiat", PCon is benchmarked against two state-of-the-art (SOTA) GSR methods: NeRO and RT-Splatting. Referring to Figure 1 below, PCon reconstructs the car hood more than twice as accurately as the SOTA methods. But more importantly, the local damage profile error for PCon is 35 um (0.035 mm), whereas the two other SOTA methods are essentially unable to measure the damage at all. Our project website is available at this https URL.

---


### 377. [The Calibration Channel Determines the Bayes-Error Proxy: An Exact Law for Temperature-Induced Distortion](https://arxiv.org/abs/2607.18162)

**<font color=#1a73e8>作者：</font>** Shreyas Pradeepkumar Khandale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The soft-label Bayes-error estimator beta(z) = E[min(z, 1-z)] of Ishida et al. estimates the irreducible error of a binary task directly from probability-valued labels. Recent work by Ushio et al. showed that this estimator is fragile when the probabilities are not the true posterior: even perfectly calibrated soft labels can yield a substantially inaccurate estimate, and they propose isotonic calibration as a consistent remedy. We complement that line of work by characterizing exactly how the most widely used post-hoc calibration map -- temperature scaling -- distorts the proxy. We prove an exact, model-free identity reducing the temperature-scaled proxy to the classifier's margin distribution, from which we obtain (i) strict monotonicity in the temperature and (ii) a continuous bijection from the temperature axis onto the open interval (0, 1/2), so that a fixed classifier -- with fixed decisions and fixed 0-1 error -- can be made to report any proxy value whatsoever. Under a Gaussian model of the logits we further derive a two-parameter closed form for the entire proxy-versus-temperature curve. Across CIFAR-10, Fashion-MNIST, and SVHN (eight binary tasks), the proxy varies by 56x to 980x at constant test error, the closed form reproduces the empirical curve to within 0.018, and the calibration temperature that minimizes the expected calibration error does not coincide with any stable proxy value. Our results give a precise, predictive account of the distortion whose existence motivates calibration-based remedies, and they reinforce the practical recommendation that a proxy value is meaningful only together with the mechanism that produced its probabilities.

---


### 378. [A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control: A Case Study in Additive Manufacturing](https://arxiv.org/abs/2607.18164)

**<font color=#1a73e8>作者：</font>** Yi-Ping Chen, Ying-Kuan Tsai, Vispi Karkaria 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital Twins rely on surrogate models to mirror physical systems in real time, yet these models can degrade as operating conditions evolve, a phenomenon known as concept drift. Maintaining surrogate fidelity under drift, particularly when models must also capture aleatoric uncertainty, remains an open challenge. Existing adaptive frameworks lack principled mechanisms for detecting when updates are needed, for efficiently adapting models from limited streaming data, and for certifying that updates genuinely improve predictive performance. Here we present an adaptive Digital Twin framework that integrates a Fisher score--based multivariate drift detector, Low-Rank Adaptation (LoRA) for parameter-efficient continual learning, and a Mann--Whitney $U$ test for online statistical validation. The framework monitors surrogate-model confidence via Fisher score vectors, triggers targeted fine-tuning of fewer than 1% of model parameters upon drift detection, and statistically certifies predictive improvement before deploying the updated surrogate. Applied to a stochastic linear system and a directed energy deposition additive manufacturing process as case studies, the framework successfully detects distributional shifts with short delays and restores both predictive accuracy and uncertainty quantification under abrupt and incremental drift. These results establish a statistically rigorous and computationally tractable pathway for sustaining the trustworthiness of neural-network--based Digital Twins throughout their operational life cycle.

---


### 379. [RRAM-DP: Device-Calibrated Differential Privacy for In-Memory Edge Learning](https://arxiv.org/abs/2607.18169)

**<font color=#1a73e8>作者：</font>** Kwunhang Wong, Jichang Yang, Karl M.H. Lai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge Artificial Intelligence of Things (AIoT) systems often collect sensitive data in situ, raising serious privacy concerns. Resistive-switching random-access memory (RRAM) is an attractive substrate for efficient AIoT thanks to its multi-bit storage and compute-in-memory (CiM) capabilities, while its inherently stochastic write behavior provides a natural source of randomness that can be leveraged for differential privacy (DP) protection. Yet how to transform this device-level randomness-typically viewed as detrimental to accuracy-into a principled randomized mechanism while preserving model utility remains underexplored. We propose RRAM-DP, a hardware-algorithm co-design that relaxes RRAM write-verify operations to inject calibrated noise for inherently (epsilon, delta)-DP with formal DP analysis; together with pretraining techniques, it renders a novel private, high-utility CiM training paradigm. On CIFAR-10/100, STS-B, and SST-2, RRAM-DP-SGD incurs at best only a 3.8% accuracy drop at (epsilon=2, delta=O(1/n))-DP relative to non-private SGD. At the same privacy level, RRAM-DP-SGD delivers up to 57x and 3.2x energy savings and 2.7x and 1.8x speedups over A100 and DiVa-GEMM, respectively. These results point toward efficient, privacy-preserving in-memory training on RRAM at the edge.

---


### 380. [Certified Training for Convolutional Perturbations](https://arxiv.org/abs/2607.18195)

**<font color=#1a73e8>作者：</font>** Benedikt Brückner, Alessio Lomuscio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision models have been found to be susceptible to perturbations such as motion blur induced at runtime by a shaking camera. This impedes their deployment in critical applications since phenomena such as slightly blurred vision might lead to failures, for example an object detector missing objects. While methods such as data augmentation or Adversarial Training can improve empirical robustness, they lack formal safety guarantees, making it difficult to identify and mitigate hidden vulnerabilities. We introduce a novel Certified Training approach that leverages an efficient encoding of convolutional perturbations to train provably robust models. Our method significantly outperforms Adversarial Training, achieving, for example, over 80% robust accuracy against motion blur of reasonable intensity on CIFAR10 while maintaining comparable standard accuracy.

---


### 381. [Three-Body Scattering for Generative Modeling](https://arxiv.org/abs/2607.18198)

**<font color=#1a73e8>作者：</font>** Peng Sun, Zhenglin Cheng, Deyuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern generative models typically rely on an adversarial critic, a prescribed noise-to-data path, or an autoregressive factorization. Instead, we show that a proper distributional energy can induce sample-level motion and provide direct regression supervision for a one-step generator. Three-Body Scattering Modeling (TBSM) for generation turns the energy distance into a constant-size per-projectile interaction: each projectile is attracted toward one real source and repelled from one independently generated source. Conditioned on the projectile and its condition, its expectation equals the $2$-Wasserstein gradient-flow velocity of $\frac12D_E^2(P_{\theta},Q)$. A batch of $B$ frozen-target events yields $O(B)$ sample-level losses, each using one reference for its condition instead of the minibatch-wide all-pairs field used by methods such as Drifting Models. Tracking this conditional expectation online can reduce field noise. Using scattering in frozen image features, TBSM trains one-step generators on ImageNet-256, achieving FID${}=2.23$ with pixel-space PixelDiT-XL and FID${}=1.63$ with latent-space DiT-XL at NFE${}=1$. We provide a design map relating diffusion-related supervision, Drift-like dynamics, and GAN-like objectives. These results establish tracked scattering as a route to high-dimensional one-step generation. Code: this https URL.

---


### 382. [Causal Discovery on Irregular Time Series](https://arxiv.org/abs/2607.18226)

**<font color=#1a73e8>作者：</font>** Martim Penim, Ricardo Ribeiro Pereira, Jacopo Bono 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery methods have shown strong performance in temporal systems, but they typically rely on regular and discrete lag structures, limiting their applicability to regularly sampled data. However, many real-world tasks require dealing with irregularly sampled streams of events, such as sensor streams, healthcare data, and financial transactions. In this work, we propose an extension of PCMCI+, a state-of-the-art method for causal discovery on regular multivariate time series, to allow for handling irregular time series. Instead of modelling causal relations through fixed-lag dependencies, our method aggregates causal influence over predefined temporal windows. We evaluate our method on synthetic irregular event streams with known causal structures under different signal-to-noise ratios, showing that it consistently recovers the underlying causal graph and substantially outperforms the standard PCMCI+ on irregularly sampled data.

---


### 383. [FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry](https://arxiv.org/abs/2607.18227)

**<font color=#1a73e8>作者：</font>** Dingyun Zhang, Lixue Gong, Wei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In line with the prevailing direction of vision research, we explore the integration of both generation and editing capabilities for video and image modalities within a single model. Current approaches to collecting video editing data typically depend on labour-intensive, time-consuming curated procedures--involving object mask annotation, the use of error-introducing pair synthesis via I2V model and ControlNet-like guidance, and VLM-based quality filtering or refinement--and demonstrate limited task scalability. As a result, the diversity of editing tasks remains substantially narrower than that available for image editing models. We develop a pixel-pair temporal warped flow field that can directly generate corresponding video editing samples in real time from image editing samples, and we demonstrate across multiple levels of video editing tasks that a model can learn video editing using only such data. We regard the image modality as a particular form of the video modality. Accordingly, we design a modality mimic generation loss and a modality mimic editing loss to relatively align the capabilities--and thereby the output distributions--of the two modalities through mutual imitation. Moreover, language-based visual editing entails the comprehension of the editing instruction and the reference visual content, the localization of the region corresponding to that instruction within the reference visual contents, and the modification of that region alone. Existing approaches predominantly rely on external aids, such as fine-tuning an additional MLLM or explicitly supplying a mask sequence as auxiliary input during inference. In contrast, we aspire for the model to internalize this capability. To that end, we introduce sense-related tasks--for instance, referring expression segmentation--along with corresponding editing-region-aware latent-level loss and attention-level loss.

---


### 384. [Logical Judgments Under Pressure: Diagnosing Syllogistic Stability with Learned Soft Prefixes](https://arxiv.org/abs/2607.18228)

**<font color=#1a73e8>作者：</font>** Brian K Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To test how correct logical judgments respond to learned context, we prepend a soft prefix to an exactly labeled syllogistic reasoning benchmark while keeping the model fixed. Soft prefixes are opaque continuous vectors, so we characterize them through the behavior they induce across controlled variations in logical form and interface. By studying which prefixes succeed and how their effects generalize, we characterize how learned contextual pressure can override correct judgments and expose limits in a model's logical stability. Across Qwen3.6-35B-A3B MoE, Qwen3-8B, and Gemma 4 31B, learned prefixes redirect many correct answers and remain effective across unseen forms and interface changes. In repeated tests with Qwen3.6 MoE and Gemma, they outperform paired random controls in all 16 model--direction--split comparisons by 37 to 99 percentage points. Qwen3.6 MoE flip rates remain between 72% and 90% across wording and prompt changes, while Gemma validity prefixes retain 54% to 56% flip compared with less than 1% for matched random prefixes. Diagnostic tests show that the dominant effect is a broad preference for one answer meaning rather than fixed-symbol forcing or a logical operation that transfers reliably between tasks. The form of this bias differs across models. In both Qwen models, simple score models often predict which judgments will flip but not how far their margins will move, whereas Gemma's overall response is more closely approximated by the same models. These results show that the dominant behavioral effect of successful soft prefixes is a broad answer preference, while the remaining response reveals substantial model-specific differences in logical stability.

---


### 385. [Automated Discovery Has No Universally Superior Harness](https://arxiv.org/abs/2607.18235)

**<font color=#1a73e8>作者：</font>** Akshat Gupta, Jermaine Lei, Alexander Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous discovery systems such as OpenEvolve and TTT-Discover are often used as general-purpose harnesses. However, in practice these are composite systems combining several design choices about archives, parent selection, exploration, and budget allocation into a single recipe. Because discovery runs are expensive and inherently stochastic, existing harnesses are often compared using too few independent trials to distinguish key methodological improvements from run-to-run variance. We systematically decompose OpenEvolve-style evolutionary search and the TTT-Discover search harness into its constituent components and systematically evaluate 30 budget-matched harnesses across 12 model-problem pairs using more than 3.1 million LLM rollouts and repeated-trial statistical analysis. Our results show that discovery harnesses have a generalization problem: No fixed harness is reliably superior across the evaluated model-problem pairs, and variants of OpenEvolve generally underperform simpler alternatives. Thus, harness choice is better viewed as a hyperparameter rather than as a universal recipe, and should be tailored to the specific problem and underlying model. We also find that early discovery progress predicts final performance, and use this property to present a budget-matched adaptive-allocation experiment that starts multiple harnesses, prunes weak partial runs, and reallocates compute to stronger survivors, outperforming both commitment to a randomly sampled fixed harness and a non-adaptive harness ensemble. Together, these results motivate shifting from fixed harness selection to online adaptation guided by early performance. We release all run pools including baseline null distributions for every model-problem pair as reusable statistical infrastructure against for future harness proposals.

---


### 386. [The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric](https://arxiv.org/abs/2607.18237)

**<font color=#1a73e8>作者：</font>** Sheng-Yu Wang, Yotam Nitzan, Aaron Hertzmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human visual similarity judgments are context-dependent. For example, two images may be similar in shape but distinct in color. Existing perceptual similarity metrics, however, collapse these nuances into a single scalar value, offering no mechanism to condition on specific aspects. To bridge this gap, we introduce a large-scale dataset of human similarity judgments over image triplets, where each triplet is annotated across multiple, free-form semantic aspects of similarity. Benchmarking a broad range of frontier vision-language models (VLMs) reveals a considerable performance gap compared to human annotators' consensus. Leveraging our data, we fine-tune a VLM to produce our Text-Prompted Image Perceptual Similarity (TPIPS) metric, capturing multiple senses of visual similarity depending on the specified text prompt. We demonstrate that TPIPS aligns more closely with human perception and generalizes reliably beyond the training distribution. Finally, we show that TPIPS unlocks new capabilities in text-guided retrieval, compositional search, and the fine-grained evaluation of generative models. Our code, data, and trained models are at this https URL

---


> [!TIP]
> 当前位于：**351-386**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-386**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
