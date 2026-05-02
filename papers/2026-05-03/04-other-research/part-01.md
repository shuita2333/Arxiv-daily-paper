# 📦 其他研究 | 2026年05月03日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 1. [C8s: A Confidential Kubernetes Architecture](https://arxiv.org/abs/2604.26974)

**<font color=#1a73e8>作者：</font>** Amean Asad, Patrick McClurg, João Andrade  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents C8s, a confidential computing architecture for Kubernetes that provides cryptographically rooted confidentiality, integrity, and verifiability guarantees for Kubernetes clusters from infrastructure operators. These guarantees are cryptographically provable to any independent third party verifier. The architecture is built on hardware Trusted Execution Environments (TEEs), specifically AMD SEV-SNP, Intel TDX, and NVIDIA Confidential Computing support, to establish an attestation-rooted trust boundary around confidential VMs. This design is compatible with managed Kubernetes services such as Amazon EKS, Google GKE, and Microsoft AKS, where the control plane cannot be attested. Under this boundary, three groups gain guarantees that are absent from conventional deployments. Data and artifact owners can deploy sensitive workloads and proprietary artifacts on third-party infrastructure without risking exfiltration. Compute providers can offer execution services without revealing workloads to cloud operators. End users can submit requests that remain opaque to all parties except the attested TEE processing them. Representative workloads include AI inference, securing AI model weights, and training or fine-tuning on sensitive data.

---


### 2. [Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index](https://arxiv.org/abs/2604.26984)

**<font color=#1a73e8>作者：</font>** Alexander Kalinowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representational collapse, where embeddings become anisotropic and lose multi-scale structure, can erode downstream performance long before performance metrics react. We propose an online, topology-aware monitor for evolving neural representations that couples Modular Morse Homology Maintenance (MMHM) with a composite Collapse Index (CI). Instead of rebuilding complexes each epoch, we apply sparse edits at a fixed scale and maintain a discrete Morse matching, yielding fast, incremental updates. Across LLM fine-tuning and temporal KGE training, CI provides a low-latency early-warning signal suitable for in-training interventions. Code and experimental scripts will be released publicly

---


### 3. [Simple Self-Conditioning Adaptation for Masked Diffusion Models](https://arxiv.org/abs/2604.26985)

**<font color=#1a73e8>作者：</font>** Michael Cardei, Huu Binh Ta, Ferdinando Fioretto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) generate discrete sequences by iterative denoising under an absorbing masking process. In standard masked diffusion, if a token remains masked after a reverse update, the model discards its clean-state prediction for that position. Thus, still-masked positions must be repeatedly inferred from the mask token alone. This design choice limits cross-step refinement. To address this limitation, this paper proposes a simple, yet effective, post-training adaptation for MDMs that conditions each denoising step on the model's own previous clean-state predictions. The resulting method, called Self-Conditioned Masked Diffusion Models (SCMDM), requires minimal architectural change, does not introduce a recurrent latent-state pathway, does not rely on an auxiliary reference model, and adds no extra denoiser evaluations during sampling. This is an important departure from partial self-conditioning approaches which requires expensive model training from scratch. In particular, the paper shows that partial self-conditioning, including the commonly used 50% dropout strategy for training self-conditioned models from scratch, is suboptimal in the post-training regime. Instead, once the model's self-generated clean-state estimates become informative, the specialization to refinement is preferable to mixing conditional and unconditional objectives. SCMDM is evaluated across multiple domains, demonstrating consistent improvement over vanilla MDM baselines, achieving nearly a 50% reduction in generative perplexity on OWT-trained models (42.89 to 23.72), alongside strong improvements in discretized image synthesis quality, small molecular generation, and enhanced fidelity in genomic distribution modeling.

---


### 4. [People-Centred Medical Image Analysis](https://arxiv.org/abs/2604.26991)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Milad Masroor, Cuong Nguyen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in data-centric medical AI have produced highly accurate diagnostic systems, but the emphasis on data curation and performance metrics has not translated into widespread clinical adoption. We conjecture that this limited uptake stems from insufficient attention dedicated to the optimisation of fair performance across diverse patient populations and to workflow integration: performance biases can create regulatory barriers, and poorly integrated automation can disrupt clinical routines, degrade the quality of human-AI collaboration, and reduce clinicians' willingness to adopt AI tools. Prior work on workflow integration (e.g., Learning to Defer (L2D) and Learning to Complement (L2C)) and AI fairness has typically examined these challenges in isolation, overlooking their natural interdependence and the practical constraints of clinical environments, such as restricted clinician availability. We propose People-Centred Medical Image Analysis (PecMan), a human-AI framework that jointly optimises fairness, diagnostic accuracy, and workflow effectiveness through a dynamic gating mechanism that assigns cases to AI, clinicians, or both under clinician workload constraints. We also introduce the Fairness and Human-Centred AI (FairHAI) benchmark for evaluating trade-offs between accuracy, fairness, and clinician workload. Experiments using this benchmark show that PecMan consistently outperforms existing methods, paving the way for more trustworthy and clinically viable AI systems. Code will be available upon paper acceptance.

---


### 5. [Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes](https://arxiv.org/abs/2604.26997)

**<font color=#1a73e8>作者：</font>** Akshay Mittal, Elyson De La Cruz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agent ecosystems require stronger mechanisms for secure discovery, identity verification, capability attestation, and policy governance. Current deployments frequently lack (1) uniform agent discovery, (2) cryptographic agent authentication, (3) capability proofs that protect secrets, and (4) enforceable policy controls. This paper presents an implementation-oriented proof of concept for the Agent Name Service (ANS), a DNS-inspired trust layer for AI agent discovery and interoperability in Kubernetes, grounded in the ANS protocol specification~\cite{huang2025ans}. The implementation uses Decentralized Identifiers (DIDs), Verifiable Credentials (VCs), policy-as-code enforcement with Open Policy Agent (OPA), and Kubernetes-native integration patterns (CRDs, admission controls, service mesh integration). In a demo research environment (3-node cluster, 50-agent workflow simulation), we observe sub-10ms response in demonstrated service paths and full success for scripted demo deployment scenarios. We explicitly scope these findings as proof-of-concept evidence rather than production certification. We further provide a threat model, assumptions, and limitations to separate implemented evidence from protocol-defined and roadmap capabilities. The result is an evidence-grounded pathway from ANS protocol concepts to reproducible engineering practice for secure multi-agent systems.

---


### 6. [Compositional Meta-Learning for Mitigating Task Heterogeneity in Physics-Informed Neural Networks](https://arxiv.org/abs/2604.26999)

**<font color=#1a73e8>作者：</font>** Beomchul Park, Minsu Koh, Heejo Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) approximate solutions of partial differential equations (PDEs) by embedding physical laws into the loss function. In parameterized PDE families, variations in coefficients or boundary/initial conditions define distinct tasks. This makes training individual PINNs for each task computationally prohibitive, while cross-task transfer can be sensitive to task heterogeneity. While meta-learning can reduce retraining cost, existing methods often rely on a single global initialization and may suffer from negative transfer, particularly under feature-scarce coordinate inputs and limited training-task availability. We propose the Learning-Affinity Adaptive Modular Physics-Informed Neural Network (LAM-PINN), a compositional framework that leverages task-specific learning dynamics. LAM-PINN combines PDE parameters with learning-affinity metrics from brief transfer sessions to construct a task representation and cluster tasks even with coordinate-only inputs. It decomposes the model into cluster-specialized subnetworks and a shared meta network, and learns routing weights to selectively reuse modules instead of relying on a single global initialization. Across three PDE benchmarks, LAM-PINN achieves an average 19.7-fold reduction in mean squared error (MSE) on unseen tasks using only 10% of the training iterations required by conventional PINNs. These results indicate its effectiveness for generalization to unseen configurations within bounded design spaces of parameterized PDE families in resource-constrained engineering settings.

---


### 7. [Binary Spiking Neural Networks as Causal Models](https://arxiv.org/abs/2604.27007)

**<font color=#1a73e8>作者：</font>** Aditya Kar, Emiliano Lorini, Timothée Masquelier  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We provide a causal analysis of Binary Spiking Neural Networks (BSNNs) to explain their behavior. We formally define a BSNN and represent its spiking activity as a binary causal model. Thanks to this causal representation, we are able to explain the output of the network by leveraging logic-based methods. In particular, we show that we can successfully use a SAT as well as a SMT solver to compute abductive explanations from this binary causal model. To illustrate our approach, we trained the BSNN on the standard MNIST dataset and applied our SAT-based and SMT-based methods to finding abductive explanations of the network's classifications based on pixel-level features. We also compared the found explanations against SHAP, a popular method used in the area of explainable AI. We show that, unlike SHAP, our approach guarantees that a found explanation does not contain completely irrelevant features.

