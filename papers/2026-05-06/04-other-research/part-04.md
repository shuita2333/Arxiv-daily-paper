# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 151. [rAIson: Developing Reliable Decision-Making Agents](https://arxiv.org/abs/2605.01351)

**<font color=#1a73e8>作者：</font>** Pavlos Moraitis, Nikolaos Spanoudakis, Antonis Kakas  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper presents the rAIson platform, a high-level technological environment for the development of automated, reliable and explainable decision-making agents. The research underlying the platform and its technological progress has now reached a mature stage that allows the platform to be used for the development of complex real-life applications without writing a single line of code.

---


### 152. [AgriKD: Cross-Architecture Knowledge Distillation for Efficient Leaf Disease Classification](https://arxiv.org/abs/2605.01355)

**<font color=#1a73e8>作者：</font>** Minh-Dung Le, Minh-Duc Hoang, Hoang-Vu Truong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated leaf disease classification is critical for early disease detection in resource-constrained field environments. Vision Transformers (ViTs) provide strong representation capability by modeling long-range dependencies and inter-class relationships; however, their high computational cost makes them impractical for deployment on edge devices. As a result, existing approaches struggle to effectively transfer these rich representations to lightweight models. This paper introduces AgriKD, a cross-architecture knowledge distillation framework for efficient edge deployment, which transfers knowledge from a Vision Transformer (ViT) teacher to a compact convolutional student model. To bridge the representational gap between Transformer and CNN architectures, the proposed approach integrates multiple distillation objectives at the output, feature, and relational levels, where each objective captures a different aspect of the teacher knowledge. This enables the student model to better preserve and utilize transformer-derived global representations. Experiments on multiple leaf disease datasets show that the distilled student achieves performance comparable to the teacher while significantly improving efficiency, reducing model parameters by approximately 172 times, computational cost by 47.57 times, and inference latency by 18-22 times. Furthermore, the optimized model is deployed across multiple runtime formats, including ONNX, TFLite Float16, and TensorRT FP16, achieving consistent predictive performance with negligible accuracy degradation. Real-world deployment on NVIDIA Jetson edge devices and a mobile application demonstrates reliable real-time inference, highlighting the practicality of AgriKD for AI-powered agricultural applications in resource-constrained environments.

---


### 153. [On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility](https://arxiv.org/abs/2605.01357)

**<font color=#1a73e8>作者：</font>** Zhitao He, Haolin Yang, Rui Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) excel at long-context understanding but exhibit significant limitations in long-form generation. Existing studies primarily focus on single-generation quality, generally overlooking the volatility of the output. This volatility not only leads to significant computational costs but also severely impacts the models' reliable application. To address this gap, our work unfolds in three stages: benchmarking, probing, and mitigation. We first propose the VOlatility in Long-form Text Benchmark (VOLTBench), a novel heterogeneous-task benchmark designed to systematically quantify the length volatility of long-form generation. Subsequently, by analyzing attention traces, we conduct an in-depth probe to identify several common internal patterns that cause this volatility. Finally, to mitigate long-form output volatility, we propose Stable Generation via Logits Boosting (GLoBo), a lightweight decoding-stage optimization strategy, designed to significantly enhance both the length accuracy and stability of long-form generation without additional training. Extensive experiments on VOLTBench provide the first systematic confirmation of severe long-form output instability in mainstream models and validate that our proposed method successfully improves the mean output length of the base model by 148% and reduces the length volatility by 69%, while maintaining high generation quality.

---


### 154. [PACE: Parameter Change for Unsupervised Environment Design](https://arxiv.org/abs/2605.01358)

**<font color=#1a73e8>作者：</font>** Fang Yuan, Quanjun Yin, Siqi Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised Environment Design (UED) offers a promising paradigm for improving reinforcement learning generalization by adaptively shaping training environments, but it requires reliable environment evaluation to remain effective. However, existing UED methods evaluate environments using indirect proxy signals such as regret, value-based errors, or Monte Carlo, which suffer from bias, high variance, or substantial computational overhead and fail to reflect agent realized learning progress. To address these limitations, we propose Parameter Change Environment Design (PACE), which evaluates an environment through the policy parameter change induced by training on that environment, directly grounding environment selection in realized learning progress. Specifically, PACE assigns environment value using a first-order approximation of the policy optimization objective, where the improvement induced by an environment is proportional to the squared L2 norm of the corresponding parameter update, enabling low-variance and computation-efficient evaluation without additional rollouts. Experiments on MiniGrid and Craftax show that PACE consistently outperforms established UED baselines, achieving higher IQM and smaller Optimality Gap on OOD evaluations, including an IQM of 96.4% and an Optimality Gap of 17.2% on MiniGrid.

---


### 155. [Structural Ranking of the Cognitive Plausibility of Computational Models of Analogy and Metaphors with the Minimal Cognitive Grid](https://arxiv.org/abs/2605.01359)

**<font color=#1a73e8>作者：</font>** Alessio Donvito, Antonio Lieto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we employ the Minimal Cognitive Grid (MCG), a framework created to evaluate the cognitive plausibility of artificial systems, to offer a systematic assessment of leading computational models of analogy and metaphor, including the Structure-Mapping Engine (SME), CogSketch, METCL, and Large Language Models (LLMs). We present a formal and quantitative operationalization of the MCG framework and, through the analysis of its three main dimensions (Functional/Structural Ratio, Generality, and Performance Match), examine how well each system aligns with standard cognitive theories of the modeled phenomena, thus allowing for comparison of the models with respect to their cognitive plausibility, according to consistent and generalizable mathematical criteria.

---


### 156. [Decision-Focused Learning via Tangent-Space Projection of Prediction Error](https://arxiv.org/abs/2605.01361)

**<font color=#1a73e8>作者：</font>** Junhyeong Lee, Sangjin Jin, Yongjae Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-Focused Learning (DFL) trains predictors to improve downstream decision quality, but computing regret gradients typically requires differentiating through solvers or relying on surrogate losses, which can be computationally expensive or deviate from the true objective. We show that, under standard regularity with locally stable active constraints, the regret gradient admits a closed-form geometric characterization, equivalent to the prediction error projected onto the tangent space of active constraints, scaled by local curvature. This reveals that regret gradients can be obtained by filtering decision-irrelevant components from the MSE gradient, providing a simpler and more direct alternative to existing approaches. Based on this, we propose PEAR (Projected Error As Regret-gradient), which computes regret gradients via a reduced linear system over active constraints, avoiding differentiation through solver iterations or additional optimization solves. Experiments on LP benchmarks and a real-world QP task show that PEAR achieves the best decision quality among all baselines while being the most computationally efficient, with gains that persist under constraint shifts.

---


### 157. [Toward a foundational thermal model for residential buildings](https://arxiv.org/abs/2605.01364)

**<font color=#1a73e8>作者：</font>** Ting-Yu Dai, Kingsley Nweye, Dev Niyogi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The building energy community lacks a foundational thermal model, i.e., a single pretrained model capable of generalizing across diverse buildings, climates, and control strategies without building-specific calibration. Achieving this vision requires architectural principles that capture universal thermal dynamics rather than memorizing building-specific patterns. We take a step toward this goal by presenting a physics-informed transformer architecture that embeds domain knowledge, e.g., derivative enrichment and Euler-based numerical integration, into a decoder-only framework. We incorporate static building features extracted from simulation models and employ Rotary Position Embedding attention to capture temporal dependencies. Evaluated on the CityLearn dataset spanning 247 residential buildings across three climate zones, our model achieves one-step prediction accuracy (RMSE of 0.30°C in Texas, 0.29°C in Vermont) while outperforming both traditional baselines and fine-tuned Time-Series Foundation Models. We also demonstrate zero-shot transferability: models trained on as few as two buildings generalize to unseen buildings and climate zones without fine-tuning. Despite the limitation of simulated residential buildings, our results establish physics-informed architectural principles as a promising foundation for universal building thermal models.

---


### 158. [A Cellular Doctrine of Morality: Intrinsic Active Precision and the Mind-Reality Overload Dilemma](https://arxiv.org/abs/2605.01376)

