# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**801-850**（第 17/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-850** | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 801. [Implementing Data Diodes Using Commodity Hardware and Open Source Software](https://arxiv.org/abs/2609.35256)

**<font color=#1a73e8>作者：</font>** Peter Story, Gert-Jan den Besten  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> One-way network devices, known as data diodes, are used to defend against sophisticated cyberattacks. Partly due to their high cost, data diodes are mostly deployed in nuclear power plants and within the government for handling classified information. Although commercially available data diodes are expensive, a data diode's hardware can assembled from commodity fiber-optic network equipment. However, specialized software is needed to send data through a data diode reliably: the receiving program cannot request retransmission of dropped packets, so packet loss must be minimized and mitigated. First, we developed a minimal program to measure packet loss. We found that most packet loss was caused by the receiving program processing incoming packets too slowly, and that packet loss often occurs in clusters. Also, we discovered ways to minimize packet loss on Linux and macOS without using superuser privileges. Next, we tested three existing open source programs for one-way data transfers: netcat, UDPcast, and lidi. Although these programs were unreliable in their default configurations, we identified reliable configurations for UDPcast and lidi. Finally, we incorporated our findings into pydiode, our cross-platform program for reliable one-way data transfers.

---


### 802. [Latency and accuracy tradeoffs in Spiking Neural Networks](https://arxiv.org/abs/2609.35260)

**<font color=#1a73e8>作者：</font>** Zhanglu Yan, Zixuan Zhu, Kaiwen Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks are attractive for low-power speech command recognition, yet their latency has received far less attention than their energy efficiency, and their multi-timestep execution is widely assumed to make them slower than quantized neural networks. This paper challenges the assumption that more local timesteps necessarily imply higher network latency. By overlapping computation across adjacent layers at the timestep level, SNNs may complete execution in less time than comparable bit-serial QNNs. However, this overlap relies on spikes firing on incomplete inputs, and a spike once generated cannot be withdrawn, so its error persists and reduces accuracy. Waiting for more input before firing would seem to improve accuracy at the cost of reduced overlap. Yet we find and prove that this intuition fails at some layers, where even a small increase in waiting can change spike timing and downstream computation, making the network both slower and less accurate. We therefore propose a Pipeline Delay Search method which selects each layer's delay by balancing task-level accuracy gains against added network latency. We then adapt the selected configurations through spike-based quantization-aware training and bounded tuning of firing thresholds and initial membrane potentials. Together, these steps form Falcon, a framework for Fine-grained Analysis of Latency and Controlled firing which systematically analyzes and optimizes SNN latency under a spatial analog compute-in-memory mapping with shared digital engines. We evaluate Falcon on GSCV2 and SSC, achieving competitive accuracies of 96.31 and 83.02 at modeled network-core latencies of 119.64 and 124.00us, respectively. Together, our analysis and results show that SNNs can compute more yet finish faster, and wait longer yet predict worse, highlighting why Falcon matters for both latency and accuracy.

---


### 803. [SpikeCredit: Temporal Credit Carrier for Reinforcement Learning with Sparse Rewards](https://arxiv.org/abs/2609.35268)

**<font color=#1a73e8>作者：</font>** Yingchao Yu, Pengfei Sun, Wenxuan Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) with sparse rewards is challenging because delayed outcomes provide little guidance about which intermediate computations caused success or failure. We argue that reliable credit assignment requires policy dynamics that preserve and expose credit-relevant information over time, a role we formalize as Temporal Credit Carriers (TCCs) and that spiking neural networks (SNNs) naturally fulfill through graded membrane traces and event-driven spikes. Based on this hypothesis, we propose SpikeCredit, an SNN-based framework for RL with sparse rewards that first performs task-adaptive TCC selection and then closes the loop between a fast TCC-reading pathway, where self-motion feedback constraint uses local behavior-grounded cues to constrain transition-level credit recovery, and a slow TCC-writing pathway, where credit-targeted trace alignment feeds recovered credit back into the actor to make future TCC dynamics more credit-readable. Across sparse-reward MuJoCo tasks, SpikeCredit improves Last10 return over sparse SNN baselines by +1169% on Ant, +953% on Hopper, +723% on Swimmer, and +1781% on Walker2d, and exceeds the dense-reward baseline on Swimmer by +113%. Mechanistic analyses further show substantially stronger alignment with dense rewards than the sparse SNN baseline. These results position spiking dynamics as credit-preserving substrates for sparse-reward RL.

---


### 804. [eval-unlearn: Benchmarking unlearning in Text-to-Image Diffusion Models](https://arxiv.org/abs/2609.35269)

**<font color=#1a73e8>作者：</font>** Mansi, Nikhil Raghavan, Zixia Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rising number of concept unlearning techniques for text-to-image (T2I) diffusion models has produced a fragmented evaluation landscape. Methods are assessed under heterogeneous experimental conditions making principled cross-method comparison difficult. We present eval-unlearn, an open-source Python library providing a unified, reproducible benchmarking framework for concept unlearning in T2I Diffusion models. eval-unlearn integrates twelve published unlearning techniques spanning fine-tuning, closed-form model editing, and inference-time intervention, alongside nine complementary evaluation metrics covering erasure efficacy, adversarial robustness, generative quality, and concept retention. Its plugin architecture lets third-party techniques and metrics self-register without modifying the core framework, and its streaming, batched pipeline supports efficient evaluation of both standard NSFW concepts and arbitrary general concepts. As a further contribution, we release a public leaderboard on HuggingFace along with an interactive tool for real-time evaluation of unlearning techniques. The leaderboard compares nudity concept erasure case study across all twelve techniques, exposing significant accuracy-quality trade-offs that are obscured by heterogeneous evaluation. eval-unlearn is released under the MIT license; the package, code, leaderboard, and documentation are all available at this https URL.

---


### 805. [Multi-Attractor GNNs: Set-Valued Expressivity Beyond Unique Equilibria](https://arxiv.org/abs/2609.35274)

**<font color=#1a73e8>作者：</font>** Jialin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent and equilibrium graph neural networks (GNNs) often enforce a unique fixed point or use one training target per graph. Yet many combinatorial and scientific problems admit multiple valid solutions, with no preferred one. A designated target can then impose an arbitrary selection rule. For tasks invariant to node relabeling, a symmetric graph may have a symmetric solution set but no symmetric solution.
We show that multiple equilibria enable one weight-tied message-passing GNN to represent set-valued equivariant maps: different initializations approach different valid solutions. Under stated regularity assumptions, we first construct globally Lipschitz, permutation-equivariant dynamics that converge almost surely to valid solutions and reach every solution branch with positive probability. We then establish approximate realization by recurrent message passing with continuous component maps, with arbitrarily small update and limiting errors and arbitrarily high probability. This goes beyond standard universality arguments: although message passing alone cannot distinguish symmetric nodes, the evolving state keeps nodes distinguishable at every finite step without auxiliary node identifiers. Such dynamics can be learned without solution labels using problem-specific energies. On Ising ground states, structural module detection in protein graphs, and chemical reaction steady states, the learned updates produce multiple high-quality predictions with high numerical convergence rates. They achieve better average solution quality than the tested unique-equilibrium, single-target, and feedforward baselines, while remaining competitive with much larger diffusion-based solvers.

---


### 806. [Evaluating Hierarchy-Aware Deep Learning for the Recognition of Tironian Notes](https://arxiv.org/abs/2609.35277)

**<font color=#1a73e8>作者：</font>** Yule Kang, Thomas Gorges, Janne van der Loop 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tironian notes are generally regarded as the first Latin shorthand system and are notable for their large, fine-grained symbol inventory. Their high visual similarity and large class set make manual reading time-consuming, leaving manuscripts that contain Tironian notes inaccessible to many researchers. Automatic recognition is also challenging because models must distinguish subtle differences in stroke shape and sign structure while realistic training data remain scarce. However, standard flat classifiers do not explicitly use visual or structural relations between related signs. This paper investigates whether structural relationships between Tironian notes can support automatic recognition. We use the Supertextus Notarum Tironianarum (SNT) by Martin Hellmann, which provides idealized sign forms and a hierarchical organization of Tironian notes. We compare flat ResNet18, ConvNeXt, Shifted Window Transformer (Swin), and Vision Transformer (ViT) classifiers with Hierarchical Deep Convolutional Neural Network (HD-CNN)-style coarse-to-fine models and hierarchy-aware routing models based on visual class cleaning and similarity-based re-clustering. The models are evaluated on handwritten samples and manuscript-domain samples from Vergilius Turonensis, both with and without limited few-shot adaptation to the manuscript domain. The results show that the relative performance of flat and hierarchical models depends on adaptation. On Vergilius Turonensis, HD-CNN achieves the best non-adapted Top-1 result with 45.43%, while flat classification reaches the best Top-1 result after few-shot adaptation with 82.09%. Overall, the results indicate that hierarchical structure can support Tironian note recognition, especially under non-adapted conditions.

