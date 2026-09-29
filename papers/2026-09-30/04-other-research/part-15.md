# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**701-750**（第 15/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 701. [From Pixel Generation to Topological Inference: Structural Dual Super-Resolution for Trustworthy Cross-Physical-Domain Trabecular Morphology Learning](https://arxiv.org/abs/2609.34716)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Yi Zhang, Ling Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical CT and UHRCT cannot resolve individual trabeculae, whereas synchrotron radiation microCT (SR{\mu}CT) provides 3.2{\mu}m high-resolution references but is not applicable for in vivo imaging. The two domains differ by 31.25x in resolution, are only coarsely paired, and have drastically different data volumes. Moreover, clinical UHRCT suffers from severe partial volume effects, strong noise, and beam hardening/scatter artifacts, while SR{\mu}CT is nearly free. Existing super-resolution networks and pretrained-prior methods underperform because they target pixel generation--diverse details and SSIM/PSNR--and do not explicitly model these physical differences. This indicates that 32x super-resolution via pixel generation is intrinsically ill-posed. We propose a paradigm shift from pixel generation to topological inference: deterministically predicting invariant microstructures from macro-scale low-resolution inputs, evaluated by morphological parameters. We realize this paradigm via structural dual super-resolution, coupling forward physical degradation (micro-to-macro) with inverse structural inference (macro-to-micro) through structural duality constraints. The method is an end-to-end, few-shot, compact structural dual network (SDN), comprising a bidirectional modeling network for forward degradation and inverse reconstruction, a pyramid structural consistency discriminator, and four structural duality constraints. On the testset, SDN achieves morphological parameters largely consistent with SR{\mu}CT across 7 metrics, enabling clinical UHRCT with micro-imaging-level morphological quantification, with SSIM reaching 0.8. Trained on 3.2{\mu}m SSRF data, the model generalizes well to 3.25{\mu}m BSRF data from an independent source, validating cross-source generalization and confirming that the designed network achieves trustworthy structural inference rather than pixel generation.

---


### 702. [Geometry as Address: Routing Attention to Visual Memory for Long-Horizon Camera-Controlled Video Generation](https://arxiv.org/abs/2609.34722)

**<font color=#1a73e8>作者：</font>** Zesong Yang, Weikai Chen, Liyuan Cui 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon camera-controlled video generation requires recovering previously observed content from an ever-growing visual history. Existing approaches either search historical context implicitly or reconstruct it into persistent 3D memory, facing inefficient memory access or accumulated geometric errors. Our key insight is that geometry need not explain the scene--it only needs to determine where visual memory should be read from, while attention decides what should be recovered. Based on this insight, we introduce GEAR, a Geometry-Enabled Attention Routing framework that uses geometry as an explicit token-level address for visual memory. Rather than fusing historical observations into a persistent global 3D representation, GEAR retains them as frame latents and uses per-frame geometry only to establish token-level correspondences with target views, thereby avoiding persistent error accumulation from global fusion. Guided by these correspondences, Geometric Correspondence Attention (GCA) selectively injects geometrically matched historical features into noisy target patches during denoising. We further introduce an Invisible Octree to accumulate visibility evidence and reject geometrically plausible but occluded correspondences. Extensive experiments demonstrate that GEAR achieves state-of-the-art visual quality, precise camera control, and revisit consistency, enabling minute-long video generation along challenging trajectories.

---


### 703. [Edge-Level Automorphism in GNNs: A Quantitative Framework and Effective Designs For Link Prediction](https://arxiv.org/abs/2609.34729)

**<font color=#1a73e8>作者：</font>** Chen Shao, Donald Loveland, Tobias Käfer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are effective for learning node and link embeddings through permutation-equivariant aggregation. However, standard GNNs collapse automorphic nodes, i.e., those with identical structural roles (or orbits) into indistinguishable representations, leading to the node automorphism problem. This collapse limits their expressive power and degrades link prediction performance. Existing approaches to characterize GNN expressiveness rely primarily on Weisfeiler-Lehman (WL) analyses, but these methods are typically qualitative and often misaligned with empirical results. To address this gap, we begin by introducing a novel quantitative framework to assess GNN expressiveness for link prediction. We first formalize edge-level automorphism through edge orbits, which capture the set of structural role pairs for nodes that share a link. Then, we introduce the edge automorphism ratio (EAR), a scalar metric that quantifies a GNN's ability to distinguish links in a given graph. We empirically demonstrate that EAR correlates strongly with performance, validating its practical benefit. Building on this insight, we design EDGE-ORBIT EQUIVARIANT GRAPH NEURAL NETWORK (EO-GNN), a GNN architecture that addresses automorphism collapse while preserving equivariance and incurring minimal computational overhead. EO-GNN accomplishes this through two core designs combined with WL-based node hashes: (i) automorphism-aware dropouts and (ii) subgraph orbit-biased aggregation. Empirical evaluations on synthetic and real graphs show improvements of up to 42.36% and 28.44%, respectively, in predicting links in scenarios with high automorphism.

---


### 704. [What Visual Generators Need from Teachers: Rethinking Representation Alignment](https://arxiv.org/abs/2609.34732)

**<font color=#1a73e8>作者：</font>** Yongcong Wang, Hingchin Chen, Mingyu Fan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment speeds up diffusion transformer training by pulling an intermediate block of the model (student) toward features of a frozen pretrained encoder (teacher). Which teacher layer to align, and for how long, is still set by convention, and each alternative costs a training run. We find that alignment helps where the student cannot linearly recover the teacher's features, not where it already resembles them. Since a deep teacher layer is largely predictable from the one below, we isolate what each layer adds, its increment, and measure how much of it an unaligned student recovers. The student fills the teacher's hierarchy from the bottom up and stalls near the top, which we call hierarchy filling: even after 400K steps it recovers almost none of the deepest. The recoverability gap is the unrecovered share of an increment, read from one unaligned checkpoint. In short runs that each align one teacher layer at one block, the gap nearly reproduces their ranking by FID improvement, and CKA, a measure of feature similarity, largely reverses it. Representation Alignment and Recoverability Estimation (RARE) picks the teacher layer with the largest gap before training. During training, it tracks each token's remaining distance to that layer, the online counterpart of the gap, weights tokens by it, and phases out the loss once the average distance stops falling. With SiT-B/2 on ImageNet $256\times256$, RARE reaches an FID of 18.02 without guidance and 4.46 with it, ahead of seven alignment baselines including REPA, iREPA and HASTE. It also trains in 14% fewer GPU-hours than iREPA. Its FID stays below iREPA's across model scales, teachers, datasets and backbones.

---


### 705. [SurgGMF: Fully Causal Gaussian Motion Forecasting for Anticipatory Surgical Scene Rendering](https://arxiv.org/abs/2609.34733)

**<font color=#1a73e8>作者：</font>** Jingqian Sun, Yichao Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic surgical scene modeling is essential for robotic perception, simulation, and decision support. Although existing neural rendering methods enable efficient reconstruction and rendering of deformable surgical scenes, they remain primarily focused on observed-frame reconstruction rather than forecasting future scene states. To this end, we present SurgGMF, a fully causal Gaussian motion forecasting framework for anticipatory surgical scene rendering. Rather than predicting future RGB images directly, SurgGMF forecasts future Gaussian motion states represented by position, scale, and rotation residuals (X/S/R) from historical Gaussian motion fields. To prevent target leakage, we introduce a full-causal-last rendering protocol, where future Gaussian states are rendered without accessing target-frame Gaussian attributes while preserving causal appearance propagation. We evaluate SurgGMF on 12 EndoNeRF and StereoMIS video slices using neural temporal learners and classical dynamics baselines under a unified forecasting protocol. Learned Gaussian motion forecasting consistently outperforms classical dynamics baselines in render space, demonstrating gains beyond hand-crafted state extrapolation. Latency analysis further reveals an accuracy--efficiency trade-off: under the current implementations, TKAN achieves the highest accuracy, whereas GRU and LSTM provide more favorable module-level latency profiles. These results establish SurgGMF as a reproducible framework for causal Gaussian motion forecasting and advance surgical Gaussian representations from retrospective reconstruction toward predictive scene modeling.

---


### 706. [From Human Narrative to Harmonic Structure: A Human-Centered Investigation of Algorithmic Music Generation through the Chord Wheel Diagram](https://arxiv.org/abs/2609.34735)