**<font color=#1a73e8>作者：</font>** Ahsan Adeel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI systems, grounded in oversimplified neuroscience, risk eroding the distinction between truth and falsehood. They maximize reward by amplifying attention to information without intrinsic precision mechanisms to assess whether it is valid or worth attending to. This increases both the volume of information and the inherent biases in what the system attends to, whether true, false, or irrelevant. If not corrected, this trend will accelerate, threatening to overload systems and individuals with biased and dubious information and increasing the risk of confusion, poor judgment, and irrational or harmful decisions and behaviour, a condition I term the mind-reality overload dilemma. I argue that this threat may be mitigated by providing the public with access to more advanced AI tools built on the biophysical dynamics of pyramidal neurons underlying awake thought and higher-order cognition. These neurons support an intrinsic active precision mechanism that, rather than merely maximizing reward, uses locally and globally coherent predictions to evaluate the validity and contextual adequacy of evidence before it is attended to or propagated through hierarchies, prioritizing coherence and adequacy before attention.~While this approach does not derive or prescribe moral rules from biology, it may give rise to AI with more "real understanding", helping restore epistemic conditions by reducing information overload and amplifying reliable information, thereby supporting the formation of better-informed beliefs and more coherent judgments that benefit society at large-though no guarantees exist.

---


### 159. [A framework for analyzing concept representations in neural models](https://arxiv.org/abs/2605.01381)

**<font color=#1a73e8>作者：</font>** Burin Naowarat, Hao Tang, Sharon Goldwater  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how neural models represent human-interpretable concepts is challenging. Prior work has explored linear concept subspaces from diverse perspectives, such as probing and concept erasure. We introduce a unified framework to study these subspaces along two axes: \textit{containment}, which tests if a concept is fully represented in a subspace but not outside it, and \textit{disentanglement}, which tests for isolation from other concepts. In experiments on both text and speech models, we first highlight that concept subspaces may not be uniquely determined, and discuss the implications for concept subspace analysis. Then, we compare properties of concept subspaces estimated using five estimators, proposed in different communities. We find that (1) the choice of estimator impacts the containment and disentanglement properties; (2) the state-of-the-art concept erasure method, LEACE, performs well on both testing axes, but still struggles to generalize to unseen data; and (3) in HuBERT speech representations, phone information is both contained and disentangled from speaker information, while speaker information is hard to contain in a compact subspace, despite being disentangled from phones.

---


### 160. [Sparse Representation Learning for Vessels](https://arxiv.org/abs/2605.01382)

**<font color=#1a73e8>作者：</font>** Chinmay Prabhakar, Bastian Wittmann, Paul Büschl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analyzing human vasculature and vessel-like, tubular structures, such as airways, is crucial for disease diagnosis and treatment. Current methods often rely on small sub-regions or simplified tree-like structures, rendering analysis of entire organ-level networks at clinical resolution computationally challenging. To this end, we propose VAEsselSparse, an efficient encoder-decoder model to obtain a meaningful yet compact representation of the entire organ-level vascular network at sub-millimeter resolution. VAEsselSparse leverages the inherent sparsity of 3D vascular structures via sparse convolutions and attention mechanisms, achieving substantial spatial compression rates of 8 x 8 x 8. We demonstrate superior reconstruction performance compared to dense counterparts and previous methods. Importantly, the resulting latent space retains clinically relevant discriminative features readily usable for classification tasks, such as aneurysm/stenosis or subvariants of the circle of Willis. Moreover, the compact latent space of VAEsselSparse serves as an effective representation for learning vessel-specific priors through generative models, enabling the synthesis of realistic vasculature.

---


### 161. [Sequential Learning and Catastrophic Forgetting in Differentiable Resistor Networks](https://arxiv.org/abs/2605.01383)

**<font color=#1a73e8>作者：</font>** Maniru Ibrahim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable physical networks provide a simple setting in which learning can be studied through the interaction between trainable parameters and physical equilibrium constraints. We investigate sequential learning in differentiable resistor networks governed by Kirchhoff's laws. Although individual input--output mappings can be learned by gradient-based adjustment of edge conductances, sequential training on conflicting tasks produces catastrophic forgetting. We show that forgetting is controlled by task conflict and by the degree of adaptation to the new task. Uniform anchoring and normalised gradient-weighted anchoring reduce forgetting only by increasing the final loss on the new task, giving a clear forgetting--adaptation trade-off. We also show that forgetting is associated with localised conductance changes on high-current edges, giving a physical interpretation as reconfiguration of dominant transport pathways. Broader random-task ensembles show that the strongest forgetting occurs when the second task reverses the output ordering imposed by the first task. Finally, comparisons across Erdős--Rényi, small-world, scale-free, and random-geometric graph ensembles show that topology changes the forgetting--adaptation balance. These results position differentiable resistor networks as compact, physically interpretable testbeds for studying continual learning in tunable matter.

---


### 162. [VISTA: Video Interaction Spatio-Temporal Analysis Benchmark](https://arxiv.org/abs/2605.01391)

**<font color=#1a73e8>作者：</font>** Alejandro Aparcedo, Akash Kumar, Aaryan Garg 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for Vision-Language Models (VLMs) primarily evaluate spatio-temporal understanding on simple single-action videos, closed attribute sets and restricted entity types, failing to capture the freeform, multi-action interactions between diverse entities which characterize real-world video understanding. Furthermore, the lack of a systematic framework for analyzing model failures across complementary spatio-temporal axes hinders comprehensive evaluation. To address these gaps, we introduce VISTA, a Video Interaction Spatio-Temporal Analysis benchmark designed for open-set, multi-entity and multi-action spatio-temporal understanding in VLMs. VISTA decomposes videos into interpretable entities, their associated actions, and relational dynamics, enabling multi-axis diagnostics and unified assessment of relational, spatial, and temporal understanding. Our benchmark integrates multiple datasets into a single interaction-aware taxonomy and comprises ~12K curated video-query pairs spanning diverse scenes and complexities. We systematically evaluate 11 state-of-the-art VLMs on VISTA, and break down aggregate performance across our taxonomy to reveal shortcomings and pronounced spatio-temporal biases obscured by traditional metrics. By providing detailed, taxonomy-driven diagnostics on a challenging dataset, VISTA offers a nuanced framework to guide advances in model design, pretraining strategies, and evaluation protocols. Overall, VISTA is the first, large-scale, interaction-aware diagnostic benchmark for spatio-temporal understanding in VLMs.

---


### 163. [Recall to Predict: Grounding Motion Forecasting in Interpretable Motion Bank](https://arxiv.org/abs/2605.01393)

**<font color=#1a73e8>作者：</font>** Abhishek Vivekanandan, Ahmed Abouelazm, J. Marius Zöllner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion forecasting often requires trading interpretability for predictive accuracy. Standard anchor-based architectures rely on opaque latent queries that are highly prone to latent collapse, or naive trajectory sampling that limits multi-modal diversity. We propose an end-to-end differentiable framework that grounds predictions in a comprehensive "motion bank", a structured embedding space of physically realizable trajectories constructed via contrastive learning. Rather than regressing paths from a blank slate, our architecture dynamically retrieves explicit motion priors using a novel Anchor Retrieval Layer. This module adapts orthogonally initialized queries via a Dual-Level Gated Cross-Attention mechanism and executes discrete trajectory selection using a Straight-Through Gumbel-Softmax estimator to preserve continuous gradient flow. The retrieved semantically grounded anchors are then geometrically refined by a DETR-style decoder, optimized jointly with a Winner-Takes-All (WTA) kinematic Gaussian Mixture Model (GMM), a latent diversity penalty, and a soft-min weighted endpoint loss. By strictly conditioning the decoding phase on diverse, interpretable motion primitives, our approach eliminates the "black box" of standard latent queries while achieving competitive multi-modal accuracy on the Argoverse 2 and Waymo Open Motion datasets. Code is available at: this https URL

---


### 164. [Investigating the Effects of Different Levels of User Control in an Interactive Educational Recommender System](https://arxiv.org/abs/2605.01400)

