# 📦 其他研究 | 2026年09月17日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

---

### 51. [Negation Beyond the Verbal Channel: Temporal Multimodal Correlates in Dialogue](https://arxiv.org/abs/2609.16396)

**<font color=#1a73e8>作者：</font>** Leon Hammerla, Patrick Schrottenbacher, Alexander Mehler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negation is typically modeled through its linguistic realization, although spoken interaction is accompanied by tightly coordinated nonverbal behavior. We ask whether contexts centered on spoken negation cues contain measurable multimodal behavioral information: whether they can be distinguished from matched control contexts without lexical or acoustic input, where this information occurs in time, which modalities carry it, and whether it extends to the dialogue partner. We study 27 human-human interviews conducted in virtual reality, comprising temporally aligned gaze, facial, head, body, hand, and finger behavior and 964 annotated negation cues. Treating classification as a predictive probe, we compare 20 time-series models while excluding lexical and acoustic information, and then systematically vary temporal context, interactional source, modality availability, and event timing. Across grouped 10-fold cross-validation, the strongest probes reach up to .75 mean held-out AUROC from speaker-side behavior. Temporal analyses show that predictive information is concentrated around cue onset but remains detectable over a broader surrounding interval, while dialogue-partner behavior carries weaker predictive information with a comparatively diffuse temporal profile. Ablation and timing perturbations further show that facial features produce the largest modality-ablation effect and that the trained probe is sensitive to the temporal organization of the observed events.

---


### 52. [Implementing a White-Box Undetectable Backdoor for Random Fourier Features](https://arxiv.org/abs/2609.16403)

**<font color=#1a73e8>作者：</font>** Michael Collins, Jada Cumberland, Brianne Dunn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Goldwasser et al. showed that undetectable backdoors can be planted in machine learning models trained with the Random Fourier Features (RFF) algorithm, under a hardness assumption tied to the Continuous Learning With Errors (CLWE) problem. Under standard cryptographic assumptions, even a full white-box audit of a model's weights cannot detect this class of backdoor. The construction is stated in terms of cryptographic reductions and probabilistic lemmas, without a reference implementation, and relies on secondary machinery such as the Sparse Gaussian Pancakes distribution and a homogeneous CLWE conditional density. Its realizability in ordinary numerical code is not obvious from the paper alone.
This paper implements the white-box CLWE-RFF backdoor construction end to end using only numpy and scipy, to test whether this threat is realizable with commodity scientific-computing tools or requires specialized cryptographic infrastructure. We give two samplers for the core $GP_d(b_k)$ distribution. The first is a rejection-sampling proxy. The second is an exact closed-form sampler derived from the homogeneous CLWE density and verified against its own analytic form.
Using this implementation, we run statistical indistinguishability tests, covering both weight-space and functional black-box comparisons. We find no evidence of detectable difference between backdoored and clean models across a range of sparsity ratios $\rho = d_{\text{sparse}}/D$. We report which parts of the construction were straightforward to realize, which required derivation not spelled out in the paper. We also highlight which parts we did not attempt to reproduce, including the underlying lattice hardness reduction. We see this work as a contribution to understanding the practical realizability of the Goldwasser white-box CLWE core, not as a new theoretical result.

---


### 53. [Context-Aware Emotionally Adaptive Voice Assistants: A Multimodal Framework for Empathetic Human-Agent Interaction](https://arxiv.org/abs/2609.16417)

**<font color=#1a73e8>作者：</font>** Tapon Kumer Ray, Rajkumar Yesuraj  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Voice-assistant interruptions tend to be intrusive because existing systems fail to consider the affective state, cognitive load and situational context of the user when deciding when and how to this http URL-assistant interruptions tend to be intrusive, since existing systems do not consider the affective state, cognitive load or situational context of the user when determining when and how to interrupt. In this paper, EmpathicVA, a closed-loop framework integrating physiological sensing, vocal-affect analysis, contextual modeling and reinforcementlearning interruption policy, is introduced. A hierarchical fusion model involves integrating HRA, EDA, respiration, acousticprosodic features, linguistic embeddings, and contextual cues and computing the probabilities of five affective states. A Double Deep Q-Network selects immediate response, brief or extended delay, empathetic response, or silent mode based on these probabilities, context and interaction history. The multimodal model obtained an accuracy of 92.3% and an F1-score of 0.922 at the macro level on a held-out test set, outperforming the highest accuracy unimodal model by 6.0 percentage points. Comparing the six-week within-subject field study with 48 participants with a baseline and context-only assistants, there was a corresponding increase in satisfaction, trust, and appropriateness of timing, as well as a large reduction in interruption-related stress episodes. The results suggest that affect-aware timing and restraint are both important in voice interaction in addition to the response wording.

---


### 54. [No Bit Left Behind: Using Brute-Force Lifting to Achieve Fully Static Binary Recompilation](https://arxiv.org/abs/2609.16423)

**<font color=#1a73e8>作者：</font>** Tianjiao Huang, Po-An Chen, Nick Baron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binary recompilation is a technique for operating directly on executable code. It promises to automate two important tasks: retrofitting security mitigations onto legacy binaries, and migrating binaries across instruction set architectures (ISAs). Yet today, there is no fully automated system that can reliably lift arbitrary binary executables to a compiler intermediate representation (IR) such as LLVM IR, or that can fully statically and reliably translate non-trivial binary executables from one ISA to another. The main underlying problem is that recovering a program's control flow graph (CFG) statically is impossible in general: computed branches can jump to targets that cannot be determined without actually running the program. Existing systems resort to runtime fallback mechanisms, requiring a significant portion of the binary translation machinery to accompany the translated program on the target machine.
This article presents a fully static, whole-program binary lifting system requiring no runtime translation support on the target. Rather than attempting to distinguish code from data, we treat every byte offset as a potential branch target and lift the entire binary in a brute-force manner, constructing a superset CFG that conservatively contains all feasible control flows. Statically unresolvable computed branches are thereby reduced to lookups in a dispatch table that points to the corresponding translated control flow path. We have implemented this approach as a prototype binary recompiler from x86-64 binaries to LLVM IR, requiring no code/data heuristics. We validate it with a fully static cross-compilation to AArch64, achieved by reusing existing LLVM backends with no modification.

---


### 55. [Adaptive Bayesian Partner Selection for Federated Clinical Centers](https://arxiv.org/abs/2609.16446)

**<font color=#1a73e8>作者：</font>** Navid Seidi, Satyaki Roy, Sajal K. Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) in healthcare faces pronounced heterogeneity and temporal concept drift across clinical centers, where evolving patient populations and care practices shift data distributions. Existing approaches rely on persistent global communication, incurring substantial bandwidth overhead while risking negative transfer from poorly aligned peers. We propose Adaptive Bayesian Partner Selection (ABPS), a peer-to-peer framework that governs who collaborates, when, and at what cost. Each center maintains a Beta-Bernoulli posterior over prospective peers' Shapley marginal utility, ranks candidates with an Upper Confidence Bound (UCB) criterion, and forms collaborations through a lightweight propose-reject mechanism, with the option to abstain from communication when no mutually beneficial partner exists. The framework admits a stochastic decision interpretation, yielding finite-sample concentration guarantees and O(kappa log T) regret in partner selection, along with conditions under which intentional isolation is optimal under negative transfer. Lightweight extensions (head personalization, bfloat16 quantized communication, and a tunable active-set size) further improve efficiency, and a goal-aware metadata filter enables institution-specific collaboration strategies. On binary in-hospital mortality prediction over the first 24 hours of an ICU stay, with 230 non-IID clinical centers drawn from MIMIC-IV, the full ABPS-X variant matches the strongest federated baseline (FedDyn, AUROC 0.758) at 0.09x the communication cost of FedAvg, with reduced variability. A diversity-driven configuration activates intentional isolation for a substantial fraction of centers. These results show that adaptive, utility-aware collaboration reduces communication without sacrificing accuracy when centers are numerous and small, offering a scalable paradigm for healthcare FL.

---


### 56. [Decentralized Gossip Learning and Federated Averaging for Histopathology Image Classification](https://arxiv.org/abs/2609.16448)