**<font color=#1a73e8>作者：</font>** Josef Pavlíček, Petra Pavlíčková, Irena Štrausová  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contemporary AI-based music generation can produce compositions that satisfy formal requirements of tonality and musical coherence. However, whether musical expression can be described by mathematical properties alone remains a fundamental question. Human composers operate within personal and cultural contexts that influence harmonic decisions and deliberate departures from established patterns. This study investigates six narrative-driven popular songs by Bob Dylan, Johnny Cash, and Ritchie Valens. Original human harmonies are compared with outputs of an explainable computational harmonizer operating on the same melodies without access to the original chord progressions. We examine harmonic vocabulary, functional persistence, repetition, non-diatonic events, and tension-resolution patterns using Chord Wheel Diagrams and BPMN-based representations. Results show that high melody-chord compatibility does not necessarily imply preservation of the original human harmonic decision pattern. Some generated harmonizations retain the economical structure of the reference, while others alter harmonic diversity or suppress distinctive events while remaining compatible with the melody. Rather than quantifying artistic quality, the study introduces narrative-conditioned harmonic structure as a complementary perspective for computational music analysis. The findings suggest that generative systems may benefit from modeling not only harmonic correctness, but also structural identity, context, and human compositional intention.

---


### 707. [Predictive Dual Smoothing for Column Generation](https://arxiv.org/abs/2609.34740)

**<font color=#1a73e8>作者：</font>** Senne Berden, Noah Schutte, Andrea Lodi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving large-scale linear programs efficiently is an important challenge in many optimization settings. A key technique is column generation, which alternates between solving the master problem over a restricted subset of the variables, and using a pricing subproblem to identify new variables to add. The pricing subproblem is guided by the dual solution of the current restricted master problem, but oscillations in these dual solutions can substantially slow convergence. Dual stabilization methods address this issue. Dual smoothing is a common stabilization method, which guides the pricing subproblem using a combination of the current dual solution and duals from previous iterations. However, while past dual solutions can stabilize the dual trajectory, they do not necessarily guide pricing towards useful new variables. We therefore introduce predictive dual smoothing, which instead combines the current dual solution with a learned prediction of future duals to steer pricing towards variables that are more useful in subsequent iterations. The predictor is trained offline using supervision extracted from standard column generation trajectories and is used only to modify the pricing subproblem's objective function, while exact reduced-cost checks and fallback pricing with the unsmoothed duals preserve correctness. Experiments on cutting stock and generalized assignment problems show that predictive dual smoothing substantially reduces generated columns and wall-clock time relative to standard column generation and existing classical and learned stabilization methods. These gains extend to out-of-distribution instance sizes, and predictive smoothing provides further improvements when combined with strong classical stabilization.

---


### 708. [Optimizing and Securing the Modern Watermarking Channel for Images](https://arxiv.org/abs/2609.34744)

**<font color=#1a73e8>作者：</font>** Enoal Gesny, Eva Giboulot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To comply with recent regulations requiring traceable generated content, modern watermarking has adopted multi-bit post-hoc watermarking schemes. These modern designs rest on an encoder-decoder pair implemented as deep neural networks. These models are usually treated as pure black-boxes trained end-to-end, with the noise of the watermarking channel modeled through a fixed set of geometric and valuemetric transforms applied to watermarked images. We argue that this purely empirical approach leads to unquestioned design flaws and a lack of theoretical performance guarantees. This work proposes a general theoretical model of modern post-hoc watermarking schemes grounded in a statistical analysis of the outputs of the encoder/decoder pair. We show that these deep neural networks implicitly define a watermarking channel modeled as parallel AWGN channels, with messages transmitted using BPSK modulation. This imposes a binary alphabet, greatly limiting the capacity of these watermarking systems. Another fatal flaw is their lack of a secret key, making them intrinsically insecure. We make this notion of watermarking security precise for post-hoc schemes by linking it to the possibility of estimating the secret key under a given statistical model of the decoder's output. By putting together the results from this theoretical analysis, we introduce SNW: a novel post-hoc watermarking system that significantly outperforms existing state-of-the-art baselines in terms of capacity while also providing strong security guarantees. Notably, it does not depend on a fixed codebook or binary alphabet, allowing it to reach a rate close to Shannon capacity through the use of capacity-achieving error-correcting codes.

---


### 709. [CoDrive: Cross-Vehicle World-Consistent Video Generation with Precise Trajectory Control for Cooperative Driving](https://arxiv.org/abs/2609.34749)

**<font color=#1a73e8>作者：</font>** Yu Meng, Baining Zhao, Junta Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world driving is inherently multi-agent, yet most existing driving world models generate observations from a single ego vehicle. Independently extending them to multiple vehicles does not ensure that different agents observe a consistent shared world. We present CoDrive, a cross-vehicle, multi-view driving video generation framework that jointly generates observations of vehicles sharing the same dynamic scene with precise camera-trajectory control. CoDrive interleaves local self-attention, which models spatiotemporal dependencies among the views of each vehicle, with global self-attention, which enables information exchange and consistency modeling across vehicles. To explicitly encode their spatial relationships, all camera trajectories are represented in a shared world coordinate system and injected into the attention layers through projective relative positional encoding. We further adopt a progressive mixed-task training strategy that combines large-scale real-world single-agent data with synthetic cross-agent interaction data, allowing the model to benefit from real-world appearance distributions while learning cross-agent consistency from simulation. For systematic evaluation, we introduce CoDrive-Bench, a benchmark covering real and synthetic multi-vehicle scenarios and evaluating trajectory controllability, scene geometry consistency, and instance-level consistency. Experiments show that CoDrive improves trajectory controllability and cross-agent geometric and instance consistency while maintaining competitive visual quality.

---


### 710. [A Unifying Framework of Concept-based Explainable AI with Completeness Guarantees](https://arxiv.org/abs/2609.34750)

**<font color=#1a73e8>作者：</font>** Vojtěch Kůr, Adam Kukučka, Tomáš Brázdil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept-based explanations describe neural network predictions through human-understandable properties of inputs called concepts. The field encompasses approaches that differ in how they define and represent concepts and connect them to model predictions. We introduce a theoretical framework that describes these approaches in a common mathematical language and supports a shared analysis of their properties. For concept discovery, which identifies concepts automatically within a latent space of a trained model, we employ a concept autoencoder view. An encoder extracts concept representations from the model's latent space, and a decoder uses them to reconstruct the original latent representation. The autoencoder's reconstruction error measures how accurately its decoder recovers the original latent representation. We revisit model completeness: how well the concepts can reproduce the model's outputs. We show that model incompleteness of the concepts can be bounded by the autoencoder's reconstruction error. The autoencoder view also provides a common way to define individual concept attributions, which measure each concept's contribution to a prediction. We establish when these attributions sum to the model's prediction, and bound the discrepancy otherwise, thus providing attribution completeness guarantees.

---


### 711. [LongPuzzleBench: Evaluating GUI Agents on Long-Horizon Visual Puzzles](https://arxiv.org/abs/2609.34769)

**<font color=#1a73e8>作者：</font>** Bingo Zhang, Haochuan Lu, Zongjie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GUI agents need long-horizon visual reasoning: they must interpret a changing interface while keeping a multi-step plan viable as earlier actions constrain later ones. Existing benchmarks evaluate grounding, computer use, and game play, but rarely test whether agents stay coherent across long chains of coupled decisions. Long-horizon visual puzzles expose this capability directly: a legal move that looks like progress can make the puzzle unsolvable, and the loss shows only several moves later. We introduce LongPuzzleBench, 114 levels in six puzzle games played through native GUI actions, where one objective can take a human over a thousand actions on persistent boards and dead ends go unannounced. With Native GUI Actions alone, the strongest agents solve most objectives, but success falls sharply on harder, longer boards: seven of ten general-purpose agents solve nothing harder than Medium, and none completes Bolt Unscrew Hard, which a human solves along with every other objective. Code Execution CUA does not close this gap, and its scores mix visual solving with algorithmic search. Controlled diagnostics trace these failures to one limitation that neither rules, state hints, nor failure memory removes: agents judge each move by the visible progress it makes, not by the future options it leaves.

---


### 712. [Projective Normal Fields: A Convex Optimization Method for Constructing Smooth UDFs](https://arxiv.org/abs/2609.34784)

**<font color=#1a73e8>作者：</font>** Jiayi Kong, Chen Zong, Fei Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Constructing a smooth approximation of an unsigned distance field (UDF) from a raw point cloud is challenging because the input provides neither surface connectivity nor consistently oriented normals. Methods that directly learn a scalar UDF must also handle its non-differentiability on the zero level set and weak supervision away from the samples, which can lead to unstable optimization and spatial artifacts. We introduce Projective Normal Fields (PNFs), an orientation-free representation and convex optimization framework for estimating bidirectional normals from point positions alone. Each normal axis is encoded by a rank-one projector, which is invariant to normal reversal. We relax the non-convex set of hard projectors to its convex hull: the symmetric positive-semidefinite matrices with unit trace. Each soft tensor defines a local quadratic distance model and retains the relative weights of candidate normal axes. We estimate a coherent PNF by combining local tangent-plane fitting, soft-PCA anchoring, and overlap regularization on a fixed neighborhood graph. With positive anchoring weights, the objective is strongly convex and admits a unique global minimizer. Principal eigenvectors provide bidirectional normals, while the corresponding eigengaps provide spectral confidence indicators. We use these indicators to select and weight directional sources for heat diffusion, followed by Poisson integration to construct a regularized UDF approximation. By separating local geometry estimation from scalar-field construction, PNF avoids directly fitting the non-differentiable UDF. Experiments demonstrate reduced sensitivity to neighborhood size, competitive reconstruction under noise and outliers, and improved accuracy near non-manifold junctions. The project page is available at this https URL