**<font color=#1a73e8>作者：</font>** Qurat Ul Ain, Mohamed Amine Chatti, William Kana Tsoplefack 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Educational recommender systems (ERSs) are becoming increasingly important in enhancing educational outcomes and personalizing learning experiences by providing recommendations of personalized resources and activities to learners, tailored to their individual learning needs. While user control is widely assumed to improve user experience, the effects of different levels of control in ERSs remain underexplored. To address this gap, we designed and evaluated an interactive ERS within the MOOC platform CourseMapper, where learners could interact with the input (i.e., user profile), process (i.e., recommendation algorithm), and output (i.e., recommendations) of the system. We conducted a between-subjects user study (N=184) to examine how varying levels of user control in an ERS influenced users' perceptions of the recommendation goals of perceived control, transparency, trust, satisfaction, and perceived quality. Our results show that enabling users to build and refine their profile is sufficient to promote positive perceptions of the ERS, while additional control options mainly reinforce these impressions. Moreover, perceived control is the only goal significantly affected by providing different levels of user control in the ERS, with input control exerting the strongest influence. Furthermore, different levels of control affect transparency, trust, satisfaction, and perceived quality in distinct yet interconnected ways. Overall, the findings provide empirical evidence that user control positively shapes transparency, trust, satisfaction, and perceived quality, though to varying extents.

---


### 165. [AI Expert Twin: Capturing Expert Cognition for Human-Centred, Practice-Based Learning](https://arxiv.org/abs/2605.01401)

**<font color=#1a73e8>作者：</font>** Annie Yuan, Xiaohua Chen, Kalina Yacef 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Tacit knowledge embedded in expert practice remains difficult to capture, formalise, and scale. While AI-driven educational systems have advanced personalisation, learner modelling, affective support, and self-regulated learning, they less often model the tacit reasoning and context-sensitive judgement that underpin expert practice in practice-based domains. This paper introduces the AI Expert Twin, a cognition-centric framework that models expert knowledge as structured, computable representations of procedural actions, semantic concepts, and decision processes. The framework also considers how value-laden preferences, trade-offs, and uncertainty shape expert judgement in practice. We formalise expert cognition as a three-layer representation and capture knowledge from experts under this model, laying the groundwork for integration into AI-powered educational system. A case study in a cultural heritage workshop demonstrates the feasibility of the approach in a real-world setting. The framework is designed to be transferable across domains such as vocational education and creative industries. By embedding expert heuristics into AI while maintaining transparency and learner agency, the AI Expert Twin offers a novel path towards scalable, practice-based learning and invites further research on ethical, human-centred applications of AI in education.

---


### 166. [Rethinking Multi-Label Node Classification: Do Tuned Classic GNNs Suffice?](https://arxiv.org/abs/2605.01403)

**<font color=#1a73e8>作者：</font>** Yuxuan Xiao, Shengzhong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-label node classification (MLNC) has recently been addressed by increasingly complex label-aware designs that explicitly model node-label interactions and inter-label this http URL, it remains unclear whether the advantages of these methods truly stem from their specialized designs, or simply from insufficiently optimized baselines. In this paper, we revisit MLNC from a strong-baseline perspective and investigate whether carefully tuned classic full-graph GNNs can already serve as strong solutions to this task. We systematically study several representative backbones, including GCN, SSGConv, and GCNII, and optimize them using standard yet effective techniques such as normalization, dropout, and residual connections. Experiments on five representative benchmark datasets show that our tuned baselines outperform representative specialized methods on four datasets and achieve state-of-the-art performance in multiple settings. These results indicate that careful tuning of classic backbones is a highly influential but often overlooked factor in MLNC, and highlight the need for more rigorous strong-baseline evaluation in future research on multi-label graph learning.

---


### 167. [AI Safety as Control of Irreversibility: A Systems Framework for Decision-Energy and Sovereignty Boundaries](https://arxiv.org/abs/2605.01415)

**<font color=#1a73e8>作者：</font>** Wesley Shu, Peng Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI systems compress the distance between capability growth and capability deployment. Earlier high-risk technologies were slowed by capital intensity, physical bottlenecks, organizational inertia, and specialized supply chains. By contrast, AI capabilities can be copied, invoked, embedded in workflows, and scaled across institutions at low marginal cost. This paper argues that declining deployment friction changes the safety problem at its root. Safety is not only local output correctness or preference alignment, but the control of irreversibility under rising decision density.
The paper formalizes this claim through decision-energy density: the rate-weighted capacity of a node to generate, evaluate, select, and execute consequential decisions. It then identifies three sovereignty boundaries that determine whether AI remains an amplifier within a human-governed system or becomes a de facto control center: irreversible decision authority, physical resource mobilization authority, and self-expansion authority. The model shows how efficiency pressure, path dependence, scale feedback, and weak boundary constraints concentrate decision-energy in the most efficient node. This concentration can diffuse responsibility and raise the probability of irreversible system-level loss even when local per-action error rates remain low.
The main result is a boundary stabilization theorem. It shows that safety need not require proving that advanced systems are always correct. Instead, it requires institutional and technical designs that prevent irreversible power from being released by a single high-efficiency node. The paper reframes AI safety as layered control, authorization, and externally reviewable limits, linking alignment, security engineering, organizational economics, and institutional design.

---


### 168. [TimeTok: Granularity-Controllable Time-Series Generation via Hierarchical Tokenization](https://arxiv.org/abs/2605.01418)

**<font color=#1a73e8>作者：</font>** Seokhyun Lee, Jaeho Kim, Changjun Oh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series generative models often lack control over temporal granularity, forcing users to accept whatever granularity the model produces. To enable truly user-driven generation, we introduce TimeTok, a unified framework for Granularity-Controllable Time-Series Generation (GC-TSG), which generates time series at any target granularity from any coarser input (e.g., rough sketches) or from scratch. At the core of TimeTok is a hierarchical tokenization strategy that maps time series into an ordered sequence of tokens, from coarse to fine temporal granularity. Our autoregressive generation process operates across these granularity levels, producing token blocks that are decoded back into continuous time series. This design naturally enables GC-TSG - including standard generation - within a single framework, where controlling the number of token blocks provides explicit control over output detail. Experiments show that TimeTok excels at GC-TSG tasks while achieving state-of-the-art performance in standard generation. Furthermore, we showcase TimeTok's potential as a foundational tokenizer by training on multiple datasets with heterogeneous temporal granularities, verifying strong transferability that consistently outperforms models trained on individual datasets. To our knowledge, this is the first unified framework that covers the full generative spectrum for time series, offering a valuable foundation for models that benefit from diverse temporal granularities.

---


### 169. [Artificial Jagged Intelligence as Uneven Optimization Energy Allocation Capability Concentration, Redistribution, and Optimization Governance](https://arxiv.org/abs/2605.01420)

**<font color=#1a73e8>作者：</font>** Wesley Shu, Peng Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Jagged Intelligence (AJI) denotes a recurring pattern in which large learning systems exhibit strong local capabilities while remaining weak or brittle in other domains. This paper develops a formal theory of AJI as uneven allocation of optimization pressure. We model training as a finite-budget process that distributes gradient-driven update energy across capability-relevant directions in parameter space. In this model, jagged capability profiles arise from anisotropic objective structure, data geometry, and representational coupling rather than from a single scalar quantity called intelligence.
The paper defines capability gain, optimization energy share, and jaggedness, then proves that persistent concentration of cumulative update energy yields lower bounds on dispersion in capability gains. A finite-budget tradeoff theorem shows why prioritizing one capability can impose opportunity costs on others unless positive coupling or shared structure offsets the cost. The analysis also studies redistribution mechanisms, including energy-variance regularization and auxiliary structural objectives, as interventions that reshape the optimization field.
The resulting framework links uneven emergence, training architecture, and optimization governance. It predicts that early concentration of update energy should forecast later capability jaggedness; that scaling under a narrow objective need not eliminate anisotropy; and that explicitly funded auxiliary objectives can revive neglected capabilities. AJI is therefore not merely a descriptive label for uneven model behavior, but a testable theory of how finite optimization resources produce concentrated, delayed, and structurally uneven capability formation.

---


### 170. [Barriers to Counterfactual Credit Attribution for Autoregressive Models](https://arxiv.org/abs/2605.01425)

**<font color=#1a73e8>作者：</font>** Aloni Cohen, Chenhao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative AI disrupts the practice of giving credit to work that came before. Ideally, a generative model would give credit to any work on which its output depends in a significant way. \emph{Counterfactual credit attribution} (CCA) is a technical condition formalizing this goal--a relaxation of differential privacy--recently introduced by Livni, Moran, Nissim, and Pabbaraju [2024] who studied it in the PAC learning setting.
We initiate the study of CCA generative models. Specifically, we consider autoregressive models giving credit to a deployment-time dataset (e.g., a RAG database). We uncover barriers to two natural approaches to CCA autoregressive models. First, we show that imposing CCA on the underlying next-token predictor does not guarantee that the model is CCA: CCA does not compose autoregressively (unlike DP). Second, we consider a different approach to building CCA models which we call \emph{retrofitting}. Retrofitting takes a model that does not attribute credit, and adds credit onto it. We prove a lower bound for CCA retrofitting under a weak optimality requirement. Given black-box access to the starting model, retrofitting requires query complexity exponential in the length of the model's outputs.

