# 📦 其他研究 | 2026年10月06日

> 本类共 **260** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-260](./part-06.md)

---

### 151. [A Benchmark for Spatially Grounded Gesture Generation](https://arxiv.org/abs/2610.03105)

**<font color=#1a73e8>作者：</font>** Anna Deichler, Rishabh Dabral, Fethiye Irmak Dogan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Communication in shared space interweaves verbal and non-verbal signals, and pointing gestures anchor language to the environment: "put the cup on that one" is uninterpretable without the gesture that fixes the referent. Yet no common framework exists for evaluating whether generated gestures indicate their intended referent; distributional metrics reward a gesture aimed at the wrong object as long as it looks natural. We introduce a benchmark for spatially grounded gesture generation, comprising ~2K pointing-annotated clips from naturalistic VR dialogue with ground-truth 3D referents, a task in which systems must decide when, how and where to point within conversational speech, and a protocol that separates temporal alignment, spatial grounding and perceived naturalness. We also provide a flow-matching baseline, MM-Conv-Flow. Evaluating it alongside an independent retrieval-based system and captured human motion, we find that geometric grounding can exceed that of human pointing without any gain in perceived naturalness, showing that referential gesture quality must be measured along separate dimensions.

---


### 152. [Exploring the Trade-Off Between Structured Pruning and Fault Tolerance in Deep Neural Networks for Space Applications](https://arxiv.org/abs/2610.03117)

**<font color=#1a73e8>作者：</font>** Toon Vinck, Naïn Jonckers, Jaro De Roose 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) inherently exhibit a degree of robustness to bit-level faults due to their distributed representation of information. As a model increases in width, this information becomes more dispersed, theoretically reducing the impact of any single bit fault. In this paper, we empirically investigate the relationship between model width and robustness to Single Event Upsets (SEUs). We conduct a comprehensive experiment in which baseline models undergo iterative structured pruning to reduce their width while preserving task performance as much as possible. At each pruning stage, we run a targeted fault-injection campaign to evaluate the model's performance under simulated bit-flip scenarios. Our results show that, although structured pruning increases per-inference sensitivity to faults by reducing redundancy, this effect is effectively counterbalanced by shorter execution time, which lowers the probability of encountering an SEU. These findings suggest that structured pruning can yield significant energy and latency savings without compromising overall reliability, providing useful guidance for designing robust AI systems for space applications.

---


### 153. [How to Find and Reuse Policies for Continuous Adaptation in Lifelong Reinforcement Learning](https://arxiv.org/abs/2610.03119)

**<font color=#1a73e8>作者：</font>** Saptarshi Nath, Inish M. D'Souza, Antonio Carta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In lifelong reinforcement learning, retaining previously learned policies is not sufficient for effective transfer to a new task. Useful knowledge may be distributed across several prior policies, and its relevance may change as the learner acquires experience. One hypothesis is that task similarity can be effectively used in a continual learning setting to find and combine previously learned policies. To test it, Adaptive Mask Selection and Composition (AMSC) is designed to estimate similarity from online experience via non-parametric Wasserstein task embeddings from state-action-reward samples. The z-score-normalized sparsemax of the similarity scores are used to derive a variable-size support to periodically choose and weight policies to form a prior when learning a new task. On CT-graph and MiniGrid, AMSC achieves higher mean performance and forward transfer than the evaluated modular composition baselines while exhibiting no forgetting. Results on Continual World suggest that identifying relevant prior knowledge and determining its layer-specific composition may require additional layer-specific tuning. Ablations show that selecting relevant sources and determining how strongly to reuse them are central to these gains. Independently measured pairwise transfer is also positively associated with task-embedding similarity. These results indicate that task similarity can be an effective criterion to select and weight specific knowledge for reuse in lifelong reinforcement learning.

---


### 154. [In-Distribution Forcing for Long Video Generation at Test Time](https://arxiv.org/abs/2610.03120)

**<font color=#1a73e8>作者：</font>** Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern autoregressive (AR) video diffusion models excel at short-horizon video generation, yet generating long videos remains challenging due to drifting, where colors and textures shift, and motion dynamics decay. Existing works primarily rely on KV conditioning, which selects or modifies cached key-value (KV) entries to mitigate drifting. However, we observe that KV conditioning alone is insufficient as it assumes cached KV entries remain in-distribution. This assumption fails beyond the training horizon: nothing constrains the construction of KV entries during rollout, giving rise to the KV-provenance problem where cached entries themselves become out-of-distribution (OOD). To address this, we propose In-Distribution Forcing (ID-Forcing), a test-time framework that aligns both KV caching and KV conditioning with training configurations. Its key mechanism, self-caching, prevents OOD KV entries at their source. Each chunk is cached without attending to prior KV entry, keeping the rolling window exactly in-distribution. Consequently, ID-Forcing seamlessly extends short-horizon models to minute-scale video generation. Extensive evaluations show that our method remains competitive on standard video generation benchmark while substantially outperforming prior work in mitigating drifting, as validated by both our drift metrics and a user study.

---


### 155. [Coverage You Can Steer: Online Conformal Calibration for RL-Driven Hardware-Aware NAS](https://arxiv.org/abs/2610.03127)

**<font color=#1a73e8>作者：</font>** Pedro Brandimarte, Nerea Aranjuelo, Marcos Nieto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hardware-aware neural architecture search (NAS) is dominated by evaluation cost: every architecture must be trained before its reward is known. Conformal-prediction filters cut this cost by pruning candidates whose predicted-reward upper bound misses a threshold, with a distribution-free guarantee that at most a fraction $\delta$ are wrongly discarded. That guarantee assumes exchangeability between calibration and test candidates, which the surrounding reinforcement-learning (RL) loop violates: the policy's proposals improve as search proceeds and, in layer-by-layer construction, shift within every episode. We replace one-shot quantile estimation with online feedback control (Adaptive Conformal Inference, with tuning-free, locally-adaptive, and group-conditional variants), restoring steerable coverage: dialing the target delivers it, monotonically and reproducibly, for arbitrary sequences. Across three neural-network architecture families and both single-step and sequential search (three seeds), it tracks every requested level to within ${\sim}10^{-3}$ while pruning 25-50% of evaluations at no measured accuracy cost, whereas static calibration loses control of its coverage and a Gaussian-process baseline stays conservative regardless of the request. Finally, used as an acquisition function on one constrained testbed, the same optimistic bound beats random search, a gain that fixed optimism already carries and online calibration sharpens. The source code is available at this https URL.

---


### 156. [Keeping JEPA World Models Plannable When Little of the Frame Moves](https://arxiv.org/abs/2610.03137)

**<font color=#1a73e8>作者：</font>** Florian Strohm, Patrick Wagner, Jannik Schwab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Specifying a goal in language rather than as a goal frame is a natural interface for planning with a latent world model, but testing it needs scenes in which language must discriminate between several objects. We build SLIM, a pushing benchmark with several small objects and paired visual and language goals on identical scenes. On SLIM a LeWM world model that solves PushT succeeds on under 1% of trials, although a scripted controller with simulator state solves every tier. Probes locate the failure in the encoder: its latent is nearly action-insensitive, neither pusher nor object positions can be decoded from it, and rollouts are no better than copying the current latent forward. One inverse-dynamics auxiliary loss, applied to encoder latents and to predicted latents through a shared head discarded at test time, restores every probe and raises success from 0.003 to 0.35 (0.16 on the hard pushing tier, where a goal-agnostic policy scores zero), and improves PushT at twice the trained horizon. Controls attribute the repair to the gradient into the encoder, and a response sweep shows that the vanilla model plans once enough of the frame responds to actions. A cheap action-sensitivity probe, computable without environment access, acts as an empirical necessary condition: all configurations below its threshold failed to plan. On the repaired latent, a small language-goal head plans from sentences without retraining the world model: it reaches 0.84 on navigation (visual-goal oracle 1.00), follows the named zone when it is swapped with a decoy, and degrades gracefully to unseen nouns. A single goal sentence rarely completes a push, but given the push as a sequence of stage sentences the head raises success on the medium and hard pushing tiers from 0.04 to 0.25, on par with the goal-frame oracle, also when the switch between stages is read from the latent alone.

---


### 157. [CalCErt: Bin-wise Certification of Confidence Calibration in Medical Image Classification](https://arxiv.org/abs/2610.03142)