---


### 713. [Physics-Guided Spectral Distillation for Underwater Image Enhancement on Resource-Constrained Devices](https://arxiv.org/abs/2609.34795)

**<font color=#1a73e8>作者：</font>** Yifan Chen, Kai He, Ye Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater image enhancement is crucial for improving visual perception in marine applications. Existing underwater image enhancement studies mainly focus on enhancement quality and visual fidelity, while rarely considering real-time deployment capability, which is essential for resource-constrained underwater robots. To this end, we introduce a physics-guided spectral distillation (PSD) method, which reduces model capacity for real-time applications while maintaining the high performance of underwater image enhancement models. To decompose the outputs of teacher and student models, PSD adopts a multilevel Haar discrete wavelet transform. It transfers low-frequency color and illumination information as well as high-frequency structural details through band-specific objectives. Moreover, the distillation process of PSD is degradation-aware. We estimate degradation-aware weights through a physical head and combine them with ground-truth-guided reliability masks to selectively retain valuable teacher guidance. Experiments on the UIEB, LSUI, and EUVP datasets validate the effectiveness of the proposed method. Furthermore, we demonstrate the benefits of enhanced images for downstream perception tasks, including object detection. Deployment on a self-developed ROV further demonstrates its practical applicability in real-world underwater scenarios.

---


### 714. [STRIDE: Automated Evaluation of Text-to-Trajectory Alignment across Diverse Contexts](https://arxiv.org/abs/2609.34799)

**<font color=#1a73e8>作者：</font>** Wanchun Ni, Tao Qi, Leonel Aguilar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-conditioned trajectory generation is here, but its evaluation has not kept pace. Existing pedestrian trajectory metrics compare trajectories with real-world human data. This does not scale to text-to-trajectory generation across diverse contexts, as collecting human trajectories for every scenario is costly and infeasible. Moreover, pedestrian behavior is heterogeneous and context-dependent, with no single metric as the correct answer, and current evaluation frameworks are not transferable to this domain. These challenges make scalable, reliable evaluation difficult. We introduce STRIDE, the first framework for evaluating context alignment between scenario descriptions and pedestrian trajectories. STRIDE addresses these challenges through three design choices. First, we derive our VRDST evaluation protocol from sociological theories to define a complete evaluation space. Second, it decomposes high-level context into scenario-adaptive behavioral questions. Third, every question is resolved against a deterministic measurement tool library that yields reproducible answers. Together, STRIDE enables complete, verifiable, automated, and scalable evaluation across diverse contexts without requiring human trajectory data. We instantiate STRIDE in the crowd domain as STRIDE-Bench, comprising 1K scenarios, 6K behavioral questions, and 11K measurements with calibrated expected answers across 30 real-world maps. Comprehensive human validations show that STRIDE-Bench is consistent with human behavior and judgment, achieving 80% human agreement. We further evaluate several text-to-trajectory models, finding limited context-alignment capability and persistent challenges in fine-grained context conditioning. We believe that the STRIDE framework provides a first step toward principled evaluation of context-aligned pedestrian trajectory generation.

---


### 715. [Physics-Attested Federated Learning: Securing Collaborative Anomaly Detection in Critical Water Infrastructure](https://arxiv.org/abs/2609.34804)

**<font color=#1a73e8>作者：</font>** Jeff Nijsse, Shu Su, Benjamin Oholeguy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning enables industrial operators to train shared intrusion detection models without disclosing proprietary operational telemetry. However, existing defenses operate strictly in update space, leaving aggregators blind to data poisoning; model updates derived from fabricated telemetry remain indistinguishable from honest contributions. We repurpose cyber-physical process invariants, such as conservation laws and actuator couplings, from runtime detection heuristics into a verifiable admission requirement for federated updates, mined automatically from clean operational data. We evaluate this admission gate across two physical water testbeds (SWaT, WADI) and a distribution benchmark (BATADAL), testing seven aggregation rules against telemetry fabrication, exposure-only replay poisoning, and an invariant-aware adaptive adversary. Across three testbeds the mined invariants reject none of 100 honest shards and all naively fabricated ones, including optimised perturbations that FoolsGold admits in full. On real telemetry, five mined invariants detect 12 of SWaT's 35 attacks, while nine invariants detect 20, with no honest shard rejected. With nine rules, the physics gate recovers 69--100% of the targeted-attack recall lost to replay poisoning, and 54--100% of that lost to fabricated telemetry, across five standard aggregators. To reconcile physical admission control with federated data privacy, we show invariant compliance using zero-knowledge proofs (zk-SNARKs) to allow clients to prove batch adherence without revealing operational telemetry.

---


### 716. [Polylogarithmic Nash Regret in Matrix Games with Bandit Feedback](https://arxiv.org/abs/2609.34812)

**<font color=#1a73e8>作者：</font>** Yuheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Nash regret minimization in unknown finite matrix games with bandit payoff feedback and observed opponent actions. We develop Optimistic Payoff Balancing (OPB), which achieves instance-dependent $\mathcal{O}(\log^2 T)$ Nash regret against arbitrary adaptive opponents, including games with nonunique equilibria. This resolves the open problem posed by Maiti et al. (2025), extending their polylogarithmic guarantee under bandit feedback from $2\times2$ games to arbitrary finite dimensions. To handle nonunique equilibria, we construct a reference strategy that leaves room for local adjustments. We order independent payoff differences by estimation accuracy and scale these adjustments by uncertainty, allowing the learner to exploit the opponent's imbalance to offset estimation costs. Our result thus shows that observing opponent actions suffices for polylogarithmic Nash regret in general finite matrix games.

---


### 717. [ESTHER: Egocentric Stereo Hand Estimation and Reconstruction in the Wild](https://arxiv.org/abs/2609.34817)

**<font color=#1a73e8>作者：</font>** Hongyu Ma, Hairong Qu, Shiqi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human dexterity is guided by two eyes watching two hands: binocular vision supplies the metric 3D structure that fine-grained manipulation consumes. Egocentric stereo is therefore the natural perceptual interface for robots, AR, and VR-yet metric 3D hand reconstruction from this very signal still has neither an end-to-end model nor an in-the-wild benchmark. We propose ESTHER, a model whose stereo geometry, temporal reasoning, and output representation are designed for wearable egocentric stereo. It is trained on pseudo-labels from a calibrated labeling pipeline and in turn assembles our benchmark ESTHER3D, an egocentric stereo hand dataset pairing a large in-the-wild training set of model-generated labels with a motion capture test set of true metric ground truth. Experiments show state-of-the-art accu?racy, superior external generalization, and robustness to the missing views, dropped frames, and lighting and motion blur extremes of real egocentric capture that break existing meth?ods. This robustness runs deeper than graceful degradation: stereo guidance teaches the model to bind apparent hand scale to metric depth, so it not only adapts to different stereo rigs and modalities with minimal fine-tuning, but more strikingly preserves true metric scale even after collapsing to a single monocular view.

---


### 718. [Generative Residual Factorization](https://arxiv.org/abs/2609.34824)

**<font color=#1a73e8>作者：</font>** Letian Gong, Yuzhou Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Under a shared-factor model, the conditional law of the next image patch factors into a posterior over the shared scene factor and a residual kernel given that factor. A sufficient statistic of the past replaces the raw past in the posterior and does not replace the kernel. The conditional entropy splits into residual entropy, which no observation of the factor can remove, and a posterior term, which a better representation of the past can remove. Next-embedding prediction is a directional likelihood on a shallow map, so the fiber of that map is unidentified and a constant embedding remains a minimizer. The same split is an equality in a scalar Gaussian model, evaluated in closed form.

---


### 719. [Gaussian Neural Networks](https://arxiv.org/abs/2609.34825)