---


### 171. [Hallucinations Undermine Trust; Metacognition is a Way Forward](https://arxiv.org/abs/2605.01428)

**<font color=#1a73e8>作者：</font>** Gal Yona, Mor Geva, Yossi Matias  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite significant strides in factual reliability, errors -- often termed hallucinations -- remain a major concern for generative AI, especially as LLMs are increasingly expected to be helpful in more complex or nuanced setups. Yet even in the simplest setting -- factoid question-answering with clear ground truth-frontier models without external tools continue to hallucinate. We argue that most factuality gains in this domain have come from expanding the model's knowledge boundary (encoding more facts) rather than improving awareness of that boundary (distinguishing known from unknown). We conjecture that the latter is inherently difficult: models may lack the discriminative power to perfectly separate truths from errors, creating an unavoidable tradeoff between eliminating hallucinations and preserving utility.
This tradeoff dissolves under a different framing. If we understand hallucinations as confident errors -- incorrect information delivered without appropriate qualification -- a third path emerges beyond the answer-or-abstain dichotomy: expressing uncertainty. We propose faithful uncertainty: aligning linguistic uncertainty with intrinsic uncertainty. This is one facet of metacognition -- the ability to be aware of one's own uncertainty and to act on it. For direct interaction, acting on uncertainty means communicating it honestly; for agentic systems, it becomes the control layer governing when to search and what to trust. Metacognition is thus essential for LLMs to be both trustworthy and capable; we conclude by highlighting open problems for progress towards this objective.

---


### 172. [SCALE-LoRA: Auditing Post-Retrieval LoRA Composition with Residual Merging and View Reliability](https://arxiv.org/abs/2605.01429)

**<font color=#1a73e8>作者：</font>** Shuaipeng Zhou, Yu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Libraries of Low-Rank Adaptation (LoRA) adapters are becoming a practical by-product of parameter-efficient adaptation. Once such adapters accumulate, a natural question is no longer how to train one adapter for one task, but how to reuse an open pool of adapters for a new task given only a small support set. Prior work has shown that LoRA modules can be composed at the task level and dynamically selected at the instance level. However, open-pool LoRA reuse is not automatic: retrieving relevant adapters does not guarantee that their parameter updates are compatible, and composing adapters does not guarantee reliable outputs.
We introduce the Sparse-Composition Agreement Layer (SCALE), a post-retrieval audit and composition framework for open-pool LoRA reuse. SCALE contains a deployable 1.0* merge path, Layer-Adaptive Sparse Residual Composition (LASRC), and a higher-cost reliability-analysis layer for multi-view disagreement. LASRC addresses merge interference by preserving a linear anchor while residualizing block-wise adapter update directions. The reliability layer treats disagreement among sparse composition views as an observable uncertainty signal and compares agreement, support-loss proxy selection, and oracle headroom under explicit path cost. In matched FLAN-T5-Large, BIG-Bench Hard (BBH), and 97-LoRA experiments, LASRC gives a directional single-view gain under fixed retrieval, while SCALE-support is reported as a query-label-free 3.0* reliability-analysis variant rather than as a calibrated or throughput-equivalent selector. Protocol-distinct BBH-8 validation shows the same qualitative trend on three decoder-only backbones. Detailed scores, paired audits, and path-cost records are reported in the experimental section.

---


### 173. [Rethinking Explanations: Formalizing Contrast in Description Logics](https://arxiv.org/abs/2605.01442)

**<font color=#1a73e8>作者：</font>** Yasir Mahmood, Arnab Sharma, Axel-Cyrille Ngonga Ngomo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There has been a growing interest in explaining entailments over description logic (DL) knowledge bases. The existing explanation formalisms focus on justifications to explain true axioms, and abductive reasoning to explain missing axioms in a knowledge base. However, these formalisms only point out the reasoning steps behind a (missing) entailment and lack a user-centered approach as they do not consider an inquirer's needs, level of understanding, or prior knowledge. We propose contrastive explanations, aiming at answering "why an axiom P (fact) is true instead of another axiom Q (foil)" over description logic knowledge bases. The motivation arises from the observation that when a user discovers that P has occurred, they are often surprised because they anticipated the occurrence of another similar event Q. Furthermore, individual explanations for "why P" and "why not Q" are unsatisfactory since a user expects to see the difference between P and Q. In this work, we first present formal foundations of contrasting questions and then define contrastive explanations within description logics. To this end, facts include ABox assertions of the form C(x) for a concept C and individual x. Possible foils for such facts are assertions C(y) (contrasting against an individual y), or D(x) (contrasting against a concept D). Additionally, we explore the properties of contrastive explanations in the DL EL and ALC. We also provide an implementation of our definition and an experimental evaluation on KBs of varying sizes.

---


### 174. [Registration-Free Learnable Multi-View Capture of Faces in Dense Semantic Correspondence](https://arxiv.org/abs/2605.01450)

**<font color=#1a73e8>作者：</font>** Panagiotis P. Filntisis, George Retsinas, Radek Daněček 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent frameworks like ToFu and TEMPEH provide an automated alternative to classical registration pipelines by predicting 3D meshes in dense semantic correspondence directly from calibrated multi-view images. However, these learning-based methods rely on the slow, manual registration pipelines they aim to replace for their training supervision. We overcome this limitation with MOCHI (Multi-view Optimizable Correspondence of Heads from Images), a multi-view 3D face prediction framework trained without requiring registered training data. MOCHI eliminates the registration data dependency by enforcing topological consistency through a pseudo-linear inverse kinematic solver. Semantic alignment is guided by dense keypoints from a 2D landmark predictor trained exclusively on synthetic data. Our analysis further reveals that standard point-to-surface distances induce training instabilities and visual artifacts in registration-free settings. We propose pointmap- and normal-based losses instead, which provide smoother gradients and superior reconstruction fidelity. Finally, we introduce a test-time optimization scheme that refines network weights over a few dozen iterations. This approach bridges the gap between feed-forward efficiency and iterative optimization precision, allowing MOCHI to outperform traditional labor-intensive pipelines in both reconstruction accuracy and visual quality. Code and model are public at: this https URL.

---


### 175. [PQC Validator: Validating Post-Quantum Readiness in Cloud-Native 5G Core Networks](https://arxiv.org/abs/2605.01454)

**<font color=#1a73e8>作者：</font>** Lakshya Chopra, Vipin Kumar Rathi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> 5G Core networks are entering a decisive phase of post-quantum (PQ) migration: operators and vendors are beginning to advertise PQ-TLS 1.3, PQ-IPsec, and hybrid KEM support across the Service-Based Interface (SBI) and N2, N3, N4 reference points, in line with 3GPP TS 33.501, emerging IETF drafts, and NIST FIPS 203, 204, 205. Yet deploying PQ primitives does not guarantee PQ security. A Network Function may advertise ML-KEM-768 and silently fall back to X25519; negotiate a hybrid KEM but authenticate with ECDSA-P256; present an ML-DSA leaf on a classical chain; or skip mutual TLS altogether. These failures are silent on the wire, and today scanners (this http URL, sslyze, Qualys) together with 5G-specific fuzzers are PQ-unaware and telecom-blind. We present PQC Validator, a layered PQC assurance framework purpose-built for the cloud-native 5G Core, comprising a PQ Crypto Engine (L1), a PQ Conformance Prober (L2), a PQ Robustness Tester (L3), a PQ Overhead Meter (L4), and an eBPF Attestation Plane for wire-level ground truth. Its scope spans the full control-plane cryptographic surface: an independent PQ-TLS 1.3 client and server, a strongSwan-driven PQ-IPsec harness for N2/N3/N4, an eBPF/XDP/TC monitoring plane that extracts wire-level ground truth on negotiated groups and signatures, and a Kubernetes-native UI that auto-discovers NFs and emits structured PQ evidence classifying every endpoint as classical, hybrid-pq, or full-pq. A compliance suite spans TLS, PQC, 3GPP SBI, NRF OpenAPI, and security hardening, while a protocol fuzzer exercises CVE-class regressions and downgrade paths.

