# 📦 其他研究 | 2026年11月10日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-222](./part-05.md)

---

### 151. [Cutpurse: Decomposing Explanation-Guided Model Extraction on Tabular Data](https://arxiv.org/abs/2611.09375)

**<font color=#1a73e8>作者：</font>** Seyma Selcan Magara, Hanru Zhang, Fatme El Zahraa Hamad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Explanation APIs are often treated as increasing model-extraction risk, but an end-to-end attack comparison cannot show whether an explanation reveals model-specific information or merely supplies a convenient next-query coordinate. We study this distinction for explanation-guided extraction of tabular classifiers. We separate an explanation into an attribution channel, which ranks influential features, and a coordinate channel, which supplies candidate feature values for perturbing those features. We then test whether the useful bin edges are privileged to the service or reproducible from the adversary's own data.
Across six datasets and five target families, using attribution rankings to choose which features to perturb provides no systematic extraction advantage. Lime's discretization bin edges can improve fidelity by up to 41 percentage points on continuous features, but those edges are quantiles of the explainer's background data rather than properties of the target model. In controlled comparisons, an attacker-side grid reproduces the useful bin-edge gains without querying an explanation API. We use these findings to derive Cutpurse, which combines a self-computed grid with diverse query generation and boundary search. Against a service that withholds bin edges, Cutpurse improves fidelity by 16.3 percentage points on continuous-feature targets. It also exceeds the undefended published attack by 7.0 percentage points. Thus, withholding default Lime bin edges alone does not prevent effective extraction under the in-domain auxiliary-input, probability-output, and same-family surrogate assumptions studied here. Our results concern default Lime and Shap configurations for tabular classifiers. They do not establish the same conclusion for other explainers, target classes, or data-free attackers.

---


### 152. [KineCouple: Substrate-conditioned residual readout for enzyme kinetic prediction](https://arxiv.org/abs/2611.09377)

**<font color=#1a73e8>作者：</font>** Chun Kang, Yunbo Zhang, Fanhu Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of enzyme kinetic parameters can support enzyme engineering and metabolic modeling by complementing experimental characterization. Existing prediction methods often pool residue-level protein features before combining them with substrate features. Such substrate-independent pooling cannot adapt residue weighting to the substrate during aggregation, potentially diluting information relevant to a specific enzyme-substrate pair. Since the contributions of individual residues to catalysis can depend on the substrate, substrate-conditioned aggregation offers a way to emphasize residue features relevant to the prediction. We introduce KineCouple, which uses substrate queries and residue-level keys and values in cross-attention, allowing the substrate to guide residue selection before aggregation. The model preserves the global protein representation and adds a gated correction defined as the difference between the conditioned readout and a uniform readout. ProtT5 and MolT5 remain frozen, and separate models predict kcat and Km on a logarithmic scale. In pooled out-of-fold predictions on the CataPro benchmarks, KineCouple reduces kcat RMSE from 1.333 to 1.330 and increases PCC from 0.492 to 0.496 relative to reproduced CataPro. For Km, RMSE decreases from 0.998 to 0.997 and PCC increases from 0.633 to 0.634. Spearman correlation also improves for both tasks.

---


### 153. [A Bridge from Paste to Place: Physics-Guided One-Step Image Composition via Object-Scene Interaction](https://arxiv.org/abs/2611.09387)

**<font color=#1a73e8>作者：</font>** Hongzhen Li, Youwei Pan, Yingfang Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic image composition must make a pasted object appear naturally present in a scene while preserving the fine details of both foreground and background. Reference-based insertion methods can change object pose and appearance, while foreground harmonization methods and shadow-specific synthesis methods each address only part of this task. An efficient, unified solution to this task remains an open challenge. We introduce Paste2Place, an end-to-end, physics-guided flow-based model that learns a direct, one-step latent bridge from pasted inputs to realistic composites, guided by explicit albedo-shading-residual decomposition and recomposition within the model. To support model training and evaluation, we develop a Blender rendering and validation pipeline to generate paired composites with physical annotations, and construct real-scene pairs from open-source object-removal data. This effort yields 86,273 training pairs and a 1,500-example benchmark. Extensive qualitative and quantitative experiments demonstrate that Paste2Place achieves substantial advantages in image composition quality and inference speed. Overall, our work provides a clear task definition and an effective solution for image composition, and fills a gap in large-scale, high-quality datasets and benchmarks for training and evaluating image composition.

---


### 154. [k-Volume: a Unified Active Learning Strategy](https://arxiv.org/abs/2611.09388)

**<font color=#1a73e8>作者：</font>** Eliot Tron, Alain Celisse, Christophe Denis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the classification context where revealing the label of a sample is costly, we propose a new Active Learning (AL) strategy named k-Volume (kVol). It randomly selects a sample to be labeled according to the volume of the smallest ball containing its k nearest neighbors. kVol is highly versatile: it can be applied either in the input space or in the output space, and it enjoys the desirable properties of the three main families of AL strategies: density, diversity, and (when performed in the output space) uncertainty. From a theoretical perspective, we establish that kVol is asymptotically equivalent to uniform sampling over the support of the (input or output) data distribution. Based on experiments on various synthetic and real-life tabular datasets and images, we observe that kVol is surprisingly stable: whatever the classifier or the experimental setup, it still lies among the best AL strategies unlike other competitors that fail dramatically. In particular, kVol outperforms state-of-the-art competitors such as CoreSet, TypiClust or Uncertainty on several real-life datasets, at a low computational cost.

---


### 155. [Travel Cost Calibration for Multi-Agent Target Assignment and Pathfinding](https://arxiv.org/abs/2611.09396)

**<font color=#1a73e8>作者：</font>** Yu Kumagai, Ryohei Banno, Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Target assignment and pathfinding (TAPF) is an appealing extension of classical multi-agent pathfinding (MAPF): each agent has a set of targets, and the planner must both assign a target to each agent and plan collision-free paths for them. A trivial approach is to compute an assignment that minimizes the total single-agent shortest-path distance over agent--target pairs, and then solve the resulting MAPF instance. However, this approach falls short because the shortest-path distance remains a proxy that ignores interference among agents. Assigning targets based on the costs agents actually pay, which depend on how every other agent is assigned and routed, would yield a better final outcome. To this end, we propose an iterative TAPF method that improves target assignments by calibrating travel cost estimates from fast, suboptimal MAPF feedback. Experiments show that our method produces solutions close to optimal on small instances and outperforms existing planners in solution quality on larger ones.

---


### 156. [A Spiking Neural Model of the Mental Lexicon: Representations, Similarity Structure, and Associative Retrieval in Perception and Production](https://arxiv.org/abs/2611.09402)

**<font color=#1a73e8>作者：</font>** Bernd J. Kröger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A neural account of lexical access requires an explicit distinction between the structure of lexical representations, the associations linking representational levels, and the activity generated during retrieval. This paper specifies a spiking neural implementation of the mental lexicon within the Neural Engineering Framework and Semantic Pointer Architecture. Conceptual and phonological form representations are constructed recursively from relational graphs, whereas lemma representations provide independent lexical identities. The implementation contains 613 lexical entries and supports two directed processing pathways: perception maps a phonological form to its associated concept via a lemma, whereas production maps a concept to its associated phonological form via a lemma. Each pathway combines two associative-memory variants, winner-take-all (WTA) selection (competition) and thresholded transfer, and uses 199,400 leaky integrate-and-fire neurons. We formalize within-level similarity, cross-level associative retrieval, and the interpretation of decoded activity. Simulations show successful retrieval of eight selected words from the lexicon in both processing directions, with retrieval evaluated against all 613 lexical entries. These simulations use complete phonological forms as input for perception and complete concepts as input for production, illustrating lexical retrieval through the corresponding processing pathways. This paper provides a transparent description of lexical representations and neural retrieval mechanisms, supported by accessible code, lexical data, and online simulation documentation.

---


### 157. [Future-Informed Actor-Critic](https://arxiv.org/abs/2611.09417)

