# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-335](./part-07.md)

---

### 201. [Isotropic Yet Undecodable: The Sequential Content-Sufficiency Gap in Latent-Predictive Text Representations](https://arxiv.org/abs/2610.07906)

**<font color=#1a73e8>作者：</font>** K. P. Santoso, N. Z. Fadil, F. P. Harsanti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study sequential content sufficiency by investigating whether a representation retains the ordered target information available in its input. An information-theoretic decomposition separates input ambiguity, representation loss, and readout mismatch. We construct recoverable views where perfect agreement and joint isotropic Gaussianity coexist with zero target information, and establish limits imposed by deterministic canonical anchors. Token log-loss provides a one-sided information-loss bound; a fixed-penalty ridge analysis shows why rank alone cannot determine prediction risk. These results motivate CANOPE, a nonautoregressive framework with ordered latent canvases, canonical-token supervision, and geometric regularization. On 40,000 validation sequences, latent-agreement (PL0) and token-grounded (PL2) have nearly identical pooled ranks but reach 13.5% and 98.8% positional Recall@1, respectively, under strong natural corruption when the correct target length is provided. On 3,930 LJSpeech validation utterances, frozen PL2 with a trained MatchaTTS readout yields 21.54% word error rate (WER) on corrupted text, versus 99.22% for frozen PL0, while end-to-end MatchaTTS reaches 10.93%. These results show that geometric regularity alone does not guarantee recoverable sequential content or effective downstream access in the text settings studied here.

---


### 202. [Revisiting Temporal Regularization for Smooth Control in Deep Reinforcement Learning](https://arxiv.org/abs/2610.07910)

**<font color=#1a73e8>作者：</font>** SungJae Ahn, Jeong Woon Lee, Kyoleen Kwak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Reinforcement Learning policies can produce nonsmooth action oscillations that hinder deployment on physical robots. Existing architectural and penalty-based approaches seek spatial smoothness by directly reducing sensitivity to changes in state inputs, but their broad constraints can degrade task performance as stronger smoothing is pursued. Temporal regularization instead constrains action differences along observed transitions, but has been considered unable to provide the spatial smoothness needed under observation noise. We revisit this assumption by proving that the temporal penalty bounds the expected action differences between current states sharing a next state, revealing a spatial effect that empirically extends to spatial smoothness. Building on this finding, we propose Conditioning for Action using only Temporal Smoothness (CATS), which combines a temporal penalty with linear ramp-up. We highlight temporal regularization's ability to provide spatial smoothness while better preserving task performance than explicit spatial regularization. Through linear ramp-up, CATS allows the policy to learn rewarding behavior before progressively smoothing its actions, improving return preservation and both temporal and spatial smoothness. Experiments in both simulation and the real world show that CATS substantially reduces action oscillation without degrading task performance, with little computational overhead.

---


### 203. [Diverse Motion Customization via Control-based Dynamic Optimization](https://arxiv.org/abs/2610.07911)

**<font color=#1a73e8>作者：</font>** Youngyoon Choi, Kihyun Kim, Jeongwoo Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in video generation, motion customization remains challenging due to content leakage, where appearance attributes from the reference video unintentionally propagate into the generated output. We identify this issue as a consequence of the generative process collapsing toward the reference video, which arises from formulating the learning objective as a direct regression on the reference. To address this, we propose Control-based Motion Customization (CMC), a principled training framework that is structurally robust to content leakage. Our key idea is to steer generative dynamics toward desired motion while avoiding collapse toward the reference video, which we formalize using Stochastic Optimal Control (SOC). Under this formulation, customized videos acquire the target motion yet remain within the pre-trained model's prompt-conditional distribution, where appearance is determined by the text prompt rather than the reference video. Furthermore, to improve efficiency, we tailor the SOC formulation to motion customization by eliminating the need for an explicit reward and introducing a timestep-adaptive motion cost that focuses only on early generative stages, accelerating training by 2.5 times. Extensive experiments demonstrate that CMC effectively mitigates content leakage and achieves competitive motion fidelity while preserving the diversity of the base model across diverse scenarios.

---


### 204. [Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization](https://arxiv.org/abs/2610.07916)

**<font color=#1a73e8>作者：</font>** Xuekang Zhu, Kaiwen Feng, Ruifeng Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image Manipulation Localization (IML) is commonly formulated as a fully supervised learning task that estimates the optimal manipulation mask $y$ for a given image $x$. In this work, we first reveal the latent nature of artifacts and thus reinterpret IML as a latent-variable problem, $P(y|x)=\int P(y|z)\,P(z|x)\,dz$, where $z$ denotes the artifacts. Following this interpretation, we pinpoint the cause for the current IML models' insufficiency as their implicit artifacts modeling strategy, highlighting the necessity of modeling $z$ in an explicit manner. Without direct labels, feature disentanglement is the most appropriate solution for this explicit modeling. Accordingly, we propose a two-stage learning paradigm with the Pairwise Artifacts Learning (PAL) and Standard Localization (SL) phases to estimate $P(z|x)$ and $P(y|z)$ via edit relations. To support our edit-relation-based learning, we further curate EditGroup-45K, a source-anchored dataset organized into edit groups for pair construction. Extensive experiments show that our PAL paradigm yields consistent improvements across diverse IML architectures, and empirical analyses further verify that PAL does capture artifacts explicitly through feature disentanglement. Code and dataset are available at this https URL

---


### 205. [Dynamic Alignment and Calibration for Multimodal Learning](https://arxiv.org/abs/2610.07928)

**<font color=#1a73e8>作者：</font>** Jinghao Xu, Zhenhua Guo, Xiaofeng Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic multimodal learning aims to learn robust representations by adaptively modeling information discrepancies across modalities. However, existing methods still suffer from two limitations: (i) static cross-modal alignment strategies usually impose uniform constraints on all samples while overlooking sample-wise variations, potentially leading to unreasonable over-alignment; and (ii) confidence- or uncertainty-aware fusion methods often fail to adequately account for feature magnitude and confidence differences across modalities. For modality pairs with significant feature magnitude differences or small confidence gaps, it might be unreliable to strictly align fusion weights according to confidence. To address these issues, we propose an Alignment- and Calibration-driven Multimodal Learning framework (ACML). Specifically, ACML incorporates a dynamic cross-modal triplet alignment module, which enforces strong semantic consistency for high-confidence positive pairs while encouraging diverse representation learning between high- and low-confidence positive pairs according to their confidence gaps. Additionally, ACML introduces a difference-aware attention calibration strategy that adaptively adjusts attention regularization based on feature magnitude and confidence differences across modalities, thereby mitigating biases caused by unreasonable fusion constraints. Extensive experiments on multiple multimodal benchmark datasets demonstrate that ACML consistently achieves superior performance and robustness over recent state-of-the-art methods.

---


### 206. [Where does a rust speedup come from? Language and algorithm effects in sliding window threat scorer](https://arxiv.org/abs/2610.07931)

**<font color=#1a73e8>作者：</font>** Nikolaos D. Tantaroudas, Ilias Karachalios, Andrew J. McCracken  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rewriting a hot path from Python into Rust is a common way to speed up security analytics, and large speedups are routinely reported. A rewrite usually changes the language and the algorithm at once, so a single factor can credit the language with a gain that comes from a better algorithm. We study this on a sliding window threat scorer modelled on the traffic light calculator of the SentinelSphere platform. Five implementations, three in Python and two in Rust, produce bit identical scores, confirmed by a shared checksum, and we time them from 100 to one million events in a bounded and a burst regime. The language alone contributes between about 4 and 29 times. Replacing a per event rescan of the window by an incremental update contributes more than 11,000 times in the burst regime, so the end to end factor reaches about 195,000 times when the window keeps filling and levels off near 13,000 times when it does not. A power law fit to the timings reported for the original rewrite gives growth exponents of 1.85 for Python and 0.88 for Rust, the signature of an algorithmic difference. Performance claims for security tooling should therefore report the language and algorithm contributions separately.

---


### 207. [Leveraging a four-quadrant approach for evaluating Redpine Science](https://arxiv.org/abs/2610.07937)