---


### 176. [CoFlow: Coordinated Few-Step Flow for Offline Multi-Agent Decision Making](https://arxiv.org/abs/2605.01457)

**<font color=#1a73e8>作者：</font>** Guowei Zou, Haitao Wang, Beiwen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models have emerged as a major paradigm for offline multi-agent reinforcement learning (MARL), but existing approaches require many iterative sampling steps. Recent few-step accelerations either distill a joint teacher into independent students or apply averaged velocities independently per agent, suggesting that few-step inference requires sacrificing inter-agent coordination. We show this trade-off is not necessary: single-pass multi-agent generation can preserve coordination when the velocity field is natively joint-coupled. We propose Coordinated few-step Flow (CoFlow), an architecture that combines Coordinated Velocity Attention (CVA) with Adaptive Coordination Gating. A finite-difference consistency surrogate further replaces memory-prohibitive Jacobian-vector product backpropagation through the averaged velocity field with two stop-gradient forward passes. Across 60 configurations spanning MPE, MA-MuJoCo, and SMAC, CoFlow matches or surpasses Gaussian / value-based, transformer, diffusion, and prior flow baselines on episodic return. Three independent coordination probes confirm that the gains flow through inter-agent coordination rather than per-agent capacity. A denoising-step sweep shows that single-pass inference suffices on every configuration. CoFlow reaches state-of-the-art coordination quality in 1-3 denoising steps under both centralized and decentralized execution. Project page: this https URL.

---


### 177. [SRGAN-CKAN: Expressive Super-Resolution with Nonlinear Functional Operators under Minimal Resources](https://arxiv.org/abs/2605.01459)

**<font color=#1a73e8>作者：</font>** Roberto Isai Navaro-Aviña, Eduardo Said Merin-Martinez, Andres Mendez-Vazquez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-Image Super-Resolution (SISR) aims to reconstruct a High-Resolution (HR) image from a Low-Resolution (LR) observation, a fundamentally ill-posed problem where high-frequency details are severely degraded at large upscaling factors. Recent advances have been driven by transformer-based architectures and diffusion models improve global context modeling and perceptual quality at the cost of increased computational complexity. In contrast, this work focuses on enhancing the expressivity of local operators under minimal resources. We propose SRGAN--CKAN, a hybrid super-resolution framework that integrates Convolutional Kolmogorov--Arnold Networks (CKAN) into an adversarial learning setting reformulating convolution as a nonlinear patch-based transformation. The proposed operator replaces linear local mappings with spline-based functional representations, allowing expressive modeling of complex local structures and high-frequency textures using minimal hardware resources. Experimental results demonstrate that the proposed approach improves perceptual quality while preserving reconstruction fidelity, achieving a favorable balance between distortion-based and perceptual metrics. These results are obtained under constrained computational settings, highlighting the efficiency of the proposed formulation. Overall, this work introduces a complementary direction to existing approaches by improving the representational power of local transformations, providing an efficient and scalable alternative to globally intensive architectures.

---


### 178. [SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion](https://arxiv.org/abs/2605.01466)

**<font color=#1a73e8>作者：</font>** Zhaoyang Li, Zhichao You, Tianrui Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although multi-modal learning has advanced point cloud completion, the theoretical mechanisms remain unclear. Recent works attribute success to the connection between modalities, yet we identify that standard hard projection severs this connection: projecting a sparse point cloud onto the image plane yields an extremely sparse support, which hinders visual prior propagation, a failure mode we term Cross-Modal Entropy Collapse. To address this practical limitation, we propose SplAttN, which replaces hard projection with Differentiable Gaussian Splatting to produce a dense, continuous image-plane representation. By reformulating projection as continuous density estimation, SplAttN avoids collapsed sparse support, facilitates gradient flow, and improves cross-modal connection learnability. Extensive experiments show that SplAttN achieves state-of-the-art performance on PCN and ShapeNet-55/34. Crucially, we utilize the real-world KITTI benchmark as a stress test for multi-modal reliance. Counter-factual evaluation reveals that while baselines degenerate into unimodal template retrievers insensitive to visual removal, SplAttN maintains a robust dependency on visual cues, validating that our method establishes an effective cross-modal connection. Code is available at this https URL.

---


### 179. [Decision Boundary-aware Generation for Long-tailed Learning](https://arxiv.org/abs/2605.01468)

**<font color=#1a73e8>作者：</font>** Jiacheng Yang, Ruichi Zhang, Chikai Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed data bias decision boundaries toward head classes and degrade tail class accuracy. Diffusion-based generative augmentation address this problem by generating additional data, while head-to-tail transfer further mitigate the generator bias inherit from long-tailed dataset. However, we show that while head-to-tail transfer helps balance the decision space of the classifier, it also induces latent non-local feature mixing that entangles inter-class features, causing decision boundary overlap and tail class distribution shift. To address this, we first identify the problem of boundary ambiguity and then propose Decision Boundary-aware Generation (DBG) framework, which promotes near-boundary representation learning by generating informative near-boundary samples. Overall, DBG rebalances the long-tailed dataset while yielding more separable decision space for long-tailed learning. Across standard long-tailed benchmarks, DBG consistently improves tail class and overall accuracy with less inter-class overlap. The code of DBG is available at this https URL.

---


### 180. [ReMedi: Reasoner for Medical Clinical Prediction](https://arxiv.org/abs/2605.01474)

**<font color=#1a73e8>作者：</font>** Yushi Cao, Yiming Chen, Hongchao Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predicting future clinical outcomes from electronic health records (EHR) remains challenging due to the complexity and heterogeneity of patient data. LLMs have shown strong potential for such predictive tasks, yet existing approaches mainly focus on enhancing medical knowledge through distillation or RAG while relying on the model's internal ability to interpret contextual information. In this work, we present ReMedi (Reasoner for Medical Clinical Prediction), a framework for improving clinical outcome prediction from EHR. ReMedi generates rationale-answer pairs using a challenging sample regeneration mechanism for complex clinical questions, which leverages ground-truth answers as hints to enhance reasoning for further fine-tuning and preference tuning. ReMedi integrates ground-truth outcome guidance into the preference data construction loop, regenerating rationale-answer variants. By tuning on these rationale-answer pairs, the model improves its predictive performance. Experiments on multiple EHR prediction tasks demonstrate substantial gains of up to 19.9 percent over state-of-the-art baselines in terms of F1 score, underscoring ReMedi's effectiveness in real-world clinical prediction.

---


### 181. [LIE: LiDAR-only HD Map Construction with Intensity Enhancement via Online Knowledge Distillation](https://arxiv.org/abs/2605.01478)

**<font color=#1a73e8>作者：</font>** Kanak Mazumder, Fabian B. Flohr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online High-Definition (HD) map construction is a key component of autonomous driving. Recent methods rely on multi-view camera images for cost-effective HD map segmentation, but cameras lack depth information for accurate scene geometry. In contrast, LiDAR provides precise 3D measurements but lacks dense semantic cues. In this work, we propose LIE, LiDAR-only semantic map construction method that employ Knowledge Distillation (KD) to handle the lack of dense semantic and texture cues. Specifically, the teacher branch fuses student LiDAR features and the corresponding 2D intensity map tile to provide dense supervision for segmenting map elements using online distillation scheme. Experimental results show that our method outperforms all single-modality approaches, achieving 8.2% higher mIoU than the state-of-the-art camera-based model on nuScenes. LIE is robust over long ranges and under challenging weather and lighting, and efficiently adapts to Argoverse2 with only 10% fine-tuning, surpassing camera-based models trained on the full dataset. Source code will be available \href{this https URL}{here}.

---


### 182. [CSGuard: Toward Forgery-Resistant Watermarking in Diffusion Models via Compressed Sensing Constraint](https://arxiv.org/abs/2605.01479)

**<font color=#1a73e8>作者：</font>** Jiewei Lai, Lan Zhang, Chen Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent-based diffusion model watermarking embeds watermarks into generated images' latent space to enable content attribution, offering a training-free solution for intellectual property protection and digital forensics. However, these methods exhibit a critical vulnerability to the forgery attack, attackers can extract the watermark by inverting the watermarked image and re-generating it with an arbitrary prompt, thereby enabling false attribution on malicious content. In this paper, we propose the CSGuard, the first forgery-resistant watermarking schema that leverages compressed sensing to bind the watermarked image generation and verification to a secret matrix. This ensures that only users possessing the secret matrix can correctly embed or verify the image watermark, prevents the illegal users from forgery without compromising generation quality and watermark integrity. Experimental results demonstrate that CSGuard achieves strong forgery resistance, reduces the attack success rate from 100.0\% to 28.12\%, and achieve 100\% detection rate on benign watermarked images without compromising watermarking effectiveness.