**<font color=#1a73e8>作者：</font>** Yusuf Ozturk, Enes Goltekin, Bengisu Atli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast histopathology analysis increasingly relies on distributed learning because direct data pooling across institutions is often restricted by privacy, governance, and communication constraints. This study compares server-based Federated Averaging (FedAvg), fully decentralized gossip learning, and Hybrid Gossip-FedAvg for invasive ductal carcinoma (IDC) patch classification. Experiments used 277,524 color image patches with patient-disjoint training, validation, and test partitions and a workload-balanced, Dirichlet-guided allocation across six nodes. Ring, random degree-3, and fully connected gossip topologies were evaluated together with sensitivity analyses for statistical heterogeneity, mixing coefficient, learning rate, model drift, prediction disagreement, calibration, clinically motivated operating points, communication payload, and patient-level IDC burden, together with auxiliary backbone robustness analyses. In the principal alpha=0.3 experiment, Hybrid Gossip-FedAvg achieved a test area under the receiver operating characteristic curve (ROC-AUC) of 0.8811, closely followed by FedAvg at 0.8801 and fully connected gossip at 0.8751. Across three independent patient-level repetitions, FedAvg and Hybrid Gossip-FedAvg obtained the same mean ROC-AUC of 0.9082, with standard deviations of 0.0037 and 0.0043, respectively. Hybrid achieved the highest mean area under the precision-recall curve of 0.8240, whereas FedAvg produced the lowest mean Brier score of 0.1335. Denser gossip graphs improved discrimination but increased theoretical model payload, while ring gossip remained sensitive to learning rate and mixing strength. Overall, FedAvg provided the most consistently reliable server-based baseline, topology-aware gossip offered a viable decentralized alternative, and Hybrid Gossip-FedAvg provided a balanced compromise between peer-to-peer diffusion and periodic global coordination.

---


### 57. [Not All Relations Are Equal: Relation-Balanced and Calibrated Graph Learning for Provenance-Based Intrusion Detection](https://arxiv.org/abs/2609.16462)

**<font color=#1a73e8>作者：</font>** Lijie Zheng, Ji He, Alessandro Brighente 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance-Based Intrusion Detection Systems (PIDSs) detect Advanced Persistent Threats (APTs) by analyzing system interactions. However, existing methods largely treat relations uniformly, overlooking statistical heterogeneity; in CADETS, relation frequencies differ by approximately $140{,}000\times$. This may cause PIDSs to focus more on frequent relations and overlook differences in normal error levels across relations, increasing the risk of false alarms and missed detections. We present RECAL, an unsupervised framework using relation-balanced masked graph learning to better capture rare interaction patterns. It further calibrates reconstruction errors against each relation's benign error distribution to produce comparable anomaly evidence, helping distinguish attacks from benign behavior and reduce false alarms. On three DARPA E3 datasets, RECAL achieves F1 scores of 99.99\%, 99.93\%, and 99.99\%, outperforming the best baseline on each dataset by 0.88, 0.82, and 0.42 percentage points, respectively. Compared with the baseline reporting the lowest FPR, RECAL reduces mean FPR by approximately $105\times$, $4\times$, and $41\times$.

---


### 58. [Online Gradient Computation for Warping Gaussian Process Transformations](https://arxiv.org/abs/2609.16472)

**<font color=#1a73e8>作者：</font>** Emilio Ruiz-Moreno, Konstantinos Slavakis, Baltasar Beferull-Lozano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Warped Gaussian processes (GPs) handle non-Gaussian observations by mapping them into a latent standard GP via a parametric transformation called warping. Existing streaming variants, however, either optimize the warping parameters periodically or sacrifice analytical tractability for a higher model capacity. To bridge this gap, we show that the gradient of the instantaneous negative log-likelihood of a warped GP admits an exact recursive computation. Based on this result, we propose a novel online method for warped GPs that jointly updates the latent GP moments and optimizes the warping parameters.

---


### 59. [MDN-Control: Mask-Depth-Noise Guided Region Control for Multi-Subject Video Editing](https://arxiv.org/abs/2609.16475)

**<font color=#1a73e8>作者：</font>** Jiayi Yu, Xi Ye, Lina Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi subject video editing modifies designated subjects while preserving non target content, but faces cross subject attribute leakage, and occlusion ambiguity. Existing approaches rely on masks and struggle to distinguish overlapping subjects or ensure consistent generation. To address these limitations, we propose MDN-Control, a training free framework jointly controlling target localization, occlusion geometry, and appearance initialization. Specifically, mask-guided localization provides consistent target localization, while depth-aware occlusion control resolves ambiguous boundaries between overlapping subjects. We further introduce noise latent prompting, which retrieves Gaussian initializations from a noise library for prompt relevant priors. Experiments on MSVBench show that MDN-Control achieves the lowest CM-Err and the highest Q-Edit, while maintaining competitive text alignment and temporal consistency, demonstrating the effectiveness of combining spatial, geometric, and latent priors for multi subject video editing.

---


### 60. [Decoder Design Matters for ECG Delineation](https://arxiv.org/abs/2609.16489)

**<font color=#1a73e8>作者：</font>** Joseph Scharpf, William Han, Chaojing Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) delineation identifies the boundaries of P waves, QRS complexes, and T waves, providing structural annotations that can guide AI models in learning to interpret ECGs. However, training accurate delineation models requires manual annotations that are scarce and time-consuming to obtain. Recent work addresses this limitation through semi-supervised learning (SSL), but the design of the architecture, particularly the decoder, has received less attention. To this end, we propose R-U-Net, an ECG delineation model that pairs a ResNet-18 encoder with a U-Net decoder. On SemiSegECG, R-U-Net outperforms the strongest evaluated ResNet-18 + fully convolutional network (FCN) head baseline in each of the 16 in-domain settings by 3.3-13.0 mIoU and achieves 82.6 mIoU in the cross-domain setting, an improvement of 8.1 mIoU. Controlled ablations show that decoder design contributes more to performance gains than the evaluated SSL methods, motivating further exploration of architectures for ECG delineation. All code is open-source at this http URL.

---


### 61. [From Manual Construction to AI-Driven Scenario Emergence: Rethinking Catastrophe Risk Modeling](https://arxiv.org/abs/2609.16493)

**<font color=#1a73e8>作者：</font>** Hang Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional catastrophe (CAT) risk models rely on costly manual construction to generate extreme weather scenarios, an approach largely unchanged since the 1990s. As climate extremes intensify, this creates mounting challenges to the entire risk transfer chain. This study proposes the TAISE framework, which repurposes AI weather forecasting models to produce coherent extreme weather sequences at a fraction of traditional costs. Through self-iterative generation, the framework produces continuous global atmospheric fields from which extreme events emerge. A proof-of-concept experiment demonstrates an order-of-magnitude reduction in computational cost compared with conventional methods, while capturing temporal continuity and cross-regional correlations absent in snapshot-based approaches. These findings suggest a pathway toward democratising catastrophe risk quantification and enabling dynamic, comprehensive portfolio assessment for insurers, reinsurers, ILS fund managers and public-sector risk managers.

---


### 62. [High-Performance Tensor Formulation of the Viterbi Algorithm for Hidden Semi-Markov Models](https://arxiv.org/abs/2609.16500)

**<font color=#1a73e8>作者：</font>** Lorenzo Piarulli, Elia Belli, Daniele De Sensi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hidden Semi-Markov Models (HSMMs) are fundamental probabilistic models widely adopted across diverse domains, from computational biology to finance and signal processing. The Viterbi algorithm decodes the most likely state sequence given an HSMM and can be applied iteratively for ab initio model learning. However, existing Viterbi implementations remain sequential, and GPU-accelerated solutions are entirely absent, making HSMM decoding impractical for large-scale workloads. We present a tensor-based formulation of the Viterbi algorithm for HSMMs, restructuring the inner loops into tensor operations that naturally map onto SIMD units and massively parallel architectures. Building on this formulation, we provide optimized implementations spanning single- and multi-core CPUs, and, for the first time, GPU. Experimental evaluation demonstrates speedups of up to 14x on a single core, over 200x with multi-core, and over 570x on GPU over the state-of-the-art sequential baseline, establishing a new performance baseline for large-scale HSMM decoding.

---


### 63. [Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array](https://arxiv.org/abs/2609.16518)