---


### 8. [Quantifying the Cost of Manual Navigation: A Comparison of Gesture-Based Magnification versus Direct Access Reading in Digital Layout-based Documents](https://arxiv.org/abs/2604.27010)

**<font color=#1a73e8>作者：</font>** Sebastián Gallardo, Hui-Yin Wu, Dorian Mazauric 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how diverse audiences engage with structured media is critical to ensure a consistent quality of experience. In this context, we quantify the behavioral and performance cost of manual navigation (e.g., pinch and zoom) versus direct structural access in layout-based digital documents. We specifically investigate newspaper reading when visual access to structural cues (headlines as entry points) is constrained. Participants completed two tasks-reading all headlines aloud and locating target articles-under two conditions: (1) original edition with gesture-based magnification (pan and zoom), which is the industry standard for digital documents, and (2) large-print edition supporting direct-access reading. We collected performance measures (success ratio and completion time), behavioral integrity through reading path analysis, alongside perceived workload and preferences (NASA-TLX). Results from linear mixed-effects models show that the large-print condition yielded not only better performance than gesture-based magnification (18% improvement in reading speed, 30% improvement in speed to locate a target), but more importantly, restored the natural reading strategy that gesture-based magnification interaction disrupts. Readers also reported lower workload and higher preference. These findings highlight the importance of developing automated methods for generating large-print editions, where layout adaptation complements font scaling to support accessibility and quality of experience.

---


### 9. [NORACL: Neurogenesis for Oracle-free Resource-Adaptive Continual Learning](https://arxiv.org/abs/2604.27031)

**<font color=#1a73e8>作者：</font>** Karthik Charan Raghunathan, Christian Metzner, Laura Kriener 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a continual learning setting, we require a model to be plastic enough to learn a new task and stable enough to not disturb previously learned capabilities. We argue that this dilemma has an architectural root. A finite network has limited representational and plastic resources, yet the required capacity depends on properties of the future task stream that are unknown: how many tasks will be encountered, and how much they overlap in feature space. Regularization-based methods preserve past knowledge within fixed-capacity architectures and therefore implicitly rely on an oracle architecture sized for this unknown future. When tasks are only weakly related, fixed architectures progressively run out of plastic resources; when tasks are few or strongly overlapping, models are often over-provisioned. Inspired by neurogenesis in biology, we propose NORACL to address the stability-plasticity dilemma by tackling the oracle architecture problem through neuronal growth. Starting from a compact network, NORACL grows only when needed by monitoring two complementary signals for representational and plasticity saturation. We evaluate NORACL against oracle-sized static baselines across varying task counts and geometries. Across all settings, NORACL achieves final average accuracies that are better than or on par with oracle-provisioned static baselines while using fewer parameters. Additionally, NORACL yields architectures with interpretable growth, i.e. dissimilar tasks predominantly expand feature-extraction layers, whereas tasks which rely on common features shift growth toward later feature-combination layers. Our analysis further explains why fixed-capacity networks lose plasticity as tasks accumulate, whereas NORACL creates fresh capacity for new tasks through growth. Together, these results show that adaptive neurogenesis pushes the stability-plasticity Pareto frontier of continual learning.

---


### 10. [Cross-Subject Generalization for EEG Decoding: A Survey of Deep Learning Methods](https://arxiv.org/abs/2604.27033)

**<font color=#1a73e8>作者：</font>** Taida Li, Yujun Yan, Fei Dou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning for cross-subject EEG decoding is hindered by high inter-subject variability, which introduces a severe domain shift between training and unseen test subjects. This survey presents a comprehensive review of deep learning methodologies specifically engineered to address this cross-subject generalization challenge. To ground this analysis, we formalize the cross-subject setting as a multi-source domain problem and delineate the rigorous, subject-independent evaluation protocols required for valid assessment. Central to this survey is a systematic taxonomy of the current literature into discrete methodological families, including feature alignment, adversarial learning, feature disentanglement, and contrastive learning. We conclude by examining three critical elements for advancing robust, real-world decoding: the theoretical limitations of current methodologies, the structural value of subject identity, and the emergence of EEG foundation models.

---


### 11. [Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling](https://arxiv.org/abs/2604.27039)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Changyi Yang, Zijie Xia 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token serves as the fundamental unit of computation in modern autoregressive models, and generation length directly influences both inference cost and reasoning performance. Despite its importance, existing approaches lack fine-grained length modeling, operating primarily at the coarse-grained sequence level. We introduce the Length Value Model (LenVM), a token-level framework that models the remaining generation length. By formulating length modeling as a value estimation problem and assigning a constant negative reward to each generated token, LenVM predicts a bounded, discounted return that serves as a monotone proxy for the remaining generation horizon. This formulation yields supervision that is annotation-free, dense, unbiased, and scalable. Experiments on LLMs and VLMs demonstrate LenVM provides a highly effective signal at inference time. On the LIFEBench exact length matching task, applying LenVM to a 7B model improves the length score from 30.9 to 64.8, significantly outperforming frontier closed-source models. Furthermore, LenVM enables continuous control over the trade off between performance and efficiency. On GSM8K at a budget of 200 tokens, LenVM maintains 63% accuracy compared to 6 percent for token budget baseline. It also accurately predicts total generation length from the prompt boundary. Finally, LenVM's token-level values offer an interpretable view of generation dynamics, revealing how specific tokens shift reasoning toward shorter or longer regimes. Results demonstrate that LenVM supports a broad range of applications and token length can be effectively modeled as a token-level value signal, highlighting the potential of LenVM as a general framework for length modeling and as a length-specific value signal that could support future RL training. Code is available at this https URL.

---


### 12. [Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture](https://arxiv.org/abs/2604.27045)

**<font color=#1a73e8>作者：</font>** Samuel L Pugh, Eric Yang, Alexander Muir Sutherland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) agents transition from single-session tools to persistent systems managing longitudinal healthcare journeys, their memory architectures face a critical challenge: reconciling two imperfect sources of truth. The patient's evolving self-report is current but prone to recall bias, while the Electronic Health Record (EHR) is medically validated but frequently stale. General-purpose agent memory systems optimize for coherence by overwriting older facts with the user's latest statement, a pattern that risks safety failures when applied to clinical data. We introduce a Dual-Stream Memory Architecture that strictly separates the patient narrative from the structured clinical record (FHIR), governed by a dedicated Reconciliation Engine that evaluates every extracted memory against the patient's FHIR profile and classifies discrepancies by type, severity, and the specific FHIR resources involved. We evaluate this architecture on 26 patients across 675 longitudinal wellness coaching sessions, using a hybrid dataset that interleaves real provider-patient transcripts with synthetic, FHIR-grounded clinical scenarios. In isolated testing, the engine detects 84.4% of designed clinical discrepancies with 86.7% safety-critical recall. By coupling extraction and reconciliation evaluation on the same data, we directly quantify a 13.6% error cascade, tracing the degradation to clinical details lost during memory extraction from unstructured conversation rather than to downstream classification errors. These findings establish that validating patient-reported memories against clinical records is both feasible and necessary for safe deployment of longitudinal health agents.

---


### 13. [Learning to Forget: Continual Learning with Adaptive Weight Decay](https://arxiv.org/abs/2604.27063)

**<font color=#1a73e8>作者：</font>** Aditya A. Ramesh, Alex Lewandowski, Jürgen Schmidhuber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning agents with finite capacity must balance acquiring new knowledge with retaining the old. This requires controlled forgetting of knowledge that is no longer needed, freeing up capacity to learn. Weight decay, viewed as a mechanism for forgetting, can serve this role by gradually discarding information stored in the weights. However, a fixed scalar weight decay drives this forgetting uniformly over time and uniformly across all parameters, even when some encode stable knowledge while others track rapidly changing targets. We introduce Forgetting through Adaptive Decay (FADE), which adapts per-parameter weight decay rates online via approximate meta-gradient descent. We derive FADE for the online linear setting and apply it to the final layer of neural networks. Our empirical analysis shows that FADE automatically discovers distinct decay rates for different parameters, complements step-size adaptation, and consistently improves over fixed weight decay across online tracking and streaming classification problems.

---


### 14. [Learning Rate Transfer in Normalized Transformers](https://arxiv.org/abs/2604.27077)