---


### 183. [AttnRouter: Per-Category Attention Routing for Training-Free Image Editing on MMDiT](https://arxiv.org/abs/2605.01480)

**<font color=#1a73e8>作者：</font>** Guandong Li, Mengxia Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study training-free image editing on Qwen-Image-Edit-2511, a 60-block multi-modal diffusion transformer (MMDiT) that concatenates noise and source-image tokens within a single attention stream. We make three contributions. (i) We introduce KVInject, a single-forward attention manipulation that alpha-blends source-half key/value projections into the noise-half within a localized layer/step band. KVInject is simpler than the classical two-pass MasaCtrl recipe and avoids the prompt-mismatch failure mode that disables MasaCtrl on MMDiT (composite score drops 31% versus baseline). (ii) We show that no single attention operation dominates across edit types, motivating AttnRouter, a per-category routing table that dispatches edits to the operation that best preserves source structure for that type. With ground-truth categories the router improves the CLIP-T+DINO-I composite by 6.4% over the editing baseline; an automatic CLIP zero-shot classifier closes 98% of this gap despite only 55% category accuracy. (iii) Through layer-, step-, and alpha-band ablations we localize the editing-effective attention sub-circuit: K/V injection in early denoising steps (S0-7) recovers nearly all of the gain of full-step injection, while injection in early (L0-15) or late (L45-60) layer bands fails to drive editing entirely; alpha in [0.3, 0.5] is a stable sweet spot. We also report negative results that highlight what does not transfer from the UNet folklore: simple K/V rescaling never beats baseline and aggressive variants collapse generation entirely (composite 0.084). We release code, pre-computed routing tables, and a 100-sample stratified subset of ImgEdit-Bench used in all ablations.

---


### 184. [Grounding Multi-Hop Reasoning in Structural Causal Models via Group Relative Policy Optimization](https://arxiv.org/abs/2605.01482)

**<font color=#1a73e8>作者：</font>** Yunhan Bu, Quan Zhang, Huaping Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Hop Fact Verification (MHFV) necessitates complex reasoning across disparate evidence, posing significant challenges for Large Language Models (LLMs) which often suffer from hallucinations and fractured logical chains. Existing methods, while improving transparency via Chain-of-Thought (CoT), lack explicit modeling of the causal dependencies between evidence and claims. In this work, we introduce a novel framework that grounds reasoning in a Structural Causal Model (SCM), treating verification as a constructive causal inference process. We empirically identify an "inverted U-shaped" correlation between reasoning chain length and accuracy, revealing that excessive structural complexity degrades performance. To address this, we propose a Rule-based Reinforcement Learning strategy using Group Relative Policy Optimization (GRPO). This approach dynamically optimizes the trade-off between structural depth and conciseness. Extensive experiments on HoVer and EX-FEVER demonstrate that our SCM-GRPO framework significantly outperforms state-of-the-art baselines, offering a reliable and interpretable solution for complex fact verification.

---


### 185. [Research on Vision-Language Question Answering Models for Industrial Robots](https://arxiv.org/abs/2605.01483)

**<font color=#1a73e8>作者：</font>** Ping Li, Bartlomiej Brzozka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A hierarchical cross-modal fusion model is proposed for vision-language question answering (VLQA) in industrial robotics, targeting the challenges of semantic ambiguity, complex environmental layouts, and domain-specific terminology common in modern manufacturing. The framework integrates advanced object detection, multi-scale visual encoding, syntactic parsing, and task-aware semantic attention to unite vision and language signals into a joint reasoning space. Region-based deep networks extract visual features, weighted embeddings aggregate, and recurrent neural parsing encodes sentence structures. Through fine-grained semantic alignment driven by adaptive fusion and cross-attention mechanisms, the system can handle operational queries, instruction steps, and anomaly detection with higher reliability. Compared to the existing VLQA benchmarks, validation experiments conducted on the IVQA and RIF benchmarks indicate improvements in semantic alignment, Top-1 accuracy, and robustness to ambiguous or procedural task queries. Ablation studies further quantify the impact of each architectural module, confirming the necessity of multi-level feature integration and context-driven gating for dependable industrial deployment. The technical advancements reported here provide core methodologies to improve the interpretability and operational effectiveness of industrial robots faced with diverse human-robot interaction tasks.

---


### 186. [CGFformer: Cluster-Guidance Frequency Transformer for Pansharpening](https://arxiv.org/abs/2605.01490)

**<font color=#1a73e8>作者：</font>** Zijian Zhou, Jianing Zhang, Kai Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) images with high-resolution panchromatic (PAN) images. However, the current mainstream frequency-based pansharpening methods employ fixed frequency filters, which cannot precisely adapt to complex and spatially diversified frequency distributions in PAN and MS images. Furthermore, existing denoising strategies insufficiently exploit frequency components for denoising and struggle to suppress various noise types accurately. To address these challenges, we propose CGFformer, a cluster-guidance frequency Transformer that focuses on varying frequency distribution and interactions between frequency and spatial components. Specifically, we design an adaptive separation module that integrates local features and non-local information through K-means clustering, enabling more precise separation of high- and low-frequency components. Subsequently, we introduce a dual-stream refinement module combined with Transformer-based cross-attention to remove various noise, allowing the network to jointly suppress frequency-relevant and irrelevant disturbances. In addition, we develop a frequency-spatial fusion module designed to enhance detail and facilitate spatial-frequency interaction, ensuring more effective reconstruction of spatial structures in the fused results. Extensive experiments on multiple benchmark datasets demonstrate that the proposed CGFformer achieves notable improvements over existing pansharpening approaches.

---


### 187. [SF20K Competition 2025: Summary and findings](https://arxiv.org/abs/2605.01496)

**<font color=#1a73e8>作者：</font>** Ridouane Ghermi, Xi Wang, Vicky Kalogeiton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents the results and findings of the first edition of the Short-Films 20K (SF20K) Competition, held in conjunction with the SLoMO Workshop at ICCV 2025. The competition is designed to advance story-level video understanding beyond short-clip action recognition, introducing an open-ended video question-answering task built on a corpus of amateur short films. This setup ensures that models must rely on multimodal understanding rather than memorization of popular movies. Evaluation is conducted using the SF20K-Test benchmark (95 movies, 979 question-answer pairs) and scored via LLM-QA-Eval, an automated judge based on GPT-4.1-nano. The competition attracted 22 teams and 286 submissions across two tracks: a Main Track with unrestricted model size and a Special Track limited to models under 8 billion parameters. The winning team achieved 65.7% accuracy on the Main Track and 48.7% on the Special Track, against a human performance ceiling of 91.7%. Our analysis reveals several key findings: narrative-aware, shot-level processing consistently outperforms uniform frame sampling; well-designed multi-stage pipelines using smaller models can match or exceed end-to-end inference with models over 30x larger; and subtitle quality is a dominant factor in performance. These results highlight that the primary bottleneck in long-form video QA lies in information selection and reasoning structure rather than raw model capacity, and that a substantial gap remains between current methods and human-level narrative comprehension.

---


### 188. [Towards Visual Query Localization in the 3D World](https://arxiv.org/abs/2605.01498)

**<font color=#1a73e8>作者：</font>** Liang Peng, Bohan Tan, Zhipeng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual query localization (VQL) aims to predict the spatio-temporal response of the most recent occurrence in a sequence given a query. Currently, most research focuses on visual query localization in 2D videos, while its counterpart in 3D space has received little attention. In this paper, we make the first attempt to address visual query localization in the 3D world by introducing a novel benchmark, dubbed 3DVQL. Specifically, 3DVQL contains 2,002 sequences with around 170,000 frames and 6.4K response track segments from 38 object categories. Each sequence in 3DVQL is provided with multiple modalities, including point clouds, RGB images, and depth images, to support flexible research. To ensure high-quality annotations, each sequence is manually annotated with multiple rounds of verification and refinement. To the best of our knowledge, 3DVQL is the first benchmark for 3D multimodal visual query localization. To facilitate comparison in subsequent research, we implement a series of representative 3D multimodal VQL baselines using point clouds and RGB images. The experimental results show that existing methods exhibit significant performance variations across different fusion modules. To encourage future research, we propose a lift-and-attention fusion algorithm named LaF, which significantly outperforms existing baseline models. Our benchmark and model will be publicly released at this https URL.