**<font color=#1a73e8>作者：</font>** Svetoslav Kolev, Lingni Ma, Michael Goesele 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Capturing hand motion and interaction forces is critical for interactive computing, VR, and high-fidelity tactile demonstrations for robot learning. We introduce a wrist-worn pressure-sensing wristband that recovers continuous full-hand pose and distributed contact force on a single wearable. The system consists of flexible capacitive sensor arrays around the wrist, which require no electrical skin contact, and a recurrent network that maps the resulting pressure signal to hand state. Our key insight is that muscle contraction and tendon displacement produce pressure patterns, which correlate strongly with hand pose and interaction force. To validate this, we collect synchronized recordings of wrist pressure, optical motion-capture hand pose, and tactile-glove interaction force, covering isolated finger motion, fingertip-force stress tests, and natural hand-object manipulation. On isolated single-user motion the wristband attains $4.6^\circ$ mean finger-joint MAE, and across four users manipulating everyday objects it estimates per-finger contact force at $R^2=0.57$, which an external pose signal brings up to $0.75$. We see the wristband as one node in a constellation of everyday wearables -- e.g. paired with an egocentric camera -- adding the contact force that vision cannot observe and taking over when the hand is occluded.

---


### 64. [FlowATC: Aircraft Trajectory Prediction via Flow Matching](https://arxiv.org/abs/2609.16528)

**<font color=#1a73e8>作者：</font>** Mathurin Petit, Emir Torun, Louis Brusset 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building accurate decision-support tools for next-generation air traffic control requires robust trajectory prediction models. We present a flow-matching architecture trained exclusively on historical aircraft trajectories, with no route labels or chart supervision. Trained on 1.15 million Automatic Dependent Surveillance-Broadcast trajectory windows collected over the San Francisco Bay Area, the model generates aircraft trajectory distributions that closely match historical traffic, reproducing known airspace structure around San Francisco Airport such as the shape of SFO's published NIITE FOUR departure procedure. Our model is trained directly on the native, irregular ADS-B sampling interval. Trajectory prediction is cast as sequence inpainting using a block-causal Transformer that denoises future state tokens conditioned on the observed history using Conditional Flow Matching or Denoising Diffusion Probabilistic Models. We compare our architecture against constant-velocity, deterministic-Long Short Term Memory, and Conditional Variational Autoencoders baselines. At matched parameter count, CFM outperforms DDPM by 11-26% in minADE@20, and both generative objectives surpass the CVAE baseline by 31-41%. We further show that the error degrades gracefully with prediction horizon, and the architecture remains effective when retrained on temporally decimated feeds. Lastly, we sample $K$ independent completions, yielding spatial probabilistic occupancy estimates that can serve as input to downstream conflict-risk estimation.

---


### 65. [What Does Layer-Importance Reveal About Transformers and State-Space Models?](https://arxiv.org/abs/2609.16537)

**<font color=#1a73e8>作者：</font>** Istabrak Abbes, Nizar Islah, Irina Rish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers and state-space models (SSMs) are the two dominant families of sequence models, and a central open question is how far the analytical knowledge built for transformers transfers to SSMs. We address this through the lens of layer importance which underpins compression, selective fine-tuning, and interpretability across both families. We decompose layer importance into two distinct notions. \emph{Necessity} captures how much the pretrained model depends on a layer's existing contribution, measured by the loss increase from bypassing it. \emph{Plasticity} captures where the model absorbs new information during fine-tuning, measured by the magnitude of task-specific weight updates. Our analysis reveals that the two families behave fundamentally differently: in every evaluated residual transformer up to $14$B parameters, Necessity and Plasticity anti-align across depth, whereas in the evaluated Mamba-style SSMs they point to overlapping regions. The sign of this alignment also predicts downstream adaptation behavior. In the evaluated transformers, concentrating updates in the most plastic layers increases catastrophic forgetting, while this tier-dependent effect disappears in the evaluated Mamba-style SSMs.

---


### 66. [Ptolemy: A Semantic Map of Exploratory Data Analysis](https://arxiv.org/abs/2609.16539)

**<font color=#1a73e8>作者：</font>** Dylan Wootton, Denny Bromley, Vidya Setlur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A central challenge in exploratory data analysis (EDA) is keeping track of what has already been examined in order to decide what to analyze next. In practice, analysts often run dozens of analyses while building an understanding of a dataset. However, most tools provide little support for maintaining an overview of this evolving process, instead exposing only a linear history of analysis steps. These tools show sequence, what came before, but not position, how a current analysis relates to the broader space of possible analyses. As a result, analysts must mentally reconstruct which parts of the space they have explored and where gaps remain, increasing the risk of redundant work or overlooked patterns. We present Ptolemy, a navigational interface that externalizes analysis history as a semantic map. Each analytic step is represented as a point positioned by embeddings derived from a structured description of its effective data view (e.g., columns, filters, transformations), allowing spatial distance to reflect analytic similarity. In a mixed-methods study comparing map, canvas, and tree representations, we find that maps improve global orientation and local comparison, while ordered layouts reduce decision cost. These findings surface a trade-off between orientation and actionability, and highlight design principles for supporting strategic exploration in EDA.

---


### 67. [A Cyber Range Evaluation of Autonomous Network Incident Response Agents](https://arxiv.org/abs/2609.16541)

**<font color=#1a73e8>作者：</font>** Jakob Nyberg, Teodor Sommestad, Andrei Buhaiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We test the performance of agents for automated network intrusion response in a cyber range intended for human operator training. The range implements an emulated networking environment with a variable network topology, red-team emulation and simulated user agents. The goal of the defensive agents is to prevent hosts in the network from being accessed by the red-team agent, while minimizing the availability costs induced from defensive measures. Alerts are generated using a SIEM platform and mapped to a data modeling language used by the agents. We test a combination of heuristic agents and policies learned using reinforcement learning. The learned policies are optimized to minimize the combined cost using a cyber attack simulator modeling the network. We found that the reinforcement learning agents were overall more efficient at defending the system than the heuristic policy, and that the performance depends highly on the policy of the adversary in combination with the simulated users.

---


### 68. [GPUThor: Amplifying Rowhammer Attacks via Non-Uniform Patterns to Exploit ECC-Protected GPUs](https://arxiv.org/abs/2609.16546)

**<font color=#1a73e8>作者：</font>** Chris S. Lin, Joyce Qu, Aditya Rajeev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> GDDR memory in GPUs is vulnerable to Rowhammer attacks, where rapid memory accesses induce bit flips in adjacent cells, enabling data tampering and privilege escalation. However, prior GPU Rowhammer attacks trigger only tens to hundreds of bit flips, orders of magnitude fewer than CPU attacks, severely limiting their practical impact. This gap stems from the reliance of existing GPU Rowhammer attacks on uniform hammering patterns that activate aggressor and decoy rows equally, which results in low hammering intensity for aggressor rows.
We present GPUThor, a high-intensity Rowhammer attack on NVIDIA GPUs leveraging non-uniform hammering. GPUThor reverse engineers GPU memory-access coalescing behavior to enable non-uniform hammering patterns on GPUs, that activate aggressor rows more intensely than decoy rows. Additionally, by identifying refresh instances when in-DRAM mitigations are applied, it constructs longer attack patterns that escape mitigation across refresh intervals, further increasing hammering intensity. Together, these techniques yield 500X to 23,500X more bit flips than prior GPU Rowhammer attacks, across several NVIDIA GPUs (A4000, A4500, A5000, A6000), reaching bit flip rates close to state-of-the-art CPU Rowhammer attacks. GPUThor also enables the first Rowhammer exploits on ECC-protected GPUs, inducing uncorrectable double and triple bit flips, making denial-of-service and privilege-escalation attacks practical even on GPUs with ECC enabled.

---


### 69. [QueryFormer: Winning Solution for KDD Cup 2026 Tencent UniRec Challenge](https://arxiv.org/abs/2609.16548)

**<font color=#1a73e8>作者：</font>** Yuanzhe Zhou, Zhaoyang Zeng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-click conversion rate (pCVR) prediction requires jointly modeling feature interactions and sequential user behaviors. The KDD Cup 2026 Tencent UniRec Challenge calls for a unified architecture addressing both. We observe that existing unified architectures often generate query tokens---the central information hub---with projection-based multi-layer perceptrons (MLPs), without explicit token-to-query attention for refining the query side. We propose QueryFormer, centered on a stackable unified field--sequence block that bridges non-sequential multi-field features and behavioral sequences, and provide a latency-aware scaling study over view width $H$, model width, depth, data, and compute. The block generates queries through cross-attention and packs sequence queries into shared-parameter attention. QueryFormer secured 1st place in the Industrial Track, achieving an official test area under the ROC curve (AUC) of 0.83254; a modest post-competition scale-up reached 0.832713. Within our grid, $H$-scaling improves validation AUC from 0.84540 to 0.84615 and beats HyFormer at comparable budgets. Ablation identifies query generation as the largest contributor. Packed shared-parameter cross-attention keeps H=8 inference latency to only 1.89x that of H=1, positioning the bridge as an efficient stackable unified block.

