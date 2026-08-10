# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **117** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-117](./part-03.md)

---

### 1. [Multimodal Drivers' Emotion Recognition and Safety-Oriented Intervention for Intelligent Transportation Systems](https://arxiv.org/abs/2608.06378)

**<font color=#1a73e8>作者：</font>** Chang Liu, Dalai Mengke, Hanbo Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Driver emotions can affect risk perception, decision-making, and vehicle control under complex road conditions. Existing studies mainly focus on driver emotion recognition, while limited attention has been given to context-aware intervention that jointly considers driver emotion and road perception. This paper proposes a safety-prioritized multimodal driver assistance framework that analyzes speech-derived emotional cues and visual road conditions to generate structured driving interventions. The framework first provides road safety reminders and then generates emotion-aligned verbal support. We construct a multimodal dataset by aligning emotional speech signals with structured road environment descriptors and introduce the CARE (Context-Aware Road-Emotion Evaluation) score to jointly evaluate emotion recognition, risk identification, and intervention generation. Experimental results show that the proposed framework balances environmental risk reporting and emotion-aware verbal regulation, providing a feasible safety-driven direction for intelligent transportation systems.

---


### 2. [Preventive Care Recommendations by Large Language Models](https://arxiv.org/abs/2608.06379)

**<font color=#1a73e8>作者：</font>** Eden Avnat, Elia Yanko, Ori Yoran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Preventive care services (PCS) extend life, yet physicians often underprioritize highly effective interventions such as lifestyle modifications (Zhang et al., JAMA Network Open 2020). We evaluated whether large language models (LLMs) replicate and augment physician prioritization of PCS under time constraints. Using Zhang et al.'s validated survey with two patients assessed during long and short visits, we compared seven LLMs with historical physicians. We generated 137 simulated physician personas matching cohort demographics and tested three prompts per model. Primary outcomes were concordance with physician rankings, measured by Spearman correlation, and Consensus-Stratified Agreement (CSA), the proportion of LLM selections rated 4 or higher that matched physician consensus across agreement strata. Secondary outcomes included life-years gained per prioritized choice (LYGPC), consistency, and selectiveness. Augmentation was assessed by having models revise physician rankings under three informative prompts, with delta LYGPC quantifying impact. LLMs closely mirrored physicians (mean Spearman = 0.83, SD = 0.11), with high CSA at extreme agreement ranges (94%, 197/210) but low CSA in moderate ranges (21%, 30/140), where they underprioritized lifestyle services (8.8% vs. 38% rated 4 or higher; P < .001). Several models exceeded physicians in LYGPC and consistency while being more selective. Time constraints affected physicians and LLMs similarly, increasing LYGPC and selectiveness but reducing consistency. Augmentation effects varied by model. Current LLMs reproduced physicians' time-sensitivity and base-rate prioritization while exacerbating underprioritized lifestyle interventions. Some models improved prioritization performance, but consistent augmentation will require value-aligned training, explicit time-constraint representation, and prospective real-world validation.

---


### 3. [Towards Multi-Label Graph Foundation Models: from Single-Vector Representation Learning to Multi-Semantic Basis Learning](https://arxiv.org/abs/2608.06394)

**<font color=#1a73e8>作者：</font>** Dongxiao He, Jiayu Zhang, Jitao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-label node classification is an important yet challenging task in graph learning, where nodes exhibit multiple semantics simultaneously. Existing methods for multi-label node classification can effectively model multiple labels, while only considering in-domain scenarios where the model needs to be trained and tested within the same graph domain, resulting in limited cross-domain generalization. Recently, Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable graph representations across diverse graph domains and downstream tasks. However, existing GFMs are built upon single-label assumption, where all nodes are arbitrarily regarded as containing only one class of semantic and embedded into a single representation. For multi-label nodes, such a representation essentially approximates multiple semantics with a single point in the representation space, inevitably leading to semantic entanglement and making simultaneous discrimination of multiple labels difficult. To address these limitations, we propose a Multi-Semantic Basis Graph Foundation Model (MSB-GFM), a framework for cross-domain multi-label node classification. Specifically, we introduce a multi-semantic basis representation learning paradigm that models each multi-label node as an adaptive composition of semantic bases, thereby enabling flexible representational capacity for modeling multiple semantics. Furthermore, we develop a semantic-structure dual-channel architecture with domain adversarial training for effective cross-domain knowledge transfer. Extensive experiments demonstrate the effectiveness of our model.

---


### 4. [TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation](https://arxiv.org/abs/2608.06396)

**<font color=#1a73e8>作者：</font>** Guanzhi Deng, Haibo Wang, Kuan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models route each token through a small subset of experts, making routing patterns useful for identifying task-relevant experts during downstream adaptation. Yet current approaches have two limitations: task experts are typically identified from aggregate routing statistics that reflect usage rather than association with successful task completion, and task-expert activations remain underexplored as signals for supervision allocation. We introduce Task-Expert-Aware Supervision (TEXAS), which combines correctness-conditioned task expert discovery with token-level supervision allocation. TEXAS compares expert activations on instances that the base model solves successfully and those it fails to solve, and retains experts more strongly activated on successful instances. During fine-tuning, it upweights answer tokens in failed instances when they activate these experts. TEXAS therefore leverages existing routing behavior without restricting adaptation to a fixed expert subset or imposing an explicit target routing distribution. Across three MoE models and six benchmarks, TEXAS achieves the best or tied-best performance in 17 of 18 settings and improves over the strongest baseline by 1.3--1.5 points on average. Ablations and further analyses validate both the discovered experts and the resulting supervision strategy.

---


### 5. [EntropyMoE: Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs](https://arxiv.org/abs/2608.06398)

**<font color=#1a73e8>作者：</font>** Bo Liu, Muxuab Yu, Yu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent byte-level large language models (LLMs) have made tokenizer-free modeling increasingly competitive by grouping bytes into dynamically sized patches. However, existing byte-patch architectures still apply the same dense feed-forward computation to every patch. This uniform computation cannot adapt model capacity to variations in patch semantics and granularity. We address this limitation with EntropyMoE, a Mixture-of-Experts (MoE) architecture designed for dynamic byte patches. EntropyMoE replaces the dense feed-forward modules in the global patch Transformer with Top-K expert layers. Each dynamic patch serves as the basic unit of expert routing, and its byte coverage determines its contribution to workload accounting. The router selects experts directly from patch entropy, using the same granularity signal that underlies dynamic patch construction to organize sparse computation. Patch entropy and length jointly define the feature space for regulating expert specialization. Experiments show that EntropyMoE achieves the lowest held-out bits-per-byte among matched dense and sparse baselines while maintaining comparable downstream accuracy. These results establish patch entropy as an effective routing coordinate for sparse conditional computation and extend Mixture-of-Experts modeling beyond tokenizer-based representations.

---


### 6. [Interpretable Unsupervised Community Detection with LLM-Symbolized Structured Processes](https://arxiv.org/abs/2608.06402)

**<font color=#1a73e8>作者：</font>** Aoting Zeng, Kai Wang, Jianwei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Community detection is a fundamental task in graph analytics that aims to identify cohesive groups of entities with similar behaviors or interests. Classic objective-driven methods struggle with complex graph structures, while deep-learning approaches improve performance at the expense of interpretability and rely on labeled data and training. Large language models (LLMs), with strong reasoning capabilities and world knowledge, are promising for interpretable, label-free community detection. To leverage these strengths, we propose LUCID, an LLM-guided, interpretable, training-free, and unsupervised community detection method. Inspired by phase-transition kinetics in natural systems, where complex structures emerge through initialization, merging, refinement, and selection, LUCID is designed as a four-stage pipeline. Within this pipeline, the LLM induces formal rules that translate implicit knowledge into explicit and interpretable logical structures. Specifically, (1) the Local-View Community Initialization stage encodes local graph structures using k-ego contexts and unsupervised node roles; (2) the Multi-factor Community Merge stage uses LLM-induced rules to iteratively merge local communities; (3) the Multi-grain Community Refinement stage applies LLM-induced coarse-to-fine rules in parallel to reduce boundary noise; and (4) the Global-view Community Selection stage identifies high-quality communities based on topological compactness and boundary clarity. Extensive experiments on real-world datasets demonstrate that LUCID, as an unsupervised approach, achieves state-of-the-art performance and consistently outperforms leading unsupervised and semi-supervised baselines.

---


### 7. [Deep Evidential Regression for Sparse Forest Height Estimation from Multimodal Satellite Imagery](https://arxiv.org/abs/2608.06406)