**<font color=#1a73e8>作者：</font>** Filip Dorm, Leonora Vesterbacka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Redpine Science gives models and agents a single access point to a wide range of peer-reviewed literature, queried directly through the Model Context Protocol (MCP) and an API. This report evaluates Redpine Science on two levels: the relevance of the retrieved chunks, and a model's answer when it has access to Redpine Science compared to web search. Both public and expert-validated benchmarks are used. Public benchmarks are a widely accepted way to test model development and are comparable across labs, but risk saturation and memorization. To address this, we complement them with an expert-validated question set. In total, this report presents four evaluations. On ScholarQABench SciFact, the public answer-quality benchmark reported here, an agent with Redpine Science answers 94.4% of claims correctly against 87.6% with no retrieval. On the expert-validated question set, an agent with Redpine Science states 80.1% of the required claims against 70.2% for an agent restricted to web search. On the 668 queries of a public retrieval benchmark whose gold paper Redpine holds, stripped of any model reasoning, Redpine Science places the correct source paper in its top ten results for 83.1% of queries (Recall@10), against 79.3% for the benchmark's creator. A blinded expert relevance panel places Redpine Science's Precision@5 at 75.2% against 39.8% for the PubMed search tool. We release the expert-validated question set and instructions to reproduce every headline result above, at this https URL.

---


### 208. [Generalized Matheron Variational Implicit Processes](https://arxiv.org/abs/2610.07938)

**<font color=#1a73e8>作者：</font>** Luis A. Ortega, Andrés R. Masegosa, Thomas D. Nielsen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit-process priors specify distributions over functions through sample-forward mechanisms such as Bayesian neural networks and stochastic simulators, but their function-space densities are typically unavailable. We introduce Generalized Matheron Variational Implicit Processes (GMVIP), a pathwise variational family for posterior inference with such priors. For Gaussian-process priors, GMVIP recovers the standard inducing-variable variational GP construction; for general implicit priors, its empirical covariance construction preserves the prior mean and covariance in the population limit. GMVIP constructs posterior samples by drawing a function from the prior and applying a correction anchored at a set of inducing inputs. The effect of this correction away from the inducing inputs is determined directly from prior samples, allowing the posterior to retain the structure and variability of the original implicit process. The (surrogate) prior and variational posterior use the same pathwise construction and differ only in the distribution of whitened inducing coefficients, yielding a tractable coefficient-space Kullback-Leibler divergence. Experiments on regression, classification, and forecasting with simulator-defined and retrieval-conditioned empirical trajectory priors show that GMVIP is broadly competitive with existing methods.

---


### 209. [Revisiting Numerical Forecasting Models for Language-Based Trajectory Prediction](https://arxiv.org/abs/2610.07954)

**<font color=#1a73e8>作者：</font>** JunGyu Lee, Inhwan Bae, Hae-Gon Jeon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-based trajectory predictors represent coordinates as discrete tokens and learn auxiliary tasks such as destination and group reasoning. This formulation enables the model to capture behavioral intent and social context beyond coordinate dynamics alone. However, token-level objectives provide only indirect guidance for continuous coordinate-space dynamics. To address this limitation, we introduce MoRE (Mixture of Reward Experts), a refinement framework that transfers numerical forecasting priors into a pretrained language-based predictor through reinforcement learning. Five frozen numerical predictors provide complementary coordinate-level knowledge of motion and interactions. Their predictions are converted into expert rewards and combined through an uncertainty-weighted consensus that penalizes disagreement. A ground-truth reward anchors the prediction to the target trajectory. To focus refinement on difficult cases, MoRE refines the policy using the top 1% of training samples ranked by predictive entropy. Expert predictions are computed once and cached before PPO training, so the experts are not run during policy updates or inference. In this way, MoRE combines the contextual modeling of the language-based predictor with coordinate-level feedback from numerical experts. On ETH-UCY, MoRE reduces ADE from 0.22 to 0.20 m and FDE from 0.32 to 0.29 m. Relative to the base policy, ADE decreases by 17.9% on SDD and 12.7% on NBA. On ETH-UCY, MoRE also reduces collision rates and better matches ground-truth pedestrian spacing, without increasing measured inference memory or latency. The project page is available at this https URL.

---


### 210. [DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given](https://arxiv.org/abs/2610.07958)

**<font color=#1a73e8>作者：</font>** Minhyeok Lee, Jungho Lee, Minseok Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) reconstructs a scene in a single forward pass, replacing per-scene optimization with a network trained across many scenes. Its quality, however, degrades sharply as the number of input images drops. The bottleneck is upstream of the reconstruction heads: from a few unposed views, the internal representation they read carries no evidence for unobserved regions, leaving holes, floaters, and blur. The common remedy supplies that evidence as pixels, synthesizing extra views with an image or video generator and re-encoding them, which is costly and not 3D-consistent by construction. We instead densify the evidence itself. We present DensiTok, a plug-in module for pretrained feed-forward 3DGS models that densifies their internal geometry tokens directly, making a frozen backbone behave as though it had observed many more views than it was given. DensiTok compresses those tokens into a compact latent space, completes the latents of the unobserved viewpoints in a single flow-matching step conditioned on camera geometry, and decodes them back into tokens that the original reconstruction heads. The same module design can be integrated into different pretrained predictors while keeping each backbone and its reconstruction heads frozen. Completion in a low-dimensional latent space requires no image synthesis or additional encoder passes. Across three pretrained backbones and two benchmarks, DensiTok consistently improves sparse-view reconstruction and recovers much of the gap to dense-view reconstruction.

---


### 211. [EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation](https://arxiv.org/abs/2610.07969)

**<font color=#1a73e8>作者：</font>** Yikai Qin, Yifei Deng, Mingjian Liang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce EmbodiedSmith, a framework for scalable embodied data generation through recursive self-improvement (RSI). EmbodiedSmith unifies asset, scene, and task generation in a pipeline that supports autonomous creation and language-driven customization. Its core is an agentic refinement loop: scene generation anticipates downstream task requirements, while task generation guides targeted scene edits, allowing scenes and tasks to iteratively improve one another. This joint refinement improves task generation success, including for long-horizon tasks. The framework further supports mobile manipulators, humanoids, and dexterous hands, as well as interactions involving deformable objects and fluids, broadening the range of behaviors and physical phenomena represented in generated data. Together, these capabilities provide a flexible simulation engine for both robot pretraining and evaluation. Extensive experiments validate the quality, diversity, and generation efficiency of the resulting data, while downstream policy experiments demonstrate that increased data diversity improves generalization.

---


### 212. [Can Agents Work for Everyone? Cross-User Reliability for Mobile GUI Agents in Personalized User Interfaces](https://arxiv.org/abs/2610.07972)

**<font color=#1a73e8>作者：</font>** Yeji Park, Jaeyun Shim, Taesik Gong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents increasingly operate on interfaces influenced by users' histories and preferences, but their reliability across different users remains underexplored. We introduce PAIR (Personalized Application-state Instantiation and Rendering), a pipeline for constructing user-conditioned application states that enables controlled evaluation of the same task across different users. We further introduce RePAIR (Reinforcement learning with Personalization-Aware Interaction Rewards), a training approach that learns from cross-user differences in subgoal outcomes to improve reliability across user-conditioned mobile environments. Across six agents, we find substantial variation in task success across users and consistently lower subgoal achievement in user-conditioned UI contexts (6.98 to 15.4 pp). This gap further increases for personal targets drawn from each user's own content (8.77 to 22.0 pp). Failures in these contexts frequently involve selecting another item instead of the intended target, particularly before target exposure. Finally, RePAIR improves user-conditioned SAR (+5.87 pp), all-success (+7.50 pp), and overall Task SR (+9.42 pp) over its supervised fine-tuning parent on unseen users, providing initial evidence that explicitly learning from cross-user variation can improve GUI-agent reliability.

---


### 213. [Learning a Ranking from Human Feedback in Log-Concave Random Utility Models](https://arxiv.org/abs/2610.07973)

**<font color=#1a73e8>作者：</font>** Diego Alovisetti, Marco Mussi, Alberto Maria Metelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of recovering the ranking of a fixed set of items according to their unknown numerical utilities. At each interaction with the environment, a learner presents the item set to a human and receives comparative feedback of two types. Under full-ranking feedback, each interaction reveals a noisy ranking of all items, whereas under winner-only feedback, it reveals only the item ranked first. In both settings, we model human feedback using a random utility model with log-concave noise and study the number of observations needed to recover an $\epsilon$-accurate ranking with high probability. This novel criterion tolerates ordering errors only between items whose utilities differ by less than $\epsilon$. For both feedback types, we establish worst-case sample-complexity lower bounds and develop algorithms that match these bounds up to logarithmic factors. Neither algorithm requires knowledge of the noise distribution, while only requiring an upper bound on its variance. Our results show that the ranking problem under winner-only feedback is intrinsically harder by exposing the sample complexity dependence on the minimum winning probability across the item set.