---


### 70. [Which Pretext Task Transfers? Self-Supervised Pretraining Objectives for Lung Ultrasound](https://arxiv.org/abs/2609.16551)

**<font color=#1a73e8>作者：</font>** Moein Heidari, Junbo Rao, Jai Choraria 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) can reduce the need for labelled medical images, but the choice of pretext objective remains unclear for lung ultrasound (LUS). Contrastive learning, masked reconstruction, and joint-embedding predictive architectures (JEPA) differ in the space in which their targets are defined, yet existing ultrasound studies compare them under different corpora, backbones, and evaluation protocols. We compare these three objective families using the same encoder backbone, pretraining corpus, optimisation schedule, and frozen-evaluation protocol. Encoders are pretrained on COVID-BLUeS LUS videos and evaluated with linear, $k$NN, and attentive probes at 5\%, 10\%, 50\%, and 100\% label budgets. Evaluation is performed on POCUS using patient-level five-fold cross-validation and on the independently acquired Mendeley-Uganda dataset, which is excluded from both pretraining and probe fitting. At the full label budget under linear probing, VideoMAE and V-JEPA achieve $66.5 \pm 13.1$ and $65.4 \pm 11.7$ balanced accuracy on POCUS, while MoCo achieves $42.1 \pm 1.2$. On Mendeley-Uganda, the ranking reverses: MoCo performs best at $62.7 \pm 1.0$, followed by VideoMAE at $53.8 \pm 2.8$, while V-JEPA falls near chance at $35.1 \pm 4.9$. These results show that POCUS probe accuracy alone does not identify the objective that transfers best across datasets. We also outline planned representation-level analyses to examine this reversal. Code is publicly available at this https URL.

---


### 71. [The MAL Simulator: Cyber Operations Simulation based on Attack & Defense Graphs](https://arxiv.org/abs/2609.16563)

**<font color=#1a73e8>作者：</font>** Jakob Nyberg, Sandor Berglund, Andrei Buhaiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We have developed the MAL Simulator, a cyber operation simulator based on the Meta Attack Language (MAL). The MAL Simulator is intended for decision-driven cyber attack and defense simulations, for system analysis and the development of automated agents. By building the simulator around an attack modeling language, it can be adapted to different target domains without modifying the source code. We used the simulator for two case studies where we trained two types of agents for automated cyber operations: a defensive agent and an offensive agent. To ground the experiments, we base the models in data collected from an emulated network implemented in the cyber range CRATE. We found that the trained attacker policy could reach the designated targets more efficiently than the compared search methods, and that the trained defender agent induced lower costs than a naive heuristic agent under noisy alert conditions. When testing the RL attacker against the RL defender, we found that the performance of the defenders dropped significantly. This emphasizes the importance of cyber attack simulators to facilitate training both offensive and defensive agents. The MAL Simulator and associated tooling is publicly available and provides common interfaces for compatibility with existing machine learning frameworks.

---


### 72. [Vision And Text Transformer For Predicting Answerability On Visual Question Answering](https://arxiv.org/abs/2609.16565)

**<font color=#1a73e8>作者：</font>** Tung Le, Huy Tien Nguyen, Le Minh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answerability on Visual Question Answering is a novel and attractive task to predict answerable scores between images and questions in multi-modal data. Existing works often utilize a binary mapping from visual question answering systems into Answerability. It does not reflect the essence of this problem. Together with our consideration of Answerability in a regression task, we propose VT-Transformer, which exploits visual and textual features through Transformer architecture. Experimental results on VizWiz 2020 dataset show the effectiveness and robustness of VT-Transformer for Answerability on Visual Question Answering when comparing with competitive baselines.

---


### 73. [Counterfactual Reasoning for Robust Visual Question Answering](https://arxiv.org/abs/2609.16567)

**<font color=#1a73e8>作者：</font>** Truong-Binh Duong, Thanh-Ngan Tran, Ngoc-Thao Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Visual Question Answering (VQA) models often exploit spurious correlations in training data, leading to poor out-of-distribution (OOD) generalization due to language bias. Although counterfactual learning has shown promise, existing methods can be improved to better guide attention toward causal evidence and strengthen feature discrimination. To address this, we propose a novel training framework that enhances counterfactual contrastive learning for VQA. Our framework introduces three key contributions: (1) a three-stage curriculum for stable multi-objective optimization, (2) an enhanced Batch-Contrastive loss for more discriminative feature learning, and (3) two novel regularizers, Answer-Contrastive (AC) loss to refine the prediction space and Gradient-Discrepancy (GD) loss to enforce causal visual grounding. Our model achieves a competitive accuracy of 61.64% on the bias-sensitive VQA-CP v2 benchmark while maintaining 62.80% on the standard VQA v2 dataset, yielding a small generalization gap of 1.16%. This demonstrates a strong balance between OOD robustness and in-distribution performance.

---


### 74. [Efficient Text-to-Image Generation: An Adaptive Step Schedule Controller for Diffusion Models](https://arxiv.org/abs/2609.16572)

**<font color=#1a73e8>作者：</font>** Kuluhan Binici, Cihan Acar, Shivam Aggarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models often use a fixed number of denoising steps, balancing time costs and image quality. However, the optimal number of steps depends on the complexity of the input text prompt. We propose an adaptive diffusion controller that dynamically adjusts the number of steps to generate high-quality images efficiently, without additional model training. By leveraging a mixture of step schedules with varying step sizes and evaluating the error term discrepancy at each timestep, our method transitions between schedules to optimize performance. Experiments on COCO and DiffusionDB show that our approach reduces inference time while maintaining visual fidelity, offering a more efficient alternative for text-to-image diffusion models.

---


### 75. [AsyncCouple-Flow: Asynchronous Cross-Modal Coupling and Flow Matching for Spatio-Temporal Forecasting](https://arxiv.org/abs/2609.16573)

**<font color=#1a73e8>作者：</font>** Zhixiang Wu, Yining Liu, Bo Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-modal spatio-temporal forecasting (MM-STF) supports weather nowcasting, traffic prediction, and earth-system modeling by combining heterogeneous sources such as physical fields, satellite imagery, and in-situ sensors. Three obstacles persist: (i) modalities have different spatio-temporal sampling rates, forcing lossy interpolation onto a unified grid; (ii) modalities are frequently missing at deployment due to sensor outages or revisit gaps, while most methods train with full availability; and (iii) autoregressive decoders accumulate errors over long horizons, amplified by multi-modal conditioning. We propose AsyncCouple-Flow to address these issues jointly. A Modality-Aware Token Sparsification (MATS) module performs scale-aware tokenization and uses a shared importance scorer to select top-k tokens per timestep, producing equal-length sequences. An Asynchronous Cross-Modal Coupling Graph (ACCG) replaces fixed cross-attention with a learnable graph whose edges encode time offsets, semantic similarity, and modality-specific physical priors, enabling fusion under arbitrary asynchrony and missingness. A Flow-Matching Forecasting Head models multi-step prediction as a conditional ODE, trained with stochastic modality dropout and integrated jointly to avoid autoregressive drift. Experiments on ERA5+GOES+ISD weather forecasting and PEMS-BAY traffic prediction with multi-source side information show that AsyncCouple-Flow outperforms state-of-the-art baselines and remains robust with up to two missing modalities. The code will be released upon acceptance.

---


### 76. [GraLoD: Graphics-Inspired Continuous Level-of-Detail Learning for Image Restoration](https://arxiv.org/abs/2609.16578)

**<font color=#1a73e8>作者：</font>** Hu Gao, Lizhuang Ma, Yulong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The spatial support required for image restoration varies across degradation types, image regions, and reconstruction stages. However, most existing methods rely on predefined multi-scale hierarchies and aggregate features through fixed fusion or attention, leaving the representation scale itself largely determined by the network architecture. This limitation becomes more pronounced when a task-specific backbone is extended to heterogeneous degradations in all-in-one restoration. Inspired by level-of-detail (LOD) rendering in computer graphics, we propose GraLoD, a plug-and-play framework that treats restoration scale as a spatially varying and stage-dependent continuous variable. GraLoD reuses the native encoder hierarchy, aligns its multi-scale features into a shared LOD representation space, and predicts a stage-conditioned LOD field at each decoder stage. Each spatial location then continuously queries only two neighboring representation levels, enabling the effective restoration scale to adapt to both local image content and reconstruction progress. To prevent degenerate or arbitrary scale selection, we further introduce minimal-sufficient footprint calibration (MSFC) together with structure-aware regularization (SAR) to encourage restoration-effective and spatially coherent LOD assignments. GraLoD can be directly integrated into existing restoration backbones without redesigning their fundamental feature-processing blocks. Extensive experiments demonstrate consistent improvements in task-specific and all-in-one restoration.