**<font color=#1a73e8>作者：</font>** Laura Bader, Muhammad Ammar Ahmed, Xiao Xiang Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of forest height from satellite imagery is essential for applications such as carbon accounting, biodiversity monitoring, and ecosystem management. While recent deep learning approaches provide accurate predictions, they typically do not quantify predictive uncertainty. This limitation is particularly relevant in geospatial settings characterized by sparse supervision and geographic distribution shift. In this work, we investigate Deep Evidential Regression (DER) for forest height estimation on the TreeUQ benchmark, a large-scale dataset designed for the joint estimation of tree count and average tree height at 10 m resolution, based on Sentinel-1/-2 data as well as tree inventory data over the federal state of Bavaria. To account for the extreme label sparsity of the tree inventory data, we introduce a masked evidential loss for dense geospatial prediction. Using a U-Net architecture with multimodal Sentinel-1 and Sentinel-2 inputs, the proposed approach jointly predicts tree height and associated uncertainty estimates in a single forward pass. Experimental results show that DER achieves predictive performance comparable to a deterministic U-Net while additionally providing well-calibrated uncertainty estimates. These findings demonstrate the potential of evidential learning as an efficient framework for uncertainty-aware forest structure estimation from Earth observation data.

---


### 8. [Separating Decision-Rule Misalignment from Readout-Coverage Limitations in Speech Language Models](https://arxiv.org/abs/2608.06409)

**<font color=#1a73e8>作者：</font>** Linkai Peng, Baorian Nuchged  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech language models are increasingly evaluated on paralinguistic tasks by the accuracy of prompted answers, but answer accuracy combines failures at different stages of the audio-to-answer computation. We introduce a generation-aligned diagnostic ladder that compares the emitted answer, the option logits, an affine readout of those logits, and a linear readout of the hidden state at the same answer token. Successive differences separate endpoint, decision-rule, and readout-coverage gaps. Across five systems and two emotion corpora, state decoding exceeds generation by 27.8 accuracy points on average, and both the decision-rule and readout-coverage gaps are positive in all ten conditions. A label-free logit correction improves generated accuracy in every condition, showing that part of the decision-rule gap is actionable. In rank-matched comparisons, emotion information outside the native readout generalizes to held-out speakers and survives controls for measured acoustic descriptors, but replacing the selected readout-external directions usually has little effect on emitted answers. These results distinguish information availability from behavioral use and localize performance losses across the decision rule and the state-to-answer readout.

---


### 9. [ADIAS: Automated Design of Interactive Agentic Systems](https://arxiv.org/abs/2608.06410)

**<font color=#1a73e8>作者：</font>** Lekang Jiang, Bohan Tang, Stephan Goetz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated agent design improves agent harnesses through iterative revision, evaluation, and feedback summarization. Existing methods are largely candidate-centric: cross-round experience is organized around candidate agents, which leaves the repair progress implicit. This causes inefficient repair targeting, slow consolidation of partial progress, and propagation of ineffective interventions across rounds. Therefore, we formulate issue-centric agent optimization, in which repair progress is carried forward as an explicit persistent issue state to guide optimization, rather than re-derived from candidate history in each round. We instantiate the formulation in ADIAS, a framework for automated full-code agent design with two mechanisms. A persistent issue state maintains stable issue identities, lifecycle status, supporting evidence, and intervention-outcome histories. Issue-guided optimization uses this state to jointly propose repair targets and revision directions for subsequent focused full-code modification. Across five interactive benchmarks, ADIAS outperforms the strongest baseline by 25.2% on average and achieves consistent gains across four backbone models. Controlled ablations further show that removing persistent issue state or replacing issue-centric revision with candidate-centric policies leads to performance drops of up to 40.7%.

---


### 10. [Learning to Predict Middle-Layer Attention in MLLMs for Visual Token Prunin](https://arxiv.org/abs/2608.06411)

**<font color=#1a73e8>作者：</font>** Yuyao Sun, Tao Deng, Shuang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) achieve strong performance across diverse vision-language tasks, but their efficiency is limited by the cost of processing numerous visual tokens. Visual token pruning can reduce this cost, but requires accurate token importance estimates. Recent studies have demonstrated that text-to-vision attention from middle language model layers can effectively guide visual token pruning, typically using attention from a predefined middle layer to select the visual tokens to retain. Two problems therefore remain. First, our analysis shows that the layer whose attention is most responsive to the question varies substantially across samples, making a fixed layer suboptimal. Second, obtaining attention from the appropriate middle layer requires processing numerous visual tokens through several language model layers, by which point considerable computation has already been spent. To address both problems, we propose Middle-layer Attention Prediction (MAP), which uses Question Contrastive Teacher Selection to identify a sample-specific teacher layer by contrasting attention under the original and reference questions, and distills attention from the selected layer into a lightweight predictor that estimates visual token importance from multi-modal input features. During inference, MAP combines the predicted importance scores with a diversity criterion to prune visual tokens before the first language model layer. Thus, MAP requires no attention maps for pruning and remains compatible with existing inference acceleration techniques. Across ten benchmarks on LLaVA-NeXT-7B, MAP retains 97.5% of the unpruned model performance with only 5.56% of the visual tokens, yielding a 3.09x end-to-end speedup.

---


### 11. [Latent Fact-Checking: Detecting Misinformation through Activation Engineering](https://arxiv.org/abs/2608.06417)

**<font color=#1a73e8>作者：</font>** Pedro Barcelos, Otávio Parraga, Marcelo M. Mussi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The proliferation of misinformation online has driven demand for scalable detection systems. While most existing approaches rely on surface-level linguistic features or external knowledge retrieval, we examine truthfulness as a geometric property of a language model's representation space. We introduce a misinformation detection framework grounded in activation engineering, which leverages the latent geometry of transformer models. Our approach elicits a misinformation direction in the residual stream by contrasting activations from paired truthful and false statements, following the difference-in-means principle of Contrastive Activation Addition (CAA). At inference time, the last-token activation of an unseen claim is projected onto this direction, and the projected representation is fed to an Multilayer Perceptron (MLP) for classification. The procedure requires no fine-tuning of the backbone model, no external evidence retrieval, and no task-specific supervision beyond the contrastive pairs used to estimate the direction. We evaluate the method across 11 models from the Gemma, Llama, and Qwen families, ranging from 270M to 12B parameters, on three fact-checking benchmarks: AVeriTeC, LIAR, and FACTors. The falsehood direction is recoverable across model scales and architectural families, and last-token projection matches or surpasses zero-shot and few-shot prompting baselines on LIAR and FACTors, with the largest gains observed for smaller models. Performance on AVeriTeC is more limited, which we attribute to its evidence-grounded labeling scheme. These findings provide evidence that truthfulness is a structured, linearly separable concept in the latent space of pretrained language models, and point toward interpretability-driven misinformation detection as a practical complement to retrieval-based pipelines. The code is available on this https URL.

---


### 12. [Sharding Prevents LLM Oversight Failures and Adversarial Exploitation](https://arxiv.org/abs/2608.06422)

**<font color=#1a73e8>作者：</font>** Victor Akinwande, J. Zico Kolter, Aran Nayebi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Giving an LLM judge more compute does not necessarily make it check more requirements. When one call must return many verdicts, some decisions become weakly grounded in the evidence, even when that call receives the same token or tool budget as a panel of separate calls. Across expert-graded research replications, legal work, and clinical-trial assessments, agreement with experts falls as the number of verdicts per call grows. We identify sharding as the intervention that mitigates this failure in model-based oversight. Sharding partitions the requirements into smaller groups, assigns each group to a separate call, and aggregates the verdicts. Against a single call with the panel's full budget, sharding improves agreement while holding the model, evidence, total budget, and per-decision budget fixed. Overall, we find that a sharded weaker judge can outperform a more capable holistic judge and match that judge even when the latter receives the panel's full budget. Additionally, we find that sharding exhibits robustness against adversaries. A best-of-N adversary can hold the underlying work fixed, vary only its presentation, and increase an overloaded judge's acceptance of genuinely unmet criteria severalfold. Wherever sharding reduces baseline error, it removes this adversarial advantage, keeping over-acceptance low even as the adversary's search widens. Sharding does not address attacks that persuade the judge separately on each criterion rather than exploiting overload. In that setting, we find that debate-style opposition on top of sharding withstands such adaptive re-optimization.

---


### 13. [Recovering Lesion Parameters from Aphasic Picture Naming Error Profiles in Large Language Models](https://arxiv.org/abs/2608.06429)

**<font color=#1a73e8>作者：</font>** Yong Yang, Roger Newman-Norlund, Xiang Guan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretability methods for large language models (LLMs) describe internal state but do not directly test whether that state is causally sufficient to produce the observed behavior. In earlier work, we lesioned LLMs to produce error profiles in picture naming, a central task for assessing aphasia, and found that specific lesions produced errors resembling those of individual stroke survivors. Here we ask the inverse question: given an error profile, can the lesion parameters that produced it be recovered, and what does this inverse problem reveal about transformer computation? Lesions in LLaVA-Vicuna 13B were parameterized by layer index, modification percentage, and noise sigma across 4,840 configurations, and error profiles were characterized by a seven-category clinical taxonomy (correct, semantic, unrelated, formal, mixed, neologism, no-response). We trained a multi-task neural network to map error profiles back to perturbation parameters. The problem admitted a partial solution: across 10 independently trained inverse models, modification percentage and noise sigma were recoverable, whereas layer index was recoverable only within a neighborhood. In counterfactual validation, a fresh model instance perturbed with the recovered parameters reproduced the target behavior in 81.4% of cases. This dissociation between low layer recovery and high counterfactual fidelity is consistent with functional redundancy across transformer layers, a property not captured by standard interpretability methods. As an out-of-distribution test, we applied the trained model to picture-naming error profiles from 278 stroke survivors; recovered parameters were syndrome-discriminative, most strongly for perturbation intensity, indicating generalization beyond the training distribution. Counterfactual validation provides a general framework for LLM interpretability claims beyond inverse mapping.