**<font color=#1a73e8>作者：</font>** Samy Mokeddem, Gaspard Lambrechts, Adrien Bolland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Actor-critic methods optimize a parametrized policy using a critic to estimate their policy gradient. Recent work has shown that conditioning the critic on features of future states, actions, or rewards can improve sample efficiency and even final return. However, existing methods are restricted to exogenous features (independent of actions), overlooking endogenous features (dependent on actions) that may be crucial for credit assignment. We introduce the future-informed value function, which can be conditioned on both exogenous and endogenous features of future states, actions, and rewards. Then, we express the policy gradient using this value function, yielding the future-informed policy gradient. Building on that, we propose the future-informed actor-critic algorithm. Empirical results show that this algorithm leveraging endogenous features of the future outperforms standard actor-critic algorithms in environments with noisy and sparse rewards.

---


### 158. [DeepRadio: A Human-Agent Workspace for Physical Radio Development](https://arxiv.org/abs/2611.09418)

**<font color=#1a73e8>作者：</font>** Jiazhen Lei, Yuxin Sha, Sihan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic programming can automate software-defined radio (SDR) development, but decisions can propagate from software to hardware without sufficient user visibility or control. We present DeepRadio, a human-agent workspace embedded in GNU Radio Companion (GRC) for jointly constructing, verifying, and operating physical radio systems. DeepRadio uses a dynamic and state-driven workflow to coordinate a traceable radio specification, claim-oriented cross-layer verification, and mixed-initiative control. These mechanisms expose decisions, tie conclusions to available evidence, and return control to users before consequential hardware actions. Across seven atomic SDR tasks, DeepRadio completed nearly all runs while satisfying all prescribed software and radio-frequency constraints. In a 20-participant study, more participants achieved a verified physical deployment with DeepRadio than with Codex-assisted GRC. Participants reported stronger support for shared intent and understanding while retaining initiative and control. These results suggest that DeepRadio can make agent-assisted physical radio development more reliable, understandable, and controllable.

---


### 159. [Robust & Scalable Website Fingerprinting via Minimal DRAM Traffic](https://arxiv.org/abs/2611.09422)

**<font color=#1a73e8>作者：</font>** Shubham Roy, Samar Parwez, Biswabandan Panda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Website fingerprinting attacks infer websites visited by users and threaten their privacy. These attacks are classified as on-path, which monitor network traffic, and co-located, which exploit shared system resources. Existing co-located attacks, such as sweep-counting and loop-counting, achieve over 90% accuracy but suffer significant performance degradation on many-core systems. Loop-counting accuracy drops from 93% on 8 cores to 50% on 24 cores, while sweep-counting accuracy decreases from 84% to 45% across multiple Core Complex Dies (CCDs). To address these limitations, we propose memory-chasing, a scalable website fingerprinting attack that exploits DRAM traffic interference through pointer-chasing traversals with minimal interference. By counting DRAM accesses over fixed intervals, the attack generates distinctive traces for website classification. Evaluated on the top 50 websites, memory-chasing achieves 96% accuracy on a 24-core system, 86% across multiple CCDs, 80% across multiple sockets, and 97% in an open-world setting. Extensive evaluation across hardware configurations, browsers, operating systems, isolation mechanisms, system noise, and countermeasures demonstrates its robustness and scalability.

---


### 160. [DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning](https://arxiv.org/abs/2611.09433)

**<font color=#1a73e8>作者：</font>** Seokin Seo, Sung Kuk Shyn, Minji Seo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring high returns while providing strong safety guarantees in offline imitation learning (IL) is a fundamental challenge: existing approaches either rely on explicitly specified cost functions, which are difficult to design for complex real-world safety constraints, or require expert demonstrations that are both safe and high-performing, which are often too costly to collect. We introduce dual-expert imitation learning, which leverages two complementary data sources: (i) safety-compliant demonstrations that faithfully follow safety guidelines but may be suboptimal, and (ii) performance-oriented demonstrations that achieve high returns but may violate safety guidelines. To address this problem, we propose DexDICE (Dual-expert offline imitation learning via stationary DIstribution Correction Estimation). Instead of conventional distribution constraints, DexDICE combines DICE-style offline learning with safe support constraints, enabling agents to exploit high-return behaviors while remaining within safety-compliant regions. We prove that the ideal solution satisfying this constraint exactly has zero unsafe-region visitation with high probability. We evaluate DexDICE on a re-curated DSRL benchmark and validate it on a real-world mobile-robot navigation task trained directly from human teleoperation demonstrations, where it substantially outperforms baselines and remains robust to data scarcity and quality degradation.

---


### 161. [The Role Of Recurrent Refinement In Medical Image Segmentation](https://arxiv.org/abs/2611.09436)

**<font color=#1a73e8>作者：</font>** Joao D.S. Marques, David Calhas, Arlindo L. Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While feed-forward segmentation networks perform well on large cohorts, they degrade in constrained clinical settings with few training samples and imaging artifacts. Human vision, by contrast, remains robust under these conditions, a property partly attributed to the recurrent and feedback connectivity of the visual cortex, which refines visual information over time. Inspired by this, we append lightweight recurrent refinement blocks to segmentation backbones, namely Conditional Random Fields (CRFs), modern Hopfield networks and convolutional GRUs, and study their behaviour as the number of iterations increases at test time (including beyond the training horizon). Evaluated on two open-source datasets, Kvasir- SEG and ARCADE, our recurrent blocks add less than 1.5% parameters and yield gains on clean data (up to 1.4 pp) and under noise (up to 17 pp) while reducing HD95. Code is available at this https URL .

---


### 162. [Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2611.09448)

**<font color=#1a73e8>作者：</font>** Song Yu, Li Li, Zhenming Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy entropy is widely used to diagnose exploration and collapse in reinforcement learning with verifiable rewards (RLVR), yet its magnitude does not consistently track reasoning performance across optimization objectives. We argue that this ambiguity arises because global token entropy conflates uncertainty in successful and failed trajectories, diversity across correct solution strategies, and variation among realizations of the same strategy. We introduce \textbf{Reward-Conditioned Entropy Allocation (RCEA)}, a hierarchical diagnostic framework that separates complete-trajectory entropy from average token entropy, conditions uncertainty on verifier outcome and process validity, measures correct-solution-mode retention, and connects these population-level quantities to local covariance-driven updates. In controlled sweeps over six RLVR objectives at two model scales, entropy trajectories do not induce a stable ordering of reasoning accuracy. Token entropy is higher for verifier-failed than successful trajectories under both broad separately aggregated estimates and a common-question paired analysis, whose confidence intervals exclude equality at 10 of 12 displayed endpoints. A local covariance approximation predicts the direction of adjacent-checkpoint entropy change in 95.5\% of nonfailed transitions; a reward-stratified endpoint proxy further shows that positive chosen-token covariance is more tail-concentrated within failed prefixes. Every reportable trained endpoint exhibits some contraction in independently audited correct-solution-mode breadth, whose positive association with large-\(k\) coverage remains exploratory. These results show that entropy collapse should be diagnosed by which uncertainty is removed, rather than by global entropy alone.

---


### 163. [Overview of the ImageCLEFmedical 2026 GANs task: Exploring fingerprint detection, privacy leakage, and synthetic medical image generation](https://arxiv.org/abs/2611.09455)

**<font color=#1a73e8>作者：</font>** Alexandra-Georgiana Andrei, Mihai Gabriel Constantin, Mihai Dogariu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 2026 ImageCLEFmedical GANs Task Exploring Fingerprint Detection, Privacy Leakage, and Synthetic Medical Image Generation continues to investigate privacy and security concerns around using patient data to generate synthetic medical images, now in its fourth edition. This edition introduces three complementary subtasks: the first extends prior editions by asking participants to detect which real images were used in training a Generative Adversarial Network to produce given synthetic outputs; the second is a novel subtask requiring participants to identify which latent vector produced each synthetic image, probing the faithfulness and reversibility of the latent-to-image mapping; the third asks participants to generate privacy-preserving CT slices, quantifying the trade-off between image fidelity and patient privacy. Ground-truth annotations and benchmark datasets of real and GAN-generated lung CT slices are provided for all subtasks. Evaluation is based on Cohen's Kappa for Subtask 1, matching accuracy for Subtask 2, and a combination of FID and Privacy Preservation Score (PPS) for Subtask 3. Overall, 37 teams registered for the task, with 10 teams submitting runs across subtasks and 6 teams submitting working notes papers. This paper presents an overview of the task setup, datasets, evaluation metrics, and summarises the approaches and results of participating teams.