---


### 214. [Quantifying the Privacy Posture of Operator-Side 5G/O-RAN Profiles](https://arxiv.org/abs/2610.07976)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Apostolos Valiakos, Alexios Lekidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Operator-side network profiles derived from 5G/ORAN traffic carry personal data such as ephemeral subscriber identifiers, slice-level KPIs, and control-plane signalling, and must be anonymised before release to a federated-learning aggregator, threat-intelligence exchange, or ML training pipeline. We study how much re-identification risk remains after standard operator-side anonymisation. We quantify privacy posture with k-anonymity, l-diversity and t-closeness, aggregate them into a composite Privacy-Posture Index (PPI), and measure residual re-identification across eight transformation configurations on internal PCAP captures and the public Idaho Labs 5GAD corpus, under a full-QI syntactic bound and two simulated adversaries. The evaluation is modest in scale, and we read its trends as indicative rather than definitive. Three findings emerge. Pseudonymisation alone leaves re-identification unchanged; material privacy gains arise when quasi-identifiers are coarsened through generalisation, optionally combined with suppression. A downstream classification task then shows that suppression-heavy releases retain majority-class utility but sacrifice much of their minority-class recall, a cost the aggregate metrics hide. Finally, the standard kmin-based PPI correlates only modestly with the disclosure bound and not at all with the partial-knowledge attack, whereas a mean-class-size variant PPI correlates strongly with all three disclosure/attack measures; we therefore read PPI as a regulator-facing summary, not a security bound. The profiles are produced by passive operator-side monitoring with rule-based DPI; our contribution is the privacy-quantification layer that computes these metrics, applies the transformation policy, and exposes both through an inspectable dashboard.

---


### 215. [Learning from Revision Consequences: Hindsight Meta-Experience Distillation for Self-Improving Agents](https://arxiv.org/abs/2610.07979)

**<font color=#1a73e8>作者：</font>** Qianhan Feng, Zhongzhen Huang, Yakun Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents continuously improve by generating and revising Skills, the process that discovers and refines those Skills becomes a learnable object in its own right. Task-Skills directly act on task execution, whereas Meta-Skills govern how agents discover and improve future Skills; their value therefore emerges through the subsequent search processes they induce. Existing approaches improve Meta-Skills from observed raw Skill-search trajectories and branch outcomes. However, branch performance entangles the effects of the initial discovery state and the Meta-Skill revision that generated the search process, making it difficult to characterize what a particular revision actually changed, and pushing updates toward revisions that benefit from favorable states rather than those that improve the process. We introduce HMED (Hindsight Meta-Experience Distillation), a mechanism for constructing Meta-Experience for self-improving agents. HMED revisits the completed event from which a revision originates and re-executes the incumbent and revised Meta-Skills from the same restored discovery state, so that the changes associated with the revision can be observed under a shared condition. Each comparison is distilled into a Meta-Experience, a structured record that can be reused by future updates, so that even revisions that are not ultimately retained still contribute a learning signal. Across three interactive agent benchmarks and both open-source and closed-source models, HMED consistently improves Skill discovery performance over strong baselines, shifting Meta-Skill learning beyond branch outcomes toward the consequences of changing the improvement process.

---


### 216. [Do Higher-Order Models Win for Higher-Order Reasons? Rethinking Performance Gains in Hypergraph Learning](https://arxiv.org/abs/2610.07981)

**<font color=#1a73e8>作者：</font>** Fanchen Bu, Fan Li, Geon Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Higher-order models (e.g., hypergraph neural networks) often outperform lower-order baselines on hypergraph learning benchmarks, and their advantages are commonly attributed to their ability to exploit higher-order information. However, better performance alone does not establish this explanation. We therefore ask: Do higher-order models win for higher-order reasons? To investigate this question, we introduce a controlled performance-attribution framework that perturbs higher-order information while preserving the lower-order, i.e., pairwise, information. Across 25 commonly used hypergraph learning benchmarks spanning three tasks, we frequently observe an intriguing pattern: higher-order models originally outperform lower-order baselines, yet retain most of their advantage after perturbation. This suggests that much of the observed advantage remains achievable without the higher-order information. We then investigate potential lower-order explanations for these remaining gaps. We find that simple additions to a lower-order baseline, e.g., richer pairwise weighting, more steps of pairwise feature propagation, and normalization, reduce the remaining performance gaps, supporting lower-order explanations for part of the observed advantage. Our analysis calls for the hypergraph learning community to rethink performance attribution by distinguishing performance gains from their explanations, adopt stronger lower-order baselines, and use suitable benchmarks that better test the value of higher-order information.

---


### 217. [Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels](https://arxiv.org/abs/2610.07984)

**<font color=#1a73e8>作者：</font>** Youxing LI  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal assistants answer questions from long-term memories that contain images. After retrieval, each retrieved image reaches the answering model either as pixels, at about a thousand visual tokens per image, or as a stored text proxy that often misses the detail the question asks about. We find that the benefit of pixels usually comes from one or two retrieved memories, and that it can be predicted before the answering model runs, without reading any full-resolution image. In PixelTriage, a plug-in placed after retrieval, a small model that does not generate text reads the dialogue, a short note and a thumbnail of each retrieved memory and predicts how much its pixels would add. It is trained on synthetic memory episodes labeled by a frozen 27B model that answers each question with and without each memory's pixels. With a 7B answering model, PixelTriage lies on the accuracy--cost frontier of M$^3$Exam, DMV and MemEye and uses 11--23\% of the visual tokens without a significant loss of accuracy. On DMV it answers 2.9 times faster than opening all images. It outperforms retrieval order and uniform down-sizing at equal budgets and transfers to other memory systems and to a 397B answering model.

---


### 218. [A Broader Look at Model Merging: Rethinking Implicit Regularization Induced by Task Arithmetic](https://arxiv.org/abs/2610.07990)

**<font color=#1a73e8>作者：</font>** Sin-Han Yang, Shih-Cheng Huang, Chieh-Yen Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging aims to build a multi-task model cheaply by combining the weights of individual task-specific models. To perform well across multiple tasks, most existing merging methods use an additional dataset to find the coefficients for the best linear combination of task-specific weight updates. However, we identify an implicit regularization in this standard practice: searching over coefficients restricts the candidate models to a subspace spanned by task-specific weight updates. In this work, we investigate whether this regularization is actually useful. Surprisingly, empirical results show that optimizing merged-model weights without this regularization significantly boosts the performance of common merging methods across multiple architectures, domains, and even in an extremely data-limited scenario where only one instance is available per class. Moreover, directly optimizing the pretrained model weights even outperforms some existing merging methods. Analysis shows that better multi-task weights exist outside the subspace and can be found using multiple methods. We study different strategies for using the additional dataset, discussing their practical use and implications for model merging. Overall, this work calls for revisiting the existing model-merging pipeline, motivating a broader exploration of the weight space and a reconsideration of the implicit regularization induced by task arithmetic.

---


### 219. [Can phenotypic activity be predicted without experimental readouts?](https://arxiv.org/abs/2610.07997)

**<font color=#1a73e8>作者：</font>** Télio Cropsal, Rocío Mercado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular encoders contrastively pretrained on paired molecule-morphology data, such as CLOOME and CellCLIP, have been proposed as cheap surrogates for phenotypic prediction, avoiding the need to run a Cell Painting assay. We evaluate this idea for these molecular encoders under a protocol designed to control for two confounds that can inflate apparent performance: leakage across an encoder's own pretraining boundary, and the correlation between phenotypic activity and cytotoxicity. Testing six representations, including a non-pretrained MLP control matching CLOOME's input and layer count, on two distinct Cell Painting screens, we find that once these confounds are controlled for, the pretrained molecular encoders show no clear advantage over plain physicochemical descriptors, and that toxicity is generally easier to predict than phenotypic activity across representations. Our results suggest leakage-aware, confound-controlled evaluation should be standard practice before phenotype-pretrained encoders are trusted as surrogates for phenotypic drug discovery.

---


### 220. [Spectra: Exact Component Transport for Test-Time Prior Adaptation in Simulation-Based Inference](https://arxiv.org/abs/2610.08021)