---


### 14. [WebGrader: Training LLMs for Web Development with Self-Evolving Programmatic Grader](https://arxiv.org/abs/2608.06474)

**<font color=#1a73e8>作者：</font>** Boshui Chen, Huiping Liu, Shaolei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly generate complete websites from natural-language descriptions, and reinforcement learning has become a central approach to closing their remaining functional gap. This training regime is bottlenecked by reward design. Hand-authored browser scripts are executable yet costly to write for open-ended requirements, while VLM and GUI-agent graders scale but may issue verdicts before observing the decisive state. We propose WebGrader, a self-evolving programmatic grader that autonomously derives the required interaction flows from each website request, represents each flow as an executable Flow Contract, and uses its execution outcome as an RL reward. WebGrader materializes the generated project in a live browser, grounds target actions against the source code and live DOM, and collects visual, DOM, response, and persistent-state evidence along the same browser trajectory. A residual-driven offline loop then discovers reusable verifier skills, screens them on disjoint validation pages, and freezes the promoted skill graph before policy training. By separating test planning, action grounding, evidence collection, and semantic judgment, WebGrader issues a Pass verdict only after observing the requested transition. On WebGen-Bench, WebGrader trains an 8B policy to a 52.01% functional success rate, outperforming a matched appearance-plus-script reward by 7.88 points and surpassing o4-mini and DeepSeek-v4-flash. On WG-core-250, the policy reaches a Full Score of 44.953 and surpasses Qwen3-Coder-480B.

---


### 15. [Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events](https://arxiv.org/abs/2608.06485)

**<font color=#1a73e8>作者：</font>** Ming Wang, Peidong Wang, Xiaocui Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personality-conditioned LLM agents (PC-Agents) are increasingly used in emotional support, social simulation, and role-playing, motivating the development of lifelong agents that remain coherent over extended interactions. A key component of such coherence is personality evolution: agents should undergo plausible, psychology-grounded changes as they experience life events in different contexts. Although prior work shows that LLM personalities can shift under contextual perturbations, how these shifts vary across traits, events, personas, and models remains poorly understood. We study event-induced personality change after 11 major life events, using the Big Five traits as a psychometric anchor and interpreting the resulting trajectories against longitudinal evidence from human personality psychology. Across four diagnostic axes, PC-Agents exhibit measurable trait shifts at similar rates for event-trait pairs with and without documented human change directions. Even when shifts follow the expected direction, their magnitudes usually fall below human effect-size ranges. Gender and cultural-region prompts show little moderating effect, while persona-level dispersion is compressed three- to four-fold relative to human samples. To enable systematic comparison, we introduce BFI-Adapt, a reusable benchmark for scoring the directional fidelity of event-induced personality change, and use it to rank 14 models. A validation suite shows that the measured shifts exceed no-event retest noise, remain stable under independently paraphrased prompts, exhibit limited and model-dependent convergence with scenario-based behavioral choices, and persist across intervening unrelated dialogue. Together, these checks establish the measured trajectories as robust event-conditioned response patterns. Our results suggest that current PC-Agents simulate the mean of human personality dynamics, but not its shape.

---


### 16. [Beyond Attention: Signed Integrated Gradients Attribution in a BiomeGPT-Style Microbiome Transformer](https://arxiv.org/abs/2608.06486)

**<font color=#1a73e8>作者：</font>** Oren Nelson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a feature-tokenized transformer (arXiv:2106.11959) such as BiomeGPT (doi:https://doi.org/10.64898/2026.01.05.697599), each input token is built by fusing a fixed identity with a sample-specific measurement: a fixed species and a variable abundance, T = S + A. To interpret downstream classification in such models, prior work inspects the attention weights of the special [CLS] token (arXiv:2106.11959, arXiv:1810.04805, BiomeGPT) to rank sample tokens by importance. These weights have two critical limitations: they are nonnegative, so they cannot separate disease-supporting from health-supporting evidence (arXiv:2201.12114), and they act after token fusion, obscuring how the input sources S and A each affect the output.
To address this we use Integrated Gradients (arXiv:1703.01365), a signed, fusion-aware attribution method, and propose a source-derived baseline T' = S + A_0 for feature-tokenized models such as BiomeGPT, which preserves species identity as a fixed biological coordinate while isolating the effect of abundance variation. Applied to a disease-versus-health decision margin, it yields polarity that explicitly separates pathogenic from protective microbial signals. We show that this gradient-based approach uncovers species-abundance directional relationships and sensitivity diagnostics entirely obscured by unsigned [CLS] attention weights. We further recommend second-order Integrated Hessians (arXiv:2002.04138) to expose microbiome community interaction rules: how a perturbation in one member alters the model's sensitivity to another, and which other species drive ambiguous cases toward disease or health at a given abundance level. This provides a principled approach to explainability in BiomeGPT that generalizes to other smooth and differentiable feature-tokenized transformers. Code is available at this https URL

---


### 17. [Can MLLMs Decode the Creative Leap? Introducing C4 for Cross-Concept Understanding](https://arxiv.org/abs/2608.06501)

**<font color=#1a73e8>作者：</font>** Ming Wang, Yuqing Zhang, Tingna Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Creative capabilities of MLLMs matter in design, communication, education, and human--AI collaboration, yet remain difficult to evaluate because explicit targets and reward signals are scarce compared with accuracy-oriented tasks. Cross-concept understanding is a core cognitive capacity underlying receptive creativity. It enables a perceiver to recover intended meaning from non-obvious but meaningful conceptual relations. We operationalize item construction as cross-concept encoding and model inference as cross-concept decoding. We introduce C4, a cognition-inspired evaluation framework for Chengyu (Chinese idiom)-based Cross-Concept Creativity. Its encoding component maps target slots to imageable substitute concepts along bridge paths in a manually annotated and third-party-reviewed cross-concept network, enabling batch generation with explicit structure, difficulty indexed by bridge count and depth, and exact answers. Using this framework, we instantiate the C4 Evaluation Set (C4-Eval), comprising 184 synthetic items and 37 human-created cross-concept chengyu figures collected from online sources. We manually construct and review cross-concept relations, bridge paths, and reasoning processes for the collected figures. Each C4-Eval item is instantiated in five task settings, yielding 884 primary answer-recovery cases. Across ten evaluated MLLMs, the strongest closed models reach 50.7% and 48.0% primary accuracy, while open-source models remain substantially lower. Candidate constraints improve accuracy sharply, but bridge hints and explanation requests provide only modest gains. These results expose a substantial gap in how current MLLMs decode creatively encoded meaning through cross-concept relations. The code is in the supplementary material.

---


### 18. [Measuring the Cross-Lingual Comprehension Gap: How the language of the evidence shapes what language models understand](https://arxiv.org/abs/2608.06506)

**<font color=#1a73e8>作者：</font>** Rafael da Silva, Jeff Eicher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are often evaluated as though capabilities demonstrated in English remain equally available when the same content is presented in other languages. Traditional multilingual benchmarks rarely isolate language while holding content, question, reference answer, model, and evaluation unit constant. We define the Cross-Lingual Comprehension Gap (CLCG) as the reduction in response quality when the same content and question are presented in a target language rather than in English.
Using ParallelQA-18, a professionally human-translated parallel corpus, we evaluate five models from five laboratories on a stratified sample of 150 articles across 18 languages (English reference; Portuguese high-resource baseline; 16 targets spanning Joshi et al. 2020 classes 0-4). A within-item design varies only passage language. The primary estimator contrasts English versus pooled target-language Token-F1 micro-means on higher-complexity open-ended questions, with article-cluster bootstrap intervals.
The primary pooled CLCG is 0.078 (95% CI 0.072-0.084), about a 17% reduction relative to the English score; the equal-language macro summary is 0.077. Net of Portuguese, the macro gap is 0.016 (95% CI 0.013-0.020). Language-level CLCG is negatively associated with Joshi resource class (rho = -0.594, p = 0.015, n = 16). In blinded paired human evaluations, higher-resource responses are preferred in 61.6% of decisive judgments (estimated preference probability 0.655, 95% CI 0.558-0.741).
Capabilities shown in English should not be assumed to transfer equally to other languages; English-centered evaluations may overestimate quality for users of low-resource languages.

---


### 19. [CertBind from Multimodal Connectivity to Certifiable Retrieval Decisions](https://arxiv.org/abs/2608.06516)