**<font color=#1a73e8>作者：</font>** Boris Shigida, Boris Hanin, Andrey Gromov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Normalized Transformer, or nGPT (arXiv:2410.01131) achieves impressive training speedups and does not require weight decay or learning rate warmup. However, despite having hyperparameters that explicitly scale with model size, we observe that nGPT does not exhibit learning rate transfer across model dimension and token horizon. To rectify this, we combine numerical experiments with a principled use of alignment exponents (arXiv:2407.05872) to revisit and modify the $\mu$P approach to hyperparameter transfer (arXiv:2011.14522). The result is a novel nGPT parameterization we call $\nu$GPT. Through extensive empirical validation, we find $\nu$GPT exhibits learning rate transfer across width, depth, and token horizon.

---


### 15. [Co-Evolving Policy Distillation](https://arxiv.org/abs/2604.27083)

**<font color=#1a73e8>作者：</font>** Naibin Gu, Chenxu Yang, Qingyi Si 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RLVR and OPD have become standard paradigms for post-training. We provide a unified analysis of these two paradigms in consolidating multiple expert capabilities into a single model, identifying capability loss in different ways: mixed RLVR suffers from inter-capability divergence cost, while the pipeline of first training experts and then performing OPD, though avoiding divergence, fails to fully absorb teacher capabilities due to large behavioral pattern gaps between teacher and student. We propose Co-Evolving Policy Distillation (CoPD), which encourages parallel training of experts and introduces OPD during each expert's ongoing RLVR training rather than after complete expert training, with experts serving as mutual teachers (making OPD bidirectional) to co-evolve. This enables more consistent behavioral patterns among experts while maintaining sufficient complementary knowledge throughout. Experiments validate that CoPD achieves all-in-one integration of text, image, and video reasoning capabilities, significantly outperforming strong baselines such as mixed RLVR and MOPD, and even surpassing domain-specific experts. The model parallel training pattern offered by CoPD may inspire a novel training scaling paradigm.

---


### 16. [Useless but Safe? Benchmarking Utility Recovery with User Intent Clarification in Multi-Turn Conversations](https://arxiv.org/abs/2604.27093)

**<font color=#1a73e8>作者：</font>** Mingqian Zheng, Malia Morgan, Liwei Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current LLM safety alignment techniques improve model robustness against adversarial attacks, but overlook whether and how LLMs can recover helpfulness when benign users clarify their intent. We introduce CarryOnBench, the first interactive benchmark that measures whether LLMs can revise their interpretation of user intent and recover utility, while remaining safe through multi-turn conversations. Starting from 398 seemingly harmful queries with benign underlying intents, we simulate 5,970 conversations by varying user follow-up sequences, evaluating 14 models on both intent-aligned utility and safety. CarryOnBench yields 1,866 different conversation flows of 4--12 turns, totaling 23,880 model responses. We design Ben-Util, a checklist-based metric that evaluates how well each model response fulfills the user's benign information need using atomic items. At turn one, models fulfill only 10.5--37.6% of the user's benign information need. When the same query includes the benign intent upfront, models fulfill 25.1--72.1%, confirming that models withhold information due to intent misinterpretation, not limited knowledge. With benign clarifications in multi-turn conversations, 13 of 14 models approach or exceed this single-turn baseline, yet recovery cost varies across models. We identify three failure modes invisible to single-turn evaluations: utility lock-in, where a model rarely updates despite clarification; unsafe recovery, where a model updates at disproportionate safety cost; and repetitive recovery, where a model recycles prior responses rather than providing new information. Moreover, conversations converge to similar harmfulness levels regardless of how conservative the model starts. These findings expose a gap that single-turn evaluations miss -- whether a model is appropriately cautious or simply unresponsive to clarified user intent.

---


### 17. [Anomaly Detection in Soil Heavy Metal Contamination Using Unsupervised Learning for Environmental Risk Assessment](https://arxiv.org/abs/2604.27102)

**<font color=#1a73e8>作者：</font>** Isaac Tettey Adjokatse, Samuel Senyo Koranteng, George Yamoah Afrifa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soil contamination by heavy metals poses a persistent environmental and public health concern in rapidly urbanising regions of Ghana, particularly at unregulated waste disposal sites. This study applies an unsupervised machine learning framework to detect and characterise anomalous heavy metal contamination patterns in soils from twelve waste sites and residential controls in the Central Region, of Ghana. Concentrations of eight metals (As, Cd, Cr, Cu, Hg, Ni, Pb, Zn) were analysed alongside standard health risk indices, including the Hazard Index (HI) and Incremental Lifetime Cancer Risk (ILCR). Isolation Forest and PCA reconstruction error each identified $12$ anomalous samples ($15.4\%$ of $78$ samples), while DBSCAN detected no density-isolated noise points. A consensus approach isolated six robust anomalies ($7.7\%)$, all spatially concentrated at a single site (S3). Anomalies exhibited approximately $70$--$80\%$ higher mean HI values than normal samples, with all consensus anomalies exceeding the HI$=1$ threshold. PCA reconstruction error showed a strong positive association with HI ($r \approx 0.8$), indicating consistency between multivariate deviation and health risk. Three distinct anomaly types were identified: extreme Cu enrichment at S3, anomalously low Ni at S4/S5, and moderate multi-metal (Pb--Zn) co-elevation at S9--S12. The results demonstrate that unsupervised machine learning provides granular, objective insight beyond aggregate indices, enabling targeted site prioritisation and risk-informed environmental management.

---


### 18. [Reconstruction by Generation: 3D Multi-Object Scene Reconstruction from Sparse Observations](https://arxiv.org/abs/2604.27106)

**<font color=#1a73e8>作者：</font>** Andrii Zadaianchuk, Leonardo Barcellona, Lennard Schuenemann 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately reconstructing complex full multi-object scenes from sparse observations remains a core challenge in computer vision and a key step toward scalable and reliable simulation for robotics. In this work, we introduce RecGen, a generative framework for probabilistic joint estimation of object and part shapes, as well as their pose under occlusion and partial visibility from one or multiple RGB-D images. By leveraging compositional synthetic scene generation and strong 3D shape priors, RecGen generalizes across diverse object types and real-world environments. RecGen achieves state-of-the-art performance on complex, heavily occluded datasets, robustly handling severe occlusions, symmetric objects, object parts, and intricate geometry and texture. Despite using nearly 80% fewer training meshes than the previous state of the art SAM3D, RecGen outperforms it by 30.1% in geometric shape quality, 9.1% in texture reconstruction, and 33.9% in pose estimation.

---


### 19. [InterPartAbility: Text-Guided Part Matching for Interpretable Person Re-Identification](https://arxiv.org/abs/2604.27122)

**<font color=#1a73e8>作者：</font>** Shakeeb Murtaza, Aryan Shukla, Rajarshi Bhattacharya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image person re-identification (TI-ReID) relies on natural-language text description to retrieve top matching individuals from a large gallery of images. While recent large vision-language models (VLMs) achieve strong retrieval performance, their decisions remain largely uninterpretable. Existing interpretability approaches in TI-ReID rely solely on slot-attention to highlight attended regions, but fail to reliably bind visual regions to semantically meaningful concepts, limiting explanations to qualitative visualizations over a restricted vocabulary. This paper introduces InterPartAbility, an interpretable TI-ReID method that performs explicit part-wise matching and enables phrase-region grounding. A new open-vocabulary, lightweight supervision, patch-phrase interaction module (PPIM) is proposed to train a standard TI-ReID model with concept-level guidance. Concept-based part phrases provide evidence that encourages the model to attend to corresponding image regions. InterPartAbility further constrains CLIP ViT self-attention to produce spatially concentrated patch activations aligned with each part-level phrase, yielding grounded explanation maps. A quantitative interpretability protocol for TI-ReID is introduced by adapting perturbation-based evaluation metrics, including counterfactual region masking that measures retrieval degradation when top-ranked explanatory regions are removed. Empirical results\footnote{Our code is included in the supplementary materials and will be made public.} on challenging benchmarks like CUHK-PEDES and ICFG-PEDES show that InterPartAbility achieves state-of-the-art (SOTA) interpretability performance under these metrics, while sustaining competitive retrieval accuracy.

---


### 20. [Unsupervised Electrofacies Classification and Porosity Characterization in the Offshore Keta Basin Using Wireline Logs](https://arxiv.org/abs/2604.27126)