---


### 807. [The Argument and the Letterhead: Source-Position Coherence in AI Evaluation](https://arxiv.org/abs/2609.35286)

**<font color=#1a73e8>作者：</font>** Michele Loi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An argument can be surprising coming from a particular speaker without being a bad argument. Do AI evaluators keep these judgments apart? Two preregistered descriptive studies and a later Jev supplement collected 2,976 usable evaluations of six fixed texts about US AI policy, Germany's debt brake and Swiss nuclear energy. Each text was presented under several source attributions. The key comparison asks whether the gap between two sources changes when the argument changes. On Sol, for example, a national-security argument received mean ratings of 0.359 under CODEPINK and 0.639 under College Republicans; a civil-rights argument received 0.742 and 0.721. A constant preference for one source cannot explain that pattern. Related interactions appeared across topics and recent model configurations, including those with reasoning enabled, while several comparisons yielded small effects. The later European Jev supplement yielded five interactions below the adopted absolute reference of 0.05; its distinct rubric and interrupted collection limit comparison with the chat systems. Some written evaluations explicitly invoked a mismatch between a source and its attributed position. Taken together, the numerical and verbal evidence supports source-position coherence as a plausible explanation, alongside competing accounts involving credibility, authenticity and interpretation of the task. The paper develops this inference through controlled comparisons, reports conditional post hoc p-values in an appendix, and documents the human decisions and delegated checks behind an AI-conducted study.

---


### 808. [$λ$-JEPA Spectral Anti-Collapse Regularization for Self-Supervised Learning](https://arxiv.org/abs/2609.35288)

**<font color=#1a73e8>作者：</font>** Berker Demirel, Clémentine Dominé, Valentino Maiorca 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding self-supervised learning typically combines an invariance objective across augmented views with additional mechanisms to prevent representational collapse. These objectives are often applied after a projection head, while downstream tasks use the backbone representation before the projector. We find that this mismatch does not necessarily prevent dimensional collapse in the backbone, which can retain low effective rank and potentially limit downstream transfer. To address this, we introduce SACReg, a spectral anti-collapse regularizer motivated by an analysis of $\lambda$-balance, which captures the relative scale of weight matrices across layers. In a two-layer linear network, we show that (i) $\lambda$-balance prevents collapse, and (ii) our regularizer applied to the backbone induces $\lambda$-balance. In the nonlinear case, this regularizer leads to anti-collapse as well and, in realistic architectures on ImageNet100, it empirically increases the representations' ranks. We apply SACReg to JEPA and propose $\lambda$-JEPA, which improves over LeJEPA and VISReg on ImageNet-1k classification and in average linear-probe transfer performance across eight downstream image datasets. On video self-supervised learning, $\lambda$-JEPA improves over LeVJEPA and V-JEPA 2 on the Something-Something-v2 and Kinetics-400 benchmarks. Code is available at this https URL.

---


### 809. [Domain-adaptive Zero-Shot Image Enhancement via Locality-Constrained Diffusion Guidance](https://arxiv.org/abs/2609.35289)

**<font color=#1a73e8>作者：</font>** Theresa Neubauer, Dimitrios Lenis, Astrid Berg 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Denoising Diffusion Probabilistic Models have shown remarkable performance in unconditional image generation. In order to generate images with desired semantics, recent works have restricted the solution space by using guidance constraints in the diffusion sampling process.
However, for image enhancement across different domains, these methods struggle to balance two main requirements: looking realistic in the target domain (photorealistic images) and preserving relevant features of the source domain, e.g., low-quality renderings or art paintings. Here, small local changes can alter the fidelity of the image completely, while large changes in other regions might be insignificant.
We introduce LocDiff, a locality-constrained guidance method for image enhancement, which serves as a zero-shot extension to pre-trained diffusion models, ensuring the preservation of critical features during domain adaptation. In this way, we retain important local features, while allowing less critical regions to remain unconstrained and not interfere with the guidance process for relevant regions. We evaluate our method on two different domain-shift tasks: For art-to-photo translation, we apply the method in a fully zero-shot setting, preserving facial identity from paintings while generating photorealistic details. For enhancing low-quality fetal ultrasound renderings, we demonstrate zero-shot inference with auxiliary prior alignment. Here, the objective is to artificially add high-resolution characteristics and produce photorealistic ultrasound renderings, a target domain for which no ground truth distribution exists. Our experimental results demonstrate that LocDiff achieves favorable realism-faithfulness trade-offs compared to state-of-the-art methods, enabling controllable cross-domain enhancement.

---


### 810. [EvoIn: Bridging Evolution and Internalization for Agent Fine-Tuning](https://arxiv.org/abs/2609.35290)

**<font color=#1a73e8>作者：</font>** Shihan Dou, Shaofan Liu, Zhonghang Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has explored improving agents by jointly evolving their harnesses and models, but often takes a ''potpourri'' approach that bundles together new tools, new decision-making procedures, and model adaptation to the evolved harness under a single notion of agent improvement. In this paper, we instead investigate how agents can improve their decision-making procedures. In particular, we propose EvoIn, an agent fine-tuning framework that bridges evolution and internalization. EvoIn first analyzes agent execution traces to evolve and validate new decision-making procedures by temporarily instantiating them in the harness. The validated procedures guide the agent to generate improved reasoning traces. These traces are then rewritten into self-contained reasoning traces, removing explicit references to harness instructions while expressing the induced decision logic as the model's own reasoning. Finally, EvoIn fine-tunes the model on the rewritten traces, internalizing these procedures so that the improved decision-making persists without the evolved harness at inference time. We evaluate EvoIn on diverse benchmarks and find that it consistently enables agents to learn stronger decision-making procedures, raising the pass rate by 10.9 points in-domain and by 9.2 points out-of-domain. Results further show that the internalized decision procedures generalize to unseen tasks. Case studies show that agents can learn to decide how to solve a task before solving it, for example by checking a document's length to choose between reading it in full and searching it. EvoIn is also broadly applicable, showing consistent improvements on another model family.

---


### 811. [Scaffold Then Internalize: Representation Injection for Diffusion Transformers](https://arxiv.org/abs/2609.35292)

**<font color=#1a73e8>作者：</font>** Han Fu, Jiacheng Chen, Baoquan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent representation alignment (REPA) methods accelerate diffusion transformer training by aligning projections of the transformer's hidden states with representations from pretrained visual encoders. In this work, we explore a reverse and complementary direction to REPA: rather than projecting diffusion representations into the encoder's space, we inject encoder representations into the diffusion transformer, allowing them to actively participate in the denoising process. To this end, we introduce \textit{REPresentation Injection} (REPI), a training framework based on a scaffold-to-internalization strategy, in which projected encoder representations initially serve as a temporary scaffold and are then progressively internalized by the diffusion transformer. REPI outperforms REPA across a wide range of backbones and is highly complementary to it: combining the two yields substantial gains over either alone. Notably, with only 160K training steps, REPI + REPA matches vanilla SiT trained for 7M steps, a speedup of over $43.5\times$. Code will be available at this https URL

---


### 812. [AbGaze: Attentive Geometric Representation Learning for End-to-End Antibody Design](https://arxiv.org/abs/2609.35296)

**<font color=#1a73e8>作者：</font>** Jiashuo Wang, Siqi Fan, Yizhen Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational antibody design requires representations that capture the geometric patterns underlying antigen--antibody interactions, yet existing approaches often rely on scalar distances or surface-intrinsic features, leaving cross-molecular geometry largely implicit. We present AbGaze, an end-to-end antibody design framework based on attentive geometric representation learning, which encodes distance, spatial direction, and surface-normal orientation of antigen surfaces relative to antibody-residue local frames, and adaptively aggregates these geometric interactions according to their interfacial context. The learned interaction representation is shared across multi-CDR co-design, complex structure prediction, and affinity optimization, with local-frame geometric supervision further constraining the representation. AbGaze outperforms prior methods across all three tasks: relative to the second-best method, it improves amino-acid recovery by 7.1% and reduces structural error by 14.9% on average over the six CDRs, improves interface docking quality (DockQ) by 6.6%, and raises the affinity improvement rate (IMP) by 32.5%.

---


### 813. [RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts](https://arxiv.org/abs/2609.35311)