---


### 164. [Left-Right-Consistent Iterative Stereo Matching via Cross-Injection](https://arxiv.org/abs/2611.09458)

**<font color=#1a73e8>作者：</font>** Manuel Knott, Diogo Luvizon, Daniel Scharstein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art stereo matching models predominantly predict the disparity of only the left (reference) view. However, applications such as per-eye AR/VR rendering, novel view synthesis, or two-view depth fusion require disparity for both views, and need those two maps to agree. The usual workaround of running the network a second time on the horizontally flipped and swapped pair gives two independent predictions that can be inconsistent, especially on transparent surfaces, in textureless regions, and at occlusion boundaries. We introduce cross-injection (CI), a lightweight extension for iterative (refinement-based) models that can be added to any pretrained left-only iterative matcher. It couples the two passes by injecting the explicit, signed left-right inconsistency as an additional input cue at every step of the refinement stage. We empirically show that CI substantially reduces left-right disagreement on every benchmark (more than halving it on Booster for FoundationStereo), while largely preserving sharp object boundaries. Furthermore, using two state-of-the-art stereo matching models, we show that CI also reduces the single-view disparity error, making it a worthwhile extension even if only left disparity is needed.

---


### 165. [Consensus-Constrained Dual-Federated Optimization with Client-Side Dynamic Weighting for Distributed Android Device Threat Defense](https://arxiv.org/abs/2611.09470)

**<font color=#1a73e8>作者：</font>** Mohammad Mashreghi, Mohammad Hossein Badiei, Md. Jalil Piran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smartphones, smart-home hubs, and wearables are increasingly exposed to sophisticated Android malware, while centralized threat-detection pipelines raise privacy and scalability concerns. Federated learning (FL) enables collaborative model training without collecting raw client data, but partial participation and variation in local model quality can destabilize global optimization. In this article, we propose DW-FedADMM, a federated optimization framework that combines primal-dual coordination with performance-dependent client-side weighting. The dynamic coefficient modulates each participating client's local state before the augmented-Lagrangian update, while the dual variables regulate disagreement between local and global model states. We evaluate DW-FedADMM on three Android malware benchmarks, namely Drebin, Malgenome, and TUANDROMD, with 5, 10, and 15 clients holding IID data shards, partial client participation, and communication budgets of 5 and 10 rounds. Each configuration is repeated with ten random seeds. DW-FedADMM obtains the highest seed-averaged accuracy on Drebin (97.64% +/- 0.20%) and the best mean accuracy in 9 of the 18 dataset-client-round configurations, including 7 of the 9 configurations with a 10-round budget. Pooled over all configurations, it reaches 95.42% accuracy, 94.62% F1-score, 96.06% precision, and 99.45% AUC, compared with 95.32%, 94.51%, 95.56%, and 99.41% for FedADMM, while also giving the lowest mean false-positive rate and the smallest client update norm among the six compared methods. Both primal-dual methods are well ahead of the averaging- and proximal-based baselines on Malgenome and TUANDROMD, where the latter often remain at the majority-class solution when clients are fragmented. The gain of dynamic weighting over FedADMM is most pronounced on Drebin and with the longer communication budget, where it also reduces the variation across seeds.

---


### 166. [FusionCLIP: Multimodal Contrastive Pretraining for Fusion Plasma Diagnostics](https://arxiv.org/abs/2611.09493)

**<font color=#1a73e8>作者：</font>** Qiang Chen, Xiao Wang, Qingquan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-light videos and multivariate diagnostic signals provide complementary observations of tokamak discharges. However, existing fusion pretraining methods, primarily learn representations by reconstructing or predicting observations, leaving the correspondence between these modalities underexplored. Representation learning is further challenged by the fact that plasma-related regions occupy only part of each video frame and diagnostic variables have substantially different sampling rates. We propose FusionCLIP, a multimodal contrastive pretraining framework. Spatiotemporal Stability Selection retains informative visual tokens, while a Temporal Query Encoder integrates asynchronous diagnostic signals using their observation timestamps. Contrastive learning then aligns the two modality representations. We construct EAST Multimodal Diagnostics (EAST-MMD), comprising 1307 EAST discharges, and evaluate the model on three independently fine-tuned tasks: disruption prediction, edge-localized mode (ELM) classification, and $H_{98}$ regression. FusionCLIP achieves an aggregate score of 89.07\%, exceeding the best general-purpose pretraining configuration and an in-domain contrastive pretraining configuration without Spatiotemporal Stability Selection by 6.27 and 2.12 percentage points, respectively. Ablations and attention visualizations further support the contributions of its key components.

---


### 167. [Mosaic:montage-agnostic self-distilled graph learning for subject-independent ieeg seizure detection](https://arxiv.org/abs/2611.09496)

**<font color=#1a73e8>作者：</font>** Arya Jalali, Mahsa Shoaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intracranial EEG provides high signal-to-noise ratio and spatial resolution for detecting epileptic activity, but patient-specific electrode placement leads to substantial variation in channel count and montage across subjects. This heterogeneity limits the generalization of existing detectors under subject-independent evaluation. We propose MOSAIC (MOntage-agnostic Self-distilled Adaptive Inter-channel Connectivity learning), a lightweight graph-learning framework for subject-independent iEEG seizure detection. MOSAIC pairs a shared convolutional channel encoder with a patient-agnostic channel-attention module that infers a weighted inter-channel adjacency matrix from the encoded features, requiring no fixed montage graph. An exponential moving average self-distillation objective regularizes each prediction toward a slowly updated per-patient teacher. Across four public iEEG corpora (SWEC-ETHZ long- and short-term, Mayo, FNUSA), MOSAIC outperforms state-of-the-art baselines in F2 and Cohen's $\kappa$ while learning more stable inter-channel adjacencies, demonstrating that self-distilled connectivity learning transfers across unseen implantations.

---


### 168. [e-means: outperforming k-means (in one-tenth the epochs)](https://arxiv.org/abs/2611.09501)

**<font color=#1a73e8>作者：</font>** Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

---


### 169. [BEiTScore++: Reference-free Image Captioning Evaluation with BEiT-3 and Conformalized Quantile Regression](https://arxiv.org/abs/2611.09505)

**<font color=#1a73e8>作者：</font>** Gonçalo Gomes, Bruno Martins, Chrysoula Zerva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is important for deploying evaluation metrics in real-world settings, where both input ambiguity and domain shifts are common. In this work, we propose an uncertainty-aware extension of the BEiTScore image captioning metric, producing conformally calibrated confidence intervals alongside alignment scores. Our approach models predictive distributions over human judgments, enabling both accurate scoring and principled uncertainty quantification in a single forward pass. We evaluate our BEiTScore++ metric across multiple benchmarks with human-annotated ratings, showing that it preserves the ranking correlation of BEiTScore, while producing intervals whose width tracks the prediction error more closely than Monte Carlo dropout on most benchmarks. The estimated uncertainty also grows under image degradation and on out-of-domain artwork images, making BEiTScore++ a practical tool for uncertainty-aware evaluation of image-caption alignment.

---


### 170. [A Physics-Informed Learning Framework for Linking Microscopic Surface Degradation to Bolted Joint Functional Behavior](https://arxiv.org/abs/2611.09514)