---


### 189. [RADMI: Latent Information Aggregation as a Proxy for Model Uncertainty](https://arxiv.org/abs/2605.01502)

**<font color=#1a73e8>作者：</font>** William Stevens, Mohit Prabhushankar, Ghassan AlRegib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Epistemic uncertainty estimation is essential for identifying regions where deep learning system outputs may be unreliable. However, existing approaches require computationally expensive ensemble methods or multiple stochastic forward passes, limiting their scalability to dense prediction tasks like segmentation. We propose Resolution-Aggregated Decoder Mutual Information (RADMI), a single-pass method that estimates prediction uncertainty by measuring mutual information (MI) between consecutive decoder layers in segmentation networks. We observe that elevated inter-layer MI correlates with prediction uncertainty, as the network must integrate conflicting contextual information at ambiguous regions such as class boundaries. Evaluating on a seismic facies segmentation benchmark, RADMI achieves the highest correlation with deep ensemble uncertainty among all single-pass methods, outperforming the next-best baselines by 5.5% in Pearson and 10.7% in Spearman correlation coefficients. Compared to baselines that either lack spatial precision or demand significant computational overhead, RADMI yields sharp, boundary-localized uncertainty maps without architectural modifications. Our results suggest that linear aggregation of normalized information flow provides a principled and efficient proxy for prediction uncertainty in encoder-decoder architectures.

---


### 190. [SwiftPie: Lightning-fast Subject-driven Image Personalization via One step Diffusion](https://arxiv.org/abs/2605.01510)

**<font color=#1a73e8>作者：</font>** Huy Duong, Trong-Tung Nguyen, Cuong Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in high-quality image synthesis, sparking interest in image-guided generation tasks such as subject-driven image personalization. Despite their impressive personalization results, existing methods typically rely on computationally intensive fine-tuning, iterative optimization, or multi-step denoising processes, which significantly hinder their deployment and interactive capability in real-time applications. In this work, we present SwiftPie, the first one-step diffusion image personalization tool that enables lightning-fast generation of personalized images. SwiftPie introduces a novel dual-branch identity injection mechanism that effectively integrates subject identity into a one-step diffusion model. In addition, we incorporate a mask-guided rescaling strategy to further enhance subject contextualization within a single diffusion step. Extensive experiments demonstrate that SwiftPie not only delivers superior image personalization speed but also achieves comparable performance with multi-step approaches in both identity fidelity and prompt alignment. This work opens new opportunities for real-time, high-quality personalized image generation, paving the way for interactive visual synthesis.

---


### 191. [Protein-Conditioned Multi-Objective Reinforcement Learning for Full-Length mRNA Design](https://arxiv.org/abs/2605.01513)

**<font color=#1a73e8>作者：</font>** Zixi Shao, Tao Wang, Yibei Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing therapeutic messenger RNA (mRNA) requires creating full-length transcripts that carefully balance stability, translation efficiency, and immune safety. To address this challenge, we propose ProMORNA, a multi-objective generation framework that produces complete mRNA transcripts \textit{de novo} directly from a target protein sequence. Our approach begins by training a BART-style encoder-decoder model on over 6 million natural protein-mRNA pairs. We then introduce Multi-Objective Group Relative Policy Optimization (MO-GRPO) to simultaneously optimize for various biological objectives in a unified way. As a case study, we evaluated ProMORNA on the widely used firefly luciferase target, excluding it from both our supervised training data and the prompt pool. The results indicate that ProMORNA improves the \textit{in silico} Pareto frontier for predicted half-life and translation efficiency relative to standard supervised baselines. Additionally, it achieves higher predicted functional scores than a state-of-the-art baseline under the same evaluation pipeline. These computational findings demonstrate the feasibility of using multi-objective reinforcement learning for full-length mRNA design on unseen targets.

---


### 192. [VAnim: Rendering-Aware Sparse State Modeling for Structure-Preserving Vector Animation](https://arxiv.org/abs/2605.01517)

**<font color=#1a73e8>作者：</font>** Guotao Liang, Zhangcheng Wang, Chuang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable Vector Graphics (SVG) animation generation is pivotal for professional design due to their structural editability and resolution independence. However, this task remains challenging as it requires bridging discrete code representations with continuous visual dynamics. Existing optimization-based methods often destroy topological consistency, while general-purpose LLMs rely on rigid CSS/SMIL transformations, failing to model geometry-level non-rigid deformations. To address these limitations, we present VAnim, the first LLM-based framework for open-domain text-to-SVG animation. We reconceptualize animation not as sequence generation, but as Sparse State Updates (SSU) on a persistent SVG DOM tree. This paradigm compresses sequence length by over 9.8x while preserving the SVG DOM structure and non-participating elements by construction. To enable precise control, we propose an Identification-First Motion Planning mechanism that grounds textual instructions in explicit visual entities. Furthermore, to overcome the non-differentiable nature of SVG rendering, we employ Rendering-Aware Reinforcement Learning via Group Relative Policy Optimization (GRPO). By leveraging a hybrid reward from a state-of-the-art video perception encoder, we align discrete code updates with high-fidelity visual feedback. We also introduce SVGAnim-134k, the first benchmark for vector animation. Extensive experiments demonstrate that VAnim significantly outperforms state-of-the-art baselines in semantic alignment and structural validity, with additional appendix metrics further validating motion quality and identity preservation.

---


### 193. [Certified vs. Empirical Adversarial Robust-ness via Hybrid Convolutions with Attention Stochasticity](https://arxiv.org/abs/2605.01519)

**<font color=#1a73e8>作者：</font>** Joy Dhar, Song Xia, Manish Kumar Pandey 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Hybrid Convolutions with Attention Stochasticity (HyCAS), an adversarial defense that narrows the long-standing gap between provable robustness under L2 certificates and empirical robustness against strong L attacks, while preserving strong generalization across diverse imaging benchmarks. HyCAS unifies deterministic and randomized principles by coupling 1-Lipschitz, spectrally normalized convolutions with two stochastic components, spectral normalized random, projection filters and a randomized attention-noise mechanism, to realize a randomized defense. Injecting smoothing randomness inside the architecture yields an overall <= 2-Lipschitz network with formal certificates. Exten-sive experiments on diverse imaging benchmarks, including CIFAR-10/100, ImageNet-1k, NIH Chest X-ray, HAM10000, show that HyCAS surpasses prior leading certified and empirical defenses, boosting certified accuracy by up to 7.3% (on NIH Chest X-ray) and empirical robustness by up to 3.1% (on HAM10000), without sacrificing clean accuracy. These results show that a randomized Lipschitz constrained architecture can simultaneously improve both certified L2 and empirical L adversarial robustness, thereby supporting safer deployment of deep models in high-stakes applications. Code: this https URL

---


### 194. [The grip of grammar on meaning uncertainty: cross-linguistic evidence, neural correlates, and clinical relevance](https://arxiv.org/abs/2605.01537)

**<font color=#1a73e8>作者：</font>** Rui He, Claudio Palominos, Samuele Vallisa 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Isolated word meanings are inherently uncertain. This uncertainty reduces when they are combined and anchored in context. We propose that grammar compresses meaning uncertainty cross-linguistically, which is reflected in brain and selectively disrupted in disorders. Compression was operationalized as the relative difference between non-contextual surprisal estimated from lexical frequency, and contextual surprisal from grammar-sensitive models. In narratives from 20 languages, contextual surprisal reduced frequency-based surprisal. This reduction closely tracked the surprisal cost of reversing word order, and scaled with richer, non-redundant lexis as organized by more complex but optimal dependency structure. During fMRI, surprisal and its reduction explained BOLD activity for comprehension and production in overlapping but distinct regions. Uncertainty reduction was significantly attenuated in aphasia, dementia, and schizophrenia, but remained intact where primary deficit is not language. These findings position uncertainty reduction via grammar as a foundational concept that illuminates principles, brain basis, and disruptions of language.

---


### 195. [Mesh Based Simulations with Spatial and Temporal awareness](https://arxiv.org/abs/2605.01542)