**<font color=#1a73e8>作者：</font>** Jin Hyun Kim, Min Young Kim, Soohwan Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned video world models predict future robot interactions from multiple cameras, yet their outputs remain disparate video collections rather than a shared metric scene queryable across viewpoints and time. While existing 4D reconstruction methods offer a path to spatialize these predictions, independently reconstructing and merging each camera stream fails to enforce cross-view consistency. This limitation is particularly detrimental when combining moving robot-mounted cameras with fixed external views. To address this, we introduce RoGSW4RLD, a feed-forward framework that lifts synchronized multi-camera rollouts into a unified, time-queryable metric 4D Gaussian field. Rather than learning a separate geometric transition model, RoGSW4RLD directly reconstructs the visual future generated by existing world models. Its core innovation is a two-stage architecture: Stage 1 jointly forms the metric 4D field by fusing cross-view evidence with robot-specific articulated geometry and kinematics, while Stage 2 refines the field's geometry and appearance while strictly preserving the initial temporal displacements. Evaluated on 256 held-out DROID episodes, RoGSW4RLD significantly outperforms camera-wise reconstruction with calibrated merging, improving novel-view PSNR by 2.15 dB, reducing depth AbsRel by 47%, and lowering robot displacement error by 61%. These robust gains extend to action-conditioned Cosmos 3 rollouts, demonstrating that predicted video futures can be successfully translated into consistent, spatially queryable 4D metric representations.

---


### 814. [When Should a Satellite Estimate Be Changed? Stress-Testing Neural Corrections for Evapotranspiration](https://arxiv.org/abs/2609.35314)

**<font color=#1a73e8>作者：</font>** Marco Trotta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural residuals can improve satellite evapotranspiration (ET) estimates, but selectors must predict when a correction helps and reject unsupported inputs. We evaluate ten-member models on 16,366 flux-tower observations from 151 stations paired with OpenET, across nine rolling years and five spatial folds. At one held-out station, Gain accepted corrections on all 32 physically invalid records: it predicted a mean benefit of 0.83 mm/day, but the corrections increased mean absolute error by 21.6 mm/day versus OpenET. On spatially held-out unit errors, SupportGain reduced station-macro MAE versus Gain by 0.148 mm/day under wind x3.6 (simultaneous 95% interval, 0.070 to 0.226), with 9.3% acceptance versus Gain's 51.8%; on clean inputs, its 0.006 mm/day advantage had an interval that includes zero. These fault analyses are exploratory; none of 40 preplanned temporal comparisons passed Holm correction, while a separate predeclared cropland contrast found 0.041 mm/day lower station-macro MAE with crop-only training (95% interval, 0.009 to 0.079).

---


### 815. [Reliability Engineering for AI Systems: Challenges, Methods, and Directions](https://arxiv.org/abs/2609.35316)

**<font color=#1a73e8>作者：</font>** Rong Pan, Yili Hong, Min Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI reliability concerns whether an AI system performs its intended function dependably over a stated period and under stated operating conditions, with stated evidence. As these systems become more autonomous, that function includes more than a correct output. Retrieval, memory, tool use, permissions, human oversight, and interactions among systems must operate consistently and safely, and, for generative systems, so must the reasoning process that produces the output. Average benchmark accuracy measures capability; it does not quantify this broader reliability claim. This paper adapts established reliability engineering methods, from failure definitions and operational envelopes to FMEA, accelerated testing, field monitoring, and reliability growth, to AI systems. A four-level diagnostic framework classifies failures as component, operational-loop, agentic-conduct, or network and governance failures. Test, evaluation, verification, and validation (TEVV), sequential monitoring, and FRACAS create and refresh evidence. SMART provides statistical guidance for measurement, analysis, assessment, and test planning; the NIST AI Risk Management Framework provides organizational guidance for governance, evaluation, monitoring, and mitigation. Three cases illustrate the program: adversarial testing of a convolutional neural network, perception-error propagation, and autonomous-vehicle disengagements. Established reliability engineering provides a usable foundation; new measurements and safety guardrails are still needed as these systems are self-evolving.

---


### 816. [Weighting Schedules Govern What and When Score-Based Generative Models Learn from Multimodal Data](https://arxiv.org/abs/2609.35322)

**<font color=#1a73e8>作者：</font>** Jérémie Klinger, Raphaël Urfin, Giulio Biroli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based generative models generate new samples by integrating a time-dependent drift that carries Gaussian noise onto the target distribution. In practice this drift is modeled by a neural network, trained on a loss integrated over time $t$ with a weighting schedule $w(t)$. Along the backward dynamics, and for multi-modal distributions, trajectories commit to modes of the target within a narrow time window, the \textit{speciation time}. In this work, focusing on high-dimensional data, we decompose the integrated loss into its single-time contributions and analyze each at fixed signal-to-noise ratio $\Lambda(t)$: we show that $\Lambda(t)$ sets the rate at which each feature of a multimodal target - the mode directions and their relative weights - is acquired during training. Crucially, at high $\Lambda(t)$ all mode directions are acquired together, on a single timescale insensitive to their amplitudes, while the relative weights are not learned at all. Only near the speciation time, where $\Lambda(t)$ becomes of order one, do all features become learnable, each on its own timescale: the weights are acquired jointly with the directions, and the directions at rates set by their relative amplitudes. For models trained on time-integrated objectives, the learning dynamics is then governed by how much of the weighting effectively sits near the speciation time, which provides insights on $w(t)$ design choices. These results follow from an exact high-dimensional analysis of the training dynamics of unbalanced and hierarchical Gaussian mixtures. Numerical experiments on image and human genome haplotype generation recover the predicted hierarchy of learning timescales in more complex settings.

---


### 817. [Scalable In-Context Reinforcement Learning with Recurrent Algorithm Distillation](https://arxiv.org/abs/2609.35333)

**<font color=#1a73e8>作者：</font>** Yuanqing Ma, Zhenrui Zheng, Chenjun Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithm Distillation (AD) has demonstrated the remarkable ability of Transformers to perform in-context reinforcement learning without explicit weight updates. However, capturing long-term learning progress necessitates expansive context windows, which incur prohibitive memory costs and limit scalability in complex, long-horizon tasks. To address this bottleneck, we propose Recurrent Algorithm Distillation (RAD). RAD employs a dual-component architecture: a Compression Transformer that distills extended interaction histories into compact latent tokens, and an AD Transformer that auto-regressively generates actions using a hybrid context of these compressed memories and recent transitions. By maintaining a fixed-size latent buffer, RAD decouples the effective history length from computational complexity, functionally providing the model with a long-horizon memory. Empirical evaluations across diverse environments demonstrate that RAD matches the asymptotic performance of standard AD with significantly reduced context window sizes, offering a scalable solution for efficient in-context decision-making.

---


### 818. [NeuronDiscover: Agent-in-Twin for Mechanistic Discovery in Neuronal Microenvironments with World Action Models](https://arxiv.org/abs/2609.35338)

**<font color=#1a73e8>作者：</font>** Haowei Xu, Wanyi Fu, Hongbin Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic discovery in neuronal microenvironments requires interventions and measurements that separate competing explanations of solute transport and neuronal response. Predictive accuracy cannot settle the question: a real mechanistic change and an error in the computational twin leave the same signature in sparse observations. We formalize this twin confounding and reason over a joint mechanism--discrepancy belief, designing experiments that separate the two. NeuronDiscover is an Agent-in-Twin framework whose shared, mechanism-grounded World Action Model (WAM) couples prediction, intervention proposals, and observation design; independently adjudicated outcomes revise a scoped Mechanism--Intervention--Observation--Outcome (MIOY) graph, whose supported relations compile into executable programs carrying discrepancy-adjusted acceptance bounds. We evaluate on simulated brain-fluid tracer-transport worlds adjudicated by an independently frozen finer-mesh reference solver, and on donor-disjoint public current-clamp recordings of cortical neurons. Counting only relations that reach a certified terminal status, and scoring abstentions as unresolved for every method, at a matched budget of 16 experiments over 32 source units NeuronDiscover resolves 4.0 relations per assigned world against 3.4 for the strongest baseline and 3.2 without graph revision, at 5% false support and 82% scope accuracy. Joint mechanism--discrepancy acquisition resolves 3.8 relations versus 2.9 for plug-in expected information gain; discrepancy-adjusted verification lowers accepted-program failure from 15% to 9% at 60% acceptance coverage; and transfer to the recordings yields 1.94 versus 1.53 relations per assigned world. Correctness is adjudicated within declared model worlds and archival recordings.

---


### 819. [Generative Uncertainty as a Self-supervised Signal for Semantic Similarity Learning](https://arxiv.org/abs/2609.35341)