---


### 77. [Recovering Physical Parameters from Fragmented Observations via Exact Distributed Spline Merging](https://arxiv.org/abs/2609.16579)

**<font color=#1a73e8>作者：</font>** Naveen Mysore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific measurements are frequently distributed across locations, time periods, and institutions. Combining such fragments into a continuous, differentiable field enables recovering governing physical parameters from its derivatives. This paper makes two contributions toward that goal. First, the established additive structure of fixed-basis ridge-regression statistics is applied to tensor-product spline fields: each data holder computes a local Gram matrix and moment vector, and the merged solution is mathematically identical to centralized fitting, with no raw data shared and no iterative synchronization. This property is specific to the fixed-feature squared-error setting; the present derivation does not establish an analogous guarantee for general jointly trained multilayer networks. Second, a complete pipeline connects distributed observations to physical parameter inference through field reconstruction, derivative extraction, and linear regression. The diffusion coefficient is recovered to 0.11% error and wave speed to 0.12% error; in both cases, distributed merging introduces zero degradation relative to centralized fitting. Application to 41 years of NOAA sea-surface temperature data confirms the result on real spatiotemporal observations.

---


### 78. [EmoPhone: A Multi-Wave Dataset for In-the-Wild Mobile and Wearable Affect Sensing](https://arxiv.org/abs/2609.16581)

**<font color=#1a73e8>作者：</font>** Panyu Zhang, Minseo Park, Soowon Kang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce a three-wave, in-the-wild multimodal dataset for affect sensing that integrates smartphone sensing, wearable sensing, and dense experience-sampling-method (ESM) labels collected annually from 2020 to 2022. The dataset supports moment-level affect modeling through a shared dimensional label core across all waves, with additional affective descriptors available in the third wave (D-3). We describe the resource in terms of study design, temporal density of in-situ labels, and sensing and label coverage across waves. To support evaluation within this resource, we define an initial three-setting benchmark spanning temporal prediction from within-user history, within-wave cross-user generalization, and cross-wave generalization in which each wave is treated as a separate dataset. Our benchmark results show that the strongest method family depends on the evaluation setting: supervised baselines perform best in the temporal setting, unsupervised domain adaptation is strongest overall in the within-wave cross-user setting, and domain generalization shows the strongest overall cross-wave performance, although its margin over strong baselines is modest. These findings indicate that robust mobile affective computing is constrained not only by label availability but also by substantial participant-level variability and realistic cross-wave differences inherent in longitudinal in-situ deployments.

---


### 79. [FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation](https://arxiv.org/abs/2609.16591)

**<font color=#1a73e8>作者：</font>** Guangyu Sun, Shlok Kumar Mishra, Wentao Bao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional multimodal representation learning and generation are two stages: a contrastive or self-supervised visual encoder is trained first, followed by a separate downstream generative model. This setup bottlenecks generative performance behind frozen embeddings. To bridge this gap, we revisit joint multimodal representation learning and generation to produce linearly interpolatable embeddings that are directly consumable by generative decoders. We present FLAT (Flexible-Length Aligned Transmodal representations), a representation pre-training framework that jointly optimizes a shared multimodal encoder alongside downstream text-to-image (T2I) and image-to-text (I2T) decoders. By combining contrastive alignment with bidirectional cross-modal generative objectives, FLAT ensures its representations function as both discriminative semantic descriptors and generative conditions. Architecturally, FLAT maps visual and textual inputs into a unified continuous 1D sequence space, applying nested dropout over prefix-K tokens to enable dynamic output lengths. A single pre-training stage allows FLAT to perform cross-modal retrieval and generation across variable prefix K, achieving a T2I GenEval score of 71.1. Task-specific fine-tuning aligns model performance with state-of-the-art baselines: 83.1 GenEval on T2I generation; 40.5 BLEU-4 and 138.6 CIDEr on MS-COCO image captioning; and Recall@5 scores of 86.8 (I2T) / 75.8 (T2I) on MS-COCO alongside 98.3 (I2T) / 93.6 (T2I) on Flickr30K. Finally, qualitative evaluations demonstrate that FLAT representations natively support linear interpolation, latent space arithmetic, and zero-shot composed retrieval.

---


### 80. [FRPSS: Feature Rearrangement in Pre-Shape Space for Single-Image Generation](https://arxiv.org/abs/2609.16594)

**<font color=#1a73e8>作者：</font>** Yuexing Han, Haoxuan Zhang, Bing Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models trained on a single image often struggle to balance global structural integrity and local diversity. Existing single-image generation methods commonly rely on random noise to drive the generation process and lack explicit global structural constraints, making the generated results prone to spatial structural misalignment when structural variations occur. To address the issue, Feature Rearrangement in Pre-Shape Space for Single-Image Generation (FRPSS) is proposed in this paper. The core of FRPSS is the Manifold Structural Rearrangement with Feature Augmentation on Geodesic Surface (MSR-FAGS) module. MSR-FAGS replaces the randomly initialized features of the low-scale generator with rearranged Pre-Shape features and uses the features to guide image generation at subsequent scales, thereby reducing the risk of structural misalignment. To support downstream tasks such as stylization, a Scale-adaptive Sliding-window Patch Extraction (SSPE) strategy is further designed, and a directional Contrastive Language-Image Pre-training supervision module with SSPE (CLIP-SSPE) is constructed. Qualitative and quantitative experiments demonstrate that FRPSS achieves the best Single Image Fréchet Inception Distance (SIFID) scores on all three datasets while maintaining competitive Learned Perceptual Image Patch Similarity (LPIPS). Further qualitative experiments verify the effectiveness of FRPSS across multiple downstream tasks with the CLIP-SSPE module.

---


### 81. [CATVis: A Collaborative Multi-Agent Workflow for Turbomachinery Simulation Data Visualization](https://arxiv.org/abs/2609.16598)

**<font color=#1a73e8>作者：</font>** Zhe Wang, Zehao Lou, Guanghui Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI for Science have enabled natural language (NL) interfaces for scientific data analysis. In turbomachinery CFD post-processing, translating ambiguous high-level analytical goals (e.g., vortex identification) into precise visualization procedures supporting complex domain-specific analysis is challenging. We present CATVis, a Collaborative multi-agent workflow system that bridges this gap by transforming NL intents into structured middle representation for visualization. Our approach reformulates domain-specific visualization procedures as composable workflow representations, and use multi agent to generate workflow representations via intent planning, template generation, and error-aware refinement, where each stage incrementally updates a shared structured representation. We evaluate the impact of external knowledge and workflow structuring on generation accuracy, demonstrating that the proposed approach significantly improves complex workflow generation correctness while reducing prompt complexity.

---


### 82. [G3AR: Graph-Guided Neural Visual Geometry for Scalable Multi-Sequence Aerial Registration](https://arxiv.org/abs/2609.16603)

**<font color=#1a73e8>作者：</font>** Jeng Wen Joshua Lean, Ting-Yu Yen, Wei-Fang Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-context neural visual geometry is impractical for thousands of images, while sequence-based chunking poorly captures irregular non-local overlap in multi-sequence aerial collections. We present Graph-Guided Neural Visual Geometry for Aerial Registration (G3AR), a graph-guided framework for scalable dense neural geometry. Before local inference, G3AR builds a geometrically verified image-proximity graph that guides bounded overlapping chunks and induces a chunk graph whose maximum spanning tree defines alignment topology. Compatible backbones process chunks independently; shared-image predictions then estimate three-dimensional similarity (Sim(3)) transforms that register local cameras and geometry in a common frame. Across four real aerial scenes, G3AR improves pose error and runtime in matched VGGT- and Pi3-backed comparisons, while its DA3 variant achieves the lowest pose error among evaluated neural-geometry methods.

---


### 83. [A Weighted Kernel Method for Approximation that Adapts to Learned Multivariable Structure](https://arxiv.org/abs/2609.16606)