**<font color=#1a73e8>作者：</font>** Leo Fillioux, Stergios Christodoulidis, Stergios Christodoulidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks remain vulnerable to adversarial perturbations, which can distort not only predictions but also confidence scores, undermining uncertainty calibration. While existing certification methods focus on preserving the predicted category, providing guarantees on how calibration behaves under adversarial attacks remains overlooked. In this work, we introduce CalCErt, a simple and efficient post-hoc strategy that certifies bin-wise confidence calibration for any pretrained differentiable classifier. Our approach combines empirical calibration estimates, statistical concentration bounds, and local Lipschitz estimates of the confidence function to derive data-dependent upper bounds on worst-case miscalibration within an $ell_2$-ball of radius R. We evaluate CalCErt across 11 medical image classification tasks and multiple adversarial perturbations, demonstrating substantially higher certified coverage than baseline strategies while maintaining competitive tightness. Our code is available at this https URL.

---


### 158. [Does Physics Live in the Activations? Localizing Physical Quantities in Video Diffusion Models](https://arxiv.org/abs/2610.03154)

**<font color=#1a73e8>作者：</font>** Jonas Kneifl, Jakub Skalski, Bartłomiej Twardowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models produce strikingly realistic sequences and are increasingly proposed as world models, yet recent benchmarks reveal pronounced deficits in their physical reasoning. This raises the question of whether these models internalize physical principles or merely reproduce familiar motion patterns. We address this by probing internal representations of video Diffusion Transformers (DiTs) for simulator-derived ground-truth physical quantities spanning kinematic motion and rigid-body dynamics under gravity and contact. We find that these quantities are linearly decodable with high accuracy early in the denoising process, substantially outperforming a baseline decoded directly from the model's own noised latents, indicating that the relevant physical information is actively constructed during denoising rather than already present in the input. Additionally, we show that activations at on-object tokens carry the relevant physical information and that quantities defined over multiple frames are readable from single latent frames. Hence, information is sharply localized within the token sequence and is computed globally but stored locally. The probes further show partial extrapolation, transferring to scene variations and object configurations outside their training regime, so what they read is not simply a correlate of the scenes they were fit on. When fitted directly in the full-resolution activation space, the probing directions can serve as steering vectors to change the model's output.

---


### 159. [Sample complexity of variance-reduced policy gradient: weaker assumptions and lower bounds](https://arxiv.org/abs/2610.03165)

**<font color=#1a73e8>作者：</font>** Gabor Paczolay, Matteo Papini, Alberto Maria Metelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several variance-reduced versions of REINFORCE based on importance sampling achieve an improved $O(\epsilon^{-3})$ sample complexity to find an $\epsilon$-stationary point, under an unrealistic assumption on the variance of the importance weights. In this paper, we propose the \algo (Defensive Policy Gradient) algorithm, based on defensive importance sampling, which achieves the same rate without any assumption on the variance of ordinary importance weights. We also establish lower bounds in a generalized black-box policy-optimization model that hides states and actions and permits parameter-dependent rewards. In this model, the optimal rates are $\Theta(\epsilon^{-4})$ with bounded-variance one-policy feedback and $\Theta(\epsilon^{-3})$ with mean-square-smooth coupled two-policy feedback. Under standard policy-regularity conditions, REINFORCE and \algo realize the corresponding oracle conditions and attain the $O(\epsilon^{-4})$ and $O(\epsilon^{-3})$ upper bounds, respectively. Although the lower bounds do not apply directly to the classical MDP interaction model in which these algorithms operate, this correspondence provides oracle-level evidence that the faster rate of \algo is optimal and genuinely separated from that of vanilla policy gradient.

---


### 160. [LiBRA: Detection-Aware Image Watermark Removal via Bidirectional Latent Optimization](https://arxiv.org/abs/2610.03166)

**<font color=#1a73e8>作者：</font>** Saibo Ye, Huajie Chen, Xin Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital watermarking supports source attribution for AI-generated images, but its reliability depends on resistance to removal attacks. Some attacks attempt to remove watermarks by forcing the decoded watermark to differ from the original. However, this can produce an inverted watermark that remains detectable, causing removal to fail, while further attempts to alter the watermark may unnecessarily degrade image quality. To address these limitations, we present LiBRA (Latent In-band Bidirectional Removal Attack), which aims to make watermarks undetectable while preserving image quality. Instead of continually pushing the watermark toward inversion, LiBRA adjusts the image to conceal the watermark without encouraging further changes that could degrade image quality. Some attacks keep pushing decoded bits away from the original watermark, even when further changes preserve detectability and damage image quality. With access to the watermark key and decoder, LiBRA makes bounded changes in a public autoencoder's latent space. Unlike inversion-driven objectives that cannot correct excessive inversion, LiBRA guides average decoding confidence toward random guessing from either direction. This helps avoid an inverted but detectable watermark. Leaving individual bits flexible allows image-quality constraints to favor less damaging changes, while an optional frequency-guided mask limits their location. We verify removal using an exact two-sided binomial test rather than assuming the confidence target guarantees success.

---


### 161. [Geometry-Aligned Semantic Matching for Cross-Modal Planar Image Registration](https://arxiv.org/abs/2610.03167)

**<font color=#1a73e8>作者：</font>** Zhiwei Wang, Defeng He, Yuxing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal image matching establishes stable and accurate geometric correspondences across modalities for planar registration. Existing semantic representations provide cross-modal consistency, but semantic similarity does not necessarily imply geometric correspondence. Meanwhile, fine-grained CNN features provide accurate local details but lack global cross-modal semantic guidance for stable refinement. To address these issues, we propose CDPM, which first establishes geometrically consistent semantic representations and then preserves their dominant role in correspondence estimation during fine-grained localization. Specifically, we progressively adapt DINOv3 using geometrically consistent cross-modal patch pairs, enabling feature similarity to better reflect true cross-modal spatial correspondences. We then construct a DINO-Centric Feature Pyramid, where multi-scale DINO representations maintain stable cross-modal correspondences, while a lightweight CNN branch provides auxiliary structural details for precise local refinement. Extensive experiments on three cross-modal datasets demonstrate the superior performance of CDPM. On VIS-IR, compared with the dense matcher RoMa, CDPM improves AUC@3/5/10/20 by 7.36, 13.40, 13.75, and 10.42 percentage points, respectively, and reduces mACE from 5.83 to 2.78 pixels. It also outperforms RoMa v2 across all metrics while requiring 45.6% fewer FLOPs. The online demo and dataset are available, and the code will be released on our project page at this https URL.

---


### 162. [FinNextAssist: Towards Professional Financial Deep Research Assistant](https://arxiv.org/abs/2610.03174)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Fengbin Zhu, Xuan Yao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Deep Research (DR) agents have demonstrated strong capabilities in complex, research-oriented tasks through autonomous planning, iterative retrieval, multi-step reasoning, and structured reporting. However, adapting DR agents to finance introduces unique challenges: financial analysis demands the joint completion of heterogeneous sub-tasks spanning diverse data types, tools, and analytical workflows. We identify three key requirements for a professional financial DR agent: integration of authoritative, heterogeneous financial data sources; specialized analytical tools and skills; and dedicated sub-agents for domain-specific sub-tasks. Building on these principles, we propose FinNextAssist, an end-to-end deep research framework designed for professional financial analysis. FinNextAssist decomposes the research process into four stages: Task Planner, Evidence Compiler, Reasoning Engine, and Report Assembler, and introduces two novel lightweight sub-agents: TabAgent, for cross-market financial table understanding, and HeteroAgent, for cross-modality heterogeneous financial data interpretation. Extensive experiments on FinDeepResearch, the Finance Agent Benchmark, and FinTMMBench-Web show that FinNextAssist substantially outperforms both strong proprietary and open-source DR agents, with ablation studies confirming the contribution of each component across diverse markets and languages.

---


### 163. [Reversing the Clock: Layout-Aware Recovery of Design Intent from Clock Distribution Networks](https://arxiv.org/abs/2610.03182)

**<font color=#1a73e8>作者：</font>** Sascha Tommasone, Zehra Karadağ, Christopher Pawlowicz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware reverse engineering supports competitive analysis and hardware assurance by recovering information about an integrated circuit (IC) from its physical implementation. While existing techniques primarily recover the gate-level netlist, which represents logical functionality, they often overlook physical design decisions such as placement, routing, delay insertion, and interconnect optimization. The clock distribution network encapsulates many of these decisions; however, no prior published work has recovered this network from a fabricated IC to infer design intent. We present a layout-aware methodology that recovers and analyzes the clock distribution network by integrating a recovered gate-level netlist with layout information extracted from scanning electron microscope imagery. Our four-phase pipeline recovers clock-tree topology, buffering, gating and switching, interconnect delay, and crosstalk-mitigation measures. We demonstrate our methodology on a commercial 450 nm IC, recovering a global H-tree backbone with local X-tree-like branching, identifying an independent clock tree and global clock gating, quantifying latency, skew, and routing lengths, and confirming the absence of dedicated crosstalk mitigation. Together, these findings let us reason about the designer's intent. To encourage further research and support reproducibility, we release our clock tree recovery algorithm as open source.

