# 📦 其他研究 | 2026年06月05日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-265**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-265**

---

### 251. [ZipSplat: Fewer Gaussians, Better Splats](https://arxiv.org/abs/2606.05102)

**<font color=#1a73e8>作者：</font>** Alexander Veicht, Sunghwan Hong, Dániel Baráth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting methods reconstruct a scene from posed or pose-free images in a single forward pass, yet current approaches predict one Gaussian per input pixel, tying the representation budget to camera resolution rather than scene complexity. A flat wall and a richly textured object thus produce equally many Gaussians despite very different geometric needs. We propose ZipSplat, a token-based feed-forward model that decouples Gaussian placement from the pixel grid. A multi-view backbone extracts dense visual tokens, and k-means clustering compresses them into a compact set of scene tokens. Cross- and self-attention refine these tokens, and a lightweight MLP decodes each into a group of Gaussians with unconstrained 3D positions. Because clustering is applied at inference, a single trained model spans the quality-efficiency curve without retraining. ZipSplat operates without ground-truth poses or intrinsics, yet sets a new state of the art on DL3DV and RealEstate10K with ${\sim}6{\times}$ fewer Gaussians than pixel-aligned methods, surpassing the best pose-free baseline by 2.1dB and 1.2dB PSNR, respectively. It further generalizes zero-shot to Mip-NeRF360 and ScanNet++, outperforming all comparable baselines. Our project page is at ${\href{this https URL}{this https URL}}$.

---


### 252. [Identifying Gems from Roman RAPIDly](https://arxiv.org/abs/2606.05103)

**<font color=#1a73e8>作者：</font>** Karan Gandhi, Ashish A. Mahabal, Jacob E. Jencson 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Nancy Grace Roman Space Telescope (Roman), set for launch as early as September 2026, will conduct wide-field infrared imaging surveys with unprecedented spatial resolution and cadence, enabling the discovery of millions of astronomical transients. Hence, it is necessary to have automated pipelines for generating alerts in place so that the telescope can begin discovering reliable transients and variable objects soon after it is launched. However, no real Roman data currently exist, making the development of such pipelines difficult. In this work, we present a machine learning model $RuBR$ and a general methodology for distinguishing genuine transient and variable detections from spurious (bogus) detections within the RAPID pipeline. In particular, we present three models using this methodology: $RuBR_{comb}$ trained and tested on combined locally injected and OpenUniverse2024 transients, $RuBR_{loc}$ trained on locally injected transients and tested on OpenUniverse2024 transients, and $RuBR_{DA}$ that combines locally injected transients with a fraction of OpenUniverse2024 transients in domain-adaptation mode for training. This paves the way for strategies to adapt the $RuBR_{comb}$ model to real observations in the absence of any ground-truth labels during the early phases of the Roman mission. While the image differencing pipeline continues to be improved, our experimental results demonstrate the effectiveness of the proposed approach and its promise for robust real-bogus classification in the Roman era.

---


### 253. [Continual Visual and Verbal Learning Through a Child's Egocentric Input](https://arxiv.org/abs/2606.05115)

**<font color=#1a73e8>作者：</font>** Xiaoyang Jiang, Yanlai Yang, Kenneth A. Norman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Children learn the meanings of words from a continuous, temporally structured stream of egocentric experience. Recent work shows that neural networks can also learn word-referent mappings from a child's egocentric video recordings, but they cycle through the shuffled data for hundreds of epochs, contrasting with how children actually encounter their environment. We introduce BabyCL, a continual multimodal learning framework that processes the SAYCam dataset in a single chronological pass, combining streaming visual representation learning with an image-text contrastive objective. BabyCL combines a multi-stage temporal segmentation of the stream with a dual replay buffer that independently manages visual and multimodal histories, and it is jointly trained with three contrastive losses on a shared backbone. Under a matched optimization budget, BabyCL outperforms streaming learning baselines on the SAYCam Labeled-S 4AFC benchmark, substantially narrowing the gap to an upper bound of offline training. Ablations show that the gains are robust to the length of the online temporal segmentation window and the eviction rule of the replay buffer. Together, these results show that meaningful word-referent mappings can emerge under training conditions much closer to a child's actual experience.

---