**<font color=#1a73e8>作者：</font>** John E. Darges, Laura Weidensager  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Approximating the input-output behavior of a multivariable black-box function from limited data is challenging when blind to the importance of its inputs and their interactions. We introduce total sensitivity kernels (TSKs), a method based on families of weighted ANOVA kernels that learn and adapt to this multivariable structure. TSKs parameterize the weights on each multivariable component of the target function by factors for each input. We propose learning these factors directly from function evaluations by selecting the reproducing kernel Hilbert space (RKHS) in which the target function has minimum norm. Under suitable conditions, we show that this norm-minimization problem admits a unique solution, and we establish consistency of a finite-data formulation based on minimum-norm interpolation. The learned TSK factors characterize the participation of individual inputs across interactions and main effects, providing a kernel-dependent notion of input sensitivity related to total Sobol indices. Numerical experiments demonstrate that adapting the kernel to learned multivariable structure can substantially improve approximation accuracy over a standard product kernel.

---


### 84. [Stable by Construction: Variational Latent Markov Operators for Long-Horizon PDE Prediction](https://arxiv.org/abs/2609.16621)

**<font color=#1a73e8>作者：</font>** Junyi Liao, Johann Guilleminot, Vahid Tarokh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE solvers provide efficient surrogates for time-dependent physical systems, but autoregressive prediction over long horizons remains challenging because local errors can induce distribution shift and accumulate under recursive deployment. We develop a variational approach to this problem by introducing latent Markov dynamics in which physical states are represented by latent distributions and evolved through probabilistic transitions. The framework is formulated directly on function spaces and specialized to functional Gaussian models, where structured latent perturbations induce a spectral geometry and variational transition alignment regularizes the learned dynamics. We further analyze how these mechanisms affect autoregressive error propagation, providing a theoretical connection between variational training and long-horizon prediction. We instantiate the framework as the Variational Autoencoding Markov Operator (VAMO), which combines spatially resolved latent fields, structured Gaussian perturbations, and a neural-operator transition. Empirically, we demonstrate the effectiveness of VAMO on several fluid-dynamics benchmarks with prediction horizons extending substantially beyond those represented during training, where it consistently reduces error accumulation and improves rollout stability over several deterministic and noise-injection baselines. Overall, these results highlight variational modeling as a complementary approach to robust long-horizon neural PDE dynamics.

---


### 85. [JewelTry: Mask-Free Scale Aware Jewelry Virtual Try-On](https://arxiv.org/abs/2609.16626)

**<font color=#1a73e8>作者：</font>** Xinlei Niu, Peixia Li, Jun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on (VTON) enables customers to visualize how fashion products appear when worn and has become an important technology for online shopping. While recent advances have substantially improved garment VTON, jewelry remains a challenging and underexplored category due to its small size, rigid structure, and sensitivity to fine-grained visual details. Realistic jewelry VTON requires not only faithful appearance transfer but also accurate scale and placement relative to the wearer. Existing jewelry VTON methods typically rely on mask guidance, whereas mask-free approaches lack explicit guidance for modeling the product scale. To bridge this gap, we introduce JVTO-Bench, a benchmark dataset for scale-faithful jewelry VTON, providing reference source target triplets with real-world product-scale annotations across four major jewelry categories. Building upon this benchmark, we propose JewelTry, a mask-free diffusion framework for scale-aware jewelry VTON. JewelTry incorporates a scale adapter that encodes product dimensions into a scale token, enabling the model to learn scale relationships between jewelry items and surrounding human anatomy in-context. To further improve jewelry consistency, we introduce a single-directional condition attention mechanism and an attention refinement loss that preserve both coarse geometry and fine-grained structural details of the reference jewelry. Extensive experiments show that JewelTry achieves a balance among visual fidelity, background preservation, object consistency and scale accuracy, establishing a strong baseline for mask-free, scale-aware jewelry virtual try-on.

---


### 86. [Can Knowledge Transfer Parameters Be Learned? LePoKet for Efficient Robotic Vision](https://arxiv.org/abs/2609.16637)

**<font color=#1a73e8>作者：</font>** Yanick C. Tchenko, Felix Mohr, Hicham Hadj-Abdelkader 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient perception is central to robotic systems operating under constrained computation, memory, and latency budgets. Knowledge transfer from larger pretrained models offers a practical route to stronger compact perception networks, but existing approaches commonly rely on fixed distillation objectives or manually designed interaction mechanisms. Building on Hereditary Knowledge Transfer (HKT), we propose LePoKet (Learnable Parameter Optimization for Knowledge Transfer), a structural transfer framework that embeds knowledge inheritance directly into the forward computation. LePoKet introduces a block-wise Extract-Transform-Mix interface whose interaction parameters are optimized jointly with the child network through a Learnable Genetic Attention (LGA) operator, without auxiliary distillation losses or temperature scaling. We first characterize the mechanism on CIFAR-10 and CIFAR-100 using ResNet parent-child pairs, obtaining relative error reductions of 24.57% and 25.1%, respectively, over standard child training. We then evaluate LePoKet for dense motion estimation by integrating it into a compact RAFT-based optical-flow model trained only on FlyingChairs and FlyingThings3D. LePoKet improves the compact RAFT baseline from 2.21 to 1.92 EPE on Sintel Clean, from 3.35 to 3.01 on Sintel Final, and from 7.51 to 6.39 on KITTI. A direct comparison with HKT further shows that LePoKet improves CIFAR-10 accuracy from 92.40% to 93.40% while achieving the best Sintel Final and KITTI errors among the evaluated compact transfer variants, with comparable performance on Sintel Clean. These results demonstrate that learnable structural transfer generalizes across recognition and motion perception tasks and provides a promising approach for efficient robotic vision.

---


### 87. [Beyond Benefit or Risk: Perceived Impact Profiles of Human-AI Affective Interaction and Their Associations with Psychological Functioning](https://arxiv.org/abs/2609.16645)

**<font color=#1a73e8>作者：</font>** Lu Chen, Fenghua Tang, Jiayu Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Relational AI increasingly serves as an emotional shelter for humans, and its impact is mixed. Prior research has focused on either positive or negative impacts, leaving unclear how they are configured within individuals and relate to psychological functioning. To address these gaps, this study used a sequential mixed-methods design. Study 1 interviewed 52 users with emotional ties to AI and identified four positive impact domains (emotional relief, loneliness alleviation, enhanced interpersonal functioning, and personal growth) and four negative impact domains (virtual-real boundary blur, social replacement, cognitive-emotional reinforcement, and excessive use). Study 2 followed 673 Chinese AI users for six months and identified four profiles of individuals differently impacted by relational AI use: minimal impact, benefit-driven impact, mixed impact, and risk-driven impact. Users in the mixed impact and risk-driven impact profiles were both high in human-AI affective bonding, but those showing risk-driven impact had greater vulnerability, indicated by higher interpersonal need frustration and emotion-regulation difficulties, more depressive and anxiety symptoms, and lower self-esteem and flourishing. Users in the benefit-driven and mixed impact profiles showed more favorable psychological functioning. After controlling for baseline functioning and relevant covariates, Wave 1 profiles did not predict five of the six Wave 2 indicators; only users in the mixed impact profile reported higher flourishing than those in the minimal impact profile. Overall, potential psychological harms associated with relational AI engagement appeared limited and selective. These findings portray relational AI as a heterogeneous socio-emotional context that may partly mirror users' states and traits, warranting individualized, adaptive safeguards.

---


### 88. [Channel-Wise and Token-Aware Post-Training Quantization for Visual State Space Duality](https://arxiv.org/abs/2609.16656)

**<font color=#1a73e8>作者：</font>** Jonghyeon Lim, Changhoon Yim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State space models (SSMs), particularly Mamba, have emerged as efficient alternatives to attention-based architectures and have been extended to vision through ViM, VMamba, and Visual State Space Duality (VSSD). Yet the low-bit post-training quantization (PTQ) behavior of VSSD remains insufficiently understood. A weight-activation split on VSSD-Tiny identifies activation quantization as the dominant low-bit bottleneck, while representative inputs to selected VSSD-backbone linear layers exhibit strong channel-wise magnitude variation and token-localized extremes. We propose the Channel-wise Token-balanced Output-Aware Clipping (CTOAC) method, which learns per-input-channel clipping bounds by minimizing a token-balanced reconstruction loss on the corresponding linear outputs. Only the selected linear layers and their input activations are quantized; other backbone operations retain their original precision. Across VSSD-Tiny, VSSD-Small, and VSSD-Base, the proposed CTOAC method retains ImageNet-1K accuracy and remains substantially more robust than the evaluated baselines at more aggressive precision settings. Applying the same quantization scope to VSSD backbones on COCO and ADE20K preserves strong object detection, instance segmentation, and semantic segmentation performance. An optimized RTX 4090 deployment configuration achieves up to 1.42x end-to-end speedup over FP32.