---


### 164. [PocketSplat: Mobile Gaussian Reconstruction via World-Space Latent Allocatio](https://arxiv.org/abs/2610.03192)

**<font color=#1a73e8>作者：</font>** Wenzhi Guo, Xianda Chen, Dongxuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile Gaussian reconstruction must satisfy two requirements: the reconstruction model must execute within a device resource envelope, and the resulting Gaussian asset must expose a representation size suited to downstream mobile use. Existing feed-forward Gaussian reconstructors commonly decode dense, image-aligned candidates whose final cardinality is implicitly determined by the input resolution and number of views. We present PocketSplat, a feed-forward framework for budgeted mobile Gaussian asset construction. Given a prescribed output budget, PocketSplat organizes dense geometry-aware latent candidates in predicted world space, allocates exact integer capacity across local latent cells, and decodes complete Gaussian attributes only for retained candidates. Cell-conditioned latent fusion aggregates repeated multi-view evidence before decoding, while spatial responsibility decoding adapts Gaussian support after local sparsification. Experiments on DL3DV and out-of-distribution benchmarks establish a strong quality--budget trade-off against feed-forward Gaussian reconstruction baselines. On Mip-NeRF 360, PocketSplat executes directly on a target iPhone and constructs compact, higher-quality Gaussian assets substantially faster than a deployable streamed MVSplat variant; native MVSplat and DepthSplat exceed the device memory budget.

---


### 165. [Contextual Flow Matching: Adaptive Step Selection in Flow Models for Efficient Visual Generation](https://arxiv.org/abs/2610.03202)

**<font color=#1a73e8>作者：</font>** Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow Matching enables high-quality visual generation via continuous-time dynamics, but inference remains costly due to multiple sequential function evaluations. Existing acceleration methods reduce the number of function evaluations but often introduce additional training overhead, degrade quality, or fail to account for input-dependent variability. We propose COFLOW, an inference-time method that adaptively selects the step counts each generation based on the prompt features. Our context-aware COFLOW is trained online with an unsupervised reward that balances inference efficiency and generation fidelity. Our method is plug-and-play, requiring no retraining of the underlying generative model. It generalizes to image and video generation, achieving over 2.5x speedup while preserving perceptual and semantic quality. We further provide a theoretical analysis establishing an O(1/K) forward-Euler discretization error bound under standard regularity conditions.

---


### 166. [The Effects of Air-Conditioning and Road-Traffic Noise on Perceived, Cognitive, and EEG Responses in a University Classroom](https://arxiv.org/abs/2610.03210)

**<font color=#1a73e8>作者：</font>** Yuanzhi Su, Cynthia Hou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Air-conditioning and road-traffic noise are common in classrooms, and their effects are often judged by cognitive performance. However, a sound that leaves performance unchanged may still be perceived differently or alter brain activity. In a within-participant design, this study tested whether perceived, cognitive, and EEG responses are consistent, and whether perceived and EEG responses distinguish conditions that performance does not. Sixteen students completed cognitive tasks in a university classroom under air-conditioning and road-traffic noise, each played back at 55, 60, and 65 dBA. Participants rated acoustic appraisal and perceived workload after each condition, and EEG was recorded during the tasks. The results show that cognitive performance did not differ significantly between conditions in any task. By contrast, noise was rated louder, less pleasant, and more arousing than a no-noise control, and all three ratings varied with sound level; perceived workload was also higher under noise. Task-period EEG power also showed significant differences between sources or levels in specific tasks and scalp regions. Within participants, relative EEG band power covaried mainly with loudness and pleasantness; louder and less pleasant ratings coincided with higher relative theta and lower relative gamma power. Associations with arousal and performance were rare, and none were found for workload. The three response types were thus only partly consistent, and perceived responses and EEG distinguished conditions that performance did not. Non-significant performance differences do not mean the conditions were equivalent for students. Assessments of air-conditioning and road-traffic noise in classrooms should therefore consider perceived responses alongside cognitive performance, with EEG providing complementary information on neural activity during tasks.

---


### 167. [HyperFuse: Fast Self-Supervised Node Embeddings for Attributed Hypergraphs](https://arxiv.org/abs/2610.03211)

**<font color=#1a73e8>作者：</font>** Megha P, Harshit Kumar, Srajan Agarwal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised hypergraph representation learning can produce informative node embeddings, but existing methods often require deep encoders trained for hundreds of epochs, making embedding generation costly even for hypergraphs with a few thousand nodes. This limits applications requiring embeddings for many or evolving hypergraphs. We present HyperFuse, a label-free pipeline for fast hypergraph representation learning. HyperFuse (i) computes structural node coordinates by maximizing a spectral relaxation of hypergraph modularity using Banerjee's hypergraph adjacency and a matrix-free operator with cost linear in node-hyperedge incidences; (ii) constructs multi-scale feature summaries and assigns bounded utility weights to hyperedges based on member stability under feature and membership masking; and (iii) trains a lightweight utility-weighted hypergraph encoder for 100 epochs using an invariance-decorrelation objective. We compare HyperFuse with TriCL, SE-HSSL, VilLain, and HypeBoy on nine public hypergraphs using six downstream classifiers and k-means clustering. On the eight datasets where all methods completed, HyperFuse required 8.7 s per dataset on average, achieving 13-179x geometric-mean speed-ups over the baselines. It achieved the highest average accuracy with five of six classifiers, while classification and clustering performance was not significantly different from TriCL and SE-HSSL. Compared with HypeBoy, HyperFuse was 13x faster and 2.1-4.1 percentage points more accurate across all classifiers. HyperFuse provides a practical approach for fast, repeated hypergraph embedding generation.

---


### 168. [Kernel Singular Value Decomposition with Extension to Multiple Data Sources](https://arxiv.org/abs/2610.03216)

**<font color=#1a73e8>作者：</font>** Xinjie Zeng, Qinghua Tao, Johan Suykens  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel Singular Value Decomposition (KSVD) learns a pair of singular vectors w.r.t. an asymmetric kernel matrix, which can be induced by two data sources, e.g., the queries and keys in self-attention or the rows and columns of a given matrix. In this work, we extend KSVD to multiple data sources, namely eKSVD, which conducts joint nonlinear feature learning upon asymmetric kernels. In the primal formulation, the projections associated with each data source are jointly learned to capture maximal information, while incorporating pair-wise couplings. With the Lagrangian and its Karush-Kuhn-Tucker (KKT) conditions, the optimization in the dual leads to a generalization of the shifted eigenvalue problem in Lanczos decomposition theorem of KSVD. Further, a covariance-based framework is derived together with using neural networks (NNs) for explicit feature mappings, complementary to the kernel-based interpretation and optimization. Numerical experiments verify the effectiveness of our eKSVD compared to methods based on Mercer kernels for tackling multiple data sources, and our innovation of deploying NNs demonstrates great flexibility for kernel methods.

---


### 169. [VisionMX: Unlocking Microscaling Post-Training Quantization for Vision Models](https://arxiv.org/abs/2610.03218)

**<font color=#1a73e8>作者：</font>** Elad Dror Cohen, Ofir Gordon, Lior Dikstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microscaling (MX) formats are emerging as a hardware-supported approach to efficient training and inference. They combine low-precision elements with shared block scales, but their impact on vision models remains underexplored. We systematically investigate post-training MX quantization across vision models and tasks. An analysis of direct conversion identifies three sources of error: block-scale representation, the poor alignment of some small convolutional weight tensors with nonuniform element grids, and the underuse of signed codes by nonnegative activations. These findings motivate VisionMX, a post-training MX quantization method that optimizes bounded weight rounding and applies a foldable affine correction to activations. We evaluate VisionMX across image classification, object detection, semantic segmentation, and low-light image enhancement using several MX-style formats. It improves on direct conversion and the evaluated post-training quantization baselines, with the largest performance recoveries in architectures most sensitive to MX conversion

---


### 170. [VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](https://arxiv.org/abs/2610.03221)