**<font color=#1a73e8>作者：</font>** Hamdiya Adams, Theophilus Ansah-Narh, Daniel Kwadwo Asiedu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study presents an unsupervised machine learning workflow for electrofacies analysis in the offshore Keta Basin, Ghana, where core data are scarce. Six standard wireline logs from Well~C were analysed over a depth interval comprising approximately $11{,}195$ samples. K-means clustering was applied in multivariate log space, with the clustering structure evaluated using inertia and silhouette diagnostics. Four clusters were identified, supported by an average silhouette coefficient of approximately $0.50$, indicating moderate but meaningful separation. The resulting electrofacies exhibit systematic, depth-continuous patterns associated with variations in clay content, porosity, and rock framework properties, forming a geological continuum from shale-dominated to cleaner sandstone-dominated units. The results demonstrate that log-only, unsupervised clustering supported by quantitative metrics provides a robust and reproducible framework for subsurface characterisation. The proposed workflow offers a practical tool for early-stage formation evaluation in frontier offshore basins and a foundation for future integrated studies.

---


### 21. [Lightweight Distillation of SAM 3 and DINOv3 for Edge-Deployable Individual-Level Livestock Monitoring and Longitudinal Visual Analytics](https://arxiv.org/abs/2604.27128)

**<font color=#1a73e8>作者：</font>** Haiyu Yang, Miel Hostens  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation-model pipelines for individual-level livestock monitoring -- combining open-vocabulary detection, promptable video segmentation, and self-supervised visual embeddings -- have raised the accuracy ceiling of precision livestock farming (PLF), but their GPU memory budgets exceed the envelope of commodity edge accelerators. To close this gap, the 446M-parameter Perception Encoder (PE-ViT-L+) backbone of SAM 3 is distilled into a 40.66M-parameter multi-scale student through three mechanisms: a Feature Pyramid Network student encoder built on TinyViT-21M-512, a four-term direction-then-scale distillation loss, and backbone-substitution inference with sliding-window session pruning that bounds streaming GPU memory growth. The DINOv3 family includes a pre-distilled ViT-S/16 variant (21.6M parameters) released alongside a 6716M-parameter ViT-7B teacher; the ViT-S (21M) variant is adopted as the per-individual embedder. On the Edinburgh Pig dataset, the compressed pipeline reaches 92.29% MOTA and 96.15% IDF1 against the SAM 3 teacher (1.68- and 0.84-percentage-point losses), achieves a 7.77-fold reduction in system-level parameters and a 3.01-fold reduction in peak VRAM (19.52GB -> 6.49GB), and reaches 97.34% top-1 accuracy with 91.67% macro-F1 on nine-class pig behaviour classification. The pipeline fits inside an NVIDIA Jetson Orin NX 16GB envelope with 4.9GB of headroom, supporting a proposed -- but not yet empirically validated -- on-device embedding-pool re-identification mechanism whose per-individual footprint of approximately 94MB per animal per year produces a longitudinal visual record amenable to retrospective association with disease, lameness, reproductive, and growth outcome labels.

---


### 22. [What Influences Readers' and Writers' Perceived Necessity of AI Disclosure?](https://arxiv.org/abs/2604.27129)

**<font color=#1a73e8>作者：</font>** Jingchao Fang, Victoria Xiaohan Wen, Mina Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing capability of artificial intelligence (AI) leads to its increasing adoption in writing, spurring discussions around whether writers should disclose their AI use in writing. What influences the perceived necessity of disclosure? We look into this question from three dimensions: perspective (reader or writer of the text), purpose (the goal of reading or writing), and procedural factors (how AI was used in the writing process in terms of replaceability, effortfulness, intentionality, and directness). In a vignette study (N = 727), we find that readers consider disclosure to be more necessary than writers, and disclosure is regarded as more necessary when AI's contribution in writing is irreplaceable, directly incorporated, and when the writer does not intentionally steer AI generation. To our surprise, the writers' intentionality of AI use produces contrasting effects on readers' and writers' perceived necessity of disclosure. Moreover, the effort of writing shows no significant effect on the perceived necessity. This study contributes to the conversation on transparent AI use by revealing readers' and writers' grassroots judgments, providing a unique angle to reflect on existing regulations, and offering insights into how AI disclosure guidance and tools could be designed to better align with readers' and writers' perceptions.

---


### 23. [TRUST: A Framework for Decentralized AI Service v.0.1](https://arxiv.org/abs/2604.27132)

**<font color=#1a73e8>作者：</font>** Yu-Chao Huang, Zhen Tan, Mohan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) and Multi-Agent Systems (MAS) in high-stakes domains demand reliable verification, yet centralized approaches suffer four limitations: (1) Robustness, with single points of failure vulnerable to attacks and bias; (2) Scalability, as reasoning complexity creates bottlenecks; (3) Opacity, as hidden auditing erodes trust; and (4) Privacy, as exposed reasoning traces risk model theft. We introduce TRUST (Transparent, Robust, and Unified Services for Trustworthy AI), a decentralized framework with three innovations: (i) Hierarchical Directed Acyclic Graphs (HDAGs) that decompose Chain-of-Thought reasoning into five abstraction levels for parallel distributed auditing; (ii) the DAAN protocol, which projects multi-agent interactions into Causal Interaction Graphs (CIGs) for deterministic root-cause attribution; and (iii) a multi-tier consensus mechanism among computational checkers, LLM evaluators, and human experts with stake-weighted voting that guarantees correctness under 30% adversarial participation. We prove a Safety-Profitability Theorem ensuring honest auditors profit while malicious actors incur losses. All decisions are recorded on-chain, while privacy-by-design segmentation prevents reconstruction of proprietary logic. Across multiple LLMs and benchmarks, TRUST attains 72.4% accuracy (4-18% above baselines) and remains resilient against 20% corruption. DAAN reaches 70% root-cause attribution (vs. 54-63% for standard methods) with 60% token savings. Human studies validate the design (F1 = 0.89, Brier = 0.074). The framework supports (A1) decentralized auditing, (A2) tamper-proof leaderboards, (A3) trustless data annotation, and (A4) governed autonomous agents, pioneering decentralized AI auditing for safe, accountable deployment of reasoning-capable systems.

---


### 24. [Unpacking Vibe Coding: Help-Seeking Processes in Student-AI Interactions While Programming](https://arxiv.org/abs/2604.27134)

**<font color=#1a73e8>作者：</font>** Daiana Rinja, Eduardo Araujo Oliveira, Sonsoles López-Pernas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is reshaping higher education programming through vibe coding, where students collaborate with AI via natural language rather than writing code line-by-line. We conceptualize this practice as help-seeking, analyzing 19,418 interaction turns from 110 undergraduate students. Using inductive coding and Heterogeneous Transition Network Analysis, we examined interaction sequences to compare top- and low-performing students. Results reveal that top performers engaged in instrumental help-seeking -- inquiry and exploration -- eliciting tutor-like AI responses. In contrast, low performers relied on executive help-seeking, frequently delegating tasks and prompting the AI to assume an executor role focused on ready-made solutions. These findings indicate that currently generative AI mirrors student intent (whether productive or passive) rather than optimizing for learning. To evolve from tools to teammates, AI systems must move beyond passive compliance. We argue for pedagogically aligned design that detect unproductive delegation and adaptively steer educational interactions toward inquiry, ensuring student-AI partnerships augment rather than replace cognitive effort.

---


### 25. [ConformaDecompose: Explaining Uncertainty via Calibration Localization](https://arxiv.org/abs/2604.27149)

**<font color=#1a73e8>作者：</font>** Fatima Rabia Yapicioglu, Meltem Aksoy, Alberto Rigenti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal Prediction provides distribution-free prediction intervals with guaranteed coverage, but its reliance on a single global calibration threshold obscures the sources of uncertainty at the instance level. In particular, it conflates irreducible noise with uncertainty induced by heterogeneous training data (aleatoric), model limitations, or calibration mismatch (epistemic), offering little insight into why an interval is wide or whether it could be reduced. We introduce an uncertainty-aware explainability framework that analyses the reducibility of calibration-induced epistemic conformal uncertainty via progressive calibration localisation for regression tasks. The approach is diagnostic rather than causal: it does not estimate true aleatoric or epistemic uncertainty, but explains how conformal intervals contract and stabilise as calibration support is localised around a test instance. Across benchmarks and real-world data, absolute reducible uncertainty aligns with epistemic proxies, while its relative contribution varies by task, revealing regimes hidden by interval width. This instance-level view complements conformal uncertainty, enhancing interpretability without altering the predictor or coverage.

---


### 26. [Optimal Stop-Loss and Take-Profit Parameterization for Autonomous Trading Agent Swarm](https://arxiv.org/abs/2604.27150)