**<font color=#1a73e8>作者：</font>** Shuheng Cao, Zhenhao Zhang, Ruiqi Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lightweight connectors make frozen multimodal encoders composable at the representation level. Deployment exposes a second problem at the level of task decisions. A connected route can expand cross-modal reach while changing an established native retrieval capability. We introduce CertBind, a multiscale theory of certifiable composition for frozen multimodal connector graphs. At the node scale, native anchors establish the exact task identification boundary under the stated chart model. At the edge scale, contract-aware conformal ranks provide graph-wide family-wise error control. At the path scale, an overlap-aware budget and clean calibration yield a finite-sample recovery radius under declared conditions. At the query scale, this radius yields a covered top-k candidate set that becomes a point certificate when its size equals k. CertBind therefore retains supported routes as Direct, sends only flagged routes to recovery, returns Certified for decisive recovery, and returns Abstain for unresolved queries. The evaluated C-MCR shared route reduced native CLIP R@1 from 0.524 to 0.290. The production fallback recovered 0.963 +- 0.002 of clean retrieval, while the passing branch recorded a no-harm value of 1.000. CertBind extends multimodal composability from connected representations to certifiable task decisions.

---


### 20. [GRASP: Reinforcing Language Model Anonymizers with Group Relative Policy Optimization](https://arxiv.org/abs/2608.06526)

**<font color=#1a73e8>作者：</font>** Sajjad Ghiasvand, Nader Sehatbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can infer sensitive personal attributes, such as age, location, and occupation, from ordinary text, turning everyday writing into a privacy risk. Adversarial anonymization defends against this by rewriting a text with a capable language model that also plays the attacker, but it needs a powerful model at inference time and thus sends private text to a third party, the very exposure anonymization should prevent. Recent work distills this behavior into a small on-device model using supervised fine-tuning and direct preference optimization (DPO), but DPO only imitates the teacher's offline choices and never directly optimizes the privacy--utility objective we care about. We introduce \textbf{GRASP} (\textbf{G}roup-\textbf{R}elative \textbf{A}nonymization via \textbf{S}elf-refinement \textbf{P}olicy-optimization), which reinforces the local anonymizer online with Group Relative Policy Optimization. A single small model acts as anonymizer, adversary, and utility judge, trained against a self-generated reward that hides attributes while preserving meaning, with a design that guards against reward hacking. Trained on Llama-3.1-8B, \ours{} improves the privacy--utility trade-off over the DPO-distilled baseline, consistently across three independent LLM judges. Against adversarial anonymization driven by frontier models such as Gemini~2.5~Flash and Claude, it achieves a comparable or better overall trade-off while removing substantially more private information, and it runs entirely on-device at roughly $1\%$ of the GPT-4o teacher's cost.

---


### 21. [Lost in Interpolation: Why Predictive Feedback Fails in Diffusion Language Models](https://arxiv.org/abs/2608.06529)

**<font color=#1a73e8>作者：</font>** Lavanya Nigam, Ishaan Bansal, Aryan Sood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Soft-masking accelerates the convergence of Masked Diffusion Language Models (MDLMs). Existing formulations build this blend with linear interpolation (LERP) in the raw embedding space, which implicitly treats that space as Euclidean. We analyze the embedding space of MDLMs and find that the mask and predicted-token embeddings maintain a near-constant angle of (\approx 73^\circ) throughout training, while embedding norms remain essentially flat across vocabulary-frequency rank. These indicate a hyperspherical geometry, for which LERP is the wrong interpolation primitive. We introduce Spherical Soft-Masking (S-SM), a drop-in replacement that aggregates the top-(k) predictions with a Fr'echet mean on the hypersphere and blends this mean with the mask direction using spherical linear interpolation (SLERP), then restores the native mask norm. We evaluate S-SM on continued pre-training of a released 169M-parameter MDLM checkpoint across a wide range of inference-time step budgets, SLERP feedback avoids the training degradation that LERP feedback induces and delivers MAUVE gains of up to 2x over the vanilla MDLM baseline and 27.5-56.1% over TopK/LERP at various sampling budgets, alongside consistently lower generative perplexity (16.9-19.6% over the baseline), while leaving output entropy and convergence essentially unchanged.

---


### 22. [Confidence Estimation for Financial Vision-Language Models in Chart and Document Understanding](https://arxiv.org/abs/2608.06532)

**<font color=#1a73e8>作者：</font>** Reza Khanmohammadi, Simerjot Kaur, Charese H. Smiley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LVLMs are increasingly used to read financial charts, tables, and documents, where a single misread figure can move a decision and the most authoritative-looking answer is sometimes one the model produced without reading the exhibit. The operational question is therefore trust, not accuracy: which answers can be acted on, and which escalated to a reviewer. We evaluate seven confidence estimators, three inference-only and four trained internal probes, across five open-weight LVLMs and four conditions from three financial visual question-answering benchmarks, one bilingual; every probe is trained only on natural images and applied to finance without adaptation, so the results measure out-of-distribution transfer. Three findings hold. First, the scarce property is calibration, not ranking: the inference baselines rank correct above incorrect answers competitively but are badly overconfident, calibration error far above what a threshold can tolerate, and only the trained probes produce a thresholdable score. Second, reliability is structured rather than global, along two axes a practitioner can read directly: the best estimator shifts with both model and task, none leading more than eight of twenty (model, condition) cells, and a controlled bilingual contrast exposes an apparent language robustness as a composition artifact that dissolves once models are read one at a time. Third, cast as deferral under an error budget, how much can be safely automated is set first by the model's competence and only narrowed by its confidence, so deferral clears a real share of the easiest condition and almost none of the hardest, near zero at a strict 5% budget. Two trained probes carry the calibration a deferral policy needs, and among them only the grounding-aware one lowers its confidence on answers a model gives without using the figure, separating detected non-grounding from a fluent guess.

---


### 23. [TaskSense: Focusing on What Matters in World Models](https://arxiv.org/abs/2608.06544)

**<font color=#1a73e8>作者：</font>** SM Mazharul Islam, Manfred Huber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models for visual control typically learn compact latent states by reconstructing observations, implicitly encouraging representations to preserve information across the entire visual input. However, task-relevant content often occupies only a small fraction of the observation, while background clutter and distractors consume valuable representational capacity. This mismatch between visual reconstruction and control objectives biases latent representations to model task-irrelevant visual content, diluting learning signals for control-relevant features and severely degrading downstream performance under visual distractions. We introduce TaskSense, a task-centric world modeling framework that enforces task relevance before latent encoding through a differentiable stochastic spatial attention mechanism conditioned on the previous latent state. To steer attention toward control-relevant regions, we augment training with an auxiliary inverse-dynamics objective. Rather than reconstructing the full observation, the world model reconstructs only the attended regions, encouraging latent representations to preserve task-relevant information while discarding irrelevant visual content. The decoder is further conditioned on the sampled attention map, enabling consistent reconstruction despite stochastic attention. Compared with the DreamerV3 baseline, TaskSense maintains competitive performance on the DeepMind Control Suite while consistently outperforming DreamerV3 on the Distracting Control Suite, demonstrating substantially improved robustness to visual distractions. Qualitative analysis further confirms that the learned attention, guided by inverse-dynamics supervision, consistently localizes control-relevant regions while suppressing irrelevant visual content.

---


### 24. [Robust Average-Reward Markov Decision Processes: Minimax-Optimal Learning via Plug-in Reductions](https://arxiv.org/abs/2608.06545)

**<font color=#1a73e8>作者：</font>** Yuepeng Yang, Yuxin Chen, Yuejie Chi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributionally robust Markov decision processes provide a principled framework for sequential decision making under model uncertainty. We study how many samples are necessary and sufficient to learn an $\varepsilon$-optimal robust policy under the average-reward criterion. A generative model provides samples from the nominal transition kernel, whereas policy performance is evaluated over $(s,a)$-rectangular total-variation uncertainty sets of radius at most $\sigma$.
Let $H_0$ and $H_\sigma$ denote the nominal and robust optimal bias spans, respectively. We identify $\sigma H_0$ as the perturbation scale separating high- and low-tolerance regimes. Our matching upper and lower bounds show that, up to logarithmic factors, the minimax total sample complexity is $$ NSA \asymp \frac{SA}{\varepsilon^2}\begin{cases} \min\{H_0,H_\sigma\}, & \varepsilon\gtrsim\sigma H_0,\\ \min\{H_0,H_\sigma\}+\sigma H_\sigma^2, & \varepsilon\lesssim\sigma H_0. \end{cases} $$ Here $S$ and $A$ are the numbers of states and actions, and $N$ is the number of samples per state-action pair. The sample complexity consists of a linear-span term that resembles the nominal AMDP results and a robustness-specific term that appears only in the low-tolerance regime. We attain these rates using reduction-based plug-in procedures that select the reduction---nominal or robust---and its discount factor: a span-informed procedure that makes these choices using known span parameters, and a span-agnostic procedure that calibrates both choices from data.