**<font color=#1a73e8>作者：</font>** Yutong Wang, Xingtong Ge, Enhuai Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video creation spans text-to-video (T2V), image-to-video (I2V), and condition-based generation, yet video diffusion models remain costly because they repeatedly evaluate large backbones during sampling. Distribution matching distillation (DMD) reduces this cost, but its reverse Kullback--Leibler (KL) objective can provide unstable or incomplete guidance when the student and teacher distributions have limited overlap. VDOT addressed this issue by adding optimal transport distillation (OTD), whose explicit coupling supplies geometric directions for condition-based generation. Balanced OTD, however, performs full-mass matching between the spatial tokens of each corresponding student--teacher frame pair. This assumption weakens for T2V and I2V, where one condition admits many valid outputs and spatial content need not align across different realizations. We present VDOT++, a unified distillation framework that applies the same training recipe separately to generators for the three task families. It makes OTD robust to output diversity through an asymmetric unbalanced formulation that allows unreliable student tokens to carry less mass while maintaining coverage of the teacher tokens. An $\ell_1$ ground cost further replaces mean-based aggregation with a more mode-preserving weighted median that limits the influence of distant transport targets. The two changes respectively determine whom to match and how the selected targets should be aggregated. We additionally combine distribution matching and adversarial refinement through sequential backward passes, and exploit the decoupled score networks for cross-scale distillation, where larger score networks improve a compact generator. Experiments on UVCBench, VBench, VBench-I2V, and the VACE benchmark show that the resulting four-step generators are competitive with many-step teachers and strong few-step baselines across all three task families.

---


### 171. [Uncertainty as a Proxy for Semantic Correctness in Diffusion-Based Medical Image Synthesis](https://arxiv.org/abs/2610.03224)

**<font color=#1a73e8>作者：</font>** Yuxuan Ou, Konstantinos Kamnitsas, OxAAA Study 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models can synthesise contrast-enhanced CT (CECT) from non-contrast CT (NCCT), avoiding contrast administration and its environmental and patient-access costs. However, visually realistic images are not necessarily anatomically correct, and the pixel-intensity and feature-space similarity metrics used to assess generation quality do not directly measure anatomical correctness. In this work, we investigate whether uncertainty can serve as a proxy for semantic correctness in diffusion-based medical image synthesis.
We study NCCT-to-CECT synthesis using AortaDiff, a multitask diffusion framework that jointly generates CECT images and lumen segmentations. The segmentation output provides an explicit representation of the generated vascular anatomy, enabling segmentation-derived errors to be used as a quantitative measure of generation correctness. Six methods spanning weight (Ensemble, HyperDiff, BayesDiff), architecture-perturbation (MCDropout), generative-stochasticity (RDS) and input-perturbation (TTA) uncertainty are compared at the pixel, region and image levels, and for detection of clinically relevant out-of-distribution (OOD) cases.
Uncertainty proves informative at all three spatial scales, remains informative on an external multi-centre dataset under distribution shift, and supports OOD detection. MCDropout stands out among the six: it ranks among the leading methods at every scale, generalizes well on the external dataset, and can be enabled at inference on any model already trained with dropout, so reliable uncertainty comes at no extra training cost. Uncertainty reliably flags severe failures but discriminates poorly among already high-quality images. These findings support uncertainty as a practical and computationally economical signal for quality filtering, reliability assessment and OOD detection in NCCT-to CECT synthesis.

---


### 172. [The Neuro-Physical Inverter: A Modular Framework for Magnetotelluric Inversion Coupling Ensemble Conditioning with Residual Learning](https://arxiv.org/abs/2610.03225)

**<font color=#1a73e8>作者：</font>** Jae Deok Kim, Sai Ravela, Rob. L. Evans  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the Neuro-Physical Inverter (NPI), a modular, uncertainty-aware framework for geophysical inversion that couples ensemble-based conditioning with constrained residual learning, demonstrated in the 1D magnetotelluric (MT) setting as a controlled testbed. The framework operates in two stages. An Ensemble-Conditional Gaussian Process (EnsCGP) conditions a prior ensemble of resistivity models on the observed response, producing a physically admissible reference ensemble. A residual-learning neural network then predicts targeted corrections to this reference, trained on synthetic data and fine-tuned per station for field application through a physics-coupled objective. Because an ensemble is conditioned, refined, and propagated through both stages, every estimate carries an associated ensemble spread. Synthetic experiments show that NPI systematically reduces ensemble-mean error without destabilizing the ensemble. Applied to broadband MT data from the Gabbs Valley geothermal region (Nevada, USA), NPI reduces the across-station mean misfit over the mid-period band while retaining comparable ensemble spread. The propagated ensemble yields a factor of uncertainty that serves as an operational measure of constraint within the assumed model class. Both stages are dimension-agnostic in formulation, and the design principles established here are intended to scale to higher-dimensional parameterizations.

---


### 173. [Seeing through the Eyes of AI: Situated Explainability in Augmented Reality](https://arxiv.org/abs/2610.03232)

**<font color=#1a73e8>作者：</font>** Ana Stanescu, Lucchas Ribeiro Skreinig, Tobias Langlotz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Explainable Artificial Intelligence (AI) enables humans to understand and interpret decisions of AI models. Instead of having a black box, explainability supports humans in understanding AI models' behavior. Existing explainable AI approaches often present explanations on 2D displays using pre-recorded data, requiring users to relate the displayed information back to the physical objects and real world locations involved in a model's decision. Users are forced to decouple data exploration and capture from AI model interpretation. For AI systems that work within physical environments, this separation can make explanations difficult to interpret in context. We propose using Augmented Reality (AR) to enhance the understanding of AI models by enabling spatial explainability information directly in a user's workspace, in real time, as they explore the world. We show how known explainability methods can be applied in AR and provide insights into user experiences with such an application.

---


### 174. [EmbPASS: Towards Cross-Embodiment Open Panoramic Segmentation](https://arxiv.org/abs/2610.03248)

**<font color=#1a73e8>作者：</font>** Pujun Guo, Yuanfan Zheng, Fei Teng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic images provide a complete 360-degree field of view, enabling comprehensive scene understanding for embodied perception. However, heterogeneous embodied platforms exhibit substantial differences in observation viewpoints and spatial layouts, giving rise to cross-embodiment observation shifts that pose additional challenges to consistent and reliable panoramic perception, while systematic studies of this problem remain limited. To bridge this gap, we introduce a new task, termed Cross-Embodiment Open Panoramic Segmentation. Meanwhile, we establish EmbPASS, a multi-platform panoramic semantic segmentation benchmark spanning Vehicle, Drone, Wearable, and Quadruped platforms under a unified semantic taxonomy, providing a testbed for systematically studying cross-embodiment panoramic perception. We further propose EPONet, an open-vocabulary panoramic semantic segmentation network that integrates Relation-Aware Metric Adapter (RAMA) and Content-Adaptive Semantic Transfer (CAST) to enhance spatial modeling and semantic transfer under heterogeneous embodied observations. Extensive experiments show that EPONet achieves the best platform-balanced performance on EmbPASS with 35.82% mIoU, outperforming the strongest baseline by 1.10%, while remaining competitive on existing panoramic segmentation benchmarks. The source code and EmbPASS benchmark will be made publicly available at this https URL.

---


### 175. [Learning a Fact Is Not Learning How to Retrieve It](https://arxiv.org/abs/2610.03251)

**<font color=#1a73e8>作者：</font>** Chaemin Jang, Jihee Kim, Dongman Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model trained on "The capital of X is Y" may produce "Y" after "The capital of X is" but fail after "The capital of X:". We call these different ways of eliciting the same fact request forms. To separate learning a fact from retrieving it, we train two models in two stages. In the first stage (request-form training), one model sees each fact in five forms and the other sees the same facts only as statements. In the second stage (target-fact training), both receive identical training on new facts, all as statements. Both then retrieve the new facts almost equally well from statements, but differ sharply on other request forms. Thus, a model can learn how to retrieve through a request form before it learns the facts. To understand this difference, we examine the hidden state immediately before the answer, which we call the context state. When given two different request forms for the same fact, the model trained on five forms in stage one produces more similar context states than the model trained on statements alone in that stage. Changing this state at retrieval time can enable or prevent retrieval of an already learned fact, and the same effect transfers across facts and factual relations, such as capitals and currencies. To test its role during learning, we change the context state only during target-fact training. This intervention changes later retrieval without intervention at test time. Together, these results show that later retrieval depends on earlier request-form experience and the context state during fact learning.

---