### 254. [Graph Set Transformer](https://arxiv.org/abs/2606.05116)

**<font color=#1a73e8>作者：</font>** Jose E. Escrig Molina, Baoquan Chen, Daniel Probst  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Graph Set Transformer (GST), a neural network architecture for learning on sets of graphs, designed for tasks in which per-element predictions depend on set-wide context as well as local structure. Existing architectures, including DeepSets and SetTransformer, require pre-encoded graph embeddings from a separate GNN, creating a bottleneck between feature extraction and set-level contextualisation. In contrast, GST interleaves node-level feature propagation and cross-graph contextual modelling at every layer, fusing the two levels of information through a gating mechanism. We evaluate GST on a controlled synthetic suite designed to isolate set-conditional structural reasoning and on three real-data benchmarks spanning per-atom reaction-centre identification, reaction yield prediction, and image classification. Under matched parameter budgets, GST performs better than the baselines across these settings. An architectural ablation strongly suggests that the interleaving of local and set context contributes substantially to this advantage.

---


### 255. [A-Live: Passive Liveness Detection via Neuromuscular Micro-Motion Signatures on Commodity Sensors](https://arxiv.org/abs/2606.05126)

**<font color=#1a73e8>作者：</font>** Mohammed Gharib, Sam Burns, Martin Zizi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Liveness detection has evolved from a safeguard against presentation and replay attacks in biometric authentication to a broader requirement for distinguishing human users from non-human agents in modern digital systems. The emergence of generative and agentic AI further amplifies this need, positioning liveness as a fundamental security primitive. Existing approaches face key limitations, including reliance on explicit user interaction, specialized hardware, vulnerability to increasingly realistic spoofing, and limited scalability in real-world deployments. We present A-Live, a passive liveness detection framework that operates solely on inertial measurement unit (IMU) signals available in commodity devices. A-Live is based on the observation that neuromuscular micro-motions inherent to human motor control produce subtle but measurable signatures in inertial data, which are often treated as noise in prior work. We design a lightweight feature extraction pipeline and a compact classifier suitable for real-time on-device deployment, and introduce a controllable physical micro-motion platform to evaluate robustness against engineered non-human motion. Extensive evaluation across Android and iOS devices, including both automated and real-user settings, shows that A-Live achieves over 99.5\% accuracy with low false acceptance and rejection rates. Our results demonstrate that neuromuscular micro-motion signatures provide a scalable and passive foundation for liveness detection under emerging AI-driven threat models.

---


### 256. [Preserving Data Privacy in Learning Causal Structure with Fully Homomorphic Encryption](https://arxiv.org/abs/2606.05129)

**<font color=#1a73e8>作者：</font>** Jian Yang, Yuan Tong, Qinbin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Preserving data privacy is an important topic in structural data management and data mining. However, the issue of privacy leakage in distributed causal structure learning is a persistent challenge, especially in cases where data transmission and computation are required. In this paper, we propose a method based on fully homomorphic encryption (FHE) that performs calculations on ciphertexts, keeping data encrypted in transition and computation. Nevertheless, adopting FHE to causal structure learning is challenging due to the high computation cost and limited support on division as well as logarithm operations in FHE. To tackle this challenge, we propose a series of novel techniques including (i) circuit simplification for better efficiency, (ii) approximation of division and logarithm through Newton-Raphson Reciprocal and Taylor expansion, and (iii) a batching technique with SIMD-acceleration to enhance the whole learning process. Additionally, our method can be easily extended beyond FHE by demonstration of its portability to support differential privacy. Empirical results show that our method achieves high consistency and comparable causal structure with the plaintext version in the datasets tested. Last, our method is efficient and practical to complete learning causal structures in tens of minutes even under the privacy protection of FHE.

---


### 257. [Deep Embedded Multiplicative DMD for Algebra-Preserving Koopman Learning](https://arxiv.org/abs/2606.05131)