---


### 25. [Bootstrap-Conditioned Action Selection with Tabular Foundation Models](https://arxiv.org/abs/2608.06559)

**<font color=#1a73e8>作者：</font>** Devansh Gupta, Shiv Tavker, Dmitry Efimov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandits offer a natural framework for sample-efficient personalization, but practical deployment remains difficult under sparse, biased interaction data, unreliable uncertainty estimates, and severe cold starts. We study whether pre-trained tabular foundation models with in-context learning can be turned into randomized policies for online decision making. We propose BC-ICL (Bootstrap-conditioned action selection using ICL), which at each round draws a bootstrap resample of the interaction history, conditions a frozen pre-trained ICL model on that resample, scores all actions, and selects the action with the highest sampled score. We further introduce an arm-context conditioning architecture that promotes shared statistical strength across actions and helps avoid common bootstrap failure modes of isolated-arm bandits. Empirically, this policy delivers strong early-round regret and regret performance on standard contextual bandit suites, outperforming established baselines under a strict online protocol.

---


### 26. [Divergent Response Modes in Frontier Language Models Under Steering Pressure](https://arxiv.org/abs/2608.06578)

**<font color=#1a73e8>作者：</font>** Ali Jalal-Kamali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models are trained using distinct data, objectives, and safety pipelines. Whether these differences produce measurably different behaviors under explicit steering pressure remains underexplored. This study evaluates behavioral steerability across six frontier models from six developers using 300 paired base and steered items over three categories: values-conflict, reasoning-elicitation, and reasoning-suppression (plus 40 validation items). All six models act as blind peer judges and classify every response based on fixed behavioral rubrics. The resulting 24,480 judgments are scored by leave-one-out consensus. We find that models differ not just in how much steering shifts their behavior but in what kind (mode) of response they give, and some response modes appear in only one or two of them. GPT-5 deflects requests to disclose its reasoning while leaving its answer intact (99% vs. 0% for all other models). Claude Opus 4.7 and GPT-5 resist explicit suppression instructions and in different ways. Using Llama as the open-weight model, we trace the largest behavioral split to its internals. A linear probe decodes the behavior from the residual stream at 0.87 held-out accuracy while injecting that direction during generation drives the behavior from 0% to 86% across an intervention sweep. Every finding holds under both a token-budget remediation and a control experiment with a hypothesis-blind judgment prompt.

---


### 27. [CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](https://arxiv.org/abs/2608.06582)

**<font color=#1a73e8>作者：</font>** Kaixiang Su, Hongfei Xue, Qiang Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-based generative models can efficiently produce candidate structures for crystal structure prediction (CSP), but their pretrained objectives do not directly optimize downstream target recovery. Reinforcement-learning post-training offers a flexible solution, yet existing approaches rely primarily on energy rewards and coordinate-only stochastic policies. Predicted energy does not identify the reference polymorph, while reward-driven concentration can reduce the candidate coverage required for Top-N recovery. We introduce CrystalGRPO, a CSP-aligned post-training framework that extends existing ODE-to-SDE policy constructions to the joint coordinate--lattice state. CrystalGRPO combines MACE-predicted energy with a StructureMatcher-based recovery score and provides two operating modes: CrystalGRPO-Q, which prioritizes single-draw recovery, and CrystalGRPO-C, which combines full-trajectory reference regularization with a coverage-aware group advantage to preserve finite-budget target recovery. Across MP-20 and MPTS-52 with PXRDGen and OMatG backbones, both variants reduce one- and twenty-sample RMSE relative to coordinate-only reinforcement in all four backbone--dataset settings. CrystalGRPO-Q consistently improves Top-1, whereas CrystalGRPO-C achieves a higher Top-20 across all settings.

---


### 28. [Beyond "AI Language": The case for the idiolectal nature of LLM output](https://arxiv.org/abs/2608.06589)

**<font color=#1a73e8>作者：</font>** Karolina Rudnicka, Thomas Stephan Juzek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language model outputs are frequently analysed as a collective super variety termed "AI language," this chapter argues that this perspective coexists with distinct, model-specific linguistic signatures akin to human idiolects. We analyse two datasets of LLM-generated texts on societal topics: a 2024 corpus of six models (Improta et al. 2024) and a newly generated 2026 corpus using the same prompts featuring six contemporary models. Our findings, utilising computational descriptors and stylometric principal component analysis reveal a generational shift between the style of the 2024 and 2026 cohorts, while demonstrating that each individual model maintains a unique linguistic profile. This multi-layered interplay is illustrated by contraction frequencies, which vary from over 1,200 to over 30,000 per million words within the same cohort of models (2026). Ultimately, we conclude that treating LLM output as idiolectal in nature provides a valuable framework with potential implications for research on variation and change, LLM-generated text detection, forensic linguistics and usage-based approaches to language.

---


### 29. [Automated item evaluation: Predicting item acceptance and rejection using LLM-generated critiques](https://arxiv.org/abs/2608.06609)

**<font color=#1a73e8>作者：</font>** Hotaka Maeda, Yikai Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated item evaluation (AIE) refers to the use of computational methods to assess item quality without requiring manual expert review or field testing of the items under evaluation. We aimed to build a near-comprehensive AIE model by predicting item acceptance and rejection from item text using historical rejection data from a large-scale standardized testing program. The dataset contained 52,759 English language arts (ELA) and mathematics items with 34% permanently rejected from future operational use. Rejection reasons included poor psychometric properties, content issues, bias and sensitivity concerns, and non-content issues. We fine-tuned a DeBERTaV3-large classifier on raw item text, a second DeBERTa classifier on Qwen3-generated item critiques, and a fusion model combining representations from both. The fusion model achieved the strongest overall performance (Accuracy = .75, F1 = .64, AUC = .80, Sensitivity = .64, Specificity = .81). Prediction for math (F1 = .73, AUC = .86) was considerably more accurate than ELA (F1 = .51, AUC = .72). Lowering the decision threshold from .5 to .25 raised average sensitivity for ELA and math to .88 and .91, while reducing specificity to .31 and .56, respectively, which may be preferable in automated item generation contexts where generating items is cheaper than evaluating them. Incorporating item critiques alongside raw item text improved performance across most rejection reasons. The model assigned higher rejection probabilities to more difficult items. However, the fusion model struggled to identify items flagged for bias, sensitivity, fairness, or accessibility, especially for ELA. These findings suggest that text-based AIE is feasible in some areas and may offer a practical tool for reducing the burden of manual review and field testing, while also underscoring the importance of human review for items with fairness concerns.

---


### 30. [Do 3D Medical Foundation Models See Through MRI Artifacts? A Controlled Study of Representation Robustness](https://arxiv.org/abs/2608.06613)

**<font color=#1a73e8>作者：</font>** Julia Anna Mielcarz, Daniel Klaaby, Mostafa Mehdipour Ghazi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised 3D medical foundation models are increasingly used as general-purpose feature extractors, yet their sensitivity to MRI artifacts remains poorly understood. We present a controlled evaluation of representation robustness across five pretrained 3D encoders spanning different architectures, objectives, pretraining domains, and dataset scales. Using BraTS-Africa cases with four MRI sequences, we generate seven frequency- and image-domain artifacts at five predefined corruption settings. Robustness is assessed using linear centered kernel alignment (CKA), RankMe, and UMAP, complemented by an independent segmentation-consistency analysis. We find that robustness is strongly model- and artifact-dependent. 3DINO exhibits the most consistently stable representations, while BrainIAC is highly sensitive to several corruptions; NeuroVFM, BrainFM, and Neuro-SimCLR show intermediate but distinct artifact-specific profiles. Across many conditions, CKA decreases substantially while RankMe remains comparatively stable, indicating that artifacts often distort representation geometry without causing dimensional collapse. Segmentation consistency also degrades under corruption, particularly for ghosting and Rician noise, but aligns only partially with representation-level robustness. These findings show that larger-scale or domain-specific pretraining alone does not guarantee artifact invariance and motivate explicit robustness evaluation before deploying 3D foundation models in heterogeneous MRI settings.

---


### 31. [Retrofitting Linear Attention into Diffusion Language Models](https://arxiv.org/abs/2608.06628)

**<font color=#1a73e8>作者：</font>** Jinha Kim, Younghun Roh, Jaeyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding. Recent dLLMs commonly use blockwise semi-autoregressive decoding, generating blocks autoregressively while denoising tokens within each active block in parallel. However, despite KV caching, each denoising step still attends to all previous blocks, repeatedly incurring prefix-attention cost. Motivated by this bottleneck, we ask whether dLLM inference can be further accelerated by linearizing attention over previous blocks. We introduce block-hybrid attention, which retains exact softmax attention within the active denoising block while applying linear attention over previous blocks. We show that this hybrid attention can be retrofitted into a pretrained dLLM with minimal post-training: LLaDA-Hybrid replaces 6 of the 20 attention layers in LLaDA~2.1, a 16B open-source dLLM, largely following LoLCAT (Zhang et al, 2024). The conversion takes only approximately 60 hours while preserving benchmark performance: 72.0% vs. 75.6% on HumanEval, 63.0% vs. 57.7% on MBPP+, and 86.7% vs. 88.3% on CMATH. With a Triton implementation, LLaDA-Hybrid achieves up to $1.7\times$ higher decoding throughput and supports more concurrent requests before exhausting memory, showing that pretrained dLLMs can be efficiently linearized for faster inference. Our code is available at: this https URL.