### 176. [Cross-cohort TB classification using clinical data gathered in Uganda and South Africa](https://arxiv.org/abs/2610.03256)

**<font color=#1a73e8>作者：</font>** Joshua M. Jansen van Vüren, Devendra S. Parihar, Daphne Naidoo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a first evaluation of machine learning applied to patient clinical and demographic data gathered in two different countries for the purpose of tuberculosis (TB) screening to identify people who would benefit from expensive molecular testing. Experiments are based on the recently-compiled CAGE-TB dataset, which includes sub-cohorts of people with presumptive TB presenting at community health care centres in South Africa and Uganda. Three neural network architectures (logistic regression (LR), multilayer perceptrons (MLP) and convolutional neural networks (CNN)) are considered in conjunction with greedy feature selection. For the convolutional neural network, a strategy that jointly optimises feature selection and feature ordering is proposed and shown to lead to consistent development and test set improvements. For all three models, development set area under the receiver operating characteristic (AUROC) curve is improved by 2-7% using feature selection. LR after feature selection achieves an AUROC of 0.8 [0.75,0.86] (95% CI) and 0.84 [0.78,0.9] when testing on the held-out Ugandan and South African data respectively. Although outperforming LR on the development cohort, the deeper networks (MLP, CNN) show inconsistent trends on the held-out cohorts, while LR achieves performance within 1-2% of the best achieved in terms of AUROC. LR narrowly misses the WHO minimum requirements by 4-9% in sensitivity even though the network is being evaluated on a completely held-out cohort. The development of neural-network based classifiers for TB screening therefore appears viable.

---


### 177. [Mapping and Advancing the Scalability-Accuracy Frontier of Nonlinear Causal Discovery](https://arxiv.org/abs/2610.03258)

**<font color=#1a73e8>作者：</font>** Hendrik Suhr, Sascha Xu, Jilles Vreeken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalable nonlinear causal discovery requires methods that combine flexible mechanism estimators with efficient search over large graph spaces. Several algorithmic families have been proposed to address this challenge, yet their accuracy-runtime trade-offs remain poorly understood. We empirically compare the four major approaches: differentiable structure learning, amortized structure learning, score-matching, and combinatorial search. Our results reveal complementary bottlenecks: differentiable and amortized methods scale well but exhibit an accuracy gap, score-matching methods can be accurate in low dimensions but degrade quickly for increasing feature sizes, and combinatorial methods remain accurate but are slowed by repeated and redundant local scoring. Motivated by this bottleneck, we develop SPADE, a spline-based score-evaluation scheme that compiles sufficient statistics once and reuses them throughout combinatorial search. Under bounded indegree, its Gaussian variant reduces algorithmic complexity from O(nd^3) to O(nd^2+d^3). Empirically, SPADE shifts the observed scalability-accuracy frontier by orders of magnitude: it solves 100-variable problems with 160K samples in seconds and 1600-variable problems with 2.5K samples in minutes, while retaining high structural accuracy across synthetic and real-world benchmarks. These results reveal a substantial shift in the practical scale of combinatorial search and highlight the importance of evaluating scalable causal-discovery methods along the full accuracy-runtime frontier.

---


### 178. [PaMIR: Open Benchmark of Public Credit-Default Datasets](https://arxiv.org/abs/2610.03259)

**<font color=#1a73e8>作者：</font>** Mikhail Liashkov, Ilyas Varshavskiy, Shuhratjon Khalilbekov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We release PaMIR (Public Arrival-ordered Measurement for Inference in Risk), an open benchmark for credit-default prediction when labels are scarce and arrive late. The field's reference benchmark studies use eight datasets each, only two or four of them public. PaMIR brings together 19 public datasets with binary default labels -- 1.24M loans, firms and card accounts from nine countries -- rebuilt from pinned source snapshots by one leakage-audited recipe and never redistributed; to our knowledge it is the one of its kind as of today. Every model is a single function, scored under a repeated i.i.d. split and a label-delayed stream in which each application is scored on arrival, with AUC reported by label budget; fleet means are withheld unless every dataset is scored. A synthetic-data harness tests generated training rows without letting a generator see held-out rows. This report describes release 0.4.0 of this living benchmark.

---


### 179. [Consecutive Posterior Fusion for Diffusive Recovery of Unobservable Image Structures](https://arxiv.org/abs/2610.03261)

**<font color=#1a73e8>作者：</font>** Elena Morotti, Davide Evangelista, Elena Loli Piccolomini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving severely ill-posed imaging inverse problems requires recovering image structures that are unobservable or weakly constrained by the measurements. Diffusion models provide expressive learned priors for inferring such missing information, while posterior sampling incorporates measurement consistency along the reverse process. Standard diffusion posterior samplers, however, rely on instantaneous measurement-aware estimates, without explicitly exploiting information carried by previous posterior corrections.
We introduce Consecutive Posterior Fusion Denoising Diffusion Null-Space Models (CPF-DDNM), an inference-time strategy that fuses consecutive measurement-aware estimates to improve the diffusive recovery of unobservable image structures, without requiring retraining or additional denoiser evaluations. We instantiate this principle within DDNM, whose range/null-space decomposition reveals that consecutive fusion preserves the measurement-determined component while acting exclusively on the prior-driven null-space estimate. We thus provide a geometric interpretation of CPF-DDNM and a local error analysis that characterizes the optimal time-dependent fusion coefficient, including the extrapolative regime.
Experiments on sparse-view and simulated low-dose computed tomography, as well as medical image super-resolution, show consistent improvements over DDNM and competitive performance against diffusion-based inverse solvers.

---


### 180. [Asymptotic Analysis of Trading Fees in CFMM](https://arxiv.org/abs/2610.03262)

**<font color=#1a73e8>作者：</font>** Peiyang Jin, Clouds, Jing Qian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the dominant trading mechanism in decentralized finance, Automated Market Maker has been widely studied in research. However, limited research has been done with the trading fees taken into consideration. In this work, we study how much trading fee Liquidity Providers(LPs) can receive from arbitrage trading when the fee rate approaches zero. We give a closed-form formula for it and our result shows that the trading fees generated by arbitrage trading can fully offset the LVR loss when the price process is continuous. We further extend our conclusions to price processes with jumps and the theoretical analysis shows that jumps are the only cause of LP loss apart from market risks. Our results provide practical guidance for AMM designers as well as LPs.

---


### 181. [Moving Forward with Video Saliency: A New Dataset and Benchmark where Motion Matters](https://arxiv.org/abs/2610.03276)

**<font color=#1a73e8>作者：</font>** Susmit Agrawal, Rebecca Wanner, Juliane Verwiebe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video saliency prediction is inherently harder to model than static image saliency due to the additional temporal dimension. Video saliency benchmarks rest on the premise that predicting gaze on video requires utilizing temporal activity distributed across frames. Prior work has challenged this, showing that static baselines recover a significant fraction of the explainable gaze information on LEDOV, a popular video saliency dataset, and that video saliency models fail in the same places as this static baseline. We verify that this diagnosis still stands: under a more capable gold standard than the original analysis, and an updated panel of recent architectures, the strongest temporal architecture in the panel still does not substantially improve over a fine-tuned static baseline. However, it remains unclear whether the marginal gain reflects limitations of current temporal architectures or a lack of temporal patterns in the benchmark itself. We introduce SalTempto, a video saliency benchmark with greater dynamism: 224 clips of highly dynamic content, sourced from the HACS-Segments dataset so that each clip contains an event together with its lead-up and aftermath, with gaze recordings from up to 16 subjects and a training split for adapting pretrained models. On SalTempto, the static baseline recovers only about 13\% of the headroom above the centerbias, against more than half on LEDOV. A fine-tuned temporal architecture shows a substantial gain in performance over the static baseline, indicating that it does capture meaningfully more temporal information, which LEDOV fails to measure. Yet, even this SoTA model still leaves nearly half of SalTempto's headroom unexplained, indicating room for improvement in video saliency modelling. Examination of SalTempto also lets us describe human tendencies that models miss. SalTempto link: this https URL.

---


### 182. [S$^{2}$-PINN: Stochastic Separable Physics-Informed Neural Networks](https://arxiv.org/abs/2610.03303)