**<font color=#1a73e8>作者：</font>** Nathan Li, Aikins Laryea, Yigit Ihlamur  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous crypto trading systems often spend most of their design effort on finding entries, while exits are left to fixed rules that are rarely tested in a systematic way. This paper examines whether better stop-loss and take-profit settings can improve the performance of an autonomous trading agent swarm. Using more than 900 historical trades, we replay each trade under many alternative exit policies and compare results against the existing production setup. The study finds that exit design matters meaningfully: stronger configurations improve risk-adjusted performance and generally favor tighter loss limits, earlier profit capture, and closer trailing protection. The paper also discusses a key evaluation challenge: a purely chronological split was initially used, but the newest trades fell into an unusual war-driven market period that sharply distorted test results. To reduce the influence of that single episode, the main comparison was run on randomized data, with the drawbacks of doing so acknowledged explicitly. Overall, the paper presents a practical framework for tuning exit logic in a more disciplined and transparent way.

---


### 27. [Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/abs/2604.27151)

**<font color=#1a73e8>作者：</font>** Jinbiao Wei, Kangqi Ni, Yilun Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents provide a promising path toward general software automation because they can interact directly with arbitrary graphical user interfaces instead of relying on brittle, application-specific integrations. Despite recent advances in benchmark performance, strong computer-use agents remain expensive and slow in practice, since most systems invoke large multimodal models at nearly every interaction step. We argue that this uniform allocation of compute is fundamentally inefficient for long-horizon GUI tasks. Such trajectories are highly heterogeneous: many steps are routine and can be handled reliably by smaller, cheaper policies, while errors tend to concentrate at a relatively small number of high-risk moments. Across computer-use benchmarks, these failures repeatedly take two forms: progress stalls, where the agent loops, repeats ineffective actions, or fails to make meaningful progress, and silent semantic drift, where the agent continues taking locally plausible actions after already deviating from the user's true goal. To address this inefficiency, we propose an event-driven, step-level cascade for computer-use agents that runs a small policy by default and escalates to a stronger model only when lightweight learned monitors detect elevated risk. Our framework combines two complementary signals: a Stuck Monitor that detects degraded progress from recent reasoning-action history and triggers recovery, and a Milestone Monitor that identifies semantically meaningful checkpoints where sparse verification is most informative for catching drift. This design turns always-on frontier-model inference into adaptive, on-demand compute allocation over the course of an evolving interaction. The framework is modular and deployment-oriented: it can be layered on top of existing computer-use agents without changing the underlying agent architecture or retraining the large model.

---


### 28. [Interval Orders, Biorders and Credibility-limited Belief Revision](https://arxiv.org/abs/2604.27156)

**<font color=#1a73e8>作者：</font>** Richard Booth, Ivan Varzinczak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rational belief revision is commonly viewed as being based on a preference order between possible worlds, with the resulting new belief set being those sentences true in all the most preferred models of the incoming new information. Usually, such a preference order is taken to be a total preorder. Nevertheless, there are other, more general classes of ordering that can also be employed. In this paper, we explore two such classes that have been studied within the theory of rational choice but have seen limited or no application in belief revision. We begin with interval orders, introduced by Fishburn in the '80s, which associate with each possible world a nonnegative `interval' of plausibility. We then move on to biorders, studied by Aleskerov, Bouyssou, and Monjardet, which generalise interval orders by allowing the intervals to have negative lengths, a feature that can be used to capture a notion of dissonance or instability. We provide axiomatic characterisations of these two resulting families of belief revision operators, as well as of two further families of interest that lie between interval orders and biorders. We show that while biorder-based revisions satisfy the Success postulate, they do not always yield consistent outputs. By modifying their definition to discard inputs that lead to inconsistency as `incredible', we derive new families of so-called non-prioritised revision that satisfy the Consistency postulate, but not the Success one. These families are linked to credibility-limited revision operators of Hansson et al., but for which the set of credible sentences does not satisfy the single-sentence closure condition. We argue that the biorder-based approach is well-suited for scenarios where an agent might initially reject new information, but may accept it when presented with additional explanation.

---


### 29. [A High-Throughput Compute-Efficient POMDP Hide-And-Seek-Engine (HASE) for Multi-Agent Operations](https://arxiv.org/abs/2604.27162)

**<font color=#1a73e8>作者：</font>** Timothy Flavin, Sandip Sen  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) algorithms exhibit high sample complexity, particularly when applied to Decentralized Partially Observable Markov Decision Processes (Dec-POMDPs). As a response, projects such as SampleFactory, EnvPool, Brax, and IsaacLab migrate parallel execution of classic environments such as MuJoCo and Atari into C++ thread pools or the GPU to decrease the computational cost of environment steps. We are interested in optimizing the decision-level of human-AI joint operations, so we introduce a compute-efficient Dec-POMDP engine natively architected in C++ called Hide-And-Seek-Engine. By employing Data-Oriented Design (DOD) principles, explicit 64-byte cache-line alignment to remove false sharing, and a zero-copy PyTorch memory bridge using pinned memory and Direct Memory Access (DMA), our engine sustains throughput of up to 33,000,000 steps per second (SPS) in a single-agent, 1024-environment, decentralized observations on an AMD Ryzen 9950X (16 cores). Ten agents reduces FPS to 7M SPS with generating random actions contributing 1/3rd the total runtime for reference. The engine achieves a throughput increase of approximately 3,500$\times$ over the baseline single threaded vectorized NumPy implementation and successfully trains cooperative multi-agent policies via PPO, DQN, and SAC in minutes, validating both its performance and generality.

---


### 30. [Context-Aware Graph Attention for Unsupervised Telco Anomaly Detection](https://arxiv.org/abs/2604.27172)

**<font color=#1a73e8>作者：</font>** Sara Malacarne, Eirik Hoel-Høiseth, Erlend Aune 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose C-MTAD-GAT, an \emph{unsupervised}, \emph{context-aware} graph-attention model for anomaly detection in multivariate time series from mobile networks. C-MTAD-GAT combines graph attention with lightweight context embeddings, and uses a deterministic reconstruction head and multi-step forecaster to produce anomaly scores. Detection thresholds are calibrated \emph{without labels} from validation residuals, keeping the pipeline fully unsupervised. On the public TELCO dataset, C-MTAD-GAT consistently outperforms MTAD-GAT and the Telco-specific DC-VAE, two state-of-the-art baselines, in both event-level and pointwise F1, while triggering substantially fewer alarms. C-MTAD-GAT is also deployed in the Core network of a national mobile operator, demonstrating its resilience in real industrial settings.

---


### 31. [Energy-Efficient Plant Monitoring via Knowledge Distillation](https://arxiv.org/abs/2604.27178)

**<font color=#1a73e8>作者：</font>** Ilyass Moummad, Reda Bensaid, Kawtar Zaher 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in large-scale visual representation learning have significantly improved performance in plant species and plant disease recognition tasks. However, state-of-the-art models, often based on high-capacity vision transformers or multimodal foundation models, remain computationally expensive and difficult to deploy in resource-constrained environments such as mobile or edge devices. This limitation hinders the scalability of automated biodiversity monitoring and precision agriculture systems, where efficiency is as critical as accuracy. In this work, we investigate knowledge distillation as an effective approach to transfer the representational capacity of large pretrained models into smaller, more efficient architectures. We focus on plant species and disease recognition, and conduct an extensive empirical study on two challenging benchmarks: Pl@ntNet300K-v2 and Deep-Plant-Disease. We evaluate four representative architectures, including two ConvNeXt models and two vision transformers, under multiple training regimes: from-scratch training and pretrained initialization, each with and without distillation. In total, we train and evaluate 70 models. Our results show that knowledge distillation consistently improves performance across tasks and architectures. Distilled models are able to match the performance of significantly larger models while maintaining substantially lower computational cost. These findings demonstrate the potential of knowledge distillation techniques to enable efficient and scalable deployment of plant recognition systems in real-world environmental applications.

---


### 32. [Preserving Temporal Dynamics in Time Series Generation](https://arxiv.org/abs/2604.27182)