**<font color=#1a73e8>作者：</font>** Xin Zhao, Nico Scherf, Robert Trampel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-based inference (SBI) has become a powerful approach to Bayesian inference in complex scientific models whose likelihoods are difficult or impossible to evaluate. Amortized SBI learns reusable inference models from simulated data, enabling rapid posterior inference for new observations, and modern generative models have made these models increasingly expressive. However, this reuse is limited to the prior distribution chosen during training, whereas scientific analyses often need revised priors as knowledge accumulates or alternative assumptions are tested. We introduce Spectra, a test-time adaptation method for diffusion-based SBI. Spectra uses an exact score-transport identity to obtain the adapted score from a frozen diffusion model in closed form for structured prior changes, without additional simulation or training. Across six SBI benchmarks, Spectra achieves accurate adaptation under strong prior shifts at low online sampling cost. This enables pretrained SBI models to incorporate updated prior information at test time.

---


### 221. [Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA](https://arxiv.org/abs/2610.08033)

**<font color=#1a73e8>作者：</font>** Jordy Kieto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look. We judge one from the outside. We learn a structured, multi-agent world model of a complete ten-hero MOBA (206 units, every hero acting every tick, games of up to 6,000 ticks), train a policy only inside it with 1,400-tick free-running imagined episodes, and measure that policy in the real game against the opponent the game ships with. The real game never provides a gradient; it provides the policy's own games as training data for the world model, and an online evaluation that selects and anchors the policy. Run as a continuous asynchronous Dyna loop, the policy wins 70.2% of real games as radiant (421 of 600; 95% CI 66.4-73.7) on seeds never used for any decision, up from 0% for dream training alone and 33.7% before the loop. It wins none as dire, and neither does the shipped opponent when it plays itself. Four findings explain the result. Model exploitation is invisible from inside the dream: every unanchored run collapsed within a few updates while no in-dream metric tracked the collapse. A world model that is accurate on its training corpus is badly wrong on the policy's own games, and Dyna repairs it there, which is worth +9.2 points of real win rate with the policy recipe held fixed. Finally, the policy inherits its world model's fidelity profile mechanic by mechanic: the model represents the macro game but not crowd control, cast timing or lethality, and the policy wins by map-wide pressure with almost no coordinated fighting. We release the world model, the dream-PPO harness, a world-model debugger, the evaluation protocol, and every policy and log.

---


### 222. [SepsisLens: Structure-Preserving Sequence Modelling for Decomposable Early Sepsis Warning](https://arxiv.org/abs/2610.08046)

**<font color=#1a73e8>作者：</font>** Yikun Ou, Wei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early sepsis warning from ICU records can be cast as a structure-preserving prediction problem. A model needs to detect deterioration from irregular measurements while keeping each alert connected to the physiological signals that support it. Many temporal models fuse clinical variables into a patient-level representation, supporting scalar risk prediction but weakening the structure needed for clinical decomposition. We present SepsisLens, which preserves variable-indexed temporal states until risk composition. Observation-aware representations encode each variable's dynamics and measurement history, while a shared temporal encoder models each trajectory without collapsing the variable axis. The StructuredRiskHead composes multi-horizon risk from explicit variable-level and organ-level components. We evaluate SepsisLens on three public ICU cohorts and one private-hospital cohort under a common pre-onset protocol. SepsisLens achieves strong discrimination on all four cohorts and lower alert burden at matched event recall on MIMIC-IV. Structural ablations support the design, while input-side masking shows that the ranked components reflect variables with greater influence on prediction.

---


### 223. [A Riemannian Geometry for Low-rank Adaptation](https://arxiv.org/abs/2610.08049)

**<font color=#1a73e8>作者：</font>** Shoichiro Takeda, Shin'ya Yamaguchi, Satoshi Suzuki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is widely used as a parameter-efficient fine-tuning technique for pre-trained deep neural networks, which approximates the weight update via full fine-tuning by a low-rank matrix $BA^\top$. This parameterization leads to the equivalence relation $(B, A) \sim (BG^{-1}, AG^\top)$ for any invertible matrix $G$ because $BA^\top = BG^{-1}(AG^\top)^\top$ and thus both pairs yield the same loss value. This relation induces a quotient manifold where matrices $(BG^{-1}, AG^\top)$ for all $G$ are identified, eliminating redundant directions along which the loss value remains unchanged. To respect the geometry of this manifold, the original search space is endowed with a Riemannian metric that is invariant under the equivalence relation. Such a metric induces preconditioning at each gradient step and ensures that each weight update via LoRA changes the loss value, leading to efficient optimization. In this paper, we propose a new Riemannian metric that is specifically tailored to LoRA to close the gap to full fine-tuning at the weight level. We theoretically show that LoRA with our preconditioning induced by this metric satisfies the following two properties at each iteration: (i) The weight update follows the direction closest to the gradient of full fine-tuning within the subspace of first-order weight changes allowed by the LoRA parameterization. (ii) The updated weight matrix is closer in Frobenius norm to that of full fine-tuning than the updated weight matrices of LoRA with conventional preconditioning and without preconditioning. These theoretical insights suggest that our preconditioning makes LoRA better approximate full fine-tuning, thereby leading to more efficient optimization. Experiments show the effectiveness and efficiency of our preconditioning for LoRA on fine-tuning tasks with language and vision domains.

---


### 224. [Systematically Optimized CNN-Transformer with Focal Loss for Imbalanced Intrusion Detection on NSL-KDD](https://arxiv.org/abs/2610.08066)

**<font color=#1a73e8>作者：</font>** Kartick Sutradhar, Ranjitha Venkatesh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion Detection Systems (IDS) struggle with imbalanced datasets like NSL-KDD, especially in detecting rare R2L and U2R attacks. This work describes a systematically optimized and explainable framework using a CNN-Transformer architecture to improve performance on highly imbalanced data. We decided to use XGBoost for feature selection and Focal Loss as the main mechanism for minority class learning. We used Optuna for end-to-end hyrate=0.00042, batch size=256, and Focal Loss {\gamma}), using a thoughtful data splitting process to prevent data leakage. Critically, our ablation studies pointed out that while Focal Loss (optimally at {\gamma} = 1.5) substantially enhanced minority recall, adding oversampling methods like SMOTE caused precision degradation via over-correction. Our final model, using only tuned Focal Loss, achieved 98.73% overall accuracy on the NSL-KDD test data, with significantly balanced F1-scores of 84.63% (R2L) and 69.66% (U2R) over baseline approaches. Additionally, we performed SHAP analysis to understand model predictions, understand salient features (e.g., service http, logged in), and explain the persistent U2R precision challenge due to feature overlap. This study presents a comprehensive pipeline for imbalanced IDS, providing methodological insights, and demonstrates that tuned Focal Loss can be a sufficient and effective strategy for class balancing.

---


### 225. [Frontstage Mediation Work: Invisible Work Bridging Gaps Between AI Decisions and User Expectations](https://arxiv.org/abs/2610.08067)

**<font color=#1a73e8>作者：</font>** Yongjae Sohn, Daehyun Kwak, Jiyeon Amy Seo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated service systems increasingly generate algorithmic operational decisions that shape how services are delivered. However, these decisions reach end-users only through frontline workers who carry them out in real-world settings. During this process, automated decisions can diverge from user expectations, surfacing as friction at the service encounter. We propose Frontstage Mediation Work as a preliminary analytic lens for examining the often invisible labor through which frontline workers anticipate and manage such misalignments between algorithmic decisions and user expectations. Drawing on a qualitative case study of an On-Demand Ride-Pooling service, we identify four recurring practices through which drivers sustain the service encounter when frictions arise. Such labor remains absorbed into routine operations, leaving no trace in performance metrics, system logs, or formal job descriptions. This paper contributes to worker-centered HCI scholarship by illustrating how automated services shift onto frontline workers the responsibility of managing the interactional consequences of system-level decisions.

---


### 226. [Detecting a Shift Is Not Enough: Exact Minimax Limits of Linear Representation Repair](https://arxiv.org/abs/2610.08069)

**<font color=#1a73e8>作者：</font>** Anuar Aimoldin, Yankai Chen, Ayana Mussabayeva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A mean shift between two data sources can be easy to detect but hard to remove without substantially changing their representations. We cast its removal as a statistical decision problem: from noisy differences between paired calibration measurements in $\mathbb{R}^d$, learn one linear map, applied to both sources under a hard distortion budget, that leaves as little of the shift as possible on fresh data. We derive the exact finite-sample minimax risk over all such maps, $(d-k) \mathbb{E}[1/(d+2J)]$ with $J\sim\mathrm{Pois}(\kappa/2)$, where the budget allows deleting $k$ directions and $\kappa$ is the calibration signal-to-noise ratio. Projecting out the mean calibration difference attains it without knowing $\kappa$ or the noise scale. This exposes a detection-repair gap: detecting the shift needs only $\kappa\gg\sqrt d$, whereas removing a fixed fraction of it at constant distortion needs $\kappa\asymp d$, as for estimating its direction. Standard linear concept erasers (MP, SAL, LEACE) remove the same calibration difference, so the formula gives, before fitting, exactly how much shift they leave on fresh data and how much calibration a target requires. The limit is robust: pairing keeps it exact for non-Gaussian shared content, the projection keeps its guarantee under anisotropic noise, and selective abstention cannot close the gap. On paired clinical and wearable sleep EEG, where differences between participants act as calibration noise, the formula predicts the device shift left in new participants, and more recordings per person soon stop helping. Together, these results tell whether a correction that falls short needs a better method, more recordings, or more participants.