**<font color=#1a73e8>作者：</font>** Peter Kuhn, Victoria Heusinger-Heß  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian neural networks (GaNNs) are proposed as a novel regularization mechanism for neural networks. From a Bayesian perspective standard regularization techniques can be viewed as imposing priors over weight-space. Assuming priors over activation-space remains a largely unexplored possibility. GaNNs assume such priors. They do this by treating activities from earlier layers like signals with Gaussian noise and predicting the properties of the noise distribution using an additional unsupervised loss. While training, the unsupervised loss acts as a penalty on unexpected activities, allowing greater weight updates in less surprising directions. The paper demonstrates the superiority of Gaussian neural networks over standard neural networks on a variety of classification and regression tasks. We also investigate the ability of GaNNs to quantify uncertainty.

---


### 720. [Structured Neural SDEs for Functional Calibration](https://arxiv.org/abs/2609.34831)

**<font color=#1a73e8>作者：</font>** Francesco Piatti, Andrea Iannucci, Thomas Cass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Stochastic Differential Equations (Neural SDEs) provide flexible continuous-time generative models, but generic neural drift and diffusion networks are costly to simulate on long horizons and can give unstable gradients when the training signal is a path functional rather than a pointwise observation. We introduce SLiSDE, a family of Neural SDE models built from structured linear stochastic layers. Parallel-in-time simulation is obtained at the layer level, while expressivity is recovered by gated in-flow stacking: previous-layer paths modulate the next layer's latent flow through learned gates. For functional calibration tasks in which rare paths dominate the loss, we add an optional Girsanov tilt that acts as a learned importance sampler with an exact likelihood-ratio correction. We prove well-posedness, a discretisation error bound, validity of the change of measure, and a universality result: the terminal laws of the gated stack are dense in the space of square-integrable laws. Experiments on functional calibration benchmarks show that the structured model outperforms fully neural SDE baselines while retaining parallel-time simulation and stable importance weights.

---


### 721. [Multi-Scale Semantic Mapping in Urban Environments via Observation Calibration and Policy Dependence Regularization](https://arxiv.org/abs/2609.34833)

**<font color=#1a73e8>作者：</font>** Runling Long, Junhao Feng, Jia Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic mapping is fundamental to embodied navigation, yet existing methods are developed for indoor environments, where objects exhibit relatively limited scale variation and are observed from a restricted range of viewpoints. Urban environments pose substantially greater challenges: agents must map objects ranging from pedestrians to buildings while navigating large spaces with highly diverse viewing distances. These conditions introduce two key difficulties that existing datasets and methods fail to cover. First, object scale and observation distance can be severely mismatched. For example, small objects may be viewed from far away, whereas large objects may be observed at extremely close range, resulting in unreliable observation likelihoods. Second, objects with substantially different sizes and geometries require distinct mapping behaviors, which are difficult to capture with a single shared value estimator. To investigate these challenges, we introduce a large-scale urban semantic mapping dataset featuring realistic city layouts, high-fidelity rendering, and instance-level annotations spanning multiple object scales. We then propose a category-aware likelihood calibration policy that identifies and alleviates unreliable observations according to object category and viewing distance. Because the calibration and motion policies are optimized toward the same mapping objective, they may learn redundant shortcuts and become excessively coupled. We therefore introduce a mutual-information (MI) regularizer that penalizes their estimated representation dependence and encourages complementary behaviors. To better model heterogeneous mapping strategies across object scales, we further employ category-wise value estimators. We formulate their joint optimization as a Pareto optimization problem to mitigate conflicting gradients across categories.

---


### 722. [Transform-Aligned Learned Features for Lossy Point Cloud Attribute Compression](https://arxiv.org/abs/2609.34834)

**<font color=#1a73e8>作者：</font>** Yueru Chen, Pengpeng Yu, Dingquan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transform-based methods provide an effective framework for point cloud attribute compression by representing attributes as transform coefficients. Introducing learned spatial context into this framework requires mapping spatial representations to the transform domain, but this known basis change is often left for the network to learn implicitly. We propose Transform-Aligned Learned Features (TALF) by applying the attribute transform to learned spatial representations, explicitly aligning them with the coding targets. Our analysis shows that the resulting features exactly represent the first-order prediction term of a smooth nonlinear model, with a bounded Taylor remainder. We integrate TALF into a transform-based attribute codec with explicit coefficient prediction and conditional residual entropy modeling under a unified coefficient-domain rate--distortion objective, while retaining explicit quantization-step control. Extensive experiments across three benchmark datasets and multiple transform bases demonstrate that TALF improves rate--distortion performance over conventional and learned baselines.

---


### 723. [OpenWhistle: A Large-Scale Longitudinal Dataset and Benchmark of Bottlenose Dolphin Vocalizations](https://arxiv.org/abs/2609.34839)

**<font color=#1a73e8>作者：</font>** Faadil Mustun, Chiara Semenzin, Roberto Dessi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in bioacoustics have been driven by large-scale corpora and standardized benchmarks, yet existing resources are overwhelmingly bird-centric and shallow per species, limiting their use for studying the structure of a single species' communication system. This gap is particularly acute for cetaceans: despite bottlenose dolphins (Tursiops truncatus) being a compelling case of complex vocal communication among non-human mammals, existing dolphin datasets are small, fragmented, and largely closed. We introduce OpenWhistle, the largest publicly available dataset of dolphin vocalizations. It comprises approximately 180,000 whistles (114 hours) recorded over five years from a stable pod of five individuals in a semi-natural environment, paired with a curated subset of 8,354 expert-annotated whistles and reproducible evaluation protocols for whistle-type detection and classification. We further release the full processing pipeline for whistle detection, segmentation, and categorization. To demonstrate its utility, we pretrain a Wav2Vec2.0 model adapted to dolphin acoustics on the OpenWhistle corpus and show that it learns effective representations, outperforming general-purpose bioacoustic models such as AVES and BioLingual on both tasks while leaving meaningful headroom for future work. By releasing the dataset, pipeline, and evaluation protocol, we provide the first open dolphin whistle dataset tailored for training self-supervised models, laying the groundwork for advancing dolphin communication research and developing models that capture fine-grained acoustic structure within species.

---


### 724. [Nociception as a Control Primitive: Afferent Channels and Nociceptive Memory for Agents Deployed in One Body](https://arxiv.org/abs/2609.34840)

**<font color=#1a73e8>作者：</font>** Wolfgang Maass  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent deployed in a single body cannot learn how fast that body wears, because every trial that would reveal its wear resistance wears the body it would protect. We study this \emph{epoch-one} setting, in which the parameters of a fixed-weight policy are set before the body is drawn and never updated in life. The agent carries a load-gated nociceptive channel and a memory that retains what was felt. We prove that felt cost moves the allocation to the best-\emph{paid} work not yet felt rather than the gentlest, that an agent without retention never sees the felt-cost constraint bind, and that the channel pays only where the threat is individually unpredictable, cheap to avoid and expensive to ignore. We measure per body, setting the agent with channel and memory against the same individual without them, where neither carries a schedule learned across lives. On $2{,}000$ simulated floor-layer knees, with wear anchored to published loss rates, feeling, retaining and substituting extends the working life from age $55.2$ to $59.6$ and raises career output from $33.7$ to $36.1$. $69.3\%$ of bodies gain and \textbf{none lose}. A body that feels but retains nothing past the day gains one of the $+4.4$ years, and retention carries the rest. A population-trained agent gains $+0.65$ years from the same channel at $-0.54$ output. The difference is what a species prior already supplies, and a single body has none. The two are related by an identity, the ablation mean reporting $(1-\chi)$ of the per-body value with $\chi$ the share a blind schedule already captures, so we report both. Where the regime map predicts value, a care robot sextuples its certified service life and a field-anchored fleet writes off $0.15$ of its machines instead of $0.55$. Where it predicts none, a rover gains little over blind caution, so the map holds in both directions.

---


### 725. [ORAV: Benchmarking Audio-Video Generation from Multimodal Contexts](https://arxiv.org/abs/2609.34843)

**<font color=#1a73e8>作者：</font>** Jiacheng Hua, Xiaokun Feng, Jiaqi Hua 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-video generation using heterogeneous multimodal references has emerged as a new challenge, requiring both compositional control over generation and grounded understanding of multimodal context. In this paper, we introduce ORAV Bench for Omni Reference Audio-Video Generation, comprising 380 task instances with 2-10 references, 9 semantic roles, and 30 role compositions. Instructions specify the relationships among references; the media supply the identities, dynamics, and audio characteristics to be realized. To evaluate these open-ended outputs, we develop a reference-aware pairwise protocol that prepares visual and auditory evidence, compares the intended contribution of each reference, and checks the overall verdict in both presentation orders. On held-out instances, it achieves 86.08% effective agreement with human judgments. Across 5 frontier systems, overall rankings conceal distinct strengths across reference compositions. A recurring failure is to reproduce unintended source content in place of the requested result, despite closely resembling a reference. Reproducible pointwise diagnostics of quality, reference affinity, and speech reveal distinct dimensions of model behavior. ORAV thus offers a benchmark for tracking progress toward controllable, compositional, and reference-faithful audio-video generation.