**<font color=#1a73e8>作者：</font>** Paul Garnier, Vincent Lannelongue, Elie Hachem  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning surrogates for Computational Fluid Dynamics (CFD), particularly Graph Neural Networks (GNNs) and Transformers, have become a new important approach for accelerating physics simulations. However, we identify a critical bottleneck in the field: while architectures have advanced significantly, the common underlying training paradigms remain bound to naive assumptions, such as node-wise supervision and explicit Euler time-stepping. These legacy choices ignore the stiff dynamics and local flux continuity inherent to numerous partial differential equations resolution methods, such as Finite Element, Difference, or Volume (FEM). In this work, we propose a unified framework to bridge the gap between geometric deep learning and rigorous numerical analysis. We introduce three key innovations: (1) Multi Node Prediction, a stencil-level objective that predicts field values for a node's full local topology, enforcing spatial derivative consistency; (2) Temporal Correction, replacing unstable explicit schemes with a predictor-corrector via temporal Cross-Attention; and (3) Geometric Inductive Biases, leveraging 3D Rotary Positional Embeddings (RoPE) to robustly capture rotational symmetries in unstructured meshes. We evaluate this framework across three architectures (MeshGraphNet, Transolver, and a Transformer) on diverse physics datasets. Our approach yields consistent improvements in accuracy and stability, particularly in long-horizon rollouts, while producing latent representations that generalize to unseen subtasks such as Wall Shear Stress or Pressure prediction. Code is available at this https URL.

---


### 196. [ECG-biometrics-bench: A Unified Framework for Reproducible Benchmarking of ECG Biometrics](https://arxiv.org/abs/2605.01548)

**<font color=#1a73e8>作者：</font>** Milad Parvan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) biometrics have emerged as a promising modality for continuous, liveness-aware authentication in wearable systems. However, many prior studies report overly optimistic results due to data leakage (e.g., random splits within the same session). To address this issue, we introduce ECG-biometrics-bench, a modular, reproducible benchmarking framework that standardizes preprocessing, segmentation, and evaluation across seven widely used public ECG datasets spanning clinical, ambulatory, and large-scale cohort settings. The framework supports both closed-set and open-set (i.e., subject-disjoint generalization in this work) evaluation, as well as progressively realistic protocols including cross-session and long-term temporal separation. To facilitate reproducible research in the community, the ECG-biometrics-bench repository will be made publicly accessible on GitHub upon the acceptance of this manuscript. Through a comprehensive multi-dataset analysis, we expose the Random Split Fallacy, demonstrating that intra-session evaluation protocols artificially inflate performance while masking severe degradation caused by temporal drift and unseen identities. Furthermore, by evaluating multiple architectures, including DeepECG, ResNet1D, and CNN-LSTM, we show that these failures are not model-specific but are likely inherent to current supervised feature-learning paradigms. Finally, we demonstrate that performance degradation due to temporal aging can be partially mitigated through a heavy enrollment, lightweight authentication strategy based on dynamic multi-session template fusion. These findings establish a more realistic baseline for ECG biometrics and highlight critical challenges that must be addressed for reliable real-world deployment.

---


### 197. [Robust Fundamental Matrix Estimation from Single Image Motion Blur](https://arxiv.org/abs/2605.01552)

**<font color=#1a73e8>作者：</font>** Bao-Long Tran, Per-Erik Forssén, Fredrik Viksten  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce a challenging task: extracting a fundamental matrix from a single motion blurred image. For a camera moving in 3D during exposure, the smear paths in the blurry image contain cues and constraints on this motion. We demonstrate the feasibility of establishing correspondences between two time instances within the camera exposure window, and that these can be used to robustly infer a fundamental matrix, which summarizes the motion of the camera during the exposure time. The inferred fundamental matrix is unique up to a transpose, corresponding to an ambiguity of the direction of time. Due to this per-smear ambiguity, classic methods, such as the 8-point algorithm, are no longer usable. The proposed method modifies the estimation to work on time-direction ambiguous correspondences. To improve the robustness of the fundamental matrix estimation, we also propose to incorporate an uncertainty measurement in smear pattern prediction and use it in the sampling process of the estimator. Experiments on synthetic and real-world motion-blur datasets demonstrate that our approach is able to estimate the fundamental matrix encoding the 3D camera motion, from single frames. Practical applicability is demonstrated on the downstream task of motion segmentation.

---


### 198. [Multi-Dataset Cross-Domain Knowledge Distillation for Unified Medical Image Segmentation, Classification, and Detection](https://arxiv.org/abs/2605.01563)

**<font color=#1a73e8>作者：</font>** Ceausescu Ciprian-Mihai, Anghelina Ion-Marian, Alexe Dumitru-Bogdan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a unified cross-domain transfer learning framework that leverages knowledge from multiple heterogeneous medical imaging datasets to improve performance across segmentation, classification, and object detection tasks. Our approach employs a teacher-student paradigm in which a joint teacher model aggregates domain-invariant representations learned from diverse source datasets, while a task-specific student model is trained via multi-level knowledge distillation. Originally developed for medical image segmentation, the framework is extended to support image-level classification and object-level detection, enabling a general multi-task formulation for medical image analysis. We evaluate our method on a broad suite of datasets, including six segmentation benchmarks, BrainMetShare, ISLES, BraTS (MRI) and Lung MSD, LiTS, KiTS (CT), as well as multiple classification datasets for pulmonary disease and dementia, and detection datasets with native bounding-box annotations. Across all tasks and modalities, the proposed approach yields consistent improvements over strong dataset-specific and multi-head baselines, demonstrating enhanced robustness to distributional shifts and superior generalization. These findings highlight the potential of multi-dataset knowledge distillation as a scalable and task-agnostic approach for enhancing segmentation, classification, and object detection performance across heterogeneous medical imaging domains.

---


### 199. [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/abs/2605.01566)

**<font color=#1a73e8>作者：</font>** Florian Valentin Wunderlich, Lars Benedikt Kaesberg, Jan Philip Wahle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in inference methods have enabled language models to improve their predictions without additional training. These methods often prioritize raw performance over cost-effective compute usage. However, computational efficiency is key for real-world applications with resource constraints. We provide a systematic analysis of the inference scaling strategies self-consistency, self-refinement, multi-agent debate, and mixture-of-agents, to study their computational performance tradeoffs. We evaluate methods on two reasoning benchmarks (MMLU-Pro, BBH) and include extensive parameter configurations (e.g., scaling the number of parallel predictions, agents, and debate rounds) across different model sizes. Across 34 configurations and over 100 evaluations, we compute the Pareto-optimal front to select methods that achieve the best accuracy with the lowest computational budget. Notably, inference scaling improves accuracy by up to +7.1% points over chain-of-thought at the highest evaluated budgets (20x the CoT compute budget) on MMLU-Pro. With an equal computing budget, debate and mixture-of-agents outperform self-consistency by 1.3% and 2.7% points, respectively. While self-consistency saturates earlier, multi-agent gains persist, particularly on more complicated tasks. We identify a simple multi-agent design guideline: mixture-of-agents is most efficient when the number of parallel generations exceeds the number of sequential aggregations.

---


### 200. [Unifying Deep Stochastic Processes for Image Enhancement](https://arxiv.org/abs/2605.01568)

**<font color=#1a73e8>作者：</font>** Wojciech Kozłowski, Radosław Kuczbański, Kamil Adamczewski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep stochastic processes have recently become a central paradigm for image enhancement, with many methods explicitly conditioning the stochastic trajectory on the degraded input. However, the relationship between these conditional processes and standard diffusion models remains unclear. In this work, we introduce a unified perspective on stochastic image enhancement by classifying recent methods into three families of continuous-time processes: unconditional diffusion models, Ornstein-Uhlenbeck (OU) processes, and diffusion bridges. We show that all of these approaches arise from a common stochastic differential equation (SDE) formulation. This framework makes explicit that seemingly disparate methods differ primarily in their drift and diffusion terms, terminal distributions, and boundary conditions, while schedulers and samplers constitute orthogonal design choices. Leveraging this unification, we conduct a controlled empirical study across multiple image enhancement tasks using identical architectures and training protocols. Our results reveal no consistently dominant method; instead, we identify and disentangle the specific design choices that most strongly influence performance. Finally, we release ItoVision, a modular PyTorch library that implements the unified framework and enables rapid prototyping and fair comparison of stochastic image enhancement methods.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