---


### 227. [Optimization Encoders: Rethinking Second-Order Meta-Learning for Neural Fields](https://arxiv.org/abs/2610.08075)

**<font color=#1a73e8>作者：</font>** Rudolf L.M. van Herten, Soufiane Ben Haddou, Rachit Saluja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional neural fields represent signals continuously, but their effectiveness depends on how the conditional latent representations are inferred from observed data. In meta-learning, this encoding occurs through gradient updates induced by the decoder, tying representation learning directly to decoder design. We formalize this connection by interpreting latent optimization as an optimization encoder, unifying the roles of second-order differentiation, latent parameterization, and task supervision. This concept enables second-order meta-learning for end-to-end training of the encoding procedure alongside the decoder, and clarifies which learning pathway first-order approximations discard. Guided by this view, we introduce Attentive Latent Fields (MetaLF), an equivariant transformer-based neural field that contextualizes a latent pointcloud through self-attention. These interactions shape both field predictions and the updates that construct their representation, allowing local observations to inform coherent non-local structure. Disentangling the inner encoding objective from outer task supervision unifies reconstruction, classification, and segmentation within an end-to-end meta-learning framework, using reconstruction-only latent adaptation at test time. Controlled experiments on polynomial fields link latent coordination to lower effective rank and stronger alignment with the underlying function space. Across image and 3D shape reconstruction, MetaLF improves fidelity within three to five gradient updates, while supporting semantic prediction across images, shapes, and volumes. Together, these findings position the optimization encoder perspective as a unified basis for designing neural fields around how representations are constructed, coordinated, and used.

---


### 228. [Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight](https://arxiv.org/abs/2610.08077)

**<font color=#1a73e8>作者：</font>** Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can hindsight teach an agent what it could have anticipated before acting? We introduce prospective learning, which uses post-hoc experience to supervise foresight predictions from the pre-interaction view, and instantiate it with Self-Retrospection Distillation (SRD). Intuitively, a completed trajectory reveals knowledge that would have been useful and pitfalls that should be avoided; SRD distills this privileged hindsight into trajectory-blind foresight of the same policy. Foresight serves only as a training target and need not be explicitly generated at inference time. Across 10 tool-integrated reasoning and long-horizon agentic tasks, SRD complements RLVR and self-distillation baselines with gains of up to $24.2$ pp. Its advantage is especially pronounced when reward contrast is scarce: when $37$--$98\%$ of rollout groups are reward-uniform across model scales, yet SRD can still exploit learning signal from sampled trajectories. In the 2B setting, where $98\%$ of groups are all-failure, the RLVR training ends up at $0.0\%$ success, while adding SRD reaches $60.6\%$ under the same rollout budget. Our results suggest that post-hoc agent experience is useful not only for evaluating or improving behavior, but also for shaping predictive representations before available interaction.

---


### 229. [Multi-Dataset Diagnostic Utility of Clinical Visual Concepts in AI Systems for Dermatology](https://arxiv.org/abs/2610.08086)

**<font color=#1a73e8>作者：</font>** Linda Wermelinger, Simone Lionetti, Fabian Gröger 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The clinical integration of AI systems in digital dermatology relies heavily on human trust. Clinically interpretable visual concepts can act as intermediate representations enhancing trust and reliability. However, research in this domain is currently limited by scattered, heterogeneous dataset annotations. In this work, we introduce SkinLex, a harmonized dataset of 48 clinical morphological attributes across four public datasets (SkinCon, DermaCon-IN, MM-Skin, and PASSION) for a total of 20,411 records. Supervised nine-partition classification of skin conditions shows that limiting features to specific visual groups, like shapes or colors alone, reduces diagnostic accuracy. Bootstrapped backward elimination reveals that the set of 48 visual concepts has some degree of redundancy for algorithmic nine-partition diagnosis on the examined dataset. This demonstrates that coarse diagnosis on the selected dataset requires a relatively small but varied combination of clinical concepts, and motivates further research to improve concept taxonomy. Results can be translated into clinical benefits by reducing inputs for concept-based models, improving efficiency for annotation and modeling, and further enhancing interpretability. Code and prompt templates are available at this https URL.

---


### 230. [When Tools Lie: Reliability of Mathematical Agents Under Corrupted Tool Feedback](https://arxiv.org/abs/2610.08097)

**<font color=#1a73e8>作者：</font>** Kavienan Jegatheesan, Gayathri Lihinikaduarachchi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mathematical problem solving often requires deterministic computational steps that agents delegate to tools and implicitly trust. Yet tools can fail silently, returning plausible but incorrect results. How well can agents detect and correct corrupted tool call outputs? We study this through a controlled corruption framework where a hidden interceptor replaces tool call results with plausible incorrect information on targeted problems. We evaluate agents across 31 problems under four verification designs including no verification (baseline), mandatory same-context reflection, optional fresh-context verification, and optional structural verification. Without verification, corruption causes dramatic accuracy loss, from 100% down to 72.4%. Mandatory reflection fully recovers this performance to 100%. Optional verification improves accuracy only when models actively invoke it. Our results show that checking frequency is strongly associated with robustness differences, while unequal invocation prevents a controlled comparison of verifier quality. A supporting recovery experiment shows that full problem restart succeeds in 100% of cases after explicit detection. These findings demonstrate that verifier availability and verification policy are separate components of mathematical-agent reliability. Mandatory policies enforce verification while optional policies depend on the model's own choice to invoke it.

---


### 231. [Supermarket Product Detection and Recognition: Utilizing Deep Learning with Rectified Imagery](https://arxiv.org/abs/2610.08126)

**<font color=#1a73e8>作者：</font>** Mayank Sah, Jimson Mathew  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Product Identification has sprung up to become one of the most challenging problems in the automation of the retail industry. With the new industry 5.0 standards, automated inventory management, and catalog creation tasks are vitally important. Object identification models have emerged as a viable answer with their unprecedented identification and localization accuracy. However, the close-knit rack design of supermarkets generates the problem of angle variation in capturing images. The angle-variant densely packed images(a single image contains many objects) become overwhelming for these models alone. In this paper, we try to supplement object detection models with traditional Hough transform (HT) and homogeneous estimation concepts. We study the effect of rectified images using homography estimation and hough transform and their limitations on the problem of grocery identification. We make a case for creating a new dataset to test the effects of such rectification and produce analytical results on different scenarios of angle variation and object densities per image. Extensive experiments on different object detection models suggest that image rectification of angled images improves the detection accuracy of grocery products in images. The results also highlight the limitation of rectification on the angle of image capture and the object density of the image.

---


### 232. [Mu-DisCoCat: A Variational Pipeline for Compositional Generalization on Quantum Processors](https://arxiv.org/abs/2610.08131)

**<font color=#1a73e8>作者：</font>** Mina Abbaszadeh, Matilda Karabina Moore, Raem Haq 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving compositional concept generalization (CoCoGen), the ability to understand novel situations by recombining learned primitives, remains a fundamental challenge in artificial intelligence. Compositional semantic models such as Compositional Distributional Semantics (DisCoCat) offer solutions by generalising vectors to tensors, but suffer from scaling bottlenecks when learning the tensors. Mapping DisCoCat onto Variational Quantum Circuits (VQCs) resolves this limitation for text, yet the methodology has not been expanded to multimodal situations such as the ones involved in CoCoGen. This paper introduces Mu-DisCoCat: a multimodal variational quantum learning framework for DisCoCat that achieves CoCoGen. The framework first learns stable object representations from single-object image-text pairs, then fixes these and uses them to learn the relations between them in multi-object situations. In classical simulations, the model used Uhlmann state fidelity to compute the overlap between the multimodal circuit representations and achieved higher relational OOD accuracy than the evaluated CLIP baseline. Its deployment was evaluated using the destructive SWAP test across noisy quantum emulators, including a range of IBM fake backends, IQM FakeAphrodite, and the IBM Marrakesh quantum processor. Despite real-world device noise, the hardware-executed models maintained a strong positive correlation with simulated fidelities, reliably distinguishing unseen similar and dissimilar pairs. Our work establishes a framework for executing CoCoGen on VQCs, demonstrating a viable use case for near-term quantum hardware.