---


### 726. [Context-dependent time-series prediction via HyperReservoirs](https://arxiv.org/abs/2609.34847)

**<font color=#1a73e8>作者：</font>** Kohei Tsuchiyama, Takatomo Mihana, Ryoichi Horisaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series prediction is a common application of reservoir computing. When the training and testing time series data contains multiple dynamical regimes, because an underlying parameter is changing, or the data in fact consists of multiple distinct systems, simple application of the reservoir computing principle produces high prediction errors. Here, we propose a HyperReservoir as an extended model of reservoir computing especially designed for such cases. The HyperReservoir combines a main reservoir with a smaller context reservoir, where the latter modulates the output weights of the former. This structure resembles the hypernetworks from deep neural network literature. However, in contrast, HyperReservoirs retain the simple training via linear regression of standard reservoir computing. We compare the proposed architecture with a conventional ESN, in which context acts at the input, and a full-matrix Conceptor, in which context modulates the reservoir state space. We evaluate all three models on time-series prediction tasks based on Lorenz and Rössler systems, including for varying bifurcation parameters and time sampling scales. We find that the HyperReservoir achieves the lowest mean test error in all three tasks, and particularly outperforms conceptors on data that is sampled from the same attractor but at different time scales.

---


### 727. [From Soft Targets to Reward Signals: How Assignment and Reward Objectives Interact](https://arxiv.org/abs/2609.34850)

**<font color=#1a73e8>作者：</font>** Jiangtao Lin, Bangyang Wei, Siyi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Soft preference targets specify supervision strength, and reward objectives convert that strength into learned reward signals. A central design question remains: how does assigning a fixed set of preference strengths to different response pairs change the rewards produced by different objectives? We introduce assignment geometry to study this interaction. Mean-matched smoothing controls target dispersion, while within-stratum reassignment changes correspondence and preserves the complete target distribution. Across five reward objectives, intact correspondence retains the largest clean preference margins among the compared soft targets within a common accuracy-equivalence budget. Attenuation orderings change with the reward objective, revealing different responses to the same target assignments. Independent reassignments and a related source construction reproduce the retention direction. An attenuation-retention profile compares these combinations through margin magnitude, edit response, and accuracy. Against independently calibrated scaling, APLOT uniform targets deliver additional attenuation on both aggregate and presentation edits. These findings establish a joint design space in which target placement and reward objective shape reward properties beyond preference accuracy.

---


### 728. [EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853)

**<font color=#1a73e8>作者：</font>** Sungho Moon, Kota Shimomura, Junwoo Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene understanding enables object localization and segmentation from free-form text queries without a fixed category vocabulary. Many recent methods build on 3D Gaussian Splatting and consolidate multi-view observations, such as masked crops from individual views, into language features or compact object descriptors before the query is known. However, observations of the same object vary across viewpoints and are not equally informative: some reveal cues relevant to a particular query, whereas others provide incomplete or misleading evidence. Pre-query consolidation can therefore suppress cues on which a later query depends. We introduce EviSplat, which preserves individual observation features as evidence for later text queries. EviSplat retains individual observation features within class-agnostic 3D instances that represent objects, object parts, or background regions. It also learns, for each Gaussian, a distribution describing which visual appearances its observations support. Given a text query, EviSplat scores each instance using its most relevant observations. It then computes a score for each Gaussian by combining instance-level relevance with locally supported evidence, weighted by how often and how unambiguously that Gaussian was observed. Different queries can thus draw on different visual cues from the same preserved evidence. Experiments across diverse datasets and evaluation protocols demonstrate state-of-the-art performance, supporting the benefit of preserving multi-view evidence until query time and aggregating it according to the query.

---


### 729. [AUV-Bench: Aesthetic Understanding and Generation Evaluation for User Interfaces](https://arxiv.org/abs/2609.34854)

**<font color=#1a73e8>作者：</font>** Zhijie Deng, Ling Li, Junhao Ji 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal foundation models are increasingly used for evaluating and generating user interfaces (UIs), often producing seemingly reasonable aesthetic judgments and visually plausible pages. However, under professional design scrutiny, their behavior can differ substantially from that of human designers. In professional design practice, designers rely on a systematic set of aesthetic principles that consistently guide judgment, diagnosis, repair, and creation. A coherent aesthetic capability should therefore connect aesthetic judgment with design actions. Existing evaluations, however, typically assess these abilities in isolation, making it difficult to determine whether task-level success reflects a shared aesthetic understanding or merely fragmented task-specific competence. To address this gap, we introduce AUV-Bench, developed in collaboration with professional UI designers around 1,395 executable web interfaces and four tasks: aesthetic scoring, diagnosis, repair, and text-to-UI generation. The tasks share a pool of UIs and aesthetic principles, with diagnosis and repair further aligned on 660 controlled-degradation instances to enable instance-level analysis of judgment and action. Evaluation of 12 models reveals a capability imbalance: models show moderate agreement with professional designers in holistic aesthetic scoring, yet exact diagnosis-chain success peaks at only 24.7%. On the aligned diagnosis-repair cases, correct judgments and successful repairs do not consistently coincide, exposing a Judgment-Action Gap between identifying aesthetic problems and successfully acting on them. In open-ended generation, even leading models achieve only moderate aesthetic quality under human-calibrated evaluation. Overall, current models exhibit partial aesthetic competence, but still lack the fine-grained understanding and judgment-action coherence required for reliable UI design.

---


### 730. [Attention-based Hierarchical Variational Information Bottleneck for Robust Multi-Agent Communication under Variable Bandwidth](https://arxiv.org/abs/2609.34860)

**<font color=#1a73e8>作者：</font>** Lukas Koch Vindbjerg, Qi Zhang, Yury Brodskiy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based multi-agent communication under limited bandwidth does not only require deciding what to communicate, but also structuring messages so that partial transmissions remain useful. We study this problem under prefix truncation, where only the first part of each message is received. To address it, we propose \textbf{AH-VIB}, an attention-based autoregressive variational communication model that combines a variational information bottleneck (VIB) with sequential message generation and a hierarchical robustness loss. We evaluate AH-VIB on a custom cooperative object-inspection and occupancy-mapping task, where agents equipped with a limited field-of-view sensor coordinate to scan inspection objects in an occupancy-grid world, under variable and fixed bandwidth conditions, and compare it against MADDPG, CommNet, a flat VIB baseline, and an autoregressive MLP ablation. AH-VIB achieves competitive mean return while improving performance reliability under the most constrained bandwidth conditions.
These results indicate that AH-VIB improves the reliability and graceful degradation of learned communication under bandwidth constraints.

---


### 731. [SPOC-Net: Single-Primitive Online Composition Network for GNSS Jamming Set Recognition](https://arxiv.org/abs/2609.34875)

**<font color=#1a73e8>作者：</font>** Zhihan Zeng, Kaihe Wang, José A. López-Salcedo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable positioning, navigation, and timing support intelligent transportation, autonomous systems, and space-air-ground integrated networks. However, global navigation satellite system (GNSS) jamming recognizers that treat each mixture as a separate class are difficult to extend to new combinations. Therefore, this paper proposes SPOC-Net, which decomposes the recognition problem into identifying a set of basic jamming components. Multi-resolution time-frequency features and learned component queries provide evidence for each component type. A high-resolution branch estimates the number of active types, and a structured decoder combines this estimate with component evidence to select a valid set. For training, measured single-component records are the only physical samples used in gradient optimization. Their associated clean in-phase and quadrature (IQ) sequences are combined on demand during training to produce labeled mixtures with different relative powers and jamming-to-noise ratios. Separate measured mixtures from ten training-listed compositions support model selection and decoder calibration; six other compositions are reserved for final testing. Evaluation on 14,220 independently generated, conductively combined, and recorded radio frequency mixtures yields 80.69% exact-set accuracy and a 92.84% micro-averaged F1 score. On combinations excluded from model development, SPOC-Net achieves 80.89% exact-set accuracy, exceeding the strongest comparison method by 18.77 percentage points under the reported protocols.

---


### 732. [ECHO: Event-Augmented Context with Hindsight and Outlook for Wrist-Only Manipulation](https://arxiv.org/abs/2609.34893)