**<font color=#1a73e8>作者：</font>** Zhendong Li, Akwum Onwunta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) for random partial differential equations (PDEs) is ubiquitous in computational science and engineering. However, classical spectral solvers for this class of problems face the curse of dimensionality, and existing neural solvers often ignore the stochastic structure that makes moments and calibration tractable. We introduce a stochastic separable physics-informed neural network, dubbed S$^{2}$-PINN, that represents the solution $u(t,\mathbf{x},\mathbf{Z})$ of a random PDE with a learnable Gaussian spatial dictionary, Fourier temporal features, and a generalized polynomial chaos (gPC) stochastic basis, coupled by a low-rank Canonical Polyadic (CP) tensor decomposition core. The method is trained with a hybrid strong-form and gPC-projected residual loss. Our theoretical analysis establishes that the separable class is dense in $L^2$ under mild conditions, and the projected residual corresponds exactly to a stochastic Galerkin constraint. Furthermore, we show that mini-batch projection coefficients are logarithmically dependent on the number of gPC modes, and that the orthogonality penalty controls the conditioning of the learned spatial dictionary. Using four manufactured random PDE benchmarks, we show that S$^{2}$-PINN outperforms nine baselines in terms of mean and variance accuracy, as well as calibration, while using significantly fewer parameters. Further evaluations on non-manufactured Poisson and Darcy problems, a stochastic Navier--Stokes problem, a diffusion scaling study of higher random dimensions, and two stochastic inverse problems reveal the generalization capabilities of the proposed structure. Together, these results support stochastic separability as an effective design principle for physics-informed neural UQ. The code for the experiments can be found in this https URL

---


### 183. [Training-Loss Guarantees for Muon with Finite-Step Newton--Schulz Orthogonalization](https://arxiv.org/abs/2610.03306)

**<font color=#1a73e8>作者：</font>** Amartya Roy, Souvik Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing convergence analyses of Muon either assume exact orthogonalization or analyze classical Newton--Schulz polynomials, and guarantee only stationarity, so it is unresolved what Muon's five tuned Newton--Schulz steps preserve and whether that suffices to reach a prescribed neural-network training loss. We establish a finite-time training guarantee that accounts for both momentum accumulation before orthogonalization and the tuned finite-step update. For full-batch training of a sufficiently wide two-layer ReLU network with fixed random output weights and a positive-definite limiting neural tangent kernel, we prove that Muon reaches any target empirical squared loss $\varepsilon>0$ with high probability over initialization. For every momentum parameter $\mu\in[0,1)$, a target-dependent constant learning rate proportional to $(1-\mu)\sqrt{\varepsilon}$ yields a hitting-time bound of $O((1-\mu)^{-1}\varepsilon^{-1/2})$, with other problem parameters fixed. The sufficient width is independent of both target accuracy and momentum. The analysis shows that the tuned Newton--Schulz map preserves alignment with the momentum buffer while bounding the update's spectral norm. Control of gradient variation near initialization transfers this alignment to the current gradient, ensuring descent until the target is reached without requiring exact orthogonalization. Numerical experiments support these mechanisms at widths below the sufficient theoretical threshold: gradient-update alignment remains above the analytical reference, and all 30 runs across six widths and five student initializations on a fixed teacher-student dataset reach the target loss while maintaining kernel positivity.

---


### 184. [T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction from Images](https://arxiv.org/abs/2610.03308)

**<font color=#1a73e8>作者：</font>** Atsuhiro Noguchi, Tianhan Xu, Yiming Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We reconstruct high-fidelity 3D scene meshes from posed multi-view images without per-scene optimization, across scales ranging from single objects to large outdoor scenes. Per-scene optimization methods lack the learned 3D prior needed when observations are sparse or surfaces are glossy or transparent. Existing generative methods leverage such priors to complete geometry in sparsely observed regions, but typically operate at a fixed resolution over a limited spatial extent, trading spatial coverage against detail. Reconstructing a large scene therefore often requires partitioning it into independently processed overlapping local regions, making it difficult to maintain global geometric consistency. To address these issues, we propose T3lescope, which applies a single fixed-resolution generator across scene scales in an inference-time coarse-to-fine cascade. A coarse level establishes the scene layout, and finer levels perturb and denoise geometry inherited from the coarser level within progressively finer spatial cells to recover surface detail. The model is trained on individual cells at multiple scales and shares its weights across all levels, so no hierarchy is fixed during training, and the number of levels, cell scales, and cell locations are determined at inference time. On indoor, outdoor, and city-scale scenes, T3lescope outperforms feed-forward and generative baselines, matches or surpasses per-scene optimization, and recovers fine structures as well as glossy and transparent surfaces. These results show that our method generalizes across diverse scenes, view counts, and image resolutions. Project page: this https URL

---


### 185. [Optimal Planning in a Dynamic World](https://arxiv.org/abs/2610.03312)

**<font color=#1a73e8>作者：</font>** Devin Wild Thomas, Solomon Eyal Shimony, Wheeler Ruml 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: We address the problem of planning when the set of feasible states or actions changes over time. For example, in the problem of path planning among moving obstacles (sometimes known as SIPP), the feasibility of being at a particular location can change as the obstacles move. Or, the action of boarding a particular train is feasible only while it is stopped at the station. This dynamism means that the optimal plan and its duration can change depending on when execution begins. In practice, execution start time is often unknown until planning has completed or another agent gives the go-ahead. However, most prior planning work either ignores dynamism or assumes a known start time. This makes it straightforward to assess state and action feasibility but is impractical for some applications. Objectives: In this paper, we relax the assumption of a known start time. We define the setting of {\em any-start-time planning} and provide algorithms for it. Methods: We present a data structure called a compound arrival time function (cATF) that compactly encodes the optimal plan as a function of start time. We provide general-purpose planning algorithms, based on heuristic graph search, that assemble cATFs by propagating functions along edges instead of scalar costs. Results: We prove that the size of a cATF is at most linear in the problem size. An experimental evaluation of an implementation for the specific problem of SIPP shows that, on difficult problems, agents that rely on replanning often fail, while any-start-time algorithms using cATFs can quickly look up the optimal plan once the execution start time is known. Conclusions: By enabling efficient representations and reasoning for time-dependent plans, this work provides a foundation for planning in dynamic worlds.

---


### 186. [Cordial Learning: Distributed Training with Correlated Data](https://arxiv.org/abs/2610.03330)

**<font color=#1a73e8>作者：</font>** Sarah Shitrit, Ilai Bistritz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider a distributed learning task with agents that have correlated data. Specifically, the label of an agent depends on the input of other agents for the same sample, and these inputs are also correlated. Correlated data is the reality when agents share the same environment. Existing decentralized methods, such as federated learning, ignore the structure of the problem and perform poorly on correlated data. On the other hand, centralized approaches are infeasible due to privacy and communication constraints. We introduce cordial (correlated and distributed) learning to address this gap by sharing only low-dimensional outputs between the agents while training local models to extract informative signals from peers. This distributed learning induces a game in which the loss function of each agent depends on the models of others. Assuming a linear model, we prove that cordial learning converges with probability one to a globally optimal solution, despite the nonconvex global objective. Experiments on structured multi-digit MNIST tasks demonstrate that cordial learning remains highly effective even in highly nonlinear settings.

---


### 187. [A Fully Automatic Pipeline for 3D Dendrite Instance Segmentation in SBF-SEM](https://arxiv.org/abs/2610.03332)

**<font color=#1a73e8>作者：</font>** Zewen Zhuo, Ilya Belevich, Eija Jokitalo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate three-dimensional (3D) reconstruction of individual dendrites in serial block-face scanning electron microscopy (SBF-SEM) is essential for quantifying structural plasticity in the brain, yet manual annotation at scale is infeasible. We present a fully automatic pipeline for 3D dendrite instance segmentation that unifies YOLOv6-guided Segment Anything Model (SAM) prompting on downsampled slices, iterative two-dimensional mask refinement, random forest 3D instance linking, and instance-aware high-resolution refinement using nnU-Net at native resolution into a single system requiring no manual prompting at inference. Applied to hippocampal CA1 SBF-SEM datasets from a control rat and a pilocarpine- induced epileptic rat, our pipeline reconstructs coherent, well- separated dendrites with high semantic accuracy (Dice 0.93 and 0.91) and strong instance-level performance on control tissue, while analysis of the more challenging epileptic tissue identifies instance recognition in dense regions as the principal remaining limitation. The high-resolution refinement stage recovers thin dendritic protrusions, providing a basis for downstream spine- level analysis. Code is available at this https URL ZE-WEN/dendrite-3d-instance-seg.

---


### 188. [Geometry Meets Physics: Data-Efficient Pre-Training for Unstructured Neural PDE Solvers](https://arxiv.org/abs/2610.03363)