---


### 233. [Test-Time Agent Evolution for Long-Horizon Legal Reasoning](https://arxiv.org/abs/2610.08138)

**<font color=#1a73e8>作者：</font>** Haotian Chen, Shuaicheng Niu, Haocong Rao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal intelligence aims to support reliable decision-making across long-horizon legal processes involving evolving case states and multiple roles. However, real-world legal deployment exhibits substantial case heterogeneity in facts, evidence, and procedural contexts, exposing the limitations of static agent strategies. Moreover, legal reasoning is inherently interdependent across roles and procedural stages, making global reliability fundamentally different from isolated role competence. To address these challenges, we study training-free test-time agent adaptation, where agents continuously exploit deployment-time signals from preceding cases and ongoing interactions without updating model parameters. We propose \method, which introduces \emph{Test-Time Memory Evolution} to retrieve reusable experience from previous cases, adapt it to the current factual and procedural context, and consolidate accumulated experience for subsequent decision-making. Further, \emph{Rubric-Aligned Collaboration} verifies and revises role-specific actions according to behavioral and procedural requirements, enabling coordinated decision-making across roles and stages. Extensive experiments on J1-EVAL and LegalWorld across five backbone models demonstrate consistent improvements over representative reasoning and agent baselines with reasonable interaction and computational costs. Ablation and case studies further show that the two components provide complementary benefits in experience adaptation and cross-role coordination, improving the reliability and efficiency of long-horizon legal reasoning.

---


### 234. [Partially Observable Zero-shot coordination by Predicting Intention of Partner](https://arxiv.org/abs/2610.08142)

**<font color=#1a73e8>作者：</font>** Jinnyeong Yang, Yuhwan Jeong, Hoyong Kwon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-shot coordination in embodied settings requires acting while the partner is intermittently out of view, leaving existing methods with ambiguous partner representations and uncertainty over hidden partner states. We propose Predicting Intention of Partner (PIP) to jointly address these challenges. PIP uses a Joint-view VAE to distill richer training-time evidence from the union of both agents' local observations into a partner representation available from local observations alone. Partner-state Belief networks further infer the partner's hidden location and behavioral tendencies from the ego agent's interaction history. We evaluate PIP in Burrito-PO, Overcooked-PO, and a Melting Pot substrate, together with a human evaluation in Burrito-PO. PIP attains the highest mean performance among the compared methods across all three benchmarks. Human evaluation and diagnostic analyses further support coordination with unseen partners and the contributions of both components under partner occlusion.

---


### 235. [Making COMET Comparable Across Scripts: Diagnosis and Correction of Tokeniser-Induced Script Bias in Indic MT Evaluation](https://arxiv.org/abs/2610.08159)

**<font color=#1a73e8>作者：</font>** G. L. John Salvin, Swapnil Hingmire  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> COMET reports translation quality as a single number, and that number is routinely compared across target languages written in different scripts. Such a comparison assumes Script Invariance: the score should not depend on the writing system that carries the target. We test it on IndicMT Eval by re-encoding the target into Latin script, which changes orthographic form while holding content and human ratings fixed. Script identity then accounts for 22.9% of native-script COMET variance, and agreement with annotators falls in all five languages studied. We trace the effect to the tokeniser and measure it with three label-free diagnostics. The bias is two faults, not one. Scores from different scripts occupy incompatible ranges, and within a single script the metric orders translations less accurately. No order-preserving transform of the score can repair the second fault. The first is removed exactly by COMET-QN, which maps the score distribution of each (language, script) pair onto a shared reference. Pooled agreement with annotators rises from 0.300 to 0.399, which is what makes scores from different scripts safe to place on one axis, and every within-language ordering is provably preserved. A regressor over parity features recovers a further 17.1% of the lost sensitivity. The remainder belongs to the encoder, and no post-processing can reach it. We therefore recommend publishing the normalised score, the three diagnostics, and the identity of the tokeniser they were computed against, so that a reader can tell how much of a score reflects translation quality and how much reflects the writing system.

---


### 236. [Which alloy composition,what process parameters? Inferring the recipe from optimized metallic microstructure and texture](https://arxiv.org/abs/2610.08165)

**<font color=#1a73e8>作者：</font>** Mahish K. Guru, Jan Bohlen, Louam Lemjid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The mechanical properties of a metallic alloy are set by its microstructure and texture: the size and shape of its grains and the orientation of their crystals. That structure is in turn set by a recipe, the alloy composition together with the processing parameters. Alloy development runs this chain forwards, tuning the structure until a target property is met. Running it backwards, from an optimized structure to the recipe that would produce it, still relies on expert knowledge. We ask whether this backwards step can be learned. On an in-house dataset of 107 magnesium alloy extrusion conditions across 14 alloys, each with optical micrographs and an X-ray texture measurement, we compare three descriptors of microstructure and texture: conventional grain and texture statistics, a vision embedding from a pretrained image encoder, and a graph neural network on the grain network. Each is paired with prediction heads for two tasks: the alloy composition given the process (Task A), and the process parameters given the composition (Task B). Under 5-fold cross-validation, the conventional descriptors identify the correct alloy for 65% of held-out conditions, against 17% for always guessing the most common alloy, while the learned embeddings stay below 30%. The process parameters are recoverable but noisier: compared with using the composition alone, the microstructure roughly halves the temperature error. Because only a few alloys were cast and only a few press settings were used, both answers are discrete, and heads that pick from these known options, while respecting their order, worked better than heads that predict a free value.

---


### 237. [FBAN: A Fully Homomorphic Encryption Compatible Bottleneck Attention Network for Privacy-Preserving Behavioral Authentication](https://arxiv.org/abs/2610.08174)

**<font color=#1a73e8>作者：</font>** Jichao Xiong, Atsuko Miyaji, Jiageng Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continuous authentication (CA) strengthens session security by repeatedly verifying the user during device interaction, yet it inherently relies on highly sensitive behavioral traces (e.g., fine-grained touch dynamics) that are often outsourced to cloud/edge services for scalable inference. This raises a fundamental privacy-in-use challenge: protecting behavioral features during computation, not only in transit or at rest. Fully homomorphic encryption (FHE) offers a principled solution, but deploying modern CA models under FHE remains difficult due to non-linearities and attention-style operations that incur high ciphertext cost.
We propose FBAN, a TFHE-compatible Bottleneck Attention Network and an end-to-end encrypted CA framework. FBAN is designed for integer-only execution via a two-stage pipeline (floating-point pretraining followed by quantization-aware training) and is compiled into TFHE circuits for homomorphic inference. We further specify a client-server protocol with session-bound blinding and decrypt-and-return verification, enabling the server to authenticate users without observing raw behavioral features. We provide a cryptographic security analysis against an honest-but-curious server under TFHE IND-CPA security, and formalize resistance to replay and impersonation without the TFHE secret key. Experiments on two public touchscreen datasets demonstrate that FBAN achieves strong authentication utility under encrypted inference while maintaining a lightweight model footprint, with TFHE parameters instantiated at $\geq 128$-bit security.

---


### 238. [LFHE: Local-First Heuristic Evolution for Bounded Local Topology Search in Decentralized Learning with Non-IID Data](https://arxiv.org/abs/2610.08176)

**<font color=#1a73e8>作者：</font>** Yin-Kuan Liang, Yan Gao, Yang Long  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized learning is highly sensitive to communication topology under non-IID data. Adaptive peer-selection methods can exploit local model information, but broader peer discovery may require increasingly large control state, whereas direct spectral optimization typically relies on graph-wide information. We study the intermediate setting of bounded local topology search and propose Local-First Heuristic Evolution (LFHE), a representation-driven rewiring framework whose candidate discovery and scoring use only ego-neighborhood and friend-of-a-friend (FoF) information. The structural score admits an exact interpretation through graph Dirichlet energy: its sum across clients equals twice the representation Dirichlet energy, which under standard linear consensus dynamics governs the instantaneous dissipation of representation disagreement. LFHE combines this state-dependent structural signal with early exploration and degree control, while algebraic connectivity remains an offline graph diagnostic. Under bounded sparse degree, its FoF candidate state remains local rather than expanding toward population-wide peer tracking. Across four image, speech, and text benchmarks, LFHE achieves competitive decentralized learning performance. Matched-protocol controls identify the structural term as the principal empirical topology-selection signal, while comparison with broader peer discovery exposes a trade-off between predictive performance and discovery-state locality. Together, these results motivate state-aware bounded local topology search between pairwise peer selection and globally informed topology optimization.