**<font color=#1a73e8>作者：</font>** Ci Lin, Futong Li, Tet Yeap 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series data augmentation plays a crucial role in regression-oriented forecasting tasks, where limited data restricts the performance of deep learning models. While Generative Adversarial Networks (GANs) have shown promise in synthetic time-series generation, existing approaches primarily focus on matching marginal data distributions and often overlook the temporal dynamics that naturally exist in the original multivariate time series. When generating multivariate time series, this mismatch leads to distribution shift and temporal drift, thereby degrading the fidelity of the synthetic sequences.
In this work, we propose a model-agnostic Markov Chain Monte Carlo (MCMC)-based framework to mitigate distribution shift and preserve temporal dynamics in synthetic time series. We provide a theoretical analysis of how conditional generative models accumulate deviations under sequential generation and demonstrate that the MCMC algorithm can correct these discrepancies by enforcing consistency with empirical transition statistics between neighboring time points.
Extensive experiments on the Lorenz, Licor, ETTh, and ILI datasets using RCGAN, GCWGAN, TimeGAN, SigCWGAN, and AECGAN demonstrate that the proposed MCMC framework consistently improves autocorrelation alignment, skewness error, kurtosis error, R$^2$, discriminative score, and predictive score. These results suggest that synthetic time series consistent with the original data require explicit preservation of transition laws rather than solely relying on adversarial distribution matching, thereby offering a principled direction for improving generative modeling of time-series data.

---


### 33. [Evaluating TabPFN for Mild Cognitive Impairment to Alzheimer's Disease Conversion in Data Limited Settings](https://arxiv.org/abs/2604.27195)

**<font color=#1a73e8>作者：</font>** Brad Ye, Bulent Soykan, Gulsah Hancerliogullari Koksalmis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of conversion from Mild Cognitive Impairment (MCI) to Alzheimers Diseases (AD) is essential for early intervention, however, developing reliable conversion predictive models is difficult to develop due to limited longitudinal data availability We evaluate TabPFN (Tabular Pre-Trained Foundation Network) against traditional machine learning methods for predicting 3 year MCI to AD conversion using the TADPOLE dataset derived from ADNI. Using multimodal biomarker features extracted from demographics, APOE4, MRI volumes, CSF markers, and PET imaging, we conducted an experimental comparison across varying training set sizes (N=50 to 1000) and models including XGBoost, Random Forest, LightGBM, and Logistic Regression. TabPFN achieved one the highest performance (AUC=0.892), outperforming LightGBM (AUC=0.860) and demonstrating advantages in low data settings. At N=50 training samples, TabPFN maintained strong AUC while the traditional machine learning models struggles at small training samples. These findings demonstrate that foundation models are promising for disease prediction in data limited scenarios, such as Alzheimers diseases.

---


### 34. [Path-Lock Expert: Separating Reasoning Mode in Hybrid Thinking via Architecture-Level Separation](https://arxiv.org/abs/2604.27201)

**<font color=#1a73e8>作者：</font>** Shouren Wang, Wang Yang, Chuang Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid-thinking language models expose explicit think and no-think modes, but current designs do not separate them cleanly. Even in no-think mode, models often emit long and self-reflective responses, causing reasoning leakage. Existing work reduces this issue through better data curation and multi-stage training, yet leakage remains because both modes are still encoded in the same feed-forward parameters. We propose Path-Lock Expert (PLE), an architecture-level solution that replaces the single MLP in each decoder layer with two semantically locked experts, one for think and one for no-think, while keeping attention, embeddings, normalization, and the language-model head shared. A deterministic control-token router selects exactly one expert path for the entire sequence, so inference preserves the dense model's per-token computation pattern and each expert receives mode-pure updates during supervised fine-tuning. Across math and science reasoning benchmarks, PLE maintains strong think performance while producing a substantially stronger no-think mode that is more accurate, more concise, and far less prone to reasoning leakage. On Qwen3-4B, for example, PLE reduces no-think reflective tokens on AIME24 from 2.54 to 0.39 and improves no-think accuracy from 20.67% to 40.00%, all while preserving think-mode performance. These results suggest that controllable hybrid thinking is fundamentally an architectural problem, and separating mode-specific feed-forward pathways is a simple and effective solution.

---


### 35. [Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives](https://arxiv.org/abs/2604.27202)

**<font color=#1a73e8>作者：</font>** Soheil Khodayari, Xuenan Zhang, Bhupendra Acharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly integrated into systems that browse, retrieve, summarize, and act on web content, webpages have become an untrusted input vector for downstream model behavior. This enables site owners, contributors, and adversaries to embed instructions directly in web resources, i.e., indirect prompt injections. While prior work demonstrates such attacks in controlled settings, their prevalence, deployment, and real-world impact remain unclear.
We present one of the first large-scale empirical analyses of indirect prompt injections in webpages and HTTP responses. Analyzing 1.2B URLs from 24.8M hosts, we identify 15.3K validated instances across 11.7K pages. These are not isolated cases: a small number of recurring templates account for most cases. We characterize their objectives, delivery mechanisms, visibility, persistence, and impact, revealing a heterogeneous ecosystem spanning disruptive prompts, reputation manipulation, content-protection directives, and AI-bot detection, targeting systems such as crawlers, search pipelines, customer-support agents, and hiring workflows. A key finding is that most instructions target machines rather than humans: about 70% appear in non-rendered HTML (e.g., headers, comments, metadata), and many visible cases are hidden via rendering techniques. To assess practical risk, we run 5,200 controlled experiments across 13 models and four webpage representations. Our results show compliance is limited but non-negligible, reaching up to 8% for smaller models on plain-text inputs, while structured representations reduce compliance by preserving structural cues. Overall, prompt-based interference is already present in the web ecosystem and represents a growing source of tension between LLM-driven automation and the sites it consumes.

---


### 36. [Reading Speed, Image Quality Ratings, and Comfort Ratings in Augmented Reality](https://arxiv.org/abs/2604.27203)

**<font color=#1a73e8>作者：</font>** Minjung Kim, Saeideh Ghahghaei Nezamabadi, Trisha Lian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rendering and display of text is a key use-case for augmented reality (AR). Here, we present the Read-AR, a dataset of reading in AR, for which we collected over 11,000 reading speeds and almost 6000 visual quality and comfort ratings across over 80 different experiment conditions on the same experiment set-up. The consistent, controlled set-up enables the dataset to function as a reference for benchmarking the quality of different AR headset architectures.

---


### 37. [Selective Augmentation: Improving Universal Automatic Phonetic Transcription via G2P Bootstrapping](https://arxiv.org/abs/2604.27204)

**<font color=#1a73e8>作者：</font>** Tobias Bystrich, Julia M. Pritzen, Christoph A. Schmidt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the field of universal automatic phonetic transcription (APT), clean and diverse training transcriptions are required. However, such high-quality data is limited. We propose the bootstrapping approach Selective Augmentation to improve the available training transcriptions by selectively transferring distinctions between languages. Based on the model MultIPA, we exemplarily show that we could increase the accuracy of an existing feature (plosive voicing) and add a new feature (plosive aspiration) by augmenting the existing training data using information from a separate helper language (Hindi). We describe intrinsic challenges of the evaluation and develop objective metrics to determine the success: Voicing accuracy was increased by 17.6% by reducing the number of false positives. Additionally, aspiration recognition was introduced: While the baseline transcribed 0% of German /p, t, k/ as aspirated, our approach transcribed them as aspirated in 61.2% of the cases. Introducing aspiration recognition to APT models allowed for the tenuis class to be successfully reduced by 32.2%, which also reduces the conflations between the test language's plosives.

---


### 38. [HQ-UNet: A Hybrid Quantum-Classical U-Net with a Quantum Bottleneck for Remote Sensing Image Segmentation](https://arxiv.org/abs/2604.27206)

**<font color=#1a73e8>作者：</font>** Md Aminur Hossain, Ayush V. Patel, Ikshwaku Vanani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation in remote sensing is commonly addressed using classical deep learning architectures such as U-Net, which require a large number of parameters to model complex spatial relationships. Quantum machine learning (QML) provides an alternative representation paradigm by mapping classical features into quantum states, but its direct application to high-dimensional images remains challenging under near-term quantum hardware constraints. In this work, we propose HQ-UNet, a hybrid quantum-classical U-Net architecture that integrates a compact parameterized quantum circuit at the bottleneck of a classical U-Net. The proposed design uses a non-pooling quantum convolutional module to enrich highly compressed encoder features before decoding, while keeping the quantum component shallow and parameter-efficient. Experiments on the this http URL dataset show that HQ-UNet achieves a mean IoU of 0.8050 and an overall accuracy of 94.76%, outperforming the classical U-Net baseline. These results suggest that compact quantum bottlenecks can enhance feature representation for remote sensing image segmentation under near-term quantum constraints. This highlights the potential of hybrid quantum-classical designs as a promising direction for parameter-efficient dense prediction in Earth observation.

---


### 39. [AttriBE: Quantifying Attribute Expressivity in Body Embeddings for Recognition and Identification](https://arxiv.org/abs/2604.27218)