**<font color=#1a73e8>作者：</font>** Kelan Gray, Finlay Brown, Nicolas Boullé 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Koopman theory turns nonlinear dynamics into a linear spectral problem. In computation, however, everything depends on a hard finite-dimensional choice: the observables must be expressive, nearly invariant under the dynamics, and, ideally, compatible with composition. Deep Koopman methods learn flexible coordinates, whereas structure-preserving methods enforce operator identities on fixed dictionaries. We combine these ideas by introducing Deep Embedded Multiplicative Dynamic Mode Decomposition (DeepMDMD), a method that learns a latent space and a partition of it, while enforcing the Koopman product rule as an exact algebraic constraint. Training alternates between an exact multiplicative operator update and a differentiable latent-clustering step that promotes Koopman closure. The result is a finite transition map on learned latent cells. Its nonzero spectrum lies on the unit circle, its dictionary is shaped by the dynamics rather than by ambient geometry, and forecasts are made in latent coordinates before being decoded to physical space. Across Hamiltonian, chaotic, and fluid examples, DeepMDMD learns dictionaries that are far more compact and dynamically coherent than those produced by geometric MDMD partitions. It reduces spectral pollution, reveals richer continuous-spectrum structure, and gives stable forecasts under severe noise. In high-dimensional flows, including a 158,624-dimensional cylinder wake and a noisy $Re=20,000$ lid-driven cavity, it preserves coherent structures and long-time spectral statistics where state-space MDMD fails. These results suggest a practical rule for Koopman learning: learn the coordinates, constrain the algebra.

---


### 258. [Generating Financial Time Series by Matching Random Convolutional Features](https://arxiv.org/abs/2606.05138)

**<font color=#1a73e8>作者：</font>** Konrad J. Mueller, Nikita Zozoulenko, Ben Wood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating realistic financial time series is challenging as training data is often limited to a single historical path. With such scarce data, overfitting is hard to avoid, especially under adversarial training where a trained discriminator can memorize the training samples. To mitigate this, recent approaches train generators to minimize the discrepancy between untrained feature representations of real and generated time series. In these works, the feature maps are based on path signatures, which can fail to capture relevant time series properties at tractable truncation depths. In this work, we instead train generators by matching random convolutional features of real and generated time series. Existing random convolutional feature maps, such as Rocket and Hydra, have been shown to provide informative representations of real-world time series, but cannot supervise generative models because they are non-differentiable. We introduce SOCK (SOft Competing Kernels), a fully differentiable random convolutional feature map, suited to train generative time series models. We show that generators trained by matching random SOCK features consistently outperform signature and diffusion baselines across a wide range of small-sample financial datasets. We further demonstrate SOCK's expressiveness on two-sample hypothesis testing and time series classification tasks, where SOCK matches or outperforms existing unsupervised feature maps.

---


### 259. [BBOmix: A Tabular Benchmark for Hyperparameter Optimization of Unsupervised Biological Representation Learning](https://arxiv.org/abs/2606.05139)

**<font color=#1a73e8>作者：</font>** Luca Thale-Bombien, Jan Ewald, Ralf König 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of high-throughput sequencing has led to large, high-dimensional omics datasets. Deep unsupervised learning architectures, particularly Autoencoders (AEs), are increasingly used for dimensionality reduction and representation learning in this domain. However, AEs are highly sensitive to architectural choices and hyperparameters, and unsupervised optimization typically relies on reconstruction loss, which may be a poor proxy for downstream utility. Exhaustive hyperparameter optimization (HPO) is computationally expensive, leading researchers to frequently rely on suboptimal default configurations. To democratize access to large-scale unsupervised HPO research, we introduce $\textbf{BBOmix}$, the first open-source tabular benchmark for unsupervised representation learning on real-world biological data. Our benchmark includes 105,000 evaluations across four AE architectures and seven multi-omics modalities from the TCGA and SCHC datasets. We quantify the correlation between reconstruction loss and downstream task performance and provide an extensive evaluation of state-of-the-art single-fidelity, multi-fidelity, and transfer learning HPO methods, establishing a rigorous baseline for future research in unsupervised biological representation learning.

---


### 260. [GeM-NR: Geometry-Aware Multi-View Editing for Nonrigid Scene Changes](https://arxiv.org/abs/2606.05142)