**<font color=#1a73e8>作者：</font>** Luis Medrano-Navarro, Giacomo Baldan, Qiang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural surrogate models for Partial Differential Equations (PDEs) on unstructured 3D geometries are often limited by poor generalization and the high cost of generating large-scale training datasets. Consequently, pre-training on massive datasets of related PDE dynamics has emerged as a critical alternative to enhance the robustness and scalability of these models. However, this strategy is neither compute- nor data-efficient, as it relies on massive pre-computed data that is very costly to generate. In this work, we introduce a disk-data-free pre-training framework tailored to both steady-state and transient regimes. For steady-state problems, we propose a geometry-driven strategy that leverages intrinsic shape descriptors to learn representations of complex 3D domains. For transient problems, we introduce a physics-driven approach based on online generation of synthetic PDE data, enabling scalable pre-training without reliance on expensive datasets. Across multiple experiments, our approach achieves faster convergence, greater data efficiency, and higher accuracy during fine-tuning, particularly under realistic low-data regimes. This methodology provides a practical pathway toward data-efficient neural emulators for large-scale simulations.

---


### 189. [Multilingual GSM-Symbolic: What determines capability transfer across languages?](https://arxiv.org/abs/2610.03367)

**<font color=#1a73e8>作者：</font>** Kenneth Enevoldsen, Riley Herchert, Sofie Mosegaard 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We understand little about how capabilities acquired in one language carry over to another, or what governs this transfer: evaluations rely on incomparable, saturation-prone datasets and rarely examine its determinants jointly. Identifying what predicts transfer would let us avoid exhaustive evaluation across all language pairs and let developers target the factors that limit performance in low-resource languages. To evaluate cross-lingual capability transfer, we introduce Multilingual GSM-Symbolic, an extensible multilingual mathematical dataset covering 30,000 item-matched question-answer pairs and spanning 15 languages. It utilises symbolic templates to prevent overfitting and ensure generalisation by allowing generation of millions of high-quality variations from a single sample. Using Multilingual GSM-Symbolic, we quantify the largest determinants of capability as model size ($\beta = 1.77$), language resource level ($\beta = 0.77$), reasoning ($\beta = 0.67$) and typological distance ($\beta = -0.25$). This joint estimation allows these determinants to be expressed in terms of one another: a 32B model evaluated in Marathi performs like a 10B model in English. Our findings have important implications for model developers, showing that model size and reasoning narrow the performance gap between low- and high-resource languages ($\beta = -0.27$ and $\beta = -0.20$, respectively), while similar levers have little or no effect on typologically distant languages.
Overall, our analysis framework explains 92% of between-language variation, but only 23% of the model-by-language variation, and predicts a model's performance on an unseen language within 6.0pp (r=.96). Incorporating measurements from just 10 templates in the target language reduces this to 4.19pp, enabling reasonable estimates of performance with little or no downstream dataset.

---


### 190. [LAS-CLIP: A Lightweight Adapter Steering Approach for CLIP's Visual Encoder](https://arxiv.org/abs/2610.03370)

**<font color=#1a73e8>作者：</font>** Anh-Khoa Dinh-Duc, Duc-Tai Dinh, Tam V. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP's visual encoder produces only global image representations, limiting its use in region-level tasks. Existing adaptations rely on visual prompting, input masking, or encoder fine-tuning, each compromising pre-trained representations. We propose LAS-CLIP, a Lightweight Adapter Steering approach that keeps every CLIP parameter frozen. A compact MaskAdapter generates per-head, per-layer attention biases from an input mask and injects them into the frozen self-attention layers, steering attention toward the target region. Crucially, because the backbone remains strictly untouched, LAS-CLIP seamlessly reverts to vanilla CLIP when no mask is provided, preserving its foundational zero-shot capabilities. With approximately 116K to 145K trainable parameters and 100K training samples on two T4 GPUs, LAS-CLIP achieves competitive or superior results compared to Alpha-CLIP on ImageNet-S zero-shot classification and RefCOCO referring expression comprehension, despite the latter fine-tuning its entire encoder on millions of samples. Qualitative analysis further confirms stronger representational fidelity under incorrect masks and in downstream generation. Our project page is link to this https URL

---


### 191. [EVEWorld: Physical Evolution Supervision for Embodied World Models](https://arxiv.org/abs/2610.03374)

**<font color=#1a73e8>作者：</font>** Kaiqi Wang, Songxin Zhang, Zejian Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied world models enable scalable simulation of embodied interactions for robot learning. However, existing models are prone to Model Laziness, as they focus on visual fidelity at the expense of physical reasoning and lack process-level supervision over the temporal dynamics of manipulated objects. In this work, we propose EVEWorld, a physical evolution-supervision framework for physically consistent target evolution. EVEWorld consists of two components: Instance-Guided Restoration (IGR) and Temporal Instance Alignment (TIA). First, IGR promotes instance consistency through restoration supervision. Second, TIA promotes cross-frame consistency by aligning target instances across adjacent frames. We further introduce the Model Laziness Rate (MLR), a metric that measures persistent violations of instance consistency in generated trajectories. Extensive experiments on DreamGenBench, EWMBench, and PBench demonstrate the effectiveness of EVEWorld, notably achieving an 87.5% reduction in MLR compared with GigaWorld-0. On the WorldArena 2.0 Track 1 leaderboard, our model ranks 6th in JEPA Similarity and 17th overall, which further validates the performance of our evolution supervision strategy.

---


### 192. [Operator-informed initialization for Fourier features physics-informed neural networks](https://arxiv.org/abs/2610.03378)

**<font color=#1a73e8>作者：</font>** Juan Molina, Paris Perdikaris, Mircea Petrache 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) typically exhibit spectral bias, where some frequencies of the target function converge more slowly than others. In this work, we analyze the training dynamics of Fourier Feature PINNs in the Neural Tangent Kernel regime to address this limitation. We derive an explicit evolution equation to estimate the residual error in the frequency domain, demonstrating that the convergence rate of specific frequencies is primarily governed by the product of the differential operator's symbol and the spectral density of the initialization weights. Leveraging this theoretical insight, we propose an informative initialization strategy that tailors the initial weight distribution to the specific PDE being solved. With this method, we can diminish the operator-induced spectral bias, balancing the convergence rates across the frequency spectrum and achieving better prediction accuracy. Numerical experiments on linear and nonlinear partial differential equations confirm that this initialization strategy improves learning dynamics and approximation accuracy across frequencies compared to standard initialization methods, with no additional training cost.

---


### 193. [Interpretable Deepfake Detection in Videos via Explicit Forensic Features and Temporal Modeling](https://arxiv.org/abs/2610.03380)

**<font color=#1a73e8>作者：</font>** Chahira Benhama, Mohand Saïd Allili, Assia Hamadene  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection in videos remains challenging, as manipulated content may appear visually consistent at the frame level while exhibiting subtle temporal inconsistencies. This paper introduces an interpretable deepfake detection framework that models spatially and temporally coherent facial features in video sequences. Unlike end-to-end deep models relying on implicit representations, the proposed approach explicitly encodes physically grounded forensic cues, enabling transparent analysis and improved multi-dataset generalization. The pipeline transforms videos into identity-consistent facial trajectories, segments them into fixed-length temporal windows, and represents each frame using 68 structured descriptors spanning four complementary domains: photometric, textural, geometric, and compression-based features. These descriptors provide a compact multi-domain representation of manipulation artifacts and are processed by a Long Short-Term Memory (LSTM) network to capture temporal dependencies and subtle irregularities. Evaluation on four benchmark datasets, FaceForensics++, Celeb-DF v2, a curated subset of the DeepFake Detection Challenge (DFDC), and DeeperForensics, yields strong and consistent F1-scores of 98.0%, 91.0%, 97.6%, and 96.2%, respectively. The approach also demonstrated a good cross-dataset generalization, providing a robust and interpretable solution for video deepfake detection.

---


### 194. [Benchmarking Candidate Coverage in Typed Decision Models](https://arxiv.org/abs/2610.03387)