**<font color=#1a73e8>作者：</font>** Nehal Afifi, Gerhard Kachel, Sven Matthiesen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Returned products in circular engineering often have heterogeneous degradation histories, making remaining function difficult to assess. For bolted joints, corrosion alters surface morphology, contact, friction, preload retention, and mechanical response. This paper presents a physics-informed multimodal framework for linking microscopic and camera-based degradation observations to functional indicators of corroded bolted joints. The workflow defines the corrosion failure mode, generates synchronized inspection and functional-response records, preprocesses image, roughness, exposure, and joint descriptors, aligns microscopy and camera observations through similarity learning, and constructs a calibrated corrosion-severity field. Partial differential equation (PDE) discovery is applied to this field to identify candidate effective mesoscale laws rather than complete electrochemical mechanisms. The corrosion-evolution model is coupled to a separate functional model, with friction coefficient as the primary target and preload loss included when clamp-force data are available. The contribution is a reproducible pathway for physically constrained assessment of degraded bolted-joint behavior.

---


### 171. [Benchmarking Speaker Embedders in the Sub-Second Regime for Real-Time Voice AI Agents](https://arxiv.org/abs/2611.09516)

**<font color=#1a73e8>作者：</font>** Abhishek Gautam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time Voice AI agents must separate the active user from intelligible background speech that survives conventional noise suppression. Background sources include television audio, family members, and colleagues. Production denoisers remove non-stationary environmental noise effectively. Background speech shares the spectral characteristics of the target and passes through, causing false acceptances in downstream speaker verification (SV) and automatic speech recognition (ASR). We benchmark open-source speaker embedders TitaNet-Large, TitaNet-Small, ECAPA-TDNN, CAM++, and SpeakerNet under a strict sub-second latency budget. Evaluation combines a controlled benchmark with a weighted human-annotated production set. Our controlled benchmark is built from real calls in which a second real speaker is injected into silence intervals at modulated amplitude. We report three findings. First, denoising before embedding is generally harmful and raises equal error rate (EER) across architectures. Second, truncating audio below the full voice-activity segment degrades every model. Third, roughly half of the TitaNet embedding is redundant for this task. Trailing dimensions encode population attributes such as language and gender. Such attributes carry little discriminative value in a demographically homogeneous user base. We distill these results into deployment guidance. Verification should run on raw audio with full voice-activity chunks. Thresholds should favor precision over F1. Truncated embeddings reduce the cost of similarity search.

---


### 172. [Active Learning of Robust Models](https://arxiv.org/abs/2611.09520)

**<font color=#1a73e8>作者：</font>** Mizu Nishikawa-Toomey, Andreas Kirsch, Laurent Charlin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many domains from species identification to cancer diagnosis, labelling data to train predictive models remains costly. In these settings, it is advantageous to intelligently select data points to label to achieve the maximum information gain, this is the motivation behind the study of active learning. In addition to the high costs of acquiring data in such domains, there is the added complexity of data distribution shifts that can occur between training and deployment. For example, the features of cancerous skin cells taken in one country may be different in another region of the world. These two challenges - efficient labelling of data, and learning models robust to distribution shifts have been studied separately but not together, even though these challenges often co-occur in real-life settings. We identify failure modes of standard active learning approaches when the distribution of data at deployment is different from the distribution in which the data is sampled for labelling. We propose a new strategy for efficiently learning classifiers that generalise under specific forms of distribution shift, namely subpopulation shift. Drawing on work in learning from heterogeneous data, we aim to train models that perform well across subpopulations of the data, through active learning. To handle this challenging setting, we exploit the fact that many datasets include metadata about data collection that can serve as a noisy proxy for each sample's underlying subpopulation. We demonstrate how to leverage these noisy labels during active learning selection, and demonstrate empirically that our approach improves classifier accuracy across subpopulations.

---


### 173. [Embedding Predictive Adaptation and Refinement for Multi-Modal Industrial Anomaly Detection](https://arxiv.org/abs/2611.09521)

**<font color=#1a73e8>作者：</font>** Jaeho Cho, Jinsik Bang, Taehwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial Anomaly Detection (IAD) has evolved from 2D image-based approaches to multi-modal methods that leverage the complementary nature of RGB images and 3D point clouds. Among these, memory bank-based methods, which identify anomalies by the discrepancy between each query patch feature and its nearest normal prototype, have proven particularly effective. However, two limitations remain: (i) employing frozen pretrained encoders yields insufficient discrimination between normal and anomalous features due to the domain gap, while existing contrastive learning-based adaptation struggles to capture the spatial relationships required for precise localization; and (ii) pixel-level anomaly maps interpolated from patch-level distance scores remain coarse, lacking fine-grained detail. To address these limitations, we propose EPAR (Embedding Predictive Adaptation and Refinement). We adapt encoders by predicting the embeddings of masked regions to capture spatial relationships, together with patch-level Variance-Invariance-Covariance (VIC) regularization, resolving the poor discriminability between normal and anomalous features caused by the domain gap. We further propose a Noise Suppression Network that refines coarse maps by learning the relational discrepancy between each patch feature and its nearest normal prototype, rather than the anomaly's appearance. This relational signal remains valid for unseen real defects, despite being learned from synthetic anomalies. EPAR demonstrates strong practical applicability, excelling in few-shot settings and improving AUPRO@1% on MVTec 3D-AD and Eyecandies by +1.8% and +1.9%, respectively.

---


### 174. [ExQuery: Explicit Structured Query Priors for Temporal 3D Object Detection](https://arxiv.org/abs/2611.09527)

**<font color=#1a73e8>作者：</font>** Honglin Sun, Yifei Zhang, Junyang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse query-based 3D detectors commonly encode heterogeneous semantic, geometric, and motion information into unified latent queries, including when explicit 3D anchors are used. We introduce ExQuery, an explicit structured query framework for temporal 3D object detection. Each decoded query is organized into a shared semantic context slice and physical-state-specific slices for center, dimensions, orientation, and velocity. This structure is preserved from prior encoding to branch-specific regression and is reused to reconstruct temporal queries: predicted physical states are transformed by ego motion, classification scores form soft semantic priors, and the reconstructed query is fused with the stored latent instance feature through gated affine modulation. Experiments on the nuScenes benchmark show that our method achieves competitive detection performance, and ablation studies validate the effectiveness of our proposed modules.

---


### 175. [PreForceVision: Physics-Guided Optical Estimation of Bolt Preload from Bolt-Head Deformation](https://arxiv.org/abs/2611.09529)

**<font color=#1a73e8>作者：</font>** Nehal Afifi, Klaus Rappenecker, Florian Peinhardt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bolt preload is a decisive functional quantity in bolted joints because it determines whether external loads are transmitted primarily through frictional clamping or directly through the bolt. Existing preload measurement techniques, including strain-gauge bolts, force washers, ultrasonic methods, and bolt-length measurements, are effective in certain applications but require additional hardware, coupling, calibration, or joint modifications. This limits their scalability for large numbers of standard fasteners and motivates a non-contact optical approach. This paper proposes PreForceVision, a physics-guided optical framework for estimating bolt preload from preload-induced surface deformation of the bolt-head front face. The method treats preload estimation as an inverse deformation-to-force problem, where deformation of the optically accessible bolt-head surface is extracted from reference-loaded image pairs and related to the internal preload state. Preliminary results for an M16 strength class 8.8 bolt show an approximately \SI{12}{\micro\meter} simulated head-face depression at \SI{90}{\kilo\newton}, strain-gauge measurements of comparable magnitude, and an optical 3D measured central depression of approximately \SIrange{10}{20}{\micro\meter}. The contribution is a physics-guided optical methodology combining controlled image-pair acquisition, DIC- or optical-flow-based deformation extraction, multimodal validation, and uncertainty-aware regression for rough preload estimation under controlled conditions.

---


### 176. [Marginal-Nonuniform Multiclass Learning](https://arxiv.org/abs/2611.09543)

**<font color=#1a73e8>作者：</font>** Nataly Brukhim, Steve Hanneke, Amirreza Shaeiri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of multiclass classification within the framework of marginal-nonuniform learning, where the constants in the learning rate may depend on the unknown marginal distribution generating the unlabeled data, but not on the target concept. This notion naturally lies between classical PAC learning, where the constants are independent of both the marginal distribution and the target concept, and more recent universal learning, where the constants may depend on both. We give a complete characterization of the optimal marginal-nonuniform learning rates, establishing a fundamental trichotomy: exponential, linear, and arbitrarily slow rates. This characterization is witnessed by a new combinatorial dimension, termed the uncentered DS-eluder dimension. A key ingredient in the upper-bound proofs is a set of new distributional exhaustion lemmas that exploit the sequential nature of this dimension and may be of independent interest.