**<font color=#1a73e8>作者：</font>** Enrico Pallotta, Sina Raoufi, Lars Doorenbos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating semantic similarity between videos is a fundamental challenge in computer vision, essential for tasks ranging from out-of-distribution (OOD) detection to video retrieval. However, defining and labeling video similarity is notoriously difficult and expensive due to the complex spatio-temporal nature. In this paper, we propose a novel self-supervised approach that leverages generative uncertainty from text-to-video (T2V) diffusion models to learn semantic similarity without human annotations. Our method is based on the observation that T2V models produce consistent outputs for familiar concepts but exhibit high variance and uncertainty when prompted with specialized concepts. We utilize this behavior to identify stable semantic features within existing pretrained representations, such as VideoMAE and V-JEPA. Specifically, we learn a mask over these embeddings using purely generated data, encouraging the model to retain features that remain consistent across generations of general concepts while discarding those associated with generative noise or uncertainty. Experimental results across three key tasks demonstrate that our learned feature subspaces consistently outperform original pretrained features and baseline feature selection methods.

---


### 820. [Jev thinks "I don't know'', but doesn't say it: Introducing Sys1Cal-v1 Dataset for Probability Calibration](https://arxiv.org/abs/2609.35342)

**<font color=#1a73e8>作者：</font>** Riccardo Porcedda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The appearance of Jev marked the era of System One Models, foundation models that return structured decisions with probability distributions rather than text. Aside from low cost and great speed, Jev's central promise is that these probabilities are calibrated: such claim is not backed by any public test and available external benchmarks evaluate confidence calibration, not whether every returned option probability has the right numerical meaning. To tackle this issue, we introduce Sys1Cal-v1, a dataset of True/False questions about a proposition $A$ for which the exact probability $P(A)$ is known by construction. Each item is queried through the three Jev primitives - Noul, Choice and Score - and evaluated by total variation distance from the ground-truth distribution, which can be used to estimate a soft accuracy of System One Models.
We showcase the utility of Sys1Cal-v1 as a benchmark dataset by evaluating Jev and SemIf, an open-source Choice-style baseline. In this work, however, we focus even more deeply on Jev, by studying the calibration of its Score and Choice answers. In particular, we discover a peculiar behaviour that can be explained by assuming that Jev suppresses a third truth value, going beyond True and False. In other words, in \texttt{Choice} answers, $P(A)$ and $P(\neg A)$ are presented as if $P(A)+P(\neg A)=1$, while a term $P(U)\neq0$ is missing in the sum. Recovering $P(U)$ leads to an improvement of median soft accuracy in \texttt{Choice} answers from $0.771$ to $0.978$, suggesting that, even in binary decisions, Jev wants to answer with a third option:``I don't know''.

---


### 821. [From Data to Program: Fast & Direct Generative Program Inference from Empirical Data](https://arxiv.org/abs/2609.35348)

**<font color=#1a73e8>作者：</font>** Simon Klüttermann, Xueying Ding, Leman Akoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating probability densities from a finite set of samples typically requires dataset-specific model fitting. We introduce PRODiGI, a pretrained data-to-program model that infers an explicit, executable generative program in a single forward pass. Pretrained on synthetic datasets paired with their ground-truth programs, PRODiGI accommodates diverse generative families and data dimensionalities through template prediction and non-autoregressive program parameter decoding. Its inferred programs support direct sampling, density and score evaluation, and inspection independently of the pretrained model. We further introduce program-space fine-tuning, which refines differentiable program parameters by matching generated and empirical samples while keeping model parameters intact. Experiments show that PRODiGI achieves lower average density and score MAE than existing pretrained models, while offering multi-fold speedups over its closest competitors. Program-space fine-tuning further reduces generation MMD by 84%. By turning empirical data into explicit, reusable programs, PRODiGI introduces a new direction for fast, interpretable tabular generative modeling.

---


### 822. [Quasi Linear Kernel Attention with Infinite Capacity](https://arxiv.org/abs/2609.35349)

**<font color=#1a73e8>作者：</font>** Nicolaj Rux, Johannes Hertrich, Sebastian Neumayer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evaluation cost of transformers with softmax attention scales quadratically with sequence length. Kernel attention addresses this by replacing softmax with a more general kernel function. In this paper, we aim to identify kernels that retain the expressivity of attention while enabling quasi linear computation. To quantify expressivity, we introduce a capacity for each kernel, measuring the maximum sequence length for which the attention matrix can approximate the identity. A higher capacity thus indicates greater expressivity. We show that expressive kernels like softmax, Gauss, and Laplace have infinite capacity. In contrast, common quasi linear kernels, such as those derived from finite dimensional feature maps, exhibit finite capacity. As a solution, we propose additive kernels constructed from univariate spline and polynomial exponential kernels. We prove that these maintain infinite capacity while allowing quasi linear computation via sorting. Finally, we implement additive sorting kernels efficiently and benchmark them against modern softmax backends, demonstrating advantages for long sequences.

---


### 823. [Interference Beyond Geometry in Concept Extraction](https://arxiv.org/abs/2609.35351)

**<font color=#1a73e8>作者：</font>** Valérie Costa, Bahareh Tolooshams  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interference is commonly treated as geometric overlap between learned features. We introduce effective interference, which combines feature geometry and code statistics to capture realized interactions, distinguishing constructive from destructive interference and frequent weak interactions from rare strong ones. Under local fixed-support assumptions, we characterize how architectural constraints shape interference through four mechanisms: feature orthogonalization, bias compensation, gain adaptation, and encoder-decoder separation. Experiments with sparse autoencoders show that constrained architectures selectively reduce overlap among co-active features, while bias, gain, and encoder freedom allow constructive cross-contributions to remain. Together, these results show that interference in learned representations depends not only on feature geometry, but also on how features are used and on the architecture that produces their codes.

---


### 824. [Fiona: Accelerating FHE Inference with Packing-Aware Ternary Weights](https://arxiv.org/abs/2609.35352)

**<font color=#1a73e8>作者：</font>** Yiteng Peng, Zhibo Liu, Dongwei Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables neural network inference directly on encrypted inputs, but it remains orders of magnitude slower than plaintext in- ference. Applying the server's plaintext weights to encrypted activations involves plaintext-ciphertext multiplications (PMult) and accounts for more than half of inference time in recent systems. Ternary quantization can replace these multipli- cations with additions and subtractions, but the savings rarely materialize under packed execution. A single PMult applies a weight group fixed by the packing layout and can be avoided only when all its weights share the same ternary value. Ternarizing all groups, however, largely degrades accuracy.
We present FIONA, an offline optimizer that selectively ternarizes weights within a given packing layout based on the estimated effect of ternary conversion on the model's performance. FIONA encourages a shared ternary value within each weight group and retains full-precision weights for sensitive groups, so ternar- ized and full-precision paths coexist within a layer. It then compiles these hybrid operators exactly, applying common scaling factors once to accumulated inputs and reusing sums across outputs. Weight ternarization can also narrow the input ranges of downstream polynomials. FIONA fits lower-degree replacements under a cumulative accuracy budget, reducing multiplicative depth and bootstrapping. On VGG11, ViT, and BERT, FIONA reduces PMult operations by 53.4-79.5% and accelerates end-to-end encrypted inference by 2.38x, 1.68x, and 1.84x, re- spectively, with less than 1% accuracy loss across all three models.

---


### 825. [Do Temporal Link Predictors Need Learned Memory? A Smoothed-Count Baseline with a Handful of Parameters](https://arxiv.org/abs/2609.35364)

**<font color=#1a73e8>作者：</font>** Lisi Qarkaxhija, Ingo Scholtes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many temporal link predictors summarize past interactions through learned node representations. We examine whether simple counts of recurring interaction patterns can provide competitive predictions without learning these representations. We propose a temporal link predictor based on statistical language modelling. It pools transition and co-occurrence counts across sources to predict links that a source has never formed. We smooth sparse estimates using destination frequencies or Kneser-Ney continuation counts. A shared log-linear rule combines these estimates with popularity, source history, and recency, without node embeddings. In our main evaluation, the model achieves the highest MRR among the compared methods on 7 out of 16 datasets from TGB and TGB-Seq. It also outperforms EdgeBank and Base3 on all 16 datasets and the heuristic family on 14. These gains extend to datasets designed to limit repeated edges. With only 9--13 learned parameters, our model provides a simple and competitive baseline for evaluating future neural temporal link predictors.

---