**<font color=#1a73e8>作者：</font>** Jiawen Lu, Tongtong Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Typed decision models return choices or distributions over answer options supplied at request time. Accuracy with complete options does not establish whether a model recognizes that a reference answer is missing or avoids rejecting valid candidates. We present a paired candidate-coverage benchmark protocol and an initial evaluation of Laya and Jev across AG News, DBpedia, Emotion, and TREC. The models receive identical frozen texts and requests: 300 calibration and 589 test texts yield 23,932 predictions per model. Present/absent pairs match ordinary candidate count, and name variants preserve descriptions, members, and order. Native rejection behavior differs sharply: at five TREC candidates with natural names, Laya detects 97.2% of missing-answer cases but falsely rejects 69.7% of present controls; Jev's rates are 24.8% and 0.0%. Calibration-only none-score thresholds change these rates to 33.9%/3.7% and 45.0%/1.8%, respectively. On DBpedia, Jev's high coverage-score AUROC supports a stronger operating point, whereas both models have weak complete-set accuracy on Emotion. Competence-conditioned analysis, probability-precision sensitivity, and interface audits show why classification, score ranking, and rejection policies need separate measurement. This initial benchmark is descriptive and limited to reference-label omission; it does not establish natural out-of-scope generalization, causal mechanisms, or a new rejection method.

---


### 195. [Native Action-Prior Learning from Videos for World Action Models](https://arxiv.org/abs/2610.03391)

**<font color=#1a73e8>作者：</font>** Zhaochong An, Fei Zhang, Menglin Jia 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models integrate future visual dynamics with robot action prediction, but their scalability remains limited by the need for action-annotated robot trajectories. Observation-only videos contain rich evidence about interaction dynamics, but existing approaches typically use them either to pretrain visual representations that must later be adapted for control, or to infer latent actions that are subsequently grounded to robot commands. We present NAVA-WAM, which introduces native action-prior learning by directly pretraining the action policy from observation-only videos, avoiding indirect representation-to-control transfer or a separate latent-action model. Our training consists of two stages. First, we pretrain on observation-only videos, where future-video flow-matching supervision over visual transitions is propagated through transition-structured joint attention to optimize the Action-DiT and learn action-relevant priors. Second, we use action-labeled demonstrations to post-train the Action-DiT for robot control through joint video--action flow matching, while asymmetric attention decouples the visual branch from iterative action denoising and enables efficient action-only inference. Extensive experiments show that NAVA-WAM consistently outperforms prior approaches under both in-distribution and out-of-distribution settings, while demonstrating strong action-label efficiency and effective real-robot generalization. These results establish native action-prior learning as an effective approach to directly pretrain action policies from observation-only videos, providing a scalable path beyond action-labeled robot data.

---


### 196. [Bidirectional Voronoi-biased Exploration Curriculum for Reinforcement Learning](https://arxiv.org/abs/2610.03395)

**<font color=#1a73e8>作者：</font>** Juri Pfammatter, Kaixian Qu, Clemens Schwarke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks with sparse rewards pose an exploration bottleneck for goal-conditioned reinforcement learning: a policy started from the initial state rarely reaches the goal and receives no learning signal. Reference motions, hand-designed curricula, and shaped rewards supply this signal but require demonstrations or task-specific engineering; automatic start-state and goal curricula avoid this but typically expand from one side only, so the full distance to the target must be covered from that side. We propose the Bidirectional Voronoi-biased Exploration curriculum for Reinforcement learning (BVER), which expands from both ends at once. Inspired by bidirectional RRT planning, BVER grows start states outward from the goal and goals outward from the initial state distribution, biases both toward unexplored task space, and steers them toward each other, training one goal-conditioned policy on both. On point-mass mazes, quadrupedal box climbing, and robot-arm ring-on-peg transfer, BVER learns faster than all compared reference-free curricula. On box climbing, it reaches 95% success on a 0.4 m box in roughly 65% fewer iterations than the best of them, is the only one of them to learn to climb a 0.7 m box, and yields a policy robust to start, goal, and yaw variation. Without a demonstration, it approaches the sample efficiency of reference-based curricula on the 0.4 m box and on ring-on-peg transfer. Ablations show that expanding from both ends outperforms either direction alone.

---


### 197. [A Unified Framework for Bayesian Data Assimilation with Generative Models and Observation Interpolants](https://arxiv.org/abs/2610.03396)

**<font color=#1a73e8>作者：</font>** Nikolaj T. Mücke, Benjamin Sanderse  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian data assimilation combines model forecasts with noisy observations, but sampling high-dimensional, non-Gaussian posteriors remains challenging. We introduce an observation-interpolant framework that turns pretrained stochastic interpolant, flow matching, and diffusion models into posterior samplers without retraining. Conditioning the interpolant path on observations yields a shared likelihood-score correction to the drift or velocity, unifying stochastic and deterministic posterior sampling. The resulting SDEs and ODEs sample the exact posterior when the intermediate likelihood score is known. For practical computation, we approximate this score using a closed-form Gaussian surrogate with a bias-corrected mean and covariance inflated by the model's source covariance. Jacobian-free and ensemble-shared approximations make the method tractable in high dimensions. We evaluate the framework on linear-Gaussian dynamics, stochastic two-dimensional Navier-Stokes, and urban airflow with up to $O(10^4)$ degrees of freedom.

---


### 198. [Beyond Entropy: Self-Diagnostic Multi-Role Token Optimization for Video Reasoning](https://arxiv.org/abs/2610.03400)

**<font color=#1a73e8>作者：</font>** Yudong Han, Yong Wang, Zaiquan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has substantially advanced multimodal reasoning, yet it remains fundamentally limited by ambiguous token-level credit assignment. While high-entropy token heuristics encourage possibility exploration, naively extending them to video reasoning tends to induce lengthy reasoning, as the model becomes overly reliant on high-entropy visual activations. Alternative approaches that rely on counterfactual-based visual token localization for credit assignment also tend to over-prioritize visual exploration at the expense of decisive reasoning cues for answer derivation, thereby exacerbating the interference from spurious visual nuances. Moreover, these methods employ static counterfactual strategies that fail to co-evolve with the policy during training. In this paper, we introduce DyCPO, a co-evolutionary framework that jointly optimizes reliable token selection and adaptive counterfactual intervention. It constructs a multi-role dependence metric to balance visual exploration and answer-relevance mining in token-wise contrastive learning, while suppressing exploration-only filler tokens and spurious visual noise. Rather than relying on static counterfactual priors, DyCPO dynamically derives counterfactual signals from the model's own successful and failed rollouts, enabling self-diagnostic analysis and co-evolution of the optimization objective with the policy. Extensive experiments on complex video reasoning and general video understanding benchmarks demonstrate consistent performance improvements, establishing DyCPO as a robust token-level credit assignment paradigm for multimodal reinforcement learning.

---


### 199. [16-bit Precision of Convolutional Neural Networks on Microcontroller Units for 8-bit Costs](https://arxiv.org/abs/2610.03402)

**<font color=#1a73e8>作者：</font>** Rui Liu, Benjamin Paaßen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To deploy deep neural networks on edge hardware, highly efficient inference schemes are necessary that retain high accuracy. This work presents W16A16, a high precision (16-bit), fast speed, low energy quantization method. On a widely applied microcontroller architecture Armv7E-M, our proposed approach achieves faster speed and lower energy consumption on layer- and model-level compared to alternative quantization schemes. We analyze the architecture of Armv7E-M, explain the underlying principles behind the performance advantages of 16-bit approaches, and evaluate the empiric quantization errors for regression and classification tasks, as well as empiric time- and energy consumption in MCU deployment. We observe ca.\ 10 times lower quantization errors compared to 8-bit quantization schemes while achieving similar or better inference times and energy consumption.

---


### 200. [ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation](https://arxiv.org/abs/2610.03403)

**<font color=#1a73e8>作者：</font>** Zhihao Zhan, Le Tao, Yifei Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forest point cloud segmentation is fundamental for fine-grained 3D forest scene understanding, yet remains challenging due to irregular tree structures, severe occlusions, density variations, and ambiguous instance boundaries. Recent query-based forest segmentation methods have shown promise for unified semantic and instance prediction, but they still insufficiently exploit forest-specific spatial structure and account for boundary uncertainty. In this paper, we propose ForestQuery, a boundary-aware and spatially anchored query learning framework for unified forest point cloud segmentation. ForestQuery enhances instance and semantic query learning through two complementary designs. Specifically, boundary uncertainty is explicitly modeled to guide reliable instance query construction and modulate query optimization through adaptive loss reweighting. Meanwhile, spatially anchored semantic query enhancement (SA-SQE) introduces learnable 3D anchors encoding forest vertical stratification priors to enrich semantic queries with explicit spatial references. We evaluate ForestQuery on multiple public forest point cloud benchmarks and a self-collected annotated real-world dataset. Extensive experiments demonstrate consistent improvements in both individual-tree segmentation and semantic segmentation across diverse forest scenes. Code and data are publicly available at this https URL

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-260](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