---


### 177. [CoMoFlow: Controllable Protein Conformational Ensemble Generation via Explicit Collective-Mode Modeling](https://arxiv.org/abs/2611.09548)

**<font color=#1a73e8>作者：</font>** Yusong Wang, Zheyuan Gu, Ailiang Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein conformational ensemble generation aims to efficiently characterize the structural variations accessible to a protein beyond a single static structure. Recent flow-based methods efficiently generate conformational ensembles, but they model coordinated structural variation implicitly, which can limit ensemble fidelity and hinder direct control. To address this limitation, we propose CoMoFlow, a controllable framework for generating protein backbone conformational ensembles by explicitly modeling collective variation. CoMoFlow constructs protein-specific collective modes from the equilibrium structure, learns the distribution of their coefficients across the molecular dynamics (MD) ensemble, and uses sampled collective variations to guide SE(3) flow matching through feature conditioning and prior recentering. Experiments on ATLAS and de novo proteins show that CoMoFlow improves reconstruction of MD conformational distributions and coordinated structural variation relative to strong flow-based baselines, while enabling direct control over targeted conformational changes.

---


### 178. [Solver-Free Decision-Focused Learning via Neural Optimization Layers for Edge Selection](https://arxiv.org/abs/2611.09560)

**<font color=#1a73e8>作者：</font>** Xinda Zheng, Frits de Nijs, Edward Lam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning trains prediction models to improve downstream decisions, but many methods require costly solver calls or optimal-solution labels. We propose a solver-free decision-focused learning framework for NP-hard edge-selection problems with uncertain parameters in the objective, the constraints, or both. A neural optimization layer is first trained without solution labels, using problem objectives and constraint penalties. Graph-informed edge scoring and iterative refinement encourage concentrated and structurally consistent continuous decisions. The layer is then frozen, and a prediction model is trained through its continuous output using a problem-specific loss evaluated under observed parameters. At deployment, the predictor, optimization layer, and a lightweight decoder produce decisions without solving the original NP-hard problem. Experiments on the asymmetric traveling salesperson and endpoint-free orienteering problems show consistently better decision quality than prediction-focused learning and improvements over most evaluated decision-focused baselines. Our framework requires less training time than the evaluated decision-focused baselines, even when optimization-layer pretraining is included. Neural deployment also produces decisions faster than solver-based deployment, offering a better quality-efficiency trade-off. The layer also reduces training cost in existing decision-focused methods when used as an approximate optimization oracle.

---


### 179. [Performance Bottlenecks in Computing ZK Proofs on a GPU](https://arxiv.org/abs/2611.09569)

**<font color=#1a73e8>作者：</font>** Victor Carolino, Caleb Geren, Michael Kaufman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge proofs allow one party to prove the correctness of a statement or execution of a computation while revealing no more than the statement of correctness itself. Recent use cases, such as AI datasets, suggest the need for faster proof generation over increasingly large constraint sets. This paper explores efforts in optimizing zero-knowledge proof generation, specifically PlonK, using GPUs, for applications that are not amenable to solution via incrementally verifiable computing (IVC).
Our intention with this work is to improve ZK performance by introducing fundamental changes in the low-level architectural structure of proof generation. These changes affect performance curves for most current proof
generation algorithms. In particular, this paper explores the trade-offs between increased parallelization on GPUs and the resultant memory management problems that occur due to this parallelization. We implement a parallelized PlonK in order to analyze these trade-offs and make arguments concerning the nature of data flows within the proving protocol. Our results lead us to consider multi-GPU environments to maximize performance for large circuit sizes. Such environments introduce issues of communication, efficient hardware management, data partition, and data
transfers. This paper further discusses the use cases that motivate multi-GPU implementations, their cost models, and the use of remote direct memory access (RDMA) for data transfer among GPUs.

---


### 180. [Video Stitching from Multiple Moving Cameras](https://arxiv.org/abs/2611.09570)

**<font color=#1a73e8>作者：</font>** Shira Ifergane, Roy Amoyal, Shahar Benishay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address geometric video alignment for the same scene captured by multiple freely moving cameras. Existing methods, which are based on image stitching or video stabilization, are typically limited to two cameras or must assume the restrictive setting of a fixed linear ordering of the cameras. We propose MViS, a lightweight test-time optimization framework for joint multi-view alignment with temporal consistency. MViS uses a spatial-transformer-inspired net to jointly process frames from all views within a short temporal window and predict per-view, per-time homographies. Optimization proceeds in two stages: geometry-guided alignment followed by appearance-based refinement, with both stages enforcing multi-view and temporal consistency across the sequence. The method requires no scene-specific hyperparameter tuning, handles arbitrary and time-varying view-intersection graphs, and remains robust under rapid camera motion. On a standard two-view video benchmark, MViS matches or surpasses the state of the art. To facilitate evaluation in more complex scenarios, we introduce an annotated dataset with more than two freely moving cameras and establish the first benchmark for this setting. Project page: this https URL .

---


### 181. [MSR-ABC: Complementary Feature Fusion for Clear Cell Renal Cell Carcinoma Classification](https://arxiv.org/abs/2611.09583)

**<font color=#1a73e8>作者：</font>** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clear cell renal cell carcinoma (ccRCC) classification from computed tomography (CT) may benefit from representations that capture different aspects of tumour phenotype. However, simply concatenating reconstruction-derived features, image--text embeddings, and radiomic descriptors may not fully exploit their complementary information. We propose MSR-ABC, a global--local framework integrating MedVAE, MedSigLIP, and radiomics. Spatially matched local image descriptors interact through cross-representation attention, while radiomic auxiliary supervision encourages the pooled local representation to retain quantitative tumour attributes. A gated residual mechanism integrates local information with global summaries. Area-aware pooling and visual and soft-text prompting complete the framework. We evaluate discrimination using a patient-level split of 396 KiTS23 cases and an external cohort of 111 TCGA/TCIA cases, reporting mean AUROC over three training seeds with 95% patient-bootstrap confidence intervals. MSR-ABC achieves mean AUROCs of 0.806 internally and 0.879 externally. Internally, it exceeds global MedVAE--radiomics and three-source concatenation by 3.35 and 3.61 AUROC percentage points, respectively. Removing any source lowers mean AUROC in both cohorts, with the largest decreases following radiomics removal. Individual removal of cross-representation attention, auxiliary supervision, or gated fusion also lowers internal mean AUROC. These findings are consistent with complementary contributions within the integrated architecture and support further investigation of structured representation fusion for non-invasive renal tumour characterisation.

---


### 182. [Coordinatewise Epsilon for Adam under Heavy-Tailed Noise](https://arxiv.org/abs/2611.09596)

**<font color=#1a73e8>作者：</font>** Jeonseong Kim, Chenglin Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam estimates second moments coordinatewise, but typically adds the same scalar $\varepsilon$ to every denominator. We study how this shared $\varepsilon$ affects convergence when noise and curvature vary across coordinates. Under coordinatewise finite-$p$ noise moments, $p\in(1,2]$, choosing $\varepsilon_i$ from the noise and curvature bounds for each coordinate attains the heavy-tailed $\ell_1$-stationarity benchmark $O(T^{-\frac{p-1}{3p-2}})$, matching the known optimal time exponent for smooth nonconvex stochastic optimization. For $1<p<2$, Adam with a shared $\varepsilon_t$ admits a lower bound of order $\Omega(T^{-\frac{p-1}{2p}})$. This lower bound holds for every predictable scalar choice of $\eta_t$, $\beta_{1,t}$, $\beta_{2,t}$, and $\varepsilon_t$, precluding a dimension-uniform benchmark rate for this class.

---


### 183. [Dual-Region Slice Aggregation for CT-Based Renal Tumor Classification](https://arxiv.org/abs/2611.09599)