### 826. [Ego-Forge: Text and Geometric-Attention Free Exo-to-Egocentric Video Generation](https://arxiv.org/abs/2609.35368)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi, Luc Van Gool, Danda Pani Paudel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Exo-to-egocentric video generation aims to synthesize what a person sees from their own viewpoint given third-person footage and a target head trajectory. The task requires transferring appearance and semantics across large viewpoint changes while hallucinating content never observed by the exocentric camera. Existing approaches either impose additional input requirements, such as a ground-truth initial egocentric frame or multiple synchronized exocentric views, or remain limited to category-specific settings. EgoX is the first to address cross-activity and in-the-wild generalization, but requires a human-provided caption of the non-existent egocentric view at inference and introduces a computationally expensive geometry-guided attention bias that can propagate reconstruction errors and suppress textual and visual context. We therefore propose \textbf{Ego-Forge}, a caption-free and bias-free framework for exo-to-egocentric generation. It introduces \textit{Dynamic Captioning}, which derives conditioning tokens directly from the model's hidden states and adapts them to the diffusion timestep and network depth, replacing external text conditioning. By scaling training by an order of magnitude and using all available exocentric viewpoints, Ego-Forge learns cross-view correspondence implicitly and eliminates the need for geometry-guided attention, requiring only a lightweight depth prior. Ego-Forge achieves state-of-the-art performance on Ego-Exo4D, runs faster end-to-end, requires no external annotation at inference, and generalizes to in-the-wild scenes, including cases where over-reliance on geometry blocks appearance inference. Our model and source code will be made publicly available.

---


### 827. [A decision-support system applied to Law: Reasoning and explainability of the decision](https://arxiv.org/abs/2609.35370)

**<font color=#1a73e8>作者：</font>** Jeremy Bouche-Pillon, Pascale Zarat{é}, Yannick Chevalier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of the digital transition brought an increasing need to control the processing of digital information, including in Law Enforcement Agencies (LEAs). At the EU level, in recent years, many regulations have emerged to control data processing and exchange. Texts other than the GDPR, such as the ''Law Enforcement Directive (LED)'', appeared to regulate specifically how Law Enforcement Agencies (LEAs) could process data. A formal representation of these regulations can be part of decision systems that support LEAs in processing data in compliance with the regulations. Although many new formalisms have emerged to represent legal norms and rules, few are provided with a reasoning mechanism. Furthermore, systems used in decision-making processes in critical contexts such as medical diagnoses or legal decisions cannot be fully automated, and the explainability of their results is essential to ensure user confidence in decisions. This explainability aspect, while crucial, is lacking in most modern approaches that rely on machine learning. This paper describes a framework to operate formal rules from regulations, by focusing on explainability of the decision. After describing the general architecture of the proposed decision support framework, the paper showcases how symbolic AI and the SPARQL query language can support legal reasoning. It then describes an algorithm to generate a justification for the reasoning results, and outlines the procedure to be followed when the reasoning does not lead to a satisfactory conclusion. We notably focus on a method based on decision trees to determine what additional information to request from the user.

---


### 828. [Deep Learning Methods in Neuroscience: From Modeling Molecular Mechanisms to Classifying States of Consciousness](https://arxiv.org/abs/2609.35372)

**<font color=#1a73e8>作者：</font>** Elena Benderskaya, Anastasiia Alifanova, Svetlana Batalova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A critical analysis of contemporary approaches to the study of conscious states. The review focuses on methods of classification, clustering, modeling of brain states under anesthesia and identification of measurable neurobiological characteristics of brain function. A comparative analysis was conducted in the following three major areas: automatic detection of states of consciousness using neural networks based on EEG and fMRI data; modeling of the structural-functional dynamics of the brain under the effects of anesthetics; and detection of neurophysiological indicators which correlate with the level of consciousness. The obtained conclusions demonstrate the growing effectiveness of deep neural models in the classification and prediction of brain states and the analysis of dynamic structural-functional connectivity. Nonetheless, significant limitations were also identified, including the limited interpretability of the models, the lack of standardized metrics, and the problem of the specificity of consciousness markers. Our findings support the need for developing hybrid, generalizible, physiologically grounded architectures. Furthermore, such approaches may improve the translational potential of computational models in clinical neuroscience. Diverse methods of machine and computational modeling have demonstrated their effectiveness in tasks of automatic clustering and classification of brain states, the development of multilevel models and the identification of connectivity patterns correlated with levels of consciousness. A larger-scale analysis and a larger dataset, as well as the implementation of model interpretability approaches are required for the practical application of the analyzed models. The models based on EEG and LFP are the most promising for clinical application due to their availability and the possibility of real-time monitoring.

---


### 829. [First Learn, Then Memorize: The Spectral Bias of Diffusion Models](https://arxiv.org/abs/2609.35377)

**<font color=#1a73e8>作者：</font>** Raphaël Urfin, Tony Bonnaire, Giulio Biroli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models trained on a finite dataset first learn to generate novel, high-quality samples and only much later collapse onto their training set. We identify the mechanism behind this separation of timescales and the object that probes it. The training dynamics of the score function are governed---exactly, and at any width---by the Gram matrix of the Neural Tangent Kernel (NTK) evaluated on the noisy training data, so the timescales of generalization and of memorization must be encoded in its spectrum. We show that they are, and that the structure responsible has no analogue in standard kernel settings. The use of multiple noise realizations per sample ($m$ noised copies at a fixed noise level) in the score-matching loss is what restructures the Gram matrix spectrum into two distinct parts. The first, of large eigenvalues, carries the global features of the target distribution and is present already for $m=1$. The second, which the repeated noising creates, consists of the smallest eigenvalues and is supported on eigenvectors aligned with the sample-specific noise directions; it sets a memorization timescale parametrically larger in the training set size $n$. We establish this picture on two fronts. Analytically, we solve the spectrum in the lazy high-dimensional limit for both linear ($n \asymp d$) and polynomial ($n \asymp d^k$) sample complexities, and prove through a bias--variance decomposition that the first bulk minimizes the approximation error while the second drives the error associated with memorization. Empirically, we show the same two-bulk structure in Convolutional NTKs on CelebA and in finite-width U-Nets trained well beyond the lazy regime, and we make the link causal: truncating the Gram matrix at rank $r$ tunes the generalization--memorization transition, and an $L_2$ penalty targeting the second bulk suppresses memorization in feature-learning U-Nets.

---


### 830. [Identifying Neural Source Dynamics from Unknown Local Interventions](https://arxiv.org/abs/2609.35379)

**<font color=#1a73e8>作者：</font>** Ayana Mussabayeva, Jiaqi Sun, Anuar Aimoldin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) records mixtures of brain-source activity. Even with a known anatomical forward model, experiments that excite only part of the source-state space leave the dynamics unidentified, and repetition cannot resolve the ambiguity. We show that unknown local mechanism changes can supply the missing information. We consider linear dynamics among fixed anatomical sources with known source-state initialization patterns. Changing one source's update rule for one transition leaves a rank-one, source-specific signature in subsequent EEG: subtracting matched baseline responses isolates it, and the forward model identifies the source and calibrates its response history. Combining these histories with initialization responses recovers source interactions without baseline reachability and without first identifying the intervention coefficients. We establish sufficient recovery conditions, a direct estimator, and a noise-sensitivity bound conditional on correct source labels. Simulated EEG on anatomy derived from magnetic resonance imaging confirms the information gain: with baseline excitation confined to four of twelve source coordinates, eight unknown changes recover all dynamics in 32/32 systems, whereas baseline realization, baseline regression through an invertible forward model, and changes that leave the tested states unexposed all fail, and explicitly constructed alternative dynamics reproduce every baseline mean. Where baseline information suffices, direct reconstruction is also more reliable than a matched-information spectral estimator. Nonlocal changes and forward-model error limit accuracy even when source labels are correct.

---


### 831. [The Hidden Ratio in Adam: Stable Structure, Compression, and Sign Dynamics](https://arxiv.org/abs/2609.35392)

**<font color=#1a73e8>作者：</font>** Yihe Zhou, Tongtian Zhu, Yingxiao Huo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam is the default optimizer for training modern deep neural networks, yet its adaptive behavior remains poorly understood due to the complex interaction between its first- and second-moment exponential moving averages (EMAs). We study Adam in the tied-$\beta$ regime, where the two EMA decay rates are equal, and show that its adaptive dynamics can be expressed through a transformed ratio with approximately scale-stable behavior. Empirically, this transformed ratio exhibits a stable, heavy-tailed distribution across tasks, model scales, and training stages, in contrast to the variability of raw moment magnitudes. This empirical stability has both practical and conceptual consequences. First, we derive a recurrence for the transformed ratio, yielding a reparameterization of Adam that replaces the second moment with a compressible state. Leveraging its stable distribution, we show that a fixed 4-bit codebook is sufficient in our experiments to store this state without auxiliary scaling, achieving performance competitive with full-precision Adam. Second, the transformed ratio view clarifies Adam's connection to sign-based methods: Adam reduces to sign-based momentum modulated by the transformed ratio, and replacing it with a constant recovers Signum as a limiting case. This perspective further provides a simple rule for transferring learning rates between the two methods. Together, these results suggest that tied-$\beta$ Adam admits a simple and approximately stable ratio structure underlying its adaptive behavior and demonstrate its utility for both analysis and efficient implementation.

