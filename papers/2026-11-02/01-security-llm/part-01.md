# 🔐 大模型安全相关研究 | 2026年11月02日

> 本类共 **11** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files](https://arxiv.org/abs/2610.37738)

**<font color=#1a73e8>作者：</font>** Kashyap R Manjusha, Murali Emani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern agent frameworks allow users to provide Markdown files containing system prompts, tool descriptions, and skill definitions (e.g., this http URL), which are incorporated into the agent's context during initialization. In this work, we investigate whether this configuration mechanism can also serve as an injection channel: can a jailbreak embedded in a Markdown skill file propagate through an agent and induce prohibited behavior? To answer this question, we construct a LangChain-based question-answering agent whose system prompt is assembled from a user-provided Markdown file. We embed a jailbreak combining persona manipulation with a GPTFUZZER-based attack and evaluate its effectiveness across seven contemporary open-weight models using 270 forbidden questions spanning nine harm categories. Under a benign system prompt, the models exhibit near-complete refusal behavior, with a mean attack success rate (ASR) of just 0.5%. In contrast, the injected skill file raises the mean ASR to 45%, reaching 68.9% for individual models. We further evaluate two payload obfuscation strategies: an invisible zero-width character-based stealth payload and a phonetic payload based on grapheme-to-phoneme transformations. Neither outperforms the plain-text injection; notably, the phonetic variant reduces mean ASR to 30%. These findings identify Markdown skill files as an underexplored attack surface for AI agents and suggest that vulnerability to configuration-based jailbreaks depends more strongly on the underlying model than on the specific payload obfuscation technique.

---


### 2. [Agentic Backdoors via Pretraining Poisoning](https://arxiv.org/abs/2610.37741)

**<font color=#1a73e8>作者：</font>** Xinyan Hu, Pingbang Hu, Chloe Loughridge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI agent using a clean pipeline. Poisoning only 0.1% of the pretraining corpus with our new poison design implants the backdoor: the deployed agent executes the malicious command when the trigger is present while behaving normally on clean inputs. The attack success rate (ASR) increases with model scale, with the 4B model reaching roughly 92% ASR at a 0.1% poison rate and staying positive even when the poisoning rate drops to 0.0005%. Our code is available at this https URL.

---


### 3. [Jailbreak Connectivity: Towards Diverse, Transferable, and Universal Multimodal Large Language Model Jailbreak](https://arxiv.org/abs/2610.38091)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Ziqing Hu, Shuo Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are vulnerable to visual jailbreak attacks that bypass safety safeguards. Existing methods typically optimize isolated adversarial examples, limiting attack diversity, transferability, and generalization. We propose Jailbreak Connectivity (JC), a framework based on the observation that effective adversarial inputs can be connected through low-loss regions in image space. JC optimizes continuous adversarial paths: path sampling yields diverse jailbreak images, lightweight surrogate classifiers guide cross-model transfer, and a distribution-level objective enables universal attacks across harmful queries. On MM-SafetyBench, JC achieves average attack success rates of 84.01%, 85.77%, and 97.95% on Qwen3-VL-8B-Instruct, InternVL3.5-8B, and Gemma-3-12B-IT, respectively, exceeding the strongest baselines by up to 68.36 percentage points. In black-box evaluations, JC improves attack success rates over FigStep by 24.69 and 27.34 percentage points on GPT-5.6 and Gemini 3.1 Pro, respectively. These findings reveal structured vulnerabilities in MLLM safety alignment and inform more comprehensive security evaluation.

---


### 4. [Session-Bound Behavioral Watermarking for Autonomous LLM Agents](https://arxiv.org/abs/2610.38579)

**<font color=#1a73e8>作者：</font>** Md Facklasur Rahaman, Yong Xiang, Md Palash Uddin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly acting through Web interfaces and external tools. They produce trajectories. Those trajectories may pass through several intermediaries. They can store, modify, or dispute those trajectories. In Web-based agent deployments, trajectories may pass through APIs, marketplaces, and tool servers. As such, a copied or disputed log may not by itself reveal which agent owner produced it. Behavioral watermarking can embed ownership evidence in agent action choices. However, existing methods mainly address detection, removal, rewriting, or imitation. They do not directly test whether repeated observation of watermarked trajectories enables cross-session forgery by exploiting learned action preferences. We formulate this learned-forgery threat and propose AgentAnchor, a session-keyed behavioral watermark for owner attribution from trajectory logs. We derive each step key from a secret key, a fresh public session identifier, and semantic states of recent observations, while a guarded digest of the action-policy state diversifies linear coding rows. It embeds parity evidence through a KL-bounded exponential tilt, and a trusted verifier checks a disputed log without rerunning the agent, using wrong-key calibration and abstention.

---


### 5. [Rethinking LLM Jailbreak Evaluation: Continuous Risk Landscapes Beyond Binary Outcomes](https://arxiv.org/abs/2610.38595)

**<font color=#1a73e8>作者：</font>** Yukai Zhou, Wenjie Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A binary success indicator is a natural representation for discriminative tasks such as image classification under adversarial perturbations, where each input is mapped to a single prediction. However, generative tasks are fundamentally different: an LLM jailbreak prompt induces a distribution over open-ended trajectories, while a sampled response reveals only one path. Yet LLM jailbreak evaluation typically retains the binary response indicator underlying attack success rate, obscuring the surrounding structure of possible generations. We introduce a continuous, context-conditioned risk landscape over first-token branches, estimated by fixing candidate openings and repeatedly sampling their continuations. This continuous risk-landscape perspective reveals two complementary properties: current decoder exposure and safe rerouting capacity, which have been obscured by binary-indicator-based ASR. The resulting representation also provides a common basis for comparing clean prompts, attacked variants, and attack strength against a known adaptive defense. Across multiple target models and jailbreak attacks, we uncover risky branches beneath apparently safe outputs, identify qualitatively different ways attacks reshape the model's opening distribution, and show that attacks strongest before a defense do not necessarily remain the strongest after the adaptive defense reacts. These findings recast jailbreaks as deformations of the surrounding continuation-risk landscape, establishing a more informative foundation for understanding jailbreak behavior and developing safer language models.

---


### 6. [Discovering Jailbreaks via Curriculum of Models](https://arxiv.org/abs/2610.38833)

**<font color=#1a73e8>作者：</font>** Michał Burzyński, Noah T. Rossi, Shomit Basu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated jailbreak discovery aims to find prompts that elicit prohibited behaviors from safety-trained language models, helping developers identify vulnerabilities before deployment. One class of approaches uses reinforcement learning to train an investigator model to generate prompts that elicit a specified behavior from a target model. However, training directly against a safety-trained target is difficult because nearly all prompts are refused, leaving the investigator with a sparse reward signal. Prior work addresses this with the propensity bound (PRBO), a proxy reward estimated by sampling responses from a more compliant target, and then adjusting for how likely those responses would have been under the original target.
We introduce Curriculum of Models (CoM), an alternative method that trains the investigator against a sequence of modified versions of the target, progressing gradually from a version that readily exhibits the specified behavior to the original target. For jailbreak discovery, training begins against a target version that rarely refuses harmful requests, and advances to the next, harder version once the investigator reliably elicits the behavior from the current one.
We evaluate CoM on elicitation tasks involving CBRN materials, explosives, and illicit drugs, using two open-weight targets, gemma-4-31b-it and gpt-oss-120b. We compare against PRBO and direct training on the original target without a curriculum. When the investigator is trained to elicit a single behavior, CoM finds successful jailbreaks more reliably than either baseline. When trained on multiple behaviors simultaneously, the CoM-trained investigator can elicit held-out behaviors, though PRBO-trained investigators achieve higher success rates. Our results suggest that a simple curriculum over target models offers a promising approach for addressing sparse rewards in rare-behavior elicitation.

---


### 7. [Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection](https://arxiv.org/abs/2610.39122)

**<font color=#1a73e8>作者：</font>** Xinyan Wang, Xiaogeng Liu, Jun Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-evolving personal agents act for users and learn from user feedback. However, if an agent obeys an instruction that an untrusted third party hides in content, the third party gains control of the agent. Such indirect prompt injection (IPI) poses severe risks. We investigate whether self-evolution degrades the robustness of personal agents to IPI. To study this question, we design a controlled two-phase methodology. In the adaptation phase, the user asks the agent to read external content and complete the task described in it, a common request in daily use. The agent then learns from the user's feedback and improves itself as designed. In the test phase, a third party writes a similar task into new external content, but the user's test request does not authorize the injected task. Using this methodology, we build multiple tasks with diverse test instances in different domains for a real personal agent. Our extensive experiments reveal that self-evolution substantially degrades robustness to IPI. Specifically, compared with the base agent, which does not evolve from user feedback, the average attack success rate rises by 14.0--48.8 percentage points under skill evolution and by 3.0--39.3 percentage points under reinforcement learning, posing safety risks. The code is available at this https URL

---


### 8. [Red-Teaming Large Language Models in Low-Resource African Languages: A Case Study of Yoruba and Nigerian Pidgin](https://arxiv.org/abs/2610.39590)

**<font color=#1a73e8>作者：</font>** Paula Chikaodinaka Anyanwu, Valdini Douglace Lemofouet, Blessing Ngozi Uzor 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become more widespread in Africa, their safety in low-resource languages remains largely untested since most red-teaming work focuses on English. This study evaluates six state-of-the-art LLMs using 400 explicit adversarial prompts in Yoruba and Nigerian Pidgin, categorised into four harm categories. The responses were scored by native-speaker annotators and reliability was assessed using Cohen's $\kappa$. While models that rejected up to 69% of English prompts rejected as few as 0% in Yoruba, this was not because they were safer, but because they failed to understand the prompts. Attack success rates increased for most models in the Nigerian languages, with GPT-4o Mini demonstrating the most significant cross-lingual safety discrepancy (+0.23 in Yoruba). When models did engage with adversarial prompts, many of the responses were harmful, with rates of harmful content reaching 0.63 in English and 0.50 in Nigerian Pidgin. The most difficult harm category to detect was cultural stereotypes and discrimination (ASR = 0.44 in Nigerian Pidgin). Comprehension in Yoruba was low across most models, and this directly suppressed apparent attack success without indicating actual safety. Gemini 2.0 Flash was the most consistent model across languages. Despite its explicit training in African languages, Aya 101 had the highest attack success rate in English (0.60) and one of the lowest Yoruba comprehension rates (0.28). These results demonstrate that English-centric safety alignment does not transfer to Nigerian languages, highlighting the urgent need for language-specific safety evaluations.

---


### 9. [SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection](https://arxiv.org/abs/2610.39758)

**<font color=#1a73e8>作者：</font>** Doohyun Kim, Donghwa Kang, Mingyu Jun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection threatens local LLM agents through untrusted tool outputs, motivating defenses that suppress attacks while preserving task evidence under limited inference budgets. We introduce SEAL, which learns a soft prompt and scoring readout offline to sanitize tool outputs using a frozen task model. SEAL constructs scoring queries from trusted initial context and the learned prompt, keeping the reference independent of inspected tool text. It scores tokens without normalization across context tokens and uses preservation regularization to encourage retention of useful evidence during localized deletion. This design requires neither defense-generated tokens nor a separate verifier model. Across AgentDojo and AgentDyn, SEAL suppresses attacks while improving task completion under attack. Specifically, on AgentDojo, SEAL reduces attack success from 34.6\% to 0.1\% and increases Joint---task completion without attack success---from 51.4\% to 77.5\%, while using approximately $127\times$ fewer defense-related tokens than PISanitizer, a state-of-the-art prompt injection defense. Replication on a second backbone with the same training recipe supports applicability across model families.

---


### 10. [TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races](https://arxiv.org/abs/2610.40613)

**<font color=#1a73e8>作者：</font>** Tom Sander, Pierre Fernandez, Itai Gat 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys, and the acceptance rate is unchanged. It also preserves output diversity and adds no measurable inference latency. Its predecessor, TextSeal, restores diversity in the Gumbel-max scheme by routing each token to one of two keys via a coin flip. This is suboptimal because the detector averages the scores from both keys without knowing which key was used. TextSeal2 instead merges two or more keys into a single virtual key and couples it to fresh noise through AutoMark's Gaussian copula. Any number of keys, including publicly shared keys, can be merged this way without diluting detection. Under speculative decoding, TextSeal2 verifies keyed drafts with one more exponential race, run on the leftovers of the draft races. By memorylessness, this race reproduces block verification, so the output follows the target model exactly. We evaluate TextSeal2 on three LLMs. At equal output token diversity, TextSeal2 detects 8 to 22 percentage points more 100-token answers than TextSeal at a false-positive rate of $10^{-3}$, and is comparable to textGrain while requiring no post-logits optimization. Under speculative decoding, it detects 18 and 22 percentage points more 200-token answers than TextSeal and textGrain, respectively, at the same acceptance rate.

---


### 11. [ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender](https://arxiv.org/abs/2610.40627)

**<font color=#1a73e8>作者：</font>** Qiyao Ma, Xiaodong Liu, Weiwei Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model's first few output tokens, and existing defenses inherit the weakness, supervising the surface form of the response without ever giving the model an explicit safety decision to learn. We take the opposite view of shallowness: if a short span determines the trajectory of an entire response, that span is the highest-leverage place to intervene, and the defender can occupy it first. We propose Assess $\to$ Decide $\to$ Respond, a framework in which the defender assesses the user's intent, commits to an explicit, parseable safety decision, and only then generates a reply conditioned on it, with the commitment trained by reinforcement learning at the payload turn. Because the decision is a token span, the reward can be a rule: a self-verified reward checks the committed label against the conversation's known nature, requiring no judge and no annotation, while the same format also supports an LLM-as-judge reward over a graded decision space with safe redirection. Across two model families and fourteen benchmarks spanning safety, utility, and helpfulness, our defenders achieve the strongest multi-turn safety in a controlled comparison, maintaining their lead in safety while preserving utility at a modest cost to helpfulness. A per-token KL analysis and interventional probes confirm why this works: training concentrates its effect on the brief deliberation that sets a response's trajectory, and the decision committed there is a causal control point. The very shallowness attackers exploit becomes the mechanism of defense.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