**<font color=#1a73e8>作者：</font>** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clear cell renal cell carcinoma (ccRCC) is the most common kidney cancer in adults. We present a region-aware architecture for CT-based ccRCC classification. Tumor and 0--10 mm peritumoral context are pooled separately from shared frozen DINOv3 feature maps. A shared position-aware slice aggregator precedes fixed training-only principal component analysis (PCA). The resulting representations are fused with radiomics using two scalar feature gates. Evaluation on KiTS23 and 111 external cases yields internal test and external AUCs of 0.8078\pm0.0154 and 0.9094\pm0.0015. Compared with matched single-tumor readout, mean AUC increases by 1.50 and 2.34 percentage points, respectively. Early-PCA and reconstruction controls yield lower internal mean AUCs, while external AUC is similar for early and late PCA. These findings highlight the joint role of regional readout and slice aggregation in adapting frozen visual features to renal CT.

---


### 184. [CRTrack-Cap: A New Benchmark for Cross-View Dense Video Object Captioning](https://arxiv.org/abs/2611.09617)

**<font color=#1a73e8>作者：</font>** Xiangqun Zhang, Likai Wang, Zekun Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense video object captioning (DVOC) localizes, tracks, and describes object trajectories within a video. Existing methods process each camera view independently, producing separate camera-local tracklets and captions for the same person across cameras. These outputs lack a unified description and leave complementary appearance evidence across views unused. We therefore formulate cross-view DVOC (CVDVOC), which associates these tracklets into scene-level global trajectories and generates one caption for each trajectory from synchronized views. To support this task, we construct CRTrack-Cap from CRTrack by auditing text-identity links and converting usable referring expressions into canonical captions. It retains 425 global trajectories and 838 local tracklets across 13 scenes, with canonical captions for 335 identities. We adapt CHOTA to the cross-view setting as CV-CHOTA to jointly evaluate tracking and caption quality. Our reference framework combines View-Exclusive Cross-Camera Association (VECA) for grouping tracklets with Conflict-Evidence Gating (CEG) for integrating caption evidence using its reliability and disagreement across views. Against three single-view methods adapted with MvMHAT for cross-view association, our framework achieves CV-CHOTA scores of 83.43 and 33.48 on the scene-disjoint in-domain and cross-domain tests, respectively. Together, CRTrack-Cap and our framework provide a benchmark and a strong baseline for describing the same person consistently across camera views.

---


### 185. [BiLoGo: Reducing the smoothing of localised responses in Transformer-based neural operators for sheet forming](https://arxiv.org/abs/2611.09621)

**<font color=#1a73e8>作者：</font>** Yingxue Zhao, Haoran Li, Haosu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trial-and-error FE simulation of sheet forming could be computationally expensive, neural-network-based learned simulators are used to accelerate design. These simulators should accurately capture localised responses, such as thinning around sharp radii or near ribs, which determine formability. Transformer-based neural operators propagate information efficiently across the mesh but tend to smooth such localised responses. This study develops BiLoGo, a Bipartite Local-Global learned simulator with an FE-guided design that connects local node-element message passing with a Transformer-based neural operator for long-range information exchange. BiLoGo has three modules: a bidirectional node-element GraphSAGE model that learns nodal-elemental coupling on a bipartite graph and predicts each quantity on its native FE entity without interpolation; a dual-stream Transformer-based neural operator that processes blank deformation and tool contact with separate token sets, preventing localised contact information from being averaged with the whole-blank state; and a fusion and element update module that combines global and local features via gated residual fusion and updates element features conditioned on element-node kinematics. Evaluated on a dome-shaped cold forming case and two corner-shaped hot stamping cases (one with ribs), BiLoGo achieves the lowest positional and threshold-based thinning errors on all three cases compared with single-level and hierarchical graph-based models and Transformer-based neural operators. Near the ribs, the smoothing index of predicted thinning increases from 0.41-0.56 for Transformer-based neural operators to 0.94 for BiLoGo-U. Compared with the hierarchical graph network CAtt-BiUGNN, BiLoGo-T reduces mean positional error by 15.5% on the Corner case and BiLoGo-U by 8.3% on the Corner+Rib case, with 66-69% less training memory.

---


### 186. [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning](https://arxiv.org/abs/2611.09625)

**<font color=#1a73e8>作者：</font>** Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-Based Reinforcement Learning (TT-MBRL), using gradient descent at test time to encode the memory of episode observations into world model parameters. This enables the agent to learn a distinct world model for each episode, improving memory capabilities compared to traditional approaches that solely rely on contextual memory. We first establish a proof of concept on a simplified two-dimensional variant of the Memory Maze environment, which we refer to as Memory Maze 2D, showing consistent improvements across different world model architectures. We then demonstrate the effectiveness of TT-MBRL in the 3D domain, achieving new state-of-the-art results on the Memory Maze benchmark. Finally, we show that TT-MBRL maintains strong performance on non-memory benchmarks such as DeepMind Control and Atari 100k.

---


### 187. [A Separation Principle for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.09644)

**<font color=#1a73e8>作者：</font>** Lucia Pezzetti, Nicolas Lanzetti, Antonio Terpin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study cooperative multi-agent reinforcement learning (MARL) problems in which agents evolve under decoupled noisy dynamics but share a population objective. A canonical example is a mobility operator that orchestrates a fleet of vehicles to meet customer demand. The stochastic and time-varying nature of these problems calls for learning approaches, yet existing MARL algorithms do not scale: learning assignment and routing jointly over the full state-action space becomes prohibitive as the number of agents grows. Formulating the problem over the space of probability measures, we prove a separation principle: the population cost-to-go function is upper bounded by an optimal transport problem whose transportation cost is the target-conditioned single-agent cost-to-go function. This simplifies the multi-agent problem to learning a single-agent policy and coordinating the agents via optimal transport. Building on this principle, we introduce SALT (Separation-based Assignment and Learning via optimal Transport), a family of algorithms that learn a target-conditioned single-agent policy using any standard reinforcement learning algorithm, and then coordinate the agents via optimal transport. Since learning occurs at the single-agent level, SALT scales to fleet sizes where MARL baselines become intractable and transfers without retraining to fleet sizes unseen during training. In a vehicle-delivery experiment on the southern Manhattan road network, where MARL baselines are computationally prohibitive, SALT improves travel time by 15-21% over a shortest-path routing heuristic. In stochastic grid worlds, SALT reduces average travel times by 23-61% relative to MARL baselines and scales to population sizes where these methods fail.

---


### 188. [Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers](https://arxiv.org/abs/2611.09652)

**<font color=#1a73e8>作者：</font>** Ritik K. Badiya, Siladittya Manna, Ashmit Sinha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has been increasingly adopted to fine-tune pretrained models with low computational cost and is therefore also preferred in the federated learning paradigm to reduce computational and communication overhead. In this work, we investigate the sparsely explored problem of the risk of private data leakage in LoRA-adapted Vision Transformers (ViTs), where low-rank updates weaken the gradient signal available to a server with access to individual client updates. We show that quality of reconstruction is limited by two coupled ambiguities: reduced information in LoRA gradients and missing spatial cues from frozen positional embeddings. To address this, we propose a spatially anchored generative inversion framework that incorporates server-prescribed trainable positional embeddings into ViT blocks during fine-tuning at clients. The resulting positional gradients act as layer-wise spatial anchors, providing additional positional cues, while the generative prior keeps reconstructions on a realistic image manifold, reducing duplicate-data and patch-permutation artifacts, {which produce similar gradients as those produced when the target client images are used}. Adding our proposed spatial anchoring to GIAS improves PSNR by 10.14 dB, SSIM by 0.45, and LPIPS by 0.098 on CIFAR-10, as well as PSNR gains of 7.83 and 11.74 dB on high-resolution CelebA and CARS datasets, respectively, in the FedSGD setting. Such gains in reconstructed image quality metrics are also maintained at higher batch sizes and in FedAvg settings. These results indicate that LoRA-based PEFT does not, by itself, prevent data leakage in FL, and carefully incorporated positional embeddings can help in exposing private information.

---