---


### 832. [Structural Alignment for Reliable Industrial AI: Bridging Physical Reality, Data, Models, and Human Intent](https://arxiv.org/abs/2609.35400)

**<font color=#1a73e8>作者：</font>** Lizhi Xiao, Sihong Wu, Victoria Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is increasingly deployed in critical industrial domains, including healthcare, energy grids, subsurface exploration, where failures can have severe consequences for human safety, system stability, and economic outcomes. Yet AI is still evaluated primarily through benchmark accuracy, a model-centric metric that fails to capture the structural complexity and risks of real-world deployment. We propose a framework that views industrial AI reliability as a problem of structural alignment across four interacting worlds: physical, representational, machine, and human cognitive. These worlds are connected through two interfaces: digitalization, linking physical reality to computational representations, and goal encoding, translating human cognition to the machine objectives. Together, they define the space of admissible solutions. We characterize the solution space through four attributes: existence, non-uniqueness, robustness, and interpretability and show how mismatches arise at interfaces and propagate across worlds to produce reliability failures. Applications to healthcare, energy grids, and subsurface exploration illustrate that although dominant failure modes differ across domains, for example, interpretability in healthcare, robustness in energy grids, and non-uniqueness in subsurface exploration, all originate from a shared structural mechanism. By shifting the focus from model-centric evaluation to system-level alignment, this framework offers a principled foundation for assessing and governing reliability in industrial AI systems.

---


### 833. [BiMoGen: Bidirectional Motion-Text Generation via Unified Masked Discrete Diffusion](https://arxiv.org/abs/2609.35407)

**<font color=#1a73e8>作者：</font>** Wanjiang Weng, Yongliang Wu, Xiaofeng Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation and motion-to-text captioning are two fundamental tasks in human motion modeling, both grounded in the same underlying motion-text correspondence. Existing unified approaches mostly rely on autoregressive modeling, which imposes a fixed generation order and is therefore poorly suited to the bidirectional dependencies between language and motion, allowing early prediction errors to persist as fixed context and degrade both temporal coherence and cross-modal consistency. Masked discrete diffusion, which models sequences through iterative bidirectional prediction, offers a natural remedy. We therefore propose BiMoGen (Bidirectional Motion-text Generation), a unified masked discrete diffusion framework for bidirectional motion-text modeling. To stabilize training, we design Decoupled Uni- and Cross-Modal Training, in which masked pretraining first establishes cross-modal correspondence on paired motion-text sequences, after which supervised fine-tuning specializes the model for bidirectional generation. Masked diffusion nonetheless introduces its own source of error, as the model is trained on clean ground-truth context yet encounters self-generated and potentially erroneous context at inference, with errors committed under heavily masked states propagating through subsequent steps. We further introduce Generation-Aware Self-Correction that exposes the model to its own predictions during training and applies correction passes at early sampling steps to revise unreliably committed tokens. Extensive experiments on HumanML3D and KIT-ML demonstrate competitive performance on both tasks, validating the effectiveness of the proposed two-stage training and self-correction designs. The project page is available at this https URL.

---


### 834. [Spectral Super-Resolution using Spatial-Spectral Residual Operator Networks](https://arxiv.org/abs/2609.35410)

**<font color=#1a73e8>作者：</font>** Seokhyun Chin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectral super-resolution of multispectral satellite images can enable high temporal- and spatial-resolution hyperspectral satellite imagery at a modest cost, significantly increasing the applicability of hyperspectral remote sensing. This task is inherently ill-posed, making it well-suited for deep learning-based methods. In this study, the spectral super-resolution task is framed as an operator learning problem, and SSRON is proposed as a Deep Operator Network that effectively learns function-to-function mappings from downsampled spectra to continuous spectra. The model is trained to super-resolve Sentinel-2A-like multispectral imagery to EMIT images. Compared to baseline models, SSRON achieves superior performance across all metrics. The model also demonstrates zero-shot spectral super-resolution capability by predicting bands unseen during training. Furthermore, its continuous-output formulation suggests the potential to estimate spectra at finer wavelength intervals than the native sensor. These results suggest the potential of SSRON and establishes operator learning as a promising direction for spectral super-resolution.

---


### 835. [AI-Based Vulnerability Assessment Capability and Cyber Attack Graph Analysis](https://arxiv.org/abs/2609.35414)

**<font color=#1a73e8>作者：</font>** Joni Herttuainen, Kirsi Hellsten, Vesa Kuikka 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threats targeting mission-critical infrastructure are becoming more sophisticated while the barrier to launching attacks continues to fall. Traditional point solutions like antivirus and firewalls are reactive and fail to address the combinatorial complexity of modern attack surfaces. This paper presents an investigation combining two complementary methodologies: Lockheed Martin's Vortex/Crow framework, which applies multi-agent reinforcement learning (MARL) over industry-standard cyber knowledge graph to identify and prioritize attack vectors and TTPs (tactics, techniques, and procedures); and Aalto's probabilistic attack graph model that combines network topology and its vulnerabilities to compute system-level risk metrics. The 2015 Ukraine Power Grid cyberattack serves as a well-documented validation scenario. Applied independently to the same operational technology (OT) network topology, both methodologies converge on the same attack vectors and exploit sequences as those documented in the incident record, thus providing mutual cross-validation. Attack graph analyses using node-level elimination experiments identify industrial control systems (ICS) as the most critical enablers of attack propagation, representing high-priority targets for defensive hardening. Comparison of CVSS (v2.0) and IronMiner vulnerability scoring yields in general consistent results, with IronMiner providing more actionable differentiation at network periphery nodes. The layered methodology of baseline assessment and node-level elimination proves to be scalable to large enterprise networks, thus offering defenders a structured, AI-enabled path to prioritize mitigation under realistic time and resource constraints.

---


### 836. [When Should the Count Change? Learning State Maintenance for Causal Video Counting](https://arxiv.org/abs/2609.35416)

**<font color=#1a73e8>作者：</font>** Pengyiang Liu, Dongyue Lyu, Junbo Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous video counting requires distinguishing new observations from new objects or completed events. We introduce StaMina (State Maintenance), which learns to maintain counting state through state-conditioned updates. Recurrent visual context supports recognition; learned transitions maintain visibility, persistent identities, and completed-event records. A differentiable recurrence trains event transitions over legal paths constrained by count endpoints; visibility and association objectives train the object branch. A multi-source pipeline organizes 39.8K spatial queries and complementary event annotations into counting trajectories. On SVCBench, we evaluate counting adaptation with partial video overlap and held-out groups of linked annotations. Under prefix replay (Full) and persistent streaming (Stream), 4B and 8B models reach 41.9/36.4 and 44.9/38.2 Gaussian Precision Accuracy, respectively. The 8B model gains 10.9/3.2 points over Counting-SFT on the same queries. Matched-graph comparisons isolate phase conditioning and trajectory supervision, assessing training objectives alongside hard decisions. Online video benchmarks and count-conditioned decisions assess online understanding and task eligibility. Project Page: this https URL

---


### 837. [Indistinguishability of Sum of Permutations: A Fourier Analytic Route to Classical and Quantum Security](https://arxiv.org/abs/2609.35421)

**<font color=#1a73e8>作者：</font>** Ritam Bhaumik, Chun Guo, Xiaoning Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study classical and quantum indistinguishability of sums of independent random permutations and related transformations from permutations to functions. Let $G$ be a finite abelian group of order $N$, and let $\pi^k_+(x)=\pi_1(x)+\cdots+\pi_k(x)$ for $k\geq2$ independent uniform random permutations of $G$. We give a unified Fourier analytic treatment in which the construction is represented by its probability density and a distinguisher by its acceptance function, with the classical and quantum query models imposing different restrictions on the Fourier support of the latter.
Classically, we obtain the bound $O_k(q/N^{k-1/2})$ for every $q<N$, and refine it below the birthday threshold to $O_k(q^2/N^k)$. In the quantum model, a simulation argument gives $O_k(N^{-(k-3/2)})$ for $q\leq(N-1)/2$, while Fourier interpolation gives concrete finite bounds up to $q\leq4N/15$ and the query-dependent bounds $O\left(\min\left\{N^{-1/2},q^3/N^2 + 1/N\right\}\right)$ and $O_k\left(\min\left\{q^3/N^k,N^{-(k-3/2)}\right\}\right)$, for $k=2$ and $k \geq 3$, respectively, throughout $1\leq q\leq(N-1)/2$. For $q = 1$, the first bound sharpens to $O(N^{-2})$. Over $G=\mathbb F_2^n$, a one-query Fourier attack matches the order of our one-query bound, while an $N/2$-query parity attack with advantage $1/2$ shows that our bounds reach the constant-advantage query threshold.
We further study two variants of sum of permutations over binary vector spaces. First, we allow arbitrary surjective linear postprocessing, which includes truncation, and obtain classical and quantum bounds that retain the output-size dependence. Second, we analyse Dinur's variable-output single-permutation construction, $\mathsf{LXoP}$, for every fixed output width, and derive its classical and quantum security bounds; for one- and two-block outputs, we give concrete quantum security bounds.