**<font color=#1a73e8>作者：</font>** Josef Bengtson, Yaroslava Lochman, Fredrik Kahl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent developments in multi-view image editing with generative models have brought us a step closer toward general 3D content generation and customization. Most existing works focus on rigid or appearance-only edits by utilizing the geometry of the unedited scene. This naturally limits these methods to edits that preserve the underlying scene structure. Other approaches are trained for specific image editing tasks, such as object removal and addition. Despite this progress, general nonrigid edits, i.e., edits that substantially change the scene geometry, remain challenging for existing methods. We propose GeM-NR, a fast and flexible training-free approach for general multi-view consistent image editing, including edits that drastically change the geometry and appearance of the scene. Given an anchor image edited with a chosen backbone editor (such as FLUX, Qwen, BrushNet) and a query unedited image, GeM-NR edits the query image consistently with the anchor edit. The method incorporates multiple stages: (i) depth map estimation, where we propose a strategy to maximize the alignment between the 3D point clouds of the edited and unedited scenes, (ii) projection onto a query viewpoint, and (iii) refinement of the obtained image conditioned on the unedited query. The conditioning-based formulation scales well from two to many views of an object. We demonstrate the ability of our method to handle edits with significant changes in geometry and appearance, something that existing methods struggle with. We perform an extensive evaluation showing that our method improves consistency for a wide variety of edit tasks, including generating 3D representations of the edited scene. Both quantitative and qualitative results indicate the state-of-the-art performance of our method in terms of edit quality as well as geometric and photometric consistency across multiple views.

---


### 261. [Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)](https://arxiv.org/abs/2606.05145)

**<font color=#1a73e8>作者：</font>** Nizar Islah, Istabrak Abbes, Irina Rish 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When post-trained language models fail on reasoning problems, the common test-time-scaling response is to spend more compute on additional attempts, and the failed traces play no further role. We argue this discards a crucial signal; some failures come from unlucky sampling, where more rollouts help, while others are structural and resist resampling regardless of budget. We propose that failed traces encode recoverability structure: the inference-time signature of which test-time interventions can rescue a given failure. Three problem-level trajectory features, derived from the structure of available interventions, recover this structure from the distributional signature of failed rollouts, not their text. They cluster failures into stable regimes, characterize the failure topography of different post-training methods ($84.3{\pm}4.3\%$ accuracy, $+20\%$ over a majority-class baseline), and support a training-free routing rule that lifts rescue by $+12.2\%$ on the deployment-relevant Steerable-Hard subset (failures where retry is insufficient and a bounded intervention is reachable). The features and the routing rule transfer across two cross-family probes. The same three features thus convert failed traces from discarded data into a diagnostic object, supporting test-time routing and post-training analysis without training-time or weight-space access.

---


### 262. [An Open-Source Two-Stage Computer Vision Pipeline for Fine-Grained Vehicle Classification using Vision Transformers](https://arxiv.org/abs/2606.05149)

**<font color=#1a73e8>作者：</font>** Gandhimathi Padmanaban, Fred Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle body type is a significant determinant of cyclist injury severity in overtaking crashes, yet automated tools for classifying vehicles into injury-risk-relevant categories from naturalistic roadway video do not exist in the open literature. Standard object detection benchmarks provide only coarse vehicle labels (car, truck, bus, motorcycle), while existing fine-grained recognition systems are trained on controlled imagery and lack evaluation for deployment robustness across recording sites. This paper presents an open-source two-stage computer vision pipeline combining a pre-trained RT-DETR detector for coarse vehicle localization with a fine-tuned Vision Transformer (ViT-Base/16) for six-category body-type classification: passenger car, SUV, pickup truck, minivan, large van, and commercial truck. A confidence-based abstention mechanism withholds Stage 2 predictions when softmax output falls below 0.60, producing unknown labels rather than silent misclassifications. Evaluated on 3,805 annotated overtaking events from a bicycle-lane corridor in Ann Arbor, Michigan (in-distribution), the pipeline achieved 0.94 accuracy with per-class F1 scores from 0.91 (minivan) to 0.97 (SUV). On an independent out-of-distribution evaluation of 311 events from an open cycling dataset without retraining, accuracy was 0.89. Three of four well-represented categories maintained F1 at or above 0.90 under domain shift. The largest degradation was observed for minivan (F1 = 0.72), driven by abstention rate rising from 2.4% to 25.0% rather than active misclassification, consistent with the mechanism propagating genuine model uncertainty. The full pipeline, including inference scripts, training code, evaluation utilities, and model weights, is released as open-source software to support reproducibility and reuse across roadside video archives and cycling safety research.