---


### 239. [On the Intrinsic Limited Robustness of Latent-Based Watermarking](https://arxiv.org/abs/2610.08178)

**<font color=#1a73e8>作者：</font>** Cheng-Han Yeh, Kuan-chun Yu, Cheng-Chang Tsai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing latent-based watermarking methods for diffusion models have overestimated their robustness to image distortions, including geometric transformations such as rotation, scaling, and translation (RST). Moreover, this paradigm of watermarking approaches may suffer from inherent limitations arising from the domain in which the watermark is embedded. In this paper, we provide the first theoretical analysis explaining why these methods lack invariance to perturbations. By relaxing the invariant relation, we derive a maximum perturbation bound that characterizes the relationship between pixel-space perturbations and their corresponding effects in latent space. In addition, we present the first analytical formulation that captures all components of practical detection mechanisms. Finally, we conduct experiments to validate the theoretical findings and the limitations of latent-based watermarking methods. Our theoretical and empirical results indicate that, under the current design paradigm, latent-based watermarking methods intrinsically exhibit limited robustness. We conclude by providing the analytical tool and design guidelines that future research could follow.

---


### 240. [View Matters: Keyframe-Guided Text-Driven 3D Gaussian Editing](https://arxiv.org/abs/2610.08179)

**<font color=#1a73e8>作者：</font>** Kaizhe Zhang, Yijie Zhou, Weizhan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D Gaussian editing commonly does not distinguish the editing reliability of rendered views, although different viewpoints provide supervision of substantially different quality. Views that clearly show the scene and match the edit instruction provide reliable guidance, while less informative views may weaken the edit when all views are treated equally. We present View Matters, a view-importance-aware framework that conducts editing around reliable keyframes. Keyframe Importance Estimation (KIE) identifies reliable views using geometric visibility, semantic distinctiveness, and edit relevance. Keyframe-Guided Editing (KGE) then propagates their editing signals asymmetrically to non-keyframes without noisy reverse influence, while Importance-Aware Optimization (IAO) preserves this reliability preference during 3DGS optimization. Across 23 scene-prompt pairs, View Matters achieves the highest average CLIP text-image similarity of 0.2822 and directional similarity of 0.2564 among the evaluated methods, with a four-minute editing time. Additional adjacent-view analysis indicates that the fidelity-oriented editing process maintains cross-view coherence.

---


### 241. [PIE-PS: Photometric Stereo from Physical Irradiance Event Streams](https://arxiv.org/abs/2610.08188)

**<font color=#1a73e8>作者：</font>** Xiangze Meng, Guangyu Li, Jing Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras record asynchronous log-image-irradiance changes with microsecond latency and high dynamic range. These properties are useful for photometric stereo under moving illumination, but raw events are sparse and depend on an unknown contrast threshold. We start from the event trigger model and derive a physical relation between adjacent events, light motion, and surface normals. This relation gives a direct physics-only solver, but the solver needs the threshold, enough events at each pixel, and independent per-pixel optimization. To address these limits, we introduce PIE-PS, a learning-based framework for dense surface normal reconstruction from raw event streams and known lighting. We form Physical Irradiance Events (PIEs) by pairing two adjacent events at the same pixel with their corresponding light directions. Each PIE provides a Physical Irradiance Event Feature (PIEF), defined as the signed event rate. PIEF does not require the unknown contrast threshold. To share spatial and temporal context across nearby PIEs, we introduce PIE-GNN, which treats each PIE as a graph node and encodes it with its light-pair geometry. Since the reliability of PIE observations can vary with local appearance, illumination geometry, and sensor noise, Reliability-Grading Attention (RGA) predicts reliability weights to down-weight unreliable PIEs. Pixel aggregation then produces dense normals. Experiments on synthetic and real data show that PIE-PS outperforms prior event-based photometric stereo methods and the direct solver baseline.

---


### 242. [MacJEPA: Missingness-Robust Audio-Visual Recognition from Untrimmed Egocentric Videos](https://arxiv.org/abs/2610.08192)

**<font color=#1a73e8>作者：</font>** Souptik Sen, Zahra Ahmadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual models improve egocentric action recognition by exploiting complementary cues, yet typically assume that both streams remain available at inference. Existing missing-modality methods operate on trimmed, single-event clips in which a stream is entirely present or absent, whereas real sensors fail and recover within long, untrimmed observations. We redefine egocentric modality missingness as temporally localized sensor outages within untrimmed, multi-event observations, with whole-clip absence as the limiting case. We introduce \textbf{MacJEPA}, a missing-modality-robust \textbf{Ma}sked-\textbf{c}ontext query \textbf{JEPA} that recognizes visual actions and acoustic events from supplied interval queries over audio-visual context. Window-local modality dropout simulates these sensor outages during training. MacJEPA further repurposes masking in JEPA from a self-supervised pretext into a supervised robustness objective, aligning masked and clean latent representations of both multimodal content tokens and the task-conditioned queries. All objectives are optimized jointly with recognition in a single stage, requiring no test-time adaptation. Across Epic-Kitchens-100 and Epic-Sounds, a single checkpoint remains competitive under complete input and consistently surpasses published missing-modality baselines when either the dominant or auxiliary stream is removed. MacJEPA thus unifies strong full-input recognition with temporal missing-modality robustness in a single model operating on untrimmed multi-event videos.

---


### 243. [Building A Civic Tool for Community-Police Engagement to Adapt Neighborhood Policing](https://arxiv.org/abs/2610.08212)

**<font color=#1a73e8>作者：</font>** Ravinithesh Reddy Annapureddy, Staņislavs Šeiko, Natalie Higham-James 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data-driven policing often prioritizes incident records over residents' lived experiences. In the Baltic city of Riga, with a history of distrust and limited community-police engagement, this can further alienate the public. To bridge this gap, we propose a Research through Design (RtD) inquiry into the development of Par drošu Rīgu, a civic tool for community-data-integrated policing. With municipal police, NGOs, and city staff, we ask how RtD enables stakeholder negotiation and which interaction qualities support trust and the use of combined community and incident data. The co-design process included workshops that surfaced divergent notions of safety; material probes designed as boundary objects to negotiate among stakeholders; and a pilot deployment showing how combining quantitative and qualitative data reshapes engagement and trust. Mixed-methods evaluation suggests increased officer-citizen interaction, but frictions in sustaining stakeholder collaboration. We contribute (i) an empirical RtD inquiry with public institutions, (ii) an artifact combining physical and dashboard interactions, and (iii) reflections on interaction design as a boundary-spanning practice for trust and infrastructuring.

---


### 244. [RACE-FPP: A Robust AI-assisted Characterisation Enhancement for Fringe Projection Profilometry](https://arxiv.org/abs/2610.08213)

**<font color=#1a73e8>作者：</font>** Osman Ali, Xiangjun Kong, Tibebe Yalew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fringe Projection Profilometry (FPP) requires precise system characterisation to achieve reliable three-dimensional (3D) reconstructions; however, characterisation accuracy strongly depends on robust checkerboard feature localisation, which can deteriorate under challenging imaging conditions such as lens blur and characterisation target orientations. Existing deep learning-based corner detectors are typically assessed using detection metrics and camera reprojection error alone, without considering their wider impact on projector characterisation, camera-projector stereo characterisation consistency, or overall measurement accuracy. In this work, we introduce a complete FPP characterisation pipeline that incorporates deep learning-based corner detection into the standard camera characterisation workflow. We also characterise the projector by sampling phase values at the centres of the white squares in the characterisation target. Rather than treating corner detection as an isolated task, the proposed framework explicitly analyses how localisation errors propagate throughout the entire FPP characterisation chain. Performance is evaluated using detection metrics (e.g., precision and recall), camera and projector reprojection errors, and the camera and projector stereo characterisation. Across a mixed dataset of clean and degraded images, the camera reprojection error is reduced from 1.237 pixels to 0.259 pixels, while the projector reprojection error is reduced by roughly 50%. Dimensional evaluation of reconstructed artefacts shows improved geometric accuracy compared with those resulting from the conventional pipeline. Overall, the findings indicate increased robustness of system-level characterisation under challenging imaging conditions, thereby enabling more reliable industrial FPP measurements.