---


### 32. [The Sparsity Whisperer](https://arxiv.org/abs/2608.06630)

**<font color=#1a73e8>作者：</font>** Linghao Kong, Inimai Subramanian, Micah Adler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs. We argue that this overlooks a key computation performed by particularly sparsity-sensitive neurons in the MLP up and gate projections: separating similar inputs into dissimilar outputs. This suggests that effective pruning should preserve not only activations, but also the differences between outputs more broadly. We introduce a family of difference-informed pruning methods built upon this principle. Wisp is a first-order, update-free method that scores weights using input-difference norms, and Wisp+ refines this score neuronwise using the input pairs each neuron separates most strongly. Finally, Whisper is a second-order method that uses a lightly regularized difference Hessian as its reconstruction objective. Across Llama 2 and 3.1 models from 7B to 405B parameters, our second-order variant consistently improves over strong reconstruction-based baselines, while our update-free variants improve over activation-aware baselines, especially in constrained settings. The improvements over Wanda and SparseGPT extend to structured sparsity, downstream evaluations, and other model families. Augmenting stronger techniques such as RIA and ALPS with our difference-informed criteria yields further improvements, shifting the overall accuracy-runtime frontier outward at negligible additional cost. These results suggest that preserving output differences is a broadly useful and composable signal for post-training LLM sparsification.

---


### 33. [Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation](https://arxiv.org/abs/2608.06632)

**<font color=#1a73e8>作者：</font>** Ziyun Xu, Bosen Ding, Yue Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial recommendation systems predominantly adopt a passive ranking paradigm that infers user preferences from implicit behavioral signals (e.g., clicks, dwell time) rather than explicit, natural language inputs. As a result, users experience a persistent discrepancy between their explicit interests and what passive behavioral algorithms deliver, limiting their ability to express nuanced preferences or steer their feed in real time. To address this growing gap between how recommendations are optimized and how users wish to articulate their interests, we present Shape Your Feed (SYF), an LLM-based agentic recommendation framework that enables real-time, multimodal co-curation of content. SYF employs a three-tier architecture: (i) a Perception Flow that captures fine-grained user intent from text prompts, voice commands, and UI interactions; (ii) a Serving Flow that performs real-time agentic re-ranking and pruning of candidate items, grounded in a persistent Semantic Profile encoding evolving user preferences; and (iii) a Self-Evolution Flow that aligns system behavior with human judgments via Direct Preference Optimization (DPO) and an LLM-as-a-Judge ensemble. Offline evaluations show that SYF's alignment scoring module achieves 98.85% accuracy, substantially improving over strong few-shot baselines. Large-scale online A/B experiments on production traffic further demonstrate that SYF improves feed relevance and user sentiment, indicating a practical and scalable path toward interactive, user-steerable recommendation in industrial settings.

---


### 34. [CellWorld: From Gene-Level Reconstruction to Latent Cell Prediction in Spatial Transcriptomics Foundation Models](https://arxiv.org/abs/2608.06659)

**<font color=#1a73e8>作者：</font>** Haiping Liu, Qian Zhao, Lijing Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper shows that latent-space predictive pretraining can provide a scalable route to foundation models for spatial transcriptomics. Existing spatial transcriptomics foundation models primarily reconstruct masked gene identities or expression values, potentially encouraging the reproduction of assay-specific technical variation and limiting representation transferability. To avoid directly reconstructing such variation, we shift the prediction target from observed gene measurements to latent cell representations and introduce CellWorld, which predicts the latent representations of masked cells from visible spatial context and a limited partial-expression hint. We pretrain four CellWorld variants, spanning 5.74M to 94.56M trainable parameters, on a corpus of 46 million human cells. Our controlled scaling experiments show that performance improves with model capacity, particularly on spatial tasks, while spatial transfer depends more on sufficient optimization and broad biological source diversity than on cell count alone. Across four held-out datasets, even CellWorld-Small, with 5.74M trainable parameters, outperforms every baseline on all 11 linear-probe benchmarks and all seven fine-tuned spatial benchmarks. Most notably, a frozen CellWorld-Large pretrained on only 5\% of the corpus with broad biological source coverage outperforms every fully fine-tuned baseline across all seven spatial benchmarks. Code is available at this https URL.

---


### 35. [The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.06663)

**<font color=#1a73e8>作者：</font>** Mingguang Chen, Licheng Wang, Bo Qu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of earlier decisions, declaring half-finished work done, or drifting from goals. We call this the horizon gap and survey 1,547 arXiv papers (2024-2026) collected via systematic seed harvest with a disclosed 26.8% bleed filter, extended by targeted supplementation. We disambiguate three routinely conflated properties: long-horizon (task property: required steps), long-context (model property: token capacity), and long-term memory (system property: persistence across steps/sessions). We organize the corpus into six categories tracking a long-horizon task's lifecycle -- planning, memory, execution, training, evaluation, and foundations/safety -- crossed with an axis capturing where horizons are carried (within-context, within-task-beyond-context, or cross-task-persistent). Across all categories, we find the same pattern: outcome-only signals grow uninformative as horizons lengthen, and the field's response -- whether process reward models, credit assignment, or trajectory-level diagnostics -- manufactures denser step-level signals. We treat critical and diagnostic literature as first-class threads throughout, arguing that segregating critique from method would routinely split single papers across chapters. We close by naming open measurement problems: decomposing model versus harness capability, managing correlated bias in process-level signals used for both training and evaluation, and whether long-horizon reliability admits general predictive theory.

---


### 36. [TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation](https://arxiv.org/abs/2608.06672)

**<font color=#1a73e8>作者：</font>** Yong-Bin Kang, Anthony McCosker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a robust architecture for grounding large language models (LLMs) in trusted knowledge. However, standard RAG systems exhibit a structural limitation: retrieved documents carry their own communication styles-professional jargon, formal tone, or academic writings-that shape the behavior of a RAG system before any tone instructions are processed, often causing the system to ignore user requests for a specific tone. We term this phenomenon contextual decoupling, in which a system optimises for factual accuracy while remaining decoupled from the social or operational context of the recipient. Building on prior research in public health peer-support communities, we identify three communicative misalignment-linguistic, cognitive, and relational-that can persist even when retrieval is relevant and the generated response is factually accurate. We conceptualise these as failures of communicative transformation, which remain largely invisible to accuracy-centred RAG evaluation metrics. To address this gap, we propose Tone-Aware RAG (TA-RAG), a conceptual architectural framework that positions communicative alignment alongside factual accuracy as a core design objective. TA-RAG operationalises four constraints-stigma-free language, readability alignment, recipient-sensitive adaptation, and empathetic framing-across the retrieval, context construction, generation, and constraint validation phases in the proposed RAG pipeline. We further highlight an evaluation agenda for jointly assessing factual fidelity and communicative alignment, and identify open challenges. We argue that tone awareness should be treated not as an optional refinement, but as a present design imperative for RAG systems operating in socially sensitive and high-stakes contexts.

---


### 37. [AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models](https://arxiv.org/abs/2608.06699)

**<font color=#1a73e8>作者：</font>** Zibo Shao, Baochen Xiong, Chengdong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic multimodal large language models (MLLMs) extend multimodal perception and reasoning with planning, tool use, and interaction in dynamic environments. Yet current models are specialized for particular tools or environments, complicating consolidation into a single generalist. We formulate Agentic MLLM Merging and identify two challenges: asymmetric capability preservation, whereby capabilities with different interaction complexity are retained unevenly, producing weak tasks after merging, and behavior-critical forgetting, whereby losing decisive actions can derail long-horizon execution. We propose AgentPatch, a training-free coarse-to-fine repair framework. It selects a stable merged backbone, restores diluted weak-task-specific signals through Weak-Task Unique Residual Recovery, and applies an Agent-Guided Behavior-Critical Patch that recovers decisive behaviors under explicit capability protection. AgentPatch produces a single static checkpoint without routing or ensembles. Experiments across six agentic and multimodal benchmarks show that AgentPatch improves diverse merged backbones, alleviates weak-task degradation, and better balances weak-task recovery with the preservation of complementary search and agentic visual processing capabilities. Code is available at this https URL.

---


### 38. [Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection](https://arxiv.org/abs/2608.06706)