---


### 263. [Reinforcement Learning from Rich Feedback with Distributional DAgger](https://arxiv.org/abs/2606.05152)

**<font color=#1a73e8>作者：</font>** Rishabh Agrawal, Jacob Fein-Ashley, Paria Rashidinejad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models have advanced rapidly, but the dominant reinforcement learning from verifiable rewards (RLVR) recipe remains surprisingly narrow: sample many responses and reward each with a single bit indicating whether the final answer is correct. Yet many settings provide rich feedback, including execution traces, tool outputs, expert corrections, and model self-evaluations. We study how to use such feedback through a distributional variant of the classic imitation learning algorithm DAgger, where the learner has local access to an expert distribution on states visited by the current policy. This yields a simple forward cross-entropy objective that admits a blackbox expert and whose sequence-level gradient {conduct rich credit assignment by propagating} future expert-student disagreement back to earlier decisions. We show that prior RL with self-distillation objectives based on reverse KL or Jensen-Shannon fail to guarantee monotonic policy improvement: even when the expert has higher reward, their updates may increase probability on worse actions. In contrast, we show that forward cross-entropy admits monotonic policy improvement and enjoys guarantees on regret. We further show that our objective optimizes a lower bound on teacher-weighted likelihood of success, leading to improved Pass@N. Empirically, our approach, DistIL, improves over RLVR and RL with self-distillation baselines across a variety of domains: scientific reasoning, coding, and solving hard mathematical problems.

---


### 264. [Streaming Communication in Multi-Agent Reasoning](https://arxiv.org/abs/2606.05158)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Xiaogang Xu, Wen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent reasoning systems adopt a "generate-then-transfer" paradigm that forces end-to-end latency to scale linearly with pipeline depth. We introduce StreamMA, a multi-agent reasoning system that streams each reasoning step to downstream agents as soon as it is generated, pipelining adjacent agents and thus reducing latency. Surprisingly, this pipelining also improves effectiveness: because multi-step reasoning quality is non-uniform and early steps are more reliable than later ones, working with these reliable early steps instead of the full chain prevents error-prone late steps from misleading downstream agents. We formalize both advantages with the first closed-form joint analysis of stream, serial, and single protocols, deriving the effectiveness ordering, speedup upper bound, and cost ratio. Across eight reasoning benchmarks spanning mathematics, science, and code, two frontier LLMs (Claude Opus 4.6 and GPT-5.4), and three topologies (Chain, Tree, Graph), StreamMA outperforms both baselines (avg. +7.3 pp, max +22.4 pp on HMMT 2026; Claude Opus 4.6-high). Beyond these contributions, we discover a "step-level scaling law": increasing per-agent steps consistently improves both effectiveness and efficiency, a new scaling dimension orthogonal to and composable with agent-count scaling.

---


### 265. [Controllable Dynamic 3D Shape Generation via 3D Trajectories and Text](https://arxiv.org/abs/2606.05162)

**<font color=#1a73e8>作者：</font>** Jaeyeong Kim, Ines Kim, Jahyeok Koo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce T2Mo, a feed-forward framework for controllable dynamic 3D shape generation conditioned on 3D trajectories and text. Due to the inherent ambiguity of language, generating precisely intended motions using text alone remains challenging. To address this, we adopt 3D trajectories as controllable spatial guidance, specifying the exact paths along which selected points should move. By combining both, T2Mo generates object motions that spatially adhere to the given trajectories while globally reflecting the text semantics. To robustly handle trajectory inputs with arbitrary configurations, ranging from dense to sparse and unevenly distributed, we further propose a shape-grounded trajectory embedding that maps an input trajectory set into a shape-aware token set covering the entire object. We conduct extensive comparisons against text-based baselines and cascaded video-based baselines that combine trajectory-guided video generation with video-to-dynamic mesh generation. Quantitative and qualitative evaluations, along with user studies, demonstrate that our approach produces motions that more faithfully follow the given prompts with higher expressiveness while preserving motion quality.

---


> [!TIP]
> 当前位于：**251-265**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-265**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