---


### 245. [Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology](https://arxiv.org/abs/2610.08214)

**<font color=#1a73e8>作者：</font>** Christoph Benzmüller, David Fuenmayor, Luca Pasetto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics; through these semantical embeddings a single proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes one environment in which students learn, experiment with, and compare logics. After making the pedagogical case for proof assistants in the logic classroom, we present a graded sequence of classroom examples, each transition motivated by a limitation of the preceding representation, by a need for more explicit modelling resources, or by a new application. A liars-and-truth-tellers puzzle leads from propositional to modal logic; the Wise Men puzzle leads on to dynamic epistemic logic; Boolos's curious inference illustrates what a higher-order meta-logic buys, even for automated proof search; Chisholm's paradox takes the sequence into deontic logic, and from standard to dyadic deontic logic; and Gödel's ontological argument brings it to a research-level metaphysical argument. We then rebut the objection that embedding everything in classical HOL is monism rather than pluralism, reflect on three years of teaching such a course, and sketch the portability of the approach beyond Isabelle.

---


### 246. [Quantum Entangled Multimodal Fusion Networks (QEMFN): Resource-Aware Hybrid Vision-Language Fusion via Trainable Entanglement](https://arxiv.org/abs/2610.08216)

**<font color=#1a73e8>作者：</font>** Srikar Alla, Ali Shiri Sichani, Chi-Ren Shyu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal vision-language systems typically fuse image and text embeddings through classical operators such as concatenation, attention, bilinear pooling, or tensor interactions. We propose Quantum Entangled Multimodal Fusion Networks (QEMFN), a hybrid quantum-classical framework that introduces parameterized entanglement as a structured inductive bias for multimodal fusion. Pretrained visual and textual features are projected into compact latent spaces, encoded as angle-parameterized quantum states, processed through intra-modal and paired cross-modal entangling circuits, and measured to produce fused representations for retrieval. Under matched parameter budgets and identical frozen CLIP backbones, QEMFN outperforms classical fusion baselines on COCO-5k and Flickr30k, including multilayer perceptron, tensor fusion, FiLM, cross-attention, compact transformer, and a dequantized paired-topology analogue. An ablation suite isolates the quantum module's contribution from the surrounding classical projections, and quantum-centric analyses report Meyer-Wallach entangling capability, expressibility, gradient variance against barren-plateau bounds, and entropy-performance correlation under controls for training progress alongside an intervention study on the entangling component. QEMFN is executed under shot-based estimation, a noise-modeled fake backend, and a real superconducting device with zero-noise extrapolation. This work does not claim quantum computational advantage; the contribution is the framework together with a controlled empirical and quantum-centric evaluation that positions trainable entanglement as an interpretable, hardware-executable fusion mechanism at scales accessible on contemporary devices.

---


### 247. [Confidence-Ordering Reversal under Contextual Priors in Neural Decoding](https://arxiv.org/abs/2610.08229)

**<font color=#1a73e8>作者：</font>** Xinyu Zhang, Sichao Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contextual priors improve neural-to-language decoding by reshaping candidate scores. However, confidence is read from the same reshaped scores, so the errors a prior leaves behind can become more confident with no change in accuracy to reveal it. We study how a prior shapes confidence in speech retrieval on MEG-MASC and MOUS using local decoding scores, a contextual prior combined by additive shallow fusion, and the fused top-two margin as confidence. Among initially incorrect predictions, we find a confidence-ordering reversal: a larger margin makes a repair more likely when the correct candidate starts near the top of the local ranking, but less likely when it starts lower. On MEG-MASC, pooled correctness AUROC is 0.87, yet AUROC separating repairs from residual errors falls from 0.70 at initial ranks 2-3 to 0.39 at ranks 21-50. Errors starting beyond rank 20, inside the reversed region, make up 46.6% of all post-fusion errors. We propose a score-level account: a repair must first close the correct candidate's initial deficit, limiting its final margin, whereas a residual error can build a large margin between two incorrect candidates. A causal intervention that changes only the fusion weight moves the reversal to deeper ranks as predicted. Under a word-level LM prior, it keeps moving after accuracy gain peaks, so a weight chosen for accuracy does not settle confidence. Reading local and prior scores separately improves selective decoding: the decoder answers on 74.5% of windows instead of 56.7%, while 92% of output sets still contain the correct candidate. Confidence after contextual fusion should retain the local and contextual evidence behind each prediction, not just the fused scores. Project website: this https URL Code: this https URL

---


### 248. [TSRN-RTVD: Real-Time Video Deblurring System](https://arxiv.org/abs/2610.08230)

**<font color=#1a73e8>作者：</font>** Nikita Alutis, Danila Evsyukov, Egor Chistov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video capture moves to handheld and edge devices, motion blur from camera shake has become a pervasive degradation that lowers perceptual quality and harms downstream vision tasks. The strongest deblurring networks recover impressive detail, yet they remain computationally heavy and overwhelmingly complex, so their quality comes at a cost that consumer hardware cannot pay in real time. This gap between restoration quality and on-device speed is exactly what makes real-time deblurring difficult.
We developed and implemented TSRN-RTVD, an efficient video deblurring system that explicitly reconstructs the underlying camera trajectory during exposure and uses the recovered motion to guide restoration. This approach turns the physical cause of blur into a signal that drives sharpening. Our system runs on a single consumer GPU and restores the video at 30 FPS while reaching 30.08 dB PSNR on the GoPro dataset. We demonstrate TSRN-RTVD on consumer devices with interactive side-by-side visualization of the blurry input and the deblurred output, live throughput, and an on-screen view of the recovered camera trajectory. Demo video is available at this https URL.

---


### 249. [Sensor-Language-Action Models](https://arxiv.org/abs/2610.08244)

**<font color=#1a73e8>作者：</font>** Yuekai Xu, Zitao Shuai, Yuzhe Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sensors are useful not only for understanding the world but also for deciding what to do next. Existing sensor models however largely stop at perception: they recognize states or predict outcomes, leaving actions modeled separately through task-specific and often closed label spaces. We introduce Sensor-Language-Action (SLA) modeling, a framework that connects multimodal sensor observations, natural language, and actions within a unified model. SLA uses language as a semantic interface between sensing and acting, allowing heterogeneous actions to be represented, predicted, and explained while remaining grounded in the underlying sensor evidence. We build a large-scale SLA benchmark consisting of datasets that span more than 116,000 individuals, 79 sensor modalities, and 60 action groups, together with a multi-faceted captioning pipeline that aligns user context, sensor dynamics, and action evidence. Building on this framework, we present OpenSLA, a unified SLA model for hierarchical action prediction, state understanding, and action explanation. Extensive experiments on real-world tasks in clinical prediction, operating rooms, and metabolic health verify its superior performance over the state-of-the-art. OpenSLA also demonstrates intriguing capabilities including language-guided evidence grounding and zero-shot generalization to unseen actions and cohorts.

---


### 250. [HE-OFT: Privacy-Preserving One-Shot Federated Fine-Tuning under Homomorphic Encryption](https://arxiv.org/abs/2610.08255)

**<font color=#1a73e8>作者：</font>** Halil İbrahim Kanpak, Sinem Sav, Alptekin Küpçü  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many organizations adapt large pretrained models to their own tasks by fine-tuning on private data. Several of these parties often hold data for the same task and wish to fine-tune a model together without pooling that data. Federated learning (FL) enables joint fine-tuning, but reconstruction attacks on shared intermediate values (the model or its gradients) remain a privacy risk. A one-shot protocol that exchanges one encrypted contribution exposes no intermediate value. Such a protocol still gives the trained model to every participant, which is not permitted where the model is a regulated or proprietary asset. We present HE-OFT, the first cryptographically secure one-shot federated fine-tuning protocol in which no party receives the trained model. Each client fine-tunes a low-rank adapter and a classifier head on a frozen public backbone and keeps the adapter. The client uploads one encrypted head displacement, which the server combines under multiparty CKKS and never decrypts. A quorum of clients returns only the predicted label to the querier. On four text classification tasks and one vision task, HE-OFT reaches 61 to 79 per cent accuracy, against 20 to 48 per cent for a client training alone. HE-OFT keeps 85 to 96 per cent of the accuracy of a disclosed model. A test-time query takes 443.1 to 1713.1 s on one core, or 56.1 to 255.1 s with level restoration on a GPU. Restoring levels at the server cuts the traffic per query from up to 1.6 GiB to 13.5 MiB.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-335](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