---


### 838. [Building Transformation Layers for Riemannian Neural Networks](https://arxiv.org/abs/2609.35436)

**<font color=#1a73e8>作者：</font>** Ziheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, deep neural networks on manifold-valued representations have garnered significant attention across various machine learning applications. One recent focus is the generalization of Euclidean fully connected (FC) and convolutional layers to non-Euclidean geometries. However, previous approaches typically focus on a few selected manifolds and rely on specific properties of the target manifold. In contrast, this work proposes a framework for constructing FC and convolutional layers over computationally tractable Riemannian spaces. This framework incorporates several previous FC layers across different geometries as special cases and is instantiated on ten representative manifolds, including three hyperbolic models, five geometries of the symmetric positive definite (SPD) manifold, and two Grassmannian perspectives. Experiments on different manifolds demonstrate the effectiveness and applicability of our approach. Code can be found at this https URL.

---


### 839. [Riccati State Space Models: Non-iterative Parallelization for Nonlinear Sequence Modeling](https://arxiv.org/abs/2609.35441)

**<font color=#1a73e8>作者：</font>** Mónika Farsang, Ramin Hasani, Daniela Rus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State space models (SSMs) achieve efficient sequence processing because their affine state updates are closed under composition and can therefore be evaluated with an associative parallel scan. Nonlinear recurrent models can provide richer, state-dependent dynamics, but generally lose this compositional structure: parallel evaluation then requires iterative methods that repeatedly linearize and scan the recurrence. We ask, what state-dependent nonlinear dynamics can be designed to remain exactly composable? We answer by introducing RiccatiSSM, a nonlinear SSM, in which each state dimension follows an input-conditioned Riccati differential equation. Its quadratic state dependence makes the local Jacobian explicitly state-dependent, while its exact per-step flow under piecewise-constant inputs is a Möbius transformation. Since Möbius maps are closed under composition and compose through $2\times 2$ matrix multiplication, the complete nonlinear state trajectory can be evaluated exactly with a single associative parallel scan, without iterative linearization. We further derive a constrained parameterization that ensures bounded, contractive dynamics, and avoids poles in the fractional-linear state update. Across long-sequence classification, regression, and forecasting tasks, RiccatiSSM achieves competitive predictive performance while reducing runtime by $22{-}33\%$ compared to the nonlinear LrcSSM under matched architectures. These results demonstrate that state-dependent nonlinear dynamics can retain exact composability and be evaluated efficiently within a single parallel scan.

---


### 840. [Just Initialize: A Training-Free Initialization Component for Large-Scale Routing Optimization](https://arxiv.org/abs/2609.35443)

**<font color=#1a73e8>作者：</font>** Jiale Zhao, Sirui Mao, Zimu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale routing problems are difficult to solve efficiently as their search spaces grow rapidly with problem size. Existing approaches primarily improve the optimization procedure itself, often at increasing computational cost. We instead shift the focus to a useful initialization that can be refined into a high-quality solution with limited downstream refinement. We propose Just Initialize, a training-free and solver-agnostic initialization component for large-scale routing optimization. Just Initialize compresses a large routing instance into a compact surrogate space, optimizes its global routing structure, and recovers the resulting solution as an optimization-friendly starting point in the original space. Extensive experiments on Traveling Salesman Problems (TSPs), Capacitated Vehicle Routing Problems (CVRPs), Vehicle Routing Problems with Time Windows (VRPTWs), and Prize-Collecting Traveling Salesman Problems (PCTSPs) demonstrate that Just Initialize achieves high-quality solutions comparable to or better than state-of-the-art methods while substantially reducing computational cost across instances ranging from 1K to 100K nodes, including an average speedup of approximately 70$\times$, sub-second runtimes on 10K-node instances, and runtimes within tens of seconds on 100K-node instances.

---


### 841. [DiMoP: Diffusion-Driven Motion Representation Learning With Frame-Level Pseudo-Classification for Skeleton-Based Action Recognition](https://arxiv.org/abs/2609.35444)

**<font color=#1a73e8>作者：</font>** Shanaka Ramesh Gunasekara, Wanqing Li, Nikalal Kaldera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust skeleton-based action recognition requires representations that capture a wide spectrum of motions, from subtle to moderate and strong ones. Existing methods often focus on strong motions. This paper introduces DiMoP, a masking- and diffusion-driven motion representation learning method with frame-level pseudo-classification to explicitly learn the distribution of joint motions rather than regressing deterministic coordinates, as existing methods often do. By diffusing masked joints with progressive noise and denoising them conditioned on visible joints, DiMoP learns through controllable noising and denoising processes, enabling uniform learning of weak, moderate, and strong dynamics. To enable the masking-based generative diffusion learning with a discriminative capability, a pseudo-frame classifier is proposed that enforces the learning towards sequence-consistent and temporally coherent pseudo-labels without manual annotations. Together, these strategies provide a principled mechanism for joint generative and discriminative motion modeling. DiMoP achieves state-of-the-art performance across NTU RGB+D 60/120, and PKUMMD, including a 1.1 percentage point gain over prior works on NTU RGB+D 120 with the cross-subject protocol.

---


### 842. [NeuronSifter: Intervention Planning in CNS Microenvironments](https://arxiv.org/abs/2609.35445)

**<font color=#1a73e8>作者：</font>** Haowei Xu, Wanyi Fu, Hongbin Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prioritizing central nervous system (CNS) interventions requires predicting how a dose, route, and schedule act on a partially observed microenvironment, then choosing the measurement that would change the decision. Action-conditioned predictors reduce a regimen to an identity token or a scalar exposure, discarding where and when the target is engaged; handing a point estimate to a separate planner then discards the joint uncertainty that makes a measurement worth running. We therefore treat decision quality as a property of the intervention interface, not of controller placement. NeuronSifter compiles regimens into state-conditional target-occupancy fields with support masks, propagates them through microenvironment dynamics with an occupancy-conditioned diffusion operator, and selects measurements by their expected reduction in intervention loss, assimilating typed outcomes into the same posterior. In a declared synthetic Alzheimer's disease (AD) evaluation over 64 paired scenario blocks, occupancy conditioning lowers trajectory continuous ranked probability score from 0.165 to 0.110 and raises intervention ordering accuracy from 0.760 to 0.880, and every paired benchmark contrast remains separated after Holm correction. Decision-directed acquisition attains terminal risk 0.160 against 0.166 for a matched numerical Bayesian experimental design planner, and reaches the target risk at 0.796 $[0.732,0.873]$ of an earlier design control's cost, while the corresponding ratio against the matched planner, 0.963 $[0.907,1.025]$, is not separated from equality; point-state and dependence-ablated interfaces instead raise risk to 0.220 and 0.199, and a full-posterior external controller ties exactly. Published AD trials supply a separate retrospective endpoint bridge.

---


### 843. [Manifold-Stable Flow Matching](https://arxiv.org/abs/2609.35454)

**<font color=#1a73e8>作者：</font>** Amirhossein Nazerian, Ali Pezeshki, Jianguo Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching (FM) learns generative dynamics through velocity regression. Geometric FM variants commonly assume a prior supported on the data manifold, requiring geometric knowledge that is often unavailable. Without such knowledge, low regression error alone does not guarantee manifold adherence. Adherence keeps generated samples within valid configurations and is empirically associated with better task performance. We introduce manifold-stable flow matching (MSFM), which can start from an arbitrary ambient prior, not necessarily supported on the manifold. Using tools from nonlinear dynamics, namely contraction theory, MSFM combines learned tangential transport with prescribed normal contraction. The construction uses analytical projectors for known manifolds and local affine proxies estimated by principal component analysis for unknown data geometry. By implementing contraction theory in both cases of known and unknown manifolds, we guarantee manifold invariance and transverse convergence to the manifold within a desired time window (e.g., one second). We derive a family of compatible probability paths and decompose the training loss into a learnable tangential term and a normal residual. An ellipse experiment attains a mean terminal off-manifold error of order $10^{-6}$. In Push-T robotic experiments, MSFM raises success from $74\%$ to $82\%$. In the Robomimic Square task, success increases from $60\%$ to $72\%$, while rotation-manifold deviation decreases from order $10^{-2}$ to $10^{-7}$. The MSFM terminal geometric errors are controlled by the chosen numerical tolerance. These results demonstrate stronger geometric adherence and higher observed task performance, supporting prescribed normal contraction as a complement to learned generative transport.