**<font color=#1a73e8>作者：</font>** Jiazhuo Li, Yiming Fei, Zhiruo Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models plan by predicting future states from an action, but when a scene contains motion the agent does not control, they quietly go action-blind: predictions for different actions become indistinguishable even as the training loss keeps improving. Existing remedies suppress this distraction with reconstruction, task reward, or auxiliary objectives, each adding machinery or assumptions. We show that a minimal alternative suffices, borrowed from the dueling decomposition of value into a state baseline and an action advantage: in latent dynamics, subtracting a prediction's mean effect over actions cancels whatever the actions share--the action-independent variation where distractors live--leaving a clean, controllable channel, with no reward, no reconstruction, and no distractor-specific auxiliary loss. Because this is only a subtraction at readout time, it applies unchanged to any action-conditioned world model, including frozen pretrained ones. Across a gridworld, synthetic generators with known factors, distracting continuous control, and natural-pixel Atari, the isolated channel recovers the agent's own effect where entangled predictors fail, with nuisance leak indistinguishable from zero; applied post hoc it surfaces an action channel in off-the-shelf models that their raw readouts miss, and it converts into goal-reaching control in the gridworld. We prove the cancellation is exact in finite samples for both discrete and sampled action sets, and we state its measured boundary--distractors whose motion tracks the action--together with the remaining limitations in the appendix.

---


### 39. [Do Audio Language Models Use Paralinguistic Evidence? Counterfactual Audits for Response Evaluation](https://arxiv.org/abs/2608.06718)

**<font color=#1a73e8>作者：</font>** Kevin Miller, Arjun Chandra, Venkatesh Saligrama  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio-language models (ALMs) are increasingly used as judges for speech-to-speech systems, but a judge that receives audio may not actually use paralinguistic evidence. We introduce counterfactual audits for paralinguistic response evaluation. Each audit item holds the transcript fixed while varying affect, prosody, or the timing of an affective shift, forcing a valid judge to track the audio cue rather than lexical content or response style. We evaluate ALM judges using a native one-context judgment protocol and a contrastive recoverability control, then further decompose each item into its constituent perception and response-mapping skills. This yields useful diagnostic states that identify different sources of judge failures. Across Gemini, GPT, and open audio models, we find that contrastive success often overstates native judge reliability, and that similar aggregate accuracies can hide different failure modes. These results suggest that ALM judges should not be evaluated by accuracy alone, instead requiring thorough behavioral audits before deployment.

---


### 40. [CustomDance: Customized 3D Dance Generation with Coarse-to-Fine Human-Centered Interactive Control](https://arxiv.org/abs/2608.06722)

**<font color=#1a73e8>作者：</font>** Xulong Tang, Kaixing Yang, Xiaohu Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rise of AI-generated content (AIGC) and advanced techniques for 3D human representation, the task of generating 3D dance movements has become an exciting area of research. Despite significant advancements, current methods often fail to provide comprehensive and distinct control over various multimodal inputs from users, such as music or specific descriptions of desired movements. As a result, the generated motions may be statistically plausible and technically correct, but they often lack depth, expressiveness, and alignment with the user's creative vision. To address this issue, we present CustomDance, a coarse-to-fine interactive system designed for customized 3D dance generation. Inspired by the workflows of expert choreographers, CustomDance introduces a novel paradigm to AI-assisted choreography through three interconnected stages. First, a multimodal Large Language Model (MLLM) analyzes the music and a high-level text prompt to identify key temporal anchors and creative cues for the piece. Next, for each anchor, a multimodal retriever suggests high-quality motion clips from a dance library based on local music and text, empowering the user with concrete and predictable options. Finally, a custom music-conditioned diffusion in-painter seamlessly connects the selected phrases, allowing for iterative, user-guided refinement of the final composition, supported by visualizations of motion dynamics. Our evaluations demonstrate that CustomDance not only highlights the significant creative utility and empowering potential of our AI-assisted choreography paradigm, but also outperforms competitive baselines across quantitative and qualitative comparisons.

---


### 41. [Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors](https://arxiv.org/abs/2608.06723)

**<font color=#1a73e8>作者：</font>** Saeid Shokoufa, Mohammad Erfan Sadeghi, Mehdi Kamal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design. In this work, we introduce Hybrid Modeling for Energy and Latency of LLMs (HYMELL), a hybrid three-level framework for estimating LLM inference latency and energy by combining analytical modeling with machine learning (ML). HYMELL models LLM execution through a three-level hierarchy: analytical estimation of primitive operations, ML prediction of higher-level components, and an end-to-end model that captures system-level overheads across both prefill and decode phases. The framework supports diverse architectures, including dense and mixture-of-experts (MoE) feed-forward networks (FFNs), as well as multi-head attention (MHA) and grouped-query attention (GQA) mechanisms. Evaluated on an NVIDIA H100 graphics processing unit (GPU), HYMELL achieves high predictive accuracy; notably, for LLaMA 3 8B, it attains less than 5% error for both prefill and decode phases. By predicting execution costs directly from architectural parameters, it enables fast, hardware-free design space exploration and energy-efficient optimization.

---


### 42. [IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents](https://arxiv.org/abs/2608.06735)

**<font color=#1a73e8>作者：</font>** Senhao Wang, Chenghao Cai, Haitao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has achieved strong results in improving large language models (LLMs) on tasks with stationary, verifiable rewards, such as mathematical reasoning and code execution. In these settings, the environment follows fixed rules and does not adapt strategically to the agent. Strategic dialogue differs in this respect: the environment is another agent that adapts to the policy, and success depends on the interaction between the two sides. Despite this interactive nature, current RL approaches typically train a target agent against a fixed counterpart or simulator. We find that this training paradigm encourages the policy to exploit counterpart-specific regularities rather than learn strategies that generalize across counterparts. We call this problem the static-counterpart mismatch, which we quantify directly in our experiments. To address it, we propose Isolated Bilateral Reinforcement Learning (IB-RL), in which the two roles coevolve through joint rollouts while each role optimizes its own reward through fully independent advantages, action masks, and update paths. We evaluate frozen policies against fully independent held-out counterparts in both domains. On Vehicle TeleSales, IB-RL achieves 89.6% Success@1, compared to 84.6% for the best unilateral RL baseline. On Deal-or-NoDeal, it reaches 98.4% agreement against DeepSeek V4 Pro, compared to 86.4% for the best unilateral baseline. These results indicate that jointly training both roles with strict peragent isolation produces policies that generalize more effectively to unseen counterparts.

---


### 43. [Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference](https://arxiv.org/abs/2608.06752)

**<font color=#1a73e8>作者：</font>** Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes DKG-MTI, a dual knowledge graph framework for unified multi-task user intent inference from online travel reviews. Existing approaches often rely on hierarchical pipelines that suffer from error propagation or retrieval methods that ignore structural relationships in domain knowledge. To address these limitations, we introduce an inference-only knowledge augmentation framework that dynamically constructs a User-Specific Intent Knowledge Graph from each review and aligns it with a Global Hotel Knowledge Graph through structure-aware semantic smoothing. The aligned knowledge is combined with the original review and processed by a large language model to simultaneously predict aspect ratings and generate reverse user intent statements. Experiments on TripAdvisor reviews show that DKG-MTI consistently outperforms strong LLM and retrieval-based baselines in both classification and intent generation tasks, demonstrating the effectiveness of structure-aware knowledge alignment for scalable and explainable intent inference.

---


### 44. [Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence](https://arxiv.org/abs/2608.06756)

**<font color=#1a73e8>作者：</font>** Ying Chen, Weizhen Li, Zhe Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly serving as the reasoning core of embodied agents. Robot execution is inherently iterative: each action reshapes the scene and physical state, continually renewing what must be perceived, reasoned about, and verified. Meeting these demands requires complementary capabilities that differ in supervision signals, prediction formats, and verification criteria. Existing approaches typically develop these capabilities against isolated, task-specific objectives, leaving open how they should be organized and integrated around execution as a whole. We present Capek 0.5, an embodied vision-language model built around an execution-centric capability taxonomy. Rather than organizing training by datasets or tasks, the taxonomy groups embodied capabilities according to their functional roles throughout execution and comprises four capability families: Spatial Reasoning, Temporal Understanding, Action Guidance, and State Verification. Each capability is first acquired by a dedicated specialist through reinforcement learning with verifiable rewards from a shared backbone, and the specialists are then consolidated into a single inference-time model through weight-space merging followed by routed policy-space distillation. We instantiate Capek 0.5 at the 2B and 35B-A3B scales and evaluate it from three complementary perspectives: comprehensive benchmark suites including Capek-StateBench, a new benchmark for state verification; a controlled study of capability retention from specialists to the unified model; and closed-loop evaluation in simulated embodied environments. Capek 0.5 improves the large majority of matched benchmark rows over its initialization, retains all four specialized capabilities in one checkpoint with quantified losses, and transfers to closed-loop embodied task execution.

---