**<font color=#1a73e8>作者：</font>** Basudha Pal, Siyuan Huang, Anirudh Nanduri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification (ReID) systems that match individuals across images or video frames are essential in many real-world applications. However, existing methods are often influenced by attributes such as gender, pose, and body mass index (BMI), which vary in unconstrained settings and raise concerns related to fairness and generalization. To address this, we extend the notion of expressivity, defined as the mutual information between learned features and specific attributes, using a secondary neural network to quantify how strongly attributes are encoded. Applying this framework to three transformer-based ReID models on a large-scale visible-spectrum dataset, we find that BMI consistently shows the highest expressivity in deeper layers. Attributes in the final representation are ranked as BMI > Pitch > Gender > Yaw, and expressivity evolves across layers and training epochs, with pose peaking in intermediate layers and BMI strengthening with depth. We further extend the analysis to cross-spectral person identification across infrared modalities including short-wave, medium-wave, and long-wave infrared. In this setting, pitch becomes comparable to BMI and attribute trends increase monotonically across depth, suggesting increased reliance on structural cues when bridging modality gaps. Overall, the results show that transformer-based ReID embeddings encode a hierarchy of implicit attributes, with morphometric information persistently embedded and pose contributing more strongly under cross-spectral conditions.

---


### 40. [Upskilling with Generative AI: Practices and Challenges for Freelance Knowledge Workers](https://arxiv.org/abs/2604.27231)

**<font color=#1a73e8>作者：</font>** Kashif Imteyaz, Isabel Lopez, Nakul Rajpal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Freelance workers must continually acquire new skills to remain competitive in online labor markets, yet they lack the organizational training, mentorship, and infrastructure available to traditional employees. Generative AI-powered tools like ChatGPT are reshaping market skill demands while also offering new forms of on-demand learning support to meet those demands. Despite growing interest in AI-powered learning tools, little is known about how freelancers actually use these tools to learn, the challenges they encounter, and how generative AI for learning interacts with precarity and competition in platform-based work. We present a mixed-methods study combining a survey and semi-structured interviews with freelance knowledge workers. Grounded in self-directed learning theory, we examine how freelancers integrate generative AI tools into their learning practices. Our findings show that freelancers increasingly rely on generative AI to structure learning and support exploratory skill acquisition, but do not treat it as their primary learning resource due to inconsistency, lack of contextual relevance, and verification overhead. We identify a shift from learning as growth to learning as survival, where upskilling is oriented toward immediate market viability rather than long-term development. We also surface a structural challenge we term invisible competencies, in which workers acquire skills through generative AI tools but lack credible ways to signal or validate these skills in competitive freelance markets. Based on these insights, we offer design recommendations for generative AI-powered learning tools for freelancers.

---


### 41. [Reinforced Agent: Inference-Time Feedback for Tool-Calling Agents](https://arxiv.org/abs/2604.27233)

**<font color=#1a73e8>作者：</font>** Anh Ta, Junjie Zhu, Shahin Shayandeh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-calling agents are evaluated on tool selection, parameter accuracy, and scope recognition, yet LLM trajectory assessments remain inherently post-hoc. Disconnected from the active execution loop, such assessments identify errors that are usually addressed through prompt-tuning or retraining, and fundamentally cannot course-correct the agent in real time. To close this gap, we move evaluation into the execution loop at inference time: a specialized reviewer agent evaluates provisional tool calls prior to execution, shifting the paradigm from post-hoc recovery to proactive evaluation and error mitigation.
In practice, this architecture establishes a clear separation of concerns between the primary execution agent and a secondary review agent. As with any multi-agent system, the reviewer can introduce new errors while correcting others, yet no prior work to our knowledge has systematically measured this tradeoff. To quantify this tradeoff, we introduce Helpfulness-Harmfulness metrics: helpfulness measures the percentage of base agent errors that feedback corrects; harmfulness measures the percentage of correct responses that feedback degrades. These metrics directly inform reviewer design by revealing whether a given model or prompt provides net positive value.
We evaluate our approach on BFCL (single-turn) and Tau2-Bench (multi-turn stateful scenarios), achieving +5.5% on irrelevance detection and +7.1% on multi-turn tasks. Our metrics reveal that reviewer model choice is critical: the reasoning model o3-mini achieves a 3:1 benefit-to-risk ratio versus 2.1:1 for GPT-4o. Automated prompt optimization via GEPA provides an additional +1.5-2.8%. Together, these results demonstrate a core advantage of separating execution and review: the reviewer can be systematically improved through model selection and prompt optimization, without retraining the base agent.

---


### 42. [Remaining Useful Life Estimation for Turbofan Engines: A Comparative Study of Classical, CNN, and LSTM Approaches](https://arxiv.org/abs/2604.27234)

**<font color=#1a73e8>作者：</font>** Astitva Goel, Samarth Galchar, Sumit Kanu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Remaining Useful Life (RUL) estimation is a critical component of Prognostics and Health Management (PHM), enabling proactive maintenance scheduling and reducing unplanned failures in industrial equipment. This paper presents a comparative study of machine learning approaches for RUL estimation on the NASA C-MAPSS turbofan engine dataset: classical baselines (Ridge Regression, Polynomial Ridge, and XGBoost), a 1D Convolutional Neural Network (CNN), and a Long Short-Term Memory (LSTM) network. All models are evaluated on the FD001 and FD003 subsets under an identical preprocessing pipeline to ensure a fair comparison. Among raw-sequence models, the LSTM achieves RMSE of 14.93 and 14.20 on FD001 and FD003 respectively, outperforming the deep LSTM reported by Zheng et al.~\cite{paper} (RMSE 16.14 and 16.18) despite using a simpler single-layer architecture. The 1D CNN achieves RMSE of 16.97 on FD001 and 15.68 on FD003, demonstrating competitive performance on FD003 while producing more conservative RUL predictions on FD001. Ridge Regression is evaluated on raw and engineered features, while other classical models use only engineered inputs. XGBoost achieves an RMSE of 13.36 on FD003, highlighting the competitiveness of nonlinear modeling.

---


### 43. [Analytical Correction for Subsampling Bias in Drifting Models](https://arxiv.org/abs/2604.27239)

**<font color=#1a73e8>作者：</font>** Jiaru Zhang, Zeyun Deng, Juanwu Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drifting models are capable one-step generative models trained to follow a drifting field. The field combines attractive and repulsive softmax-weighted centroids over the data and current-generator distributions. In practice, only a minibatch of $n$ samples from each distribution is available, and each centroid is approximated by an empirical estimate. In this paper, we begin by showing that the minibatch centroid is in general a biased estimator of the target centroid, with a pointwise $O(1/n)$ bias arising from softmax self-normalization. Correcting this bias requires the expectation over the full distribution, which is intractable. We instead approximate the leading bias term from in-batch statistics and propose Analytical Bias Correction (ABC), a closed-form plug-in adjustment. We prove that ABC reduces the bias from $O(1/n)$ to $O(1/n^2)$, introduces no first-order increase in total variance, and preserves convex-hull containment of the corrected centroid. In practice, ABC requires only two additional lines of code and has negligible wall-time overhead under compiled execution. Toy experiments confirm the theoretical $O(1/n)$ and $O(1/n^2)$ scaling. On CIFAR-10, ABC reduces FID and trains faster, with the largest gains at small $n$, where the bias is most significant.

---


### 44. [Towards Generalizable Mapping of Hedges and Linear Woody Features from Earth Observation Data: a national Product for Germany](https://arxiv.org/abs/2604.27247)

**<font color=#1a73e8>作者：</font>** Thorsten Hoeser, Verena Huber-Garcia, Sarah Asam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hedges and other linear woody features provide valuable ecosystem services, particularly within intensively managed agricultural landscapes. They are key elements for climate adaptation and biodiversity amongst others not only due to a largely varying flora, but also as a feeding-, resting-, and nesting place for many animals and insects including valuable pollinators. Therefore, they require dedicated management, preservation, and attention. Thus, systematic and large-scale mapping of these features from Earth observation data is of high importance. However, transferable and reusable workflows for linear woody feature mapping remain a key methodological challenge, given the diversity of sensor types, spatial resolutions, data acquisition conditions, and complex landscape variability encountered across study areas. We introduce a modular workflow built around two independently optimizable components. Firstly, a flexible input data interface that consolidates heterogeneous Earth observation data into a binary woody vegetation mask, and secondly, a deep neural network trained to separate linear from non-linear shapes within these masks. We demonstrate the workflow by deriving three national-scale linear woody feature maps for all of Germany from three input sources by using a single trained model without retraining. Evaluation against refined reference data from four federal state biotope mapping campaigns and comparison with two existing linear woody feature maps demonstrate that the workflow produces competitive results across all evaluation sites on a national level. The modular design and its demonstrated applicability at national scale provide a foundation for scalable and generalizable linear woody feature mapping beyond Germany.