---


### 89. [DiaWhisper-DPO: Role-Attributed Transcription of Clinical Interviews via Failure-Mined Preference Optimization](https://arxiv.org/abs/2609.16661)

**<font color=#1a73e8>作者：</font>** Weiming Li, Ana Catarina Fidalgo Barata, Miguel Constante 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated depression screening from clinical interviews requires attribution of utterances to the clinician or patient. We evaluate two datasets: DAIC-WOZ, where participant-only recordings require re-synthesizing both sides for controlled two-party evaluation, and PDCH-HAMD, comprising voice-converted real Chinese interviews for cross-lingual validation. Cascaded systems combine speaker diarization with role-assignment heuristics, so errors can propagate across stages. We propose an end-to-end model, which we named DiaWhisper, that fine-tunes Whisper-large-v3 with LoRA and an auxiliary frame-level role head for transcription and attribution, together with DiaWhisper-DPO, a failure-mined refinement that uses genuine decoding failures as DPO rejected completions without human preference annotation. On 29 DAIC-WOZ test sessions, DiaWhisper-DPO achieves 0.973 role accuracy and 0.119 DER, 72% below the strongest cascaded baseline, and reduces seed variation from {\sigma} = .205 to .002. Retrained on PDCH-HAMD, it achieves 0.757 role accuracy and improves all 78 session-seed pairs.

---


### 90. [SAVTrack: Selective Vote Aggregation for Reliability-Aware Point Cloud Tracking](https://arxiv.org/abs/2609.16662)

**<font color=#1a73e8>作者：</font>** Sifan Zhou, Linyue Tan, Qiwei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D single object tracking (SOT) in LiDAR point clouds is essential for autonomous systems, but remains challenging under sparse and incomplete observations. In such cases, different target points provide highly uneven constraints on the object center, causing some point-to-center votes to be substantially less reliable than others. Existing point-based trackers typically aggregate these hypotheses without explicitly modeling their reliability, allowing inaccurate votes to contaminate proposal clustering and degrade localization accuracy. To address this issue, we propose \textbf{SAVTrack}, a motion-aware tracking framework with \textbf{Selective Vote Aggregation (SAV)}. SAVTrack estimates the reliability of each candidate vote from both local seed features and inter-frame motion context, and removes low-confidence hypotheses before proposal clustering. This pre-aggregation gating prevents unreliable hypotheses from affecting cluster formation while introducing only modest computational overhead. SAVTrack achieves competitive performance on KITTI and nuScenes, reaching 68.4/87.4 and 58.44/69.82 Success/Precision, respectively, while running at 82 FPS. It retains fewer than one-sixth of the candidate votes used by dense aggregation and remains particularly effective under sparse target observations.

---


### 91. [Lesion-centered 3D mapping of colonoscopy procedures: validation of a hierarchical ensemble pipeline on public benchmark videos](https://arxiv.org/abs/2609.16672)

**<font color=#1a73e8>作者：</font>** Hyunjun Kim, Hyeonwoo Na, Jaewoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Colonoscopy recording practice preserves text reports and still photographs, while the spatial information already present in the recorded video - where the scope traveled, where a lesion was observed, and whether the same lesion was seen again - is discarded when the procedure ends. This study determines whether a lesion-centered spatial record can be assembled and validated without full-colon 3D reconstruction. Methods: A four-layer hierarchical pipeline was assembled - (1) a global topological map, (2) lesion-level spatio-temporal tracks, (3) on-demand local 3D reconstruction, and (4) persistent lesion identity across repeated observations - and ran end to end on four public videos (two C3VDv2 sequences with ground-truth depth and two full REAL-Colon procedures; 40,245 frames). All components are published, individually validated methods; the contribution is their lesion-centered assembly, linking rules, and evaluation. Results: Revisits, impossible under forward-only mapping by construction, were detected by entry-map Bayesian localization: 5,614 and 4,043 revisit events (56 and 68 distinct nodes) in the two full procedures. Lesion-identity merging at the adopted threshold 0.5 maintained ground-truth purity 1.0 while auto-merging 20 of 231 candidate pairs. The endoscopy-specific geometry engine outperformed a general-purpose foundation model on all metrics (overall absolute relative error (AbsRel) 0.2276 vs. 0.3523). Conclusions: The results are partial but establish a concrete near-term path: revisit detection, lesion identity, and local 3D each returned quantitative, reproducible output without waiting for complete geometric reconstruction; validating the record on clinical data is the next step.

---


### 92. [From Hypervisor to Container: Cloud Security Vulnerabilities, Defense Mechanisms, and Open Challenges](https://arxiv.org/abs/2609.16675)

**<font color=#1a73e8>作者：</font>** Swapnil Vishwas Baviskar, Sanoj R, Hiran V Nath  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cloud computing, different users share the same physical hardware, which creates serious security risks. To protect data, cloud systems rely on virtual machines and containers to keep users isolated. This paper reviews over 120 security publications from 2008 to 2025, focusing on how these isolation boundaries can be breached. We examine threats like virtual machine escape, virtual machine hopping, CPU cache side-channels, container breakouts, vulnerable container images, and distributed denial of service (DDoS) attacks. We evaluate these security threats and their defenses using three key research questions. To compare different defense systems, we introduce a quantitative scoring framework called ADPO, which rates defenses from 0 to 3 based on their Accuracy, Deployment ease, Performance impact, and Operational overhead. We also map the impact of these attacks onto a 1-to-5 severity scale for Confidentiality, Integrity, and Availability. Finally, we highlight the trade-offs between security and system performance, and we outline open challenges like building low-overhead intrusion detection and creating realistic test datasets.

---


### 93. [MEgoVista: Multi-view Ego-aware Motion Estimation for Metric 4D Hands and Head in the Wild](https://arxiv.org/abs/2609.16684)

**<font color=#1a73e8>作者：</font>** Jiangong Xiao, Zhihao Zhang, Yifei Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning manipulation from human video requires high-fidelity hand-motion reconstruction in metric units. Today's metric hand labels come from studio rigs and instrumented headsets, and both are confined in the same two ways: neither leaves a prepared setting, and neither is checked against an independent reference. Unconstrained head-worn recording promises the opposite trade-off, scaling with the number of people wearing a device. We therefore introduce MEgoVista, an offline pipeline that turns a single unprepared MEgo View recording into metric two-hand and head motion in one gravity-aligned world frame. Three properties set it apart from existing egocentric reconstruction systems: first, it reconstructs in settings studio volumes and tabletop rigs cannot reach, settling hand ownership at detection so bystander hands stay out of the wearer's trajectory; second, it takes its metric gauge from calibrated stereo rather than a monocular prior, installing scale at initialisation so policies receive physical units, not arbitrary coordinates; third, both outputs are scored inside a motion-capture volume against independent Chingmu optical capture, under a protocol that audits its own reference and charges what a method declines to predict. MEgoVista is offered as a measured route from egocentric video to metric hand supervision, one that widens where such labels can be gathered.

---


### 94. [NephoCodex: Exploring Bounded Material Agency in Weather Data Physicalization](https://arxiv.org/abs/2609.16687)

**<font color=#1a73e8>作者：</font>** Yuxuan Weng, Yunge Wen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Weather is a complex, continuously changing system in which uncertainty is intrinsic. Physicalizing this uncertainty introduces further variation because computational outputs cannot fully determine material behavior. We distinguish computational uncertainty from material variability and introduce bounded material agency: computation constrains material realization without fixing its exact appearance. We present NephoCodex, a data physicalization system informed by a formative study that constructs five artistic weather states and predicts probability distributions over them. Probability-weighted mappings translate these distributions into material control proposals, while entropy-based regulation, local sensing, and safety constraints bound their execution through mist, airflow, light, and transparent displays. A within-participant study found increased spatial presence and physical demand, while perceived data comprehensibility remained inconclusive after correction. These findings contribute to hybrid data physicalization by showing how variable material expression can be paired with stable digital annotations and how embodied experience can be evaluated separately from data comprehension.

---


### 95. [Efficient 3D Whole-Body PET Image Denoising via Conditional Rectified Flow With Optimized Sampling Strategy](https://arxiv.org/abs/2609.16690)