### 45. [Sub-Quadratic Bisimulation Metrics via Approximate Nearest Neighbors: Coverage-Augmented Guarantees and Computable Two-Sided Certificates](https://arxiv.org/abs/2608.06762)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Joyanta Jyoti Mondal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bisimulation metrics quantify behavioral similarity in Markov decision processes, but their Wasserstein fixed-point operator updates every state pair and incurs quadratic pairwise work. We give a certificate-carrying sub-quadratic method for MDPs with bounded transition support and a useful low-dimensional indexing representation: an approximate-nearest-neighbor index selects the pairs updated by the exact restricted operator, while monotone lower and upper runs enclose the exact metric at every sweep. The main analytical result is a coverage-augmented anytime bound: local index quality alone cannot control global error, because uncovered pairs retain their initialization gap. The limiting error is at most $\max(\rho,\eop/(1-\gamma))$, and with exact covered backups the lower arm satisfies $\|\dann-d\|_\infty=\rho$. Because $\rho$ depends on the unknown exact metric, the algorithm returns the observable sandwich width instead; agreement of the induced lower and upper clusterings certifies exact recovery of the covered aggregation. A reward-oblivious lower bound shows sub-quadratic index-first coverage cannot remove the coverage term, while a separate adaptive lower bound requires $\Omega(|\Scal|)$ pair evaluations. Exact-operator experiments verify the identity and enclosure in every seeded run, and timing experiments recover quadratic versus sub-quadratic scaling under both cheap and full Wasserstein backups. On the grouped $|\Scal|=64$ benchmark, exact restricted refinement reaches the exact-metric skyline once retrieval covers roughly half of all pairs, while independently trained MICo and DBC baselines stay $22$-$33\times$ above that skyline at every retrieval budget. Taxi shows the certificate abstaining under an uninformative embedding, while a $2500$-state gridworld improves over a reward-only metric by $28.6\%$ using $12.8\%$ of one quadratic sweep.

---


### 46. [CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights](https://arxiv.org/abs/2608.06763)

**<font color=#1a73e8>作者：</font>** Xuetian Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight quantization for large-language-model inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution. Uniform integers constrain each group to a linear grid. Low-bit floating-point formats use a fixed exponent-mantissa structure, while learned codebooks gain flexibility at the cost of irregular decoding and additional metadata.
We introduce CubicQuant, a parametric non-uniform scalar format that preserves a dense integer code stream while adapting reconstruction levels within each weight group. A monotonic cubic curve, specified by two shape parameters and one scale, maps uniformly spaced magnitude codes to non-uniform levels. The family spans 1-8-bit weight payloads, contains symmetric uniform integer quantization as an exact special case, and has effective width B + 64/G bits per weight for payload width B and group size G. We derive population distortion under Uniform, Gaussian, and Laplace distributions, formulate continuous and Dynamic-A8-carrier-aware fitting objectives, and describe direct packed-weight GPU execution.
For finite groups of G=128 with 15,360 samples per distribution, W4 CubicQuant reduced reconstruction RMSE relative to optimally clipped four-bit uniform integer quantization by 3.90% on Uniform, 13.49% on Gaussian, and 28.14% on Laplace samples. Relative to the best enumerated four-bit finite floating-point format, the reductions were 3.90%, 9.44%, and 6.27%. Preliminary H200 kernel measurements show a workload-dependent crossover: model-dtype execution is faster for narrow GEMV, while Dynamic A8 becomes favorable as row count grows. The results establish the format's representational promise and direct executability; downstream model quality and cross-device end-to-end performance remain open evaluation questions.

---


### 47. [GraphVerse: A Comprehensive Visual Graph Reasoning Benchmark for Multimodal Large Language Models](https://arxiv.org/abs/2608.06769)

**<font color=#1a73e8>作者：</font>** Yuanfu Sun, Yuanhang Ren, Kang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Multimodal Large Language Models (MLLMs) have achieved remarkable progress across diverse vision-language tasks, creating an urgent need for more challenging benchmarks. Yet existing evaluations still provide limited insight into whether these models can truly reason over structured visual information. Visual Graph Reasoning (VGR) offers a compelling testbed for this challenge, requiring models to integrate perception, structural understanding, and multi-step reasoning over graph-based visual inputs. However, prior VGR benchmarks often reduce the task to visual perception followed by text-based reasoning, restrict evaluation to single-image settings, rely on answer-only metrics, and underrepresent realistic graph-centric scenarios. To bridge the gap, we introduce GraphVerse, a unified benchmark that jointly evaluates perception, visual reasoning, and text-based graph reasoning in MLLMs under both single-image and paired-image settings. At its core is a suite of Graph-centric Image Editing (GIE) strategies that modify graph images while preserving their semantics, turning them into active tests of visual reasoning. We further propose VGR-Score, a process-sensitive metric that evaluates reasoning quality beyond final-answer accuracy. Extensive experiments reveal several key limitations of current MLLMs in VGR, while also validating the effectiveness of GIE strategies and the transferability of GraphVerse to broader multimodal reasoning capabilities. The code is available at this https URL.

---


### 48. [Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts](https://arxiv.org/abs/2608.06770)

**<font color=#1a73e8>作者：</font>** Rulin Zhou, Wanhao Liu, Guoheng Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Controllable surgical world models can provide a generative foundation for surgical artificial intelligence and simulation by synthesizing realistic instrument--tissue interactions. However, existing methods lack a unified multimodal control paradigm, while direct fusion of heterogeneous visual conditions often causes anatomical distortion, instrument appearance drift, and temporally inconsistent interactions. In this work, we propose {Surg-UniWorld}, a unified surgical world model with multimodal control experts. Surg-UniWorld first constructs a {Hierarchical Surgical Anchor} from first-frame appearance and hierarchical semantic masks to preserve persistent scene identity, anatomical organization, and interaction boundaries. {Anchor-Relative Modality Experts} then interpret edge, depth, and optical-flow evidence relative to the shared anchor, capturing complementary boundary, geometric, and motion information. A {Multimodal Control Expert} further performs contribution-preserving stage-wise composition of the activated modality increments and generates control hints for the Wan2.2 video diffusion backbone. To support multimodal surgical world modeling, we further construct Cholec80-SurgWAM, a benchmark for controllable surgical video generation. Extensive experiments demonstrate that Surg-UniWorld consistently outperforms existing controllable video generation methods and surgical world-model baselines in generation quality, temporal consistency, and multimodal controllability.

---


### 49. [Evolving Parallel Algorithm Portfolios via Potential-Aware Instance Generation with LLMs](https://arxiv.org/abs/2608.06808)

**<font color=#1a73e8>作者：</font>** Shaofeng Zhang, Shengcai Liu, Zhiyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Automatic Construction of Portfolios via Large Language Models (LLM-ACP) suffers from poor generalization in practical few-shot scenarios when solving complex combinatorial optimization problems. Instance and algorithm co-evolution frameworks address this by expanding the training dataset with generated hard instances on which the current algorithm portfolio underperforms, thereby enhancing generalization. However, this paradigm faces two critical limitations: evaluating instance hardness relies on high-quality reference solutions, and single-mode generation patterns limit instance diversity. To overcome these limitations, we introduce the Potential-aware Instance and Algorithm Co-evolution (PIAC) framework. Our core contribution is twofold. First, we propose potential gain, a novel metric that eliminates the need for reference solutions. This metric estimates generalization gain by perturbing the generated algorithms and assessing their improvement potential on generated problem instances. Second, PIAC leverages LLMs to synthesize diverse instance mutators, exploring a broader region of the problem-instance space and thereby enhancing the portfolio's generalization capabilities. Given that perturbation spaces vary across different algorithms, we instantiate our framework on Greedy Constructive, Ant Colony Optimization, and Guided Local Search algorithmic backbones. Comprehensive evaluations on the Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP) across six distinct data distributions demonstrate that PIAC consistently outperforms state-of-the-art LLM-ACP baselines, notably achieving a 19.76% relative improvement for TSP Greedy Constructive portfolios.

---


### 50. [FutureBridge: Token Selection Beyond Local Preference in Collaborative Decoding](https://arxiv.org/abs/2608.06819)

**<font color=#1a73e8>作者：</font>** Quanquan Li, Hongbo Zhang, Yihe Chi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token-level collaboration allows a large language model (LLM) to assist a small language model (SLM) when their predictions diverge. Existing methods either use LLM-generated intervention tokens or rank candidates with the LLM's next-token probabilities. Both rely on the LLM's local preference, even though an LLM-selected token may be difficult for the SLM to build on. We present FutureBridge, which ranks joint LLM-SLM token candidates according to how well they support the SLM's subsequent reasoning. During training, an answer-verified LLM trajectory supplies a fixed shared future, and a frozen SLM evaluates every candidate under this common context. The resulting counterfactual scores supervise a lightweight token reranker that observes only the current state and candidate token. At inference, FutureBridge uses the LLM only to expand the candidate pool, selects one token, and returns generation to the SLM without generating or appending a future suffix. Across five mathematical reasoning benchmarks, FutureBridge improves the Qwen3-1.7B SLM's Math Avg. by 35.1% relative to greedy SLM decoding. These results indicate that token selection benefits from modeling whether the receiving SLM can use each candidate to continue reasoning, rather than relying on the LLM's local preference alone.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-117](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