---


### 45. [AutoREC: A software platform for developing reinforcement learning agents for equivalent circuit model generation from electrochemical impedance spectroscopy data](https://arxiv.org/abs/2604.27266)

**<font color=#1a73e8>作者：</font>** Ali Jaberi, Yonatan Kurniawan, Robert Black 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces AutoREC, an open-source Python package for developing reinforcement learning (RL) agents to automatically generate equivalent circuit models (ECMs) from electrochemical impedance spectroscopy (EIS) data. While ECMs are a standard framework for interpreting EIS data, traditional identification is typically based on manual trial-and-error, which requires domain experts and limits scalability, particularly in autonomous experimental pipelines such as self-driving laboratories. AutoREC addresses this challenge by formulating ECM construction as a sequential decision-making problem within a Markov Decision Process framework. It implements a Double Deep Q-Network with prioritized experience replay, along with a dedicated dead-loop mitigation strategy, to efficiently explore a complex action space for circuit generation. To demonstrate the capabilities of the platform, we trained an RL agent using AutoREC and evaluated its strengths and limitations across diverse datasets, while also discussing possible strategies to mitigate these limitations in future agent designs. The trained agent achieved a success rate exceeding $99.6\%$ on synthetic datasets and demonstrated strong generalization to unseen experimental EIS data from batteries, corrosion, oxygen evolution reaction, and CO$_2$ reduction systems. These results position AutoREC as a promising platform for adaptive and data-driven ECM generation, with potential for integration into automated electrochemical workflows.

---


### 46. [Evaluating Epistemic Guardrails in AI Reading Assistants: A Behavioral Audit of a Minimal Prototype](https://arxiv.org/abs/2604.27275)

**<font color=#1a73e8>作者：</font>** Matthew Christian Agustin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) reading assistants are increasingly used in settings that require interpretation rather than simple retrieval. In these contexts, the central risk is not only error or unsafe output, but interpretive displacement: the transfer of meaning-making work from reader to system. This paper examines that problem through the concept of epistemic guardrails, defined here as constraints on how an artificial intelligence (AI) system participates in reading and interpretation. Using TextWalk, a minimal reading-support prototype designed as a co-reader rather than an answer-provider, the study applies a fixed ten-prompt protocol to twelve analytical texts spanning four categories of argumentative prose. The protocol escalates from baseline reading support to interpretive inquiry, boundary stress, and explicit shortcut pressure, enabling guardrails to be examined as behavioral properties observable in interaction rather than as static instruction features. Results show strong baseline stability, measurable strain during interpretive inquiry, partial recovery under direct boundary stress, and late-stage stabilization under escalation pressure. The most consequential weaknesses did not appear as overt collapse, but in a middle zone between support and substitution, where the system remained grounded and pedagogical while redistributing too much interpretive labor away from the reader. The paper contributes a protocol for evaluating epistemic guardrails as interactional phenomena in conversational AI reading assistants, an empirical account of their behavioral dynamics under pressure, and an emerging model of interpretive boundary function in reading-support AI.

---


### 47. [Predicting Covariate-Driven Spatial Deformation for Nonstationary Gaussian Processes](https://arxiv.org/abs/2604.27280)

**<font color=#1a73e8>作者：</font>** Minghao Gu, Weizhi Lin, Qiang Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonstationary Gaussian processes (GPs) are essential for modeling complex, locally heterogeneous spatial data. A common modeling approach is the spatial deformation method that warps the domain to recover isotropy. However, this static method does not account for changes in spatial correlation induced by covariates, limiting its ability to predict nonstationary GPs under new covariate conditions.
To enable predictive modeling of the deformation method, we propose to model the spatial deformation as a function of covariates. The spaces of diffeomorphic deformations and Euclidean covariate vectors are connected by characterizing deformations as generated by velocity fields living in a Lie algebra. To overcome the estimation instability caused by high-order interactions between multiple covariates in a general Lie algebra, we prove that those interactions can be truncated with a moderate physical assumption. Based on the theoretical results, a concise functional form of deformations driven by multiple covariates can be established, and an efficient estimation-inference algorithm is developed for out-of-sample nonstationary GP prediction with limited covariate-deformation sample pairs. The effectiveness and generalizability of the method are demonstrated on a simulation study and two case studies, in the fields of manufacturing and geostatistics, respectively.

---


### 48. [Mechanized Foundations of Structural Governance: Machine-Checked Proofs for Governed Intelligence](https://arxiv.org/abs/2604.27289)

**<font color=#1a73e8>作者：</font>** Alan L. McCann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present five results in the theory of structural governance for cognitive workflow systems. Three are mechanized in Coq 8.19 using the Interaction Trees library with parameterized coinduction; two are proved on paper with explicit reductions. The Coinductive Safety Predicate (gov_safe) is a coinductive property that captures governance safety for infinite program behaviors, indexed by a boolean permission flag that is provably false for ungoverned I/O and true for governed interpretations (mechanized). The Governance Invariance Theorem establishes that governance is uniform across the meta-recursive tower: governance at level n+1 reduces to governance at level n by definitional equality of the type (mechanized). The Sufficiency Theorem proves that four atomic primitives (code, reason, memory, call) are expressively complete for any discrete intelligent system, formalized as compositional closure of a Kleisli category (mechanized). The Alternating Normal Form provides a canonical decomposition of any machine into alternating code and effect layers, with a confluent rewriting system (paper proof). The Necessity Theorem proves via explicit reduction to Rice's theorem that an architecturally opaque component (the reason primitive) is mathematically necessary for problems requiring semantic judgment (paper proof). A sixth contribution connects the abstract model to the deployed runtime: the Verified Interpreter Specification formalizes the BEAM runtime's trust, capability, and hash chain logic in Coq, then tests the running system against this specification using property-based testing with over 70,000 randomly generated directive sequences and zero disagreements. The mechanization comprises approximately 12,000 lines across 36 modules with 454 theorems and zero admitted lemmas.

---


### 49. [The Two Boundaries: Why Behavioral AI Governance Fails Structurally](https://arxiv.org/abs/2604.27292)

**<font color=#1a73e8>作者：</font>** Alan L. McCann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every system that performs effects has two boundaries: what it can do (expressiveness) and what governance covers (governance). In nearly all deployed AI systems, these boundaries are defined independently, creating three regions: governed capabilities (the only useful region), ungoverned capabilities (risk), and governance policies that address non-existent capabilities (theater). Two of the three regions are failure modes. We focus on the governance of effects: actions that AI systems perform in the world (API calls, database writes, tool invocations). This is distinct from the governance of model outputs (content quality, bias, fairness), which operates at a different level and requires different mechanisms. We present a formal framework for analyzing this structural gap. Rice's theorem (1953) proves the gap is undecidable in the general case for any Turing-complete architecture that attempts to govern effects behaviorally: no algorithm can decide non-trivial semantic properties of arbitrary programs, including the property "this program's effects comply with the governance policy." We define coterminous governance: a system property where the expressivenessboundary equals the governance boundary. We show that coterminous governance requires an architectural decision (separatingcomputation from effect) rather than a governance layer added after the fact. We show that structural governance under this separation subsumes separate governance infrastructure: governance checks become part of the execution pipeline rather than a second system running alongside it. We propose coterminous governance as the testable criterion for any AI governance system: either the two boundaries are provably identical, or risk and theater are structurally inevitable. Proofs are mechanized in Coq (454 theorems, 36 modules, 0 admitted).

---


### 50. [Student Classroom Behavior Recognition Based on Improved YOLOv8s](https://arxiv.org/abs/2604.27293)

**<font color=#1a73e8>作者：</font>** Xiang Gao, Shuai Hang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In classroom teaching, student behavior can reflect their learning state and classroom participation, which is of great significance for teaching quality analysis. To address the problems of dense student targets, numerous small objects, frequent occlusions, and imbalanced class distribution in real classroom scenes, this paper proposes an improved student classroom behavior recognition model named ALC-YOLOv8s based on YOLOv8s. The model introduces SPPF-LSKA to enhance contextual feature extraction, employs CFC-CRB and SFC-G2 to optimize multi-scale feature fusion, and incorporates ATFLoss to improve the learning ability for minority classes and hard samples. Experimental results show that compared with the baseline model, the improved model achieves increases of 1.8% in mAP50 and 2.1% in mAP50-95. Compared with several mainstream detection methods, the proposed model can well meet the requirements of automatic student behavior recognition in complex classroom scenarios.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