---


### 844. [CLIMB: A Clinical Multimorbidity Benchmark for Diagnosing Co-occurring Conditions through Multiturn Conversations](https://arxiv.org/abs/2609.35462)

**<font color=#1a73e8>作者：</font>** Yusuf Kesmen, Aniruddha Mukherjee, Yena Chang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patients often have several co-occurring clinical conditions, and the findings needed to identify and disambiguate them emerge over the course of a consultation. Evaluating clinical reasoning in this setting requires both multi-turn interaction and multi-label diagnosis. We introduce CLIMB, a benchmark in which a doctor model interviews a simulated patient to recover a ground truth set of co-occurring clinical conditions. Cases are synthesized from clinical decision algorithms and diagnostic datasets, grounding multimorbid presentations in structured clinical knowledge. Across six frontier and open models, none recovers the exact set of conditions in more than 10% of interactive cases. Diagnostic performance declines when conditions co-occur, even when models receive the full clinical record and the true number of conditions. Interaction reduces performance further. In controlled experiments, models behave like single-hypothesis trackers: they anchor on the diagnosis suggested by the opening findings, keep questioning around it, and recover a second condition mainly when a finding in view points to it. Questioning them further does not complete the set but adds mostly wrong diagnoses. We formalise this pattern with a theoretical reference model of single-hypothesis tracking. The benchmark, generator, and evaluation code are available at this https URL.

---


### 845. [W2Rep: Learning Visual Representations by Watching the World Change](https://arxiv.org/abs/2609.35464)

**<font color=#1a73e8>作者：</font>** Wen Huang, Hang Guo, Jiarui Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images capture the world at one moment, whereas video reveals how it changes. Image self-supervision learns spatial structure from a single moment, while video methods commonly learn temporal relationships inside a representation computed jointly from several frames. We ask whether watching a scene change can instead improve features available from one image without sacrificing the ability to represent video. We introduce W2Rep, a masked feature-prediction framework in which an independently encoded source image participates in prediction at the same or another moment. The predictor is conditioned on visible video context, the queried location, and the signed time interval between source and target. This gives the cross-frame objective two complementary roles: the image path learns features that remain useful across time, while the video path must gather evidence that is missing from the source image. Across model scales and downstream tasks, W2Rep improves frozen and fine-tuned recognition under our comparison protocol, while joint video encoding provides further gains over frame-wise aggregation. Controlled experiments show that these gains depend on directly updating the source-image features and on using both video context and temporal displacement. Overall, change across a video can supervise a visual encoder whose representations remain useful at either image or video granularity. Code is available at~\href{this https URL}{this https URL}.

---


### 846. [An analysis of Mirror-Descent Soft Actor-Critic](https://arxiv.org/abs/2609.35466)

**<font color=#1a73e8>作者：</font>** Denis Zorba, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soft Actor-Critic (SAC) is widely used for entropy-regularised reinforcement learning with continuous action spaces, and practical implementations perform only a few actor steps towards an evolving target. In this work, we prove convergence guarantees when the target policy arises from policy mirror descent and compare it with the classical Gibbs target. We derive sufficient conditions for the strong convexity and smoothness of the actor objective, characterised by the curvature of the $Q$-function estimate through the Legendre differential operator, and establish an $\mathcal{O}\!\left(N^{-\frac{1}{5}}\right)$ best-iterate finite-time convergence rate up to actor and critic approximation errors. Moreover, the mirror-descent step size $\lambda$ directly controls the target drift and hence actor tracking error, whereas the analogous Gibbs bound contains a non-vanishing tracking term.

---


### 847. [Universal Approximation of Measure-to-Measure Operators by Pushforwards](https://arxiv.org/abs/2609.35483)

**<font color=#1a73e8>作者：</font>** Takashi Furuya, Nicholas H. Nelsen, Frank Cole  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learning tasks map an input distribution to an output distribution. A natural way to model such an operator is to transform each input sample using a continuous function that may depend on the entire input distribution, and then take the distribution of the transformed samples. This defines a measure-dependent pushforward model and includes measure-theoretic formulations of transformers. We ask when such models can approximate arbitrary continuous operators between spaces of probability measures. We first show that universal approximation fails when atomic inputs are allowed: some continuous measure-to-measure operators that split or redistribute atomic mass cannot be approximated arbitrarily well by deterministic pushforward models. We then introduce the uniform level set condition, which requires a continuous measure-dependent scalarization whose shrinking level set neighborhoods carry uniformly vanishing mass over the input family. This condition is satisfied, in particular, by compact families of absolutely continuous measures. On every compact family satisfying this condition, we prove that any continuous measure-to-measure operator with outputs of finite $p$-th moment can be uniformly approximated, in the $p$-Wasserstein distance, by continuous measure-dependent pushforwards. Combining our theorem with existing approximation results for measure-dependent in-context maps yields universal approximation by measure-theoretic transformers. We also extend the framework to continuously-varying source measures, yielding a corresponding universality result for a class of pushforward models that are closely aligned with cross-attention architectures.

---


### 848. [Beyond Scalar Probes: Exploiting Vector-Valued Outputs in ReLU Networks For Signature Extraction](https://arxiv.org/abs/2609.35487)

**<font color=#1a73e8>作者：</font>** Gorka Abad, Claude Carlet, Ermes Franch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We revisit cryptanalytic extraction of ReLU networks from a geometric and algebraic perspective. Rather than restricting attention to a single output component, we study the full vector-valued behavior across adjacent linear regions. This leads to a rank-one characterization of Jacobian differences that recovers the usual row-signature information while also revealing complementary column-side information. Our experiments show how this additional structure can be used in ex- traction and improves numerical estimation under different numerical- precision regimes (float64, float32 and float16). We extend the analysis beyond the high-precision and output-rounding settings commonly con- sidered in the literature towards the low-precision settings encountered in many practical settings.

---


### 849. [AHMAD: Adaptive Hybrid Multi-task Vision Learning with Assisted Distillation for Keypoint Detection](https://arxiv.org/abs/2609.35490)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi, Nedyalko Prisadnikov, Yuqian Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalist multitasking vision models aim to unify multiple vision tasks within a single framework, enabling more efficient and versatile learning. However, handling diverse vision tasks -- spanning dense and sparse predictions -- remains challenging due to their inherently varying output structures. In this paper, we propose AHMAD, a simple yet effective framework for generalist multitask learning that integrates different key vision tasks: semantic segmentation, instance segmentation, depth estimation, keypoint detection, and object detection. Our approach incorporates these five tasks into a unified structure: a shared encoder-decoder with several lightweight task-specific projectors. Under the multitask learning paradigm, we observed a complementary performance gain, achieving a state-of-the-art PQ of 53.1 and an mIoU of 66.5 for COCO-val panoptic and semantic segmentation, respectively. Additionally, for top-down keypoint detection, which typically incurs high computational overhead due to multiple forward passes, we introduce a knowledge distillation-based method that enables a single forward pass over the entire image, greatly improving efficiency. Ultimately, our model delivers a lightweight yet effective generalist multitask learning framework, demonstrating strong performance across five vision tasks.

---


### 850. [From Scores to Samples: Elastic Forcing for Autoregressive Video Generation](https://arxiv.org/abs/2609.35491)

**<font color=#1a73e8>作者：</font>** Chi Zhang, Yueyi Liu, Haoyang Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video generation commonly relies on Distribution Matching Distillation (DMD), requiring a bidirectional diffusion teacher and an online fake-score model. We instead learn the rollout distribution directly from reference videos, eliminating both score models during post-training. Our framework minimizes maximum mean discrepancy (MMD) in frozen self-supervised video representation spaces, using a hybrid Nyström--Monte Carlo estimator to balance approximation bias and sampling variance. Memory-efficient replay and gradient subsampling make this objective practical. Using the same architecture and initialization as Self-Forcing, our 1.3B model improves the VBench Total score from 83.80 to 84.64 while retaining 17 FPS. Removing auxiliary score models also enables 14B post-training on eight H200 GPUs. Beyond distillation, learning from reference videos enables the acquisition of new visual styles, semantic concepts, and spatial priors without a target-specific diffusion teacher.

---


> [!TIP]
> 当前位于：**801-850**（第 17/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-850** | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