### 189. [Video2Asset: Online Construction of Persistent 3D Street-Scene Assets](https://arxiv.org/abs/2611.09661)

**<font color=#1a73e8>作者：</font>** Zihan Zheng, Chunlei Cai, Zhenlong Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online 3D street-scene asset construction turns multi-view video into a continually updated scene of independently editable objects. The central challenge is to accumulate partial, intermittent observations under motion and occlusion without fragmenting identities or mixing evidence across objects. To address this challenge, we propose Video2Asset, an online framework for constructing persistent 3D assets from multi-view video. Using occupancy as an intermediate representation, we construct identity-aware observations with Historical Carrier Guidance for instance decoding and an identity encoder fusing instance-aligned 3D features with multi-view appearance. Accumulated-Evidence Association compares current observations with identity, geometric, and appearance evidence accumulated within asset records to determine identity inheritance and update world-coordinate states. We instantiate meshes from an asset library using these states and combine them with an occupancy-derived static background to support scene visualization, mesh replacement, object deletion, and trajectory editing. Experiments on several datasets demonstrate improvements in temporal identity consistency and asset quality across multiple occupancy models, including a 15.4% reduction in asset fragmentation on nuScenes with SGE.

---


### 190. [Dual Architecture Fusion Vehicle Lidar 3D Target Detection](https://arxiv.org/abs/2611.09664)

**<font color=#1a73e8>作者：</font>** Muyun Li, Weizheng Jin, Yuan Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, a 3D backbone network (SpconvTransformer) based on the fusion of convolutional architecture branch and Transformer architecture branch is proposed. The convolution branch uses 3D sparse convolution and submanifold convolution to learn local voxel features and semantic information, and the Transformer branch uses the self-attention mechanism to model the remote relationship between voxels, uses the broad receptive field to capture rich context information, and complementing the advantages of the two architectures by fusing the local features extracted from the two branches and the global features solves the problem of limited receptive fields of 3D convolutional neural networks. The experimental results show that the average accuracy of SpconvTransformer in 3D object detection and bird's-eye view detection tasks reaches 81.45% and 88.09%, respectively, and the average directional similarity reaches 91.10%, which is significantly better than other existing algorithms.

---


### 191. [Online Causal Configuration for Networked Systems via Doubly Robust Steady-State Learning](https://arxiv.org/abs/2611.09665)

**<font color=#1a73e8>作者：</font>** Yuli Liu, Zhiheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Measurement exploration reveals how interacting local controllers behave but can alter the steady-state regime a network operator seeks to optimize. Exploratory rewards may therefore fail to identify a configuration's no-exploration value: under full exploration, identical logged distributions can conceal different target values. Identification requires accounting for both action-law mismatch and shifts in the steady-state context distribution. We introduce CAUSAL-UCB, which selects configurations using optimistic bounds on target causal values. Its interference-aware clipped doubly robust evaluator produces predecision certificates separating statistical variation from calibrated identification, transport, and temporal-dependence errors. For any finite horizon and predetermined schedule of measurement-exploration rates $\{\eta_t\}$, we prove lower bounds of $\Omega((1+\sum_t\eta_t)^{-1/2})$ on minimax inference error and $\Omega(\sum_t\eta_t)$ on measurement-induced deployment loss in a stationary, potentially slow-mixing family. We bound regret under valid certificates and selected-information growth, and establish an anytime finite-sample certificate with a shared radius for estimation, selection, and reporting in a restricted known-local-interference model. In a high-mismatch benchmark with 24 paired seeds and 200 rounds, CAUSAL-UCB attains target regret of $1.732$ versus $6.326$ for certified IPS-UCB, with deployment gaps of $30.607$ and $23.217$, respectively. Independent-audit coverage tests and trace-driven semi-synthetic studies further assess certificate coverage and deployment trade-offs.

---


### 192. [The Multiscale Single-Index Model: An MSE Analysis of Online SGD Dynamics](https://arxiv.org/abs/2611.09682)

**<font color=#1a73e8>作者：</font>** Gordon Dai, Joan Bruna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the Multiscale Single-Index Model (MSIM), first introduced by Oymak and Soltanolkotabi (2021), as a stylized model for hierarchical feature learning with scale separation. Each layer extracts a shared single-index feature at one physical scale and passes it to the next, giving a tractable setting in which to study how deep architectures learn local multiscale representations. Under non-degeneracy and delocalization assumptions on the link function and planted features respectively, for the two hidden-layer case ($K=2$), we analyze joint online spherical SGD under MSE loss, which is a canonical regression objective, in discrete time and show that it achieves weak recovery from random initialization in $O(d\log^2 d)$ samples, followed by strong recovery to accuracy $\varepsilon$ in $O(d\log(1/\varepsilon))$ additional samples. The main technical challenge arises from the non-Gaussian learned features observed by the second layer. We address this challenge through a quantitative Gaussian comparison using delocalization, combined with sharp trajectory-level control of the coupled SGD dynamics. This work is a companion to Bruna (2026, arXiv:2607.03347), which studies recovery under a correlation objective for general $K$.

---


### 193. [Empirical Study of Post-Quantum Cryptography Adoption Status in SSH Infrastructure](https://arxiv.org/abs/2611.09703)

**<font color=#1a73e8>作者：</font>** Md Ariful Haque, Sander Vinberg, Ben Edwards 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the anticipated arrival of Q-day, quantum computers threaten current cryptographic schemes for encryption and digital signatures. In response, major content delivery networks and cloud service providers are already adopting Post-Quantum Cryptography (PQC). The current state-of-the-art focuses on benchmarking the operational performance of implementing PQC, but the real-world adoption status remains under-researched. This work utilizes large-scale SSH fingerprint data from a proprietary scanning tool to analyze PQC adoption across 1.52 million hosts and 27,012 entities. Our study shows that the PQC transition in the SSH protocol is underway but highly polarized: 45.2% of SSH hosts on port 22 support PQC, while 54.8% remain classical-only. At the entity level, 39.9% have enabled PQC on at least one host, whereas 60.1% have no PQC support. By correlating PQC adoption with industry, geography, and organizational size (digital and financial), this study provides a comprehensive empirical assessment of PQC adoption status in SSH infrastructure.

---


### 194. [Empirical Assessment of Post-Quantum Cryptography Adoption Status in TLS](https://arxiv.org/abs/2611.09707)

**<font color=#1a73e8>作者：</font>** Md Ariful Haque, Sander Vinberg, Ben Edwards 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anticipating Q-day security concerns, major CDNs and cloud providers are migrating to post-quantum cryptography (PQC). While existing literature benchmarks PQC performance, empirical research evaluating real-world adoption data remains scarce. We present an empirical assessment of PQC deployment across seven critical protocols (HTTPS, LDAPS, SMTPS, IMAP-SSL, POP3-SSL, TELNETS, and RDP) using 10,000 target IP addresses per protocol. At the origin-server level, PQC algorithm support reaches 9.1% for HTTPS and 7.39% for LDAPS, while falling below 1% for all other evaluated protocols. At the entity level, PQC support is 11% for HTTPS and 5.4% for LDAPS, while the remaining protocols have less than 5% of entities supporting PQC on the hosted servers. We further correlate these adoption trends against organizational digital and financial footprint, and industry sectors, yielding a multi-dimensional empirical assessment of PQC deployment. Finally, at the domain level, we perform a comparative analysis of PQC adoption in Cloudflare-hosted domains against baseline Cloudflare datasets. Collectively, our findings provide critical insights into the current state of PQC readiness over Transport Layer Security (TLS).

---


### 195. [ICare-DT: a digital twin for continuous forecasting of intensive care patients](https://arxiv.org/abs/2611.09712)