**<font color=#1a73e8>作者：</font>** Xinyue Wang, Yicheng Jiang, Zesen Gan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based manipulation policies relying on RGB cameras often suffer from degraded observations under extreme exposure. Event cameras mitigate this degradation by asynchronously detecting pixel-level intensity changes to offer a high dynamic range. However, their observations heavily depend on camera placement, as fixed cameras miss static scene content while wrist-mounted camera motion causes previously visited regions to leave the field of view. To address these spatial-temporal limitations, we present ECHO (Event-augmented Context with Hindsight and Outlook), a wrist-only latent world action model that encodes wrist events into compact motion representations to provide temporal and spatial context for policy reasoning. Specifically, ECHO utilizes a pretrained event encoder to explain visual-feature changes between frames. Its hindsight module preserves the gripper trajectory with past event stream as addressable off-camera context. Concurrently, the outlook module introduces learnable event foresight queries supervised to anticipate the event window for future actions, enabling the policy to predict upcoming scene changes. Evaluated on wrist-only RLBench tasks, ECHO outperforms RGB and RGB+event baselines by 20.6 and 12.0 percentage points under normal lighting, and by 14.6 and 11.3 points under severe exposure drops, respectively, while also surpassing RGB references using a third-person camera. Real-world experiments with a wrist-mounted event camera validate that ECHO outperforms RGB-only and RGB+event baselines across multiple tasks under both nominal and severely dark lighting. Project page is at this https URL.

---


### 733. [LVMT: Video Mask Transformer for Long-term Video Segmentation](https://arxiv.org/abs/2609.34895)

**<font color=#1a73e8>作者：</font>** Narges Norouzi, Niccol`o Cavagnero, Idil Esen Zulfikar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing online video segmentation methods struggle to track objects in long, complex videos with long-term occlusions. We hypothesize that this limitation is caused by (i) the inability of their temporal propagation mechanism to adaptively select the object information that is propagated across time, and (ii) their inability to be trained on long videos due to memory requirements and vanishing gradients. To address the first limitation, we propose to use a lightweight GRU-based temporal propagation module that can learn to select which information it keeps in memory and propagates across time. Second, to allow training on long videos, we introduce Truncated Query Propagation (TQP), a training strategy in which the model processes a video in chunks of frames, where information about tracked objects is propagated between chunks but backpropagation is only conducted in individual chunks, enabling longer temporal supervision without out-of-memory issues, inference overhead, or vanishing gradients. The resulting model is called the Long-term Video Mask Transformer (LVMT). Extensive experiments on six benchmarks show that LVMT sets a new state of the art across a range of video segmentation tasks, while retaining the speed of the highly efficient model it is based on, making it 10X faster than the prior state of the art. Code: this https URL

---


### 734. [FILIGREE3D: Scaling Sparse Latent Flow Matching for Ultra-High-Resolution Image-to-3D Generation](https://arxiv.org/abs/2609.34900)

**<font color=#1a73e8>作者：</font>** Hongjie Li, Xinran Yang, Xiuchao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling image-to-3D generation to ultra-high resolutions requires controlling rapidly growing computational costs without sacrificing fine geometric detail. We present \textbf{Filigree3D}, a sparse latent flow-matching framework that generates 3D geometry from a single image at voxel resolutions up to $2048^3$, with straightforward extensibility to $4096^3$. To make training tractable, we introduce Structure-Aware Sparse Scaling, which combines spatial bounding with alternating local-global attention to constrain token growth while preserving both fine-scale details and long-range structural context. To enhance detail reconstruction, we curate training samples based on their high-resolution geometric gains and inject multi-scale image features into a sparse 3D DiT, effectively coupling structural semantics with fine-grained visual cues. Furthermore, a visibility-aware voxel regularization strategy improves robustness against sparse perturbations and facilitates the completion of unobserved geometry. Under our default configuration, Filigree3D maintains peak GPU memory consumption within practical limits for contemporary hardware, enabling the generation of highly intricate 3D geometry in approximately one minute. Extensive experiments demonstrate that our method yields substantial improvements in overall geometric fidelity and fine-detail preservation compared to existing baselines, validating practical, detail-preserving 3D generation at unprecedented resolutions.

---


### 735. [Reference-Tail Trust:Certified Probability Floors for Learned Updates Inside a Deployed Network](https://arxiv.org/abs/2609.34904)

**<font color=#1a73e8>作者：</font>** Abdolvahab Khalili Sadaghiani, Jose Nunez-Yanez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) need to exploit improved message passing without surrendering control over predictions already trusted in deployment. We introduce Reference-Tail Trust (RTT), a framework that admits learned updates inside a frozen GNN and certifies the prediction actually served. RTT couples graph-based proposal states with a constrained internal optimizer: each displacement is charged for its worst-case terminal cross-entropy increase through the incumbent's remaining message-passing layers. A trajectory-validated tube and an independent checker enforce per-node probability floors, $p^{\mathrm{s}}_{ic} \ge e^{-H_{\mathrm{row}}} p^{\mathrm{r}}_{ic}$, and a call-level budget, $\sum_i w_i D_\infty(p^{\mathrm{r}}_i \| p^{\mathrm{s}}_i) \le H^+$, uniformly over labels. Calls whose adapted outputs pass certification require no separate full incumbent rollout; failed certificates trigger whole-call fallback. We derive the exact probability-floor frontier by water-filling, characterize architecture-constrained efficiency, and establish conditions under which internal propagation exploits evidence unavailable to restricted output correctors. In the reported ogbn-arxiv audit, RTT achieves $6.5\times 10^{-3}$ nats of mean gain per call, with a one-sided 95% regression-rate upper bound of 0.95% and a 95% negative-flip upper bound of 0.51% on the uninspected part of the reserved node population. Its mean gain is 61% of a cross-fitted posterior-based frontier estimate and exceeds the strongest matched one-pass corrector by $+0.9\times 10^{-3}$ nats. Reported experiments span eight proposals, six graph-incumbent families, structural and temporal graph shifts, and molecular prediction, with additional image and tabular evaluations. RTT makes GNN adaptation a budgeted, certifiable inference decision rather than an unconditional model replacement.

---


### 736. [RISE: Red-teaming via Iterative Strategy Evolution for Modern Text-to-Image Models](https://arxiv.org/abs/2609.34920)

**<font color=#1a73e8>作者：</font>** Dmitrii Kharlapenko, Sergei Bratchikov, Konstantin Korolev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On modern production text-to-image systems, successful policy violations are rare, and previously effective human-written seeds are often patched out. Current automated red-teamers are poorly matched to this regime in two ways: unreliable success measurement and poor exploration. First, we find that judges widely used in prior T2I red-teaming work are unreliable under vague unsafe-content targets: they either miss true violations or reward benign borderline images on hardened APIs. We therefore define strict category-specific success criteria and calibrate strong VLM judges against human labels. Second, we show that broadly used prompt-modification pipelines do not solve the exploration problem: on harder guardrail settings they remain tied to seed prompts, fail to transfer, or cannot bootstrap positive examples. We introduce RISE, which evolves reusable strategies used to generate prompts rather than rewriting them one by one. The best discovered strategies are then reused to generate attacks across new scenarios. On DALL-E 3, Nano Banana 2 (Google) and GPT-Image-2, RISE reaches up to 13% human-verified ASR; under the same calibrated evaluation, prior methods with reported ASR as high as roughly 30% fall to near zero.

---


### 737. [TaoTex: Boosting Texture Detail Fidelity for Native 3D Material Generation](https://arxiv.org/abs/2609.34934)

**<font color=#1a73e8>作者：</font>** Xiuchao Wu, Shuichang Lai, Jiangjing Lyu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D generation models can produce accurate geometries while still struggling to reconstruct detailed textures. We propose a diffusion-based native 3D material generation model TaoTex, which faithfully recovers intricate textures through tailored strategies and improvements. First, we develop a data construction agent to create high-frequency textured 3D assets to bridge the data gap in public datasets. Training with these data significantly enhances the ability of TaoTex to recover challenging details such as text and patterns. Second, we design a multi-level feature fusion (MLFF) module to adaptively integrate local and global features of the conditional input, providing more complete texture cues for the diffusion model and thereby enhancing reconstruction fidelity. To alleviate VAE reconstruction errors, we adopt a latent-to-pixel space loss transition, further improving the pixel-level details and generation quality. Finally, we scale TaoTex to multi-view inputs by incorporating learnable viewpoint embeddings, achieving accurate and consistent material reconstruction across views. Extensive experiments demonstrate that our method significantly outperforms existing approaches in preserving texture details in both single- and multi-view settings.

---