**<font color=#1a73e8>作者：</font>** Jiale Shen, Guolin Wang, Chenhao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing radiation exposure in Positron Emission Tomography (PET) is important for patient safety; however, ultra-low-dose imaging suffers from severe noise, which may affect diagnostic interpretation without appropriate image enhancement. While current 3D deep generative models, particularly diffusion models, have shown strong reconstruction fidelity, their practical use can be limited by long inference times. In contrast, faster 2D-based alternatives may have difficulty maintaining volumetric consistency, an important consideration for whole-body PET imaging analysis. To bridge this gap, we propose a one-pass conditional 3D rectified flow (3D Flow) framework for whole-body PET image denoising that incorporates a novel optimized non-uniform sampling strategy. The model is trained with a one-pass linear-interpolant velocity-matching objective. This approach reconstructs a full 3D volume in approximately 30 seconds in our implementation, compared with multi-hour inference for the evaluated 3D DDPM baseline. Evaluations including zero-shot transfer to an independent clinical dataset show that our model achieves favorable global image quality and lesion conspicuity compared with the evaluated 3D DDPM and DDIM baselines, including on challenging short-acquisition data. Furthermore, the proposed method shows promising zero-shot transfer performance across the evaluated datasets and unseen dose levels (down to 1/100 of the standard dose), with artifact-focused visual comparisons supporting the need for further lesion-level validation. By balancing reconstruction fidelity and computational efficiency, this work presents a candidate approach for ultra-low-dose whole-body PET image denoising.

---


### 96. [MAETrack: Unleashing the Potential of Pretrained Geometric Priors for 3D Single Object Tracking](https://arxiv.org/abs/2609.16695)

**<font color=#1a73e8>作者：</font>** Sifan Zhou, Qiwei Wang, Linyue Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pre-training has transformed representation learning in 2D vision, yet its transferability to 3D single object tracking (SOT) remains insufficiently understood. Directly fine-tuning self-supervised 3D encoders, such as masked autoencoders (MAE), often leads to sub-optimal adaptation because the reconstruction objective is not fully aligned with the spatial-temporal matching requirements of tracking. In this paper, we observe that this difficulty can be interpreted as a layer-wise transfer mismatch: shallow layers tend to preserve transferable geometric cues, while deeper layers become increasingly specialized to the reconstruction pretext task and are less suitable for downstream tracking. Based on this observation, we propose MAETrack, a lightweight adaptation framework for transferring pre-training MAE representations to 3D SOT. MAETrack includes Layer-Selective Initialization (LSI), which initializes only the shallow stages of the tracking backbone from pre-trained weights while re-initializing deeper stages, and Geometric Residual Gating (GRG), which reinforces structurally salient regions in the search BEV features before template-search fusion through residual spatial modulation. Extensive experiments on standard 3D SOT benchmarks show that MAETrack consistently improves upon vanilla fine-tuning baselines with limited computational overhead. More broadly, our results suggest that effective transfer from 3D reconstruction pre-training to 3D tracking is not merely a matter of partial fine-tuning, but depends on a tracking-oriented transfer principle that preserves shallow geometry while adapting deeper representations to the downstream objective.

---


### 97. [Continuous-Time Machine Learning: A Unified Mathematical Perspective](https://arxiv.org/abs/2609.16710)

**<font color=#1a73e8>作者：</font>** Waleed Razzaq, Yun-Sheng Zhao, Yun-Bo Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time (CT) machine learning has emerged as a principled framework for modeling temporal dynamics as a continuous process, particularly when observations are sampled at arbitrary time points or span long-range horizons. However, major branches of CT machine learning have matured in separate research communities, leaving their mathematical relationships and design trade-offs insufficiently characterized. In this survey, we develop a unified, concept-driven view of major CT machine learning branches through a taxonomy that organizes families according to their underlying base mathematical formulations. We present a canonical mathematical formulation that relates these families through different architectural choices of vector-field parameterization, stochasticity, memory mechanisms, and discretization. We compare training algorithms, optimization strategies, and failure modes, highlighting the trade-offs across families. We further provide a comparative analysis of theoretical computational complexity alongside an illustrative architecture-controlled benchmark analysis on representative architectures from each family. We also review software ecosystems supporting their implementation. Finally, we identify open challenges in approximation theory, training stability, hardware-efficient implementations, benchmarking, foundation models, and scientific machine learning, and discuss an agenda for future research.

---


### 98. [PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation](https://arxiv.org/abs/2609.16727)

**<font color=#1a73e8>作者：</font>** Yihan Chen, Huan Ren, Wenfei Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level object pose estimation seeks to recover a similarity transform $(R,t,s)$ for unseen instances without instance-specific CAD models. Most competitive methods are correspondence-based: prior-free variants regress canonical (NOCS) coordinates directly from local observations and implicitly memorize the canonical frame in the weights, which ties the parameters to category-typical orientations and hurts generalization under distribution shift; prior-based variants introduce a category prior but typically follow a serial deform-then-align pipeline, where underconstrained canonical completion can corrupt correspondences and induce error cascades in pose. We propose PriorPose, a reference-guided correspondence framework that keeps the category prior explicit and solves canonicalization and alignment jointly in a shared feature space. A reference-guided seeded transformer embeds the partial observation and the category prior as token sets and fuses them via geometry-aware seeds, from which the network jointly predicts a per-point NOCS field for visible points and a canonical deformation of the prior that reconstructs a full canonical instance, while a deep pose head regresses $(R,t,s)$ from the induced correspondences. A two-part shape consistency objective, with canonical-space and camera-space consistency losses, couples correspondence, deformation, and pose, reducing reliance on memorized canonical orientations and avoiding deform-then-align error cascades. Experiments on standard and larger-category benchmarks demonstrate that PriorPose sets new state-of-the-art results on most evaluated metrics, especially under strict pose thresholds, while remaining competitive on relaxed pose and IoU metrics and showing improved robustness under shape variation and domain shift.

---


### 99. [When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents](https://arxiv.org/abs/2609.16732)

**<font color=#1a73e8>作者：</font>** Heng Li, Fulin Zhao, Zhe Geng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile agents are increasingly capable of autonomously interacting with mobile applications and performing consequential actions on behalf of users. Effective human oversight of such agents relies on a basic premise: users and agents observe consistent information from the same interface. We show that this premise can be systematically violated. Users perceive mobile interfaces through physical displays and the human visual system, making their observations subject to occlusion and luminance contrast limitations. In contrast, agents consume digital screenshots that may retain such content and accessibility representations that expose nonvisual widget metadata. The same UI state can therefore present materially different information to users and agents, a mismatch we term human-agent UI desynchronization. We investigate whether a repackaged clone of a legitimate APK can exploit this desynchronization to steer an agent toward attacker-designated actions, while remaining fully functional and behaviorally consistent with the original application for human users. We demonstrate that this threat is feasible: perturbations embedded before deployment can induce such deviations without access to runtime user instructions, agent detection or online adaptation. To systematically expose and evaluate this threat, we develop an automated framework that constructs user runtime instruction-agnostic UI desynchronization attacks and realizes them in deployable APKs. We conduct static and dynamic evaluations across five mobile-agent frameworks and three backbone models on 546 tasks involving various applications, achieving average misleading rates of 77.9% and 66.9%, respectively. A complementary questionnaire-based study with 186 participants finds that the visual perturbations used in our attacks are difficult for human users to notice.

---


### 100. [A Systematic Evaluation of Machine Learning Methods for Fault Detection and Line Identification in Electrical Power Grids](https://arxiv.org/abs/2609.16744)

**<font color=#1a73e8>作者：</font>** Julian Oelhaf, Georg Kordowich, Paula Andrea Pérez-Toro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of renewable energy sources into the electrical grid introduces complex challenges in fault detection and coordination of grid recovery mechanisms. Traditional relay protection systems, which operate based on static rules and predefined thresholds, are inadequate for addressing these challenges, particularly in detecting and isolating faults such as short circuits. Consequently, the conventional methodologies applied to electrical network protection frequently fail to achieve optimal performance in fault detection, especially in terms of adherence to safety standards and the selective limitation of damage. Recent research indicates that machine learning (ML)-based approaches can effectively tackle these issues; however, variations in grid configurations and analysis windows have impeded consistent comparative assessments. In this study, we assess the efficacy of various ML models in detecting electrical faults and pinpointing defective transmission lines within a 10 ms measurement interval - a critical time-frame for real-time operational viability, for the first time. The most effective model attained an F1 score of 0.991 +/- 0.018 and demonstrated a processing time of 0.342ms +/- 0.509ms.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