**<font color=#1a73e8>作者：</font>** Yanke Li, Yahang Qi, Yumi Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital twins of intensive care patients should update forecasts from new data and predict treatment responses, but few studies test whether routine records support either. We propose ICare-DT, a Transformer-based twin that updates a latent patient state hourly from new measurements without retraining. We trained it on 140,473 eICU-CRD stays to forecast vital signs crossing their training-set means. On test data, later forecasts beat the twin's own hour-6 forecasts of the same windows in all 12 settings (+0.073 to +0.153 AUROC). On validation data, controls that withheld or swapped the new hours traced the gain to the patient's own measurements. Without refitting, the model kept its gain on a second database (8 of 9 settings, +0.025 to +0.114 AUROC) in a prespecified evaluation of the previously analyzed MIMIC-IV test split. Refitted within MIMIC-IV, a twin state fine-tuned on clinical endpoints gave gradient boosting a significant gain for acute kidney injury (+0.0035 AUROC; hypotension +0.0010, not significant). To test response prediction, we built a benchmark that replaces the treatments in real records with simulated doses and injects responses of known size, visible only at measurement times. Ridge models supervised with injected effects recovered them from real records only through frequently measured variables (heart rate) read at their measurement times. We asked standard learners to predict these effects for a dosing regime no patient had received. No standard learner outperformed predicting zero effect at an out-of-support query. When told how the simulated responses were generated, a separate learner recovered the effects from the same records without seeing their true values (R2 0.30 to 0.40 at one effect size). Routine records support forecasts that improve with each patient's new data, and our benchmark is a testbed for models that learn how responses are generated.

---


### 196. [Direct Regression and Geometric Recovery for Event-based Spacecraft Pose Estimation](https://arxiv.org/abs/2611.09717)

**<font color=#1a73e8>作者：</font>** Pruthvi Nandan Janga, Kashyap Hegde Kota, Bharatesh Chakravarthi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras offer high temporal resolution and dynamic range for uncooperative spacecraft pose estimation, but models trained on synthetic event streams must generalize to the noise, background activity, and contrast variation of physical sensors. We present a comparative systems study of two independently developed approaches to synthetic-to-real, event-based 6-DoF spacecraft pose estimation. The first is a modular pipeline that combines learned keypoint detection and unlabeled target-domain adaptation with geometry-based pose recovery and temporal smoothing. The second directly regresses translation and rotation from global and cropped event representations using an apparent-scale cue, physics-motivated synthetic corruptions, and feature-consistency regularization. We evaluate both systems under the same SPARK 2026 hidden-test protocol on the real-event split of SPADES, with predictions for all test frames. The results reveal a component-wise reversal concealed by the aggregate challenge score: direct regression reduces orientation error by 22.7% (1.1767 to 0.9101 rad) and obtains a 13.4% lower composite score, whereas the modular pipeline reduces relative translation error by 78.7% (0.1335 to 0.0285). Archived configurations and a qualitative failure case identify plausible explanations for these complementary error profiles, without isolating their causes. These findings motivate a testable hybrid design that combines direct orientation estimation with geometry-constrained translation recovery.

---


### 197. [Fixed-point acceleration on Neural Wasserstein manifolds](https://arxiv.org/abs/2611.09723)

**<font color=#1a73e8>作者：</font>** Vitalii Aksenov, Sebastian Gutierrez Hernandez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a fixed-point acceleration method for optimization over probability measures, applicable to a variety of machine learning problems. We represent probability measures as pushforwards of a reference distribution through a neural network map and equip the parameter space with the induced pullback Wasserstein metric. This geometric structure allows natural gradient descent to be interpreted as a fixed-point iteration on a Riemannian manifold. We accelerate this iteration using Riemannian Anderson mixing method, which exploits historical residuals to capture approximate second-order information without forming Hessians. In the present parametric setting, the manifold is represented by Euclidean coordinates endowed with a point-dependent metric, simplifying retraction and vector transport. We evaluate the method on multimodal sampling, PDE-based inverse problems, aggregation dynamics, Bayesian logistic regression, and generative modeling. Across the tested tasks, Anderson mixing reduces the number of natural-gradient iterations and achieves competitive performance relative to SGD and Adam in terms of both loss-gradient evaluations and wall-clock time. These results suggest that fixed-point acceleration is an efficient tool for improving the computational efficiency of training on parametric Wasserstein methods.

---


### 198. [Evaluating Anterior Cruciate Ligament Risk of Injury Using a Graph Convolutional Autoencoder](https://arxiv.org/abs/2611.09724)

**<font color=#1a73e8>作者：</font>** Athanasios Babouras, Paul A. Martineau, Thomas Fevens  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current solutions for assessing the risk of anterior cruciate ligament (ACL) injury typically rely on expensive motion-capture labs that require substantial resource investment or subjective evaluations of specific athletic stress tests by experts. The Drop Vertical Jump (DVJ) and the Single Leg Hop (SLH) are two examples of such tests typically used to track progress in ACL rehabilitation. In this paper, we develop an unsupervised learning model that runs entirely on a smartphone for two tasks, based on an autoencoder architecture with multiple layers of graph convolutional networks, which utilizes pose estimation data to determine a person's injury risk status. Our model accurately predicts athletes at high risk of injury for both athletic stress tests, with average sensitivities and specificities of 78% and 78% for the DVJ, and 75% and 74% for the SLH. Our findings support the development of a widely accessible smartphone solution for real-time screening of ACL injury risk.

---


### 199. [TriNetra: Thermal-Reliability-Guided RGB-Thermal Fusion and Tracking for Surveillance](https://arxiv.org/abs/2611.09725)

**<font color=#1a73e8>作者：</font>** Sadique Khatib, Aditya Ahirrao, Vedant Sonawane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible cameras fail at night and thermal sensors fail under saturation, blur or loss of contrast, yet most RGB-thermal (RGB-T) detectors mix the two streams with fixed weights and cannot tell when one modality has become unreliable. TriNetra is a reliability-aware surveillance framework built around this problem. The proposed solution computes a frame-level Thermal Reliability Coefficient (TRC) from five label-free image cues, uses it to gate the thermal features of a dual-branch YOLOv8m detector whose visible branch, neck and head are frozen and COCO-pretrained, and passes the same score to a ByteTrack-based tracker that feeds a rule-based behaviour analyser. On the M3FD benchmark (2,940/630/630 split) the detector reaches 87.6% precision, 79.4% recall, 70.0% mAP@50 and 47.8% mAP@50:95 on the test split, with 17.0 M of its 42.9 M parameters trained. TRC stays near 0.78 on clean frames (standard deviation 0.012), decreases with the severity of thermal saturation and blur, reaching 0.53 and 0.69 at full severity, and is insensitive to RGB-thermal misalignment. With identical weights, the adaptive gate matches a fixed gate on clean data (70.0% versus 69.8% mAP@50) but keeps 43.6% mAP@50 when the thermal stream is corrupted, against 38.4%, 29.2% and 25.0% for a fixed gate, full thermal admission and a closed gate; the 5.1-point gain over the fixed gate has a 95% bootstrap confidence interval of +3.6 to +6.5 points. In tracking, the TRC-gated association performs on par with ByteTrack on a synthetic benchmark with exact ground truth and on 14 M3FD clips, and is slightly less stable under thermal saturation, so its measured benefit is confined to the detector. The limitations of the current evaluation are reported together with the results.

---


### 200. [What to Delegate, What to Preserve: Human Preferences for Agentic AI Across Everyday Life and Work](https://arxiv.org/abs/2611.09730)

**<font color=#1a73e8>作者：</font>** Sarah Wheeler, Veronica Rammouz, Yaoyao Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can execute multi-step tasks on users' behalf, yet the boundaries of acceptable delegation remain unclear. We report a scenario-based survey of 289 U.S. adults with prior AI experience covering 45 use cases across nine life domains. Each respondent evaluated one scenario per domain, producing repeated measures of automation preference, trust, collaboration, AI leadership, privacy concern, and willingness to pay. Automation preferences varied substantially across domains. Generalized estimating equation models showed that greater trust in the AI agent, desired AI leadership, prior task-specific AI use, and anticipated financial savings were associated with greater automation preference. In contrast, concerns that automation would reduce personal fulfillment predicted lower automation preference. Open-ended responses further revealed a preference for bounded autonomy, with participants often favoring substantial AI execution while retaining human involvement, oversight, or final authority. We argue that delegation is best understood as a configuration of execution, collaboration, leadership, and authority.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