### 738. [XMatch: Enhancing Covariate-Aware Time Series Forecasting through Tree-Structured Exogenous Matching](https://arxiv.org/abs/2609.34939)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Hanyin Cheng, Xiangfei Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future exogenous variables provide valuable information for forecasting endogenous time series. Existing covariate-aware methods primarily learn the direct influence of exogenous variables on endogenous variables. However, these effects can be complex and change with the pattern of the exogenous variables, making them difficult to capture. Beyond this perspective, we observe that a given exogenous pattern often co-occurs with only a small set of endogenous response patterns. These associations motivate a strategy that matches future and historical exogenous patterns and uses the corresponding endogenous patterns to enhance forecasting. However, in real-world forecasting scenarios with multiple exogenous variables, each exogenous variable provides a distinct dimension for matching, creating a dilemma for this strategy between precise matching and sufficient historical support. To bridge this gap, we propose XMatch (EXogenous MATCHing), a covariate-aware forecasting model that realizes the aforementioned strategy through a tree-structured matching process that adaptively adjusts the number of exogenous variables used as matching conditions. Specifically, we first introduce the ProtoTree Creator, which organizes historical correspondences between exogenous and endogenous patterns into a ProtoTree, whose deeper levels incorporate additional exogenous variables for matching. For forecasting, we then design the ProtoTree Matcher, which uses future exogenous variables to query the ProtoTree and adaptively determines how many exogenous variables to use for matching based on exogenous pattern similarity and historical support. Finally, the matched endogenous patterns are used as explicit historical evidence to enhance forecasting. Extensive experiments on 12 real-world datasets demonstrate that XMatch outperforms state-of-the-art baselines.

---


### 739. ["Black Mirror?": Public Sensemaking of AI-Powered Lifelogging](https://arxiv.org/abs/2609.34950)

**<font color=#1a73e8>作者：</font>** Ying Ma, Jarod Govers, Le Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-powered lifelogging wearables are emerging as a new class of consumer devices that transform everyday experience into searchable, AI-curated memory archives. We study early public sensemaking around these systems at the moment of their market entry, using the Looki L1 as an empirical lens. Analysing large-scale Chinese-language and English-language social media discourse (N = 5,053 comments), we combine topic clustering with inductive thematic analysis to examine how users interpret the social, moral, and political implications of AI-mediated memory. Across contexts, users reference dystopian surveillance imaginaries, express privacy resignation and bystander concerns, and debate assistive value alongside consumer logics. English-language comments more often framed these devices through interpersonal power, evidentiary use, and hacking anxieties, while Chinese-language comments more often foregrounded labour exploitation, governance surveillance, and technological inevitability.

---


### 740. [AX is the New AEO](https://arxiv.org/abs/2609.34951)

**<font color=#1a73e8>作者：</font>** Ido Finder, Assaf Elovic, Gad Shalev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In 2023, AI models answered from training data and hallucinated when it ran out, and businesses were told to seed that knowledge. Models' training knowledge has since given way to live web search, and the advice followed it there: answer-engine optimization, or AEO, now tells businesses to scatter breadcrumbs across forum threads, listicles, and off-site citations, so AI engines are likelier to surface and recommend them. But being surfaced is no longer enough: an agent opens the results and reads them before deciding, and one buyer question sends it through several rounds of search and fetch. What decides the outcome at this drill-down step is whether the agent can fetch and read the business's own site: agent experience (AX). We argue that AX is the new AEO. We run 37,927 agent journeys, each a buyer question about a business, across four independent harnesses over 1,056 real businesses, matched on fame, prior model knowledge, and two AEO proxies, then split based on their AX level. Only 7-10% of the finished answer comes from the model's training knowledge, whether or not the site is readable. Agent-ready businesses have answers built from their own pages 78% of the time against 56% and are clearly recommended 1.9x more often, while every grounded answer about a not-agent-ready business costs the agent 64% more. Holding business, harness, and question fixed, answers built from the site are 41% more accurate. The dominant failure is not fabrication but omission: web-built answers are 3.7x more likely to contain none of the facts the buyer asked for. Baselines differ sharply across the four harnesses, with clear-recommendation rates varying sevenfold from stack to stack, yet the effect holds in every one. In the agentic web era, being readable beats being talked about, and improving a site's AX is the strongest lever a business has.

---


### 741. [From Early Participation to Later Completion: Evidence from a Large-Scale Self-Paced Learning Programme](https://arxiv.org/abs/2609.34953)

**<font color=#1a73e8>作者：</font>** Sakshi Sharma, Pavani Ayinampudi, Aditya B.M.V. 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large-scale learning programmes generate records that make learner participation observable across different activities. Participation points are commonly used to record and encourage such participation, but their value may extend beyond the activities for which points are awarded. Existing evaluations often examine gamification outcomes within the activities or learning environments in which the game elements are implemented, providing limited evidence about whether early participation points contain information about later participation outside the points system. This study examines whether early participation points can provide information about learners' later participation in a self-paced learning track that does not award participation points. Using anonymised records from 876 learners in a large-scale remote software-upskilling internship, we examined participation points generated from live-session attendance and poll responses against later self-paced course completion. The primary analysis used the 438 learners who earned at least one point during the first week, while the full cohort was retained for the no-point analysis. Week-one participation points distinguished learners who later completed a self-paced course with an AUC of 0.89, increasing to 0.95 by the fourth week. Similar AUCs were observed at both stages of the self-paced course sequence, while the absence of week-one points identified learners who did not start or did not complete a self-paced course with 95% precision. These findings indicate that early participation points can provide information about later participation outside the activities that generate the points. Such information can help large-scale learning programmes identify learners who may require timely attention while learning is still in progress, without treating participation points as a measure of overall learner engagement.

---


### 742. [ALICE: In-context, Zero-shot, Mutual Information Estimation](https://arxiv.org/abs/2609.34962)

**<font color=#1a73e8>作者：</font>** Giulio Franzese, Simone Rossi, Pietro Michiardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating mutual information (MI) from samples is a central objective in a variety of scientific fields. Modern neural estimators are accurate in the large-data regime, but they fall short when data is scarce, and each must be fit anew for every distribution under study. Current estimators are moreover tied to specific data types. These constraints limit their adoption in many applications where per-distribution training is impractical and sample sizes are small.
We present ALICE, a foundation model that removes per-distribution training, while achieving competitive estimation accuracy. Trained exclusively on a broad family of synthetic distributions, ALICE acts as an in-context estimator of rectified-flow velocity fields: conditioned on samples of an unseen distribution, it estimates that distribution's velocity field without any explicit training. MI is then obtained through a fixed identity that integrates the squared difference between the joint and conditional fields. We validate ALICE on a standard, challenging benchmark and apply it in three domains, biology, genetics, and neuroscience, whose data the model has never seen. For the first time, we show that a single model closes the gap with neural estimators trained separately for each distribution, while natively supporting different data dimensionality and sample cardinality, enabling zero-shot MI analysis across scientific domains.

---


### 743. [Cyclostationary Phase Conditioning for Medical Time Series Diffusion](https://arxiv.org/abs/2609.34965)

**<font color=#1a73e8>作者：</font>** Samuel Ruiperez-Campillo, Michele Copetti, Jorge da Silva Goncalves 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many physiological time series, such as cardiac and brain recordings, exhibit cyclostationarity: their statistics vary periodically with an underlying cycle phase. Corruption from motion, poor contact, and physiological interference obscures morphology needed for diagnosis, making signal restoration essential. Existing diffusion approaches condition on corrupted observations alone and must learn cyclic structure implicitly. We instead propose two inductive biases which encode cyclostationarity: a shift-covariant wavelet representation and dense per-sample phase conditioning inferred from the corrupted input. We further introduce a training-free cyclostationarity index that quantifies phase structure and predicts when phase conditioning will help. Finally, we propose antithetic coupling of reverse trajectories to reduce sampling variance while achieving comparable performance with fivefold fewer network evaluations. Across modalities, our results show that explicitly encoding measurable cyclic structure improves physiological time-series restoration.

---


### 744. [Safe Greenhouse Climate Control Using Lagrangian-Constrained PPO with Kolmogorov-Arnold Networks](https://arxiv.org/abs/2609.34966)

**<font color=#1a73e8>作者：</font>** Hangzun Liu, Yuling Fan, Fang Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Greenhouse climate control balances economic return with maintaining temperature, humidity and CO2 within crop-adapted growth ranges. Conventional reinforcement learning (RL) greenhouse controllers use fixed reward penalties to limit climate constraint violations, yet such heuristic penalties cannot explicitly constrain long-term cumulative violations. Poorly tuned weights either lead to overly conservative policies and lower yields, or fail to suppress persistent climate deviations that harm photosynthesis and induce crop diseases. To address this issue, we formulate greenhouse climate regulation as a Constrained Markov Decision Process (CMDP) and use a Lagrangian safe RL framework RCPO-PPO to separate economic optimization and cumulative safety constraints, enabling adaptive penalty adjustment without manual tuning. To handle strong nonlinear, time-varying coupling between greenhouse microclimate and crop growth, Kolmogorov-Arnold Networks (KANs) replace Multi-Layer Perceptrons (MLPs) as policy and value approximators for improved nonlinear representation. Sinusoidal cyclic time features are embedded in observations to capture diurnal environmental periodicity. Simulations use a classic winter lettuce greenhouse model driven by 40-day real weather disturbances. Compared with vanilla penalty-based PPO, our method cuts cumulative climate violations by 18.65% and raises lettuce economic profit by 2.91%, keeping violations stable near the safety threshold. This decoupled CMDP optimization with KAN-based policy representation mitigates long-term climate risks and boosts planting profits, offering a constraint-aware control strategy for precision greenhouse cultivation.

---


### 745. [One Sensor, Whole Body - 3D Body Pose from a Single Consumer Earbud IMU](https://arxiv.org/abs/2609.34978)

**<font color=#1a73e8>作者：</font>** Zhilin Guo, Boqiao Zhang, Oszkár Urbán 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consumer earbuds already stream inertial motion data from the head, one of the most widely worn sensor locations on the body. We ask how much of the 3D body pose a single such head IMU can recover, and whether adding more consumer sensors actually helps. We build a multimodal capture pipeline that records four-view RGB-D video together with an AirPods head IMU and two Striv insole IMUs, synchronize the streams post-hoc, and generate pseudo-ground-truth with SAM 3D Body, yielding a 35-take single-subject benchmark spanning gait, turning, vertical, everyday, and clinically inspired motions. Adapting two recurrent model families (IMUPoser and MobilePoser), we show that one head IMU recovers lower-body pose at 79.0 mm rigid-MPJPE and per-foot ground contact at 0.809 macro-F1, and that a causal variant retains most of this accuracy at streaming latency. In paired per-take significance tests across both families, adding the consumer foot IMUs never significantly improves pose and significantly degrades it in two of four model-split combinations; a mounting-bias probe and feet-only ablation identify insole orientation quality, not foot placement, as the mechanism. Extending the output to a 20-joint full-body skeleton maps the boundary: gross distal-arm motion is partially recoverable from the head alone, proximal upper-body pose is not, and staged fine-tuning recovers the leg accuracy that naive joint training sacrifices to multi-task dilution. For learned pose from consumer wearables, sensor reliability, not sensor count, is the binding constraint here. For the devices tested, the earbud is its sweet spot. Code is available at this https URL.

---


### 746. [What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling](https://arxiv.org/abs/2609.34981)

**<font color=#1a73e8>作者：</font>** Renping Zhou, Zanlin Ni, Zihao Fan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) predict the future alongside actions during \emph{training}. Due to the heavy computation cost of video denoising, whether the future must still be generated during \emph{inference} is disputed: Explicit WAMs denoise it into clean frames along with every action chunk, whereas Latent WAMs discard it entirely for acceleration. We find that latent WAMs, despite matching explicit ones on in-distribution tasks, fail to retain the generalization benefits that originally motivated WAMs. To demonstrate this, we evaluate generalization along three axes: \emph{environmental perturbation}, \emph{data efficiency}, and \emph{task generalization}. Controlled comparisons with a matched backbone, training data, and budget reveal consistent degradation across all three axes when the action expert no longer conditions on future representations. Further analysis shows that the gap arises almost entirely from the first denoising step: the benefit comes from \emph{preparing} the future, not \emph{generating} it. We therefore propose \textbf{Simple-WAM}, which simplifies future modeling into a single forward pass of fully noised video tokens and adapts the training-time noise schedule to this inference behavior. Across simulation and real-world tasks, Simple-WAM achieves the best of both worlds, leading explicit WAMs in generalization performance with efficiency comparable to Latent WAMs. Project Page: \href{this https URL}{\textcolor{panton}{\texttt{this https URL}}}

---


### 747. [ORPG: Reconciling Multiple Reward Objectives through Objective-wise Policy Gradients](https://arxiv.org/abs/2609.34985)

**<font color=#1a73e8>作者：</font>** Shicheng Fang, Yiwen Zhao, Wenbo Tian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-reward policy optimization requires a joint update that reflects both the learning signals and the intended relationships among objectives. We introduce Objective-wise Reconciled Policy Gradient (ORPG), which constructs a separate clipped policy objective for each reward and reconciles the resulting gradients into one policy update. For compatible gradients, a cosine-dependent interpolation coordinates their contributions through a partially normalized reference while preserving the norm of their sum. We characterize this update as the unique solution of a spherical directional compromise. For conflicting gradients, projection follows the task's priorities. We evaluate the same compatible rule in helpfulness--safety alignment and correctness--cost optimization for mathematical reasoning. ORPG substantially improves average Useful and Harmless scores over the strongest external baseline on each axis. In mathematics, it achieves the highest average full-budget accuracy and three-budget hypervolume among the compared methods, with more accurate and shorter responses than the initial policy. Component comparisons and training dynamics show the larger contribution of compatible coordination and a complementary benefit from conflict handling. These results support gradient reconciliation for objectives with equal standing and for objectives with an explicit priority.

---


### 748. [Nürnberg NLP at ChildSafeAds 2026: Structurally Dissimilar Voter Ensembles under Four Levels of Data Access](https://arxiv.org/abs/2609.34986)

**<font color=#1a73e8>作者：</font>** Philipp Steigerwald, Eric Rudolph, Jens Albrecht  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the Nürnberg NLP system for ChildSafeAds 2026. The shared task asks what a monitoring system for commercial content in child-facing YouTube videos can achieve at a given level of data access. We answer with per-subtask ensembles of nine voters, organised into three branches that differ in backbone, adaptation method and class scope. Selection rests on channel-disjoint cross-validation, with the development set as a transfer check. The system wins two of the three subtasks. Its product-category score (ST2, 0.8243) and its compliance-flag score (ST3, 0.6530) are the best of the 22 final entries, and it places third on the task mean (0.7079). We further compare four access levels and report the cost at test-set scale.

---


### 749. [The Right Lesson at the Right Step: Deriving Control Updates for Self-Evolving Agents](https://arxiv.org/abs/2609.34988)

**<font color=#1a73e8>作者：</font>** Yunhe Su, ZiYi Dong, Tong Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve future behavior by reusing past experience, typically as global prompts, memories, or reflections. Yet these mechanisms rarely control where experience takes effect. In long tool-use workflows, the same lesson may correct one decision but distract another, making experience reuse a problem of localized control rather than memory alone. We introduce EvoCUE (Evolution through Control Updates from Evidence), a framework for learning reusable control-program updates from completed agent executions. EvoCUE represents the agent as an explicit state-machine controller, whose nodes perform model or tool calls and whose edges define where control passes next. This makes the workflow editable at precise locations, so each learned update can specify what to add, where it acts, and when it applies. From completed trajectories, EvoCUE uses residual goals and observed execution traces to propose localized instruction or skill edits. Each candidate is evaluated at the point where it would act by resuming the parent and edited controllers from the same checkpoint and comparing their final outcomes. Accepted edits are compiled with applicability rules, confirmed on held-out tasks, and inherited by later executions. We evaluate EvoCUE on long tool-use environments where learned conventions must reach the right execution step. From a minimal AppWorld controller without benchmark-specific onboarding instructions, EvoCUE learns the missing task-completion convention and substantially improves success on Test-Normal and Test-Challenge. On PAST-Bench office workflows, EvoCUE transfers organizational requirements from prior episodes to later tasks, improving task-execution quality. These results show that self-evolving agents should place experience inside the control flow, rather than only store it as text.

---


### 750. [Price Stability in the European Union: A Systemic Approach Using Random Matrix Theory](https://arxiv.org/abs/2609.35011)

**<font color=#1a73e8>作者：</font>** Sami Diaf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Price stability remains a pillar in monetary policy practices and carries a special importance within monetary unions. Mainstream economics tried to leverage price stability using price indices and several metrics to shed light on specific dynamics and optimal macroeconomic levels. The wide availability of data led researchers to consider the study of systems using Random Matrix Theory, based on inner correlation patterns. This aims to enhance the multivariate analysis by removing noisy patterns from the signal and improve data quality for further inferences. This work considers the collection of monthly inflation indices in the Eurozone as a \textit{system} of prices to analyze its eigenvalues' statistical and asymptotic properties and uncover inner country-level insights. Results confirm the system cannot assumed to be randomly generated, and the data exhibit noise-dominated patterns, due to small and persistent variations at the country-level. The latter make the inter-country correlations more dynamic and the separation of the signal from the noise quiet difficult. Findings identified two countries as distorting inflation dynamics besides three other distinct, regional-based groups of countries. Variability sources might stem from economic episodes fueling inflation spikes in some countries, as well as methodological aspects used to ensure data quality and representativeness in the European Union. Despite being complex, the system demonstrates a certain stability, in terms of self-organization; while large monthly fluctuations cannot be considered as rare events, but part of the data-generating process.

---


> [!TIP]
> 当前位于：**701-750**（第 15/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | **701-750** | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
